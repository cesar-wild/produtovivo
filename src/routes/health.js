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

module.exports = router;
