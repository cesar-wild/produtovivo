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
<!-- Facebook Pixel Code -->
<script>
!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','{pixel}');fbq('track','PageView');
</script>
<style>
body{{font-family:Arial,sans-serif;margin:0;padding:0;color:#222}}
header{{background:#0a7c4e;padding:16px 24px}}
header a{{color:#fff;text-decoration:none;font-size:1.4rem;font-weight:bold}}
main{{max-width:860px;margin:40px auto;padding:0 20px}}
h1{{font-size:2rem;color:#0a7c4e}}
h2{{font-size:1.3rem;color:#065f3b;margin-top:32px}}
p{{line-height:1.7}}
.lead{{font-size:1.1rem;color:#444}}
.faq{{background:#f4f9f6;border-left:4px solid #0a7c4e;padding:20px 24px;margin-top:40px;border-radius:4px}}
.faq h2{{margin-top:0}}
.faq-item{{margin-bottom:20px}}
.faq-item h3{{font-size:1rem;color:#0a7c4e;margin-bottom:4px}}
footer{{background:#065f3b;color:#cde8da;text-align:center;padding:20px;margin-top:60px;font-size:.9rem}}
</style>
<script type="application/ld+json">{schema}</script>
</head>
<body>
<header><a href="/">ProdutoVivo</a></header>
<main>
<h1>{h1}</h1>
<p class="lead">{lead}</p>
{body}
<div class="faq">
<h2>Perguntas Frequentes</h2>
{faqs}
</div>
</main>
<footer>© 2025 ProdutoVivo · Conteúdo informativo sobre gestão e tecnologia</footer>
</body>
</html>"""


def art(slug, title, desc, h1, lead, sections, faq_list):
    url = f"{DOMAIN}/blog/{slug}/"
    body_html = ""
    for sec_title, sec_body in sections:
        body_html += f"<h2>{sec_title}</h2>\n<p>{sec_body}</p>\n"
    faqs_html = ""
    schema_faqs = []
    for q, a in faq_list:
        faqs_html += f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>\n'
        schema_faqs.append({"@type": "Question", "name": q,
                             "acceptedAnswer": {"@type": "Answer", "text": a}})
    schema = json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
                         "mainEntity": schema_faqs}, ensure_ascii=False)
    html = TMPL.format(title=title, desc=desc, url=url, pixel=PIXEL,
                       h1=h1, lead=lead, body=body_html, faqs=faqs_html, schema=schema)
    out_dir = os.path.join(BASE, slug)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


# Article 4407 — B2B SaaS: aprendizado corporativo e plataformas educacionais
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-aprendizado-corporativo-e-plataformas-educacionais",
    title="Gestão de Negócios de Empresa de B2B SaaS de Aprendizado Corporativo e Plataformas Educacionais",
    desc="Como escalar um negócio de SaaS B2B de aprendizado corporativo e LMS: modelos de receita, mercado-alvo, estratégia de produto e go-to-market.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Aprendizado Corporativo e Plataformas Educacionais",
    lead="O mercado de aprendizado corporativo (corporate learning) cresce aceleradamente com a digitalização do treinamento de colaboradores e a necessidade das empresas de desenvolver competências em ritmo acelerado. SaaS de LMS (Learning Management System) e plataformas de experiência de aprendizado (LXP) atendem desde PMEs até grandes corporações com necessidades sofisticadas de trilhas de desenvolvimento.",
    sections=[
        ("O Mercado de Educação Corporativa no Brasil", "O investimento em treinamento e desenvolvimento (T&D) no Brasil supera R$ 15 bilhões anuais, segundo a ABTD (Associação Brasileira de Treinamento e Desenvolvimento). A pandemia acelerou a migração do treinamento presencial para o digital, criando uma base de clientes que já experimentou plataformas de e-learning e demanda soluções mais sofisticadas — trilhas personalizadas, microlearning, gamificação, aprendizado social e integração com o fluxo de trabalho. O ICP para SaaS de aprendizado corporativo inclui empresas com mais de 50 colaboradores, RH estruturado e cultura de desenvolvimento de pessoas."),
        ("Modelos de LMS e LXP: Diferenciação e Posicionamento", "LMS tradicionais focam no controle — quem fez qual treinamento, com qual nota e quando. LXPs (Learning Experience Platforms) focam na descoberta e personalização — recomendando conteúdos baseados no perfil, cargo e objetivos do colaborador. O mercado brasileiro tem espaço para ambos: LMS para empresas reguladas que precisam de compliance e certificações rastreáveis (bancos, saúde, indústria) e LXP para empresas de tech e serviços que querem cultura de aprendizado contínuo. A tendência é a convergência das duas abordagens em plataformas que oferecem controle e experiência simultaneamente."),
        ("Estratégia de Produto e Conteúdo", "A plataforma sozinha não sustenta o SaaS de aprendizado — o conteúdo é co-determinante do valor percebido. Estratégias de conteúdo incluem: biblioteca de cursos próprios em parceria com produtores de conteúdo, marketplace de cursos de terceiros (Coursera, LinkedIn Learning, Alura), ferramentas de criação de conteúdo interno (authoring tools como Articulate, iSpring ou authoring nativo), e integração com conteúdos externos via xAPI (Experience API). Plataformas que permitem às empresas criar e distribuir conteúdo proprietário com facilidade têm maior stickiness, pois o conteúdo produzido internamente fica hospedado na plataforma e não migra facilmente para concorrentes."),
        ("Vendas B2B para RH e L&D: Processo e Stakeholders", "O ciclo de vendas de LMS corporativo envolve múltiplos stakeholders: RH/T&D (usuário principal), TI (integração e segurança), Jurídico (contratos e privacidade) e CFO (aprovação orçamentária). A entrada mais eficaz é pelo time de L&D ou CHRO, que tem a dor e o orçamento. Propostas de valor quantificadas — horas de treinamento presencial substituídas por digital, redução de custo de deslocamento, aumento de cobertura de treinamento — tornam mais fácil a aprovação financeira. Pilotos pagos (prova de conceito de 60-90 dias com uma trilha específica) convertem bem e demonstram o valor antes do compromisso total."),
        ("Integrações, Parceiros e Expansão de Mercado", "Integrações-chave para LMS corporativo incluem: HRMS e ADP (admissão e demissão automática de usuários), SSO (Active Directory, Okta), Slack e Teams (notificações e microlearning no fluxo de trabalho), ferramentas de videoconferência para aulas ao vivo síncronas, e BI/analytics corporativo para relatórios de desenvolvimento de talentos. Parceiros de implementação (consultorias de RH, integradores de sistemas) ampliam o alcance do produto para PMEs e médias empresas que precisam de suporte na estruturação de sua estratégia de T&D, não apenas da plataforma."),
    ],
    faq_list=[
        ("Qual é a diferença entre LMS e LXP para empresas?",
         "LMS (Learning Management System) foca em controle e conformidade — rastreamento de conclusão de cursos e certificações. LXP (Learning Experience Platform) foca em personalização e descoberta — recomendando conteúdos relevantes para cada colaborador com base em seu perfil e objetivos de desenvolvimento."),
        ("Como precificar um SaaS de aprendizado corporativo?",
         "Os modelos mais comuns são: por usuário ativo por mês, por número total de colaboradores cadastrados, ou por volume de conteúdo armazenado. Contratos anuais com licença para toda a empresa (enterprise-wide) são preferíveis por garantirem receita previsível e motivarem o cliente a maximizar o uso da plataforma."),
        ("O que é xAPI e por que é importante para LMS?",
         "xAPI (Experience API) é um padrão de comunicação de dados de aprendizado que permite registrar qualquer tipo de experiência de aprendizado — vídeos, simuladores, realidade virtual, aprendizado no trabalho — em qualquer sistema. É importante para LMS modernos que querem integrar fontes diversas de conteúdo e rastrear aprendizados além de cursos formais."),
    ]
)

# Article 4408 — Clinic: medicina fetal e ultrassonografia obstétrica avançada
art(
    slug="gestao-de-clinicas-de-medicina-fetal-e-ultrassonografia-obstetrica-avancada",
    title="Gestão de Clínicas de Medicina Fetal e Ultrassonografia Obstétrica Avançada",
    desc="Guia de gestão para clínicas especializadas em medicina fetal, ecocardiografia fetal e ultrassonografia obstétrica de alta resolução.",
    h1="Gestão de Clínicas de Medicina Fetal e Ultrassonografia Obstétrica Avançada",
    lead="A medicina fetal é uma das especialidades médicas de maior crescimento no Brasil, impulsionada pelo avanço tecnológico dos equipamentos de ultrassonografia e pela crescente demanda por diagnóstico pré-natal detalhado. Clínicas especializadas enfrentam o desafio de conciliar equipamentos de alto custo, equipe altamente treinada e gestão de demanda crescente.",
    sections=[
        ("Demanda e Contexto da Medicina Fetal no Brasil", "O diagnóstico pré-natal detalhado — incluindo morfológica de primeiro e segundo trimestres, ecocardiografia fetal, dopplervelocimetria e rastreamento de anomalias cromossômicas — tornou-se padrão de cuidado esperado por gestantes com acesso a planos de saúde privados e até parte do atendimento do SUS em centros de referência. A difusão da ultrassonografia 4D e 5D em clínicas de imagem estética gerou um mercado paralelo de 'ultrassom de lembrança', que a medicina fetal especializada diferencia claramente ao oferecer diagnóstico clínico de qualidade. A procura por medicina fetal aumenta com a idade materna e com a realização de fertilização in vitro."),
        ("Equipamentos e Tecnologia em Medicina Fetal", "Clínicas de medicina fetal de referência operam com equipamentos de ultrassonografia de alta gama (Voluson E10, GE E9, Philips EPIQ), com capacidade de 3D/4D, modo STIC (para ecocardiografia fetal volumétrica) e modo HDlive. O investimento em equipamentos é elevado (R$ 500 mil a R$ 1,5 milhão por aparelho de alto padrão), exigindo planejamento financeiro rigoroso e política clara de depreciação e renovação tecnológica. Parcerias com distribuidores de equipamentos para demonstrações, financiamento e manutenção são parte da gestão estratégica do parque tecnológico da clínica."),
        ("Equipe Especializada e Formação Contínua", "A equipe de uma clínica de medicina fetal inclui médicos com título de especialista em medicina fetal (via Febrasgo/CFM) ou com formação reconhecida em centros de excelência nacionais e internacionais, técnicos e tecnólogos em radiologia com treinamento em ultrassonografia obstétrica, e secretárias com sensibilidade para atendimento de gestantes — muitas vezes ansiosas em relação ao resultado dos exames. A atualização contínua é fundamental — participação em congressos da ISUOG, Figo e Febrasgo, e treinamento em novos protocolos diagnósticos (rastreamento de pré-eclâmpsia no primeiro trimestre, medida do colo uterino) mantém a clínica na fronteira do conhecimento."),
        ("Gestão da Agenda e Experiência da Paciente Gestante", "A gestão da agenda em medicina fetal é especialmente sensível — exames morfológicos de segundo trimestre levam 60 a 90 minutos e exames de ecocardiografia fetal podem levar 45 a 75 minutos. A lotação da agenda sem margem para exames complexos ou para pacientes ansiosas que precisam de mais tempo gera insatisfação e compromete a qualidade diagnóstica. A clínica deve estabelecer slots diferenciados por tipo de exame e treinar a equipe de agendamento para identificar exames de maior complexidade. Comunicação do resultado ao obstetra de referência no mesmo dia e laudos digitais acessíveis via portal são diferenciais de experiência muito valorizados."),
        ("Financiamento, Convênios e Sustentabilidade", "Exames de medicina fetal têm bom reembolso pelos convênios privados quando codificados corretamente. A morfológica fetal de segundo trimestre, a ecocardiografia fetal e os exames de dopplervelocimetria têm tabelas específicas que, quando negociadas adequadamente com as operadoras, permitem remuneração satisfatória. A clínica deve acompanhar os processos de glosa dos convênios atentamente — laudos incompletos e códigos TUSS incorretos são as principais causas de glosa. Serviços de segunda opinião fetal (laudos revisados por especialistas de referência) e consultorias para casos de anomalias detectadas são receitas complementares de alto valor percebido."),
    ],
    faq_list=[
        ("Qual é a diferença entre ultrassom morfológico e o ultrassom de 'memória' 4D?",
         "O ultrassom morfológico é um exame diagnóstico realizado por médico especialista em medicina fetal para avaliar a anatomia do bebê em busca de anomalias estruturais. O ultrassom 4D de 'memória' é um produto estético sem valor diagnóstico, realizado em estúdios sem finalidade médica."),
        ("Com quantas semanas de gestação deve ser feito o ultrassom morfológico de segundo trimestre?",
         "O exame morfológico de segundo trimestre é idealmente realizado entre 20 e 24 semanas de gestação, quando a anatomia fetal está suficientemente desenvolvida para avaliação completa e ainda é possível intervenção ou planejamento do parto em casos de anomalias."),
        ("A ecocardiografia fetal é indicada para todas as gestantes?",
         "A ecocardiografia fetal especializada é indicada para gestantes com fatores de risco: história familiar de cardiopatia congênita, diabetes materno, uso de medicamentos teratogênicos, infecções no primeiro trimestre (rubéola, CMV) e achados sugestivos na morfológica. Em gestações de baixo risco, a avaliação cardíaca fetal pode ser feita durante a morfológica convencional."),
    ]
)

# Article 4409 — SaaS sales: centros de psicomotricidade e estimulação precoce
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-centros-de-psicomotricidade-e-estimulacao-precoce",
    title="Vendas para o Setor de SaaS de Gestão de Centros de Psicomotricidade e Estimulação Precoce",
    desc="Estratégias de vendas B2B para plataformas SaaS voltadas a centros de psicomotricidade, estimulação precoce e desenvolvimento infantil.",
    h1="Vendas para o Setor de SaaS de Gestão de Centros de Psicomotricidade e Estimulação Precoce",
    lead="Centros de psicomotricidade e estimulação precoce atendem bebês e crianças pequenas com atrasos do desenvolvimento, transtornos neuromotores e prematuridade. SaaS que integram avaliação do desenvolvimento, planos de estimulação, comunicação com famílias e controle administrativo atendem uma demanda crescente neste segmento especializado.",
    sections=[
        ("Perfil do Mercado de Estimulação Precoce no Brasil", "A estimulação precoce atende crianças de 0 a 3 anos (e em alguns casos até 6 anos) com risco ou atraso do desenvolvimento neuropsicomotor — prematuros, crianças com síndrome de Down, paralisia cerebral, TEA em suspeita ou diagnóstico precoce e bebês com intercorrências neonatais. O mercado inclui clínicas especializadas, centros de reabilitação infantil, APAEs e organizações sociais. Com o crescimento da consciência sobre a importância do diagnóstico precoce e o aumento de diagnósticos de TEA, a demanda por serviços de estimulação precoce cresceu substancialmente nos últimos anos, criando um mercado receptivo a ferramentas que melhorem a organização e a qualidade do atendimento."),
        ("Funcionalidades Prioritárias para Centros de Estimulação Precoce", "As necessidades específicas deste segmento incluem: ficha de desenvolvimento com escalas validadas (Denver II, Bayley, AIMS para motricidade grossa), plano de estimulação individualizado com metas por área (motora, cognitiva, linguagem, social), registro de sessões com evolução observacional, comunicação com famílias (relatório de progresso, orientações de estimulação em casa), agenda com lembretes automáticos e controle de faltas, e faturamento com controle de pacotes e convênios. A interface deve ser intuitiva para profissionais que passam o dia com crianças e não têm tempo para sistemas complexos."),
        ("Abordagem de Venda e Supressão de Objeções", "O principal obstáculo de venda neste segmento é a resistência de pequenos centros a sistemas digitais — muitos ainda usam fichas em papel e agendas físicas. A abordagem deve começar mostrando como o digital facilita o cotidiano: relatório de evolução para família gerado em 2 minutos, agenda sem conflitos e lembretes automáticos reduzindo faltas. Demonstrações com dados reais de uma criança (fictícia) que progride ao longo de 6 meses de estimulação tornam o valor concreto. O suporte dedicado nas primeiras semanas e a migração assistida dos dados em papel para o sistema são fatores decisivos para a conversão."),
        ("Canais de Distribuição e Comunidades Profissionais", "Os canais mais relevantes incluem: fisioterapeutas pediátricos, terapeutas ocupacionais pediátricos, fonoaudiólogos infantis e psicólogos do desenvolvimento — que são os profissionais que atuam nesses centros. Participação em congressos de reabilitação infantil, grupos de profissionais de neuropediatria e estimulação precoce no WhatsApp, e parceria com APAEs e entidades similares criam acesso qualificado. Nutricionistas infantis, neuropediatras e geneticistas que encaminham crianças para estimulação precoce são influenciadores relevantes no processo de seleção do sistema de gestão."),
        ("Retenção e Impacto Social como Diferencial de Marca", "Centros de estimulação precoce têm alta sensibilidade ao impacto social de seu trabalho — muitos são ONGs ou entidades com fins sociais. SaaS que demonstra impacto não apenas na eficiência administrativa mas também nos desfechos das crianças (relatórios de evolução do desenvolvimento que documentam o progresso das metas de estimulação) tem proposta de valor alinhada com a missão desses centros. Relatórios de impacto social gerados pela plataforma — número de crianças atendidas, áreas de desenvolvimento trabalhadas, percentual de metas atingidas — são ferramentas valiosas para prestação de contas a financiadores, famílias e órgãos públicos."),
    ],
    faq_list=[
        ("Qual é a diferença entre estimulação precoce e fisioterapia pediátrica?",
         "Estimulação precoce é uma abordagem interdisciplinar voltada ao desenvolvimento global da criança (motor, cognitivo, linguagem, social) e envolve múltiplos profissionais. A fisioterapia pediátrica foca especificamente na reabilitação motora. Na prática, muitos centros oferecem ambas de forma integrada."),
        ("SaaS de estimulação precoce precisa ter módulo específico para comunicação com famílias?",
         "Sim, é um dos módulos mais valorizados. Famílias de crianças em estimulação precoce precisam de orientações sobre como estimular em casa, relatórios de evolução compreensíveis e canal de comunicação ágil com a equipe — funcionalidades que aumentam a adesão ao tratamento e a satisfação das famílias."),
        ("Como o SaaS pode ajudar centros de estimulação precoce a obter financiamento público?",
         "Relatórios estruturados de produção (número de atendimentos, perfil das crianças atendidas, desfechos de desenvolvimento) são exigidos por Secretarias de Saúde e assistência social para prestação de contas de convênios públicos. Um SaaS que gera esses relatórios automaticamente facilita enormemente a captação e manutenção de financiamento governamental."),
    ]
)

# Article 4410 — Consulting: gestão de cadeia de suprimentos e compras estratégicas
art(
    slug="consultoria-de-gestao-de-cadeia-de-suprimentos-e-compras-estrategicas",
    title="Consultoria de Gestão de Cadeia de Suprimentos e Compras Estratégicas",
    desc="Como estruturar e desenvolver uma consultoria especializada em supply chain e compras estratégicas: metodologia, mercado e diferenciação.",
    h1="Consultoria de Gestão de Cadeia de Suprimentos e Compras Estratégicas",
    lead="Em um ambiente de cadeias de suprimento globais voláteis, pressão inflacionária e exigências crescentes de sustentabilidade, a gestão de supply chain e compras tornou-se prioridade do C-suite. Consultorias especializadas ajudam empresas a reduzir custos, aumentar resiliência e criar vantagem competitiva por meio de cadeias de suprimento mais inteligentes.",
    sections=[
        ("O Contexto de Alta Demanda por Consultoria de Supply Chain", "A pandemia de COVID-19 expôs a fragilidade de cadeias de suprimento just-in-time altamente concentradas em fornecedores asiáticos. Empresas brasileiras aprenderam na prática o custo da dependência de um único fornecedor, da falta de estoque de segurança e da ausência de planos de continuidade de fornecimento. O resultado é uma demanda crescente por diagnósticos de vulnerabilidade de supply chain, diversificação de fornecedores, nationalização de itens críticos e implementação de sistemas de visibilidade de cadeia. Além disso, pressões ESG aumentam a complexidade — rastreabilidade de fornecedores, conformidade ambiental e trabalhista na cadeia se tornaram requisitos de grandes compradores e investidores."),
        ("Mapeamento e Diagnóstico de Cadeia de Suprimentos", "O diagnóstico começa com o mapeamento da cadeia — identificando fornecedores de primeiro, segundo e terceiro níveis, classificando-os por criticidade (impacto de uma ruptura no negócio) e por vulnerabilidade (probabilidade de ruptura). Ferramentas como análise de risco de concentração de fornecedores, curva ABC de compras, análise de lead times e avaliação de capacidade de substituição rápida fornecem a base para priorização. O resultado é um mapa de riscos da cadeia com planos de mitigação — da diversificação de fornecedores à formação de estoque estratégico de itens críticos."),
        ("Estratégia de Compras e Gestão de Fornecedores", "Compras estratégicas vai além da negociação de preço — envolve segmentação de fornecedores (parceiros estratégicos, fornecedores táticos, commodities), desenvolvimento de fornecedores locais e alternativos, estruturação de contratos com cláusulas de volume, qualidade e continuidade, e criação de programas de supplier development para elevar a capacidade de fornecedores críticos. A aplicação de categorias de compras (category management) permite abordar cada família de insumos com estratégia específica — diferenciando o tratamento de commodities, itens altamente especificados e serviços críticos."),
        ("Digitalização e Tecnologia em Supply Chain", "A digitalização da cadeia de suprimentos é uma das áreas de maior investimento empresarial. O consultor de supply chain deve dominar as tecnologias que transformam o setor: sistemas de planejamento (S&OP, IBP), plataformas de gestão de fornecedores (SRM), ferramentas de visibilidade de cadeia (controle de estoque em trânsito, rastreabilidade end-to-end), IA para previsão de demanda e detecção de riscos, e blockchain para rastreabilidade de origem. Ajudar o cliente a escolher e implementar as ferramentas certas para seu nível de maturidade e seu orçamento é parte central do trabalho do consultor de supply chain moderno."),
        ("Desenvolvimento da Prática de Consultoria de Supply Chain", "Para construir autoridade no mercado, o consultor de supply chain deve combinar expertise técnica (CSCP, CPIM, certificações APICS) com casos de sucesso documentados e publicados. Participação em eventos do IMAM (Instituto de Movimentação e Armazenagem de Materiais), ABRALOG e ABF (para supply chain no varejo/franquias) aumenta a visibilidade. A especialização setorial — supply chain da indústria alimentícia, farmacêutica, de energia ou do agronegócio — permite precificação premium e diferenciação em segmentos onde as especificidades regulatórias e operacionais são relevantes."),
    ],
    faq_list=[
        ("O que é S&OP e por que é importante para supply chain?",
         "S&OP (Sales & Operations Planning) é um processo integrado de planejamento que alinha a demanda comercial com a capacidade de operações e suprimentos. Permite que a empresa antecipe necessidades de compras, produção e logística de forma coordenada, reduzindo rupturas e excesso de estoque."),
        ("Como calcular o TCO (Total Cost of Ownership) em compras estratégicas?",
         "O TCO inclui o preço de compra mais todos os custos associados ao ciclo de vida do item: transporte, armazenagem, manuseio, inspeção de qualidade, manutenção, risco de ruptura e custo de descontinuação. Analisar o TCO ao invés apenas do preço de compra frequentemente revela que fornecedores mais caros têm custo total menor."),
        ("Como a sustentabilidade está mudando a gestão de supply chain?",
         "Grandes empresas e investidores exigem rastreabilidade de fornecedores em relação a critérios ambientais (pegada de carbono, uso de água, desmatamento) e sociais (trabalho digno, diversidade). Isso cria necessidade de programas de qualificação de fornecedores ESG, auditorias de cadeia e sistemas de coleta e reporte de dados de sustentabilidade ao longo da cadeia de suprimentos."),
    ]
)

# Article 4411 — B2B SaaS: inteligência artificial e machine learning aplicada
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-inteligencia-artificial-e-machine-learning-aplicada",
    title="Gestão de Negócios de Empresa de B2B SaaS de Inteligência Artificial e Machine Learning Aplicada",
    desc="Como estruturar e escalar um negócio de SaaS B2B baseado em inteligência artificial e machine learning: produto, go-to-market e métricas.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Inteligência Artificial e Machine Learning Aplicada",
    lead="Empresas que embarcam IA e machine learning em soluções SaaS verticais estão redefinindo setores inteiros — de saúde a logística, de RH a jurídico. Mas construir um negócio sustentável de AI SaaS exige mais do que tecnologia avançada: requer estratégia de produto clara, modelo de dados diferenciado e capacidade de demonstrar valor mensurável para o cliente.",
    sections=[
        ("O Landscape de AI SaaS no Brasil e Globalmente", "O mercado global de AI SaaS cresce em taxas superiores a 30% ao ano, com vertical AI SaaS (IA aplicada a setores específicos) se destacando sobre ferramentas horizontais. No Brasil, aplicações de IA crescem em setores como finanças (detecção de fraude, credit scoring), saúde (diagnóstico por imagem, predição de risco), jurídico (análise de contratos e decisões judiciais), RH (triagem de currículos, análise de engajamento) e agro (sensoriamento remoto, previsão de colheita). A maturidade do mercado para comprar soluções de IA ainda é desigual — algumas verticais têm compradores sofisticados; outras precisam de educação de mercado intensiva antes da venda."),
        ("Modelo de Produto: AI-Native vs AI-Augmented", "SaaS de IA pode ser estruturado como AI-native (o produto só existe por causa da IA — ex: classificação automática de documentos) ou AI-augmented (produto existente com camadas de IA que aumentam valor — ex: CRM com predição de churn). Para startups, o AI-native permite diferenciação mais forte, mas exige investimento maior em dados e modelos. O AI-augmented é mais fácil de vender porque o produto base é compreensível pelo cliente e a IA é um diferencial sobre o que ele já conhece. A escolha impacta diretamente a estratégia de produto, precificação e go-to-market."),
        ("Dados como Ativo Estratégico e Moat Competitivo", "Em negócios de AI SaaS, os dados são o moat competitivo mais robusto. Empresas que acumulam dados proprietários de alta qualidade — dados de uso do produto, dados clínicos anonimizados, históricos de transações — treinam modelos melhores que os concorrentes, criando vantagem crescente com o tempo. A estratégia de dados deve ser pensada desde o início: como coletar, rotular e usar dados dos clientes (com consentimento e conformidade LGPD) para melhorar continuamente os modelos. Modelos treinados em dados de domínio específico superam modelos generalistas — mesmo os de grandes players como OpenAI e Google — em tarefas verticais especializadas."),
        ("Go-to-Market e Venda de Produtos de IA", "Vender AI SaaS é diferente de vender SaaS convencional: o cliente precisa confiar no modelo antes de confiar no produto. Estratégias de go-to-market eficazes incluem: pilotos com dados reais do cliente (onde a IA demonstra performance no contexto específico do comprador), benchmarks comparativos contra o processo manual atual (redução de tempo, aumento de precisão), e construção de confiança gradual — começando por tarefas de menor risco onde o erro tem menor impacto. Transparência sobre como o modelo funciona, quais são suas limitações e como é atualizado aumenta a confiança do comprador técnico e do comprador de negócio."),
        ("Precificação e Métricas de Valor em AI SaaS", "A precificação de AI SaaS frequentemente se baseia em valor entregue — por transação processada, por documento analisado, por predição gerada. Modelos baseados em outcome (pagamento como porcentagem do valor economizado ou gerado) são aspiracionais mas difíceis de operar. O modelo mais comum é consumo baseado em volume, com tier de assinatura para garantir receita mínima. KPIs de saúde do produto incluem: precisão e recall do modelo (métricas de ML), adoção das recomendações da IA pelos usuários (proxy de confiança no modelo), redução mensurada no tempo ou custo do processo automatizado, e NPS específico dos usuários power (que mais dependem da IA)."),
    ],
    faq_list=[
        ("Como uma startup de AI SaaS deve lidar com a dependência de modelos de terceiros (OpenAI, Anthropic)?",
         "A dependência de modelos de fundação (foundation models) de terceiros cria risco de custo e disponibilidade. A estratégia recomendada é usar modelos de terceiros para prototipagem e lançamento rápido, enquanto desenvolve dados e fine-tuning proprietário para reduzir a dependência e criar diferenciação ao longo do tempo."),
        ("LGPD e IA: quais são os cuidados necessários em AI SaaS no Brasil?",
         "A LGPD exige base legal para o processamento de dados pessoais usados no treinamento e inferência de modelos de IA. Decisões automatizadas que afetam direitos dos titulares (crédito, seleção de candidatos) precisam de explicabilidade e possibilidade de revisão humana. A anonimização de dados de treinamento e a documentação do ciclo de vida dos modelos são boas práticas fundamentais."),
        ("Como demonstrar ROI de uma solução de AI SaaS para o comprador?",
         "O ROI deve ser calculado em termos do processo específico sendo automatizado: tempo humano economizado por unidade processada, redução de erros e seu custo downstream, velocidade aumentada de processamento e seu impacto na receita ou satisfação do cliente. Pilotos de 30-60 dias com métricas acordadas previamente são o formato mais convincente para demonstrar ROI de forma objetiva."),
    ]
)

# Article 4412 — Clinic: pneumologia adulto e doenças pulmonares crônicas
art(
    slug="gestao-de-clinicas-de-pneumologia-adulto-e-doencas-pulmonares-cronicas",
    title="Gestão de Clínicas de Pneumologia Adulto e Doenças Pulmonares Crônicas",
    desc="Guia de gestão para clínicas de pneumologia adulto especializadas em asma, DPOC, doenças pulmonares intersticiais e sono.",
    h1="Gestão de Clínicas de Pneumologia Adulto e Doenças Pulmonares Crônicas",
    lead="A pneumologia adulto abrange um espectro amplo de condições — asma, DPOC, doenças pulmonares intersticiais, apneia obstrutiva do sono, pneumonias de repetição e câncer de pulmão. A gestão de clínicas especializadas nessa área demanda infraestrutura diagnóstica robusta, protocolos atualizados e capacidade de acompanhamento longitudinal de pacientes crônicos.",
    sections=[
        ("Epidemiologia e Demanda em Pneumologia no Brasil", "As doenças respiratórias crônicas afetam mais de 40 milhões de brasileiros. A DPOC é a quarta causa de morte no país; a asma afeta mais de 20 milhões de pessoas; as doenças pulmonares intersticiais são cada vez mais diagnosticadas com a difusão da tomografia de alta resolução (TCAR). A pandemia de COVID-19 criou uma nova demanda — acompanhamento de sequelas pulmonares pós-COVID, incluindo fibrose pulmonar pós-inflamatória. Além disso, o crescimento do diagnóstico de apneia do sono impulsionou a criação de laboratórios do sono associados a clínicas de pneumologia, criando um serviço complementar de alto valor agregado."),
        ("Infraestrutura e Exames em Clínicas de Pneumologia", "Uma clínica de pneumologia bem estruturada deve oferecer: espirometria com curva fluxo-volume (essencial para diagnóstico de DPOC e asma), prova de broncodilatação, pletismografia (volumes pulmonares), capacidade de difusão do CO (DLCO para doenças pulmonares intersticiais), poligrafia ou polissonografia para distúrbios do sono, teste de caminhada de 6 minutos (TC6) e oximetria de pulso ambulatorial. Parcerias com serviços de TCAR e PET-CT para estadiamento de câncer de pulmão e com laboratório de análise de escarro complementam a oferta diagnóstica sem demandar investimento próprio em todos os equipamentos."),
        ("Protocolos de Manejo de Doenças Crônicas", "O manejo longitudinal de pacientes com DPOC e asma segue diretrizes do GINA (para asma) e GOLD (para DPOC), atualizadas anualmente. Protocolos de escalonamento e desescalonamento de terapia inalatória, monitoramento de exacerbações, avaliação de técnica inalatória (ponto crítico frequentemente negligenciado) e programas de reabilitação pulmonar são diferenciais assistenciais que melhoram desfechos e reduzem internações. Programas de educação do paciente — sobre o uso correto de dispositivos inalatórios, reconhecimento de sinais de alerta de exacerbação e plano de ação escrito — são comprovadamente eficazes na redução de hospitalizações por asma e DPOC."),
        ("Laboratório do Sono: Oportunidade de Expansão", "O laboratório do sono (polissonografia) é um serviço de alto valor que complementa naturalmente a clínica de pneumologia. A apneia obstrutiva do sono tem prevalência estimada em 30-40% da população adulta e é vastamente subdiagnosticada. O modelo de negócio inclui consultas de triagem (usando escalas como Epworth e STOP-BANG), polissonografia diagnóstica (hospitalar ou ambulatorial com aparelho portátil), titulação de CPAP e acompanhamento de adesão. Parcerias com cardiologistas (apneia e risco cardiovascular), endocrinologistas (síndrome metabólica) e psiquiatras (insônia e transtornos do sono) ampliam o fluxo de encaminhamentos."),
        ("Gestão Financeira e Mix de Atendimento", "Clínicas de pneumologia têm bom potencial de receita por meio de espirometria (procedimento de volume com reembolso adequado por convênios), laboratorio do sono (alto ticket) e consultas de acompanhamento de crônicos. O desafio é a defasagem da tabela CBHPM/TUSS em alguns procedimentos, especialmente para espirometrias realizadas em série. A negociação de pacotes de acompanhamento com operadoras — especialmente para pacientes com DPOC grave que consomem muitos recursos em internações — pode gerar modelos de pagamento capitation ou por resultado que beneficiam tanto a clínica quanto a operadora, ao reduzir custos hospitalares."),
    ],
    faq_list=[
        ("Com que frequência pacientes com DPOC ou asma grave devem consultar o pneumologista?",
         "Pacientes com DPOC estável moderado a grave devem ser avaliados a cada 3-6 meses. Pacientes com asma grave ou de difícil controle necessitam de consultas mais frequentes (a cada 1-3 meses) até estabilização. A telemedicina para retornos de monitoramento tem se mostrado eficaz para reduzir deslocamentos sem comprometer a qualidade do acompanhamento."),
        ("O que é reabilitação pulmonar e quem se beneficia?",
         "Reabilitação pulmonar é um programa multidisciplinar de exercício físico supervisionado, educação e suporte psicossocial para pacientes com doença pulmonar crônica. Pacientes com DPOC moderado a grave, fibrose pulmonar e sequelas pulmonares pós-COVID são os que mais se beneficiam, com melhora comprovada de capacidade funcional, qualidade de vida e redução de internações."),
        ("Quais são os sinais de alerta de câncer de pulmão que o pneumologista deve investigar?",
         "Tosse persistente por mais de 3 semanas, hemoptise, perda de peso não intencional, rouquidão, dor torácica e dispneia progressiva em fumantes ou ex-fumantes são sinais de alerta que justificam investigação com tomografia computadorizada de tórax. O rastreamento de câncer de pulmão por TC de baixa dose é recomendado para fumantes pesados de 50 a 80 anos."),
    ]
)

# Article 4413 — SaaS sales: acupuntura e medicina integrativa
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-acupuntura-e-medicina-integrativa",
    title="Vendas para o Setor de SaaS de Gestão de Clínicas de Acupuntura e Medicina Integrativa",
    desc="Guia de vendas B2B para plataformas SaaS voltadas a clínicas de acupuntura, medicina tradicional chinesa e práticas integrativas de saúde.",
    h1="Vendas para o Setor de SaaS de Gestão de Clínicas de Acupuntura e Medicina Integrativa",
    lead="O mercado de medicina integrativa e práticas complementares — acupuntura, medicina tradicional chinesa, homeopatia, fitoterapia e outras PICs (Práticas Integrativas e Complementares) — cresce no Brasil impulsionado pela Política Nacional de Práticas Integrativas do SUS e pela demanda crescente por abordagens holísticas de saúde. SaaS adaptados a esse nicho têm oportunidade distinta.",
    sections=[
        ("O Mercado de Medicina Integrativa e PICs no Brasil", "O Brasil conta com mais de 30 modalidades de práticas integrativas reconhecidas pelo SUS, e a acupuntura está entre as mais procuradas — realizada por médicos (acupunturistas), fisioterapeutas, enfermeiros e profissionais com formação específica reconhecida pelo CFM e seus equivalentes. O CFM reconhece a acupuntura como especialidade médica; o COFFITO, para fisioterapia; e a enfermagem tem reconhecimento do COFEN. Essa multiplicidade de categorias profissionais cria um mercado heterogêneo de clientes potenciais para SaaS — cada categoria tem suas necessidades específicas de registro e documentação."),
        ("Proposta de Valor e Funcionalidades Específicas", "Um SaaS para medicina integrativa deve oferecer: anamnese em linguagem tradicional chinesa (com campos para constitutição do paciente, diagnóstico energético, mapeamento de meridianos), além do prontuário convencional biomédico. Registro de tratamentos com pontos de acupuntura utilizados, técnicas aplicadas (agulhamento, moxabustão, ventosaterapia, auriculoterapia) e evolução sessão a sessão são funcionalidades essenciais. Para profissionais que trabalham com homeopatia e fitoterapia, módulo de prescrição com banco de fórmulas e posologias típicas aumenta muito o valor percebido do sistema."),
        ("Abordagem de Venda no Nicho de PICs", "Acupunturistas e profissionais de práticas integrativas têm perfil de comprador específico — valorizando muito a filosofia por trás do produto, a sensibilidade cultural da ferramenta e a adequação à linguagem de sua prática. Demonstrações que mostram como o sistema usa termos da medicina tradicional chinesa (qi, yin/yang, meridianos, pontos de acupuntura com nomenclatura internacional e chinesa) criam identificação imediata. Canais digitais como YouTube com conteúdo sobre medicina chinesa e grupos de acupunturistas no Instagram e Facebook são eficazes para construir presença e credibilidade neste nicho."),
        ("Certificações, Regulação e Conformidade", "A prática da acupuntura no Brasil é regulada por diferentes conselhos profissionais conforme a categoria do praticante. O prontuário eletrônico deve atender às exigências de cada conselho — CFM (médicos), COFFITO (fisioterapeutas), COFEN (enfermeiros) e CFMV (médicos veterinários que usam acupuntura em animais). Para clínicas que combinam práticas integrativas com medicina convencional (clínicas integrativas), o sistema precisa suportar prontuários de múltiplas especialidades. A conformidade com a LGPD para dados sensíveis de saúde (diagnóstico energético, histórico de tratamentos) é um requisito básico de compliance."),
        ("Expansão e Ecossistema de Saúde Integrativa", "Clínicas de medicina integrativa frequentemente oferecem múltiplas modalidades — acupuntura, Ayurveda, meditação, yoga terapêutico, reiki, cromoterapia. Um SaaS que suporta todas essas modalidades em um único sistema evita que o profissional precise de múltiplas ferramentas. A expansão de conta ocorre naturalmente à medida que a clínica adiciona novas práticas ou novos profissionais. Parcerias com lojas de insumos para acupuntura (agulhas, moxa, ventosas) e com escolas de formação em MTC criam canais de distribuição orgânica e comunidades de usuários fiéis."),
    ],
    faq_list=[
        ("O SaaS para acupuntura precisa ter os pontos de acupuntura cadastrados com nomenclatura internacional?",
         "Sim. A nomenclatura padronizada pela OMS (ex: LI4, ST36, SP6) deve ser incluída, mas o sistema mais completo oferece também a nomenclatura chinesa (Pinyin e caracteres) e a localização anatômica do ponto, que são referências usadas por diferentes escolas e tradições de acupuntura."),
        ("Acupunturistas que trabalham pelo plano de saúde precisam de funcionalidades específicas no SaaS?",
         "Sim. Faturamento com código TUSS para acupuntura, autorização eletrônica de sessões pelas operadoras e relatórios de produção para prestação de contas são funcionalidades obrigatórias para acupunturistas que atendem por convênio, especialmente em contextos de hospitais e clínicas integradas."),
        ("Como o SaaS pode ajudar clínicas de medicina integrativa a fidelizar pacientes?",
         "Portal do paciente com acesso ao seu histórico de tratamentos, evolução registrada sessão a sessão, orientações personalizadas de fitoterapia ou mudanças de estilo de vida e lembretes automáticos de retorno criam uma experiência de cuidado contínuo que diferencia a clínica integrativa no mercado e aumenta a fidelização dos pacientes."),
    ]
)

# Article 4414 — Consulting: performance comercial e gestão de times de vendas
art(
    slug="consultoria-de-performance-comercial-e-gestao-de-times-de-vendas",
    title="Consultoria de Performance Comercial e Gestão de Times de Vendas",
    desc="Como estruturar uma consultoria especializada em performance comercial e gestão de times de vendas: metodologia, clientes-alvo e desenvolvimento de negócio.",
    h1="Consultoria de Performance Comercial e Gestão de Times de Vendas",
    lead="Times de vendas são o motor da receita de qualquer empresa, mas poucos funcionam no seu potencial máximo. Consultores especializados em performance comercial ajudam empresas a estruturar processos de vendas, desenvolver habilidades dos vendedores, implementar tecnologia de sales enablement e criar cultura de alta performance comercial.",
    sections=[
        ("O Problema de Performance Comercial nas Empresas Brasileiras", "Pesquisas indicam que menos de 30% dos vendedores em empresas brasileiras atingem suas metas regularmente. Os problemas mais comuns incluem: ausência de processo de vendas estruturado (cada vendedor vende do seu jeito), falta de qualificação de leads (tempo desperdiçado com prospects que nunca comprarão), pipeline mal gerenciado (previsões de vendas imprecisas), onboarding inadequado de novos vendedores (levam mais de 6 meses para ser produtivos) e liderança comercial que vende em vez de liderar. O consultor de performance comercial diagnostica a raiz do problema e implementa soluções estruturais — não treinamentos pontuais que não mudam o comportamento."),
        ("Diagnóstico Comercial: Ferramentas e Abordagem", "O diagnóstico começa com análise dos dados de vendas: taxa de conversão por estágio do funil, ciclo médio de vendas por segmento, ticket médio por vendedor, win rate contra principais concorrentes e taxa de churn por coorte de aquisição. Entrevistas com vendedores de diferentes níveis de performance (top performers vs. bottom performers) revelam diferenças de comportamento, processo e crenças limitantes. Análise de chamadas de vendas gravadas (call recordings) e reuniões de pipeline com o time revelarão padrões que os dados sozinhos não mostram. O resultado é um diagnóstico preciso das alavancas de melhoria com maior impacto potencial."),
        ("Estruturação do Processo de Vendas", "Um processo de vendas estruturado define claramente: como leads são qualificados (critérios BANT, MEDDIC ou outro framework), os estágios do funil de vendas com critérios de avanço objetivos, a abordagem de discovery (perguntas que revelam necessidades e urgência do prospect), a estrutura da proposta e os argumentos de valor, o processo de negociação e gestão de objeções, e os critérios de fechamento. O processo deve ser documentado, treinado e monitorado via CRM. Vendedores que seguem um processo estruturado consistentemente superam os que operam por intuição — mesmo os mais talentosos."),
        ("Desenvolvimento de Liderança Comercial", "O maior alavancador de performance comercial é o gerente de vendas. Pesquisas mostram que o gerente explica de 60 a 70% da variância de performance entre times. O consultor de performance comercial investe significativamente no desenvolvimento de líderes comerciais: como fazer coaching de vendas eficaz (sessões de pipeline review, análise de calls), como dar feedback corretivo que muda comportamento, como fazer gestão da performance individual e coletiva, e como construir cultura de accountability sem microgerenciamento. Líderes comerciais que mentoram ativamente seus times multiplicam o impacto do treinamento dos vendedores."),
        ("Sales Technology Stack e Sales Enablement", "A tecnologia de vendas bem implementada amplifica o processo de vendas; mal implementada, cria burocracia sem resultado. O consultor orienta a seleção e implementação do CRM adequado ao perfil e maturidade do time, ferramentas de automação de prospecção, plataformas de sales enablement (conteúdo de vendas na ponta dos dedos do vendedor), ferramentas de análise de chamadas por IA e sistemas de gamificação de metas. A implementação técnica importa menos do que a adoção — e a adoção depende de treinamento, liderança pelo exemplo e integração do CRM ao processo de gestão de pipeline da liderança comercial."),
    ],
    faq_list=[
        ("Como saber se a baixa performance comercial é um problema de processo ou de pessoas?",
         "Se os top performers do time superam consistentemente os demais usando abordagens diferentes, o problema pode ser de pessoas (habilidades ou fit). Se mesmo os melhores vendedores têm dificuldade com os mesmos estágios do funil, o problema é de processo ou oferta. A análise de dados de CRM e observação de chamadas de vendas permite distinguir as duas causas com precisão."),
        ("Quanto tempo leva ver resultados em um projeto de melhoria de performance comercial?",
         "Quick wins em atividade (número de conversas, follow-ups realizados) aparecem em 30-60 dias com a implementação de processo e gestão ativa da liderança. Melhora consistente em taxa de conversão e atingimento de metas tipicamente aparece em 90 a 180 dias, dependendo do ciclo de vendas da empresa."),
        ("Sales enablement é o mesmo que treinamento de vendas?",
         "Não exatamente. Treinamento de vendas foca em habilidades (comunicação, persuasão, gestão de objeções). Sales enablement é mais amplo: inclui treinamento, mas também fornece ao vendedor o conteúdo certo no momento certo (cases, apresentações, propostas) e as ferramentas que tornam sua execução mais eficiente e consistente ao longo de todo o processo de vendas."),
    ]
)

# ── Sitemap + trilha ──────────────────────────────────────────────────────────
root = pathlib.Path(__file__).parent
slugs = [
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-aprendizado-corporativo-e-plataformas-educacionais",
     "Gestão de Negócios de Empresa de B2B SaaS de Aprendizado Corporativo e Plataformas Educacionais"),
    ("gestao-de-clinicas-de-medicina-fetal-e-ultrassonografia-obstetrica-avancada",
     "Gestão de Clínicas de Medicina Fetal e Ultrassonografia Obstétrica Avançada"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-centros-de-psicomotricidade-e-estimulacao-precoce",
     "Vendas para o Setor de SaaS de Gestão de Centros de Psicomotricidade e Estimulação Precoce"),
    ("consultoria-de-gestao-de-cadeia-de-suprimentos-e-compras-estrategicas",
     "Consultoria de Gestão de Cadeia de Suprimentos e Compras Estratégicas"),
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-inteligencia-artificial-e-machine-learning-aplicada",
     "Gestão de Negócios de Empresa de B2B SaaS de Inteligência Artificial e Machine Learning Aplicada"),
    ("gestao-de-clinicas-de-pneumologia-adulto-e-doencas-pulmonares-cronicas",
     "Gestão de Clínicas de Pneumologia Adulto e Doenças Pulmonares Crônicas"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-acupuntura-e-medicina-integrativa",
     "Vendas para o Setor de SaaS de Gestão de Clínicas de Acupuntura e Medicina Integrativa"),
    ("consultoria-de-performance-comercial-e-gestao-de-times-de-vendas",
     "Consultoria de Performance Comercial e Gestão de Times de Vendas"),
]

sitemap_path = root / "sitemap.xml"
sm = sitemap_path.read_text(encoding="utf-8")
new_urls = "".join(
    f"<url><loc>https://produtovivo.com.br/blog/{s}/</loc></url>\n" for s, _ in slugs
)
sitemap_path.write_text(sm.replace("</urlset>", new_urls + "</urlset>"), encoding="utf-8")

trilha_path = root / "trilha.html"
tr = trilha_path.read_text(encoding="utf-8")
new_items = "".join(f'<li><a href="/blog/{s}/">{t}</a></li>\n' for s, t in slugs)
trilha_path.write_text(tr.replace("</ul>", new_items + "\n</ul>", 1), encoding="utf-8")

print("Done — batch 1462")
