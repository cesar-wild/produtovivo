# E-mail de Boas-Vindas — Comprador ProdutoVivo

Este template é o e-mail transacional enviado automaticamente após a compra.
Configurar via **Resend API** com trigger no webhook da Hotmart/Kiwify.

**From:** `cesar@produtovivo.com`
**Subject:** `Seu acesso ao ProdutoVivo chegou 🎯`
**Reply-to:** `contato@produtovivo.com`

---

## Template HTML (para Resend)

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Bem-vindo ao ProdutoVivo</title>
</head>
<body style="margin:0;padding:0;background:#f9fafb;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f9fafb;padding:40px 0;">
    <tr>
      <td align="center">
        <table width="560" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.06);">

          <!-- Header -->
          <tr>
            <td style="background:#1a56db;padding:28px 40px;">
              <p style="margin:0;color:#ffffff;font-size:1.3rem;font-weight:800;letter-spacing:-0.5px;">ProdutoVivo</p>
            </td>
          </tr>

          <!-- Body -->
          <tr>
            <td style="padding:40px 40px 32px;">
              <h1 style="margin:0 0 16px;font-size:1.5rem;font-weight:800;color:#111827;letter-spacing:-0.5px;">
                Seu guia chegou. Hora de começar. 🚀
              </h1>
              <p style="margin:0 0 20px;color:#374151;font-size:1rem;line-height:1.6;">
                Oi, {{first_name}}! Obrigado pela compra do <strong>ProdutoVivo</strong>.
                Você agora tem acesso ao guia completo com 50 prompts prontos para transformar
                seus PDFs em apps interativos com IA.
              </p>

              <!-- CTA Button -->
              <table cellpadding="0" cellspacing="0" style="margin:24px 0;">
                <tr>
                  <td style="background:#1a56db;border-radius:8px;">
                    <a href="{{download_link}}"
                       style="display:inline-block;padding:14px 32px;color:#ffffff;text-decoration:none;font-weight:700;font-size:1rem;">
                      Acessar o guia →
                    </a>
                  </td>
                </tr>
              </table>

              <p style="margin:0 0 24px;color:#374151;font-size:0.95rem;line-height:1.6;">
                Não sabe por onde começar? <strong>Vá direto para o Capítulo 3</strong> —
                em 1 hora você terá seu primeiro chatbot de conteúdo funcionando.
              </p>

              <!-- Quick start box -->
              <table width="100%" cellpadding="0" cellspacing="0"
                     style="background:#eff6ff;border-radius:8px;margin-bottom:24px;">
                <tr>
                  <td style="padding:20px 24px;">
                    <p style="margin:0 0 8px;font-weight:700;color:#1a56db;font-size:0.9rem;">
                      ⚡ Sequência recomendada para o primeiro resultado hoje:
                    </p>
                    <ol style="margin:0;padding-left:20px;color:#374151;font-size:0.9rem;line-height:1.8;">
                      <li>Escolha um PDF que você já tem</li>
                      <li>Extraia o texto (Capítulo 2 explica como em 5 min)</li>
                      <li>Use o <strong>Prompt C-01</strong> no ChatGPT gratuito</li>
                      <li>Faça 5 perguntas de teste</li>
                      <li>Adicione como bônus no seu produto</li>
                    </ol>
                  </td>
                </tr>
              </table>

              <p style="margin:0 0 8px;color:#374151;font-size:0.95rem;line-height:1.6;">
                Qualquer dúvida, responde este e-mail — eu mesmo leio.
              </p>
              <p style="margin:0;color:#374151;font-size:0.95rem;">
                Bom trabalho,<br/>
                <strong>Cesar</strong><br/>
                <span style="color:#6b7280;">ProdutoVivo</span>
              </p>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="padding:20px 40px;border-top:1px solid #f3f4f6;">
              <p style="margin:0;color:#9ca3af;font-size:0.8rem;line-height:1.5;">
                Você recebeu este e-mail porque comprou o guia ProdutoVivo.<br/>
                <a href="https://produtovivo.com/privacidade" style="color:#9ca3af;">Política de Privacidade</a>
                &nbsp;·&nbsp;
                <a href="https://produtovivo.com/termos" style="color:#9ca3af;">Termos de Uso</a>
              </p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>
```

---

## Variáveis de template

| Variável | Fonte | Exemplo |
|---|---|---|
| `{{first_name}}` | Webhook Hotmart/Kiwify → campo nome | `João` |
| `{{download_link}}` | Link de entrega do produto na plataforma | `https://hotmart.com/product/...` |

---

## Configuração no Resend

```javascript
// src/emails/welcome.js — integrar com webhook da Hotmart
const { Resend } = require('resend');
const resend = new Resend(process.env.RESEND_API_KEY);

async function sendWelcomeEmail({ firstName, email, downloadLink }) {
  await resend.emails.send({
    from: 'cesar@produtovivo.com',
    to: email,
    subject: 'Seu acesso ao ProdutoVivo chegou 🎯',
    replyTo: 'contato@produtovivo.com',
    html: WELCOME_TEMPLATE
      .replace('{{first_name}}', firstName)
      .replace('{{download_link}}', downloadLink),
  });
}
```

## Webhook trigger (Hotmart)

Hotmart envia um POST para `https://produtovivo.com/webhooks/hotmart` após cada compra aprovada.
Campos relevantes: `data.buyer.name`, `data.buyer.email`, `data.product.name`.

Adicionar handler no `src/server.js` que:
1. Verifica a assinatura do webhook (header `X-Hotmart-Hottok`)
2. Extrai nome e e-mail do comprador
3. Chama `sendWelcomeEmail()`
4. Registra a venda no log

---

## Notas

- **Envio imediato:** disparar no máximo 2 minutos após confirmação de pagamento
- **Não adicionar à lista de newsletter** sem consentimento explícito (LGPD)
- **Testar antes de ativar:** enviar um e-mail de teste para si mesmo via Resend dashboard
