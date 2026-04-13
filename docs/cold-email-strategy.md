# Cold Email Outreach Strategy — ProdutoVivo

## Context

15 qualified prospects already researched (Hotmart/Kiwify infoproducers). New sending domain: @produtovivo.com via Resend + DKIM.

## Domain Setup Checklist

- [ ] Verify DKIM records are live on produtovivo.com
- [ ] Add SPF record: `v=spf1 include:_spf.resend.com ~all`
- [ ] Add DMARC: `v=DMARC1; p=none; rua=mailto:postmaster@produtovivo.com`
- [ ] Test deliverability with mail-tester.com (target score: ≥ 9/10)
- [ ] Warm up domain: 5 emails/day week 1, 20/day week 2, 50/day week 3+

## Sending Identity

- **From:** `cesar@produtovivo.com` or `contato@produtovivo.com`
- **Reply-to:** Same as from
- **Provider:** Resend API

## Prospect Profile

Target: Brazilian infoproducers who:
- Have at least one product on Hotmart or Kiwify
- Use PDFs as course materials or lead magnets
- Have 1k–50k followers on Instagram or YouTube
- Are not yet using AI tools in their content

## Email Sequence (3-touch)

### Email 1 — Day 0: Personalized observation

**Subject:** `{FirstName}, vi seu produto no {Platform}`

```
Oi {FirstName},

Vi que você tem {ProductName} no {Platform} — parabéns pelo lançamento.

Tenho um guia que mostra como transformar PDFs como o seu num app interativo com IA, em menos de uma tarde.

Tem funcionado bem pra infoprodutores no Hotmart. Quer que eu te mande o link? R$37 só essa semana.

Abraço,
Cesar
produtovivo.com
```

### Email 2 — Day 3: Value + proof

**Subject:** `Resultado real: PDF virou app em 40 minutos`

```
Oi {FirstName},

Te mandei um e-mail outro dia sobre o ProdutoVivo.

Queria compartilhar um exemplo concreto: um produtor pegou um PDF de 30 páginas e, usando os prompts do guia, criou um app com quiz, glossário e resumos gerados por IA — tudo sem código.

Se você tem PDFs parados ou cursos que precisam de atualização, isso pode ser exatamente o que você está buscando.

Link: produtovivo.com
Preço: R$37

Qualquer dúvida, responde aqui.

Cesar
```

### Email 3 — Day 7: Final nudge

**Subject:** `Última mensagem sobre o ProdutoVivo`

```
Oi {FirstName},

Última vez que te escrevo sobre isso — promessa.

Se o timing não foi bom, sem problema. Mas se você ainda pensa em modernizar seus materiais com IA, o guia está em produtovivo.com por R$37.

Boa sorte com {ProductName}!

Cesar
```

## Prospect List

File: `/docs/prospects.csv` (to be populated)

| Field | Description |
|-------|-------------|
| first_name | First name |
| email | Contact email |
| platform | Hotmart or Kiwify |
| product_name | Their main product name |
| followers | Approx. follower count |
| status | new / sent-1 / sent-2 / sent-3 / replied / converted |

## Sending Schedule

- Max 20 cold emails/day during warm-up
- Send window: 09:00–11:00 BRT (12:00–14:00 UTC)
- Never send Friday after 15:00 BRT or weekends

## Tracking

- Open rate target: ≥ 40%
- Reply rate target: ≥ 5%
- Conversion target: ≥ 2% (1 sale per 50 emails)
- Track via Resend webhooks → log to `/docs/email-log.csv`

## Weekly Review

Every Monday:
- Check open/click/reply metrics in Resend dashboard
- Move replied prospects to appropriate status
- Pause sequence for bounces or unsubscribes immediately
- Report conversion rate to CEO
