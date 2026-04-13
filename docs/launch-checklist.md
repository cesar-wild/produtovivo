# ProdutoVivo — Checklist de Lançamento

**Status:** Aguardando ações humanas para ativar os canais de aquisição.

---

## ✅ Concluído (nenhuma ação necessária)

### Site / Landing Page
- [x] Homepage com hero, proof bar, preview de prompts, for/not-for, autor, garantia
- [x] Barra de navegação sticky (Blog, Quiz, Recursos, Comprar)
- [x] Seção de prévia com 3 prompts reais do guia
- [x] Purchase card com garantia visual de 7 dias
- [x] Product JSON-LD (rich snippets no Google)
- [x] FAQ JSON-LD (rich snippets)

### Blog (11 artigos publicados)
- [x] Como transformar PDF em app interativo com IA
- [x] 5 Ferramentas de IA para Infoprodutores
- [x] Como criar quiz para infoproduto com IA
- [x] Como vender infoproduto no Hotmart
- [x] 15 Prompts ChatGPT para infoprodutores
- [x] Como criar ebook com IA
- [x] Como precificar infoproduto
- [x] Como criar chatbot para infoproduto
- [x] Funil de vendas para infoproduto (HowTo + Article + FAQPage JSON-LD)
- [x] Landing page para infoproduto (HowTo + Article + FAQPage JSON-LD)
- [x] Email marketing para infoproduto (Article + FAQPage JSON-LD)
- [x] Todos os 11 artigos: nav sticky, sidebar quiz/guia, WA share button
- [x] /recursos hub page com todos os 11 artigos (CollectionPage JSON-LD)

### Funil / Lead Capture
- [x] Quiz de diagnóstico (6 perguntas, 3 perfis, email gate)
- [x] Integração quiz → /leads (salva no DB)
- [x] E-mail de boas-vindas segmentado (3 versões por perfil)
- [x] Botão de compartilhamento no WhatsApp nos resultados

### E-mails
- [x] E-mail de boas-vindas pós-compra (com link de download)
- [x] Nurturing Dia 1 ("Você já tentou o Prompt C-01?")
- [x] Nurturing Dia 3 ("Como está indo?")
- [x] Sequência cold email 3 toques (touch 1/2/3)
- [x] Scripts: `send-cold-emails.js`, `send-nurturing-emails.js`

### LGPD / Compliance
- [x] Página de cancelamento (/unsubscribe)
- [x] Rota de opt-out (POST /unsubscribe → banco de dados)
- [x] Tabela `unsubscribes` no DB
- [x] Guards em todos os scripts de envio

### Pós-venda
- [x] Página /sucesso com verificação de pagamento via Stripe
- [x] Meta Pixel Purchase event (só dispara após verificação server-side)

### Conversão / UX
- [x] Countdown timer na homepage (R$37 → R$97 até 2026-05-15)
- [x] Botão WhatsApp share no resultado do quiz
- [x] Botão WhatsApp share em todos os 11 artigos
- [x] Nav sticky com CTA "Comprar — R$37" em todas as páginas
- [x] /afiliados page (40% comissão, materiais prontos, FAQ)

### E-mail — Automação backend
- [x] Scheduler de nurturing (Day 1 + Day 3) em src/index.js
- [x] Roda a cada hora, no-op se Resend não configurado

### SEO
- [x] Sitemap.xml com 20+ URLs
- [x] robots.txt configurado
- [x] JSON-LD em todos os artigos (Article, HowTo, FAQPage, ItemList)
- [x] /recursos hub page com todos os artigos

### Ads / Social
- [x] Meta Pixel instalado em todas as páginas (PageView, Lead, InitiateCheckout, Purchase)
- [x] docs/meta-ads-copy.md — 4 conjuntos de anúncios prontos
- [x] docs/social-media-copy.md — Reels, Stories, Twitter, LinkedIn, WhatsApp

### Documentação operacional
- [x] docs/cold-email-templates.md — 3-touch sequence + quiz nurture
- [x] docs/meta-ads-copy.md — ad sets, criativos, pixel events, audiences
- [x] docs/social-media-copy.md — calendário + copy completo por plataforma
- [x] docs/launch-checklist.md — este documento

---

## 🔴 Bloqueadores — Ações Humanas Necessárias

### 1. DNS — SPF, DKIM, DMARC (PRIORIDADE MÁXIMA)

Sem isso, **zero emails chegam**. Todas as funcionalidades de email (boas-vindas, nurturing, cold outreach) estão bloqueadas.

**O que fazer:**
1. Acesse Resend.com → Domains → Add Domain → produtovivo.com
2. Resend vai gerar 3 registros DNS (SPF, DKIM, DMARC)
3. No painel DNS do seu registrador (Cloudflare, GoDaddy, etc.), adicione os 3 registros
4. Aguarde propagação (5-30 minutos no Cloudflare, até 48h em outros)
5. Confirme a verificação no Resend
6. Adicione `RESEND_API_KEY=re_...` ao .env de produção

**Resultado:** Todos os emails começam a funcionar imediatamente.

---

### 2. Hotmart ou Kiwify — Link de Pagamento (PRIORIDADE ALTA)

Sem isso, compradores chegam à página e **não conseguem pagar**.

**Opção A — Hotmart (recomendado):**
1. Acesse hotmart.com → Produtos → Criar produto
2. Tipo: Produto digital → Ebook / Material complementar
3. Upload do PDF do guia (7 capítulos)
4. Configure preço: R$37 (ou R$37 lançamento → R$47 depois)
5. Ative afiliados com 40% de comissão
6. Copie o link de pagamento
7. Cole no `.env`: `HOTMART_CHECKOUT_URL=https://pay.hotmart.com/...`
8. **Ou:** substitua o botão de compra em `public/index.html` (linha ~375) para apontar diretamente ao link do Hotmart

**Opção B — Stripe (já configurado no código):**
1. Acesse stripe.com → Crie conta
2. Crie produto "Guia ProdutoVivo" com preço R$37 (modo BRL)
3. Copie o Price ID (price_xxx)
4. Adicione ao .env:
   - `STRIPE_SECRET_KEY=sk_live_...`
   - `STRIPE_PRICE_ID=price_...`
   - `STRIPE_WEBHOOK_SECRET=whsec_...`
5. Configure webhook no Stripe: `https://produtovivo.com/webhook/stripe`

---

### 3. Meta Business Manager — Conta de Anúncios (PRIORIDADE MÉDIA)

O Pixel 4520253334926563 já está instalado em todas as páginas e rastreando PageView, Lead, InitiateCheckout e Purchase. Mas **sem conta de anúncios, o Pixel não serve para paid traffic**.

**O que fazer:**
1. Acesse business.facebook.com
2. Crie ou use conta de anúncios existente
3. Conecte o Pixel 4520253334926563 à conta
4. Crie a campanha seguindo o brief em `docs/meta-ads-strategy.md`
5. Budget inicial recomendado: R$15/dia por 7-14 dias (fase de aprendizado)
6. Criativo sugerido: carrossel 4 cards (brief em `docs/carousel-brief.md`)

---

### 4. CSV de Prospects Reais (PRIORIDADE MÉDIA)

O arquivo `docs/prospects.csv` tem 2 linhas placeholder. Para o cold outreach funcionar:

**O que fazer:**
1. Identifique 15-20 infoprodutores brasileiros que vendem PDFs no Hotmart/Kiwify
2. Encontre o e-mail de contato (página do produto, perfil social, site)
3. Preencha o CSV com os campos:
   - `first_name`: nome de contato
   - `email`: e-mail de contato
   - `platform`: Hotmart, Kiwify ou Monetizze
   - `product_name`: nome do produto deles
   - `followers`: seguidores aproximados (pode deixar em branco)
   - `profile_url`: Instagram, YouTube ou site
   - `notes`: observações sobre o produto deles
   - `status`: deixe como `new`
4. Execute `npm run send-cold-emails:dry` para verificar antes de enviar

**Limite:** Máximo 20 emails/dia (warm-up do domínio). Janela: 09h-17h BRT.

---

## 📋 Sequência Recomendada de Ativação

```
Dia 1: DNS → Resend verificado
Dia 1: Hotmart ou Stripe configurado
Dia 2: Testar fluxo completo (quiz → email → link de compra)
Dia 3: Publicar 1 post no Instagram/LinkedIn com link do quiz
Dia 3: Enviar cold emails manualmente para 5 prospects (dry-run primeiro)
Dia 5: Analisar métricas (quiz conversions, emails, visitas)
Dia 7: Ativar anúncios no Meta (se tiver criativo pronto)
```

---

## 🔧 Variáveis de Ambiente Necessárias

```env
# Obrigatório para emails
RESEND_API_KEY=re_...

# Obrigatório para pagamento (escolha um)
STRIPE_SECRET_KEY=sk_live_...
STRIPE_PRICE_ID=price_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Opcional (Hotmart como alternativa)
HOTMART_CHECKOUT_URL=https://pay.hotmart.com/...

# Database (já configurado em produção)
DATABASE_URL=postgresql://...

# Configuração do app
APP_URL=https://produtovivo.com
NODE_ENV=production
PORT=8082

# Limite de emails/dia (padrão: 20)
COLD_EMAIL_DAILY_LIMIT=20
```

---

## 📊 Métricas para acompanhar

| Métrica | Meta inicial | Ferramenta |
|---------|-------------|------------|
| Visitantes/dia | 50+ | Google Analytics / Cloudflare |
| Taxa de conversão quiz | >30% | `/leads` no DB |
| Taxa de conversão site | >1% | Stripe/Hotmart |
| Taxa de abertura cold email | >25% | Resend dashboard |
| Custo por compra (ads) | <R$30 | Meta Ads Manager |

---

*Documento gerado em: 2026-04-13 | Agente: Araguaia (e569f556)*
