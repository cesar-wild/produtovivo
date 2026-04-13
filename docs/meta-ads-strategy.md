# Meta Ads Relaunch Strategy — ProdutoVivo

## Context

Migrated from Polsia to ProdutoVivo brand. Previous Meta Ads campaign was paused too early with promising metrics (CTR 1.26%, <$100 total spend).

## Pixel

- ID: `4520253334926563`
- Domain: produtovivo.com
- Verify pixel is firing on landing page and thank-you page

## Ad Inventory

### Ad 1 — Woman talking (UGC)
- **Status:** Best historical performer
- **Assets:** Video not available — needs reshoot or sourcing
- **Action:** Source new UGC creator; brief on ProdutoVivo brand

### Ad 2 — Man bored at PDF
- **Status:** 400 impressions, assets available (photo + voiceover + subtitles)
- **Action:** Re-upload under ProdutoVivo ad account with updated branding; test at $5/day

## Relaunch Creative Batch

### Hook angles to test

1. **Pain hook** — "Você passa horas montando PDFs que ninguém lê"
2. **Curiosity hook** — "Veja como um PDF vira um app com IA em 10 minutos"
3. **Social proof hook** — "Infoprodutores no Hotmart estão usando isso agora"
4. **Direct offer** — "Guia completo por R$37 — aprenda hoje"

### Formats
- Static image + subtitle overlay (Ad 2 variant)
- Short-form video (15–30s) with text-on-screen hook
- Carousel: step-by-step transformation (PDF → app)

## Audience

- **Primary:** Brazilian infoproducers on Hotmart/Kiwify (custom audiences)
- **Lookalike:** Based on landing page visitors (pixel data)
- **Interest targeting:** Hotmart, Kiwify, infoproduto, marketing digital, Canva

## Budget Plan

| Phase | Budget | Duration | Goal |
|-------|--------|----------|------|
| Test | R$15/day | 7 days | Validate CTR + CPC |
| Scale | R$30/day | 14 days | Optimize CPM + conversions |
| Steady | R$50/day | Ongoing | Target CPA < R$18 |

## KPIs

- CTR target: ≥ 1.5% (current benchmark: 1.26%)
- CPC target: < R$1.50
- CPA target: < R$18 (< 50% of R$37 price)
- ROAS target: ≥ 2x

## Weekly Review Cadence

Every Monday at 10:00 UTC:
- Pull ad performance from Meta Ads Manager
- Check pixel event quality
- Pause underperforming ads (CTR < 0.5% after 500 impressions)
- Escalate to creative refresh if CPA > R$25

## Notes

- Keep ad account under ProdutoVivo Business Manager (not Polsia)
- All creatives in `/assets/ads/` with naming: `ad-{number}-{variant}-{date}.{ext}`
- UTM parameters: `utm_source=meta&utm_medium=paid&utm_campaign={campaign-slug}`
