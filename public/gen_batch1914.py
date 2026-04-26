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


# ── Batch 1914 — articles 5311–5318 ──────────────────────────────────────────

# 5311 — B2B SaaS: LIMS e gestão de laboratórios
art(
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-lims-e-gestao-de-laboratorios",
    "Gestão de Negócios de Empresa de B2B SaaS de LIMS e Gestão de Laboratórios | ProdutoVivo",
    "Como construir e escalar um B2B SaaS de LIMS e gestão de laboratórios: oportunidades, produto, go-to-market e crescimento no mercado laboratorial brasileiro.",
    "Gestão de Negócios de Empresa de B2B SaaS de LIMS e Gestão de Laboratórios",
    "Laboratórios de análises clínicas, industriais e de pesquisa precisam de LIMS moderno. Descubra como construir um SaaS lucrativo nesse mercado especializado.",
    [
        ("O Mercado de LIMS no Brasil",
         "Laboratory Information Management Systems (LIMS) são sistemas especializados para gestão de amostras, resultados, laudos e rastreabilidade em laboratórios. O Brasil tem mais de 10.000 laboratórios de análises clínicas, além de laboratórios industriais (alimentos, petroquímica, farmacêutica, metalurgia) e de pesquisa (universidades, institutos). A maioria dos laboratórios de pequeno e médio porte ainda usa sistemas legados de 15-20 anos ou planilhas Excel — criando oportunidade imensa para um LIMS moderno em cloud com preço acessível."),
        ("Funcionalidades Core: Amostras, Laudos e Rastreabilidade",
         "O LIMS mínimo viável deve cobrir: cadastro e rastreamento de amostras com código de barras/QR Code; fluxo de trabalho de análises (recebimento, processamento, resultado, liberação); geração de laudos digitais com assinatura eletrônica do responsável técnico; controle de qualidade analítica (cartas de controle, materiais de referência, repetibilidade/reprodutibilidade); gestão de equipamentos e calibrações; e integração com equipamentos analíticos (analisadores automáticos, espectrofotômetros, balanças) via protocolos RS-232 e ASTM/HL7."),
        ("Verticais: Clínico vs. Industrial vs. Ambiental",
         "LIMS serve três grandes verticais com necessidades distintas: (1) Laboratórios clínicos — laudos médicos, integração com HIS (prontuário), conformidade com RDC Anvisa 302/2005, interface com pacientes para acesso digital de resultados; (2) Laboratórios industriais — rastreabilidade de matéria-prima e produto acabado, liberação de lotes, integração com ERP e sistema de qualidade ISO 17025; (3) Laboratórios ambientais — laudos de análise de água, solo e ar para órgãos ambientais, metodologias ABNT e EPA. Focar em uma vertical no início acelera o go-to-market e a credibilidade."),
        ("Go-to-Market: Acreditação e Laboratórios em Crescimento",
         "O gatilho de compra mais poderoso é a acreditação ISO 17025 (laboratórios de ensaio e calibração) ou ISO 15189 (laboratórios clínicos) pelo INMETRO/CGCRE. A norma exige rastreabilidade de amostras, controle de qualidade analítica e gestão de equipamentos — todas funções de LIMS. Laboratórios que buscam ou renovam acreditação são leads quentes. Parcerias com consultorias de acreditação e implantação de ISO 17025 criam um canal de distribuição natural — o consultor recomenda o LIMS como ferramenta para sustentar o sistema de gestão."),
        ("Precificação e Potencial de Receita",
         "Precificação por número de amostras mensais processadas ou por número de usuários técnicos. Laboratórios clínicos de pequeno porte (500-2.000 amostras/mês) pagam R$500-2.000/mês; laboratórios industriais médios pagam R$3.000-10.000/mês; redes de laboratórios clínicos com múltiplas unidades chegam a R$30.000-100.000/mês. O módulo de portal do paciente (acesso online de laudos) é um upsell valorizado nos laboratórios clínicos. Integrações com convênios (Unimed, Bradesco) automatizam o faturamento e eliminam horas de trabalho manual, justificando o investimento."),
    ],
    [
        ("LIMS e LIS (Laboratory Information System) sao a mesma coisa?",
         "LIS (Laboratory Information System) é um termo usado especificamente para laboratórios clínicos — focado em laudos médicos, interface com médicos solicitantes e integração com planos de saúde. LIMS é mais amplo, cobrindo qualquer tipo de laboratório com foco em rastreabilidade de amostras e gestão de dados analíticos. Na prática, muitos fornecedores usam os termos de forma intercambiável. Para laboratórios clínicos, busque por LIS ou LIMS clínico; para laboratorios industriais e de pesquisa, LIMS é o termo predominante."),
        ("LIMS precisa ser validado como sistema computadorizado em farmácia?",
         "Sim, para laboratórios farmacêuticos sob BPF (Boas Práticas de Fabricação) da ANVISA, o LIMS é classificado como sistema computadorizado regulamentado e precisa passar por CSV (Computer Systems Validation) conforme GAMP5 e RDC ANVISA 17/2010 (ou atualizações). O fornecedor de LIMS que entrega documentação de validação pronta (IQ, OQ, PQ) como parte da implementação elimina uma barreira crítica de adoção no setor farmacêutico e pode cobrar um premium significativo por esse diferencial."),
        ("Como LIMS se integra com equipamentos de laboratório?",
         "A integração mais comum é via middleware de laboratório (bidirectional interface) usando protocolos como ASTM E1394, HL7 para LIS clínico, e RS-232/USB para equipamentos mais antigos. Equipamentos modernos suportam conexão TCP/IP direta. O LIMS recebe a identificação da amostra pelo equipamento, o equipamento devolve o resultado automaticamente — eliminando transcrição manual e erros de entrada de dados. Integrações com os equipamentos mais comuns no mercado-alvo (ex.: Sysmex e Roche para hematologia e bioquímica clínica) são diferencial competitivo crítico."),
    ]
)

# 5312 — Clinic: dermatologia clínica e cirúrgica
art(
    "gestao-de-clinicas-de-dermatologia-clinica-e-cirurgica",
    "Gestão de Clínicas de Dermatologia Clínica e Cirúrgica | ProdutoVivo",
    "Guia para gestão de clínicas de dermatologia: estrutura, serviços cirúrgicos, marketing digital, precificação e estratégias de crescimento sustentável.",
    "Gestão de Clínicas de Dermatologia Clínica e Cirúrgica",
    "Dermatologia combina alta demanda por consultas clínicas com procedimentos cirúrgicos de alto valor. Saiba como estruturar uma clínica dermatológica lucrativa.",
    [
        ("Dermatologia: a Especialidade com Maior Demanda por Acesso",
         "Dermatologia é uma das especialidades médicas com maior demanda reprimida no Brasil — o tempo médio de espera por uma consulta pelo SUS supera 12 meses, e mesmo pelo plano de saúde pode chegar a 3-6 meses em grandes cidades. Doenças como psoríase, acne, dermatite atópica, infecções fúngicas, vitiligo e rastreamento de câncer de pele (melanoma) são prevalentes e requerem acompanhamento especializado. Um consultório bem posicionado e ágil no agendamento pode ter agenda lotada em 3-6 meses após abertura."),
        ("Clínica Dermatológica: Serviços Clínicos e Cirúrgicos",
         "Uma clínica dermatológica completa oferece: consultas clínicas (acne, psoríase, dermatites, alopecias, infecções); dermatoscopia digital para rastreamento de lesões pigmentadas e câncer de pele; cirurgia dermatológica (remoção de nevos, cistos sebáceos, carcinomas basocelulares, biopsias); fototerapia (UVB narrowband para psoríase e vitiligo); e procedimentos estéticos (toxina botulínica, preenchedores, peelings químicos, lasers) quando o dermatologista tem formação adicional em medicina estética. A combinação clínica + cirúrgica + estética maximiza o ticket médio por paciente."),
        ("Estrutura e Equipamentos Essenciais",
         "O equipamento central é o dermatoscópio digital (R$15.000-60.000) para documentação e acompanhamento de lesões pigmentadas — indispensável no rastreamento de melanoma. Para cirurgia dermatológica: bisturi elétrico (eletrocirurgia), criocirurgia com nitrogênio líquido, e sala de procedimentos com iluminação adequada. Equipamentos para procedimentos estéticos (lasers fracionados, IPL, radiofrequência) representam investimento adicional de R$150.000-500.000 mas ampliam significativamente o potencial de receita."),
        ("Marketing e Captação para Dermatologia",
         "Dermatologia tem excelente potencial de marketing digital visual: antes e depois de tratamento de acne (com consentimento), vídeos educativos sobre autoexame de pele, cuidados com protetor solar e tratamentos de manchas geram engajamento alto no Instagram. SEO local para 'dermatologista [cidade]' e 'tratamento de acne [cidade]' captura busca ativa. O Dezembro Laranja (campanha de prevenção de câncer de pele) é uma oportunidade de marketing com propósito social que gera visibilidade e agenda lotada de consultas de rastreamento."),
        ("Teledermatologia: Ampliando o Alcance",
         "Teledermatologia — avaliação de lesões por fotos enviadas pelo paciente antes da consulta (store-and-forward) ou por teleconsulta — permite triagem eficiente e expansão do alcance geográfico. Dermatologistas em grandes centros podem atender pacientes de cidades sem especialista, com exames físicos confirmados por médicos locais quando necessário. A Resolução CFM 2.314/2022 regulamenta a telemedicina; a teledermatologia é um dos casos de uso com maior evidência de eficácia e aceitação tanto por médicos quanto por pacientes."),
    ],
    [
        ("Quanto custa abrir um consultório de dermatologia?",
         "Um consultório de dermatologia básico (sem equipamentos estéticos) requer R$80.000-200.000 de investimento inicial: adequação do espaço físico (R$30.000-80.000), dermatoscópio digital (R$15.000-60.000), material para cirurgia dermatológica (R$20.000-40.000) e capital de giro para os primeiros 3 meses. Com agenda de 20-30 consultas/semana + 2-4 cirurgias dermatológicas/semana, a receita mensal bruta de R$25.000-60.000 viabiliza o retorno em 12-24 meses."),
        ("Dermatologista precisa de especialização adicional para fazer procedimentos estéticos?",
         "A dermatologia inclui em seu escopo original toxina botulínica, preenchedores e peelings — o título de especialista em Dermatologia (aprovado pela SBD/CFM) habilita esses procedimentos. Para lasers de alta potência, a maioria dos programas de residência em dermatologia inclui treinamento, mas cursos complementares são recomendados. O CFM exige que o médico tenha formação adequada para cada procedimento que realiza, independente da especialidade — cursos de atualização na área específica são a forma de comprovar essa formação."),
        ("Como o rastreamento de câncer de pele se torna um diferencial da clínica?",
         "Criar um programa estruturado de 'mapeamento de nevos' — consulta dedicada ao registro fotográfico sistematizado de todas as lesões pigmentadas com dermatoscópio digital — gera recorrência anual automática, receita previsível e reputação de especialização em prevenção de melanoma. Parcerias com empresas para oferecer rastreamento de câncer de pele como benefício de saúde, e com clubes de corrida e esportes ao ar livre (público de alto risco por exposição solar) são canais eficazes de captação de pacientes jovens e ativos."),
    ]
)

# 5313 — SaaS Sales: e-commerce e DTC
art(
    "vendas-para-o-setor-de-saas-de-e-commerce-e-direct-to-consumer",
    "Vendas para o Setor de SaaS de E-commerce e Direct-to-Consumer | ProdutoVivo",
    "Estratégias de vendas B2B para SaaS de e-commerce e DTC: como prospectar lojistas online, marcas DTC e marketplaces para fechar contratos recorrentes.",
    "Vendas para o Setor de SaaS de E-commerce e Direct-to-Consumer",
    "O e-commerce brasileiro movimenta R$200 bilhões anuais. Saiba como vender SaaS para esse ecossistema em crescimento constante.",
    [
        ("O Ecossistema de E-commerce no Brasil",
         "O e-commerce brasileiro tem mais de 1,7 milhão de lojas virtuais ativas, com crescimento de 12-15% ao ano. O ecossistema inclui desde MEIs com loja na Nuvemshop até grandes marcas DTC (Direct-to-Consumer) com operação própria e integração com marketplaces (Mercado Livre, Amazon, Shopee). Cada camada do ecossistema tem necessidades específicas de SaaS: lojas pequenas precisam de facilidade e preço acessível; marcas DTC de médio porte buscam automação de marketing, analytics de conversão e gestão de estoque integrada; grandes operações precisam de plataformas enterprise de OMS e fulfillment."),
        ("Mapa do SaaS para E-commerce",
         "Os segmentos de SaaS para e-commerce: (1) Plataforma de loja (Shopify, VTEX, Nuvemshop — altíssima barreira de entrada); (2) Analytics e CRO — heatmaps, A/B testing, funil de conversão; (3) Marketing e retenção — e-mail marketing, SMS, push, automação de carrinho abandonado; (4) Fulfillment e logística — gestão de estoque multicanal, OMS (Order Management System), integração com transportadoras; (5) Atendimento ao cliente — chat, helpdesk, gestão de trocas e devoluções; (6) Precificação dinâmica e monitoramento de concorrentes. Segmentos 2-6 têm menor barreira de entrada e mais oportunidade para novos players."),
        ("Prospecção no E-commerce: Onde Estão os Compradores",
         "Os decisores em e-commerce são: Head de E-commerce, Diretor de Marketing Digital, CTO (para integrações técnicas) e COO (para logística e fulfillment). Canais de prospecção: eventos como NRF Brasil, E-Commerce Brasil, ABComm Fórum; grupos de empreendedores de e-commerce no Facebook e WhatsApp; parceiros de agências de performance que servem o mesmo público; e integrações com as plataformas de loja (marketplace de apps da Shopify, VTEX App Store) que expõem o SaaS a lojistas ativos diretamente no painel que já usam."),
        ("Demo e Prova de Conceito no E-commerce",
         "O demo ideal conecta ao ambiente de testes do lojista — mostra dados reais da loja dele, não dados de demonstração genérica. Para analytics de conversão, mostre o funil de abandono da loja real; para automação de e-mail, configure uma sequência de carrinho abandonado usando os produtos reais do cliente. O impacto de uma sequência de e-mail de carrinho abandonado bem configurada — recuperando 5-15% dos carrinhos abandonados — é imediatamente calculável em receita. Esse ROI tangível fecha vendas sem necessidade de ciclo de aprovação longo."),
        ("Sazonalidade e Ciclo de Vendas no E-commerce",
         "O e-commerce tem sazonalidade intensa: novembro-dezembro é a alta temporada (Black Friday, Natal) e representa 25-35% do faturamento anual de muitos lojistas. Evite mudar de sistema em agosto-outubro — o lojista não quer risco na maior época do ano. O melhor momento para vender é janeiro-março, quando o lojista está analisando o ano anterior e planejando upgrades. Lojistas que acabaram de ter um Black Friday problemático (lentidão no site, erros de estoque, logística caótica) são leads quentes em dezembro-janeiro para soluções que resolvem esses problemas."),
    ],
    [
        ("Qual o SaaS de maior crescimento no ecossistema de e-commerce em 2025?",
         "Os segmentos de maior crescimento em 2025 no e-commerce SaaS são: (1) CDP (Customer Data Platform) para unificar dados de clientes entre canais; (2) IA para personalização de produto e recomendações em tempo real; (3) Social commerce tools — integração com TikTok Shop, Instagram Shopping e live commerce; (4) Gestão de devoluções e logística reversa — custo crescente que grandes lojistas querem otimizar; (5) B2B e-commerce platforms — marcas que vendem tanto B2C quanto B2B precisam de plataformas unificadas. Todos esses segmentos têm crescimento de 30-60% ao ano."),
        ("Como SaaS de e-commerce compete com as funcionalidades nativas da Shopify/VTEX?",
         "Plataformas de loja investem em funcionalidades básicas que atendem 80% dos lojistas. SaaS especializados ganham nos 20% mais avançados: analytics mais profundo que o nativo, automação de marketing multicanal (e-mail + SMS + push + WhatsApp), logística omnichannel com múltiplos centros de distribuição. A estratégia vencedora é ser o 'melhor em uma coisa' — o SaaS que é referência em analytics de conversão ou em recuperação de carrinho tem posicionamento claro que a plataforma de loja não replica facilmente."),
        ("Qual o ticket médio de SaaS para e-commerce no Brasil?",
         "O ticket varia muito por segmento: ferramentas de analytics de CRO custam R$500-5.000/mês; plataformas de e-mail marketing para e-commerce de médio porte R$500-3.000/mês; OMS/fulfillment para operações maiores R$5.000-30.000/mês; plataformas de CDP e personalização para grandes varejistas R$15.000-100.000/mês. O sweet spot de crescimento mais rápido está em ferramentas de R$500-3.000/mês para lojistas de médio porte (R$1-20M de faturamento online) — mercado de 50.000-100.000 potenciais clientes no Brasil."),
    ]
)

# 5314 — Consulting: marketing digital e growth hacking
art(
    "consultoria-de-marketing-digital-e-growth-hacking",
    "Consultoria de Marketing Digital e Growth Hacking | ProdutoVivo",
    "Como estruturar e escalar uma consultoria de marketing digital e growth hacking: serviços, posicionamento, captação e modelos de receita para consultores digitais.",
    "Consultoria de Marketing Digital e Growth Hacking",
    "Marketing digital é a demanda mais comum de PMEs e startups. Veja como se diferenciar e construir uma consultoria lucrativa nesse mercado competitivo.",
    [
        ("O Mercado de Consultoria de Marketing Digital no Brasil",
         "Marketing digital é o serviço mais contratado por PMEs e startups brasileiras — e também o mais comoditizado. Milhares de agências e freelancers brigam pelo mesmo cliente com propostas similares. A diferenciação vem da especialização: growth hacking (crescimento acelerado via experimentação), performance marketing (ROAS e CAC como linguagem), e marketing orientado a dados (analytics, atribuição, testes A/B). Consultorias que falam a língua do negócio — receita, margem, LTV — e não apenas a linguagem de vaidade (curtidas, seguidores) cobram premium e retêm clientes por anos."),
        ("Posicionamento: do Generalista ao Especialista",
         "A armadilha mais comum em consultoria de marketing digital é tentar atender todos: e-commerce, SaaS, clínicas, varejo. A especialização aumenta o ticket e reduz o ciclo de vendas — um consultor que se apresenta como 'especialista em crescimento para SaaS B2B' é contratado em dias; um 'especialista em marketing digital' entra em concorrência com centenas. Escolha uma vertical (ex.: healthtech, e-commerce de moda, B2B SaaS) ou um serviço específico (ex.: SEO técnico, paid social para geração de leads, email marketing para e-commerce)."),
        ("Portfólio de Serviços com Margem Alta",
         "Serviços de alta margem em consultoria de marketing digital: (1) Diagnóstico e estratégia de growth — análise de funil completo, identificação de gargalos, roadmap de experimentos (R$10.000-40.000 por projeto); (2) Programa de experimentos de growth — ciclos quinzenais de hipóteses, testes A/B e análise de resultados (retainer de R$8.000-25.000/mês); (3) Auditoria de analytics — mapeamento de tracking, configuração de GA4, dashboards de KPIs (R$8.000-25.000 por projeto); (4) Treinamento de equipe interna — capacitação do time de marketing para operar com mentalidade de growth."),
        ("Captação: Conteúdo que Gera Inbound de Qualidade",
         "Um consultor de growth que não tem growth em sua própria captação carece de credibilidade. Construa sua máquina de captação: LinkedIn com conteúdo sobre casos de crescimento (sem revelar clientes), newsletter semanal com análises de campanhas e testes interessantes do mercado, podcast ou canal YouTube com entrevistas de fundadores sobre estratégias de crescimento. Esse conteúdo atrai founders e CMOs que você quer como clientes. O ciclo de vendas por inbound é 3-5x mais curto que por cold outreach para consultorias de alto valor."),
        ("Modelos de Contrato e Escalabilidade",
         "Três modelos que funcionam: (1) Projeto com prazo definido — diagnóstico, auditoria ou programa de 90 dias com entregáveis claros; (2) Retainer mensal — acompanhamento contínuo de campanha, análise de resultados e iteração de estratégia; (3) Success fee híbrido — retainer base + bônus por crescimento acima de uma meta combinada (ex.: 20% sobre o incremento de receita acima da meta). O modelo híbrido alinha incentivos e desbloqueava clientes que hesitam com honorários fixos altos. Para escalar sem perder qualidade, construa metodologia proprietária documentada e contrate analistas para a execução enquanto você faz a estratégia."),
    ],
    [
        ("Growth hacking é o mesmo que marketing digital?",
         "Growth hacking é uma abordagem dentro do marketing digital focada em experimentação rápida, dados e crescimento acelerado com recursos limitados — o termo foi criado por Sean Ellis para descrever como startups crescem sem grandes verbas. Marketing digital é mais amplo: inclui branding, conteúdo, mídia paga, SEO, e-mail, social media. Um growth hacker usa ferramentas de marketing digital, mas com mentalidade de produto e experimentação científica — testa hipóteses, mede resultados e itera rapidamente em vez de executar campanhas fixas."),
        ("Como cobrar por resultados em consultoria de marketing digital?",
         "Contratos baseados em resultado são atraentes para o cliente mas arriscados para o consultor — fatores fora do seu controle (produto ruim, sazonalidade, mudanças de mercado) podem afetar o resultado mesmo com trabalho excelente. O modelo mais equilibrado é: retainer fixo para cobrir custos e garantir dedicação, mais success fee acima de uma meta combinada de crescimento. Defina métricas de resultado claras antes de assinar (ex.: leads qualificados gerados, MRR novo atribuível ao canal, ROAS mínimo de campanhas) para evitar disputas no momento do pagamento."),
        ("Qual a diferença entre agência de marketing e consultoria de growth?",
         "Agência de marketing executa: cria campanhas, posta conteúdo, gerencia contas de mídia paga. Consultoria de growth estratégica diagnóstica, prioriza e orienta: analisa o funil completo, identifica onde está o maior gargalo de crescimento, define prioridades de experimentação. Consultorias de growth geralmente cobram mais e trabalham em menor número de clientes — o work é estratégico e de alto impacto, não operacional. Muitas consultorias de growth são 'fractional CMO' — atuam como liderança de marketing sem ser CLT, gerenciando inclusive as agências de execução."),
    ]
)

# 5315 — B2B SaaS: saúde ocupacional e medicina do trabalho SaaS
art(
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-saude-ocupacional-e-medicina-do-trabalho",
    "Gestão de Negócios de Empresa de B2B SaaS de Saúde Ocupacional e Medicina do Trabalho | ProdutoVivo",
    "Como construir e escalar um B2B SaaS de saúde ocupacional e medicina do trabalho: mercado, produto, go-to-market e crescimento no mercado de SST.",
    "Gestão de Negócios de Empresa de B2B SaaS de Saúde Ocupacional e Medicina do Trabalho",
    "Saúde e segurança do trabalho é obrigação legal de toda empresa. Veja como construir um SaaS rentável nesse mercado de conformidade permanente.",
    [
        ("O Mercado de SST e Saúde Ocupacional no Brasil",
         "Toda empresa com funcionários CLT tem obrigações de Saúde e Segurança do Trabalho (SST): PCMSO (Programa de Controle Médico de Saúde Ocupacional), PPRA/PGR (Programa de Gerenciamento de Riscos), laudos de insalubridade e periculosidade, e-Social SST (envio obrigatório de ASO — Atestado de Saúde Ocupacional — para o governo). Com o e-Social SST plenamente vigente, a digitalização de laudos médicos ocupacionais tornou-se mandatória — criando demanda imediata por sistemas que gerenciem esses dados e os transmitam ao e-Social automaticamente."),
        ("Produto: ASO Digital, e-Social e Gestão de Exames",
         "O produto core de saúde ocupacional SaaS deve cobrir: emissão de ASO (Atestado de Saúde Ocupacional) digital e integração automática com e-Social (evento S-2220); gestão de exames ocupacionais (admissional, periódico, retorno ao trabalho, mudança de função, demissional) com alertas de vencimento; gestão de riscos ocupacionais por cargo (PGR digital); controle de EPI (Equipamentos de Proteção Individual) com assinatura eletrônica do colaborador; e dashboard de indicadores de saúde ocupacional da empresa."),
        ("ICP: Clínicas Ocupacionais e Empresas com RH",
         "Dois ICPs principais: (1) Clínicas de medicina do trabalho e SESMT (Serviços Especializados em Engenharia de Segurança e Medicina do Trabalho) que atendem múltiplas empresas e precisam de sistema para gerenciar centenas de ASOs por dia; (2) Empresas com departamento de RH próprio que querem controlar internamente a gestão de saúde ocupacional sem depender totalmente da clínica terceirizada. O primeiro ICP tem maior ticket (R$3.000-20.000/mês por clínica ocupacional de médio porte) e o segundo tem maior volume de potenciais clientes."),
        ("Integração com e-Social: o Diferencial Mais Poderoso",
         "O e-Social SST criou uma obrigação de transmissão de dados de saúde ocupacional para o governo federal. Empresas que não cumprem enfrentam autuações do MTE (Ministério do Trabalho) e problemas em homologações de demissão. Um SaaS que automatiza completamente a transmissão dos eventos de SST para o e-Social (S-2210, S-2220, S-2240) elimina um risco de compliance real e mensurável — esse argumento fecha contratos rapidamente com diretores de RH que já receberam notificações do MTE. A integração com os principais ERPs (TOTVS, SAP, Senior) para sincronizar dados de colaboradores complementa o produto."),
        ("Modelo de Receita e Potencial de Mercado",
         "Precificação por número de colaboradores gerenciados: R$5-15 por colaborador/mês. Uma empresa com 200 colaboradores paga R$1.000-3.000/mês; com 1.000 colaboradores R$5.000-15.000/mês. O mercado potencial são todas as empresas com funcionários CLT no Brasil — mais de 6 milhões de empresas formais. Mesmo focando em empresas com 50-500 colaboradores (400.000+ empresas), o TAM é enorme. Churn é naturalmente baixo pois a troca implica em migrar todos os ASOs históricos e refazer a integração com o e-Social."),
    ],
    [
        ("e-Social SST é obrigatório para todas as empresas?",
         "Sim. O e-Social SST (transmissão de eventos de saúde e segurança do trabalho) é obrigatório para todas as empresas com empregados CLT, independente do porte. A transmissão do S-2220 (Monitoramento da Saúde do Trabalhador — ASO) deve ser feita sempre que um exame ocupacional é realizado. Empresas que não transmitem os eventos corretamente ficam com pendências no e-Social que podem gerar multas do MTE e dificuldades em processos trabalhistas. Micro e pequenas empresas tiveram prazo de implantação estendido, mas todas já estão obrigadas."),
        ("PCMSO e PGR precisam de software específico ou podem ser feitos em Word/Excel?",
         "Legalmente não há exigência de software específico — PCMSO e PGR podem ser documentos em Word. Contudo, com o e-Social SST, os dados do PCMSO (exames previstos por cargo e risco) precisam ser cruzados com os ASOs realizados e transmitidos eletronicamente. Fazê-lo manualmente em Excel com centenas de colaboradores é trabalhoso e propenso a erros. Um SaaS que automatiza essa correlação e a transmissão ao e-Social elimina 80% do trabalho manual do médico do trabalho ou SESMT, justificando o investimento."),
        ("Quem compra SaaS de saúde ocupacional: o RH da empresa ou a clinica terceirizada?",
         "Ambos. Clínicas de medicina do trabalho que atendem múltiplas empresas precisam de sistema para emitir ASOs em volume — é o software central de operação delas. Empresas com SESMT próprio (obrigatório para empresas acima de determinado número de funcionários por NR-4) precisam de sistema para gerenciar todo o programa de saúde ocupacional internamente. A clínica que usa o SaaS pode oferecer acesso ao portal do cliente (empresa) para que o RH acompanhe os ASOs dos colaboradores — criando um efeito de rede que fideliza ambos os lados."),
    ]
)

# 5316 — Clinic: geriatria e cuidados com o idoso
art(
    "gestao-de-clinicas-de-geriatria-e-cuidados-com-o-idoso",
    "Gestão de Clínicas de Geriatria e Cuidados com o Idoso | ProdutoVivo",
    "Guia para gestão de clínicas de geriatria e cuidados com o idoso: estrutura, equipe multidisciplinar, credenciamento e estratégias de crescimento nesse mercado em expansão.",
    "Gestão de Clínicas de Geriatria e Cuidados com o Idoso",
    "O Brasil envelhece rapidamente: 15% da população já tem 60+ anos. Saiba como estruturar uma clínica geriátrica de alto valor social e financeiro.",
    [
        ("O Envelhecimento Populacional como Oportunidade de Negócio",
         "O Brasil tem 34 milhões de pessoas com 60 anos ou mais — 15% da população — e esse número deve dobrar até 2060. O envelhecimento acelerado cria demanda crescente por geriatras especializados: são apenas 5.000 médicos com título de especialista em geriatria para atender uma população idosa de dezenas de milhões. A lacuna entre oferta de especialistas e demanda é uma das mais dramáticas da medicina brasileira, garantindo agenda cheia para qualquer clínica de geriatria bem posicionada em qualquer cidade de médio e grande porte."),
        ("Modelo de Cuidado Geriátrico: Avaliação e Longitudinalidade",
         "A consulta geriátrica é mais longa e complexa que consultas de clínica geral — uma Avaliação Geriátrica Ampla (AGA) inicial dura 60-90 minutos e avalia cognição, funcionalidade, quedas, polifarmácia, nutrição, humor e suporte social. O modelo de cuidado longitudinal (acompanhamento frequente do mesmo paciente por anos) cria receita recorrente previsível e alta fidelização. O cuidado geriátrico bem feito previne internações, quedas e perda funcional — gerando valor mensurável para o paciente, família e sistema de saúde."),
        ("Equipe Multidisciplinar e Serviços Complementares",
         "Uma clínica geriátrica completa integra: geriatra (médico coordenador do cuidado), neurologista para demências, nutricionista com especialização em idoso, fisioterapeuta gerontológica (reabilitação e prevenção de quedas), psicólogo/neuropsicólogo (avaliação cognitiva e suporte emocional), assistente social (rede de apoio familiar). Programas de reabilitação cognitiva para pacientes com déficit leve a moderado e grupos de estimulação cognitiva geram receita adicional recorrente com boa margem."),
        ("B2B Geriátrico: Planos de Saúde e Operadoras Sênior",
         "Operadoras de planos de saúde com carteiras de segurados mais velhos (planos de servidores, Cassi, Geap, FunPrev) têm altíssimo interesse em clínicas geriátricas que reduzam internações — cada internação de idoso evitada economiza R$8.000-40.000 para a operadora. Apresente sua clínica como parceira de gestão de casos complexos e programas de envelhecimento saudável para essas operadoras. Credenciar com planos sênior específicos (Prevent Senior, GEAP, Sabesprev) garante acesso a uma carteira de pacientes idosos com cobertura ativa."),
        ("Marketing e Captação para Geriatria",
         "A família do idoso é frequentemente quem busca o especialista — filhos adultos preocupados com o declínio cognitivo dos pais ou com o controle de medicamentos de um idoso com polifarmácia. Conteúdo educativo para familiares sobre sinais de demência, prevenção de quedas e cuidados com idosos gera tráfego de alta conversão no Instagram e Google. SEO local para 'geriatra [cidade]' e 'médico para idosos [cidade]' captura busca ativa de necessidade imediata. Parcerias com clínicos gerais, neurologistas, cardiologistas e oncologistas para encaminhamentos mútuos constroem rede de referência robusta."),
    ],
    [
        ("Geriatria e gerontologia são a mesma coisa?",
         "Não. Geriatria é a especialidade médica que trata doenças e problemas de saúde de idosos — o geriatra é um médico. Gerontologia é uma ciência multidisciplinar que estuda o envelhecimento humano em seus aspectos biológicos, psicológicos e sociais — inclui profissionais como psicólogos, fisioterapeutas, enfermeiros, assistentes sociais e gerontólogos (graduação específica). Uma boa clínica de geriatria integra profissionais de geriatria e gerontologia para um cuidado verdadeiramente multidisciplinar."),
        ("Avaliação geriátrica ampla (AGA) é coberta por plano de saúde?",
         "A consulta geriátrica é coberta por planos de saúde, mas o tempo de consulta mais longo (60-90 minutos) raramente é remunerado diferente de uma consulta convencional de 20-30 minutos. Isso cria tensão econômica — o custo da AGA é maior que o reembolso do plano. Muitas clínicas geriátricas optam por um modelo híbrido: a AGA inicial é cobrada no particular (R$400-800), e as consultas de acompanhamento subsequentes aceitam plano. Esse modelo valida o compromisso do paciente/família com o cuidado longitudinal."),
        ("Qual o papel do geriatra na gestão de polifarmácia?",
         "Polifarmácia (uso de 5 ou mais medicamentos simultaneamente) afeta 40-50% dos idosos brasileiros e é uma das principais causas de internação e quedas na terceira idade. O geriatra realiza a conciliação medicamentosa — revisão sistematizada de todos os medicamentos do paciente, identificando duplicidades, interações perigosas e medicamentos inadequados para idosos (Critérios de Beers). A desprescrição — retirada segura de medicamentos desnecessários — melhora a qualidade de vida e reduz o risco de eventos adversos. Essa expertise é um dos maiores valores percebidos pelo paciente e família."),
    ]
)

# 5317 — SaaS Sales: varejo físico e PDV
art(
    "vendas-para-o-setor-de-saas-de-varejo-fisico-e-ponto-de-venda",
    "Vendas para o Setor de SaaS de Varejo Físico e Ponto de Venda | ProdutoVivo",
    "Estratégias de vendas B2B para SaaS de varejo físico e PDV: como prospectar varejistas, redes de lojas e franquias para fechar contratos de alto valor.",
    "Vendas para o Setor de SaaS de Varejo Físico e Ponto de Venda",
    "O varejo físico brasileiro tem 1,5 milhão de lojas formais. Saiba como vender SaaS para esse mercado ainda subdigitalizado e de alto potencial.",
    [
        ("O Varejo Físico Brasileiro: Tamanho e Oportunidade Digital",
         "O varejo físico brasileiro tem mais de 1,5 milhão de estabelecimentos formais, do açougue local à rede de 500 lojas. A digitalização do varejo físico acelerou com a pandemia — sistemas de PDV em tablet, gestão de estoque em tempo real, e programas de fidelidade digital são agora expectativas dos consumidores. A maioria dos pequenos varejistas ainda opera com sistemas de PDV desconectados, controle de estoque manual e caixa registradora eletrônica antiga — o espaço para modernização é imenso e urgente."),
        ("Segmentos de SaaS para Varejo Físico",
         "Os principais segmentos: (1) PDV (Ponto de Venda) em tablet/cloud — NF-e, controle de caixa, integração com estoque; (2) Gestão de estoque e reposição automática — inventário em tempo real, sugestão de compra, múltiplos depósitos; (3) CRM e fidelização — programa de pontos, cashback, comunicação com cliente via WhatsApp; (4) Business intelligence — dashboard de vendas por categoria, margem, giro de estoque; (5) Gestão de pessoal de loja — escala de trabalho, comissionamento de vendedores, metas por loja. Para redes de franquias e lojas, a gestão centralizada multiunidade é o diferencial mais poderoso."),
        ("Prospecção: Abordagem por Segmento e Porte",
         "Para varejistas pequenos (1-3 lojas): canais digitais (LinkedIn, Instagram do varejista), feiras setoriais (ABF para franquias, Fecomercio eventos), e parcerias com distribuidores que atendem esses varejistas diariamente (distribuidoras de bebidas, de suplementos, de cosméticos). Para redes médias (10-50 lojas): abordagem direta ao diretor de operações ou TI com proposta de ROI por loja. Para grandes redes (100+ lojas): processo de RFP com demos e piloto em loja(s) selecionadas antes da decisão. Cada porte exige approach diferente — don't use the same pitch for all."),
        ("Demo e Piloto: Convencendo o Varejista Cético",
         "O varejista é cético por natureza — já viu muita promessa e pouca entrega. A demo deve acontecer dentro da loja do cliente quando possível, com o produto real sendo operado pelo próprio funcionário de caixa. Mostre velocidade (PDV que fecha uma venda em menos de 30 segundos), simplicidade de uso (caixa consegue operar sem treinamento extenso), e benefício imediato (estoque sincronizado em tempo real, NF-e emitida automaticamente). Um piloto de 30 dias em uma loja do cliente com KPIs combinados (redução de ruptura de estoque, aumento de ticket médio) fecha o contrato para toda a rede."),
        ("Estratégia de Expansão em Redes e Franquias",
         "Franqueadoras são o canal mais eficiente no varejo — uma parceria com uma rede franqueadora de 200 lojas abre 200 potenciais clientes com uma única negociação. Apresente ao diretor de expansão ou operações da franqueadora o valor do SaaS para a rede (padronização de operação, visibilidade em tempo real de todas as lojas, comparativo de desempenho entre franqueados). A indicação da franqueadora para seus franqueados tem taxa de conversão muito maior que prospecção fria. O contrato com a franqueadora pode incluir uma comissão por cada franqueado que adota — ou desconto de volume para toda a rede."),
    ],
    [
        ("PDV em cloud é confiável para varejo que não pode parar?",
         "PDV em cloud moderno opera em modo offline quando a conexão cai — sincroniza as vendas automaticamente quando a conexão é restaurada. A disponibilidade dos principais provedores cloud (AWS, Google, Azure) supera 99,95% — muito mais confiável que servidores locais que varejo pequeno e médio tipicamente mantinha. O risco de perder vendas por queda de internet é menor que o risco de um servidor local travar na Black Friday. Mostre os SLAs de disponibilidade e o modo offline na demo para desfazer esse mito com o varejista."),
        ("Integração com NFC-e e NF-e é obrigatória em PDV?",
         "Sim. Varejo de produtos físicos emite NF-e (Nota Fiscal Eletrônica) para pessoas jurídicas e NFC-e (Nota Fiscal de Consumidor Eletrônica) para consumidores finais. Todo PDV legal precisa emitir esses documentos fiscais eletrônicos com integração com a SEFAZ estadual. Para varejo de serviços, emite-se NFS-e (Nota Fiscal de Serviços Eletrônica), gerenciada pelo município. Um PDV SaaS que não tem emissão fiscal integrada e homologada nas SEFAZs estaduais é inviável comercialmente no Brasil — essa conformidade fiscal é obrigatória e deve ser destacada como diferencial na demo."),
        ("Como vender SaaS de PDV para o pequeno varejista que diz que 'caixa registradora funciona'?",
         "Mostre o custo do 'funciona': caixa registradora não emite NFC-e (problema fiscal crescente), não controla estoque (perda e furto invisíveis), não alimenta relatórios de vendas, não integra com fornecedores para reposição, e não tem programa de fidelidade para reter clientes. Para um varejista com R$100.000/mês de faturamento, 2% de perda por falta de controle de estoque = R$2.000/mês — valor que paga qualquer PDV SaaS com folga. Quantifique a perda atual antes de falar em preço."),
    ]
)

# 5318 — Consulting: precificação e Revenue Management
art(
    "consultoria-de-precificacao-e-revenue-management",
    "Consultoria de Precificação e Revenue Management | ProdutoVivo",
    "Como estruturar e escalar uma consultoria de precificação e Revenue Management: metodologias, posicionamento, captação e modelos de receita para consultores financeiros estratégicos.",
    "Consultoria de Precificação e Revenue Management",
    "Precificação errada é o principal destruidor de margem em empresas brasileiras. Veja como monetizar expertise em precificação como consultor estratégico.",
    [
        ("O Impacto da Precificação nos Resultados Empresariais",
         "Precificação é a alavanca de maior impacto no resultado de uma empresa — um aumento de 1% no preço, sem mudança de volume, aumenta o lucro operacional em 8-10% em média. Apesar disso, a maioria das PMEs e mesmo médias empresas brasileiras precifica de forma empírica: custo + margem fixa, ou copiando a concorrência. Consultores de precificação estratégica e Revenue Management ajudam empresas a capturar o valor que já entregam — sem precisar reduzir custos ou aumentar vendas — tornando o ROI da consultoria imediato e mensurável."),
        ("Portfólio de Serviços: do Diagnóstico ao RM Contínuo",
         "Os serviços de uma consultoria de precificação: (1) Diagnóstico de precificação — análise da política atual, identificação de vazamentos de margem, benchmark setorial; (2) Estratégia de precificação — definição de política de preços, segmentação por valor percebido, arquitetura de planos/pacotes; (3) Revenue Management — precificação dinâmica por demanda, temporada, canal de venda e perfil de cliente (aplicado especialmente em hotelaria, aéreo, e-commerce e SaaS); (4) Treinamento de equipes — capacitação de times comerciais para negociar sem conceder descontos desnecessários."),
        ("Revenue Management Além da Hotelaria",
         "Revenue Management foi desenvolvido na indústria aérea e hoteleira, mas suas técnicas se aplicam a qualquer negócio com capacidade perecível e demanda variável: restaurantes (gestão de mesas por horário e dia da semana), clínicas (gestão de agenda de médicos), cinemas, espaços de coworking, e-commerce (precificação dinâmica por estoque e concorrência) e SaaS (precificação por segmento de cliente e disposição a pagar). Consultores que transpõem Revenue Management para novos setores têm vantagem competitiva significativa sobre generalistas de precificação."),
        ("Captação: CFOs e Diretores Financeiros como Caminho",
         "Os decisores para contratar consultoria de precificação são CFOs, diretores financeiros e CEOs de empresas que percebem queda de margem ou perda de competitividade por preço. Os gatilhos de contratação: margem bruta caindo mesmo com crescimento de receita, guerra de preços com concorrentes que está destruindo rentabilidade, lançamento de novo produto ou linha onde não há referência de preço, e expansão para novos mercados (geográficos ou segmentos) que exige reposicionamento de preço. Conteúdo técnico sobre margem e precificação para CFOs no LinkedIn gera inbound de alta qualidade."),
        ("Modelos de Remuneração e ROI da Consultoria",
         "Modelos que funcionam: (1) Projeto fixo — diagnóstico e estratégia de precificação com entregáveis definidos (R$30.000-150.000 por projeto de 4-12 semanas); (2) Sucesso fee sobre melhoria de margem — percentual sobre o incremento de margem bruta nos primeiros 12 meses (ex.: 20% do incremento de margem acima da baseline); (3) Retainer de RM — acompanhamento mensal de indicadores de precificação e revenue management (R$8.000-30.000/mês). O sucesso fee é o modelo mais fácil de vender — o cliente paga apenas sobre ganho real. Para o consultor, é fundamental ter baseline clara e metodologia auditável de atribuição."),
    ],
    [
        ("Qual a diferença entre precificação estratégica e Revenue Management?",
         "Precificação estratégica define o preço de um produto ou serviço com base em valor percebido pelo cliente, posicionamento competitivo e objetivos de margem — é uma decisão relativamente estável. Revenue Management é uma disciplina operacional que ajusta preços dinamicamente em tempo real com base em demanda, disponibilidade e segmento de cliente — maximiza a receita total de uma capacidade finita. As duas disciplinas são complementares: a estratégia define o teto e o posicionamento; o RM opera dentro dessa estratégia para maximizar a captura de valor dia a dia."),
        ("Como justificar um aumento de preço para o time comercial que tem medo de perder clientes?",
         "O medo de perder clientes por aumento de preço é real mas frequentemente exagerado. Dados mostram que, em mercados com diferenciação de produto, 80% dos clientes atuais aceitam aumentos de 5-10% sem questionar — os outros 20% negociam ou saem, mas a margem nos 80% restantes mais que compensa. Para o time comercial, prepare argumentação de valor (o que o produto entrega que justifica o preço novo), treinamento em negociação de valor vs. desconto, e meça o resultado 90 dias após o aumento para ter dados reais que desmistificam o medo."),
        ("Revenue Management funciona para serviços profissionais como consultorias e clínicas?",
         "Sim, com adaptações. Consultorias têm capacidade finita de horas de consultores — RM pode otimizar quais projetos aceitar, quando oferecer desconto para preencher capacidade ociosa, e quando cobrar premium em períodos de alta demanda. Clínicas têm agenda como capacidade finita — RM otimiza a combinação de consultas (diferentes especialidades e durações), reduz no-shows com depósito antecipado, e cobra diferente para horários de pico vs. baixa demanda. O princípio é o mesmo: maximizar a receita de uma capacidade que não pode ser estocada."),
    ]
)

# ── Sitemap ───────────────────────────────────────────────────────────────────
slugs_5311 = [
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-lims-e-gestao-de-laboratorios",
    "gestao-de-clinicas-de-dermatologia-clinica-e-cirurgica",
    "vendas-para-o-setor-de-saas-de-e-commerce-e-direct-to-consumer",
    "consultoria-de-marketing-digital-e-growth-hacking",
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-saude-ocupacional-e-medicina-do-trabalho",
    "gestao-de-clinicas-de-geriatria-e-cuidados-com-o-idoso",
    "vendas-para-o-setor-de-saas-de-varejo-fisico-e-ponto-de-venda",
    "consultoria-de-precificacao-e-revenue-management",
]
titles_5311 = [
    "Gestão de Negócios de Empresa de B2B SaaS de LIMS e Gestão de Laboratórios",
    "Gestão de Clínicas de Dermatologia Clínica e Cirúrgica",
    "Vendas para o Setor de SaaS de E-commerce e Direct-to-Consumer",
    "Consultoria de Marketing Digital e Growth Hacking",
    "Gestão de Negócios de Empresa de B2B SaaS de Saúde Ocupacional e Medicina do Trabalho",
    "Gestão de Clínicas de Geriatria e Cuidados com o Idoso",
    "Vendas para o Setor de SaaS de Varejo Físico e Ponto de Venda",
    "Consultoria de Precificação e Revenue Management",
]

sm_path = pathlib.Path(__file__).parent / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")
new_urls = "\n".join(
    f"  <url><loc>{DOMAIN}/blog/{s}/</loc><changefreq>monthly</changefreq><priority>0.6</priority></url>"
    for s in slugs_5311
)
sm_path.write_text(sm.replace("</urlset>", new_urls + "\n</urlset>"), encoding="utf-8")

# ── Trilha ────────────────────────────────────────────────────────────────────
tr_path = pathlib.Path(__file__).parent / "trilha.html"
tr = tr_path.read_text(encoding="utf-8")
new_items = "\n".join(
    f'    <li><a href="/blog/{s}/">{t}</a></li>'
    for s, t in zip(slugs_5311, titles_5311)
)
tr_path.write_text(tr.replace("</ul>", new_items + "\n  </ul>", 1), encoding="utf-8")

print("Done — batch 1914")
