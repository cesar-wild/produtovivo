/**
 * Buyer Nurturing Email Sender — ProdutoVivo
 *
 * Reads the orders table, finds buyers at Day 1 and Day 3 milestones
 * who haven't received the corresponding nurturing email yet, and sends it.
 *
 * Usage:
 *   node scripts/send-nurturing-emails.js [--dry-run]
 *
 * Designed to run daily via cron (e.g. 09:00 BRT / 12:00 UTC).
 * Safe to run multiple times — idempotent via DB column check.
 *
 * Requires:
 *   DATABASE_URL and RESEND_API_KEY env vars
 */

'use strict';

require('dotenv').config();

const { pool } = require('../src/db');
const { sendNurturingEmail } = require('../src/email');

const DRY_RUN = process.argv.includes('--dry-run');

async function main() {
  if (!process.env.RESEND_API_KEY) {
    console.error('ERROR: RESEND_API_KEY not set.');
    if (!DRY_RUN) process.exit(1);
  }

  const client = await pool.connect();
  let sent = 0;
  let errors = 0;

  try {
    // Day 1: bought ≥ 20 hours ago, day 1 email not yet sent
    const day1Result = await client.query(`
      SELECT id, email, name, created_at
      FROM orders
      WHERE status = 'paid'
        AND nurturing_day1_at IS NULL
        AND created_at <= NOW() - INTERVAL '20 hours'
        AND created_at >= NOW() - INTERVAL '3 days'
      ORDER BY created_at ASC
    `);

    // Day 3: bought ≥ 3 days ago, day 3 email not yet sent, day 1 was sent
    const day3Result = await client.query(`
      SELECT id, email, name, created_at
      FROM orders
      WHERE status = 'paid'
        AND nurturing_day1_at IS NOT NULL
        AND nurturing_day3_at IS NULL
        AND created_at <= NOW() - INTERVAL '3 days'
        AND created_at >= NOW() - INTERVAL '7 days'
      ORDER BY created_at ASC
    `);

    const day1Orders = day1Result.rows;
    const day3Orders = day3Result.rows;

    console.log(`Day 1 queue: ${day1Orders.length} | Day 3 queue: ${day3Orders.length} | DRY_RUN: ${DRY_RUN}`);

    for (const order of day1Orders) {
      console.log(`[${DRY_RUN ? 'DRY' : 'SEND'}] Day 1 → ${order.email} (${order.name || 'unknown'})`);
      if (!DRY_RUN) {
        try {
          await sendNurturingEmail({ to: order.email, name: order.name, day: 1 });
          await client.query(
            `UPDATE orders SET nurturing_day1_at = NOW() WHERE id = $1`,
            [order.id]
          );
          console.log(`  ✓ Sent`);
          sent++;
        } catch (err) {
          console.error(`  ✗ Error: ${err.message}`);
          errors++;
        }
        await new Promise(r => setTimeout(r, 1500));
      } else {
        sent++;
      }
    }

    for (const order of day3Orders) {
      console.log(`[${DRY_RUN ? 'DRY' : 'SEND'}] Day 3 → ${order.email} (${order.name || 'unknown'})`);
      if (!DRY_RUN) {
        try {
          await sendNurturingEmail({ to: order.email, name: order.name, day: 3 });
          await client.query(
            `UPDATE orders SET nurturing_day3_at = NOW() WHERE id = $1`,
            [order.id]
          );
          console.log(`  ✓ Sent`);
          sent++;
        } catch (err) {
          console.error(`  ✗ Error: ${err.message}`);
          errors++;
        }
        await new Promise(r => setTimeout(r, 1500));
      } else {
        sent++;
      }
    }

    console.log(`\nDone. ${sent} emails ${DRY_RUN ? 'would be ' : ''}sent. ${errors} errors.`);
  } finally {
    client.release();
    await pool.end();
  }
}

main().catch(err => {
  console.error('Fatal:', err.message);
  process.exit(1);
});
