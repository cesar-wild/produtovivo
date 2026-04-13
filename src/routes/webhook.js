const express = require('express');
const Stripe = require('stripe');
const crypto = require('crypto');
const { pool } = require('../db');
const { sendPurchaseEmail } = require('../email');

const router = express.Router();

// Lazy Stripe client — avoids crash on startup if key is missing
let _stripe;
function getStripe() {
  if (!_stripe) {
    if (!process.env.STRIPE_SECRET_KEY) throw new Error('STRIPE_SECRET_KEY not configured');
    _stripe = new Stripe(process.env.STRIPE_SECRET_KEY);
  }
  return _stripe;
}

const APP_URL = process.env.APP_URL || 'https://produtovivo.com';
const DOWNLOAD_SECRET = process.env.DOWNLOAD_SECRET || 'change_me';

// Stripe requires the raw body for signature verification
router.post('/stripe', express.raw({ type: 'application/json' }), async (req, res) => {
  const sig = req.headers['stripe-signature'];

  let event;
  try {
    event = getStripe().webhooks.constructEvent(req.body, sig, process.env.STRIPE_WEBHOOK_SECRET);
  } catch (err) {
    console.error('Webhook signature error:', err.message);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }

  if (event.type === 'checkout.session.completed') {
    const session = event.data.object;
    if (session.payment_status !== 'paid') return res.json({ received: true });

    const email = session.customer_details?.email;
    const name = session.customer_details?.name;
    const sessionId = session.id;

    // Generate a time-limited download token
    const token = crypto.randomBytes(32).toString('hex');
    const expiresAt = new Date(Date.now() + 48 * 60 * 60 * 1000); // 48 h

    try {
      await pool.query(
        `INSERT INTO orders (stripe_session_id, stripe_payment_intent, email, name, status, download_token, download_expires_at)
         VALUES ($1, $2, $3, $4, 'paid', $5, $6)
         ON CONFLICT (stripe_session_id) DO NOTHING`,
        [sessionId, session.payment_intent, email, name, token, expiresAt]
      );

      const downloadUrl = `${APP_URL}/download?token=${token}`;
      await sendPurchaseEmail({ to: email, name, downloadUrl });
      console.log(`Order fulfilled: ${email}`);
    } catch (err) {
      console.error('Fulfillment error:', err);
      // Return 500 so Stripe retries the webhook
      return res.status(500).json({ error: 'Fulfillment failed' });
    }
  }

  res.json({ received: true });
});

module.exports = router;
