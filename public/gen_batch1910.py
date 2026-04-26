import os, json, pathlib

BASE   = os.path.join(os.path.dirname(__file__), "blog")
DOMAIN = "https://produtovivo.com.br"
PIXEL  = "4520253334926563"

TMPL = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<link rel="canonical" href="{url}"/>
<!-- Facebook Pixel -->
<script>
!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','{pixel}');fbq('track','PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id={pixel}&ev=PageView&noscript=1"/></noscript>
<!-- Schema FAQ -->
<script type="application/ld+json">{faq_schema}</script>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Segoe UI',sans-serif;color:#1a1a1a;background:#fff}}
header{{background:#0a7c4e;padding:18px 24px}}
header a{{color:#fff;font-size:1.4rem;font-weight:700;text-decoration:none}}
nav{{background:#085f3b;padding:8px 24px;font-size:.85rem}}
nav a{{color:#cde8d8;text-decoration:none;margin-right:16px}}
.hero{{background:linear-gradient(135deg,#0a7c4e,#14a86a);color:#fff;padding:56px 24px 44px;text-align:center}}
.hero h1{{font-size:2rem;max-width:780px;margin:0 auto 16px;line-height:1.3}}
.hero p{{font-size:1.1rem;max-width:640px;margin:0 auto;opacity:.92}}
main{{max-width:820px;margin:40px auto;padding:0 20px 60px}}
h2{{font-size:1.35rem;color:#0a7c4e;margin:36px 0 12px;border-left:4px solid #0a7c4e;padding-left:12px}}
p{{line-height:1.8;margin-bottom:16px;color:#333}}
.faq{{background:#f4faf7;border-radius:10px;padding:28px 24px;margin:44px 0}}
.faq h2{{border:none;padding:0;margin-bottom:20px;font-size:1.25rem}}
details{{margin-bottom:14px;border:1px solid #c3ddd1;border-radius:8px;padding:14px 16px;background:#fff}}
summary{{font-weight:600;cursor:pointer;color:#085f3b;list-style:none}}
summary::-webkit-details-marker{{display:none}}
details p{{margin:10px 0 0;color:#444;font-size:.97rem}}
.cta{{background:#0a7c4e;color:#fff;border-radius:12px;padding:36px 28px;text-align:center;margin:48px 0}}
.cta h2{{color:#fff;border:none;padding:0;margin-bottom:12px;font-size:1.4rem}}
.cta p{{color:#d4f0e4;margin-bottom:22px}}
.cta a{{background:#fff;color:#0a7c4e;font-weight:700;padding:14px 32px;border-radius:8px;text-decoration:none;font-size:1rem}}
footer{{background:#085f3b;color:#a8d5bf;text-align:center;padding:22px;font-size:.85rem}}
footer a{{color:#a8d5bf}}
</style>
</head>
<body>
<header><a href="/">ProdutoVivo</a></header>
<nav>
  <a href="/">Home</a>
  <a href="/blog/">Blog</a>
  <a href="/guia-produto-digital/">Guia</a>
  <a href="/trilha.html">Trilha</a>
</nav>
<div class="hero">
  <h1>{h1}</h1>
  <p>{lead}</p>
</div>
<main>
{sections_html}
<div class="faq">
  <h2>Perguntas Frequentes</h2>
  {faq_html}
</div>
<div class="cta">
  <h2>Pronto para escalar seu negócio digital?</h2>
  <p>O ProdutoVivo ensina infoprodutores brasileiros a criar, lançar e vender produtos digitais que geram receita recorrente.</p>
  <a href="/">Quero Começar Agora</a>
</div>
</main>
<footer>
  <p>&copy; 2025 <a href="/">ProdutoVivo</a> — Todos os direitos reservados.</p>
</footer>
</body>
</html>"""


def art(slug, title, desc, h1, lead, sections, faq_list):
    url = f"{DOMAIN}/blog/{slug}/"
    faq_items = []
    for q, a in faq_list:
        faq_items.append({"@type": "Question", "name": q,
                          "acceptedAnswer": {"@type": "Answer", "text": a}})
    faq_schema = json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
                              "mainEntity": faq_items}, ensure_ascii=False)
    sections_html = ""
    for heading, body in sections:
        sections_html += f"<h2>{heading}</h2>\n<p>{body}</p>\n"
    faq_html = ""
    for q, a in faq_list:
        faq_html += f"<details><summary>{q}</summary><p>{a}</p></details>\n"
    html = TMPL.format(title=title, desc=desc, url=url, pixel=PIXEL,
                       faq_schema=faq_schema, h1=h1, lead=lead,
                       sections_html=sections_html, faq_html=faq_html)
    out = pathlib.Path(BASE) / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"  {slug}")


# ── Batch 1910 — articles 5303–5310 ──────────────────────────────────────────

# 5303 — B2B SaaS: procurement e compras corporativas
art(
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-procurement-e-compras-corporativas",
    "Gestão de Negócios de Empresa de B2B SaaS de Procurement e Compras Corporativas | ProdutoVivo",
    "Como construir e escalar um B2B SaaS de procurement e compras corporativas: oportunidades, produto, go-to-market e crescimento no mercado brasileiro.",
    "Gestão de Negócios de Empresa de B2B SaaS de Procurement e Compras Corporativas",
    "Procurement digital reduz custos e aumenta a eficiência das compras empresariais. Conheça o mercado e as oportunidades para um SaaS especializado.",
    [
        ("O Mercado de Procurement Digital no Brasil",
         "Empresas brasileiras de médio e grande porte gastam 40-70% de seu faturamento em compras de materiais, serviços e insumos. A gestão manual de fornecedores, cotações e aprovações de compra gera ineficiências enormes: cotações por e-mail sem rastreabilidade, aprovações que travam por dias em cadeias de e-mail, contratos armazenados em pastas compartilhadas sem controle de vencimento. Um SaaS de procurement digitaliza esse fluxo — e cada 1% de economia nas compras de uma empresa de R$100M equivale a R$1M de impacto no resultado, justificando investimentos significativos na ferramenta."),
        ("Funcionalidades Core de um Procurement SaaS",
         "O produto mínimo viável deve cobrir: gestão de fornecedores (cadastro, qualificação, avaliação de desempenho); cotações e RFQ (Request for Quotation) digitais com comparativo automático; workflow de aprovação de pedidos de compra configurável por alçada e valor; emissão de pedidos de compra (PO) com integração ao ERP; gestão de contratos de fornecimento com alertas de vencimento; e indicadores de desempenho de compras (savings realizados, lead time de fornecimento, índice de homologação de fornecedores)."),
        ("Segmentação e ICP para Procurement SaaS",
         "O ICP são empresas com 100+ colaboradores e equipe de compras dedicada (gerente ou diretor de compras). Setores mais propensos à adoção: indústria manufatureira (alto volume de insumos), construção civil (obras com muitos fornecedores simultâneos), saúde (hospitais e clínicas com compras reguladas), varejo (cadeia de fornecimento complexa), e setor público (onde a digitalização de compras é mandatória pela Nova Lei de Licitações). Empresas em processo de certificação ISO 9001 ou que passaram por auditoria com achados em compras são leads quentes."),
        ("Go-to-Market: Integrações e Parcerias ERP",
         "Procurement SaaS vive ou morre pela integração com ERPs — sem sincronizar pedidos de compra, recebimentos e contas a pagar com o ERP do cliente, o produto cria trabalho duplicado. Invista em integrações nativas com TOTVS Protheus, SAP Business One, Sankhya e Oracle NetSuite — os mais comuns em PMEs e médias empresas brasileiras. Parcerias com consultorias de implantação de ERP que incluem procurement como módulo complementar criam um canal de distribuição de baixo custo com leads altamente qualificados."),
        ("Modelo de Receita e Potencial de Crescimento",
         "Precificação por número de usuários compradores ou por volume de pedidos de compra mensais. Empresas com equipe de 5 compradores pagam R$2.000-8.000/mês; operações de compras de grande porte com 50+ usuários pagam R$30.000-100.000/mês. O módulo de análise de gastos (spend analytics) — que cruza dados de compras com categorias, fornecedores e períodos para identificar oportunidades de saving — é o upsell mais valioso e justifica incrementos de 30-50% no contrato base. NRR acima de 120% é alcançável em contas maduras."),
    ],
    [
        ("Qual a diferença entre procurement SaaS e módulo de compras do ERP?",
         "Módulos de compras de ERPs como TOTVS e SAP focam no processamento transacional — emissão de PO, recebimento, aprovação e integração contábil. Procurement SaaS adiciona camadas estratégicas: portal de fornecedores para autoatendimento, cotações digitais com múltiplos fornecedores, análise de gastos por categoria, gestão de riscos de fornecedores e benchmarking de preços. As melhores implementações integram o Procurement SaaS com o ERP existente, sem substituí-lo."),
        ("Como demonstrar ROI de um sistema de procurement?",
         "O ROI de procurement digital se comprova em: savings nas cotações (comparação automática reduz 5-15% nos preços pela maior competição entre fornecedores), redução de lead time de compras (aprovações que levavam 3-5 dias caem para horas), redução de retrabalho administrativo (cotações manuais consomem 40-60% do tempo de compradores), e eliminação de compras fora do processo (maverick spending). Para uma empresa gastando R$20M/ano em compras, um saving de 5% = R$1M — ROI sobre qualquer investimento em software de procurement em semanas."),
        ("Procurement SaaS é adequado para setor público?",
         "Sim, com adaptações. O setor público brasileiro tem requisitos específicos: conformidade com a Nova Lei de Licitações (Lei 14.133/2021), integração com COMPRASNET e portais estaduais, gestão de atas de registro de preço e dispensa de licitação. SaaS com módulo específico para compras públicas atende prefeituras, autarquias e empresas estatais — um mercado enorme com digitalização mandatória e orçamentos dedicados para modernização da gestão pública."),
    ]
)

# 5304 — Clinic: cardiologia adulto e prevenção cardiovascular
art(
    "gestao-de-clinicas-de-cardiologia-adulto-e-prevencao-cardiovascular",
    "Gestão de Clínicas de Cardiologia Adulto e Prevenção Cardiovascular | ProdutoVivo",
    "Guia para gestão de clínicas de cardiologia adulto: estrutura de ecocardiografia, equipe, credenciamento, modelos de receita e estratégias de crescimento.",
    "Gestão de Clínicas de Cardiologia Adulto e Prevenção Cardiovascular",
    "Doenças cardiovasculares são a principal causa de morte no Brasil. Saiba como estruturar uma clínica cardiológica rentável com foco em prevenção e diagnóstico.",
    [
        ("A Cardiologia como Especialidade de Alta Demanda",
         "Doenças cardiovasculares respondem por 30% das mortes no Brasil anualmente — são a principal causa de mortalidade no país. Hipertensão arterial afeta 36 milhões de brasileiros, e a prevalência de diabetes, sedentarismo e obesidade alimenta um pipeline crescente de pacientes cardiológicos. Ao contrário de especialidades de demanda pontual, a cardiologia gera pacientes de acompanhamento contínuo por anos ou décadas, criando receita recorrente previsível e alta fidelização por natureza."),
        ("Estrutura Física e Equipamentos de Diagnóstico",
         "Uma clínica cardiológica bem equipada precisa de: ecocardiógrafo (modo M, bidimensional e Doppler) — investimento de R$80.000-250.000, item mais impactante na receita do serviço; eletrocardiograma de 12 derivações (R$5.000-15.000) para exames rápidos de triagem; aparelho de Holter para monitoramento de 24h do ritmo cardíaco (R$15.000-40.000); MAPA (Monitorização Ambulatorial da Pressão Arterial); e esteira ergométrica para teste de esforço (R$30.000-80.000). Cada equipamento adiciona uma linha de receita independente por exame realizado."),
        ("Modelos de Receita em Cardiologia Clínica",
         "Cinco pilares de receita: (1) Consultas cardiológicas — pacientes hipertensos e cardiopatas em acompanhamento semestral a anual; (2) Ecocardiograma — exame de maior ticket (R$400-900 no particular), alta demanda de clínicos e cirurgiões; (3) Holter e MAPA — exames de médio ticket com baixo custo operacional; (4) Teste ergométrico — avaliação de risco cardiovascular para pacientes ativos e pré-cirúrgicos; (5) Programa de prevenção cardiovascular — consultas seriadas com protocolo de estratificação de risco (Escore de Framingham, cálcio coronariano)."),
        ("Credenciamento e Parcerias Estratégicas",
         "Credenciar com operadoras que têm alta prevalência de hipertensos e cardiopatas em sua carteira — planos corporativos de grandes empresas, planos de servidores públicos, planos sênior. Parcerias com hospitais para laudos de ecocardiograma e interpretação de Holter/MAPA de outros serviços ampliam a receita sem aumentar a estrutura física. A referência e contrareferência com cardiologias intervencionistas (cateterismo, angioplastia) e cirurgiões cardíacos é essencial para casos de maior complexidade e mantém o cardiologista clínico no centro do cuidado."),
        ("Marketing e Captação para Cardiologia",
         "SEO local para 'cardiologista [cidade]' e 'ecocardiograma particular [cidade]' tem alta conversão — pessoas com sintomas cardíacos buscam ativamente. Conteúdo educativo sobre prevenção cardiovascular (como reduzir risco de infarto, importância do controle de hipertensão, exercícios seguros para cardiopatas) no Instagram e YouTube cria autoridade e gera tráfego orgânico de alto valor. A parceria com médicos de família, clínicos gerais e endocrinologistas que encaminham pacientes hipertensos e diabéticos é o canal de captação mais eficiente em volume."),
    ],
    [
        ("Qual o investimento para montar uma clínica de cardiologia com ecocardiografia?",
         "Uma clínica de cardiologia básica com ecocardiógrafo, ECG e MAPA/Holter requer R$200.000-500.000 em equipamentos, mais R$100.000-250.000 em obras e adequações, totalizando R$300.000-750.000. O payback varia conforme a agenda: com 3-4 ecocardiogramas/dia + consultas, a receita mensal bruta de R$40.000-80.000 possibilita retorno em 2-4 anos com margem de 25-35%."),
        ("Cardiologista precisa de RT hospitalar para fazer ecocardiograma ambulatorial?",
         "Para ecocardiograma ambulatorial (transtorácico), não é necessário vinculação hospitalar — o cardiologista pode realizar e laudar o exame em clínica ambulatorial própria. O CNES deve ter o serviço habilitado como 'Cardiologia' com o cardiologista como Responsável Técnico. Ecocardiogramas transesofágicos (procedimento mais invasivo) exigem estrutura de suporte e, dependendo do estado, habilitação específica da Vigilância Sanitária."),
        ("Como expandir de consultório para clínica cardiológica completa?",
         "A expansão começa pela aquisição do ecocardiógrafo — exame com maior retorno por hora de cardiologista. Com agenda de eco estabelecida, adiciona-se Holter e MAPA (baixo investimento, alta margem). O teste ergométrico vem em seguida para atender demanda de avaliação pré-operatória e check-up. Cada equipamento adiciona uma linha de receita que dilui os custos fixos e eleva a margem operacional total da clínica."),
    ]
)

# 5305 — SaaS Sales: mídia e entretenimento digital
art(
    "vendas-para-o-setor-de-saas-de-midia-e-entretenimento-digital",
    "Vendas para o Setor de SaaS de Mídia e Entretenimento Digital | ProdutoVivo",
    "Estratégias de vendas B2B para SaaS de mídia e entretenimento digital: como prospectar produtoras, streamings, agências e veículos de comunicação.",
    "Vendas para o Setor de SaaS de Mídia e Entretenimento Digital",
    "O setor de mídia e entretenimento digital movimenta R$80 bilhões no Brasil e está em rápida transformação. Saiba como vender SaaS para esse mercado dinâmico.",
    [
        ("O Ecossistema de Mídia e Entretenimento Digital no Brasil",
         "O setor de mídia e entretenimento brasileiro é diverso: produtoras audiovisuais (filmes, séries, publicidade), plataformas de streaming (Globoplay, Paramount+, plataformas independentes), veículos de imprensa digital, agências de publicidade e marketing, estúdios de games, podcasts e creators economy. Todos compartilham necessidades comuns que SaaS pode resolver: gestão de produção de conteúdo, monetização, analytics de audiência, distribuição multicanal e gestão de direitos digitais (DRM/royalties)."),
        ("Tipos de SaaS para Mídia: o Mapa do Mercado",
         "Os principais segmentos de SaaS para mídia: (1) CMS e plataformas de publicação digital — para portais de notícias, blogs corporativos e publishers; (2) Video hosting e streaming — infraestrutura para VOD e live streaming; (3) DAM (Digital Asset Management) — gestão de vídeos, fotos e arquivos de produção; (4) Ad tech — gestão de inventário publicitário, programático, DFP; (5) Royalty management — gestão de direitos autorais e pagamentos de royalties; (6) Gestão de produção audiovisual — project management específico para set e pós-produção."),
        ("Prospecção: Encontrando os Compradores em Mídia",
         "Os decisores em mídia variam por segmento: diretores de tecnologia (CTOs) de veículos digitais, heads de produção em produtoras, diretores de monetização em plataformas de conteúdo, e CMOs de agências que gerenciam múltiplos clientes de publicidade. Eventos como CCXP, Abra Aberta, Fórum da Internet no Brasil e Festival do Rio são pontos de encontro. Grupos do LinkedIn de profissionais de mídia digital e comunidades de content creators são canais de prospecção eficazes para soluções voltadas ao segmento independente."),
        ("Demo e Prova de Valor em Mídia Digital",
         "O setor de mídia valoriza velocidade, usabilidade e integração. A demo deve mostrar o fluxo real do cliente: publicação de conteúdo em múltiplos canais simultaneamente, analytics de engajamento em tempo real, monetização automatizada de vídeos, e gestão de direitos com rastreamento de uso. Mostre integrações com ferramentas do stack já usado no setor: Adobe Creative Suite, Google Analytics, Meta Ads, YouTube Studio, Cloudflare Stream. Um trial de 30 dias com suporte white-glove em uma produção real do cliente fecha contrato mais rápido que qualquer demo."),
        ("Modelos de Receita e Crescimento",
         "Modelos predominantes em mídia SaaS: por volume de conteúdo (horas de vídeo processadas, artigos publicados), por CPM (custo por mil impressões gerenciadas pela ad tech), por usuário ativo, ou por receita gerenciada (revenue share sobre monetização). Produtoras independentes pagam R$500-3.000/mês; veículos de mídia de médio porte R$5.000-30.000/mês; grandes grupos de comunicação R$50.000-200.000/mês para plataformas enterprise. A expansão ocorre quando o cliente lança novos canais, séries ou produtos digitais — cada lançamento é uma oportunidade de upsell."),
    ],
    [
        ("DAM (Digital Asset Management) é o mesmo que CMS?",
         "Não. CMS (Content Management System) gerencia a publicação e distribuição de conteúdo para audiências finais — é o back-end de um site ou portal. DAM (Digital Asset Management) gerencia os arquivos brutos de produção: vídeos em alta resolução, fotos originais, arquivos de After Effects, trilhas sonoras — o material de trabalho interno das equipes criativas. Produtoras de audiovisual precisam mais de DAM; publishers de conteúdo precisam mais de CMS. Plataformas que integram ambos têm vantagem competitiva no mercado de mídia."),
        ("Como SaaS de ad tech compete com Google DFP (Google Ad Manager)?",
         "Google Ad Manager é gratuito para publishers de menor escala e tem adoção dominante no mercado. SaaS de ad tech competem em nichos específicos: gestão de anúncios diretos (diretos negociados fora do programático), native advertising, managed campaigns para veículos que não têm equipe interna de ad ops, e relatórios de receita publicitária multi-plataforma integrados com Google + Meta + programáticas independentes. A complementaridade ao GAM, não a substituição, é a estratégia mais eficaz de posicionamento."),
        ("Como o mercado de creators economy impacta o SaaS de mídia?",
         "A creators economy criou um novo segmento de clientes: criadores individuais e pequenas equipes (podcasters, youtubers, streamers) com necessidades específicas — gestão de múltiplos canais, analytics de monetização (YouTube Adsense + Patreon + Hotmart + Kwai), gestão de marcas patrocinadoras e calendário editorial. SaaS voltado a esse público tem ticket menor (R$150-800/mês) mas mercado enorme e crescimento viral via comunidades de criadores. O PLG (Product-Led Growth) com freemium funciona bem nesse segmento."),
    ]
)

# 5306 — Consulting: sucessão familiar e governança de empresas familiares
art(
    "consultoria-de-sucessao-familiar-e-governanca-de-empresas-familiares",
    "Consultoria de Sucessão Familiar e Governança de Empresas Familiares | ProdutoVivo",
    "Como estruturar uma consultoria de sucessão familiar e governança de empresas familiares: metodologias, posicionamento, captação e modelos de receita.",
    "Consultoria de Sucessão Familiar e Governança de Empresas Familiares",
    "70% das empresas familiares não sobrevivem à segunda geração. Veja como posicionar sua consultoria nesse mercado de alta complexidade e alto valor.",
    [
        ("O Desafio da Sucessão em Empresas Familiares Brasileiras",
         "Empresas familiares representam 90% das empresas brasileiras e 65% do PIB. No entanto, apenas 30% chegam à segunda geração e menos de 15% à terceira. Os principais vilões da longevidade são: conflitos familiares não resolvidos, ausência de governança formal, sucessão planejada tardiamente (ou não planejada), e mistura entre patrimônio pessoal e empresarial. O mercado de consultoria em governança de empresas familiares e sucessão cresce à medida que a geração de fundadores envelhece e a geração seguinte (filhos de empresários) assume ou questiona o legado."),
        ("Portfólio de Serviços: do Conselho ao Protocolo Familiar",
         "Os serviços centrais de uma consultoria de empresas familiares: (1) Diagnóstico de governança familiar — mapeamento da estrutura societária, conflitos latentes e gap de governança; (2) Elaboração do Protocolo Familiar — acordo sobre regras de convivência, política de dividendos, critérios para cargos familiares, gestão de patrimônio; (3) Estruturação de Conselho de Família — fórum para tomada de decisão familiar separado da gestão; (4) Planejamento de Sucessão — preparação de sucessores, coaching de liderança para a próxima geração; (5) Implementação de Conselho de Administração com membros independentes."),
        ("Metodologia: Navegando Dinâmicas Familiares Complexas",
         "Empresas familiares exigem habilidade para trabalhar simultaneamente com a dimensão empresarial (estratégia, finanças, gestão) e a dimensão familiar (dinâmicas emocionais, rivalidades entre irmãos, expectativas de fundadores). Consultores de empresas familiares bem-sucedidos combinam conhecimento de negócios com competências de facilitação sistêmica (abordagem sistêmica familiar, terapia de grupo, constelação organizacional). O Modelo dos Três Círculos (família, propriedade, empresa) é a estrutura conceitual mais usada para explicar e trabalhar as interdependências."),
        ("Captação: Onde os Fundadores Buscam Ajuda",
         "Fundadores de empresas familiares costumam buscar ajuda quando um evento crítico ocorre: morte ou adoecimento do patriarca/matriarca, conflito aberto entre sócios familiares, entrada ou saída de cônjuges da sociedade, ou preparação para venda do negócio. Advogados societários, contadores e gestores de patrimônio são os primeiros profissionais contatados nesses momentos — parcerias com essas categorias geram os leads mais quentes. Conteúdo educativo sobre governança familiar para empresários (artigos, workshops, webinars) também gera demanda inbound de qualidade."),
        ("Precificação e Duração dos Projetos",
         "Projetos de diagnóstico de governança: R$20.000-60.000 (4-8 semanas). Elaboração de protocolo familiar: R$80.000-250.000 (3-6 meses, envolve múltiplas reuniões com a família). Acompanhamento de implementação de conselho de administração: R$15.000-40.000/mês. Coaching de sucessores: R$5.000-15.000/mês por herdeiro acompanhado. A longevidade dos projetos é alta — famílias que constroem governança continuam trabalhando com o consultor por 5-10 anos à medida que a estrutura evolui. LTV médio de um cliente de empresa familiar supera R$500.000 ao longo do relacionamento."),
    ],
    [
        ("Qual a diferença entre protocolo familiar e acordo de acionistas?",
         "O acordo de acionistas é um documento juridicamente vinculante que regula direitos de voto, transferência de ações, tag-along, drag-along e outros aspectos societários formais. O protocolo familiar (ou constituição familiar) vai além: trata das regras de convivência entre os membros da família, critérios para trabalhar na empresa, política de dividendos e distribuições, gestão do patrimônio familiar, processo de resolução de conflitos e visão de legado. Os dois documentos são complementares e idealmente elaborados juntos com assessoria jurídica e consultoria de governança familiar."),
        ("Como uma empresa familiar decide que chegou a hora de contratar uma consultoria de governança?",
         "Os gatilhos mais comuns: (a) O fundador acima de 60 anos começa a pensar em sucessão; (b) Conflito entre sócios familiares (irmãos, primos) ameaça a operação; (c) Entrada de investidor externo (PE, family office) que exige governança formal como condição; (d) Processo de venda da empresa onde compradores exigem estrutura societária clara; (e) Crescimento acelerado que torna informal a gestão inadequada. Qualquer um desses momentos cria urgência e disposição a pagar por uma consultoria especializada."),
        ("Escritório de família e governança de empresa familiar são a mesma coisa?",
         "Não. Family office (escritório de família) gerencia o patrimônio financeiro da família — investimentos, trust, planejamento tributário e sucessório do patrimônio pessoal. Governança de empresa familiar foca na empresa operacional — como a família governa o negócio, toma decisões e planeja a successão na gestão. Muitas famílias precisam dos dois tipos de serviço; alguns family offices expandem para governança familiar, e algumas consultorias de governança fazem interface com o planejamento patrimonial, mas são disciplinas distintas com profissionais de formação diferente."),
    ]
)

# 5307 — B2B SaaS: sales enablement e inteligência de vendas
art(
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-sales-enablement-e-inteligencia-de-vendas",
    "Gestão de Negócios de Empresa de B2B SaaS de Sales Enablement e Inteligência de Vendas | ProdutoVivo",
    "Como construir e escalar um B2B SaaS de sales enablement e inteligência de vendas: mercado, funcionalidades, go-to-market e crescimento.",
    "Gestão de Negócios de Empresa de B2B SaaS de Sales Enablement e Inteligência de Vendas",
    "Times de vendas que usam sales enablement fecham 49% mais negócios. Veja como construir um SaaS nesse mercado de alto crescimento.",
    [
        ("O Mercado de Sales Enablement no Brasil",
         "Sales enablement — o conjunto de processos, conteúdos e ferramentas que capacitam vendedores a vender melhor — é uma categoria em expansão acelerada no Brasil. Empresas que escalam times comerciais enfrentam o problema do onboarding lento (vendedores novos demoram 6-9 meses para atingir quota), materiais de vendas desatualizados (decks em várias versões circulando por WhatsApp), e falta de visibilidade sobre o que o conteúdo de vendas realmente é usado nas negociações. Um SaaS de sales enablement resolve essas dores com ROI demonstrável."),
        ("Funcionalidades Essenciais: Biblioteca, Playbooks e Analytics",
         "O produto core deve cobrir: biblioteca centralizada de conteúdo de vendas (apresentações, cases, propostas, battle cards) com versionamento e busca inteligente; criação de playbooks de vendas com sequências de atividades por etapa do funil; envio de conteúdo para prospects com rastreamento de visualizações (quem abriu, quanto tempo assistiu); analytics de eficácia de conteúdo (quais materiais fecham mais negócios); onboarding digital de novos vendedores com trilhas de capacitação; e integração bidirecional com CRM (Salesforce, HubSpot, Pipedrive, RD Station CRM)."),
        ("ICP e Estratégia de Go-to-Market",
         "O ICP são empresas com 15-200 vendedores B2B que já têm CRM implantado mas não têm processo de enablement estruturado. Segmentos de maior aderência: SaaS e tecnologia (vendem produto complexo que exige muito conhecimento), serviços financeiros (produtos regulados com compliance de comunicação), e consultoria/serviços profissionais (proposta de valor difícil de comunicar sem suporte estruturado). O comprador é o VP de Vendas ou o Head de Sales Enablement — um papel crescente em empresas de 100+ vendedores que ainda não existe nas menores."),
        ("Precificação e Métricas de Valor",
         "Precificação por assento de vendedor: R$150-400/mês por usuário. Uma empresa com 50 vendedores paga R$7.500-20.000/mês — facilmente justificado por 1 negócio adicional por trimestre por vendedor. Módulos de inteligência de vendas (análise de chamadas com IA para feedback automático, scoring de deal, forecast de fechamento) elevam o ticket em 40-80%. Os KPIs de ROI que o cliente monitora: tempo de ramp-up de novos vendedores (redução de 30-50%), win rate (aumento de 15-25%), e ACV (Annual Contract Value) médio por deal."),
        ("Crescimento: Integrações e Rede de Parceiros",
         "Sales enablement SaaS cresce pelo ecossistema: quanto mais integrado com o stack de vendas do cliente (CRM, videoconferência, e-mail, sequenciadores de prospecção), mais indispensável se torna. Construa integrações nativas com as ferramentas líderes de cada categoria. Parcerias com consultorias de RevOps (Revenue Operations) e agências de inside sales que implantam processos de vendas são canais poderosos — o consultor de RevOps recomenda sua ferramenta para cada cliente que estrutura um processo de enablement. Programa de parceiros com certificação e comissão recorrente cria canal de distribuição escalável."),
    ],
    [
        ("Sales enablement é o mesmo que CRM?",
         "Não. CRM (Customer Relationship Management) registra e gerencia o relacionamento com clientes e o pipeline de vendas — é o sistema de registro. Sales enablement foca em capacitar o vendedor para agir melhor em cada etapa do CRM: ter o material certo, o playbook correto, o treinamento adequado e os dados para tomar decisões. Os dois sistemas se complementam — o enablement usa dados do CRM para medir eficácia de conteúdo e correlacionar materiais com negócios fechados."),
        ("Como medir o ROI de uma plataforma de sales enablement?",
         "As métricas de ROI mais diretas: (1) Redução do tempo de ramp-up de novos vendedores (de 6 para 4 meses = 2 meses de quota extra por contratação); (2) Aumento do win rate (de 20% para 25% = 25% mais receita com o mesmo número de oportunidades); (3) Redução do ciclo de vendas (cada semana a menos no ciclo libera capacidade para mais oportunidades); (4) Aumento na utilização de conteúdo aprovado (menos conformidade jurídica/compliance e menos tempo procurando materiais). Construa um business case com esses números antes da apresentação de proposta."),
        ("Sales enablement faz sentido para times pequenos (menos de 10 vendedores)?",
         "Para times muito pequenos (menos de 5 vendedores), o custo-benefício de uma plataforma dedicada pode não se justificar — uma combinação de Google Drive organizado + HubSpot pode bastar. A partir de 10-15 vendedores, especialmente em empresas com produto complexo ou processo de vendas consultivo, a plataforma de enablement começa a pagar — o problema de 'cada vendedor fazendo as coisas do seu jeito' se torna visível e caro. O timing ideal para comprar enablement é quando a empresa contrata seu segundo gerente de vendas."),
    ]
)

# 5308 — Clinic: medicina preventiva e check-up corporativo
art(
    "gestao-de-clinicas-de-medicina-preventiva-e-check-up-corporativo",
    "Gestão de Clínicas de Medicina Preventiva e Check-up Corporativo | ProdutoVivo",
    "Guia para gestão de clínicas de medicina preventiva e check-up corporativo: estrutura, pacotes, parceiros empresariais, captação e crescimento sustentável.",
    "Gestão de Clínicas de Medicina Preventiva e Check-up Corporativo",
    "Medicina preventiva e check-up corporativo crescem com a valorização da saúde como benefício empresarial. Veja como estruturar uma clínica lucrativa nesse segmento.",
    [
        ("O Mercado de Medicina Preventiva e Check-up no Brasil",
         "O mercado de check-up executivo e medicina preventiva corporativa movimenta mais de R$3 bilhões no Brasil. Empresas investem em saúde preventiva de executivos e colaboradores como estratégia de retenção de talentos, redução de absenteísmo e compliance com programas de saúde exigidos por operadoras. A cultura de check-up anual é mais consolidada nos estratos socioeconômicos A e B, mas cresce nas classes C e D com a expansão dos planos de saúde. Clínicas de medicina preventiva bem posicionadas têm margens superiores à média por trabalharem com particular e pacotes pré-pagos."),
        ("Estrutura de Pacotes e Portfólio de Exames",
         "O modelo de negócio de check-up se baseia em pacotes pré-definidos por faixa etária e perfil de risco: (1) Check-up básico (20-39 anos) — hemograma, bioquímica básica, ECG, consulta clínica (R$800-1.500); (2) Check-up completo (40-59 anos) — exames básicos + imagem (ultrassom abdominal, mamografia, PSA masculino) (R$2.000-4.000); (3) Check-up executivo premium — acima + tomografia coronariana, colonoscopia, testes especializados (R$5.000-15.000). A precificação por pacote é mais eficiente que por exame individual para o cliente e mais previsível para a clínica."),
        ("B2B Corporativo: o Canal de Maior Volume",
         "O canal corporativo é o mais escalável para clínicas de medicina preventiva. Empresas contratam check-up para diretores e gerentes como benefício corporativo ou como exame admissional/periódico de saúde. Para acessar esse mercado: contate diretores de RH de empresas médias e grandes (200+ colaboradores), ofereça contratos anuais com número mínimo de check-ups garantidos, forneça relatório de saúde agregado da equipe (sem identificação individual) para gestão de saúde corporativa, e apresente ROI em redução de absenteísmo. Planos de saúde corporativos também contratam clínicas de check-up para programas de prevenção de suas carteiras."),
        ("Tecnologia e Experiência do Paciente",
         "A experiência do paciente de check-up é fundamental para fidelização e boca a boca. Invista em: agendamento online em até 48h (diferencial vs. hospitais com espera de semanas), atendimento em menos de 2 horas para o check-up completo (protocolo de eficiência), prontuário eletrônico com resultados disponíveis digitalmente em 24-48h após exames, e consulta de devolutiva com médico especialista que interpreta todos os resultados de forma integrada. Aplicativo próprio ou portal do paciente para acesso ao histórico de check-ups ao longo dos anos aumenta a fidelização."),
        ("Expansão: Franquias e Clínicas Satélite",
         "Clínicas de check-up com processos bem definidos têm perfil ideal para franqueamento — o modelo pode ser replicado em outras cidades com menor dependência do médico fundador. Alternativamente, modelos de clínica satélite em condomínios corporativos ou dentro de empresas (ocupational health center) atendem colaboradores sem deslocamento, reduzindo a barreira de acesso. Parcerias com corretores de benefícios e health brokers que negociam programas de saúde para empresas são canais de distribuição B2B de alto volume para pacotes de check-up corporativo."),
    ],
    [
        ("Com que frequência é recomendado fazer check-up?",
         "A frequência varia por idade e fatores de risco: abaixo de 40 anos sem fatores de risco, check-up a cada 2-3 anos é suficiente; entre 40-60 anos, anualmente é recomendado; acima de 60 anos ou com doenças crônicas (diabetes, hipertensão, histórico familiar de câncer), o acompanhamento pode ser semestral. Para executivos em cargos de alta responsabilidade e stress, check-up anual é prática padrão em empresas que valorizam a saúde como ativo estratégico da liderança."),
        ("Check-up é coberto por plano de saúde?",
         "Parcialmente. Planos de saúde geralmente cobrem exames preventivos básicos previstos na ANS (consultas, alguns exames de imagem e laboratório), mas não cobrem 'pacotes de check-up' como produto específico. Clínicas de check-up premium geralmente atendem predominantemente particular — onde o cliente paga pelo pacote completo, pela agilidade no atendimento e pela experiência diferenciada, sem as restrições de cobertura dos planos. Alguns planos corporativos de alto padrão incluem check-up executivo como benefício específico contratado com clínicas credenciadas."),
        ("Como calcular o ROI de um programa de check-up corporativo?",
         "O ROI corporativo de check-up se demonstra via: redução de absenteísmo (diagnósticos precoces evitam afastamentos longos), redução de sinistralidade do plano de saúde (doenças crônicas detectadas cedo custam 5-10x menos para tratar), e retenção de talentos (benefício valorizado por executivos). Para uma empresa com 200 funcionários, a redução de 1 dia/mês de absenteísmo por pessoa representa R$500.000/ano em produtividade — muito superior ao custo de R$50.000-100.000 de um programa de check-up anual para 200 pessoas."),
    ]
)

# 5309 — SaaS Sales: saúde mental e bem-estar digital
art(
    "vendas-para-o-setor-de-saas-de-saude-mental-e-bem-estar-digital",
    "Vendas para o Setor de SaaS de Saúde Mental e Bem-Estar Digital | ProdutoVivo",
    "Estratégias de vendas B2B para SaaS de saúde mental e bem-estar digital: como prospectar RH, fechar contratos corporativos e expandir no mercado de mental health.",
    "Vendas para o Setor de SaaS de Saúde Mental e Bem-Estar Digital",
    "O mercado de saúde mental digital cresce 40% ao ano no Brasil. Saiba como vender SaaS de bem-estar para empresas que priorizam a saúde dos colaboradores.",
    [
        ("O Boom da Saúde Mental Corporativa",
         "A pandemia normalizou a conversa sobre saúde mental nas empresas — burnout, ansiedade e depressão tornaram-se prioridades de RH, não apenas temas de RH. O Brasil tem a segunda maior prevalência de ansiedade do mundo (9,3% da população) e lideranças que antes ignoravam saúde mental agora investem ativamente em soluções. O mercado de plataformas de saúde mental corporativa cresceu de R$200M para R$1.2B entre 2020 e 2025. Empresas que oferecem acesso a psicólogos digitais, apps de meditação, programas de EAP (Employee Assistance Program) e ferramentas de wellbeing têm forte demanda de RH."),
        ("Tipos de SaaS em Saúde Mental e Wellbeing",
         "O ecossistema inclui: (1) Plataformas de telemedicina de saúde mental — acesso a psicólogos e psiquiatras por videochamada; (2) Apps de mindfulness e meditação corporativa (Headspace, Calm Business — versões enterprise); (3) Plataformas de EAP digital — programa de assistência ao empregado com psicólogos, coaches e orientadores disponíveis 24h; (4) Ferramentas de bem-estar holístico — engajamento com atividades físicas, nutrição, sono e saúde financeira; (5) Analytics de saúde organizacional — mensuração anônima de engajamento e bem-estar por departamento para intervenção proativa do RH."),
        ("Prospecção e Acesso ao Decisor de RH",
         "O comprador primário é o CHRO ou Gerente de Benefícios. Em empresas com mais de 500 colaboradores, há frequentemente um 'Head de Saúde e Bem-Estar' ou 'Head de People Experience'. Gatilhos de compra: resultado de pesquisa de clima com baixo índice de bem-estar, aumento de afastamentos por problemas de saúde mental (CID F), benchmarking com concorrentes que já oferecem o benefício, e pressão de candidatos em processos seletivos que avaliam benefícios de saúde mental. Eventos como CONARH, HR Summit e Fórum de Saúde Mental Corporativa são pontos de encontro com decisores."),
        ("Demo e Diferenciação: Impacto vs. Engagement",
         "A maior objeção em saúde mental SaaS é: 'como medir o impacto?' Diferencie com dados: mostre taxa de utilização da plataforma (engagement médio de colaboradores), scores de bem-estar antes e depois (PHQ-9 e GAD-7 de populações), e dados de sinistralidade do plano de saúde correlacionados com uso. Plataformas que entregam relatórios trimestrais de saúde organizacional (dados agregados, sem identificação individual) dão ao CHRO visibilidade para apresentar resultados ao board — isso é o que diferencia uma plataforma 'descartável' de um parceiro estratégico de saúde."),
        ("Ciclo de Vendas e Expansão",
         "O ciclo de vendas para saúde mental corporativa varia de 30-45 dias em PMEs até 3-6 meses em grandes empresas com múltiplos stakeholders (RH, Jurídico, LGPD, TI). O piloto para um departamento de 100 colaboradores é a estratégia mais eficaz para grandes contas — os dados de engajamento do piloto fecham o contrato para toda a empresa. Expansão: empresas que adotam uma solução de saúde mental tendem a expandir para outras verticais de bem-estar (financeiro, físico, nutrição) — suite completa de wellbeing maximiza o LTV do cliente."),
    ],
    [
        ("Plataforma de saúde mental SaaS precisa ter CFM/CRP para operar?",
         "Plataformas que disponibilizam atendimento de psicólogos (videochamadas, chat com profissional) precisam seguir as regulamentações do CFM (médicos psiquiatras) e CRP (psicólogos) para telemedicina. As resoluções CFM 2.314/2022 e CRP (Resolução 11/2018 atualizada) regulamentam o atendimento psicológico online. Apps de meditação, conteúdo educativo e ferramentas de autogestão de bem-estar sem atendimento profissional não se enquadram como serviços de saúde regulados, podendo operar sem essas autorizações específicas."),
        ("Como garantir conformidade com LGPD em dados de saúde mental?",
         "Dados de saúde mental são dados sensíveis segundo a LGPD (art. 11), sujeitos a tratamento mais restrito — exigem consentimento específico e explícito do titular. Plataformas de saúde mental corporativa devem: coletar consentimento individual (não corporativo) de cada colaborador; garantir que a empresa contratante não acesse dados individuais; anonimizar todos os relatórios de saúde organizacional; e ter DPA (Data Processing Agreement) robusto com as empresas clientes. Demonstrar conformidade com LGPD é critério eliminatório em RFPs de grandes empresas."),
        ("Qual a taxa de adoção esperada de plataformas de bem-estar corporativo?",
         "A média de mercado é de 20-35% de adoção ativa (colaboradores que usam a plataforma ao menos 1x/mês). Plataformas com adoção acima de 40% são consideradas de alto desempenho. Os fatores que mais impactam a adoção: lançamento com engajamento da liderança (o CEO/CHRO comunica pessoalmente o benefício), gamificação e desafios coletivos de bem-estar, e facilidade de acesso (SSO, app mobile). Plataformas integradas ao app de benefícios já usado pelos colaboradores têm adoção 2x maior que plataformas standalone."),
    ]
)

# 5310 — Consulting: CFO as a Service e finanças corporativas
art(
    "consultoria-de-cfo-as-a-service-e-financas-corporativas",
    "Consultoria de CFO as a Service e Finanças Corporativas | ProdutoVivo",
    "Como estruturar e escalar uma consultoria de CFO as a Service e finanças corporativas: serviços, posicionamento, captação e modelos de receita para consultores financeiros.",
    "Consultoria de CFO as a Service e Finanças Corporativas",
    "Startups e PMEs precisam de expertise financeira de CFO sem o custo de um executivo CLT. Veja como monetizar essa demanda como consultor financeiro.",
    [
        ("O Mercado de CFO as a Service no Brasil",
         "Startups em crescimento, PMEs com faturamento de R$2-50M e empresas em processo de captação ou M&A frequentemente precisam de expertise financeira de CFO — mas não têm escala para contratar um CFO CLT de R$30.000-80.000/mês. O modelo de CFO as a Service (CFO fracionado) permite que um consultor financeiro sênior atenda 4-8 clientes simultaneamente, entregando 2-3 dias/semana de expertise a cada um por R$8.000-25.000/mês por cliente. O mercado brasileiro de CFO fracionado cresce 30% ao ano, impulsionado pelo ecossistema de startups e pela profissionalização de empresas familiares."),
        ("Portfólio de Serviços: do Financeiro Básico ao Board",
         "Os serviços de um CFO as a Service abrangem: (1) Estruturação financeira — implantação de DRE gerencial, fluxo de caixa, orçamento empresarial e KPIs financeiros; (2) Gestão de caixa e capital de giro — planejamento de necessidade de capital, gestão de linhas de crédito; (3) Relatórios para investidores — preparação de board packs, investor updates e covenants de dívida; (4) Fundraising support — preparação de data room financeiro, modelagem de valuation para rodadas de captação; (5) M&A support — financial due diligence, modelagem de sinergia e estruturação de deal. Cada serviço tem valor unitário e pode ser contratado isoladamente ou em conjunto."),
        ("Diferenciação: Expertise Setorial e Tecnologia Financeira",
         "CFOs fracionados que se especializam em setores específicos entregam mais valor — um CFO com histórico em SaaS conhece os benchmarks de ARR, churn, CAC e LTV que são a linguagem dos investidores de tecnologia. Da mesma forma, expertise em saúde, varejo ou indústria cria contextualização mais rápida e decisões mais acertadas. No lado tecnológico, domínio de ferramentas como Power BI para dashboards financeiros, ferramentas de FP&A (Anaplan, Pigment, DataRails) e ERPs financeiros (Conta Azul, OMIE, SAP B1) diferencia o CFO fracionado do consultor financeiro genérico."),
        ("Captação: Investidores e Aceleradoras como Canais",
         "Os melhores canais de captação para CFO as a Service: (1) VCs e fundos de investimento — recomendam CFOs fracionados para seus portfólios que precisam profissionalizar o financeiro antes de uma rodada ou auditoria; (2) Aceleradoras e incubadoras — startups no programa frequentemente precisam de apoio financeiro; (3) Bancos e fintechs de crédito — empresas em processo de solicitação de crédito chegam sem organização financeira suficiente; (4) Plataformas de marketplace de CFOs fracionados (Vee, Revelo, Toptal) — canais de distribuição digital para CFOs experientes. LinkedIn com conteúdo sobre gestão financeira para CEOs e founders gera inbound de qualidade."),
        ("Precificação e Escalabilidade",
         "CFO fracionado: R$8.000-25.000/mês por cliente (2-3 dias/semana de dedicação). Com 5 clientes simultâneos, a receita mensal alcança R$40.000-125.000 — superior à maioria dos cargos CLT de CFO de médias empresas. Projetos pontuais de fundraising support ou financial due diligence: R$25.000-100.000 por projeto de 4-8 semanas. Para escalar além da capacidade individual, construa uma equipe de analistas financeiros seniores que executam a operação enquanto o CFO sênior atua no estratégico — modelo de 'CFO + time financeiro externo' com ticket maior e capacidade de atender mais clientes."),
    ],
    [
        ("Qual a diferença entre CFO fracionado e consultor financeiro tradicional?",
         "Consultor financeiro tradicional geralmente entrega projetos específicos com escopo e prazo definidos (ex.: reestruturar o plano de contas, implantar o orçamento). CFO fracionado atua como membro executivo da empresa de forma contínua — participa das reuniões de diretoria, toma decisões financeiras em tempo real, lidera o time financeiro interno e representa a função financeira junto a investidores e bancos. A diferença é operacional vs. executiva: o CFO fracionado assume responsabilidade pela função financeira; o consultor entrega um produto específico."),
        ("CFO fracionado pode assinar DREs e demonstrações contábeis?",
         "A assinatura de demonstrações contábeis legais (balanço patrimonial, DRE para SPED) requer contador ou auditor com registro no CRC — função do contador interno ou da contabilidade terceirizada, não do CFO. O CFO fracionado assina ou referenda documentos gerenciais (board packs, investor updates, modelos financeiros) que não têm status legal de demonstrações contábeis. Em captações de investimento, o CFO fracionado coordena a preparação da documentação financeira junto ao contador e ao auditor externo."),
        ("Como definir escopo e entregáveis no contrato de CFO as a Service?",
         "O contrato deve especificar: número de horas/dias por semana de dedicação; lista de responsabilidades e entregáveis recorrentes (ex.: fluxo de caixa semanal, board pack mensal, orçamento anual); responsabilidades excluídas (ex.: gestão da contabilidade operacional e folha — função do contador); política de disponibilidade para reuniões urgentes; e forma de comunicação com o CEO. Clareza no escopo previne mal-entendidos sobre o que o CFO fracionado entrega — e distingue o seu serviço de uma simples consultoria financeira pontual."),
    ]
)

# ── Sitemap ───────────────────────────────────────────────────────────────────
slugs_5303 = [
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-procurement-e-compras-corporativas",
    "gestao-de-clinicas-de-cardiologia-adulto-e-prevencao-cardiovascular",
    "vendas-para-o-setor-de-saas-de-midia-e-entretenimento-digital",
    "consultoria-de-sucessao-familiar-e-governanca-de-empresas-familiares",
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-sales-enablement-e-inteligencia-de-vendas",
    "gestao-de-clinicas-de-medicina-preventiva-e-check-up-corporativo",
    "vendas-para-o-setor-de-saas-de-saude-mental-e-bem-estar-digital",
    "consultoria-de-cfo-as-a-service-e-financas-corporativas",
]
titles_5303 = [
    "Gestão de Negócios de Empresa de B2B SaaS de Procurement e Compras Corporativas",
    "Gestão de Clínicas de Cardiologia Adulto e Prevenção Cardiovascular",
    "Vendas para o Setor de SaaS de Mídia e Entretenimento Digital",
    "Consultoria de Sucessão Familiar e Governança de Empresas Familiares",
    "Gestão de Negócios de Empresa de B2B SaaS de Sales Enablement e Inteligência de Vendas",
    "Gestão de Clínicas de Medicina Preventiva e Check-up Corporativo",
    "Vendas para o Setor de SaaS de Saúde Mental e Bem-Estar Digital",
    "Consultoria de CFO as a Service e Finanças Corporativas",
]

sm_path = pathlib.Path(__file__).parent / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")
new_urls = "\n".join(
    f"  <url><loc>{DOMAIN}/blog/{s}/</loc><changefreq>monthly</changefreq><priority>0.6</priority></url>"
    for s in slugs_5303
)
sm_path.write_text(sm.replace("</urlset>", new_urls + "\n</urlset>"), encoding="utf-8")

# ── Trilha ────────────────────────────────────────────────────────────────────
tr_path = pathlib.Path(__file__).parent / "trilha.html"
tr = tr_path.read_text(encoding="utf-8")
new_items = "\n".join(
    f'    <li><a href="/blog/{s}/">{t}</a></li>'
    for s, t in zip(slugs_5303, titles_5303)
)
tr_path.write_text(tr.replace("</ul>", new_items + "\n  </ul>", 1), encoding="utf-8")

print("Done — batch 1910")
