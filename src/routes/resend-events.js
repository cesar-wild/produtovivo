'use strict';

const express = require('express');

const router = express.Router();

/**
 * POST /webhooks/resend
 * Logs open / click / bounce events from Resend for cold email tracking.
 * No complex processing needed — just ack and log.
 */
router.post('/', (req, res) => {
  const event = req.body;
  console.log('[resend webhook]', JSON.stringify(event));
  res.sendStatus(200);
});

module.exports = router;
