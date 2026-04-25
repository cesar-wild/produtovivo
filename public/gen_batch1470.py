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


# Article 4423 — B2B SaaS: gestão de benefícios e saúde corporativa
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-beneficios-e-saude-corporativa",
    title="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Benefícios e Saúde Corporativa",
    desc="Como escalar um SaaS B2B de gestão de benefícios e saúde corporativa: plataformas de bem-estar, gestão de planos de saúde e programas de saúde ocupacional.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Benefícios e Saúde Corporativa",
    lead="A saúde dos colaboradores tornou-se um imperativo estratégico para empresas que buscam produtividade, retenção de talentos e redução de custos com afastamentos. SaaS de gestão de benefícios e saúde corporativa integram desde a administração de planos de saúde até programas de bem-estar mental e físico, atendendo o RH corporativo em toda a jornada do colaborador.",
    sections=[
        ("O Mercado de Benefícios Corporativos e Saúde no Brasil", "O Brasil tem um dos maiores mercados privados de saúde do mundo — mais de 50 milhões de beneficiários de planos de saúde, com o mercado corporativo representando mais de 70% do total. Além do plano de saúde, empresas oferecem benefícios como vale alimentação, vale refeição, seguro de vida, previdência privada, auxílio academia e programas de saúde mental. A gestão dessas despesas — que representam em média 30-40% do custo total de pessoal — é complexa e demanda plataformas especializadas. O movimento de employee benefits flexíveis (o colaborador escolhe como alocar o budget de benefícios) está crescendo no Brasil, criando demanda por plataformas de benefícios flexíveis."),
        ("Modelo de Produto: Plataforma de Benefícios vs. Health Tech Corporativa", "O mercado se divide entre plataformas de gestão de benefícios (administração de plano de saúde, conciliação de faturas, gestão de elegibilidade e movimentações de beneficiários) e plataformas de saúde corporativa ou well-being (programas de exercício, meditação, acompanhamento nutricional, saúde mental, telemedicina). A convergência é a tendência — plataformas que integram ambas as dimensões (gestão de benefícios + programas de saúde) têm proposta de valor mais ampla e conquistam tanto o RH operacional quanto o RH estratégico. Startups como Gympass/Wellhub e empresas de telemedicina corporativa (Conexa, Docway) competem com plataformas de benefícios tradicionais pelo orçamento de saúde das empresas."),
        ("Proposta de Valor e Argumentos para o RH", "Os argumentos centrais para o RH incluem: redução do custo assistencial por meio de medicina preventiva (cada R$ 1 investido em prevenção economiza R$ 3-5 em tratamento), redução de absenteísmo e presenteísmo (presença física sem produtividade por questões de saúde), melhora no índice de engajamento e retenção de talentos, e capacidade de oferecer benefícios mais atrativos em um mercado de talentos competitivo. Dados de saúde anonimizados e agregados permitem ao RH identificar riscos populacionais e direcionar programas de saúde de forma mais eficaz — inteligência que plataformas baseadas em papel jamais forneceriam."),
        ("Modelo de Receita e Ciclo de Vendas Enterprise", "Plataformas de benefícios corporativos tipicamente cobram uma taxa PMPM (Per Member Per Month) — entre R$ 15 e R$ 80 por beneficiário por mês, dependendo dos módulos contratados. O ciclo de vendas para empresas acima de 500 colaboradores é longo (90 a 180 dias) e envolve RH, financeiro e, frequentemente, o broker/corretora de benefícios que assessora a empresa. Parcerias com corretoras de seguros e benefícios são o principal canal indireto de distribuição — esses profissionais têm relacionamento estabelecido com os decisores de RH e podem recomendar a plataforma de gestão como parte da solução de benefícios."),
        ("Tendências: Saúde Mental Corporativa e Benefícios Flexíveis", "A pandemia colocou a saúde mental no centro da agenda de RH — programas de apoio psicológico (EAP — Employee Assistance Programs) e plataformas de meditação e mindfulness corporativo cresceram mais de 200% desde 2020. Benefícios flexíveis (flex benefits ou cafeteria benefits) permitem que cada colaborador personalize seu pacote conforme suas preferências — uma tendência que valoriza a autonomia e melhora a percepção do benefício pelo colaborador. SaaS que suportam a gestão de benefícios flexíveis com controle orçamentário por colaborador e marketplaces de fornecedores credenciados têm uma das propostas de valor mais diferenciadas do mercado."),
    ],
    faq_list=[
        ("O que é PMPM em plataformas de saúde corporativa?",
         "PMPM (Per Member Per Month) é o modelo de precificação mais comum em plataformas de saúde e benefícios — a empresa paga um valor mensal por cada colaborador beneficiário, independentemente do uso individual. Esse modelo alinha os incentivos da plataforma com a saúde da população de colaboradores."),
        ("Como o SaaS de benefícios pode ajudar a reduzir o custo do plano de saúde corporativo?",
         "Por meio de programas de medicina preventiva (check-ups, rastreamento de doenças crônicas, campanhas de vacinação), telemedicina que resolve casos simples sem uso de serviços hospitalares, gestão de doenças crônicas (diabetes, hipertensão) e identificação de utilizações inadequadas do plano. A redução de sinistralidade gera redução no reajuste anual do plano."),
        ("Benefícios flexíveis são permitidos pela legislação trabalhista brasileira?",
         "Sim, desde que os benefícios legalmente obrigatórios (como alimentação via PAT, quando aplicável) sejam mantidos. Os benefícios adicionais (academia, saúde mental, educação, mobilidade) podem ser oferecidos de forma flexível sem implicações trabalhistas, desde que estruturados corretamente para não caracterizar remuneração fixa."),
    ]
)

# Article 4424 — Clinic: cirurgia vascular e endovascular
art(
    slug="gestao-de-clinicas-de-cirurgia-vascular-e-endovascular",
    title="Gestão de Clínicas de Cirurgia Vascular e Endovascular",
    desc="Guia de gestão para clínicas e centros especializados em cirurgia vascular, endovascular e doenças venosas e arteriais.",
    h1="Gestão de Clínicas de Cirurgia Vascular e Endovascular",
    lead="A cirurgia vascular e endovascular atende pacientes com doenças arteriais (isquemia de membros, aneurismas, carótidas), venosas (varizes, insuficiência venosa crônica, trombose) e linfáticas. A gestão dessas clínicas demanda combinação de infraestrutura diagnóstica especializada, programa cirúrgico de alta complexidade e acompanhamento longitudinal de pacientes crônicos.",
    sections=[
        ("Demanda e Epidemiologia em Cirurgia Vascular no Brasil", "As doenças vasculares são altamente prevalentes na população brasileira envelhecida e sedentária: varizes afetam cerca de 35% dos adultos, a doença arterial periférica (DAP) tem prevalência de 12-15% em maiores de 60 anos, e os aneurismas de aorta abdominal são subdiagnosticados mas têm mortalidade elevada quando rompem. A diabetes e o tabagismo, ainda muito prevalentes no Brasil, são os principais fatores de risco para doenças vasculares graves que exigem intervenção cirúrgica ou endovascular. A demanda por cirurgiões vasculares supera a oferta em muitas regiões, especialmente fora dos grandes centros."),
        ("Mix de Serviços: Ambulatorial, Diagnóstico e Cirúrgico", "Uma clínica vascular completa oferece: consultório com ultrassonografia vascular (duplex scan arterial e venoso) realizado pelo próprio cirurgião ou por tecnólogo vascular treinado, procedimentos ambulatoriais (escleroterapia para varizes, laser endovenoso para varicosidades, curativos de úlceras vasculares), cirurgias abertas em parceria hospitalar (safenectomia, endarterectomia de carótida, bypass arterial, reparo de aneurisma de aorta), e procedimentos endovasculares (angioplastia com stent, EVAR — endovascular aortic repair). A combinação de diagnóstico em consultório e cirurgia em parceria hospitalar é o modelo predominante em clínicas de pequeno e médio porte."),
        ("Gestão do Paciente Crônico Vascular", "Pacientes com doença arterial periférica, insuficiência venosa crônica e sequelas de trombose venosa profunda requerem acompanhamento de longo prazo — ajuste de anticoagulação, monitoramento de recidiva, cuidado de úlceras crônicas e educação sobre fatores de risco. Protocolos de seguimento estruturados (índice tornozelo-braquial semestral, duplex de controle pós-cirúrgico, escalas de qualidade de vida) e integração com outros especialistas (endocrinologistas para diabéticos vasculopatas, cardiologistas para pacientes com múltiplos fatores de risco cardiovascular) são diferenciais que melhoram os desfechos e a fidelização de pacientes."),
        ("Equipamentos Diagnósticos e Gestão do Parque Tecnológico", "O ultrassom vascular duplex é o principal equipamento da clínica vascular — permite diagnóstico de doenças arteriais e venosas com alta resolução e em tempo real, sem radiação. Aparelhos de alta qualidade (GE, Philips, Siemens) custam de R$ 150 mil a R$ 500 mil e têm vida útil de 8 a 12 anos com manutenção adequada. A clínica deve avaliar o custo por exame realizado para garantir o retorno sobre o investimento. Para procedimentos endovasculares, a clínica pode optar por realizar em salas de hemodinâmica hospitalares mediante parceria, evitando o investimento em arco cirúrgico próprio (que pode custar mais de R$ 1 milhão)."),
        ("Faturamento e Sustentabilidade Financeira", "Cirurgia vascular tem boa remuneração pelo SUS e convênios para procedimentos de alta complexidade (aneurisma de aorta, carótida, revascularização de membro). Procedimentos ambulatoriais de médio porte (safenectomia, escleroterapia cirúrgica) têm remuneração intermediária. A ultrassonografia vascular, quando realizada pelo próprio cirurgião, tem boa rentabilidade por ser um procedimento repetível e de alto volume. A clínica deve monitorar regularmente a taxa de glosa de convênios — cirurgias vasculares têm custo de materiais (endopróteses, stents) elevado e a diferença entre o que o convênio reembolsa e o custo real do material pode erodir a margem se não for gerenciada."),
    ],
    faq_list=[
        ("Varizes sempre precisam de cirurgia?",
         "Não. O tratamento de varizes depende da gravidade clínica, dos sintomas (dor, edema, úlceras) e das características anatômicas do sistema venoso. Varizes pequenas podem ser tratadas com escleroterapia. Varizes de tronco com refluxo safeno têm indicação de cirurgia (safenectomia) ou procedimentos minimamente invasivos como laser endovenoso ou radiofrequência."),
        ("O que é EVAR e quando é indicado para aneurisma de aorta?",
         "EVAR (Endovascular Aortic Repair) é o reparo endovascular do aneurisma de aorta abdominal — uma endoprótese é inserida via cateter pela artéria femoral, sem cirurgia aberta. É indicado quando a anatomia do aneurisma é favorável (colo adequado) e o paciente tem condições clínicas de tolerar o procedimento. Tem menor mortalidade perioperatória que o reparo aberto, mas requer acompanhamento por imagem de longo prazo."),
        ("Cirurgia de carótida é indicada para todos os pacientes com placa carotídea?",
         "Não. A endarterectomia de carótida é indicada para pacientes com estenose significativa (geralmente acima de 70%) da artéria carótida interna sintomáticos (AVC ou AIT prévios). Em assintomáticos com estenose severa, a indicação é individualizada pelo cirurgião vascular em conjunto com o neurologista, pesando o risco cirúrgico versus o risco de AVC sem tratamento."),
    ]
)

# Article 4425 — SaaS sales: centros de quimioterapia ambulatorial
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-centros-de-quimioterapia-ambulatorial",
    title="Vendas para o Setor de SaaS de Gestão de Centros de Quimioterapia Ambulatorial",
    desc="Estratégias de vendas B2B para plataformas SaaS voltadas a centros de quimioterapia ambulatorial, infusões oncológicas e farmácias oncológicas hospitalares.",
    h1="Vendas para o Setor de SaaS de Gestão de Centros de Quimioterapia Ambulatorial",
    lead="Centros de quimioterapia ambulatorial são unidades de alta complexidade que gerenciam infusões de medicamentos oncológicos de alto custo, controle rigoroso de protocolos e faturamento complexo para SUS e operadoras. SaaS especializados nesse segmento enfrentam requisitos técnicos exigentes mas conquistam clientes de alto valor e longa retenção.",
    sections=[
        ("O Setor de Oncologia Ambulatorial e Suas Necessidades de Software", "O tratamento ambulatorial do câncer (quimioterapia, imunoterapia, terapias-alvo) cresceu substancialmente com o desenvolvimento de medicamentos que permitem tratar pacientes sem internação prolongada. Centros de quimioterapia ambulatorial — independentes ou integrados a hospitais — gerenciam dezenas a centenas de infusões diárias, com medicamentos de alto custo (R$ 10 mil a R$ 200 mil por ciclo), protocolos específicos para cada tipo de tumor e regime de quimioterapia, e necessidade de autorização prévia rigorosa por parte das operadoras ou do SUS. Esse ambiente cria demanda por software que integre o ciclo clínico (protocolo, prescrição, preparo, infusão) com o ciclo administrativo-financeiro (autorização, dispensação, faturamento)."),
        ("Funcionalidades Críticas para Centros de Quimioterapia", "As funcionalidades mais críticas incluem: gestão de protocolos oncológicos (armazenamento e execução de esquemas de QT baseados em guidelines NCCN, INCA, SBOC), prescrição eletrônica de quimioterapia com cálculo automático de dose por m² ou peso, validação farmacêutica da prescrição antes do preparo, gestão de preparo na farmácia oncológica (manipulação de citostáticos em câmara de segurança biológica), controle de infusão (taxa, volume, tempo por medicamento), gestão de autorizações de convênio (pedido eletrônico, acompanhamento de resposta, recurso de negativa), e faturamento com APAC (Autorização de Procedimento de Alta Complexidade) para o SUS."),
        ("Ciclo de Vendas e Stakeholders em Centros de QT", "O processo de venda em centros de quimioterapia envolve oncologistas (usuários clínicos principais), farmacêuticos oncológicos (usuários críticos da farmácia), enfermeiros de oncologia (usuários da sala de infusão), gestores administrativos (faturamento e autorizações) e diretoria (aprovação do investimento). O farmacêutico oncológico é frequentemente o stakeholder mais técnico e influente na avaliação de sistemas — seu aval é frequentemente determinante para a adoção. Demonstrações devem evidenciar a robustez do módulo de farmácia (validação de prescrição, cálculo de dose, controle de estoque de citostáticos e rastreabilidade por lote)."),
        ("Conformidade Regulatória e Certificações Relevantes", "Centros de quimioterapia são sujeitos a regulação rigorosa: habilitação pelo Ministério da Saúde como CACON ou UNACON (para os que realizam QT), normas da ANVISA para manipulação de quimioterápicos (RDC 220/2004), regulação da CFF (Conselho Federal de Farmácia) para farmácias oncológicas, e normas da CNEN para uso de medicamentos radioativos (quando aplicável). O SaaS deve suportar a geração de relatórios de conformidade exigidos nesses regulamentos, e a certificação do software por órgãos como o SBIS é um diferencial importante para facilitar o processo de venda em instituições altamente reguladas."),
        ("Retenção e Expansão em Centros de Quimioterapia", "A retenção em centros de quimioterapia é excepcionalmente alta — o histórico de protocolos e ciclos de tratamento acumulado por anos no sistema é praticamente impossível de migrar sem risco clínico. Contratos de 3 a 5 anos são comuns. A expansão ocorre com módulos adicionais: tele-oncologia (teleconsulta para pacientes em cidades distantes que fazem QT localmente), portal do paciente oncológico (calendário de infusões, informações sobre efeitos colaterais, canal de comunicação com a equipe), analytics de protocolos (taxa de resposta, toxicidades por protocolo, benchmarking com guidelines) e integração com registros de câncer estaduais e nacionais (RCBP — Registros de Câncer de Base Populacional)."),
    ],
    faq_list=[
        ("O que é APAC e como funciona o faturamento de quimioterapia pelo SUS?",
         "APAC (Autorização de Procedimentos de Alta Complexidade) é o instrumento de faturamento usado para quimioterapia no SUS. O centro de QT emite a APAC com dados do paciente, diagnóstico (CID-10), protocolo de QT e procedimentos realizados, e envia ao gestor local (Secretaria de Saúde) para pagamento. O ciclo de faturamento é mensal e o prazo de pagamento varia por estado."),
        ("Como o SaaS pode ajudar a reduzir as negativas de autorização de quimioterapia pelos convênios?",
         "Módulos de pré-autorização com templates pré-preenchidos por protocolo oncológico, anexos automáticos de laudos e exames de estadiamento, e acompanhamento do status de cada autorização em tempo real reduzem a taxa de negativa por inconsistência documental e diminuem o tempo de espera do paciente pelo início do tratamento."),
        ("Farmácias oncológicas hospitalares precisam de sistema específico ou podem usar ERP hospitalar genérico?",
         "Farmácias oncológicas têm necessidades específicas que ERPs genéricos raramente suportam bem: cálculo de dose por m² ou peso com validação oncológica, rastreabilidade de citostáticos por lote e paciente, controle de estabilidade de preparações (validade após manipulação) e interface com a prescrição médica oncológica. Sistemas específicos entregam mais segurança clínica e menos risco de erro de dose — o principal argumento de venda em um ambiente de alta criticidade."),
    ]
)

# Article 4426 — Consulting: qualidade e excelência operacional
art(
    slug="consultoria-de-gestao-da-qualidade-e-excelencia-operacional",
    title="Consultoria de Gestão da Qualidade e Excelência Operacional",
    desc="Como estruturar e escalar uma consultoria especializada em gestão da qualidade, excelência operacional e certificações como ISO 9001 e Lean Six Sigma.",
    h1="Consultoria de Gestão da Qualidade e Excelência Operacional",
    lead="A gestão da qualidade e a busca pela excelência operacional continuam sendo prioridades para empresas que querem reduzir defeitos, melhorar processos e conquistar certificações que abrem novos mercados. Consultores especializados entregam desde a implementação de ISO 9001 até programas complexos de Lean Six Sigma e kaizen contínuo.",
    sections=[
        ("O Mercado de Consultoria de Qualidade e Excelência Operacional", "O Brasil conta com mais de 20 mil empresas certificadas na ISO 9001 e dezenas de milhares que buscam a certificação anualmente. Setores com maior demanda incluem a indústria de manufatura, autopeças, alimentos, construção civil, saúde (ANVISA exige boas práticas de fabricação) e empresas que fornecem para clientes exigentes em qualidade (montadoras, petroquímicas, exportadoras). Além das certificações, a excelência operacional por metodologias Lean e Six Sigma ganhou espaço em serviços — bancos, hospitais, call centers e empresas de logística adotam estas metodologias para reduzir desperdícios e variabilidade dos processos."),
        ("Portfólio de Serviços de Consultoria de Qualidade", "O portfólio pode incluir: diagnóstico de conformidade com normas ISO (9001, 14001, 45001, 13485 para dispositivos médicos), implementação de SGQ (Sistema de Gestão da Qualidade), preparação para certificação por organismos acreditados pelo INMETRO (como DNV, Bureau Veritas, SGS), treinamento de auditores internos, projetos Lean (mapeamento de fluxo de valor, eliminação de desperdícios, 5S, kanban físico), projetos Six Sigma (DMAIC para redução de variabilidade e defeitos), e implementação de metodologias de excelência como Manufacturing Excellence ou o modelo da Fundação Nacional da Qualidade (FNQ/MEG)."),
        ("Metodologia de Implementação de ISO 9001", "A implementação de ISO 9001 segue etapas: diagnóstico de aderência atual (gap analysis), mapeamento e documentação de processos, treinamento da equipe sobre a norma e seus requisitos, implementação das melhorias necessárias, auditoria interna, auditoria de certificação pelo organismo certificador e manutenção e melhoria contínua pós-certificação. O consultor de qualidade deve adaptar a implementação ao contexto da empresa — evitando a armadilha de criar documentação burocrática que não reflete a realidade dos processos. ISO 9001:2015 é baseada em riscos e contexto, não em procedimentos documentados — uma diferença importante que bons consultores entendem e exploram para tornar o SGQ genuinamente útil para a empresa."),
        ("Lean Six Sigma: Projetos de Melhoria de Alto Impacto", "Projetos Lean Six Sigma seguem a metodologia DMAIC (Define, Measure, Analyze, Improve, Control) para resolver problemas crônicos com dados e ferramentas estatísticas. O consultor identifica projetos de alto impacto — com retorno financeiro claro e medição objetiva de melhoria — e lidera ou mentora as equipes internas na execução. A formação de Black Belts e Green Belts internos é parte do legado de um projeto bem-sucedido. Exemplos de projetos de alto impacto: redução de refugo em linha de produção, redução de tempo de setup (SMED), melhoria de primeiro rendimento em processo de montagem, e redução de tempo de espera em atendimento ao cliente."),
        ("Precificação, Posicionamento e Conquista de Clientes", "Projetos de ISO 9001 para PMEs têm duração típica de 6 a 12 meses e são precificados entre R$ 20 mil e R$ 100 mil dependendo do porte da empresa e da complexidade do sistema de gestão. Projetos Lean Six Sigma são precificados por projeto (com metas de ROI de 5-10x o custo da consultoria) ou por programas de capacitação (formação de Black Belts). O consultor de qualidade deve manter-se atualizado com as normas vigentes (ISO revisa suas normas a cada 5 anos), ter certificações de auditor lead (ISO 9001 Lead Auditor, IRCA) e Black Belt ou Master Black Belt para projetos Lean Six Sigma. Parcerias com organismos certificadores (DNV, Bureau Veritas) criam canais de indicação mútuos."),
    ],
    faq_list=[
        ("A certificação ISO 9001 é obrigatória para participar de licitações públicas?",
         "Não é universalmente obrigatória, mas é frequentemente exigida em licitações de maior porte no setor público — especialmente em setores como construção, indústria e fornecimento de equipamentos. Muitas empresas privadas também exigem ISO 9001 de seus fornecedores como requisito de qualificação."),
        ("Qual é a diferença entre Lean e Six Sigma?",
         "Lean foca na eliminação de desperdícios e na criação de fluxo contínuo de valor. Six Sigma foca na redução de variabilidade e defeitos usando ferramentas estatísticas. O Lean Six Sigma combina as duas abordagens — eliminando desperdícios (Lean) e reduzindo variabilidade (Six Sigma) de forma integrada para maximizar o impacto nos processos."),
        ("Quanto tempo leva a implementação da ISO 9001 em uma empresa de médio porte?",
         "Em empresas de 50 a 500 colaboradores sem SGQ prévio, a implementação leva tipicamente de 8 a 14 meses — incluindo diagnóstico, implementação, auditoria interna e auditoria de certificação. Empresas com processos bem documentados e cultura de qualidade podem certificar em 6 meses; empresas com alta complexidade de processos podem levar 18 meses ou mais."),
    ]
)

# Article 4427 — B2B SaaS: gestão de seguros e insurtechs
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-seguros-e-insurtechs",
    title="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Seguros e Insurtechs",
    desc="Como escalar um SaaS B2B para o mercado de seguros: corretoras, insurtechs, gestão de sinistros e plataformas de distribuição digital de seguros.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Seguros e Insurtechs",
    lead="O mercado de seguros brasileiro é o quinto maior do mundo em prêmios e um dos menos digitalizados em processos de distribuição, subscrição e gestão de sinistros. SaaS e insurtechs que modernizam essa cadeia encontram um mercado vasto, regulado pela SUSEP, e com compradores cada vez mais abertos à inovação tecnológica.",
    sections=[
        ("O Mercado de Seguros Brasileiro e a Oportunidade Tech", "O setor de seguros no Brasil movimenta mais de R$ 450 bilhões em prêmios anuais, com participação crescente de seguros de vida, saúde, automóvel e empresarial. A SUSEP (Superintendência de Seguros Privados) regula o setor e tem adotado agenda de inovação aberta — o sandbox regulatório da SUSEP permite que insurtechs testem novos modelos de negócio com supervisão flexível. A digitalização da jornada de seguro — da cotação ao sinistro — é o principal vetor de inovação, com insurtechs desafiando as seguradoras tradicionais e grandes corretoras com produtos mais simples, distribuição digital e uso intensivo de dados para precificação."),
        ("Segmentos de SaaS no Mercado de Seguros", "O mercado de SaaS para seguros atende diferentes atores: corretoras de seguros (CRM para corretores, gestão de carteira de clientes e apólices, integração com seguradoras via API), seguradoras (core insurance — emissão de apólices, gestão de sinistros, resseguro, contabilidade de seguros), plataformas de distribuição digital (embeded insurance, comparadores de seguro, agregadores), e prestadoras de serviço para o setor (empresas de regulação de sinistros, peritos, prestadores de assistência). Cada segmento tem compradores, processos e necessidades de integração específicos que o SaaS deve suportar."),
        ("Core Insurance: Funcionalidades Essenciais", "Uma plataforma de core insurance deve cobrir: emissão e gestão de apólices (com motor de cotação e subscrição), gestão do ciclo de prêmio (cobrança, inadimplência, cancelamento), gestão de sinistros (registro, regulação, pagamento), comissões e repasse a corretores, resseguro (cessão e recuperação), contabilidade de seguros e relatórios regulatórios para SUSEP e ANS (para saúde). A modernização de legacy systems (muitas seguradoras operam em sistemas mainframe de 30+ anos) é um dos maiores projetos de transformação digital do setor financeiro e cria demanda para fornecedores de core insurance moderno."),
        ("Insurtech: Modelos de Negócio e Posicionamento", "Insurtechs podem posicionar-se em diferentes pontos da cadeia: como MGA (Managing General Agent) com autonomia de subscrição em parceria com seguradoras, como distribuidor digital de produtos de terceiros (comparadores, afiliados), como seguradora digital (requerendo autorização da SUSEP — processo complexo), ou como prestadora de serviços tech para seguradoras (SaaS puro). O seguro embarcado (embedded insurance) — vender seguros no ponto de venda de outro produto (viagem, eletrônicos, automóveis) — é uma das maiores tendências do setor, criando demanda por APIs de seguro que se integram a varejistas e plataformas digitais."),
        ("Regulação, Compliance e Relacionamento com SUSEP", "A regulação do setor de seguros é complexa e a SUSEP possui poderes amplos de supervisão — incluindo inspeções, multas e cassação de licença. SaaS que atendem seguradoras devem suportar os relatórios regulatórios exigidos (DIOPS, FIP, RCS), as normas de solvência e capital mínimo, e os requisitos de segurança da informação do setor financeiro. O relacionamento proativo com a SUSEP — participação em consultas públicas, sandbox regulatório e grupos de trabalho de inovação — é parte da estratégia de negócio de insurtechs que querem operar de forma sustentável e antecipar mudanças regulatórias."),
    ],
    faq_list=[
        ("O que é um sandbox regulatório e como a SUSEP o usa para insurtechs?",
         "O sandbox regulatório da SUSEP permite que insurtechs testem novos produtos e modelos de negócio inovadores sob supervisão especial, com dispensa temporária de algumas exigências regulatórias. Isso permite experimentar e aprender antes de buscar a autorização definitiva, reduzindo o risco regulatório da inovação no setor de seguros."),
        ("Qual é a diferença entre uma corretora de seguros e uma insurtech?",
         "Corretoras de seguros são intermediárias reguladas pela SUSEP que vendem produtos de seguradoras para clientes finais. Insurtechs são empresas de tecnologia que inovam em algum elo da cadeia de valor do seguro — podem ser corretoras digitais, seguradoras digitais, plataformas de gestão ou fornecedoras de dados e IA para o setor. Muitas insurtechs operam como corretoras com tecnologia avançada."),
        ("Seguros embarcados (embedded insurance) precisam de autorização da SUSEP?",
         "Sim. A distribuição de seguros, mesmo em modelo embarcado dentro de outra plataforma, requer que a empresa distribuidora seja uma corretora registrada na SUSEP ou opere em parceria com uma corretora habilitada. A SUSEP publicou normas específicas sobre seguros embarcados (Resolução CNSP 382/2020) que regulam os requisitos para esse modelo."),
    ]
)

# Article 4428 — Clinic: neurologia adulto e doenças cerebrovasculares
art(
    slug="gestao-de-clinicas-de-neurologia-adulto-e-doencas-cerebrovasculares",
    title="Gestão de Clínicas de Neurologia Adulto e Doenças Cerebrovasculares",
    desc="Guia de gestão para clínicas de neurologia adulto especializadas em AVC, epilepsia do adulto, esclerose múltipla e demências.",
    h1="Gestão de Clínicas de Neurologia Adulto e Doenças Cerebrovasculares",
    lead="A neurologia adulto abrange um espectro amplo de condições neurológicas — de doenças cerebrovasculares como AVC e AIT a transtornos degenerativos como demências e Parkinson, epilepsia do adulto e doenças desmielinizantes como a esclerose múltipla. A gestão dessas clínicas exige estrutura para urgências e acompanhamento longitudinal de doenças crônicas complexas.",
    sections=[
        ("Epidemiologia e Demanda em Neurologia Adulto no Brasil", "As doenças neurológicas são a principal causa de incapacidade em adultos no Brasil. O AVC é a segunda causa de morte e a principal causa de incapacidade adquirida; as demências afetam mais de 1,7 milhão de brasileiros; a epilepsia tem prevalência de 1-2% da população adulta; e a esclerose múltipla, embora menos prevalente, tem impacto devastador na qualidade de vida de adultos jovens. A demanda por neurologistas supera amplamente a oferta — o Brasil tem cerca de 12 mil neurologistas para uma população de 215 milhões, uma proporção muito inferior ao recomendado pela OMS. Clínicas bem estruturadas têm ocupação plena e lista de espera crônica."),
        ("Mix de Serviços e Subespecialização", "Uma clínica de neurologia adulto pode oferecer atendimento geral ou especializar-se em subespecialidades de maior complexidade: unidade de AVC (com protocolo de trombólise e suporte para trombectomia mecânica em parceria hospitalar), clínica de epilepsia (com telemetria de EEG prolongada e avaliação pré-cirúrgica de epilepsia refratária), clínica de doenças neurodegenerativas (Parkinson, demências — com avaliação neuropsicológica e programa de reabilitação cognitiva), ou clínica de esclerose múltipla (com protocolo de diagnóstico pela escala McDonald e gestão de drogas modificadoras do curso da doença — DMDs)."),
        ("Infraestrutura e Equipamentos Diagnósticos", "A clínica de neurologia adulto deve ter: eletroencefalógrafo com videomonitoramento (EEG-Vídeo para epilepsia), eletromiografia e eletroneuromiografia (EMG/ENMG para doenças neuromusculares), avaliação neuropsicológica (baterias de testes cognitivos), Doppler transcraniano (DTC para avaliação vascular cerebral não invasiva) e acesso a neuroimagem (RNM de encéfalo com protocolos específicos por doença — protocolo de epilepsia, protocolo de demência, protocolo de EM). A parceria com serviços de neuroimagem de alta qualidade é fundamental — a qualidade do laudo de RNM determina diretamente a qualidade do diagnóstico neurológico."),
        ("Gestão de Urgências Neurológicas: AVC e Status Epilepticus", "A neurologia adulto tem urgências que precisam de resposta rápida — o AVC isquêmico tem janela terapêutica de 4,5 horas para trombólise intravenosa e até 24 horas para trombectomia mecânica em casos selecionados. A clínica deve ter protocolo claro de triagem de sintomas neurológicos urgentes, linha direta com hospital de referência para casos de AVC, e orientação a funcionários e pacientes sobre os sintomas do AVC (SAMU, FAST). Para epilepsia, protocolos de status epilepticus e orientação a familiares sobre benzodiazepínicos de resgate são elementos de segurança fundamentais."),
        ("Sustentabilidade Financeira e Gestão de Medicamentos de Alto Custo", "Neurologia adulto envolve frequentemente medicamentos de alto custo — drogas modificadoras da esclerose múltipla (R$ 30 mil a R$ 100 mil/ano), medicamentos para Parkinson avançado (bombas de infusão de apomorfina ou levodopa-carbidopa intestinal) e novos tratamentos biológicos para epilepsia refratária. A clínica deve orientar pacientes sobre acesso via SUS (RENAME e COMPONENTE ESPECIALIZADO), processos judiciais de fornecimento quando necessário, e programas de acesso da indústria farmacêutica. Esse suporte diferencia a clínica e cria vínculo de confiança com pacientes e familiares que frequentemente se sentem desamparados diante do custo do tratamento."),
    ],
    faq_list=[
        ("Quais são os sintomas de AVC que justificam ida imediata ao pronto-socorro?",
         "Use o método FAST: Face (assimetria facial), Arms (fraqueza em um braço), Speech (alteração da fala), Time (ligue 192 imediatamente). Outros sintomas incluem: visão dupla ou perda súbita de visão, cefaleia súbita e intensa, tontura e instabilidade ao caminhar. Cada minuto conta — o AVC deve ser tratado como emergência."),
        ("Como é feito o diagnóstico de esclerose múltipla?",
         "O diagnóstico de EM segue os critérios de McDonald, que integram dados clínicos (episódios de disfunção neurológica — surtos), ressonância magnética do encéfalo e medula com lesões características, e, quando necessário, análise do liquor (bandas oligoclonais) e potenciais evocados. O neurologista especializado em EM deve ser consultado o mais cedo possível após a suspeita."),
        ("Demência de Alzheimer é a única forma de demência?",
         "Não. O Alzheimer é a causa mais comum de demência (60-70% dos casos), mas existem outras: demência vascular (pós-AVC ou por doença de vasos pequenos), demência com corpos de Lewy, demência frontotemporal, demência por doença de Parkinson e demências potencialmente reversíveis (por hipotireoidismo, deficiência de vitamina B12, hidrocefalia de pressão normal). O diagnóstico diferencial correto é fundamental para o tratamento adequado."),
    ]
)

# Article 4429 — SaaS sales: cirurgia geral e videolaparoscopia
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-cirurgia-geral-e-videolaparoscopia",
    title="Vendas para o Setor de SaaS de Gestão de Clínicas de Cirurgia Geral e Videolaparoscopia",
    desc="Guia de vendas B2B para plataformas SaaS voltadas a clínicas de cirurgia geral, centros de videolaparoscopia e ambulatórios cirúrgicos.",
    h1="Vendas para o Setor de SaaS de Gestão de Clínicas de Cirurgia Geral e Videolaparoscopia",
    lead="Clínicas e ambulatórios de cirurgia geral gerenciam um mix amplo de consultas, procedimentos ambulatoriais e cirurgias eletivas de médio porte. SaaS que integram agendamento cirúrgico, prontuário, faturamento de procedimentos e comunicação pós-operatória têm oportunidade crescente nesse segmento altamente pulverizado.",
    sections=[
        ("Perfil do Mercado de Cirurgia Geral Ambulatorial", "A cirurgia geral ambulatorial abrange hérnias, vesícula, apêndice (eletivo), cirurgias anorretais, procedimentos dermatológicos cirúrgicos e biopsias, entre outros. Com o avanço da videolaparoscopia, procedimentos que antes exigiam internação de 3-5 dias são realizados em regime ambulatorial (same-day surgery), com alta no mesmo dia ou no dia seguinte. Esse modelo — mais confortável para o paciente e mais eficiente economicamente — exige gestão rigorosa da preparação pré-operatória, do centro cirúrgico e do acompanhamento pós-operatório imediato. Clínicas de cirurgia geral ambulatorial competem com hospitais e day hospitals, com diferencial de custo menor e experiência mais personalizada."),
        ("Funcionalidades Essenciais para Clínicas de Cirurgia Geral", "As funcionalidades mais valorizadas incluem: gestão de consultas e triagem cirúrgica, lista de espera para procedimentos com priorização por urgência clínica, prontuário cirúrgico com registro de técnica operatória e materiais utilizados, agendamento de sala cirúrgica com controle de disponibilidade de equipamentos (laparoscópio, instrumental específico), autorização prévia de convênio para procedimentos cirúrgicos, faturamento de honorários médicos e materiais com TUSS correto, acompanhamento pós-operatório (retorno agendado automaticamente), e comunicação com anestesiologistas e equipe de enfermagem cirúrgica. A integração com centros cirúrgicos hospitalares parceiros (quando a clínica não tem centro cirúrgico próprio) é especialmente relevante."),
        ("Processo de Venda e Perfil do Decisor Cirúrgico", "Cirurgiões gerais são profissionais práticos e céticos — preferem ver funcionando a ouvir promessas. A demonstração mais eficaz começa pelo fluxo cirúrgico completo de um paciente: da consulta à autorização do convênio, passando pelo agendamento da cirurgia e chegando ao faturamento da guia. Mostrar como o sistema reduz o tempo gasto com autorizações de convênio (frequentemente o maior ponto de dor) é o argumento mais convincente. Para clínicas com múltiplos cirurgiões, o gestor administrativo é o co-decisor e se importa com controle financeiro, agenda compartilhada e faturamento por médico."),
        ("Integrações Relevantes para o Ecossistema Cirúrgico", "Integrações importantes incluem: sistemas de autorização eletrônica de convênios (via TISS — Troca de Informações em Saúde Suplementar), fornecedores de materiais cirúrgicos (controle de consignação de material de síntese e próteses), sistemas do centro cirúrgico hospitalar parceiro (agenda de sala), anestesiologistas (honorários e relatório anestésico), laboratório de patologia (laudos de biopsias enviados diretamente ao prontuário) e sistemas de imagem (RX, USG, tomografia pré-operatória). A integração com sistemas de planos de saúde via TISS é obrigatória para qualquer clínica que fature por convênio."),
        ("Retenção e Upsell em Clínicas de Cirurgia Geral", "A retenção é favorecida pela acumulação de histórico cirúrgico e de protocolos de técnica operatória específicos do cirurgião no sistema. Módulos de upsell incluem: portal do paciente com orientações pré e pós-operatórias personalizadas, tele-seguimento pós-operatório (consulta de retorno por vídeo para avaliação de ferida e alta cirúrgica), análise de outcomes cirúrgicos (taxa de complicações por tipo de procedimento, tempo de cirurgia por técnica), e integração com banco de dados nacionais de cirurgia (DATASUS para produção ambulatorial). Clínicas que crescem e abrem centros cirúrgicos próprios expandem naturalmente o contrato para módulos de gestão de centro cirúrgico."),
    ],
    faq_list=[
        ("A autorização de convênio para cirurgia laparoscópica é sempre necessária?",
         "Sim, a maioria das operadoras exige autorização prévia para procedimentos cirúrgicos eletivos, inclusive laparoscopias. A solicitação deve incluir justificativa clínica, exames de apoio e código TUSS do procedimento. Alguns planos têm autorização automática para procedimentos de menor complexidade, mas cirurgias de maior porte sempre requerem análise prévia."),
        ("Clínicas de cirurgia geral precisam de CVSA (Centro de Vigilância Sanitária)?",
         "Clínicas cirúrgicas ambulatoriais com sala de procedimentos precisam de licença sanitária da Vigilância Sanitária municipal ou estadual. Os requisitos variam por estado e município, mas geralmente incluem estrutura física adequada, equipamentos de emergência, profissionais habilitados e processos de esterilização certificados."),
        ("Como o SaaS pode ajudar a controlar o material cirúrgico em consignação?",
         "Módulos de controle de consignação registram o material de síntese e próteses enviadas pelo fornecedor, o que foi utilizado em cada cirurgia, e o que precisa ser devolvido. Esse controle evita perdas, facilita a cobrança correta ao convênio (material utilizado no intraoperatório) e simplifica o processo de auditoria com fornecedores de dispositivos médicos implantáveis."),
    ]
)

# Article 4430 — Consulting: gestão de conflitos e mediação empresarial
art(
    slug="consultoria-de-gestao-de-conflitos-e-mediacao-empresarial",
    title="Consultoria de Gestão de Conflitos e Mediação Empresarial",
    desc="Como estruturar uma consultoria especializada em gestão de conflitos empresariais, mediação e arbitragem: metodologia, mercado e posicionamento.",
    h1="Consultoria de Gestão de Conflitos e Mediação Empresarial",
    lead="Conflitos empresariais — entre sócios, com fornecedores, com clientes ou internos entre departamentos — são inevitáveis e podem ser devastadores quando mal gerenciados. Consultores especializados em gestão de conflitos e mediação empresarial ajudam organizações a resolver disputas de forma mais rápida, barata e preservando relacionamentos — uma alternativa valiosa ao litígio judicial.",
    sections=[
        ("O Custo dos Conflitos Não Resolvidos nas Empresas", "Conflitos empresariais têm custos diretos e indiretos elevados. Custos diretos incluem honorários de advogados, custas processuais e o valor da causa em litígios. Custos indiretos incluem tempo da liderança dedicado à disputa em detrimento do negócio, deterioração do clima organizacional, perda de produtividade das equipes envolvidas e danos à reputação quando os conflitos se tornam públicos. Conflitos de sócio-cotistas são particularmente devastadores — podem paralisar o negócio enquanto duram e frequentemente terminam com a dissolução da empresa ou a saída forçada de um dos sócios. A mediação e arbitragem resolvem conflitos de forma mais eficiente que o sistema judicial, que pode levar anos para uma decisão definitiva."),
        ("Mediação, Arbitragem e Outros Métodos Alternativos de Resolução", "A gestão de conflitos empresariais utiliza múltiplos métodos: mediação (processo voluntário facilitado por um mediador neutro onde as partes chegam a um acordo), arbitragem (processo onde um árbitro decide a disputa — decisão vinculante como uma sentença judicial), conciliação (similar à mediação, mas o conciliador pode propor soluções), negociação assistida (suporte técnico nas negociações sem mediador formal), e coaching executivo para conflitos de liderança. A escolha do método depende da natureza do conflito, do relacionamento entre as partes e do resultado desejado — resolução rápida, preservação do relacionamento, ou decisão vinculante definitiva."),
        ("Mediação de Conflitos Societários e Sucessão Empresarial", "Conflitos societários — desacordos sobre divisão de lucros, estratégia, contratação de familiares, sucessão — são o campo mais sensível da mediação empresarial. O mediador deve ter competências técnicas (direito societário, finanças, governança) e habilidades relacionais (empatia, escuta ativa, gestão de emoções) para navegar disputas onde estão em jogo tanto o negócio quanto relações pessoais e familiares de longa data. A mediação de conflitos de empresa familiar é uma subespecialidade de alto valor — empresas familiares representam mais de 80% das empresas brasileiras e têm características únicas de conflito que o mediador precisa compreender profundamente."),
        ("Gestão Preventiva de Conflitos: Contratos e Governança", "A melhor mediação é a que previne o conflito. O consultor de gestão de conflitos pode atuar preventivamente: revisando acordos de sócios para incluir mecanismos de resolução de disputas claros (cláusulas de mediação obrigatória antes de arbitragem), assessorando na estruturação de conselhos de administração e comitês que funcionem como fóruns de resolução de discordâncias estratégicas, e treinando equipes de liderança em comunicação não-violenta e gestão de conflitos internos. Clientes que adotam uma abordagem preventiva têm menos conflitos graves e, quando os têm, os resolvem mais rapidamente."),
        ("Construção da Prática de Mediação e Gestão de Conflitos", "A credibilidade do mediador empresarial é construída por formação reconhecida (certificação pelo CONIMA — Conselho Nacional das Instituições de Mediação e Arbitragem, câmaras de arbitragem como a CAMARB, CAM-CCBC, FGV-ADR), experiência prática em casos reais, e rede de advogados e câmaras de arbitragem parceiros. Publicações sobre mediação de conflitos empresariais e familiares, participação em seminários jurídicos e de governança corporativa, e parcerias com escritórios de advocacia que encaminham casos de mediação são os principais canais de desenvolvimento de negócio nesta especialidade."),
    ],
    faq_list=[
        ("Qual é a diferença entre mediação e arbitragem empresarial?",
         "Na mediação, o mediador facilita o diálogo e as partes chegam a um acordo voluntário — o mediador não decide. Na arbitragem, o árbitro analisa as evidências e decide a disputa — a sentença arbitral tem força de título executivo judicial. Ambas são mais rápidas e privadas que o litígio judicial."),
        ("A mediação empresarial tem validade legal no Brasil?",
         "Sim. A Lei de Mediação (13.140/2015) regulamenta a mediação extrajudicial e judicial no Brasil. Acordos celebrados em mediação extrajudicial constituem título executivo extrajudicial, e a mediação judicial homologada pelo juiz tem força de sentença. As câmaras de mediação e arbitragem são instituições privadas reconhecidas pelo CNJ."),
        ("Conflitos entre sócios de startup podem ser resolvidos por mediação?",
         "Sim. A mediação é especialmente adequada para conflitos entre sócios de startups, onde a preservação do relacionamento e da empresa é prioritária. É recomendável que o acordo de sócios já inclua cláusula de mediação obrigatória antes de qualquer ação judicial, para garantir que conflitos sejam resolvidos de forma menos adversarial e mais rápida."),
    ]
)

# ── Sitemap + trilha ──────────────────────────────────────────────────────────
root = pathlib.Path(__file__).parent
slugs = [
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-beneficios-e-saude-corporativa",
     "Gestão de Negócios de Empresa de B2B SaaS de Gestão de Benefícios e Saúde Corporativa"),
    ("gestao-de-clinicas-de-cirurgia-vascular-e-endovascular",
     "Gestão de Clínicas de Cirurgia Vascular e Endovascular"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-centros-de-quimioterapia-ambulatorial",
     "Vendas para o Setor de SaaS de Gestão de Centros de Quimioterapia Ambulatorial"),
    ("consultoria-de-gestao-da-qualidade-e-excelencia-operacional",
     "Consultoria de Gestão da Qualidade e Excelência Operacional"),
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-seguros-e-insurtechs",
     "Gestão de Negócios de Empresa de B2B SaaS de Gestão de Seguros e Insurtechs"),
    ("gestao-de-clinicas-de-neurologia-adulto-e-doencas-cerebrovasculares",
     "Gestão de Clínicas de Neurologia Adulto e Doenças Cerebrovasculares"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-cirurgia-geral-e-videolaparoscopia",
     "Vendas para o Setor de SaaS de Gestão de Clínicas de Cirurgia Geral e Videolaparoscopia"),
    ("consultoria-de-gestao-de-conflitos-e-mediacao-empresarial",
     "Consultoria de Gestão de Conflitos e Mediação Empresarial"),
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

print("Done — batch 1470")
