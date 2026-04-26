import os, json, pathlib

BASE   = os.path.join(os.path.dirname(__file__), "blog")
DOMAIN = "https://produtovivo.com.br"
PIXEL  = "4520253334926563"

TMPL = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<script type="application/ld+json">{schema}</script>
<!-- Facebook Pixel -->
<script>
!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','{pixel}');fbq('track','PageView');
</script>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Segoe UI',sans-serif;background:#f9f9f9;color:#222;line-height:1.7}}
header{{background:#0a7c4e;padding:18px 24px}}
header a{{color:#fff;text-decoration:none;font-weight:700;font-size:1.3rem}}
.container{{max-width:860px;margin:0 auto;padding:32px 20px}}
h1{{font-size:2rem;color:#0a7c4e;margin-bottom:16px}}
.lead{{font-size:1.1rem;margin-bottom:28px;color:#444}}
h2{{font-size:1.4rem;color:#0a7c4e;margin:28px 0 10px}}
p{{margin-bottom:16px}}
.faq{{background:#fff;border-left:4px solid #0a7c4e;padding:16px 20px;margin:14px 0;border-radius:4px}}
.faq strong{{display:block;margin-bottom:6px}}
.cta{{background:#0a7c4e;color:#fff;padding:28px;text-align:center;border-radius:8px;margin-top:40px}}
.cta a{{color:#fff;font-weight:700;text-decoration:underline}}
footer{{text-align:center;padding:24px;font-size:.85rem;color:#777}}
</style>
</head>
<body>
<header><a href="https://produtovivo.com.br">ProdutoVivo</a></header>
<div class="container">
<h1>{h1}</h1>
<p class="lead">{lead}</p>
{sections}
<h2>Perguntas Frequentes</h2>
{faqs}
<div class="cta">
<p>Quer aprender a vender infoprodutos digitais e construir renda recorrente?</p>
<p><a href="https://produtovivo.com.br">Conheça o ProdutoVivo — o guia completo para infoprodutores brasileiros.</a></p>
</div>
</div>
<footer>&copy; 2025 ProdutoVivo. Todos os direitos reservados.</footer>
</body>
</html>"""


def art(slug, title, desc, h1, lead, sections, faq_list):
    url    = f"{DOMAIN}/blog/{slug}/"
    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faq_list
        ]
    }, ensure_ascii=False)
    sec_html = ""
    for heading, body in sections:
        sec_html += f"<h2>{heading}</h2>\n<p>{body}</p>\n"
    faq_html = ""
    for q, a in faq_list:
        faq_html += f'<div class="faq"><strong>{q}</strong>{a}</div>\n'
    html = TMPL.format(title=title, desc=desc, url=url, pixel=PIXEL,
                       schema=schema, h1=h1, lead=lead,
                       sections=sec_html, faqs=faq_html)
    out = pathlib.Path(BASE) / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"  {slug}")


# ── Article 5503 — B2B SaaS: Plataformas de Vídeo e Webinar Corporativo ──
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-plataformas-de-video-e-webinar-corporativo",
    title="Gestão de Negócios para Empresas de B2B SaaS de Plataformas de Vídeo e Webinar | ProdutoVivo",
    desc="Estratégias de gestão para empresas B2B SaaS de vídeo corporativo e webinar: crescimento, diferenciação e mercado. Guia para infoprodutores.",
    h1="Gestão de Negócios para Empresas de B2B SaaS de Plataformas de Vídeo e Webinar Corporativo",
    lead="Plataformas de vídeo corporativo e webinar são infraestrutura essencial de comunicação, treinamento e marketing no mundo pós-pandemia. Para infoprodutores que atuam no mercado de comunicação corporativa e educação empresarial, entender como essas empresas crescem e se diferenciam é oportunidade de conteúdo de alto valor.",
    sections=[
        ("O Mercado de Vídeo Corporativo e Webinar SaaS",
         "O vídeo se tornou o formato dominante de comunicação corporativa: treinamentos, all-hands, webinars de geração de leads, demonstrações de produto, onboarding de clientes e comunicação interna passaram a ter o vídeo como canal primário. O mercado de SaaS para vídeo corporativo inclui plataformas de webinar (Zoom Webinars, Hopin, ON24, RD Station), plataformas de vídeo sob demanda (Vimeo Business, Kaltura, Panopto), ferramentas de gravação e edição assíncrona (Loom, Vidyard) e plataformas de eventos virtuais e híbridos. O Brasil tem mercado expressivo impulsionado pela adoção corporativa de formatos de vídeo como canal de comunicação primário."),
        ("Diferenciação: Ao Vivo, Assíncrono e Análise de Engajamento",
         "A diferenciação em vídeo corporativo SaaS ocorre em três eixos: ao vivo (webinar, live streaming com interatividade — Q&A, polls, breakout rooms), assíncrono (vídeo gravado compartilhável com análise de visualização por capítulo e usuario) e analytics de engajamento (quem assistiu quanto, onde pausou, quais slides foram revistos). Plataformas que oferecem os três eixos integrados com CRM e ferramentas de marketing automation criam proposição de valor completa para times de marketing e vendas que usam vídeo como canal de geração de pipeline."),
        ("Go-to-Market: Marketing, Vendas e L&D como Compradores",
         "O comprador de plataforma de webinar varia: times de marketing (geração de leads via webinar), equipes de vendas (demos personalizadas, sales enablement via vídeo), L&D e T&D corporativo (treinamentos escaláveis via vídeo), e comunicação interna (all-hands assíncronos). Cada perfil tem critérios distintos de avaliação. Plataformas que dominam um segmento com profundidade (ex: webinar B2B para geração de leads) e expandem para outros usos na mesma empresa têm maior NRR. Demos ao vivo que demonstram a experiência do apresentador e do participante simultaneamente são o melhor argumento de venda no setor."),
        ("Integração e Ecossistema de Martech",
         "Plataformas de webinar e vídeo B2B criam valor máximo integradas ao ecossistema de martech: CRM (capturar leads e atualizar status de engajamento automaticamente), marketing automation (nurturing pós-webinar baseado em comportamento durante o evento), ferramentas de BI (análise de performance de webinars por segmento e campanha) e plataformas de LMS (hospedar treinamentos gravados integrados ao catálogo de aprendizado). APIs abertas e marketplace de integrações nativas são diferencial competitivo que reduz a fricção de adoção em empresas com stacks de martech já consolidados."),
        ("Tendências: IA em Vídeo, Eventos Híbridos e Personalização",
         "IA transforma a produção e o consumo de vídeo corporativo: transcrição automática e geração de legendas em tempo real, criação de cortes inteligentes de long-form para shorts, tradução automática de conteúdo para múltiplos idiomas, e personalização de vídeo em escala (cada espectador recebe versão personalizada com seu nome e empresa). Eventos híbridos — que combinam participação presencial e virtual com igual experiência para ambos os públicos — são o padrão emergente em grandes eventos corporativos. Plataformas que facilitam essa produção híbrida com baixo custo operacional capturam mercado crescente."),
    ],
    faq_list=[
        ("Qual a diferença entre webinar e videoconferência?",
         "Videoconferência é comunicação bidirecional entre múltiplos participantes (Zoom, Teams, Meet) — todos podem falar e ser vistos. Webinar é transmissão geralmente unidirecional: apresentadores falam para audiência maior (centenas ou milhares de participantes) com interatividade controlada via chat, Q&A e polls. Webinars são ideais para eventos de marketing, treinamentos em larga escala e lançamentos de produto; videoconferências para reuniões colaborativas."),
        ("Como calcular ROI de webinars de geração de leads?",
         "Meça: custo total do webinar (plataforma + produção + horas da equipe) dividido pelos leads qualificados gerados. Compare com o CPL (custo por lead) de outros canais. Adicione a taxa de conversão de leads de webinar para oportunidade e para cliente — webinar leads tipicamente convertem 20-40% melhor que leads de formulário simples porque chegam mais educados. Esse cálculo justifica investimento em plataforma e produção de qualidade para times de marketing orientados a resultados."),
        ("Vídeo assíncrono é melhor que reunião ao vivo para vendas B2B?",
         "Depende do estágio e do objetivo. Vídeo assíncrono (Loom) é excelente para prospecção personalizada (taxa de abertura 3-5x maior que e-mail de texto), follow-up pós-reunião e recapitulação de propostas. Reunião ao vivo é insubstituível para demo consultiva, negociação e construção de relacionamento. A combinação estratégica das duas modalidades ao longo do ciclo de vendas maximiza eficiência e personalização."),
    ]
)

# ── Article 5504 — Clinic: Medicina Tropical e Parasitologia Clínica ──
art(
    slug="gestao-de-clinicas-de-medicina-tropical-e-parasitologia-clinica",
    title="Gestão de Clínicas de Medicina Tropical e Parasitologia Clínica | ProdutoVivo",
    desc="Guia de gestão para clínicas de medicina tropical e parasitologia clínica: modelo assistencial, epidemiologia, financiamento e crescimento no Brasil. Para infoprodutores da saúde.",
    h1="Gestão de Clínicas de Medicina Tropical e Parasitologia Clínica",
    lead="A medicina tropical e a parasitologia clínica são especialidades de relevância estratégica no Brasil, país com ampla diversidade de ecossistemas e doenças parasitárias endêmicas. Para infoprodutores da saúde, entender a gestão dessas clínicas significa explorar um nicho com forte componente de saúde pública e crescente demanda por serviços privados especializados.",
    sections=[
        ("A Medicina Tropical no Contexto Brasileiro",
         "O Brasil concentra algumas das maiores cargas de doenças tropicais do mundo: leishmaniose, dengue, malária (especialmente na Amazônia), doença de Chagas, esquistossomose, toxoplasmose, ancilostomíase e infecções por helmintos intestinais. A medicina tropical abrange diagnóstico, tratamento e acompanhamento dessas condições, além de aconselhamento a viajantes que se deslocam para regiões endêmicas. A parasitologia clínica se dedica especificamente ao diagnóstico laboratorial e ao manejo de infecções parasitárias, complementando o trabalho do infectologista e do médico de medicina tropical."),
        ("Perfis de Pacientes e Serviços Especializados",
         "As clínicas de medicina tropical atendem perfis distintos: moradores de regiões endêmicas encaminhados de UBSs e hospitais públicos, trabalhadores de setores de risco (mineração, agronegócio, construção em regiões remotas), turistas nacionais e internacionais que visitaram áreas endêmicas, imigrantes e refugiados de países com alta carga parasitária, e pacientes imunossuprimidos (HIV, transplantados, em quimioterapia) com maior risco de parasitoses oportunistas. Clínicas de medicina do viajante oferecem vacinação internacional, quimioprofilaxia antimalárica e orientações pré-viagem — serviço de alto ticket e crescente demanda com a retomada do turismo global."),
        ("Diagnóstico Laboratorial e Parcerias Estratégicas",
         "O diagnóstico em parasitologia exige metodologias específicas: exame parasitológico de fezes (EPF) com técnicas de concentração (Hoffman, Ritchie), esfregaços sanguíneos e gota espessa para malária, sorologia para leishmaniose e doença de Chagas (ELISA, RIFI, Western blot), biópsia de pele para diagnóstico de leishmaniose tegumentar, e PCR para confirmação e genotipagem em casos complexos. Parcerias com laboratórios de referência — Fiocruz, Instituto Adolfo Lutz, laboratórios universitários — são essenciais para exames de alta complexidade que a clínica não realiza internamente."),
        ("Modelo de Negócio e Financiamento",
         "Clínicas de medicina tropical operam em modelo misto: atendimento a convênios (com tabela frequentemente inadequada para a complexidade diagnóstica), medicina do viajante como serviço predominantemente particular (vacinação, profilaxia, consultas pré e pós-viagem), e parcerias com empresas do setor primário (mineradoras, construtoras, agronegócio) que têm trabalhadores expostos a doenças tropicais e precisam de protocolo de saúde ocupacional especializado. Esse último segmento oferece contratos corporativos recorrentes com ticket elevado — o principal driver de crescimento sustentável nesse nicho."),
        ("Pesquisa, Ensino e Posicionamento como Referência",
         "Clínicas de medicina tropical que se associam a universidades e instituições de pesquisa — participando de estudos clínicos, desenvolvendo protocolos diagnósticos e formando residentes e especialistas — constroem posição única de referência que atrai casos raros e complexos de toda a região. A publicação científica e a participação em congressos de infectologia tropical (SBT, ASTMH) ampliam a visibilidade entre pares e médicos encaminhadores. Infoprodutores que abordam a interseção de saúde pública e medicina privada no contexto das doenças tropicais brasileiras têm audiência cativa entre profissionais e acadêmicos da área."),
    ],
    faq_list=[
        ("Leishmaniose tem cura?",
         "Sim. Tanto a leishmaniose visceral (Calazar) quanto a leishmaniose tegumentar têm tratamento disponível. O antimonial pentavalente (Glucantime) é o tratamento de primeira linha para a maioria das formas, com anfotericina B lipossomal como alternativa especialmente para leishmaniose visceral. O tratamento precoce é fundamental — leishmaniose visceral não tratada tem alta mortalidade. A resposta ao tratamento e a necessidade de retratamento são monitoradas pelo médico especialista."),
        ("Quem deve fazer profilaxia contra malária ao viajar para a Amazônia?",
         "A profilaxia é indicada para viajantes sem imunidade prévia que visitarão áreas de transmissão ativa de malária na Amazônia — especialmente em zonas rurais e de mata. O esquema recomendado varia por área de destino (Plasmodium vivax predominante vs. P. falciparum). A cloroquina é usada para regiões sem P. falciparum resistente; mefloquina, doxiciclina ou atovaquona-proguanil para áreas com P. falciparum. A consulta ao médico de medicina do viajante ao menos 4-6 semanas antes da viagem é fundamental."),
        ("Como abrir uma clínica de medicina do viajante no Brasil?",
         "Exige médico com conhecimento em medicina tropical e vacinas internacionais, habilitação no Centro de Referência em Saúde do Viajante (opcional, mas valorizado), estoque de vacinas e medicamentos profiláticos com cadeia de frio adequada, credenciamento no Sistema de Vigilância em Saúde do Viajante e, idealmente, parcerias com operadoras de turismo e empresas que enviam funcionários ao exterior."),
    ]
)

# ── Article 5505 — SaaS Sales: Distribuidoras e Atacadistas ──
art(
    slug="vendas-para-o-setor-de-saas-de-distribuidoras-e-atacadistas",
    title="Vendas para o Setor de SaaS de Distribuidoras e Atacadistas | ProdutoVivo",
    desc="Como vender SaaS para distribuidoras e atacadistas no Brasil: tomadores de decisão, dores operacionais, abordagem e estratégias de crescimento. Guia para infoprodutores.",
    h1="Vendas para o Setor de SaaS de Distribuidoras e Atacadistas",
    lead="Distribuidoras e atacadistas movimentam bilhões diariamente na economia brasileira, conectando indústrias a varejistas e consumidores. Para infoprodutores e consultores de vendas B2B SaaS, esse segmento combina volume expressivo com dores operacionais urgentes e crescente abertura à digitalização.",
    sections=[
        ("O Mercado de Distribuição e Atacado no Brasil",
         "O Brasil tem mais de 150 mil empresas atacadistas e distribuidoras, desde gigantes nacionais como Martins e Grupo GPS até milhares de distribuidores regionais de alimentos, bebidas, higiene e limpeza, material de construção e produtos farmacêuticos. O setor é intensivo em operações: alto volume de SKUs, roteirização de entregas, crédito a prazo para varejistas, gestão de representantes e equipes de vendas externas, controle rigoroso de estoque e gestão de devoluções e quebras. A digitalização dessas operações é urgente — empresas que operam com ERP desatualizado ou planilhas perdem eficiência e competitividade rapidamente."),
        ("Dores Operacionais e Soluções SaaS",
         "As principais dores de distribuidoras e atacadistas para SaaS resolver incluem: roteirização inteligente de entregas (reduzir custo logístico de 3-8% da receita), gestão de pedidos de representantes via app mobile (substituir papel e planilha no campo), controle de crédito de clientes com análise de risco automatizada, integração fiscal para NF-e com alto volume (centenas a milhares por dia), gestão de contratos e negociações com indústrias fornecedoras, análise de sell-in vs. sell-out e controle de sell-through de produtos, e dashboards de performance por região, produto e representante. O ROI de sistemas bem implementados em distribuidoras é frequentemente de 6-18 meses."),
        ("Tomadores de Decisão e Processo de Venda",
         "Em distribuidoras de médio porte, o CEO ou diretor financeiro lidera a decisão de tecnologia, com influência do gerente de TI ou do gestor de operações. Em grandes grupos de distribuição, TI tem papel central com processo formal de RFP. O ciclo de vendas varia de 2-4 meses para PMEs a 6-12 meses para grandes grupos. Demonstrações que simulam a operação real da distribuidora — roteirização de uma rota com 50 entregas, pedido via app do representante em campo, emissão de NF-e em massa — são muito mais convincentes que slides de funcionalidades."),
        ("Estratégias de Penetração e Crescimento no Setor",
         "Associações setoriais como ABAD (Associação Brasileira de Atacadistas e Distribuidores) e ADASP (associações estaduais) são canais de acesso à base de empresas. Parcerias com fornecedores de equipamentos de coleta de dados (coletores, tablets, impressoras térmicas) que recomendam o software criam canal indireto eficiente. Presença em feiras como APAS Show (alimentos e bebidas), FEIPLAR e eventos regionais de distribuição gera leads qualificados. Conteúdo sobre gestão de distribuidoras — roteirização, crédito, sell-through — atrai decisores via SEO."),
        ("Tendências: DMS, Força de Vendas Mobile e Integração com Indústrias",
         "DMS (Distributor Management System) integra pedidos, estoque, logística e financeiro numa visão única da operação de distribuição. Força de vendas mobile com app para representantes — pedido, consulta de estoque, histórico de cliente e cobrança integrados no celular — é o módulo de maior adoção imediata. Integração EDI com indústrias fornecedoras (para pedidos, notas fiscais e conciliação de pagamentos) e com grandes varejistas clientes cria eficiência de troca de informações e reduz erros. Distribuidoras que adotam analytics de sell-through e forecast de demanda por produto e região se tornam parceiros estratégicos das indústrias que representam."),
    ],
    faq_list=[
        ("ERP e DMS são a mesma coisa para distribuidoras?",
         "Não exatamente. ERP (Enterprise Resource Planning) é o sistema de gestão integrada de toda a empresa — financeiro, contábil, RH, estoque. DMS (Distributor Management System) é focado especificamente nas operações de distribuição: gestão de pedidos no campo, roteirização, controle de entregas, gestão de representantes e análise de sell-through. Distribuidoras de médio e grande porte idealmente têm os dois integrados; menores frequentemente adotam um DMS que também cobre funções básicas de ERP."),
        ("Quanto custa implementar ERP em distribuidora de médio porte?",
         "Sistemas como TOTVS, Senior e ERPs verticais para distribuição custam de R$1.500 a R$8.000/mês de licença, mais serviços de implementação de R$50k a R$300k dependendo da complexidade. O prazo de implementação varia de 3 a 12 meses. O ROI vem de redução de erros de faturamento, melhor controle de estoque (redução de quebras e faltas), roteirização mais eficiente e maior produtividade da equipe comercial."),
        ("App de força de vendas é diferente de CRM?",
         "Sim, embora se complementem. App de força de vendas mobile foca na operação de campo: tirar pedido, consultar estoque em tempo real, registrar visita, cobrar pendências, imprimir cupom. CRM foca no relacionamento: histórico de interações, oportunidades, pipeline de vendas e análise de performance por conta. Distribuidoras maiores usam ambos integrados; menores frequentemente precisam mais do app de pedidos do que de CRM completo."),
    ]
)

# ── Article 5506 — Consulting: Gestão de Ecossistemas Digitais e Plataformas ──
art(
    slug="consultoria-de-gestao-de-ecossistemas-digitais-e-plataformas-de-negocio",
    title="Consultoria de Gestão de Ecossistemas Digitais e Plataformas de Negócio | ProdutoVivo",
    desc="Como estruturar consultoria de gestão de ecossistemas digitais e plataformas de negócio: estratégia, modelos, aplicações e mercado. Guia para infoprodutores e consultores.",
    h1="Consultoria de Gestão de Ecossistemas Digitais e Plataformas de Negócio",
    lead="A economia de plataformas transformou os modelos de negócio globais — de Apple à Mercado Livre, de Uber ao iFood. Para infoprodutores e consultores estratégicos, a gestão de ecossistemas digitais e plataformas de negócio é um dos temas mais sofisticados e demandados no ambiente corporativo contemporâneo.",
    sections=[
        ("A Economia de Plataformas e seus Fundamentos",
         "Plataformas de negócio conectam dois ou mais grupos de usuários distintos, criando valor pela interação entre eles — o que economistas chamam de mercados de múltiplos lados (multi-sided markets). Amazon conecta vendedores e compradores; Airbnb conecta anfitriões e hóspedes; Mercado Livre conecta vendedores e compradores brasileiros. O diferencial das plataformas é o efeito de rede: quanto mais usuários em um lado, mais valor para o outro lado, criando ciclos virtuosos de crescimento que se auto-reforçam. Entender como projetar, lançar e escalar uma plataforma é competência estratégica de alto valor."),
        ("Estratégia de Ecossistema: Da Plataforma ao Ecossistema",
         "Empresas maduras vão além de plataformas para construir ecossistemas — redes de parceiros, APIs, complementadores e fornecedores que ampliam o valor entregue ao cliente central. Apple criou ecossistema em torno do iPhone: desenvolvedores de apps, acessórios, serviços (iCloud, Apple Pay, Apple Music) e hardware complementar. O consultor de ecossistemas digitais ajuda empresas a identificar o modelo mais adequado (pipeline vs. plataforma vs. ecossistema), mapear quem são os players do ecossistema e como orquestrá-los, e definir as regras de governança que equilibram abertura com controle."),
        ("Aplicação em Empresas Tradicionais: Plataformização",
         "Empresas tradicionais que não nasceram digitais enfrentam o desafio de plataformizar seus negócios sem destruir o modelo existente. Distribuidoras que criam marketplace B2B para conectar indústrias e varejistas, redes de franquias que constroem plataformas de serviços para franqueados e seus clientes, e indústrias que desenvolvem ecosistemas de parceiros integradores são exemplos de plataformização em curso no Brasil. O consultor de ecossistemas guia a estratégia de abertura de APIs, definição de parcerias-chave e design das regras de participação que atraem os complementadores certos."),
        ("Métricas de Saúde de Plataformas e Ecossistemas",
         "Plataformas saudáveis são medidas por métricas distintas das empresas lineares tradicionais: Gross Merchandise Value (GMV) — volume transacionado pela plataforma, rake/take rate — percentual de valor capturado em cada transação, liquidez — percentual de usuários ativos que encontram o que buscam, NPS de ambos os lados do mercado, tempo para primeiro valor (time-to-first-value) de novos parceiros, e Net Revenue Retention da base de parceiros ativos. O consultor que domina essas métricas fala a língua dos investidores e da liderança executiva de empresas de plataforma."),
        ("Regulação, Governança e o Futuro dos Ecossistemas",
         "A crescente regulação de grandes plataformas — Digital Markets Act na Europa, regulações antitruste nos EUA e marcos regulatórios de plataformas em discussão no Brasil — cria demanda por expertise em governança de plataformas e compliance com regulações de mercados digitais. Empresas de todos os portes que operam modelos de plataforma precisam de orientação sobre estruturação de contratos com parceiros, políticas de moderação de conteúdo, compliance antitruste e gestão de dados de usuários segundo LGPD/GDPR. Infoprodutores que antecipam e educam sobre essas tendências regulatórias têm audiência crescente em um dos temas mais quentes do direito digital e da estratégia empresarial."),
    ],
    faq_list=[
        ("Qual a diferença entre pipeline e plataforma?",
         "Um negócio pipeline cria valor linearmente: compra insumo → transforma → vende produto. A empresa controla toda a cadeia de valor. Uma plataforma cria valor facilitando interações entre grupos externos — não produz o produto/serviço ela mesma, mas orquestra quem o produz e quem o consome. A principal diferença é que plataformas podem escalar sem aumentar custos proporcionalmente, enquanto pipelines têm custos crescendo com a receita."),
        ("Como uma empresa pode começar a construir um ecossistema digital?",
         "Comece identificando qual problema seu cliente tem que você não resolve sozinho, mas que parceiros poderiam resolver em complementação ao seu produto. Abra APIs para parceiros desenvolverem integrações, crie programa de parceiros com incentivos claros (margem, certificação, leads), e governe a qualidade das integrações para proteger a experiência do cliente. O ecossistema começa pequeno — 5-10 parceiros estratégicos — e escala com o volume de clientes que valorizam as integrações."),
        ("Efeito de rede e efeito viral são a mesma coisa?",
         "Não. Efeito de rede ocorre quando o valor do produto aumenta para cada usuário à medida que mais pessoas usam — clássico em plataformas como WhatsApp e marketplaces. Efeito viral é um mecanismo de crescimento: usuários convidam outros de forma orgânica, acelerando a aquisição. Uma plataforma pode ter efeito de rede sem crescimento viral (base de usuários que não convida), e pode ter crescimento viral sem efeito de rede (produto que cresce por indicação mas não fica mais valioso com mais usuários)."),
    ]
)

# ── Article 5507 — B2B SaaS: IT Service Management e ITSM ──
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-it-service-management-e-itsm",
    title="Gestão de Negócios para Empresas de B2B SaaS de IT Service Management (ITSM) | ProdutoVivo",
    desc="Estratégias de gestão para empresas B2B SaaS de ITSM e IT Service Management: crescimento, diferenciação e mercado. Guia para infoprodutores.",
    h1="Gestão de Negócios para Empresas de B2B SaaS de IT Service Management (ITSM)",
    lead="Plataformas de IT Service Management (ITSM) são a espinha dorsal operacional das equipes de TI corporativas. Para infoprodutores que atendem o mercado de TI e operações, entender como empresas nesse espaço crescem e competem é essencial para criar conteúdos que ressoam com decisores técnicos e executivos.",
    sections=[
        ("O Mercado de ITSM e a Relevância do Gerenciamento de Serviços",
         "IT Service Management (ITSM) é o conjunto de práticas para projetar, entregar, gerenciar e melhorar serviços de TI para os usuários finais da organização. O framework ITIL (Information Technology Infrastructure Library) é a referência global de melhores práticas de ITSM, com versões adotadas por organizações no mundo todo. Plataformas SaaS de ITSM automatizam processos críticos: gestão de incidentes (restaurar serviço rapidamente), gestão de problemas (identificar e eliminar a causa-raiz), gestão de mudanças (implementar alterações controladas), gestão de ativos de TI e service desk. O mercado global de ITSM software supera US$8 bilhões e inclui ServiceNow, Jira Service Management e Freshservice."),
        ("Diferenciação: Enterprise vs. Mid-Market vs. SMB",
         "O mercado de ITSM é fortemente segmentado por porte de cliente. Enterprise (ServiceNow): plataforma de gestão de serviços corporativos com automação avançada, AI Ops e extensão para serviços não-TI (HR, financeiro, jurídico). Mid-market (Jira Service Management, Freshservice): funcionalidade robusta com implementação mais rápida e preço acessível. SMB: soluções simples de service desk com onboarding em horas, suporte básico de incidentes e SLA. Novos entrantes se diferenciam por experiência superior de usuário final, IA embarcada para classificação e roteamento automático de tickets, e integração nativa com ferramentas de DevOps para ITSM enterprise-grade."),
        ("ITIL, DevOps e a Convergência de ITSM com SRE",
         "A convergência de ITSM com práticas DevOps e SRE (Site Reliability Engineering) é a tendência mais importante do setor. Equipes que antes separavam operações (ITSM) de desenvolvimento (DevOps) agora compartilham ferramentas, práticas e responsabilidades. Plataformas que integram fluxo de mudanças com CI/CD pipelines, conectam incidentes a repositórios de código e facilitam post-mortems colaborativos capturam o mercado crescente de equipes DevOps maduras. O conceito de Platform Engineering — criar plataformas internas de self-service para desenvolvedores — é a evolução natural que amplia o TAM do ITSM tradicional."),
        ("Go-to-Market: CIOs, IT Directors e Service Desk Managers",
         "Compradores de ITSM são técnicos que precisam de aprovação executiva: IT Directors e Service Desk Managers lideram a avaliação técnica, CIOs e CFOs aprovam o orçamento. A jornada de compra começa frequentemente com frustração do service desk com ferramenta legada (péssima UX, falta de automação, relatórios inadequados). Trials gratuitos com demo pré-configurada que simula o ambiente real do prospect — com base de conhecimento, SLAs e fluxos de aprovação preconfigurados — reduzem drasticamente o tempo de avaliação e aumentam conversão."),
        ("Tendências: AIOps, ESM e Self-Healing IT",
         "AIOps (AI for IT Operations) usa machine learning para correlacionar eventos, detectar anomalias e recomendar ações antes que incidentes impactem usuários. Enterprise Service Management (ESM) expande ITSM para outros departamentos — RH, financeiro, jurídico, facilities — usando a mesma plataforma e práticas de gestão de serviços. Self-healing IT — sistemas que detectam e corrigem problemas automaticamente sem intervenção humana — é o frontier mais avançado, impulsionado por AIOps e automação de remediação. Plataformas que incorporam essas capacidades têm argumento de futuro poderoso para renovação e expansão de contratos existentes."),
    ],
    faq_list=[
        ("Qual a diferença entre ITSM e helpdesk?",
         "Helpdesk é um componente do ITSM — o canal de suporte aos usuários para reportar problemas e solicitar serviços. ITSM é o framework completo que inclui helpdesk mais gestão de incidentes, problemas, mudanças, ativos, configuração e muito mais. Uma empresa pode ter helpdesk sem ITSM estruturado; ITSM maduro sempre inclui helpdesk como peça central."),
        ("ITIL ainda é relevante com DevOps e metodologias ágeis?",
         "Sim, mas evoluiu. O ITIL 4 (versão atual) foi reformulado para integrar práticas ágeis, DevOps e lean. Não é mais um framework prescritivo de processos, mas um guia de práticas que as organizações adaptam ao seu contexto. A combinação de ITIL com DevOps é mais eficiente que qualquer um dos dois isoladamente — ITIL traz governança e gestão de serviços; DevOps traz velocidade e feedback contínuo."),
        ("ServiceNow é a única opção para enterprise ITSM?",
         "Não. Jira Service Management, Freshservice, BMC Helix, Cherwell e Ivanti são alternativas robustas para enterprise. ServiceNow domina o segmento de grandes corporações com necessidades complexas de automação cross-departamental. Para empresas de médio porte que precisam de ITSM enterprise-grade sem o custo e a complexidade do ServiceNow, há alternativas com excelente custo-benefício."),
    ]
)

# ── Article 5508 — Clinic: Endocrinologia Pediátrica e Diabetes Infanto-Juvenil ──
art(
    slug="gestao-de-clinicas-de-endocrinologia-pediatrica-e-diabetes-infanto-juvenil",
    title="Gestão de Clínicas de Endocrinologia Pediátrica e Diabetes Infanto-Juvenil | ProdutoVivo",
    desc="Guia de gestão para clínicas de endocrinologia pediátrica e diabetes infanto-juvenil: modelo assistencial, tecnologia, financiamento e crescimento. Para infoprodutores da saúde.",
    h1="Gestão de Clínicas de Endocrinologia Pediátrica e Diabetes Infanto-Juvenil",
    lead="A endocrinologia pediátrica e o manejo do diabetes tipo 1 em crianças e adolescentes são áreas de alta complexidade assistencial e crescente demanda no Brasil. Para infoprodutores da saúde, entender a gestão dessas clínicas significa explorar um nicho com pacientes crônicos, alta recorrência e tecnologia de ponta.",
    sections=[
        ("A Endocrinologia Pediátrica e suas Especialidades",
         "A endocrinologia pediátrica abrange o diagnóstico e tratamento de distúrbios hormonais em crianças e adolescentes: diabetes mellitus tipo 1 (DM1), distúrbios do crescimento (baixa estatura, puberdade precoce ou tardia), hipotireoidismo e hipertireoidismo, obesidade infanto-juvenil, síndromes adrenais congênitas, disfunções hipofisárias e distúrbios do cálcio e fósforo. O DM1 é a condição mais prevalente e mais demandante de acompanhamento — pacientes precisam de consultas frequentes, ajustes de tratamento contínuos e suporte educacional intensivo para família e escola."),
        ("Gestão do Diabetes Tipo 1 em Crianças: Complexidade e Inovação",
         "O manejo do DM1 pediátrico exige abordagem multidisciplinar: endocrinologista pediátrico, nutricionista especializada em diabetes, enfermeiro educador em diabetes, psicólogo e assistente social. A tecnologia transformou o tratamento: sistemas de monitoramento contínuo de glicose (CGM) — FreeStyle Libre, Dexterity G7 — eliminam as picadas nos dedos e fornecem dados contínuos. Bombas de insulina com algoritmos de dose automática (loop fechado) e sistemas híbridos de pâncreas artificial representam o estado da arte, com adoção crescente no Brasil após redução de preços e maior cobertura de convênios."),
        ("Educação em Diabetes e Empoderamento de Famílias",
         "A educação em diabetes — ensinar a criança, os pais e a escola a gerenciar a condição no dia a dia — é tão importante quanto a prescrição médica. Grupos de educação em diabetes, escolas de diabetes (programas estruturados de capacitação), sessões individuais de ajuste de carboidratos e atividade física, e suporte em situações especiais (festas de aniversário, acampamentos, viagens) são componentes essenciais do cuidado. Clínicas que desenvolvem programas robustos de educação em diabetes reduzem internações por descompensação e melhoram dramatically a qualidade de vida dos pacientes e famílias."),
        ("Modelo de Negócio e Recorrência em Endocrinologia Pediátrica",
         "Endocrinologia pediátrica tem modelo de negócio com altíssima recorrência: pacientes com DM1 retornam a cada 3 meses durante toda a infância e adolescência. Distúrbios de crescimento e puberdade também têm seguimento prolongado. A fidelização natural da condição crônica cria fluxo de receita estável e previsível. O desafio é a cobertura limitada de alguns procedimentos e tecnologias (CGM, bombas de insulina) pelos planos de saúde — muitas famílias buscam suporte para pleitos junto às operadoras ou no Judiciário, criando demanda por clínicas que orientem nesse processo."),
        ("Tecnologia, Telemedicina e Suporte Contínuo",
         "A telemedicina é especialmente valiosa em endocrinologia pediátrica: consultas de ajuste de doses via teleconsulta reduzem deslocamentos e facilitam o seguimento frequente que DM1 exige. Plataformas digitais de compartilhamento de dados de CGM e bomba de insulina — onde paciente e médico visualizam os mesmos dados remotamente — transformam a consulta de rotina em sessão de análise de dados em tempo real. Grupos de WhatsApp para suporte rápido entre consultas e comunidades online de famílias com DM1 criam ecossistema de suporte que fideliza e diferencia a clínica no mercado."),
    ],
    faq_list=[
        ("Criança com diabetes tipo 1 pode ter vida normal?",
         "Sim. Com o manejo adequado — insulinoterapia otimizada, monitoramento contínuo de glicose e educação em diabetes — crianças com DM1 praticam esportes, frequentam escola e têm desenvolvimento normal. A tecnologia atual (CGM + bomba de insulina com loop fechado) permite controle glicêmico muito superior ao das décadas anteriores. O suporte multidisciplinar e a educação da criança e da família são fundamentais para autonomia progressiva no autocuidado."),
        ("Qual a diferença entre diabetes tipo 1 e tipo 2 na infância?",
         "DM1 é autoimune: o sistema imune destrói as células beta do pâncreas que produzem insulina — a criança fica totalmente dependente de insulina exógena. DM2 em crianças está crescendo associado à obesidade: há resistência à insulina e produção insuficiente, manejado inicialmente com estilo de vida e metformina. DM1 é muito mais comum em crianças e adolescentes; DM2 pediátrico, embora crescente, ainda é menos frequente que em adultos."),
        ("CGM (sensor de glicose) é coberto pelos planos de saúde?",
         "A cobertura de CGM pelos planos de saúde brasileiros avança gradualmente. A ANS incluiu o CGM na lista de procedimentos obrigatórios para DM1 em crianças em decisão recente, mas a implementação e a qualidade da cobertura variam por operadora. Muitas famílias obtêm cobertura via ação judicial. O custo dos sensores sem cobertura (R$200-400/sensor, substituído a cada 7-14 dias) é significativo para muitas famílias."),
    ]
)

# ── Article 5509 — SaaS Sales: Academias de Idiomas e Escolas de Cursos Livres ──
art(
    slug="vendas-para-o-setor-de-saas-de-academias-de-idiomas-e-escolas-de-cursos-livres",
    title="Vendas para o Setor de SaaS de Academias de Idiomas e Escolas de Cursos Livres | ProdutoVivo",
    desc="Como vender SaaS para academias de idiomas e escolas de cursos livres no Brasil: tomadores de decisão, dores operacionais e estratégias. Guia para infoprodutores.",
    h1="Vendas para o Setor de SaaS de Academias de Idiomas e Escolas de Cursos Livres",
    lead="O Brasil tem mais de 30 mil escolas de idiomas e centenas de milhares de escolas de cursos livres — de música a culinária, de informática a artes. Para infoprodutores e consultores de vendas B2B SaaS, esse segmento combina volume expressivo com necessidades de gestão bem definidas e sensibilidade ao preço mensurável.",
    sections=[
        ("O Mercado de Cursos Livres e Idiomas no Brasil",
         "O setor de cursos livres e extracurriculares movimenta mais de R$20 bilhões anuais no Brasil. Academias de idiomas lideram o segmento (inglês, espanhol, mandarim), seguidas por escolas de música, artes, dança, informática, gastronomia e cursos técnicos extracurriculares. O mercado inclui desde grandes redes como CCAA, CNA e Wizard até milhares de escolas independentes locais. Todas compartilham necessidades similares: gestão de matrículas, controle de mensalidades, comunicação com alunos e responsáveis, controle de frequência e relatórios de progresso."),
        ("Dores Operacionais e o Papel do SaaS",
         "As principais dores de academias e escolas de cursos livres incluem: controle de mensalidades com alta inadimplência (cobrar via boleto, Pix e cartão, automatizar lembretes de vencimento e negativação), gestão de matrículas e rematrículas (comunicação proativa para evitar perda de aluno), controle de presença e relatórios para pais e responsáveis, gestão de turmas e horários com múltiplos professores e salas, comunicação via app e WhatsApp, e relatórios financeiros consolidados para o gestor. Sistemas que automatizam esses fluxos liberam o gestor de tarefas operacionais e reduzem inadimplência em 20-40%."),
        ("Tomadores de Decisão e Ciclo de Compra",
         "Em escolas independentes, o dono ou sócio decide — muitas vezes é também professor ou instrutor principal. A abordagem deve ser direta, focada na economia de tempo e na redução de inadimplência: dois benefícios imediatos que toda escola de cursos livres valoriza. Em redes e franquias de idiomas, a decisão é centralizada na franqueadora, que define o sistema para toda a rede — um contrato master abre centenas de unidades. O ciclo de vendas é de 1-4 semanas para independentes e 2-6 meses para redes."),
        ("Canais de Vendas no Mercado de Educação Complementar",
         "Grupos de Facebook e WhatsApp de donos de escolas de idiomas e cursos livres são comunidades ativas com alta engajamento. Parcerias com associações como ACBEU, ABECC (Associação Brasileira de Escolas de Cursos Complementares) e câmaras de comércio locais abrem portas para a base de associadas. Conteúdo sobre gestão de academias — como reduzir inadimplência, como automatizar rematrículas, como fidelizar alunos — atrai decisores via SEO e YouTube. Indicações de clientes satisfeitos têm taxa de conversão muito alta nesse mercado onde reputação circula em comunidades locais."),
        ("Tendências: Híbrido, App do Aluno e Automação de CRM",
         "A pandemia acelerou a adoção de aulas híbridas (presencial + online) que veio para ficar em muitas escolas de idiomas. Plataformas que integram gestão presencial com LMS (material de apoio online, exercícios, progresso) criam diferencial permanente. App do aluno e dos responsáveis — com acesso a notas, frequência, comunicados e pagamentos — aumenta percepção de valor e reduz contato operacional do gestor. Automação de CRM para rematrícula — campanhas automáticas para alunos com risco de evasão identificados por queda de frequência — é funcionalidade de alto impacto financeiro direto para as escolas."),
    ],
    faq_list=[
        ("Qual o ticket médio de SaaS para academias de idiomas?",
         "Planos para escolas pequenas (até 200 alunos): R$100 a R$300/mês. Planos médios (200-1.000 alunos): R$300 a R$800/mês. Planos para redes ou escolas grandes (acima de 1.000 alunos): R$800 a R$2.500/mês. O argumento de venda mais poderoso é a redução de inadimplência: se o sistema reduzir a inadimplência de 8% para 4% numa escola com R$50k de mensalidade, são R$2.000/mês de receita recuperada — muito mais que o custo do sistema."),
        ("O sistema para academia de idiomas pode integrar com WhatsApp?",
         "Sim, e essa é uma das funcionalidades mais valorizadas no Brasil. Integração com WhatsApp Business API permite: lembretes automáticos de vencimento de mensalidade, confirmação de presença, comunicados da escola, notificação de avaliações e envio de relatório de progresso. Automação que antes ocupava horas da secretaria por semana passa a ser zero-touch, liberando a equipe para atendimento de qualidade."),
        ("Como convencer uma escola que já usa planilha a migrar para sistema?",
         "Pergunte: 'quantas horas sua secretaria gasta por semana só com cobranças e controle de mensalidades?' e 'qual sua taxa de inadimplência atual?'. Se a resposta for mais de 5 horas e acima de 5% de inadimplência, o ROI do sistema é imediato e concreto. Ofereça migração assistida, trial de 30 dias com suporte dedicado e garanta que a secretária será treinada — a resistência à mudança vem de quem vai usar o sistema no dia a dia, não apenas de quem paga."),
    ]
)

# ── Article 5510 — Consulting: Gestão de Capital Humano e People Analytics ──
art(
    slug="consultoria-de-gestao-de-capital-humano-e-people-analytics-avancado",
    title="Consultoria de Gestão de Capital Humano e People Analytics Avançado | ProdutoVivo",
    desc="Como estruturar consultoria de gestão de capital humano e people analytics: metodologias, aplicações, dados e precificação. Guia para infoprodutores e consultores.",
    h1="Consultoria de Gestão de Capital Humano e People Analytics Avançado",
    lead="A gestão de capital humano evoluiu de administração de pessoal para disciplina estratégica baseada em dados. Para infoprodutores e consultores de RH e pessoas, dominar people analytics e gestão de capital humano é a fronteira de um nicho com alta demanda corporativa e diferenciação clara no mercado.",
    sections=[
        ("Capital Humano como Vantagem Competitiva",
         "A tese de que pessoas são o principal ativo das organizações ganhou substância empírica: pesquisas mostram que empresas com práticas superiores de gestão de talentos têm desempenho financeiro consistentemente superior. Capital humano abrange não apenas a força de trabalho atual, mas o conhecimento, as competências, o engajamento e o potencial de desenvolvimento de cada colaborador. O consultor de capital humano ajuda organizações a quantificar e desenvolver esse ativo — medir o retorno sobre investimento em pessoas, identificar lacunas críticas de competência e construir pipelines de talentos alinhados à estratégia."),
        ("People Analytics: Da Intuição à Decisão Baseada em Dados",
         "People analytics é a aplicação de dados, análise estatística e modelos preditivos para melhorar decisões sobre pessoas. Vai muito além de dashboards de RH: inclui análise preditiva de turnover (identificar quem vai sair antes que aconteça), análise de desempenho com controle de variáveis (o que realmente diferencia colaboradores de alto desempenho dos demais), análise de diversidade e equidade salarial, ROI de programas de treinamento e redes organizacionais (ONA) que revelam quem são os conectores informais de conhecimento. Organizações que adotam people analytics tomam decisões de RH com a mesma rigorosidade que decisões financeiras."),
        ("Diagnóstico de Maturidade em Gestão de Capital Humano",
         "O diagnóstico de maturidade avalia em que nível a organização se encontra: operacional (RH como administração de pessoal), tático (RH com processos estruturados de R&S, T&D, avaliação), estratégico (RH alinhado à estratégia do negócio, com métricas de impacto) e preditivo (people analytics avançado, decisões de talento baseadas em modelos preditivos). O consultor posiciona a organização nessa escala e define o roadmap de evolução mais adequado ao contexto, maturidade e recursos disponíveis — evitando pular etapas que garantiriam base sólida para avanços futuros."),
        ("Aplicações de People Analytics em Diferentes Ciclos de Vida",
         "People analytics aplica-se em cada etapa do ciclo do colaborador: Atração (qual canal de recrutamento traz os melhores talentos em menor custo), Seleção (quais características predizem desempenho em cada função), Desenvolvimento (qual programa de treinamento gera maior impacto em performance mensurável), Retenção (quais fatores elevam o risco de saída voluntária), Remuneração (equidade salarial e competitividade de mercado) e Planejamento da Força de Trabalho (quais competências precisarão ser desenvolvidas ou contratadas para suportar a estratégia futura). A análise integrada across todos esses pontos cria visão sistêmica do capital humano."),
        ("Ética, Privacidade e Governança em People Analytics",
         "People analytics levanta questões éticas e legais importantes: dados de colaboradores são dados pessoais sensíveis protegidos pela LGPD. O tratamento deve ter base legal clara (contrato de trabalho, legítimo interesse, consentimento informado), finalidade específica e proporcional, e proteções técnicas adequadas. Análises que criam discriminação indireta — usando dados correlacionados com raça, gênero ou origem para decisões de contratação ou promoção — violam princípios de equidade e podem gerar passivos legais. O consultor ético orienta sobre o uso responsável de people analytics, equilibrando insights de negócio com respeito aos direitos dos colaboradores."),
    ],
    faq_list=[
        ("People analytics precisa de um cientista de dados especializado?",
         "Não necessariamente para os usos mais comuns. Dashboards de RH avançados, análise de turnover por cohorte e pesquisas de engajamento com análise de texto podem ser conduzidos por profissionais de RH com treinamento em ferramentas como Power BI, Tableau e Python básico. Para modelos preditivos complexos e análises estatísticas avançadas, a parceria com um analista ou cientista de dados é recomendada. O mais importante é a mentalidade orientada a dados — fazer as perguntas certas e interpretar resultados com rigor."),
        ("Como apresentar insights de people analytics para a liderança executiva?",
         "Traduzir dados de RH para linguagem de negócio: 'o custo de turnover do nosso time de vendas foi de R$2,4M no último ano — equivale a 15% da nossa receita de vendas'. Apresente em dashboards executivos simples (máximo 5 métricas por página), foque no impacto financeiro e estratégico, e venha com recomendações acionáveis, não apenas com análises descritivas. Lideranças respondem bem a dados que mostram ROI de decisões de pessoas com a mesma clareza de decisões de investimento."),
        ("Quanto tempo leva para implementar um programa de people analytics?",
         "Depende da maturidade de dados disponíveis. Com dados estruturados de HCM (admissões, desempenho, treinamentos, turnover), é possível ter primeiros insights em 4-8 semanas. Um programa completo com modelos preditivos de turnover, análise de desempenho e planejamento da força de trabalho leva 3-6 meses para implementação inicial e 12-18 meses para maturidade operacional. A governança de dados de pessoas é frequentemente o principal gargalo — investir nela é pré-requisito para people analytics de qualidade."),
    ]
)

# ── Sitemap update ──
sm_path = pathlib.Path(__file__).parent / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")
new_urls = ""
for slug in [
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-plataformas-de-video-e-webinar-corporativo",
    "gestao-de-clinicas-de-medicina-tropical-e-parasitologia-clinica",
    "vendas-para-o-setor-de-saas-de-distribuidoras-e-atacadistas",
    "consultoria-de-gestao-de-ecossistemas-digitais-e-plataformas-de-negocio",
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-it-service-management-e-itsm",
    "gestao-de-clinicas-de-endocrinologia-pediatrica-e-diabetes-infanto-juvenil",
    "vendas-para-o-setor-de-saas-de-academias-de-idiomas-e-escolas-de-cursos-livres",
    "consultoria-de-gestao-de-capital-humano-e-people-analytics-avancado",
]:
    new_urls += f"\n  <url><loc>{DOMAIN}/blog/{slug}/</loc></url>"
sm_path.write_text(sm.replace("</urlset>", new_urls + "\n</urlset>"), encoding="utf-8")

# ── Trilha update ──
tr_path = pathlib.Path(__file__).parent / "trilha.html"
tr = tr_path.read_text(encoding="utf-8")
new_items = ""
for slug, label in [
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-plataformas-de-video-e-webinar-corporativo", "Plataformas de Vídeo e Webinar Corporativo SaaS"),
    ("gestao-de-clinicas-de-medicina-tropical-e-parasitologia-clinica", "Medicina Tropical e Parasitologia Clínica"),
    ("vendas-para-o-setor-de-saas-de-distribuidoras-e-atacadistas", "Distribuidoras e Atacadistas SaaS"),
    ("consultoria-de-gestao-de-ecossistemas-digitais-e-plataformas-de-negocio", "Gestão de Ecossistemas Digitais e Plataformas de Negócio"),
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-it-service-management-e-itsm", "IT Service Management e ITSM SaaS"),
    ("gestao-de-clinicas-de-endocrinologia-pediatrica-e-diabetes-infanto-juvenil", "Endocrinologia Pediátrica e Diabetes Infanto-Juvenil"),
    ("vendas-para-o-setor-de-saas-de-academias-de-idiomas-e-escolas-de-cursos-livres", "Academias de Idiomas e Escolas de Cursos Livres SaaS"),
    ("consultoria-de-gestao-de-capital-humano-e-people-analytics-avancado", "Gestão de Capital Humano e People Analytics Avançado"),
]:
    new_items += f'\n    <li><a href="{DOMAIN}/blog/{slug}/">{label}</a></li>'
tr_path.write_text(tr.replace("</ul>", new_items + "\n  </ul>", 1), encoding="utf-8")

print("Done — batch 2010")
