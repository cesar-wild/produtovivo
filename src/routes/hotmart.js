const express = require('express');
const crypto = require('crypto');
const { pool } = require('../db');
const { sendPurchaseEmail } = require('../email');

const router = express.Router();

const APP_URL = process.env.APP_URL || 'https://produtovivo.com';
const META_PIXEL_ID = process.env.META_PIXEL_ID || '4520253334926563';

/**
 * POST /webhooks/hotmart
 * Handles Hotmart purchase events.
 * Verifies the hottok header, inserts an order, sends the welcome email,
 * and fires a server-side Meta Purchase CAPI event.
 */
router.post('/', express.json(), async (req, res) => {
  // Verify hottok — Hotmart sends it as the X-Hotmart-Hottok header
  const hottok = req.headers['x-hotmart-hottok'] || req.query.hottok;
  if (process.env.HOTMART_SECRET) {
    if (hottok !== process.env.HOTMART_SECRET) {
      console.warn('[hotmart] Invalid hottok received');
      return res.status(401).json({ error: 'Invalid hottok' });
    }
  } else {
    console.warn('[hotmart] HOTMART_SECRET not configured — skipping signature check');
  }

  const event = req.body;
  const eventType = event?.event;

  // Only process completed/approved purchases
  if (eventType !== 'PURCHASE_COMPLETE' && eventType !== 'PURCHASE_APPROVED') {
    return res.json({ received: true, skipped: true });
  }

  const buyer = event?.data?.buyer;
  const purchase = event?.data?.purchase;

  const email = buyer?.email;
  const name = buyer?.name;

  if (!email) {
    console.error('[hotmart] Missing buyer email in webhook payload');
    return res.status(400).json({ error: 'Missing buyer email' });
  }

  // Use Hotmart transaction ID as the unique idempotency key
  const transactionId = `hotmart_${purchase?.transaction || Date.now()}`;
  const token = crypto.randomBytes(32).toString('hex');
  const expiresAt = new Date(Date.now() + 48 * 60 * 60 * 1000); // 48 h

  try {
    const result = await pool.query(
      `INSERT INTO orders (stripe_session_id, email, name, status, download_token, download_expires_at)
       VALUES ($1, $2, $3, 'paid', $4, $5)
       ON CONFLICT (stripe_session_id) DO NOTHING
       RETURNING id`,
      [transactionId, email, name, token, expiresAt]
    );

    // If DO NOTHING fired, order already processed — still return 200
    if (result.rowCount === 0) {
      console.log(`[hotmart] Duplicate event — already processed: ${transactionId}`);
      return res.json({ received: true, duplicate: true });
    }

    const downloadUrl = `${APP_URL}/download?token=${token}`;
    await sendPurchaseEmail({ to: email, name, downloadUrl });
    console.log(`[hotmart] Order fulfilled: ${email}`);

    // Fire server-side Meta Purchase CAPI (best-effort — never block fulfillment)
    fireMetaPurchaseCAPI({ email, name }).catch((err) => {
      console.error('[meta-capi] Error sending Purchase event:', err.message);
    });
  } catch (err) {
    console.error('[hotmart] Fulfillment error:', err);
    return res.status(500).json({ error: 'Fulfillment failed' });
  }

  res.json({ received: true });
});

/**
 * Fire a server-side Purchase event to the Meta Conversions API.
 * Requires META_ACCESS_TOKEN env var. Soft-fails if not configured.
 */
async function fireMetaPurchaseCAPI({ email, name, value = 37.00 }) {
  const accessToken = process.env.META_ACCESS_TOKEN;
  if (!accessToken) {
    console.warn('[meta-capi] META_ACCESS_TOKEN not configured — skipping CAPI call');
    return;
  }

  const hashedEmail = crypto
    .createHash('sha256')
    .update(email.toLowerCase().trim())
    .digest('hex');

  const payload = {
    data: [
      {
        event_name: 'Purchase',
        event_time: Math.floor(Date.now() / 1000),
        action_source: 'website',
        user_data: {
          em: [hashedEmail],
        },
        custom_data: {
          value,
          currency: 'BRL',
          content_name: 'Guia ProdutoVivo',
        },
      },
    ],
  };

  const resp = await fetch(
    `https://graph.facebook.com/v19.0/${META_PIXEL_ID}/events?access_token=${accessToken}`,
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    }
  );

  const result = await resp.json();
  if (result.error) {
    throw new Error(JSON.stringify(result.error));
  }
  console.log(`[meta-capi] Purchase event sent — events_received: ${result.events_received}`);
}

module.exports = router;
module.exports.fireMetaPurchaseCAPI = fireMetaPurchaseCAPI;
