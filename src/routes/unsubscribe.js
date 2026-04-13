const express = require('express');
const path = require('path');
const { pool } = require('../db');

const router = express.Router();

/**
 * GET /unsubscribe?email=xxx
 * Shows the unsubscribe confirmation page (served as static HTML).
 * The email is passed through as a query param so the page can pre-fill it.
 */
router.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '..', '..', 'public', 'unsubscribe.html'));
});

/**
 * POST /unsubscribe
 * Marks a lead or order email as opted out.
 * Body: { email: string }
 */
router.post('/', async (req, res) => {
  const { email } = req.body;

  if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return res.status(400).json({ error: 'E-mail inválido.' });
  }

  const clean = email.toLowerCase().trim();

  try {
    // Mark opted out in leads table
    await pool.query(
      `UPDATE leads SET opted_out_at = NOW(), updated_at = NOW()
       WHERE email = $1 AND opted_out_at IS NULL`,
      [clean]
    );

    // Also record in a dedicated unsubscribes log for cold email list
    await pool.query(
      `INSERT INTO unsubscribes (email) VALUES ($1)
       ON CONFLICT (email) DO NOTHING`,
      [clean]
    );

    console.log(`Unsubscribe: ${clean}`);
    res.json({ ok: true });
  } catch (err) {
    console.error('Unsubscribe error:', err.message);
    // Graceful degradation: still confirm to user even if DB write fails
    res.json({ ok: true });
  }
});

module.exports = router;
