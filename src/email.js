const { Resend } = require('resend');

// Lazy client — instantiated only when RESEND_API_KEY is set
let _resend;
function getResend() {
  if (!_resend) {
    if (!process.env.RESEND_API_KEY) throw new Error('RESEND_API_KEY not configured');
    _resend = new Resend(process.env.RESEND_API_KEY);
  }
  return _resend;
}

const FROM = process.env.FROM_EMAIL || 'noreply@produtovivo.com';
const SUPPORT = process.env.SUPPORT_EMAIL || 'suporte@produtovivo.com';

/**
 * Send purchase confirmation with download link.
 */
async function sendPurchaseEmail({ to, name, downloadUrl }) {
  const firstName = name ? name.split(' ')[0] : 'Criador';

  const { error } = await getResend().emails.send({
    from: FROM,
    to,
    replyTo: SUPPORT,
    subject: 'Seu Guia ProdutoVivo está pronto! 🎉',
    html: `
<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body style="margin:0;padding:0;background:#f8f9fa;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
  <div style="max-width:560px;margin:40px auto;background:#ffffff;border-radius:8px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.08);">
    <div style="background:#0f172a;padding:32px 40px;">
      <h1 style="margin:0;color:#ffffff;font-size:24px;font-weight:700;">ProdutoVivo</h1>
      <p style="margin:4px 0 0;color:#94a3b8;font-size:14px;">Guia Premium para Criadores</p>
    </div>
    <div style="padding:40px;">
      <h2 style="margin:0 0 16px;color:#0f172a;font-size:20px;">Obrigado, ${firstName}! 🙌</h2>
      <p style="margin:0 0 24px;color:#475569;line-height:1.6;">
        Seu acesso ao <strong>Guia ProdutoVivo</strong> foi confirmado. Transforme seus PDFs em apps interativos com IA — e venda como um criador profissional.
      </p>
      <a href="${downloadUrl}" style="display:inline-block;background:#2563eb;color:#ffffff;text-decoration:none;padding:14px 28px;border-radius:6px;font-weight:600;font-size:16px;">
        Baixar meu Guia →
      </a>
      <p style="margin:24px 0 0;color:#94a3b8;font-size:13px;">
        Link válido por 48 horas. Em caso de dúvidas, responda este e-mail.
      </p>
    </div>
    <div style="padding:20px 40px;border-top:1px solid #f1f5f9;text-align:center;">
      <p style="margin:0;color:#cbd5e1;font-size:12px;">
        © 2026 ProdutoVivo · <a href="https://produtovivo.com" style="color:#94a3b8;">produtovivo.com</a>
      </p>
    </div>
  </div>
</body>
</html>
    `,
  });

  if (error) throw new Error(`Resend error: ${JSON.stringify(error)}`);
}

module.exports = { sendPurchaseEmail };
