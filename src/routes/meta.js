'use strict';

const express = require('express');

const router = express.Router();

/**
 * POST /webhooks/meta-purchase
 * Manual trigger for Meta Conversions API Purchase events.
 * Useful for purchases from Kiwify or other platforms that don't have
 * a native Meta integration.
 */
router.post('/', async (req, res) => {
  const { email, value, currency = 'BRL', event_id } = req.body;

  if (!process.env.META_ACCESS_TOKEN || !process.env.META_PIXEL_ID) {
    console.warn('[meta] META_ACCESS_TOKEN or META_PIXEL_ID not set — skipping');
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
    const url = `https://graph.facebook.com/v19.0/${process.env.META_PIXEL_ID}/events?access_token=${process.env.META_ACCESS_TOKEN}`;
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

module.exports = router;
