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

/**
 * Send a buyer nurturing email (Day 1 quick-start tip or Day 3 results check-in).
 * @param {object} opts
 * @param {string} opts.to - buyer email
 * @param {string} opts.name - buyer full name
 * @param {1|3} opts.day - day number in the sequence
 */
async function sendNurturingEmail({ to, name, day }) {
  const firstName = name ? name.split(' ')[0] : 'Criador';

  const configs = {
    1: {
      subject: `${firstName}, já tentou o Prompt C-01?`,
      preheader: 'Dica rápida para seu primeiro resultado hoje.',
      headline: 'Dica rápida para começar hoje',
      body: `
        <p style="margin:0 0 16px;color:#374151;font-size:15px;line-height:1.7;">
          Oi ${firstName}, tudo bem?
        </p>
        <p style="margin:0 0 16px;color:#374151;font-size:15px;line-height:1.7;">
          Ontem você baixou o Guia ProdutoVivo. Queria compartilhar a forma mais rápida de ver resultado:
        </p>
        <div style="background:#eff6ff;border-left:4px solid #2563eb;border-radius:6px;padding:16px 20px;margin:0 0 20px;">
          <p style="margin:0 0 8px;font-weight:700;color:#1e40af;font-size:14px;">⚡ Sequência de 30 minutos:</p>
          <ol style="margin:0;padding-left:20px;color:#374151;font-size:14px;line-height:1.9;">
            <li>Abra qualquer PDF que você já tem (não precisa ser o melhor)</li>
            <li>Copie 2–3 páginas de texto</li>
            <li>Cole no ChatGPT gratuito junto com o <strong>Prompt C-01</strong> (Capítulo 4)</li>
            <li>Faça 5 perguntas sobre o conteúdo</li>
          </ol>
        </div>
        <p style="margin:0 0 16px;color:#374151;font-size:15px;line-height:1.7;">
          Isso já é o suficiente para mostrar para um cliente o que seu produto pode fazer.
        </p>
        <p style="margin:0;color:#374151;font-size:15px;line-height:1.7;">
          Qualquer dúvida, responde aqui.<br><br>
          Cesar
        </p>
      `,
    },
    3: {
      subject: `Como está indo, ${firstName}?`,
      preheader: 'Resultado em 3 dias — e um pedido rápido.',
      headline: 'Como está indo com o guia?',
      body: `
        <p style="margin:0 0 16px;color:#374151;font-size:15px;line-height:1.7;">
          Oi ${firstName},
        </p>
        <p style="margin:0 0 16px;color:#374151;font-size:15px;line-height:1.7;">
          Já faz 3 dias desde que você baixou o ProdutoVivo. Queria saber como está indo.
        </p>
        <p style="margin:0 0 16px;color:#374151;font-size:15px;line-height:1.7;">
          Você já testou algum prompt? Transformou algum PDF?
        </p>
        <p style="margin:0 16px;color:#374151;font-size:15px;line-height:1.7;">
          Se sim — ótimo! Se não, me conta o que travou. Responde este e-mail com uma linha e eu ajudo pessoalmente.
        </p>
        <div style="background:#f0fdf4;border-left:4px solid #22c55e;border-radius:6px;padding:16px 20px;margin:20px 0;">
          <p style="margin:0;color:#166534;font-size:14px;line-height:1.6;">
            <strong>Um pedido rápido:</strong> se o guia te ajudou de alguma forma, você pode me ajudar com uma resposta aqui descrevendo sua experiência? Isso faz muita diferença para criadores que ainda estão avaliando.
          </p>
        </div>
        <p style="margin:0;color:#374151;font-size:15px;line-height:1.7;">
          Obrigado,<br>
          Cesar
        </p>
      `,
    },
  };

  const config = configs[day];
  if (!config) throw new Error(`Invalid nurturing day: ${day}`);

  const html = `
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${config.subject}</title>
</head>
<body style="margin:0;padding:0;background:#f9fafb;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
  <div style="max-width:560px;margin:40px auto;background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.06);">
    <div style="background:#0f172a;padding:24px 36px;">
      <span style="color:#fff;font-size:18px;font-weight:800;">ProdutoVivo</span>
    </div>
    <div style="padding:36px;">
      <h2 style="margin:0 0 20px;font-size:20px;font-weight:700;color:#0f172a;">${config.headline}</h2>
      ${config.body}
    </div>
    <div style="padding:16px 36px;border-top:1px solid #f1f5f9;text-align:center;">
      <p style="margin:0;color:#9ca3af;font-size:12px;">
        ProdutoVivo ·
        <a href="https://produtovivo.com/privacidade" style="color:#9ca3af;">Privacidade</a> ·
        <a href="https://produtovivo.com/unsubscribe?email=${encodeURIComponent(to)}" style="color:#9ca3af;">Cancelar inscrição</a>
      </p>
    </div>
  </div>
</body>
</html>
  `;

  const { error } = await getResend().emails.send({
    from: FROM,
    to,
    replyTo: SUPPORT,
    subject: config.subject,
    html,
  });

  if (error) throw new Error(`Resend nurturing email error: ${JSON.stringify(error)}`);
}

/**
 * Send a cold outreach email (sequence touch 1, 2, or 3).
 * @param {object} opts
 * @param {string} opts.to - recipient email
 * @param {string} opts.firstName - recipient first name
 * @param {string} opts.productName - their product name
 * @param {string} opts.platform - Hotmart or Kiwify
 * @param {1|2|3} opts.touch - which email in the sequence
 */
async function sendColdEmail({ to, firstName, productName, platform, touch }) {
  const COLD_FROM = process.env.COLD_FROM_EMAIL || 'cesar@produtovivo.com';

  const subjects = {
    1: `${firstName}, vi seu produto no ${platform}`,
    2: `Resultado real: PDF virou app em 40 minutos`,
    3: `Última mensagem sobre o ProdutoVivo`,
  };

  const bodies = {
    1: `
<p>Oi ${firstName},</p>
<p>Vi que você tem <strong>${productName}</strong> no ${platform} — parabéns pelo lançamento.</p>
<p>Tenho um guia que mostra como transformar PDFs como o seu num app interativo com IA, em menos de uma tarde.</p>
<p>Tem funcionado bem pra infoprodutores no Hotmart. Quer que eu te mande o link? R$37 só essa semana.</p>
<p>Abraço,<br>Cesar<br><a href="https://produtovivo.com">produtovivo.com</a></p>
    `,
    2: `
<p>Oi ${firstName},</p>
<p>Te mandei um e-mail outro dia sobre o ProdutoVivo.</p>
<p>Queria compartilhar um exemplo concreto: um produtor pegou um PDF de 30 páginas e, usando os prompts do guia, criou um app com quiz, glossário e resumos gerados por IA — tudo sem código.</p>
<p>Se você tem PDFs parados ou cursos que precisam de atualização, isso pode ser exatamente o que você está buscando.</p>
<p>Link: <a href="https://produtovivo.com">produtovivo.com</a><br>Preço: R$37</p>
<p>Qualquer dúvida, responde aqui.</p>
<p>Cesar</p>
    `,
    3: `
<p>Oi ${firstName},</p>
<p>Última vez que te escrevo sobre isso — promessa.</p>
<p>Se o timing não foi bom, sem problema. Mas se você ainda pensa em modernizar seus materiais com IA, o guia está em <a href="https://produtovivo.com">produtovivo.com</a> por R$37.</p>
<p>Boa sorte com <strong>${productName}</strong>!</p>
<p>Cesar</p>
    `,
  };

  const html = `
<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body style="margin:0;padding:0;background:#ffffff;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
  <div style="max-width:540px;margin:40px auto;padding:0 20px;">
    <div style="font-size:15px;color:#1a1a1a;line-height:1.7;">
      ${bodies[touch]}
    </div>
    <hr style="border:none;border-top:1px solid #eee;margin:32px 0 16px;">
    <p style="margin:0;color:#999;font-size:12px;">
      ProdutoVivo · <a href="https://produtovivo.com" style="color:#999;">produtovivo.com</a>
      · <a href="https://produtovivo.com/unsubscribe?email=${encodeURIComponent(to)}" style="color:#999;">cancelar inscrição</a>
    </p>
  </div>
</body>
</html>
  `;

  const { error } = await getResend().emails.send({
    from: COLD_FROM,
    to,
    replyTo: COLD_FROM,
    subject: subjects[touch],
    html,
  });

  if (error) throw new Error(`Resend cold email error: ${JSON.stringify(error)}`);
}

module.exports = { sendPurchaseEmail, sendNurturingEmail, sendColdEmail };
