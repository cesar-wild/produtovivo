/**
 * Cold Email Sender — ProdutoVivo
 *
 * Reads docs/prospects.csv, sends the correct sequence touch based on
 * prospect status and timing, then updates the CSV.
 *
 * Usage:
 *   node scripts/send-cold-emails.js [--dry-run] [--limit N]
 *
 * Requires:
 *   RESEND_API_KEY env var (set in .env or environment)
 *   DNS: SPF, DKIM, DMARC must be live on produtovivo.com
 *
 * Sending limits:
 *   Max 20 emails/day during domain warm-up (first 3 weeks)
 *   Send window enforced: 09:00–17:00 BRT (12:00–20:00 UTC)
 */

'use strict';

require('dotenv').config();

const fs = require('fs');
const path = require('path');
const { sendColdEmail } = require('../src/email');
const { pool } = require('../src/db');

const PROSPECTS_CSV = path.join(__dirname, '../docs/prospects.csv');
const LOG_CSV = path.join(__dirname, '../docs/email-log.csv');
const DAILY_LIMIT = parseInt(process.env.COLD_EMAIL_DAILY_LIMIT || '20', 10);

const DRY_RUN = process.argv.includes('--dry-run');
const LIMIT_ARG = process.argv.indexOf('--limit');
const MAX_THIS_RUN = LIMIT_ARG !== -1 ? parseInt(process.argv[LIMIT_ARG + 1], 10) : 999;

// Sequence delays in days
const DELAY_TOUCH2_DAYS = 3;
const DELAY_TOUCH3_DAYS = 7;

function parseCsv(text) {
  const lines = text.trim().split('\n');
  const headers = lines[0].split(',');
  return lines.slice(1).map(line => {
    const values = line.split(',');
    const obj = {};
    headers.forEach((h, i) => { obj[h.trim()] = (values[i] || '').trim(); });
    return obj;
  });
}

function serializeCsv(rows) {
  if (!rows.length) return '';
  const headers = Object.keys(rows[0]);
  const lines = [headers.join(',')];
  for (const row of rows) {
    lines.push(headers.map(h => row[h] || '').join(','));
  }
  return lines.join('\n') + '\n';
}

function daysSince(dateStr) {
  if (!dateStr) return Infinity;
  const d = new Date(dateStr);
  const now = new Date();
  return (now - d) / (1000 * 60 * 60 * 24);
}

function isSendWindowOpen() {
  // Enforce 12:00–20:00 UTC (09:00–17:00 BRT)
  const now = new Date();
  const hourUTC = now.getUTCHours();
  return hourUTC >= 12 && hourUTC < 20;
}

function appendLog(entry) {
  const line = [
    entry.timestamp,
    entry.email,
    entry.firstName,
    entry.touch,
    entry.status,
    entry.error || '',
  ].join(',') + '\n';

  if (!fs.existsSync(LOG_CSV)) {
    fs.writeFileSync(LOG_CSV, 'timestamp,email,first_name,touch,status,error\n');
  }
  fs.appendFileSync(LOG_CSV, line);
}

async function main() {
  if (!DRY_RUN && !isSendWindowOpen()) {
    console.log('Outside send window (12:00–20:00 UTC). Exiting.');
    process.exit(0);
  }

  if (!process.env.RESEND_API_KEY) {
    console.error('ERROR: RESEND_API_KEY not set. Cannot send emails.');
    if (!DRY_RUN) process.exit(1);
  }

  const csv = fs.readFileSync(PROSPECTS_CSV, 'utf8');
  const prospects = parseCsv(csv);

  let sent = 0;
  const today = new Date().toISOString().split('T')[0];

  // Count emails already sent today from log
  let sentToday = 0;
  if (fs.existsSync(LOG_CSV)) {
    const log = fs.readFileSync(LOG_CSV, 'utf8');
    sentToday = log.split('\n').filter(l => l.startsWith(today) && l.includes(',ok,')).length;
  }

  // Load global unsubscribe list from DB (if DB available)
  const unsubSet = new Set();
  if (process.env.DATABASE_URL) {
    try {
      const client = await pool.connect();
      const rows = await client.query('SELECT email FROM unsubscribes');
      rows.rows.forEach(r => unsubSet.add(r.email.toLowerCase()));
      client.release();
    } catch (_) {}
  }

  console.log(`Sent today so far: ${sentToday}/${DAILY_LIMIT} | Unsubscribes: ${unsubSet.size} | DRY_RUN: ${DRY_RUN}`);

  for (const prospect of prospects) {
    if (sent >= MAX_THIS_RUN) break;
    if (sentToday + sent >= DAILY_LIMIT) {
      console.log(`Daily limit reached (${DAILY_LIMIT}). Stopping.`);
      break;
    }

    const { first_name, email, platform, product_name, status } = prospect;
    if (!email || !first_name) continue;

    // Skip opted-out emails
    if (unsubSet.has(email.toLowerCase())) {
      console.log(`[SKIP] ${email} — unsubscribed`);
      if (prospect.status !== 'unsubscribed') {
        prospect.status = 'unsubscribed';
      }
      continue;
    }

    let touch = null;

    if (status === 'new') {
      touch = 1;
    } else if (status === 'sent-1' && daysSince(prospect.sent_1_at) >= DELAY_TOUCH2_DAYS) {
      touch = 2;
    } else if (status === 'sent-2' && daysSince(prospect.sent_2_at) >= DELAY_TOUCH3_DAYS) {
      touch = 3;
    }

    if (!touch) continue;

    console.log(`[${DRY_RUN ? 'DRY' : 'SEND'}] Touch ${touch} → ${email} (${first_name}, ${platform})`);

    if (!DRY_RUN) {
      try {
        await sendColdEmail({ to: email, firstName: first_name, productName: product_name, platform, touch });

        const now = new Date().toISOString();
        if (touch === 1) {
          prospect.sent_1_at = now;
          prospect.status = 'sent-1';
        } else if (touch === 2) {
          prospect.sent_2_at = now;
          prospect.status = 'sent-2';
        } else if (touch === 3) {
          prospect.sent_3_at = now;
          prospect.status = 'sent-3';
        }

        appendLog({ timestamp: today, email, firstName: first_name, touch, status: 'ok' });
        console.log(`  ✓ Sent`);
      } catch (err) {
        appendLog({ timestamp: today, email, firstName: first_name, touch, status: 'error', error: err.message });
        console.error(`  ✗ Error: ${err.message}`);
      }
    }

    sent++;
    // Polite delay between sends
    if (!DRY_RUN && sent < MAX_THIS_RUN) {
      await new Promise(r => setTimeout(r, 2000));
    }
  }

  if (!DRY_RUN) {
    fs.writeFileSync(PROSPECTS_CSV, serializeCsv(prospects));
    console.log(`\nDone. ${sent} emails sent. Prospects CSV updated.`);
  } else {
    console.log(`\nDry run complete. Would have sent ${sent} email(s).`);
  }
}

main()
  .catch(err => {
    console.error('Fatal:', err.message);
    process.exit(1);
  })
  .finally(() => {
    if (process.env.DATABASE_URL) pool.end().catch(() => {});
  });
