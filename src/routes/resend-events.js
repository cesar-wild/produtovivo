const express = require('express');
const crypto = require('crypto');

const router = express.Router();

/**
 * POST /webhooks/resend
 * Receives and logs Resend email lifecycle events.
 * Events: email.sent, email.delivered, email.opened, email.clicked, email.bounced, email.complained
 *
 * Optionally verifies Svix webhook signature when RESEND_WEBHOOK_SECRET is set.
 * Reference: https://resend.com/docs/dashboard/webhooks/introduction
 */
router.post('/', express.json(), (req, res) => {
  const secret = process.env.RESEND_WEBHOOK_SECRET;

  if (secret) {
    // Svix signature verification
    const svixId = req.headers['svix-id'];
    const svixTimestamp = req.headers['svix-timestamp'];
    const svixSignature = req.headers['svix-signature'];

    if (!svixId || !svixTimestamp || !svixSignature) {
      return res.status(400).json({ error: 'Missing Svix headers' });
    }

    // Svix signs: "<id>.<timestamp>.<body>"
    const body = JSON.stringify(req.body);
    const toSign = `${svixId}.${svixTimestamp}.${body}`;
    const expectedSig = crypto
      .createHmac('sha256', Buffer.from(secret.replace(/^whsec_/, ''), 'base64'))
      .update(toSign)
      .digest('base64');

    // svix-signature header can contain multiple space-separated "v1,<sig>" values
    const signatures = svixSignature.split(' ').map((s) => s.replace(/^v1,/, ''));
    const valid = signatures.some((sig) => sig === expectedSig);

    if (!valid) {
      console.warn('[resend-webhook] Invalid signature');
      return res.status(401).json({ error: 'Invalid signature' });
    }
  } else {
    console.warn('[resend-webhook] RESEND_WEBHOOK_SECRET not configured — signature check skipped');
  }

  const { type, data } = req.body || {};
  const emailId = data?.email_id;
  const to = Array.isArray(data?.to) ? data.to.join(', ') : data?.to;

  console.log(`[resend-event] type=${type} email_id=${emailId} to=${to}`);

  // Log actionable events
  if (type === 'email.bounced' || type === 'email.complained') {
    console.warn(`[resend-event] Deliverability issue — type=${type} to=${to}`);
  }

  res.json({ received: true });
});

module.exports = router;
