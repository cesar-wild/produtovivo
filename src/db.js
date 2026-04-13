const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: process.env.NODE_ENV === 'production' ? { rejectUnauthorized: false } : false,
});

/**
 * Run database migrations (idempotent — safe to call on every startup).
 */
async function migrate() {
  const client = await pool.connect();
  try {
    await client.query(`
      CREATE TABLE IF NOT EXISTS orders (
        id            SERIAL PRIMARY KEY,
        stripe_session_id TEXT UNIQUE NOT NULL,
        stripe_payment_intent TEXT,
        email         TEXT NOT NULL,
        name          TEXT,
        status        TEXT NOT NULL DEFAULT 'pending',
        download_token TEXT UNIQUE,
        download_expires_at TIMESTAMPTZ,
        created_at    TIMESTAMPTZ NOT NULL DEFAULT NOW(),
        updated_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
      );

      CREATE INDEX IF NOT EXISTS idx_orders_email ON orders(email);
      CREATE INDEX IF NOT EXISTS idx_orders_download_token ON orders(download_token);
    `);
    console.log('DB migrations applied');
  } finally {
    client.release();
  }
}

module.exports = { pool, migrate };
