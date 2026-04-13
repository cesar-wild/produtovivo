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

    // Add nurturing tracking columns if they don't exist yet
    await client.query(`
      ALTER TABLE orders
        ADD COLUMN IF NOT EXISTS nurturing_day1_at TIMESTAMPTZ,
        ADD COLUMN IF NOT EXISTS nurturing_day3_at TIMESTAMPTZ;
    `);
    // Leads table for quiz funnel
    await client.query(`
      CREATE TABLE IF NOT EXISTS leads (
        id              SERIAL PRIMARY KEY,
        email           TEXT UNIQUE NOT NULL,
        quiz_profile    TEXT,
        quiz_score      NUMERIC,
        source          TEXT DEFAULT 'quiz',
        welcome_sent_at TIMESTAMPTZ,
        converted_at    TIMESTAMPTZ,
        opted_out_at    TIMESTAMPTZ,
        created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
        updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
      );
      CREATE INDEX IF NOT EXISTS idx_leads_email ON leads(email);
    `);

    // Add opted_out_at to existing leads tables (safe on re-run)
    await client.query(`
      ALTER TABLE leads ADD COLUMN IF NOT EXISTS opted_out_at TIMESTAMPTZ;
    `);

    // Global unsubscribes log (covers both leads and cold email prospects)
    await client.query(`
      CREATE TABLE IF NOT EXISTS unsubscribes (
        id         SERIAL PRIMARY KEY,
        email      TEXT UNIQUE NOT NULL,
        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
      );
      CREATE INDEX IF NOT EXISTS idx_unsubscribes_email ON unsubscribes(email);
    `);

    console.log('DB migrations applied');
  } finally {
    client.release();
  }
}

module.exports = { pool, migrate };
