const express = require('express');
const { pool } = require('../db');

const router = express.Router();

router.get('/', async (req, res) => {
  let dbOk = false;
  try {
    await pool.query('SELECT 1');
    dbOk = true;
  } catch (_) {
    // DB not connected — still respond 200 so load balancer passes
  }

  res.json({
    status: 'ok',
    service: 'produtovivo',
    db: dbOk ? 'ok' : 'unavailable',
    ts: new Date().toISOString(),
  });
});

router.get('/deploy', (req, res) => {
  res.json({
    sha: process.env.GIT_SHA || 'unknown',
    builtAt: process.env.BUILT_AT || 'unknown',
  });
});

// Returns presence of required env vars — never their values.
// Used by ops to diagnose missing config without SSH.
router.get('/env', (req, res) => {
  const required = [
    'STRIPE_SECRET_KEY',
    'STRIPE_PRICE_ID',
    'STRIPE_WEBHOOK_SECRET',
    'RESEND_API_KEY',
    'DATABASE_URL',
    'HOTMART_SECRET',
    'META_PIXEL_ID',
    'META_ACCESS_TOKEN',
  ];
  const status = Object.fromEntries(required.map((k) => [k, Boolean(process.env[k])]));
  const missing = required.filter((k) => !process.env[k]);
  res.json({ status, missing, allRequiredPresent: missing.length === 0 });
});

module.exports = router;
