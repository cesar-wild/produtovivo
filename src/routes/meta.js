const express = require('express');
const { fireMetaPurchaseCAPI } = require('./hotmart');

const router = express.Router();

/**
 * POST /webhooks/meta-purchase
 * Manual CAPI trigger — call this from Kiwify or any platform that isn't Hotmart.
 *
 * Body (JSON):
 *   { "email": "buyer@example.com", "name": "Full Name", "value": 37.00, "secret": "..." }
 *
 * Requires MANUAL_WEBHOOK_SECRET env var to prevent unauthorized calls.
 * If not configured, the endpoint is disabled (503).
 */
router.post('/', express.json(), async (req, res) => {
  const secret = process.env.MANUAL_WEBHOOK_SECRET;
  if (!secret) {
    console.warn('[meta-purchase] MANUAL_WEBHOOK_SECRET not configured — endpoint disabled');
    return res.status(503).json({ error: 'Endpoint not configured' });
  }

  const { email, name, value = 37.00, secret: providedSecret } = req.body || {};

  if (providedSecret !== secret) {
    return res.status(401).json({ error: 'Invalid secret' });
  }

  if (!email || typeof email !== 'string') {
    return res.status(400).json({ error: 'email is required' });
  }

  try {
    await fireMetaPurchaseCAPI({ email, name: name || '', value: Number(value) || 37.00 });
    res.json({ sent: true });
  } catch (err) {
    console.error('[meta-purchase] CAPI error:', err.message);
    res.status(500).json({ error: 'CAPI call failed', detail: err.message });
  }
});

module.exports = router;
