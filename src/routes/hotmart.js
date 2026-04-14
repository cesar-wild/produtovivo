'use strict';

const express = require('express');

const router = express.Router();

/**
 * Send a welcome email using the Resend API (raw fetch — no SDK dependency needed here).
 * Hotmart webhook calls this after a confirmed purchase.
 */
async function sendWelcomeEmail({ firstName, email, downloadLink }) {
  if (!process.env.RESEND_API_KEY) {
    console.warn('[resend] RESEND_API_KEY not set — skipping welcome email');
    return;
  }

  const html = `<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/></head>
<body style="margin:0;padding:0;background:#f9fafb;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f9fafb;padding:40px 0;">
    <tr><td align="center">
      <table width="560" cellpadding="0" cellspacing="0" style="background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.06);">
        <tr><td style="background:#1a56db;padding:28px 40px;">
          <p style="margin:0;color:#fff;font-size:1.3rem;font-weight:800;">ProdutoVivo</p>
        </td></tr>
        <tr><td style="padding:40px 40px 32px;">
          <h1 style="margin:0 0 16px;font-size:1.5rem;font-weight:800;color:#111827;">Seu guia chegou. Hora de começar. 🚀</h1>
          <p style="margin:0 0 20px;color:#374151;font-size:1rem;line-height:1.6;">
            Oi, ${firstName}! Obrigado pela compra do <strong>ProdutoVivo</strong>.
            Você agora tem acesso ao guia completo com 50 prompts prontos para transformar seus PDFs em apps interativos com IA.
          </p>
          <table cellpadding="0" cellspacing="0" style="margin:24px 0;">
            <tr><td style="background:#1a56db;border-radius:8px;">
              <a href="${downloadLink}" style="display:inline-block;padding:14px 32px;color:#fff;text-decoration:none;font-weight:700;font-size:1rem;">
                Acessar o guia →
              </a>
            </td></tr>
          </table>
          <p style="margin:0 0 24px;color:#374151;font-size:0.95rem;line-height:1.6;">
            Não sabe por onde começar? <strong>Vá direto para o Capítulo 3</strong> — em 1 hora você terá seu primeiro chatbot de conteúdo funcionando.
          </p>
          <table width="100%" cellpadding="0" cellspacing="0" style="background:#eff6ff;border-radius:8px;margin-bottom:24px;">
            <tr><td style="padding:20px 24px;">
              <p style="margin:0 0 8px;font-weight:700;color:#1a56db;font-size:0.9rem;">⚡ Sequência para o primeiro resultado hoje:</p>
              <ol style="margin:0;padding-left:20px;color:#374151;font-size:0.9rem;line-height:1.8;">
                <li>Escolha um PDF que você já tem</li>
                <li>Extraia o texto (Capítulo 2 — 5 minutos)</li>
                <li>Use o <strong>Prompt C-01</strong> no ChatGPT gratuito</li>
                <li>Faça 5 perguntas de teste</li>
                <li>Adicione como bônus no seu produto</li>
              </ol>
            </td></tr>
          </table>
          <p style="margin:0 0 8px;color:#374151;font-size:0.95rem;line-height:1.6;">Qualquer dúvida, responde este e-mail — eu mesmo leio.</p>
          <p style="margin:0;color:#374151;font-size:0.95rem;">Bom trabalho,<br/><strong>Cesar</strong><br/><span style="color:#6b7280;">ProdutoVivo</span></p>
        </td></tr>
        <tr><td style="padding:20px 40px;border-top:1px solid #f3f4f6;">
          <p style="margin:0;color:#9ca3af;font-size:0.8rem;line-height:1.5;">
            Você recebeu este e-mail porque comprou o guia ProdutoVivo.<br/>
            <a href="https://produtovivo.com/privacidade" style="color:#9ca3af;">Privacidade</a>
            &nbsp;·&nbsp;
            <a href="https://produtovivo.com/termos" style="color:#9ca3af;">Termos</a>
          </p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>`;

  const response = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${process.env.RESEND_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      from: 'cesar@produtovivo.com',
      to: email,
      subject: 'Seu acesso ao ProdutoVivo chegou 🎯',
      reply_to: 'contato@produtovivo.com',
      html,
    }),
  });

  const data = await response.json();
  if (!response.ok) {
    console.error('[resend] failed to send welcome email:', JSON.stringify(data));
  } else {
    console.log('[resend] welcome email sent to', email, 'id:', data.id);
  }
}

/**
 * Fire a server-side Meta Purchase event via the Conversions API.
 */
async function fireMetaPurchaseEvent({ email, value = 37.00, eventId }) {
  if (!process.env.META_ACCESS_TOKEN || !process.env.META_PIXEL_ID) return;

  const pixelPayload = {
    data: [{
      event_name: 'Purchase',
      event_time: Math.floor(Date.now() / 1000),
      event_id: eventId || `hotmart-${Date.now()}`,
      action_source: 'website',
      user_data: { em: [email] },
      custom_data: { value, currency: 'BRL' },
    }],
  };

  try {
    const pixelRes = await fetch(
      `https://graph.facebook.com/v19.0/${process.env.META_PIXEL_ID}/events?access_token=${process.env.META_ACCESS_TOKEN}`,
      { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(pixelPayload) }
    );
    const pixelData = await pixelRes.json();
    console.log('[meta] server-side Purchase event sent:', JSON.stringify(pixelData));
  } catch (err) {
    console.error('[meta] server-side event error:', err.message);
  }
}

/**
 * POST /webhooks/hotmart
 * Triggered on every purchase event from Hotmart.
 * Hotmart sends X-Hotmart-Hottok header for signature verification.
 * Docs: https://developers.hotmart.com/docs/en/webhook/
 */
router.post('/', async (req, res) => {
  const hottok = process.env.HOTMART_HOTTOK;
  const receivedToken = req.headers['x-hotmart-hottok'];

  if (hottok && receivedToken !== hottok) {
    console.warn('[hotmart] invalid hottok — rejecting webhook');
    return res.sendStatus(401);
  }

  const event = req.body;
  const eventType = event?.event;

  console.log('[hotmart] received event:', eventType);

  if (eventType !== 'PURCHASE_APPROVED') {
    return res.sendStatus(200);
  }

  const buyer = event?.data?.buyer || {};
  const purchase = event?.data?.purchase || {};
  const firstName = (buyer.name || '').split(' ')[0] || 'Olá';
  const email = buyer.email;
  const downloadLink = purchase.offer?.payment_engine_purchase_id
    ? `https://hotmart.com/product/download/${purchase.offer.payment_engine_purchase_id}`
    : 'https://produtovivo.com';

  if (!email) {
    console.error('[hotmart] PURCHASE_APPROVED missing buyer email — skipping');
    return res.sendStatus(200);
  }

  try {
    await sendWelcomeEmail({ firstName, email, downloadLink });
  } catch (err) {
    console.error('[hotmart] welcome email error:', err.message);
  }

  await fireMetaPurchaseEvent({
    email,
    eventId: `hotmart-${purchase.transaction || Date.now()}`,
  });

  res.sendStatus(200);
});

module.exports = router;
