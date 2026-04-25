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
<link rel="canonical" href="{canon}"/>
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
<script type="application/ld+json">{schema}</script>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Arial,sans-serif;color:#222;background:#fff}}
header{{background:#0a7c4e;color:#fff;padding:20px;text-align:center}}
header h1{{font-size:1.6rem;line-height:1.3}}
main{{max-width:800px;margin:30px auto;padding:0 16px}}
h2{{color:#0a7c4e;margin:24px 0 10px}}
p{{line-height:1.7;margin-bottom:14px}}
.faq{{background:#f4faf7;border-left:4px solid #0a7c4e;padding:14px 16px;margin:12px 0;border-radius:4px}}
.faq strong{{display:block;margin-bottom:6px}}
footer{{text-align:center;padding:30px 16px;font-size:.85rem;color:#666}}
footer a{{color:#0a7c4e;text-decoration:none}}
</style>
</head>
<body>
<header><h1>{h1}</h1></header>
<main>
<p>{lead}</p>
{sections}
<section>
<h2>Perguntas Frequentes</h2>
{faqs}
</section>
<p style="margin-top:28px">Quer aprofundar sua estratégia?
<a href="https://produtovivo.com.br/" style="color:#0a7c4e;font-weight:bold">
Conheça o guia completo do ProdutoVivo</a> e acelere seus resultados.</p>
</main>
<footer><p>&copy; 2025 ProdutoVivo &mdash;
<a href="https://produtovivo.com.br/blog/">Ver todos os guias</a></p></footer>
</body>
</html>"""


def art(slug, title, desc, h1, lead, sections, faq_list):
    canon  = f"{DOMAIN}/blog/{slug}/"
    schema = json.dumps({
        "@context": "https://schema.org",
        "@type":    "FAQPage",
        "mainEntity": [
            {"@type": "Question",
             "name":  q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faq_list
        ]
    }, ensure_ascii=False)
    sec_html = "\n".join(
        f"<section><h2>{h}</h2><p>{p}</p></section>"
        for h, p in sections
    )
    faq_html = "\n".join(
        f'<div class="faq"><strong>{q}</strong><p>{a}</p></div>'
        for q, a in faq_list
    )
    html = TMPL.format(
        title=title, desc=desc, canon=canon, pixel=PIXEL,
        schema=schema, h1=h1, lead=lead,
        sections=sec_html, faqs=faq_html
    )
    out = pathlib.Path(BASE) / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"  {slug}")


# ── Article 4791 ──────────────────────────────────────────────────────────────
art(
    slug  = "gestao-de-negocios-de-empresa-de-b2b-saas-de-governo-digital-e-govtech",
    title = "Gestão de Negócios de Empresa de B2B SaaS de Governo Digital e GovTech",
    desc  = "Guia completo para gestão de empresas B2B SaaS de governo digital e govtech: estratégias de crescimento, vendas para órgãos públicos e diferenciação.",
    h1    = "Gestão de Negócios de Empresa de B2B SaaS de Governo Digital e GovTech",
    lead  = "O governo digital brasileiro avança rapidamente com iniciativas como o GOV.BR, a transformação digital dos serviços públicos e o crescente uso de dados e IA na gestão pública. Empresas B2B SaaS de govtech têm oportunidade de impactar a vida de milhões de cidadãos — enquanto constroem negócios resilientes com contratos de longo prazo e grande escala.",
    sections = [
        ("O Ecossistema GovTech Brasileiro",
         "O mercado govtech inclui: governo federal (ministérios, autarquias, empresas públicas), estados e municípios, poder judiciário e tribunais, legislativo, e entidades paragovernamentais como o Sistema S (SEBRAE, SENAI, SENAC). Cada esfera tem orçamento, regulação e processo de compra distintos. O governo federal tem os maiores contratos mas os processos mais lentos. Municípios médios (50k-500k habitantes) são frequentemente o melhor ponto de entrada — contratos menores mas ágeis e replicáveis."),
        ("Transformação Digital do Governo: Oportunidades",
         "As principais oportunidades para govtech: plataformas de serviços digitais ao cidadão (eliminando filas e burocracia presencial), gestão de dados e BI para tomada de decisão baseada em evidências, automação de processos administrativos (RPA para governo), inteligência artificial para detecção de fraudes fiscais e previdenciárias, sistemas de saúde pública e educação, e infraestrutura de identidade digital. O Decreto 10.332/2020 e a Estratégia de Governo Digital guiam os investimentos federais em tecnologia."),
        ("Compliance e Segurança no Ambiente Governamental",
         "Soluções para governo exigem conformidade rigorosa: LGPD com proteção reforçada de dados sensíveis de cidadãos, lei de licitações (14.133/2021), conformidade com ABNT NBR ISO/IEC 27001 para segurança da informação, atendimento às normas da ABIN e GSI para sistemas sensíveis, e, para dados classificados, conformidade com as normas de segurança nacional. Obter certificações antes de prospectar grandes órgãos economiza meses no processo de homologação."),
        ("Go-to-Market em GovTech",
         "Estratégias eficazes para govtech: participar de aceleradoras e programas de inovação como InovAtiva Brasil, Startup.Gov.Br e o Laboratório de Inovação do TCU; construir presença em eventos como Conip, ENAP e Fórum de Governo Digital; desenvolver parcerias com grandes integradoras (Stefanini, Totvs, IBM, Accenture) que já têm contratos com o governo e podem incorporar sua solução; e iniciar com projetos-piloto em órgãos inovadores (como o Serpro, Dataprev ou municípios com agenda de inovação ativa)."),
        ("Modelos de Contrato e Receita em GovTech",
         "Contratos com governo têm características específicas: pagamento após entrega verificada (cronograma de medições), reajuste por IPCA ou INPC definido em contrato, prazo máximo de 5 anos para serviços contínuos com opção de prorrogação, e retenção de impostos na fonte. Planeje o fluxo de caixa considerando pagamentos que podem demorar 30-90 dias após medição. Contratos de serviços recorrentes (SaaS em nuvem cobrado mensalmente via empenho) têm crescido no governo, tornando o modelo de receita mais previsível."),
    ],
    faq_list = [
        ("Como uma startup govtech acelera o processo de homologação e qualificação governamental?",
         "As estratégias mais eficazes: (1) participar de programas como o LAB Inovação do governo federal que facilitam POCs sem licitação; (2) usar a modalidade de contratação direta por startups (Lei Complementar 182/2021 — Lei das Startups) que permite pilotos com órgãos públicos sem licitação completa; (3) fazer parceria com uma empresa já homologada como subcontratada; (4) obter certificações de segurança e maturidade (ISO 27001, CMMI) que aceleram a qualificação. O caminho mais rápido é geralmente via laboratórios de inovação dos órgãos, não pela área de licitações."),
        ("Qual é o impacto da rotatividade política no risco de contratos com o governo?",
         "Mudanças de gestão — especialmente após eleições municipais e estaduais — são o maior risco em contratos com governo. Mitigações: contratos de longo prazo com multas de rescisão bem estruturadas, construção de dependência técnica legítima (dados migrados, integrações profundas), relacionamento com múltiplos stakeholders além do gestor principal (técnicos, servidores de carreira que permanecem nas mudanças), e entrega de resultados públicos visíveis que tornam a continuidade politicamente óbvia para qualquer gestão subsequente."),
        ("Vale a pena desenvolver produto exclusivo para o governo ou adaptar um produto comercial?",
         "Adaptar um produto comercial para o governo é geralmente mais eficiente do que criar uma solução exclusiva do zero — especialmente para funcionalidades como autenticação via GOV.BR, emissão de NF-e governamental e integrações com sistemas do Tesouro Nacional. Investimentos exclusivos no produto para governo só se justificam quando o volume de contratos governamentais representa mais de 40% da receita ou quando o problema a resolver é genuinamente único ao setor público. A maioria das necessidades do governo (CRM, BI, gestão de projetos, RPA) pode ser atendida com adaptações de produtos comerciais."),
    ]
)

# ── Article 4792 ──────────────────────────────────────────────────────────────
art(
    slug  = "gestao-de-clinicas-de-psicologia-e-saude-mental",
    title = "Gestão de Clínicas de Psicologia e Saúde Mental",
    desc  = "Guia completo para gestão de clínicas de psicologia e saúde mental: modelos de atendimento, ética, faturamento e crescimento sustentável.",
    h1    = "Gestão de Clínicas de Psicologia e Saúde Mental",
    lead  = "A saúde mental tornou-se uma das maiores demandas de saúde no Brasil pós-pandemia — ansiedade, depressão, burnout e outros transtornos afetam uma parcela crescente da população. Clínicas de psicologia e saúde mental que oferecem atendimento de qualidade, acessível e humanizado têm oportunidade de crescimento expressivo em um mercado ainda com demanda reprimida enorme.",
    sections = [
        ("Modelos de Negócio em Psicologia Clínica",
         "Os principais modelos incluem: consultório individual do psicólogo (mais comum, baixo overhead), clínica com múltiplos psicólogos (escala, marca compartilhada), clínica multidisciplinar de saúde mental (psiquiatria + psicologia + outros), plataformas de telepsicologia (escala nacional), e serviços B2B de saúde mental para empresas (EAP — Employee Assistance Program). Cada modelo tem diferentes estruturas de custo, perfis de paciente e canais de captação. Definir o modelo certo para o mercado local é o primeiro passo estratégico."),
        ("Telepsicologia: Oportunidade e Regulação",
         "A pandemia normalizou o atendimento psicológico por videochamada e o CFP (Conselho Federal de Psicologia) regulamentou definitivamente a prática (Resolução CFP 11/2018 e atualizações). Telepsicologia permite: atender pacientes de qualquer região do Brasil, escalar a prática sem limitação geográfica, reduzir custos de consultório e oferecer mais opções de horário. A principal desvantagem é a perda do vínculo presencial que alguns pacientes e abordagens precisam. Para muitos transtornos (ansiedade, depressão, fobias, questões de relacionamento), o teleatendimento tem eficácia equivalente ao presencial."),
        ("Ética e Compliance em Psicologia",
         "O CFP regula rigorosamente a prática psicológica: código de ética, obrigatoriedade de registro no CRP, proibição de anúncio de resultados terapêuticos prometidos, sigilo profissional absoluto e limitações para atendimento de certos perfis de paciente sem estrutura adequada. Clínicas com múltiplos psicólogos devem garantir supervisão clínica regular, contratos adequados com os psicólogos (PJ ou CLT conforme o vínculo real) e um sistema de prontuário seguro e confidencial. Violações éticas podem resultar em suspensão do CRP — consequência gravíssima para a clínica."),
        ("Saúde Mental Corporativa como Linha de Receita B2B",
         "Empresas investem crescentemente em saúde mental dos funcionários: EAP (Employee Assistance Program), programas de prevenção de burnout, workshops de gestão do estresse, atendimento psicológico como benefício (individual e em grupo), e mensuração de indicadores de saúde mental organizacional. Este segmento B2B tem ticket médio maior e contrato mais previsível do que o atendimento individual. Para clínicas estabelecidas, desenvolver uma linha B2B complementa a clínica individual e diversifica receita."),
        ("Marketing Ético para Clínicas de Psicologia",
         "O marketing em psicologia tem limitações éticas importantes: não é permitido prometer cura ou resultados específicos, nem usar depoimentos de pacientes de forma que comprometam o sigilo. O que é permitido e eficaz: conteúdo educativo sobre saúde mental (temas muito procurados no Google e Instagram), apresentação da abordagem e especialização do psicólogo, informações sobre como funciona o processo terapêutico, e depoimentos que não identifiquem o paciente e sejam sobre a experiência geral (não sobre diagnóstico ou resultado específico). Conteúdo autêntico e empático sobre saúde mental tem altíssimo engajamento."),
    ],
    faq_list = [
        ("Como uma clínica de psicologia pode crescer de forma sustentável?",
         "O crescimento sustentável em psicologia clínica vem de: (1) construir uma base de pacientes em acompanhamento de longo prazo (a maioria dos processos terapêuticos dura de 1 a 3 anos — receita recorrente natural); (2) formar e acolher psicólogos associados que aumentem a capacidade de atendimento mantendo a qualidade; (3) desenvolver a linha B2B de saúde mental corporativa que tem ticket maior; (4) combinar presencial e teleatendimento para maximizar ocupação de agenda; (5) investir em marketing digital ético e consistente que gere demanda contínua de novos pacientes."),
        ("Como precificar sessões de psicologia de forma justa?",
         "O preço de sessões de psicologia varia muito: consultas populares de R$80-R$150, psicólogos experientes de R$200-R$400, especialistas em abordagens específicas ou com reconhecimento de mercado de R$400-R$800/sessão. A precificação deve considerar: formação e experiência do profissional, custo de manutenção do consultório/clínica, demanda local de mercado e posicionamento desejado. Oferecer descontos para atendimento de baixa renda em slots específicos da agenda é uma prática comum e eticamente valorizada que não compromete a renda principal."),
        ("Vale a pena abrir uma clínica com psiquiatria e psicologia integradas?",
         "Sim, a integração psiquiatria-psicologia é considerada o modelo de ouro em saúde mental — a maioria dos transtornos moderados a graves se beneficia de farmacoterapia (psiquiatria) e psicoterapia (psicologia) em conjunto. Clinicamente, é o modelo de maior eficácia. Comercialmente, tem vantagens: maior fidelização (o paciente resolve tudo em um lugar), maior ticket médio por paciente e referências cruzadas entre os profissionais que aumentam a ocupação de agenda. Os desafios são maior investimento inicial e complexidade de gestão da equipe médica e paramédica."),
    ]
)

# ── Article 4793 ──────────────────────────────────────────────────────────────
art(
    slug  = "vendas-para-o-setor-de-saas-de-supply-chain-e-gestao-de-estoques",
    title = "Vendas para o Setor de SaaS de Supply Chain e Gestão de Estoques",
    desc  = "Estratégias de vendas B2B para SaaS de supply chain e gestão de estoques: como vender para distribuidoras, indústrias e varejistas.",
    h1    = "Vendas para o Setor de SaaS de Supply Chain e Gestão de Estoques",
    lead  = "Gestão de estoque e supply chain são áreas onde erros custam caro: excesso de estoque congela capital, ruptura de estoque perde vendas e clientes, e ineficiências na cadeia de suprimentos corroem margens. Empresas que entendem esses problemas e têm um software que os resolve de forma mensurável têm uma proposta de valor clara e urgente para um mercado enorme.",
    sections = [
        ("O Mercado de Supply Chain SaaS",
         "O mercado de supply chain e gestão de estoques é amplo: distribuidoras e atacadistas, indústrias com manufatura e distribuição própria, varejistas omnichannel, empresas de e-commerce, importadores e exportadores. Os problemas mais universais — estoque excessivo em alguns SKUs e ruptura em outros, demanda mal prevista, reposição automática — têm soluções SaaS que podem ser vendidas por problemas específicos, não por projetos de transformação completa."),
        ("A Proposta de Valor em Números",
         "Supply chain SaaS deve ser vendido com ROI financeiro concreto: estoque médio atual × taxa de capital × redução percentual projetada = economia anual. Uma distribuidora com R$10M em estoque médio que reduz 15% com melhor previsão de demanda libera R$1,5M em capital de giro. Adicione: redução de ruptura de X% × margem perdida por venda não realizada. Com esses números, cobrar R$150k/ano por uma ferramenta de S&OP (Sales & Operations Planning) é irresistível."),
        ("Compradores e Influenciadores em Supply Chain",
         "Em empresas médias, o Diretor de Operações ou Logística é o champion principal. Em empresas maiores, o Chief Supply Chain Officer (CSCO) ou Vice-Presidente de Operações. O CFO é sempre um aprovador crítico — e frequentemente o principal aliado quando o argumento é de liberação de capital de giro. Gestores de estoque e planejadores são os usuários finais — sua adoção determina o sucesso da implementação. Invista em envolvê-los na demo e no piloto."),
        ("Demo e Piloto em Supply Chain",
         "Demos de supply chain SaaS devem usar dados reais do cliente: importe o histórico de vendas do prospect (mesmo que em Excel), rode os algoritmos de previsão de demanda e mostre os resultados comparados com o que eles fazem hoje. Um piloto de 90 dias com 10-20% do portfólio de SKUs mostra resultados mensuráveis sem o risco de implementação completa. Métricas do piloto: variação do estoque médio, fill rate (taxa de atendimento de pedidos), accuracy da previsão de demanda vs. baseline anterior."),
        ("Integrações com ERP como Enabler de Vendas",
         "A integração com os ERPs mais usados — SAP, Totvs, Oracle, Protheus, Senior — é frequentemente o requisito técnico número um dos clientes. Uma integração robusta com Protheus (o ERP mais usado em distribuidoras e varejistas brasileiros) e com TOTVS (presente em todo o espectro do mercado) abre um universo de prospects que já têm o ERP como sistema de registro e precisam de analytics e planejamento avançado que os ERPs nativos não entregam. Documente suas integrações prominentemente no site e nas demos."),
    ],
    faq_list = [
        ("Qual é a diferença entre WMS, TMS e S&OP, e qual tem maior demanda?",
         "WMS (Warehouse Management System) gerencia operações dentro do armazém: recebimento, armazenagem, picking e expedição. TMS (Transportation Management System) gerencia o transporte: roteirização, gestão de fretes e rastreamento de embarques. S&OP (Sales & Operations Planning) é o processo de planejamento que alinha demanda e oferta: previsão de vendas, planejamento de produção e gestão de estoques. No Brasil, a maior demanda imediata está em WMS para distribuidoras em crescimento e em ferramentas de S&OP/previsão de demanda para varejistas e indústrias — ambos com ROI mais rápido e proposta de valor mais clara do que TMS puro."),
        ("Como convencer uma distribuidora a trocar de ERP integrado para uma solução especializada de supply chain?",
         "A abordagem mais eficaz é não pedir a substituição — proponha uma camada de analytics e planejamento em cima do ERP existente. Distribuidoras não trocam de ERP facilmente, mas adotam ferramentas que completam o ERP em áreas que ele faz mal. Demonstre que sua solução se integra com o ERP atual, usa os dados que já existem, e entrega previsão de demanda e otimização de estoque que o ERP nativo não consegue. Esta abordagem tem muito menos resistência e ciclo de vendas mais curto do que propor uma migração de ERP."),
        ("Sazonalidade afeta muito a gestão de estoque em quais setores?",
         "Os setores com maior sazonalidade de estoque: varejo (Natal, Dia das Mães, Black Friday), agronegócio (safra e entressafra), turismo e hotelaria (temporada de férias), material escolar (início do ano letivo) e construção civil (primeiro e segundo trimestre). Para empresas nesses setores, algoritmos de previsão de demanda que capturam a sazonalidade são especialmente valiosos — a diferença entre prever bem ou mal a demanda de Natal pode representar milhões de reais em estoque parado ou vendas perdidas. Use esses casos de sazonalidade como gancho de vendas para prospectos nos setores citados."),
    ]
)

# ── Article 4794 ──────────────────────────────────────────────────────────────
art(
    slug  = "consultoria-de-vendas-e-aceleracao-comercial",
    title = "Consultoria de Vendas e Aceleração Comercial",
    desc  = "Como estruturar uma consultoria de vendas e aceleração comercial: metodologia, captação, precificação e diferenciação para empresas B2B e B2C.",
    h1    = "Consultoria de Vendas e Aceleração Comercial",
    lead  = "Vendas é a função que mais impacta o crescimento de qualquer negócio — e também a que mais carece de estrutura e metodologia nas PMEs brasileiras. Consultores de vendas que entregam resultados mensuráveis e reproduzíveis têm demanda constante e clientes altamente motivados, pois o impacto do trabalho é visível no faturamento.",
    sections = [
        ("Diagnóstico Comercial como Ponto de Partida",
         "Um diagnóstico comercial rigoroso revela os gargalos reais: funil de vendas com taxas de conversão por etapa, tempo médio de ciclo de venda, análise de win/loss, perfil do ICP (Ideal Customer Profile) dos clientes atuais, metodologia de precificação e proposta de valor, capacidade da equipe comercial e processos e ferramentas de CRM. Com esse mapa, priorize os 2-3 problemas de maior impacto — resolver o gargalo principal frequentemente dobra os resultados antes de qualquer outra intervenção."),
        ("Estruturação do Processo Comercial",
         "Um processo comercial estruturado inclui: definição clara do ICP e critérios de qualificação (BANT, MEDDIC), playbook de vendas com scripts por etapa do funil, SLAs de follow-up, processo de proposta e negociação, gestão de objeções documentadas, e rituais de gestão (pipeline review semanal, forecast mensal). Equipes que seguem um processo têm performance consistente independente do talento individual — e processos podem ser escalados ao contratar novos vendedores."),
        ("Treinamento e Capacitação Comercial",
         "Treinamentos eficazes de vendas vão além de técnicas de fechamento — incluem: conhecimento profundo do produto e dos clientes, habilidade de descoberta das dores do prospect (perguntas poderosas), técnicas de storytelling e apresentação, gestão do tempo e priorização do pipeline, e uso eficaz das ferramentas (CRM, LinkedIn Sales Navigator, ferramentas de prospecção). Treinamentos com role-play ao vivo e feedback imediato são muito mais eficazes do que exposições teóricas. Acompanhe indicadores antes e depois para medir impacto."),
        ("Captação de Clientes para Consultoria de Vendas",
         "CEOs, Diretores Comerciais e sócios de PMEs que lutam para crescer são os decisores primários. Abordagens eficazes: auditoria de vendas gratuita que revela o gargalo principal (demonstra valor antes de assinar qualquer contrato), cases de aceleração de receita com dados reais (empresa X cresceu Y% em Z meses), e conteúdo sobre os erros mais comuns em vendas B2B (muito compartilhado pelo público-alvo). LinkedIn é o canal principal para prospecção e conteúdo — é onde está o tomador de decisão comercial."),
        ("Modelos de Engajamento e Precificação",
         "Modelos de engajamento em consultoria comercial: projeto único de reestruturação (R$20k-R$80k), retainer mensal de acompanhamento (R$5k-R$20k/mês), treinamentos in-company (R$5k-R$20k por turma), e modelo de success fee (% de receita incremental gerada). O modelo de success fee é o mais lucrativo quando você tem confiança no resultado — mas exige baseline de receita bem definido e métricas de atribuição claras. Combine fee mensal com bônus de performance para alinhar incentivos e garantir renda base."),
    ],
    faq_list = [
        ("Como estruturar um processo de vendas B2B para uma empresa de serviços?",
         "Para empresas de serviços B2B, o processo comercial deve incluir: (1) prospecção ativa via LinkedIn, indicações e eventos do setor; (2) qualificação rigorosa — não todas as oportunidades merecem proposta; (3) reunião de diagnóstico (não de pitch) para entender profundamente a dor do cliente; (4) proposta personalizada baseada no diagnóstico, com ROI quantificado; (5) follow-up estruturado com materiais de suporte que respondem objeções comuns; (6) contrato com escopo e entregáveis claros. Empresas de serviços que implementam este processo geralmente dobram a taxa de conversão de proposta em 90 dias."),
        ("Quantos vendedores uma PME precisa para crescer consistentemente?",
         "A estrutura ideal depende do ticket médio e ciclo de venda. Para ticket médio de R$30k-R$100k com ciclo de 1-3 meses, um Inside Sales sênior pode gerenciar 20-30 oportunidades ativas simultaneamente e fechar 5-10 contratos/mês. Para tickets acima de R$200k, um Account Executive sênior gerencia 15-20 oportunidades e fecha 2-4 por mês. O mais importante não é o número de vendedores — é a qualidade do processo. Uma equipe de 3 vendedores bem treinados com processo estruturado supera 10 vendedores sem metodologia."),
        ("Como medir a eficácia de um programa de treinamento de vendas?",
         "Meça antes e depois: taxa de conversão de lead para oportunidade qualificada, taxa de conversão de proposta para fechamento, ticket médio, tempo médio de ciclo de venda e ramp time de novos vendedores. Um treinamento eficaz melhora pelo menos 2-3 desses indicadores em 60-90 dias. Além dos números, monitore comportamentos: os vendedores fazem mais perguntas de descoberta? Praticam o processo documentado? Usam o CRM corretamente? Comportamentos sustentados levam a resultados sustentados — treinamento que não muda comportamento não muda resultados."),
    ]
)

# ── Article 4795 ──────────────────────────────────────────────────────────────
art(
    slug  = "gestao-de-negocios-de-empresa-de-b2b-saas-de-dados-e-analytics",
    title = "Gestão de Negócios de Empresa de B2B SaaS de Dados e Analytics",
    desc  = "Guia completo para gestão de empresas B2B SaaS de dados e analytics: estratégias de produto, vendas para data teams e crescimento sustentável.",
    h1    = "Gestão de Negócios de Empresa de B2B SaaS de Dados e Analytics",
    lead  = "O mercado de dados e analytics cresce acima de 20% ao ano globalmente, impulsionado pela expansão do data-driven decision making nas empresas. Empresas B2B SaaS neste segmento — desde ferramentas de BI e visualização até plataformas de data engineering e MLOps — têm uma das maiores oportunidades de crescimento no SaaS atual, mas também enfrentam uma concorrência com players globais bem capitalizados.",
    sections = [
        ("Segmentos do Mercado de Dados e Analytics",
         "O ecossistema de dados inclui: Business Intelligence e visualização (Tableau, Power BI, Metabase), data integration e ETL/ELT (Airbyte, Fivetran, dbt), data warehousing em nuvem (Snowflake, BigQuery, Redshift), análise de dados em tempo real (streaming analytics), machine learning e MLOps, observabilidade de dados (data quality, data lineage) e governança de dados. Cada categoria tem diferentes compradores, ciclos de venda e propostas de valor."),
        ("O Comprador de Dados: Data Team e Business",
         "Em empresas data-mature (startups, scale-ups, grandes corporações digitais), o Chief Data Officer (CDO) ou Head of Data lidera as decisões de stack de dados. Em empresas em transformação, é frequentemente o CTO ou Diretor de TI. Um fator único em analytics SaaS: os usuários finais (analistas, data scientists, engenheiros de dados) têm forte influência na escolha — ferramentas que os desenvolvedores amam são adotadas bottom-up. Product-Led Growth funciona especialmente bem neste mercado."),
        ("Diferenciação em um Mercado com Gigantes Globais",
         "Competir diretamente com Tableau, Power BI, Snowflake ou dbt é quase impossível para startups brasileiras. A estratégia é a especialização: ser o melhor produto de BI para um setor vertical específico (saúde, varejo, indústria), ter o pipeline de dados mais simples para PMEs sem engenheiro de dados, ou resolver um problema específico da stack de dados (qualidade de dados em tempo real, governança de dados para LGPD, analytics para dados de PIX/Open Finance). A especialização permite cobrar mais, conquistar clientes mais rápido e construir uma vantagem difícil de replicar."),
        ("Estratégia de Precificação em Analytics SaaS",
         "Modelos de precificação em dados: por usuário ativo (BI e visualização), por volume de dados processados (pipelines de ETL, warehouses), por capacidade de compute (modelos de ML em produção) ou fee fixo por funcionalidade (ferramentas de governança, catálogos de dados). Para o mercado brasileiro, modelos em reais com planos claros e previsíveis têm melhor conversão do que modelos de crédito complexos inspirados em players americanos. Plano gratuito ou trial de 30 dias é quase obrigatório neste mercado — desenvolvedores e analistas precisam testar antes de recomendar para a gestão."),
        ("Open Source como Estratégia de Go-to-Market",
         "Muitas das ferramentas de dados mais bem-sucedidas (dbt, Airbyte, Metabase, Apache Superset) seguem modelo open source com versão paga na nuvem. O open source gera: comunidade de usuários, contribuidores e evangelistas que ampliam o produto, adoção orgânica em empresas que começam com a versão gratuita e convertem para a paga com crescimento, e credibilidade técnica pelo uso de código aberto que profissionais de dados valorizam. Para empresas brasileiras de dados, contribuir para projetos open source relevantes e construir ferramentas abertas na camada certa é uma estratégia de GTM poderosa."),
    ],
    faq_list = [
        ("Como vender analytics SaaS para empresas que ainda não têm maturidade em dados?",
         "Para empresas em estágio inicial de maturidade em dados, o ponto de entrada é simplificar — não oferecer uma plataforma completa mas uma ferramenta focada que resolve um problema específico imediato: conectar o CRM ao BI para ter dashboards de vendas em tempo real, ou integrar dados de e-commerce para acompanhar ROI de marketing por canal. Comece pequeno, mostre valor rápido, e expanda conforme a empresa desenvolve mais capacidade analítica. Empresas que começam com um dashboard simples de vendas evoluem naturalmente para análises mais complexas."),
        ("Qual é a maior dificuldade técnica em vender SaaS de dados para empresas médias?",
         "A maior dificuldade técnica é a integração com as fontes de dados do cliente — especialmente ERPs legados, planilhas espalhadas e sistemas proprietários sem API moderna. Empresas médias raramente têm um data warehouse estruturado; os dados estão em múltiplos sistemas desconectados. Sua solução precisa ter conectores pré-construídos para os sistemas mais comuns (Totvs, Protheus, Oracle, SAP B1) ou um processo de onboarding de dados simplificado. O time de sucesso do cliente deve ter competência técnica para ajudar na integração inicial — é onde a maioria dos projetos de analytics falha."),
        ("Como IA generativa está transformando o mercado de analytics?",
         "IA generativa está redefinindo o analytics de múltiplas formas: consultas em linguagem natural que permitem qualquer usuário de negócio fazer análises sem SQL ou código, geração automática de insights e anomalias a partir de dashboards, chatbots de dados que respondem perguntas de negócio em tempo real, e automação de tarefas repetitivas de data engineering. Ferramentas de analytics que incorporam IA generativa de forma genuinamente útil — não apenas como marketing — têm crescimento acelerado e churn mais baixo. O desafio é a alucinação dos modelos com dados sensíveis de negócio, que requer controles rigorosos de qualidade."),
    ]
)

# ── Article 4796 ──────────────────────────────────────────────────────────────
art(
    slug  = "gestao-de-clinicas-de-medicina-integrativa-e-complementar",
    title = "Gestão de Clínicas de Medicina Integrativa e Complementar",
    desc  = "Guia completo para gestão de clínicas de medicina integrativa: acupuntura, homeopatia, fitoterapia, estrutura, marketing e crescimento sustentável.",
    h1    = "Gestão de Clínicas de Medicina Integrativa e Complementar",
    lead  = "A medicina integrativa e as Práticas Integrativas e Complementares em Saúde (PICS) crescem aceleradamente no Brasil, impulsionadas pela busca por abordagens de saúde mais holísticas, pela inclusão das PICS no SUS (Política Nacional de PICS) e pelo crescente reconhecimento científico de práticas como acupuntura, meditação mindfulness e fitoterapia. Clínicas bem geridas neste segmento têm uma oportunidade de mercado sólida e crescente.",
    sections = [
        ("Regulação das Práticas Integrativas no Brasil",
         "As PICS são reguladas pelo CFM para médicos (Resolução CFM 2.290/2021 lista as práticas reconhecidas) e pelos conselhos de cada profissão para outros profissionais de saúde. Práticas como acupuntura, homeopatia, medicina antroposófica, medicina tradicional chinesa, fitoterapia e termalismo social/crenoterapia têm respaldo regulatório formal. Para clínicas, é fundamental que cada praticante tenha habilitação pelo seu conselho específico — trabalhar com profissionais sem habilitação é risco jurídico grave."),
        ("Estrutura e Mix de Serviços",
         "Uma clínica de medicina integrativa pode oferecer: acupuntura e MTC (Medicina Tradicional Chinesa), homeopatia, fitoterapia, auriculoterapia, reflexologia, práticas de meditação e mindfulness, yoga terapêutica, ayurveda e, para clínicas com médicos, integrações com medicina funcional, nutrologia e ortomolecular. O mix ideal depende dos profissionais disponíveis na região, da demanda local e do posicionamento da clínica. Um mix coerente com uma filosofia integrativa clara é mais convincente do que um catálogo aleatório de práticas."),
        ("Convênios e Faturamento em Medicina Integrativa",
         "O acesso a planos de saúde ainda é limitado para a maioria das práticas integrativas — apenas acupuntura realizada por médico acupunturista tem cobertura obrigatória pela ANS. Homeopatia médica também tem cobertura em alguns planos. A maioria das clínicas integrativas opera predominantemente no mercado particular, com preços acessíveis que reflitam o posicionamento e o público-alvo. Parcerias com empresas para programas de bem-estar corporativo são um canal B2B que permite negociar volumes e expandir acesso."),
        ("Marketing para Medicina Integrativa",
         "O público de medicina integrativa é bem definido: pessoas que buscam saúde holística, prevenção de doenças, gestão de condições crônicas através de abordagens complementares, e bem-estar geral. Instagram, YouTube e Pinterest têm alta penetração neste público — conteúdo sobre os benefícios das práticas (baseado em evidências), rotinas de saúde, meditação guiada e receitas de fitoterapia têm excelente engajamento. Parcerias com influenciadores de bem-estar e saúde holística ampliam muito o alcance de forma orgânica."),
        ("Diferenciação e Posicionamento Premium",
         "Clínicas de medicina integrativa podem se posicionar em diferentes níveis: clínica popular acessível (alto volume, preço baixo), clínica especializada em condições específicas (dor crônica, oncologia integrativa, saúde feminina), ou clínica wellness premium para um público de alto poder aquisitivo que investe em longevidade e qualidade de vida. O posicionamento premium é o mais rentável mas requer: espaço de alta qualidade, profissionais experientes e reconhecidos, serviços exclusivos e marketing alinhado com o público de alta renda."),
    ],
    faq_list = [
        ("Acupuntura tem evidência científica para quais condições?",
         "A OMS (Organização Mundial da Saúde) reconhece evidência científica para acupuntura em mais de 100 condições. As com maior suporte científico incluem: dor crônica (lombalgia, enxaqueca, cervicalgia, osteoartrite), náuseas e vômitos (inclusive quimioterapia), insônia, síndrome do intestino irritável e algumas condições de saúde mental como ansiedade. A Cochrane Database, a maior referência de revisões sistemáticas em saúde, tem múltiplos estudos positivos sobre acupuntura para dor. Comunicar essas evidências de forma clara é importante para credibilidade com pacientes céticos e com médicos que fazem encaminhamentos."),
        ("Como estruturar parcerias com médicos para medicina integrativa?",
         "Parcerias com médicos funcionam em dois modelos: médicos da clínica que oferecem medicina integrativa (acupuntura médica, homeopatia médica, medicina funcional) junto com medicina convencional, ou médicos externos que fazem encaminhamentos para as práticas da clínica. Para o segundo modelo, construa relacionamento com oncologistas (oncologia integrativa é crescente), reumatologistas (dor crônica), ginecologistas (saúde feminina integrativa) e médicos de família. Ofereça relatórios de retorno sobre os pacientes encaminhados para alimentar esse relacionamento."),
        ("Vale a pena obter credenciamento das práticas integrativas no SUS?",
         "Credenciamento no SUS permite atender pacientes que não poderiam pagar pelo serviço particular — impacto social significativo e maior volume de atendimentos. Por outro lado, as tabelas do SUS são muito abaixo do mercado particular e o processo burocrático é complexo. Clínicas que optam pelo credenciamento geralmente operam em modelo misto: atendimentos SUS como contribuição social e compromisso com o acesso à saúde, complementados com atendimentos particulares que mantêm a sustentabilidade financeira. Esta decisão deve ser baseada na missão e nos valores da clínica, não apenas na análise financeira."),
    ]
)

# ── Article 4797 ──────────────────────────────────────────────────────────────
art(
    slug  = "vendas-para-o-setor-de-saas-de-eventos-e-entretenimento",
    title = "Vendas para o Setor de SaaS de Eventos e Entretenimento",
    desc  = "Estratégias de vendas B2B para SaaS de eventos e entretenimento: como vender para produtoras, casas de shows, organizadores e empresas de experiência.",
    h1    = "Vendas para o Setor de SaaS de Eventos e Entretenimento",
    lead  = "O setor de eventos retomou crescimento acelerado pós-pandemia e se modernizou digitalmente. De festivais de música a conferências corporativas, de feiras de negócios a eventos esportivos, a demanda por tecnologia — plataformas de inscrição, gestão de credenciamento, streaming híbrido, análise de audiência — nunca foi tão alta. Para SaaS de eventos, o timing é excelente.",
    sections = [
        ("Segmentos do Mercado de Eventos",
         "O mercado de eventos inclui: eventos corporativos (conferências, congressos, incentivos), eventos culturais e de entretenimento (shows, festivais, teatro), feiras e exposições (B2B e B2C), eventos esportivos, eventos sociais (casamentos, formaturas, aniversários) e eventos educacionais (congressos científicos, feiras de educação). Cada segmento tem compradores, necessidades de tecnologia e ciclos de compra diferentes. Eventos corporativos e feiras têm os maiores orçamentos de tecnologia e processos de compra mais formais.",
         ),
        ("Stack Tecnológica de Eventos",
         "O ecossistema tecnológico de eventos inclui: plataformas de registro e gestão de inscrições, sistemas de credenciamento (QR code, NFC, reconhecimento facial), soluções de streaming para eventos híbridos e virtuais, plataformas de engajamento de audiência (polls, networking, gamificação), sistemas de gestão de fornecedores e produção, ferramentas de analytics pós-evento (dados de audiência, comportamento, leads gerados), e soluções de pagamento e controle de acesso. A tendência é a consolidação dessas funções em plataformas all-in-one."),
        ("Compradores em Eventos: Quem Decide",
         "Dependendo do porte e tipo de evento: Diretor de Marketing ou Eventos para eventos corporativos, Produtor Executivo para eventos de entretenimento, Gerente de Expositores para feiras, e Coordenador de Eventos para eventos menores. O ciclo de compra em eventos tem sazonalidade forte — tecnologia é contratada com 3-6 meses de antecedência para grandes eventos. Prospectar ativamente nos meses que antecedem as principais temporadas de eventos (março-junho e setembro-novembro) é fundamental."),
        ("A Oportunidade do Evento Híbrido",
         "Eventos híbridos — que combinam presença física com participação digital — tornaram-se o novo padrão após a pandemia. Plataformas que gerenciam ambas as experiências de forma integrada têm demanda crescente. A proposta de valor: maior alcance (público que não pode estar fisicamente presente), dados mais ricos de engajamento e ROI melhor para patrocinadores com métricas de audiência online. Para SaaS de eventos que ainda não suporta a dimensão híbrida, esta é a maior oportunidade de desenvolvimento de produto."),
        ("Modelo de Receita em Eventos SaaS",
         "Modelos comuns: fee por evento (modelo transacional — adequado para organizadores esporádicos), assinatura anual por número de eventos ou participantes (melhor para organizadores recorrentes), percentual do ticketing (alinha incentivos mas depende do volume de ingressos), ou SaaS puro com planos por funcionalidades. Para startups, começar com um modelo transacional simples e migrar para assinatura anual conforme a base de clientes cresce é uma estratégia eficaz de monetização progressiva."),
    ],
    faq_list = [
        ("Como diferenciar uma plataforma de gestão de eventos em um mercado com muitos players?",
         "Diferenciação eficaz em eventos SaaS: (1) especialização vertical — ser a melhor plataforma para congressos médicos, ou para festivais de música, ou para feiras industriais — com funcionalidades específicas que a concorrência generalista não tem; (2) experiência do participante superior — app mobile nativo de alta qualidade, networking inteligente, gamificação; (3) analytics de ROI para patrocinadores — uma lacuna enorme no mercado atual; (4) suporte presencial (equipe no evento quando necessário); (5) preço em reais com planos claros vs. players internacionais que cobram em dólar com modelo de preço complexo."),
        ("O mercado de eventos corporativos é mais rentável que eventos de entretenimento?",
         "Eventos corporativos têm maior ticket médio, processo de compra mais formal (mas mais previsível) e menor sazonalidade. Eventos de entretenimento têm maior volume mas margens mais apertadas e alta sazonalidade. Para SaaS de eventos, corporativo é frequentemente o segmento mais rentável porque: tickets de contrato maiores, renovações anuais mais frequentes e menor custo de suporte (clientes corporativos têm equipes internas de eventos mais experientes). Comece com corporativo para construir receita estável e adicione entretenimento como expansão de mercado."),
        ("Como mensurar o ROI de tecnologia de eventos para o organizador?",
         "ROI mensurável de tecnologia de eventos: (1) redução de custo de credenciamento (menos staff, filas menores); (2) aumento de receita de patrocinadores com dados de audiência mais ricos; (3) expansão de alcance com eventos híbridos (mais participantes = mais receita de inscrição e patrocínio); (4) redução de abandono no processo de inscrição (experiência digital melhor = mais conversão); (5) qualidade dos leads gerados para expositores e patrocinadores (dados de engajamento vs. apenas nome e e-mail). Construa um modelo de ROI padrão que seu time de vendas usa em cada pitch."),
    ]
)

# ── Article 4798 ──────────────────────────────────────────────────────────────
art(
    slug  = "consultoria-de-sustentabilidade-e-esg-empresarial",
    title = "Consultoria de Sustentabilidade e ESG Empresarial",
    desc  = "Como estruturar uma consultoria de sustentabilidade e ESG empresarial: serviços, captação de clientes, metodologias e diferenciação no mercado.",
    h1    = "Consultoria de Sustentabilidade e ESG Empresarial",
    lead  = "ESG (Environmental, Social and Governance) deixou de ser nicho de grandes corporações listadas em bolsa e tornou-se agenda central para empresas de todos os portes — impulsionado por exigências de clientes corporativos, acesso a financiamento, regulamentações crescentes e demanda de talentos que querem trabalhar em empresas com propósito. Consultores de ESG têm uma das maiores oportunidades de crescimento profissional e de impacto da consultoria atual.",
    sections = [
        ("O Mercado ESG Brasileiro em Crescimento",
         "O Brasil tem condições únicas para liderança global em ESG: biodiversidade extraordinária, potencial de energia renovável e uma agenda social urgente. O mercado de consultoria ESG cresce acima de 25% ao ano no país. Os drivers principais: regulamentação da CVM para relato de sustentabilidade (Resolução CVM 193/2023), exigências de ESG em cadeias de suprimento globais (fornecedores de empresas europeias precisam demonstrar conformidade com a CSRD), critérios ESG em fundos de private equity e crédito, e pressão de consumidores e talentos."),
        ("Portfólio de Serviços em Consultoria ESG",
         "Os serviços mais demandados incluem: diagnóstico de maturidade ESG, inventário de emissões de gases de efeito estufa (GHG Protocol — Scopes 1, 2 e 3), definição de metas de carbono alinhadas ao SBTi (Science Based Targets initiative), relatório de sustentabilidade (GRI, SASB, TCFD), due diligence ESG para M&A e para investidores, gestão de riscos climáticos (TCFD), programas de diversidade, equidade e inclusão (DE&I), e estratégia de comunicação ESG (evitar greenwashing)."),
        ("Metodologias e Frameworks Internacionais",
         "Domine os frameworks mais usados: GRI (Global Reporting Initiative) — o mais usado mundialmente para relatórios de sustentabilidade, SASB (Sustainability Accounting Standards Board) — específico por setor, TCFD (Task Force on Climate-related Financial Disclosures) — para riscos e oportunidades climáticos, GHG Protocol — para inventários de carbono, SBTi — para validação de metas científicas de redução de emissões, e o IFRS S1 e S2 (novos padrões internacionais de divulgação de sustentabilidade). Certificações como GRI-Certified Sustainability Professional elevam a credibilidade."),
        ("Captação de Clientes em Consultoria ESG",
         "Os melhores prospects são: empresas exportadoras que precisam de conformidade ESG para mercados europeus e americanos, empresas buscando investimento de fundos com critérios ESG, fornecedores de grandes corporações que estão sendo pressionados pela cadeia, e empresas em setores de alto impacto ambiental (agro, mineração, energia, indústria) com incentivo regulatório crescente. Parcerias com consultorias financeiras, bancos (que exigem avaliação ESG para crédito sustentável) e associações setoriais são canais eficazes."),
        ("Greenwashing: O Risco a Evitar",
         "Greenwashing — comunicar práticas sustentáveis exageradas ou falsas — é o maior risco reputacional e jurídico em ESG. Consultores devem orientar clientes a: comunicar apenas o que é verificável e mensurável, ter planos concretos para as metas declaradas, não usar termos vagos como 'eco-friendly' ou 'sustentável' sem substância, e preparar-se para auditorias independentes. A regulamentação contra greenwashing está crescendo globalmente — a CONAR, o Procon e a CVM já têm precedentes de penalização por comunicação ambiental enganosa no Brasil."),
    ],
    faq_list = [
        ("Por onde uma empresa deve começar sua jornada ESG?",
         "O ponto de partida mais prático é um diagnóstico de materialidade: identificar quais temas ESG são mais relevantes para a empresa considerando seu setor, suas operações, seus stakeholders e seus riscos e oportunidades específicos. Com a matriz de materialidade definida, priorize 3-5 temas para ação concreta no primeiro ano — não tente resolver tudo de uma vez. Para empresas com alto impacto ambiental, o inventário de emissões de carbono (GHG Protocol) é frequentemente o primeiro passo prático e obrigatório para qualquer estratégia climática séria."),
        ("ESG é relevante para PMEs ou só para grandes empresas?",
         "ESG é crescentemente relevante para PMEs por três razões práticas: (1) fornecedores de grandes corporações são cobrados por critérios ESG de suas clientes (especialmente em cadeias de exportação); (2) acesso a linhas de crédito sustentável (BNDES, Itaú, Bradesco têm produtos específicos para empresas com práticas ESG) requer demonstração de conformidade; (3) atração e retenção de talentos — especialmente millennials e Gen Z — é fortemente influenciada pela percepção de responsabilidade social e ambiental do empregador. PMEs que ignoram ESG perdem oportunidades concretas de negócio."),
        ("Quanto tempo leva para produzir um relatório de sustentabilidade no padrão GRI?",
         "Um primeiro relatório GRI para uma empresa de médio porte leva de 4 a 8 meses — incluindo definição de escopo, engajamento de stakeholders, coleta de dados de múltiplas áreas da empresa, análise de materialidade, redação e revisão do documento. Empresas com sistemas de gestão maduros (ISO 14001, ISO 45001) têm dados mais organizados e o processo é mais rápido. A partir do segundo ano, o processo é mais ágil porque a estrutura de coleta de dados já está estabelecida. Consultores que têm templates e processos bem definidos reduzem significativamente o esforço do cliente."),
    ]
)

# ── Sitemap + trilha ──────────────────────────────────────────────────────────
import pathlib as _pl

new_slugs = [
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-governo-digital-e-govtech",
    "gestao-de-clinicas-de-psicologia-e-saude-mental",
    "vendas-para-o-setor-de-saas-de-supply-chain-e-gestao-de-estoques",
    "consultoria-de-vendas-e-aceleracao-comercial",
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-dados-e-analytics",
    "gestao-de-clinicas-de-medicina-integrativa-e-complementar",
    "vendas-para-o-setor-de-saas-de-eventos-e-entretenimento",
    "consultoria-de-sustentabilidade-e-esg-empresarial",
]

new_titles = [
    "Gestão de Negócios de Empresa de B2B SaaS de Governo Digital e GovTech",
    "Gestão de Clínicas de Psicologia e Saúde Mental",
    "Vendas para o Setor de SaaS de Supply Chain e Gestão de Estoques",
    "Consultoria de Vendas e Aceleração Comercial",
    "Gestão de Negócios de Empresa de B2B SaaS de Dados e Analytics",
    "Gestão de Clínicas de Medicina Integrativa e Complementar",
    "Vendas para o Setor de SaaS de Eventos e Entretenimento",
    "Consultoria de Sustentabilidade e ESG Empresarial",
]

sitemap_path = _pl.Path(__file__).parent / "sitemap.xml"
trilha_path  = _pl.Path(__file__).parent / "trilha.html"

sm = sitemap_path.read_text(encoding="utf-8")
new_urls = "".join(
    f"\n  <url><loc>{DOMAIN}/blog/{s}/</loc></url>"
    for s in new_slugs
)
sitemap_path.write_text(sm.replace("</urlset>", new_urls + "\n</urlset>"), encoding="utf-8")

tr = trilha_path.read_text(encoding="utf-8")
new_items = "".join(
    f'\n  <li><a href="/blog/{s}/">{t}</a></li>'
    for s, t in zip(new_slugs, new_titles)
)
trilha_path.write_text(tr.replace("</ul>", new_items + "\n</ul>", 1), encoding="utf-8")

print("Done — batch 1654")
