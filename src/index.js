require('dotenv').config();
const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const path = require('path');
const rateLimit = require('express-rate-limit');
const { migrate } = require('./db');

const healthRouter = require('./routes/health');
const checkoutRouter = require('./routes/checkout');
const webhookRouter = require('./routes/webhook');
const downloadRouter = require('./routes/download');

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

// SPA fallback — serve index.html for any unmatched route
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'public', 'index.html'));
});

// Global error handler
app.use((err, req, res, _next) => {
  console.error('Unhandled error:', err);
  res.status(500).json({ error: 'Internal server error' });
});

function checkEnv() {
  const required = ['STRIPE_SECRET_KEY', 'STRIPE_PRICE_ID', 'STRIPE_WEBHOOK_SECRET'];
  const missing = required.filter((k) => !process.env[k]);
  if (missing.length) {
    console.warn(`[config] Missing env vars — checkout/webhook will fail: ${missing.join(', ')}`);
  }
}

async function start() {
  checkEnv();

  // Run DB migrations (no-op if DB not configured)
  try {
    await migrate();
  } catch (err) {
    console.warn('DB migration skipped (no DB configured):', err.message);
  }

  app.listen(PORT, () => {
    console.log(`ProdutoVivo running on port ${PORT}`);
  });
}

start();

module.exports = app;
