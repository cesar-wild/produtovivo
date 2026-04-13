const express = require('express');
const path = require('path');
const fs = require('fs');
const { pool } = require('../db');

const router = express.Router();

const PRODUCT_DIR = path.join(__dirname, '..', '..', 'product');
const GUIDE_FILE = 'guia-produtovivo-v1.pdf';

/**
 * GET /download?token=xxx
 * Validates the purchase token and streams the guide file.
 */
router.get('/', async (req, res) => {
  const { token } = req.query;
  if (!token) return res.status(400).send('Token de download inválido.');

  let order;
  try {
    const result = await pool.query(
      `SELECT * FROM orders WHERE download_token = $1 AND status = 'paid'`,
      [token]
    );
    order = result.rows[0];
  } catch (err) {
    console.error('Download DB error:', err);
    return res.status(500).send('Erro interno.');
  }

  if (!order) {
    return res.status(404).send('Link inválido ou expirado.');
  }

  if (new Date(order.download_expires_at) < new Date()) {
    return res.status(410).send('Este link expirou. Envie um e-mail para suporte@produtovivo.com para obter um novo link.');
  }

  const filePath = path.join(PRODUCT_DIR, GUIDE_FILE);
  if (!fs.existsSync(filePath)) {
    console.error('Guide file not found:', filePath);
    return res.status(503).send('Arquivo temporariamente indisponível. Contate suporte@produtovivo.com');
  }

  res.download(filePath, 'Guia-ProdutoVivo.pdf', (err) => {
    if (err) console.error('Download stream error:', err);
  });
});

module.exports = router;
