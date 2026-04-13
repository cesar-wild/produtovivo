'use strict';

const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 8082;

// ── Middleware ──────────────────────────────────────────────────────────────

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Security headers
app.use((req, res, next) => {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'SAMEORIGIN');
  res.setHeader('Referrer-Policy', 'strict-origin-when-cross-origin');
  next();
});

// ── Static files ────────────────────────────────────────────────────────────

app.use(express.static(path.join(__dirname, '..', 'public'), {
  maxAge: '1d',
  etag: true,
}));

// ── Health check ────────────────────────────────────────────────────────────

app.get('/health', (req, res) => {
  res.json({ status: 'ok', ts: new Date().toISOString() });
});

// ── Webhook: Resend email events ────────────────────────────────────────────
// Logs open/click/bounce events for cold email tracking.
// TODO: verify Resend webhook signature before processing in production.

app.post('/webhooks/resend', (req, res) => {
  const event = req.body;
  console.log('[resend webhook]', JSON.stringify(event));
  // TODO: persist to DB — log to /docs/email-log.csv for now
  res.sendStatus(200);
});

// ── Webhook: Meta Pixel server-side events ──────────────────────────────────
// Forwards purchase events to Meta Conversions API.
// Requires: META_ACCESS_TOKEN and META_PIXEL_ID env vars.

app.post('/webhooks/meta-purchase', async (req, res) => {
  const { email, value, currency = 'BRL', event_id } = req.body;

  if (!process.env.META_ACCESS_TOKEN || !process.env.META_PIXEL_ID) {
    console.warn('[meta] META_ACCESS_TOKEN or META_PIXEL_ID not set — skipping server-side event');
    return res.sendStatus(200);
  }

  const payload = {
    data: [{
      event_name: 'Purchase',
      event_time: Math.floor(Date.now() / 1000),
      event_id: event_id || `purchase-${Date.now()}`,
      action_source: 'website',
      user_data: { em: email ? [email] : [] },
      custom_data: { value: value || 37.00, currency },
    }],
  };

  try {
    const url = `https://graph.facebook.com/v19.0/${process.env.META_PIXEL_ID}/events?access_token=${process.env.META_PIXEL_ID}`;
    const response = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    const data = await response.json();
    console.log('[meta] conversions api response:', JSON.stringify(data));
    res.sendStatus(200);
  } catch (err) {
    console.error('[meta] conversions api error:', err.message);
    res.sendStatus(500);
  }
});

// ── Catch-all → serve index.html (SPA / landing page) ──────────────────────

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'public', 'index.html'));
});

// ── Start ───────────────────────────────────────────────────────────────────

app.listen(PORT, () => {
  console.log(`ProdutoVivo server running on :${PORT}`);
});

module.exports = app;
