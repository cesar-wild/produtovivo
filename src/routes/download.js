const express = require('express');
const path = require('path');
const fs = require('fs');
const { pool } = require('../db');

const router = express.Router();

const PRODUCT_DIR = path.join(__dirname, '..', '..', 'product');

// Prefer PDF; fall back to HTML if PDF not yet generated.
const CANDIDATES = [
  { file: 'guia-produtovivo-v1.pdf', downloadName: 'Guia-ProdutoVivo.pdf' },
  { file: 'guia-produtovivo-v1.html', downloadName: 'Guia-ProdutoVivo.html' },
];

/**
 * GET /download?token=xxx
 * Validates the purchase token and streams the guide file.
 * Serves PDF if available; falls back to HTML.
 */
router.get('/', async (req, res) => {
  const { token } = req.query;
  if (!token) return res.status(400).send('Token de download inválido.');

  let order;
  try {
    // Atomically increment download_count and return the updated row.
    // The WHERE clause enforces token validity, paid status, expiry, and 5-download cap.
    const result = await pool.query(
      `UPDATE orders
       SET download_count = download_count + 1, updated_at = NOW()
       WHERE download_token = $1
         AND status = 'paid'
         AND download_expires_at > NOW()
         AND download_count < 5
       RETURNING *`,
      [token]
    );
    order = result.rows[0];
  } catch (err) {
    console.error('Download DB error:', err);
    return res.status(500).send('Erro interno.');
  }

  if (!order) {
    // Distinguish between invalid token, expired, and limit reached for better UX.
    try {
      const check = await pool.query(
        `SELECT status, download_expires_at, download_count FROM orders WHERE download_token = $1`,
        [token]
      );
      const row = check.rows[0];
      if (!row || row.status !== 'paid') {
        return res.status(404).send('Link inválido ou expirado.');
      }
      if (new Date(row.download_expires_at) < new Date()) {
        return res.status(410).send('Este link expirou. Envie um e-mail para suporte@produtovivo.com para obter um novo link.');
      }
      if (row.download_count >= 5) {
        return res.status(410).send('Limite de downloads atingido. Envie um e-mail para suporte@produtovivo.com para obter um novo link.');
      }
    } catch (_) {
      // ignore secondary check error
    }
    return res.status(404).send('Link inválido ou expirado.');
  }

  const candidate = CANDIDATES.find(c => fs.existsSync(path.join(PRODUCT_DIR, c.file)));
  if (!candidate) {
    console.error('Guide file not found in product dir:', PRODUCT_DIR);
    return res.status(503).send('Arquivo temporariamente indisponível. Contate suporte@produtovivo.com');
  }

  const filePath = path.join(PRODUCT_DIR, candidate.file);
  res.download(filePath, candidate.downloadName, (err) => {
    if (err) console.error('Download stream error:', err);
  });
});

module.exports = router;
