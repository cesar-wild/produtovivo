const express = require('express');
const { pool } = require('../db');
const { sendLeadWelcomeEmail } = require('../email');

const router = express.Router();

/**
 * POST /leads
 * Captures a quiz lead: email + quiz result profile.
 * Idempotent — updates existing row if email already exists.
 */
router.post('/', async (req, res) => {
  const { email, profile, score } = req.body;

  if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return res.status(400).json({ error: 'E-mail inválido.' });
  }

  const profiles = ['iniciante', 'intermediario', 'avancado'];
  const safeProfile = profiles.includes(profile) ? profile : 'iniciante';
  const safeScore = typeof score === 'number' ? Math.min(Math.max(score, 0), 10) : null;

  try {
    // Upsert: if email seen before, update profile and reset welcome sent flag
    const result = await pool.query(
      `INSERT INTO leads (email, quiz_profile, quiz_score, source)
       VALUES ($1, $2, $3, 'quiz')
       ON CONFLICT (email) DO UPDATE
         SET quiz_profile = EXCLUDED.quiz_profile,
             quiz_score = EXCLUDED.quiz_score,
             updated_at = NOW()
       RETURNING id, welcome_sent_at`,
      [email.toLowerCase().trim(), safeProfile, safeScore]
    );

    const lead = result.rows[0];

    // Send welcome email only once per lead (non-blocking — don't fail request if email fails)
    if (!lead.welcome_sent_at) {
      sendLeadWelcomeEmail({ to: email, profile: safeProfile }).catch(err => {
        console.error('Lead welcome email error:', err.message);
      });

      pool.query(
        `UPDATE leads SET welcome_sent_at = NOW() WHERE id = $1`,
        [lead.id]
      ).catch(() => {});
    }

    res.json({ ok: true, profile: safeProfile });
  } catch (err) {
    console.error('Lead capture error:', err.message);
    // Graceful degradation: still return success so the quiz result shows
    res.json({ ok: true, profile: safeProfile });
  }
});

module.exports = router;
