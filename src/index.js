require('dotenv').config();
const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const path = require('path');
const rateLimit = require('express-rate-limit');
const { pool, migrate } = require('./db');
const { sendNurturingEmail } = require('./email');

const healthRouter = require('./routes/health');
const checkoutRouter = require('./routes/checkout');
const webhookRouter = require('./routes/webhook');
const downloadRouter = require('./routes/download');
const leadsRouter = require('./routes/leads');
const unsubscribeRouter = require('./routes/unsubscribe');

const app = express();
const PORT = process.env.PORT || 8082;

// Trust proxy (for rate limiting behind nginx)
app.set('trust proxy', 1);

// Security headers
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'", "'unsafe-inline'", "https://js.stripe.com", "https://connect.facebook.net"],
      styleSrc: ["'self'", "'unsafe-inline'", "https://fonts.googleapis.com"],
      fontSrc: ["'self'", "https://fonts.gstatic.com"],
      imgSrc: ["'self'", "data:", "https:"],
      connectSrc: ["'self'", "https://api.stripe.com"],
      frameSrc: ["https://js.stripe.com"],
    },
  },
}));

// CORS
app.use(cors({
  origin: [
    'https://produtovivo.com',
    'https://www.produtovivo.com',
    ...(process.env.NODE_ENV !== 'production' ? ['http://localhost:8082'] : []),
  ],
}));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100,
  standardHeaders: true,
  legacyHeaders: false,
});
app.use('/api', limiter);

// Stripe webhook needs raw body — mount BEFORE express.json()
app.use('/webhook', webhookRouter);

// JSON body parser
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Static files (landing page, blog, assets)
app.use(express.static(path.join(__dirname, '..', 'public')));

// Routes
app.use('/health', healthRouter);
app.use('/checkout', checkoutRouter);
app.use('/download', downloadRouter);
app.use('/leads', leadsRouter);
app.use('/unsubscribe', unsubscribeRouter);

// SPA fallback — serve index.html for any unmatched route
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'public', 'index.html'));
});

// Global error handler
app.use((err, req, res, _next) => {
  console.error('Unhandled error:', err);
  res.status(500).json({ error: 'Internal server error' });
});

/**
 * Background job: send nurturing emails to buyers at Day 1 and Day 3.
 * Runs every hour. No-ops gracefully if DB or Resend is not configured.
 */
async function runNurturingJob() {
  if (!process.env.RESEND_API_KEY || !process.env.DATABASE_URL) return;
  try {
    // Day 1: bought 23–49 hours ago, day1 email not sent yet
    const day1Rows = await pool.query(`
      SELECT id, email, name FROM orders
      WHERE status = 'paid'
        AND nurturing_day1_at IS NULL
        AND created_at < NOW() - INTERVAL '23 hours'
        AND created_at > NOW() - INTERVAL '49 hours'
    `);
    for (const row of day1Rows.rows) {
      try {
        await sendNurturingEmail({ to: row.email, name: row.name, day: 1 });
        await pool.query(`UPDATE orders SET nurturing_day1_at = NOW() WHERE id = $1`, [row.id]);
        console.log(`Nurturing Day 1 sent: ${row.email}`);
      } catch (err) {
        console.error(`Nurturing Day 1 error (${row.email}):`, err.message);
      }
    }

    // Day 3: bought 71–97 hours ago, day3 email not sent yet
    const day3Rows = await pool.query(`
      SELECT id, email, name FROM orders
      WHERE status = 'paid'
        AND nurturing_day3_at IS NULL
        AND created_at < NOW() - INTERVAL '71 hours'
        AND created_at > NOW() - INTERVAL '97 hours'
    `);
    for (const row of day3Rows.rows) {
      try {
        await sendNurturingEmail({ to: row.email, name: row.name, day: 3 });
        await pool.query(`UPDATE orders SET nurturing_day3_at = NOW() WHERE id = $1`, [row.id]);
        console.log(`Nurturing Day 3 sent: ${row.email}`);
      } catch (err) {
        console.error(`Nurturing Day 3 error (${row.email}):`, err.message);
      }
    }
  } catch (err) {
    console.error('Nurturing job error:', err.message);
  }
}

async function start() {
  // Run DB migrations (no-op if DB not configured)
  try {
    await migrate();
  } catch (err) {
    console.warn('DB migration skipped (no DB configured):', err.message);
  }

  // Start nurturing email background job (every hour)
  setInterval(runNurturingJob, 60 * 60 * 1000);
  // Also run shortly after startup (5 min delay to let server warm up)
  setTimeout(runNurturingJob, 5 * 60 * 1000);

  app.listen(PORT, () => {
    console.log(`ProdutoVivo running on port ${PORT}`);
  });
}

start();

module.exports = app;
