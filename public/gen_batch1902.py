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


# ── Batch 1902 — articles 5287–5294 ──────────────────────────────────────────

# 5287 — B2B SaaS: gestão de qualidade / QMS
art(
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-da-qualidade-e-qms",
    "Gestão de Negócios de Empresa de B2B SaaS de Gestão da Qualidade e QMS | ProdutoVivo",
    "Aprenda a construir e escalar um B2B SaaS de gestão da qualidade (QMS): mercado, funcionalidades essenciais, go-to-market e modelos de crescimento sustentável.",
    "Gestão de Negócios de Empresa de B2B SaaS de Gestão da Qualidade e QMS",
    "Normas ISO, ANVISA e regulamentações setoriais impulsionam a demanda por QMS digital. Veja como construir um SaaS lucrativo nesse mercado.",
    [
        ("O Mercado de QMS no Brasil: Normas e Demanda Corporativa",
         "Quality Management Systems (QMS) digitais são exigidos implicitamente por normas como ISO 9001, ISO 13485 (dispositivos médicos), IATF 16949 (automotivo), BPF ANVISA e FSSC 22000 (alimentos). No Brasil, mais de 20.000 empresas possuem certificação ISO 9001 vigente, e dezenas de milhares buscam certificação. Todas precisam gerenciar documentos, não-conformidades, ações corretivas (CAPA), auditorias e indicadores de qualidade. Empresas que ainda usam planilhas Excel representam o maior pool de prospectos para um QMS SaaS."),
        ("Funcionalidades Centrais do QMS SaaS",
         "O produto mínimo viável de um QMS SaaS deve cobrir: gestão de documentos com controle de versão e aprovação eletrônica; registro e tratamento de não-conformidades (NC) e CAPA; gestão de auditorias internas com checklist digital; controle de calibração de equipamentos e instrumentos de medição; gestão de treinamentos e competências da equipe de qualidade; e indicadores e dashboards de KPIs da qualidade. O diferencial competitivo vem de integrações com ERPs (SAP, TOTVS) e de módulos setoriais (ex.: validação de processos para farmacêutica)."),
        ("Segmentação de Mercado e ICP",
         "O QMS SaaS serve múltiplas indústrias, mas é mais eficiente focar em uma ou duas verticais para go-to-market inicial: (1) Indústria farmacêutica e suplementos — altíssima regulação, obrigação de rastreabilidade e validação de sistemas (CSV/GAMP5), tickets maiores; (2) Alimentação e bebidas — FSSC 22000 e HACCP, universo amplo; (3) Manufatura geral — ISO 9001, mercado vasto mas preço sensível; (4) Saúde e dispositivos médicos — ISO 13485, exigente mas disposto a pagar pelo compliance. Comece por uma vertical e expanda com módulos configurados para cada norma."),
        ("Go-to-Market: Certificadoras e Consultores como Canal",
         "Um canal de distribuição poderoso são os consultores de implementação de sistemas de gestão e as certificadoras (Bureau Veritas, DNV, TÜV, BVQI). Esses profissionais recomendam ferramentas para seus clientes diariamente — um programa de parceiros com comissão de 15-20% sobre a primeira anuidade cria um canal de vendas de baixo custo. Inbound via conteúdo técnico (ex.: 'como digitalizarr seu CAPA em conformidade com ISO 13485') atrai leads qualificados prontos para comprar."),
        ("Precificação e Retenção em QMS SaaS",
         "Modelos de precificação por número de usuários, por módulos ativos, ou por volume de documentos gerenciados. Uma clínica ISO 13485 com 20 usuários paga R$1.500-4.000/mês; uma indústria farmacêutica com 100 usuários pode pagar R$15.000-40.000/mês. Churn é baixo (4-7% anual) porque a migração de documentos históricos e logs de auditoria é extremamente custosa para o cliente. Net Revenue Retention superior a 110% é alcançável com upsell de módulos setoriais adicionais."),
    ],
    [
        ("QMS SaaS precisa passar por validação de sistemas (CSV)?",
         "Para clientes do setor farmacêutico e de dispositivos médicos, sim — o QMS é considerado um sistema regulamentado e precisa passar por validação computadorizada conforme GAMP5 e resoluções ANVISA. Oferecer documentação de validação pronta (IQ, OQ, PQ) como parte do onboarding é um diferencial que elimina uma barreira enorme de adoção nesses setores de alto valor."),
        ("Como convencer uma empresa a migrar de planilhas Excel para QMS SaaS?",
         "Mostre o custo oculto das planilhas: tempo de auditoria para localizar documentos, versões desatualizadas circulando por e-mail, impossibilidade de rastrear quem aprovou o quê e quando, e risco de reprovação em auditoria de certificação. Um calculador de ROI mostrando horas economizadas vs. custo do SaaS geralmente fecha a justificativa interna. Ofereça migração assistida dos documentos mais críticos como parte do onboarding."),
        ("ISO 9001 exige um software específico de QMS?",
         "Não, a ISO 9001 não exige nenhuma ferramenta específica. O que ela exige é que os processos de gestão da qualidade sejam documentados, controlados e auditáveis. Na prática, empresas que usam planilhas e documentos físicos têm muito mais dificuldade em demonstrar conformidade durante auditorias. Um QMS digital facilita imensamente a manutenção da certificação e reduz o estresse das auditorias de renovação."),
    ]
)

# 5288 — Clinic: infectologia e medicina tropical
art(
    "gestao-de-clinicas-de-infectologia-e-medicina-tropical",
    "Gestão de Clínicas de Infectologia e Medicina Tropical | ProdutoVivo",
    "Guia completo para gestão de clínicas de infectologia e medicina tropical: estrutura, equipe, serviços, captação de pacientes e crescimento sustentável.",
    "Gestão de Clínicas de Infectologia e Medicina Tropical",
    "Infectologia combina alta complexidade clínica com demanda crescente por HIV, hepatites virais, tuberculose e medicina do viajante.",
    [
        ("O Papel Estratégico da Infectologia no Sistema de Saúde",
         "Infectologia é uma especialidade de alta demanda e relativa escassez de especialistas no Brasil. As principais áreas de atuação ambulatorial incluem: tratamento de HIV/AIDS com TARV, hepatites virais B e C (onde a cura da hepatite C com DAAs criou um mercado específico), tuberculose e micobacterioses, infecções oportunistas em imunossuprimidos, medicina do viajante e vacinas para adultos, e consultoria de antimicrobianos em hospitais. Cada uma dessas áreas tem fluxo de pacientes e modelo de receita distinto."),
        ("Estrutura Física e Requisitos Operacionais",
         "Uma clínica de infectologia de médio porte requer consultórios com ventilação adequada (biossegurança nível 2), sala de procedimentos para coletas e curativos, área de dispensação de medicamentos para pacientes em TARV e DAAs (se credenciada pelo Ministério da Saúde), e sala de espera com privacidade para pacientes sensíveis (HIV, TB). O investimento em estrutura física é moderado (R$200-600K), mas o credenciamento para dispensação de ARVs pelo MS requer habilitação específica no CNES e contrato com a Secretaria de Saúde."),
        ("Modelos de Receita em Infectologia Ambulatorial",
         "A infectologia combina fontes de receita diversas: (1) Consultas convencionais por plano de saúde (ticket menor, volume alto); (2) Medicina do viajante — consultas de orientação pré-viagem, vacinação e prescrição de profilaxias (ticket médio R$350-700, alto potencial em cidades com aeroportos internacionais); (3) Tratamento de hepatite C particular — custos dos DAAs caíram, mas muitos pacientes preferem agilidade na consulta particular e pagam R$400-800 por consulta; (4) Parcerias hospitalares para consultoria de CCIH (Comissão de Controle de Infecção Hospitalar)."),
        ("Programa de Medicina do Viajante: Alta Margem e Diferenciação",
         "Medicina do viajante é um nicho de alto valor com ticket médio de R$500-1.200 por consulta completa (inclui vacinação). O investimento em uma sala de vacinação com câmara fria e registro no CNES como 'Serviço de Saúde do Viajante' habilita a administração de vacinas como febre amarela, hepatite A+B, febre tifoide, meningite e raiva. O público são executivos, turistas e missionários. Marketing digital direcionado a 'consulta médica para viagem internacional' captura esse público com excelente conversão."),
        ("Gestão de Equipe e Desenvolvimento Profissional",
         "Uma clínica de infectologia eficiente combina: infectologista titular (RT), enfermeiro especializado em infecciosas com treinamento em adesão ao TARV, técnico de enfermagem para coletas e vacinações, e assistente social para casos de vulnerabilidade social (HIV, TB). Parcerias com laboratórios de biologia molecular para PCR de hepatites e carga viral de HIV são essenciais — negocie preços diferenciados com volume. A participação da equipe em congressos da SBI (Sociedade Brasileira de Infectologia) mantém o conhecimento atualizado e gera rede de encaminhamentos."),
    ],
    [
        ("Clínica de infectologia precisa de isolamento para atender pacientes com TB?",
         "Para consultas ambulatoriais de TB, recomenda-se sala de atendimento com janelas para ventilação cruzada ou, idealmente, pressão negativa. Na prática, muitos ambulatórios de TB funcionam em salas ventiladas sem pressão negativa, desde que o tempo de permanência do paciente suspeito seja minimizado e haja uso de máscaras PFF2. Para procedimentos que geram aerossóis (broncoscopia, indução de escarro), o isolamento respiratório rigoroso é mandatório."),
        ("Como credenciar uma clínica para dispensar ARVs do programa HIV/AIDS?",
         "O credenciamento para dispensar antirretrovirais do programa governamental exige habilitação no CNES como 'Serviço de Assistência Especializada (SAE) em HIV/AIDS', contrato com a Secretaria Estadual ou Municipal de Saúde, farmacêutico responsável técnico registrado no CRF, e cumprimento de protocolos do Ministério da Saúde (PCDT HIV). O processo leva 3-6 meses, mas garante fluxo contínuo de pacientes do SUS e receita por consultas de acompanhamento."),
        ("Qual o potencial de receita de um consultório de medicina do viajante?",
         "Um infectologista dedicando 2 turnos por semana a medicina do viajante pode atender 8-12 consultas, com ticket médio de R$600-900 (consulta + vacinas). Isso representa R$15.000-45.000 mensais brutos por 2 turnos — uma das maiores relações receita/tempo na medicina ambulatorial. Em cidades como São Paulo, Rio e Brasília, a demanda supera a oferta de especialistas certificados em medicina do viajante."),
    ]
)

# 5289 — SaaS Sales: HCM e gestão de RH
art(
    "vendas-para-o-setor-de-saas-de-hcm-e-gestao-de-recursos-humanos",
    "Vendas para o Setor de SaaS de HCM e Gestão de Recursos Humanos | ProdutoVivo",
    "Estratégias de vendas B2B para SaaS de HCM e gestão de RH: como prospectar CHROs, demonstrar valor e fechar contratos de longa duração com empresas de médio e grande porte.",
    "Vendas para o Setor de SaaS de HCM e Gestão de Recursos Humanos",
    "O mercado brasileiro de HRTech cresceu 35% em 2024. Saiba como vender SaaS de gestão de pessoas para empresas que ainda dependem de planilhas e sistemas legados.",
    [
        ("O Ecossistema HRTech no Brasil",
         "O mercado de HRTech brasileiro é diversificado: folha de pagamento e ponto eletrônico (altamente competitivo, dominado por ADP, Sênior e Totvs), recrutamento e seleção (ATS — Applicant Tracking Systems), gestão de desempenho e OKR, engajamento e clima organizacional, gestão de benefícios flexíveis, e plataformas de HCM full-suite. Cada subvertical tem dinâmica própria de vendas. O maior potencial de crescimento está em soluções de people analytics, engajamento e gestão de desempenho — áreas onde sistemas legados de folha são fracos."),
        ("Mapeando os Decisores em RH",
         "Em empresas de 200-1.000 colaboradores, o CHRO ou Diretor de RH decide com suporte do gerente de sistemas/TI. Em PMEs com 50-200 colaboradores, frequentemente é o gerente de RH ou o próprio CEO. Key influencers: gerentes de T&D (para plataformas de aprendizagem), BPs de RH (para ferramentas de performance) e especialistas de folha (para DP digital). Identifique quem sente mais a dor antes de personalizar o pitch — um gerente de recrutamento que perde candidatos por processo lento é um champion diferente do gerente de folha que quer automatizar cálculos complexos."),
        ("Abordagem de Descoberta e Qualificação",
         "Use o framework MEDDIC adaptado: Metrics (que KPIs de RH estão abaixo do esperado?), Economic Buyer (quem aprova o orçamento?), Decision Criteria (o que o cliente prioriza — facilidade de uso, integração com folha, compliance eSocial?), Decision Process (há RFP? Quantos fornecedores estão sendo avaliados?), Identify Pain (qual a dor que custa mais em R$ ou tempo?), Champion (quem vai defender internamente?). Uma descoberta bem feita economiza demos genéricas e aumenta a taxa de fechamento."),
        ("Demo Focada em Dores Reais de RH",
         "A demo de HCM SaaS deve simular o dia a dia do cliente: processo de admissão digital (eliminar papelada), gestão de ponto integrada com folha (reduzir horas de conciliação manual), ciclo de avaliação de desempenho com calibração de lideranças, e relatório de people analytics para o board. Mostre conformidade com eSocial, LGPD e CLT — o RH brasileiro é altamente regulado e compliance é critério eliminatório. Um piloto de 60 dias com um HRBP e 50 colaboradores prova o valor antes do commit anual."),
        ("Ciclo de Vendas e Estratégia de Expansão",
         "O ciclo de vendas de HCM varia de 45 dias (PME decidindo rapidamente) a 6-12 meses (enterprise com múltiplos comitês). Para encurtar o ciclo, ofereça ROI calculator com estimativa de horas economizadas em processos manuais de RH — em empresas com DP de 3-5 pessoas, a economia pode justificar o investimento em uma planilha. Depois da venda inicial, expanda para módulos complementares a cada renovação: empresa que começa com recrutamento pode evoluir para performance, depois para LMS e eventually para HCM full suite."),
    ],
    [
        ("Qual a diferença entre HRIS, HCM e HRMS?",
         "HRIS (Human Resource Information System) foca em dados dos colaboradores e processos transacionais (admissão, demissão, folha). HCM (Human Capital Management) inclui tudo do HRIS mais gestão de talentos, performance, aprendizagem e planejamento de força de trabalho. HRMS (Human Resource Management System) é um termo mais antigo, geralmente sinônimo de HRIS. Na prática de vendas, HCM é o termo mais usado para plataformas completas — mas o cliente pode chamar tudo de 'sistema de RH'."),
        ("Como lidar com a objeção de integração com folha de pagamento legada?",
         "Folha de pagamento é o coração do RH brasileiro — ninguém quer arriscar. Invista em integrações nativas com os principais sistemas de folha (ADP, Sênior, TOTVS, Alterdata). Se a integração não for perfeita, ofereça uma fase de operação paralela de 3 meses onde o cliente valida os dados antes de desligar o sistema antigo. Uma POC de integração com o ambiente de homologação do cliente antes da assinatura remove esse obstáculo dos maiores negócios."),
        ("SaaS de RH precisa ser hospedado no Brasil por conta da LGPD?",
         "A LGPD não exige obrigatoriamente que dados sejam armazenados no Brasil, mas permite o tratamento em países com nível adequado de proteção ou mediante consentimento específico. Na prática, muitos CHROs de grandes empresas exigem hosting nacional por política interna ou recomendação jurídica. Ter a opção de hosting em cloud brasileira (AWS São Paulo, Azure Brazil South) elimina uma objeção comum em deals enterprise."),
    ]
)

# 5290 — Consulting: governança de TI e ITIL
art(
    "consultoria-de-governanca-de-ti-e-itil",
    "Consultoria de Governança de TI e ITIL | ProdutoVivo",
    "Como estruturar e escalar uma consultoria de governança de TI e ITIL: serviços, posicionamento, captação de clientes corporativos e modelos de receita.",
    "Consultoria de Governança de TI e ITIL",
    "Governança de TI e gestão de serviços com ITIL são demandas crescentes em empresas que buscam confiabilidade, conformidade e redução de custos operacionais de TI.",
    [
        ("O Mercado de Governança de TI no Brasil",
         "Empresas com mais de 200 colaboradores e TI interna estruturada são o mercado alvo de consultorias de governança de TI. Os principais frameworks demandados: ITIL 4 (gestão de serviços de TI), COBIT 2019 (governança de TI para o board), ISO/IEC 20000 (gestão de serviços — certificação), e CMMI (maturidade de processos de desenvolvimento). Bancos, seguradoras, governo e grandes varejistas são os maiores compradores — TI regulada exige governança documentada para auditorias dos órgãos reguladores (BACEN, SUSEP, TCU)."),
        ("Portfólio de Serviços: do Assessment ao ITSM",
         "Estruture o portfólio em quatro ofertas: (1) Diagnóstico de maturidade de governança de TI — entregável de 3-4 semanas com mapa de gaps e roadmap; (2) Implementação de ITSM — desenho e implantação de processos ITIL (gestão de incidentes, problemas, mudanças, configuração, nível de serviço); (3) Implantação de ferramentas ITSM (ServiceNow, Jira Service Management, TOPdesk, GLPI); (4) Preparação para certificação ISO 20000 — projeto de 6-12 meses com entrega da documentação para auditoria. Cada oferta tem ticket e público diferente."),
        ("Diferenciação e Posicionamento no Mercado",
         "O mercado de consultoria de TI é competitivo. Diferencie-se com especialização setorial (ex.: governança de TI para bancos e fintechs, focando em Resolução BCB 85 e LGPD financeira) ou com especialização tecnológica (ex.: ITSM nativo em nuvem com ServiceNow ou Jira). Consultorias que combinam conhecimento de framework com certificação de implementadores das ferramentas líderes de mercado cobram 40-60% mais do que as que entregam apenas documentação e treinamento."),
        ("Captação de Clientes: Conteúdo e Relacionamento",
         "Diretores e gerentes de TI consomem conteúdo técnico ativamente. LinkedIn com publicações sobre ITIL 4, governança de TI e gestão de serviços posiciona o consultor como referência. Parcerias com fabricantes de ferramentas ITSM (ServiceNow e Jira têm programas de parceiros que geram leads) são canais valiosos. Certificações reconhecidas (ITIL 4 MP/SL/DS, COBIT 2019 Assessor) conferem credibilidade imediata. Webinars técnicos gratuitos para CIOs e IT managers convertem bem — convide clientes de sucesso para depoimentos."),
        ("Precificação e Escalabilidade",
         "Projetos de diagnóstico de governança custam R$25.000-80.000 (2-4 semanas, 1-2 consultores). Projetos de implementação de ITSM completo para médias empresas custam R$120.000-400.000 (4-8 meses). Contratos de suporte contínuo pós-implementação (retainer mensal de R$8.000-25.000) geram receita recorrente com margem alta — um senior ITIL com 2-3 clientes em retainer tem receita previsível sem os riscos de projeto. Escale criando uma equipe de consultores júnior certificados e vendendo em volume."),
    ],
    [
        ("ITIL 4 e ISO/IEC 20000 são a mesma coisa?",
         "Não. ITIL 4 é um framework de boas práticas para gestão de serviços de TI — é uma guia de referência, não uma norma certificável. ISO/IEC 20000 é uma norma internacional que especifica requisitos para um sistema de gestão de serviços de TI — a organização pode se certificar nela após auditoria externa. ITIL 4 frequentemente serve de base para implementar os processos exigidos pela ISO 20000, mas uma empresa pode adotar ITIL sem buscar a certificação ISO, ou certificar-se na ISO sem seguir estritamente o ITIL."),
        ("Quanto tempo leva para implantar ITIL em uma empresa?",
         "Uma implantação de ITSM básico (gestão de incidentes, requisições e SLA) em uma empresa de TI com 20-50 analistas leva 3-4 meses. Uma implantação completa de ITIL 4 cobrindo todos os processos relevantes pode levar 12-18 meses. A abordagem pragmática é implantar pelos processos de maior impacto primeiro (geralmente incidentes e mudanças) e evoluir iterativamente, em vez de tentar transformar tudo ao mesmo tempo."),
        ("Governança de TI é obrigatória para empresas no Brasil?",
         "Governança de TI é obrigatória indiretamente para empresas reguladas: bancos e financeiras (Resolução BCB 4.893/2021 sobre Política de Segurança Cibernética), seguradoras (Circular SUSEP 638/2021), empresas de capital aberto (práticas de governança corporativa B3) e agências governamentais (COBIT exigido pelo TCU). Para empresas não reguladas, a governança de TI é uma decisão estratégica — mas a LGPD introduziu requisitos de gestão de riscos de TI que impactam todas as empresas que tratam dados pessoais."),
    ]
)

# 5291 — B2B SaaS: gestão de resíduos e meio ambiente
art(
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-residuos-e-meio-ambiente",
    "Gestão de Negócios de Empresa de B2B SaaS de Gestão de Resíduos e Meio Ambiente | ProdutoVivo",
    "Como construir e escalar um B2B SaaS de gestão de resíduos e meio ambiente: oportunidades de mercado, produto, go-to-market e crescimento no Brasil.",
    "Gestão de Negócios de Empresa de B2B SaaS de Gestão de Resíduos e Meio Ambiente",
    "ESG e regulação ambiental criam demanda urgente por plataformas de gestão de resíduos. Descubra como construir um SaaS nesse mercado em expansão.",
    [
        ("O Mercado de Gestão de Resíduos e Sustentabilidade Corporativa",
         "A agenda ESG transformou a gestão ambiental de um custo a ser minimizado em um ativo estratégico. Empresas precisam documentar, rastrear e reportar a destinação de resíduos para obter licenças ambientais, certificações ISO 14001, ratings ESG e contratos com grandes clientes que exigem conformidade ambiental na cadeia de fornecimento. A Política Nacional de Resíduos Sólidos (Lei 12.305/2010) e suas regulamentações estaduais criam obrigações de rastreabilidade que um SaaS pode automatizar eficientemente."),
        ("Funcionalidades Essenciais do SaaS Ambiental",
         "O produto mínimo viável deve cobrir: cadastro e classificação de resíduos por tipologia (perigosos, não-perigosos, recicláveis); gestão de manifestos de transporte de resíduos (MTR digital, exigido pelo IBAMA/SINIR); controle de contratos com empresas coletoras e destinadoras licenciadas; indicadores ambientais (taxa de desvio de aterro, índice de reciclagem, emissão de GEE evitada); e relatórios para auditoria de ISO 14001 e divulgação ESG (GRI 306, SASB). Integrações com o SINIR (Sistema Nacional de Informações sobre a Gestão dos Resíduos Sólidos) são obrigatórias para empresas reguladas."),
        ("ICP e Estratégia de Vendas",
         "O ICP são empresas geradoras de resíduos industriais em setores altamente regulados: indústria química e petroquímica, farmacêutica, alimentícia, automotiva, hospitais e clínicas (resíduos de saúde), e grandes varejistas. O gatilho de compra mais poderoso é a renovação da Licença de Operação (LO) da Vigilância Ambiental — empresas que não comprovam destinação correta arriscam não renovar. Auditorias de ISO 14001 e exigências de clientes B2B (supply chain compliance) são outros gatilhos eficazes."),
        ("Modelo de Receita e Precificação",
         "Precificação por volume de resíduos gerenciados (toneladas/mês) ou por número de unidades geradoras. Uma indústria de médio porte (100-500 colaboradores) paga R$800-3.000/mês; conglomerados industriais com múltiplas plantas pagam R$15.000-50.000/mês. Módulos adicionais de relatório ESG automatizado (GRI, CDP, TCFD) têm ticket diferenciado. Contratos anuais com auditoria de conformidade incluída criam lock-in pelo valor entregue além do software."),
        ("Crescimento: Expansão Vertical e Carbon Credits",
         "Após consolidar gestão de resíduos, expanda para módulos adjacentes: cálculo e gestão de pegada de carbono (emissões Escopo 1, 2 e 3), gestão de água e efluentes, e relatórios integrados de sustentabilidade. A interface com mercados de crédito de carbono — onde empresas que desviam resíduos de aterro podem monetizar reduções de metano — cria um diferencial de receita adicional ao cliente, tornando o SaaS um gerador de valor financeiro além de um custo de compliance."),
    ],
    [
        ("O que é o MTR (Manifesto de Transporte de Resíduos) e como um SaaS pode ajudar?",
         "O MTR é um documento obrigatório para o transporte de resíduos perigosos e não-perigosos no Brasil, exigido pelo IBAMA e gerenciado pelo SINIR. Empresas geradoras precisam emitir um MTR para cada coleta, assinado eletronicamente pela geradora, transportadora e destinadora. Um SaaS de resíduos automatiza a emissão, assinatura digital e arquivamento de MTRs, eliminando o trabalho manual de acessar diretamente o portal SINIR e garantindo rastreabilidade completa para auditorias ambientais."),
        ("ISO 14001 exige software de gestão de resíduos?",
         "A ISO 14001 não exige nenhuma ferramenta específica, mas exige que a organização identifique, monitore e controle seus aspectos ambientais significativos — incluindo geração de resíduos. Na prática, empresas que tentam gerenciar resíduos por planilhas têm dificuldade em demonstrar rastreabilidade em auditorias de renovação de certificado. Um SaaS reduz o esforço de preparação para auditorias de ISO 14001 em 60-80% segundo clientes que fizeram a transição de planilhas."),
        ("Como o SaaS de resíduos se posiciona em relação à agenda ESG?",
         "Dados de gestão de resíduos alimentam diretamente os relatórios ESG nos indicadores GRI 306 (resíduos), GRI 305 (emissões — resíduos orgânicos desviam do aterro evitando metano) e SASB setoriais. Um SaaS que automatiza a coleta desses dados e gera os relatórios no formato esperado por auditores de ESG e agências de rating (MSCI, Sustainalytics, B3 ISE) entrega valor estratégico que vai muito além do compliance operacional, justificando tickets de enterprise pricing."),
    ]
)

# 5292 — Clinic: cirurgia plástica e medicina estética avançada
art(
    "gestao-de-clinicas-de-cirurgia-plastica-e-medicina-estetica-avancada",
    "Gestão de Clínicas de Cirurgia Plástica e Medicina Estética Avançada | ProdutoVivo",
    "Guia completo para gestão de clínicas de cirurgia plástica e medicina estética avançada: infraestrutura, marketing, precificação, captação e crescimento.",
    "Gestão de Clínicas de Cirurgia Plástica e Medicina Estética Avançada",
    "O Brasil é o segundo maior mercado mundial de cirurgia plástica. Saiba como estruturar uma clínica estética de alto desempenho e crescimento escalável.",
    [
        ("O Brasil como Potência Global em Cirurgia Plástica",
         "O Brasil realiza mais de 1,5 milhão de procedimentos cirúrgicos estéticos por ano, sendo o segundo maior mercado mundial. A combinação de alta demanda, cultura de valorização da aparência e custo relativo menor que países desenvolvidos cria um mercado robusto que absorve tanto cirurgiões experientes quanto novos especialistas bem posicionados. O crescimento da medicina estética não cirúrgica (toxina botulínica, preenchedores, lasers, bioestimuladores) adiciona uma camada de receita recorrente que a cirurgia plástica isolada não oferece."),
        ("Estrutura e Infraestrutura: Cirúrgico vs. Estético",
         "Uma clínica de cirurgia plástica completa pode ter duas linhas operacionais: (1) Centro cirúrgico ambulatorial — sala de cirurgia equipada (R$500K-1.5M), habilitação Anvisa como Unidade Ambulatorial de Alto Risco, anestesiologista e equipe cirúrgica, para procedimentos como rinoplastia, mamoplastia e lipoaspiração; (2) Clínica de medicina estética — salas de procedimentos menores (toxina, preenchedores, peelings, laser, radiofrequência), menor investimento e operação mais simples. A combinação das duas linhas maximiza o ticket por paciente ao longo do ciclo de vida do cliente."),
        ("Marketing Digital para Clínicas de Estética",
         "O marketing em cirurgia plástica e estética é altamente visual e movido por prova social. Instagram e TikTok são os canais primários — antes e depois (com consentimento e seguindo CFM), lives educativas e bastidores do procedimento constroem autoridade e desejo. Google Ads para 'rinoplastia [cidade]' e 'toxina botulínica [bairro]' capturam intenção de compra imediata. O médico-influencer que combina autoridade clínica com conteúdo acessível pode escalar sua captação de forma orgânica e orgânica com CAC próximo de zero."),
        ("Precificação de Procedimentos e Gestão Financeira",
         "A precificação de cirurgias deve cobrir: custo do centro cirúrgico (aluguel ou taxa de uso), honorário anestesiologista, materiais e implantes (se aplicável), custos da equipe de enfermagem, e margem do cirurgião. Rinoplastia custa R$12.000-35.000; mamoplastia R$10.000-28.000; lipoaspiração R$8.000-20.000. Para medicina estética, toxina e preenchedores: ticket médio R$600-2.500 por sessão. A oferta de pacotes de manutenção (ex.: 3 sessões de toxina anuais por assinatura) cria receita recorrente previsível."),
        ("Fidelização e Ciclo de Vida do Paciente Estético",
         "Um paciente estético bem atendido gera receita por décadas. A chave é o ciclo de manutenção: após a cirurgia (ou o procedimento inicial), ofereça protocolos de cuidado continuado — toxina a cada 4-6 meses, preenchedores anualmente, lasers sazonais, procedimentos de corpo conforme necessidade. Um CRM médico que registra histórico de procedimentos e dispara lembretes de retorno no prazo correto pode aumentar a frequência de visitas em 30-40%. Programas de indicação (desconto no próximo procedimento por amigo indicado) também têm altíssima conversão no segmento estético."),
    ],
    [
        ("Médico esteta precisa ser especialista em cirurgia plástica para fazer procedimentos?",
         "Para cirurgias plásticas (mamoplastia, rinoplastia, lipoaspiração, lifting facial), exige-se o título de especialista em Cirurgia Plástica reconhecido pelo CFM/SBCP. Para procedimentos de medicina estética não cirúrgica (toxina botulínica, preenchedores, lasers, peelings), qualquer médico com formação adequada pode realizar — mas recomenda-se capacitação específica em sociedades como SBME ou AMEBROM. O não-cumprimento das competências de especialidade pode resultar em processos no CFM e CRM."),
        ("Como calcular o ROI de um equipamento de laser ou radiofrequência?",
         "Calcule: (ticket médio por sessão × sessões mensais projetadas) - (parcela mensal do financiamento + consumíveis + manutenção). Um laser fracionado de R$180.000 com 40 sessões mensais de R$1.200 gera R$48.000 bruto/mês, menos custo de R$8.000-10.000, resultando em R$38.000/mês de margem bruta — payback em menos de 6 meses. A taxa de ocupação do equipamento é o fator crítico: invista em marketing digital antes da compra para garantir agenda cheia desde o primeiro mês."),
        ("É necessário ter centro cirúrgico próprio para oferecer cirurgia plástica?",
         "Não — muitos cirurgiões plásticos começam realizando procedimentos em centros cirúrgicos hospitalares credenciados ou clínicas especializadas em tempo de sala, pagando taxa de uso. Isso reduz o investimento inicial para zero em estrutura cirúrgica, mantendo todo o capital disponível para marketing e qualificação. O centro cirúrgico próprio faz sentido quando o volume de cirurgias supera 8-10 por mês e os custos de locação de sala superam a amortização do centro próprio."),
    ]
)

# 5293 — SaaS Sales: escritórios contábeis
art(
    "vendas-para-o-setor-de-saas-para-escritorios-contabeis-e-contadores",
    "Vendas para o Setor de SaaS para Escritórios Contábeis e Contadores | ProdutoVivo",
    "Estratégias de vendas B2B para SaaS voltado a escritórios contábeis e contadores autônomos: como prospectar, demonstrar valor e expandir contratos no mercado contábil.",
    "Vendas para o Setor de SaaS para Escritórios Contábeis e Contadores",
    "Há mais de 90.000 escritórios contábeis no Brasil — um mercado subdigitalizado com alta disposição a pagar por ferramentas que aumentem produtividade e reduzam erros.",
    [
        ("O Universo dos Escritórios Contábeis no Brasil",
         "O Brasil tem mais de 90.000 escritórios contábeis registrados no CRC, atendendo desde MEIs até grandes empresas. A maioria são PMEs com 2-20 colaboradores, altamente dependentes de processos manuais e planilhas para gestão interna (clientes, prazos, documentos, honorários). Ao mesmo tempo, o volume de obrigações fiscais e trabalhistas cresce anualmente com novidades como eSocial, EFD-Reinf, DCTFWeb e Nota Fiscal de Serviços Eletrônica — criando demanda por ferramentas que automatizem essas entregas."),
        ("Segmentos de SaaS para Contabilidade",
         "O mercado de SaaS contábil se divide em: (1) Sistemas de contabilidade e escrita fiscal (Domínio, Alterdata, Questor — altíssima barreira de entrada); (2) Gestão do escritório contábil (ERP da contabilidade: gestão de clientes, controle de prazos fiscais, honorários, documentos); (3) Automação de obrigações acessórias (robots de download de certidões, transmissão de DCTFWeb, cruzamento de SPED); (4) Ferramentas de comunicação contábil (portais do cliente para troca segura de documentos e NF-e). Os segmentos 2, 3 e 4 têm menor competição e maior facilidade de entrada para novas startups."),
        ("Prospecção e Canais de Distribuição",
         "Os melhores canais para alcançar escritórios contábeis: eventos do CFC/CRC estaduais (Contábeis, ExpoContábeis), grupos de contadores no WhatsApp e Telegram, influencers contábeis no YouTube e Instagram (há centenas com milhares de seguidores contadores), e parcerias com associações como Fenacon e Sescon. E-mail marketing para bases de CRCs estaduais (onde disponível) tem boa conversão. Contadores recomendam ferramentas uns para os outros ativamente — um programa de indicação bem estruturado cria crescimento viral orgânico."),
        ("Demonstração de Valor: Produtividade e Conformidade",
         "A demo deve mostrar o que o contador mais valoriza: agilidade. Simule o fluxo real: abertura de cliente, configuração de obrigações por regime tributário, disparo automático de lembretes de prazo, upload seguro de documentos pelo cliente no portal, e emissão de fatura de honorários em 3 cliques. Mostre o 'antes e depois' em horas trabalhadas: um escritório com 100 clientes pode economizar 20-30 horas mensais em controle manual de prazos — R$3.000-5.000 em custo de pessoal evitado, justificando qualquer SaaS de R$300-1.500/mês."),
        ("Crescimento e Retenção no Mercado Contábil",
         "Contadores são leais quando a ferramenta funciona bem — churn anual de 8-12% em SaaS contábil bem posicionado. O risco maior é o ciclo de obrigações fiscais: se o produto falhar em algum prazo crítico (ex.: bug na transmissão de DCTFWeb), o contador migra imediatamente. Invista pesado em monitoramento de disponibilidade e suporte especializado em períodos críticos (meses de fechamento, entrega de IR). Plano de preços com desconto para escritórios com 50+ clientes incentiva crescimento da base — o escritório expande e você expande junto."),
    ],
    [
        ("Qual a diferença entre um ERP contábil e um sistema de gestão de escritório contábil?",
         "ERP contábil (Domínio, Questor, Alterdata) é o sistema onde a contabilidade é de fato processada — lançamentos, balancetes, SPED, eSocial, folha. Sistema de gestão de escritório contábil é o 'ERP do ERP': gerencia os clientes do escritório, controla prazos de obrigações, armazena documentos, gera cobranças de honorários e facilita a comunicação com o cliente. Os dois sistemas coexistem no mesmo escritório e a integração entre eles é um diferencial valorizado."),
        ("Contadores costumam pagar por SaaS ou preferem sistemas desktop?",
         "A transição para SaaS em contabilidade está acelerada: escritórios menores (1-5 contadores) já preferem SaaS pelo acesso remoto e ausência de servidor local. Escritórios maiores e mais tradicionais ainda usam sistemas desktop robustos, mas a necessidade de trabalho híbrido pós-pandemia forçou a adoção de SaaS mesmo entre os mais resistentes. O fator decisivo é a confiabilidade — um SaaS que caia no dia da entrega do SPED perde o cliente para sempre."),
        ("Como convencer contadores a trocar de sistema se já usam algo há anos?",
         "A principal objeção é o esforço de migração e a curva de aprendizado em época de alta demanda. Estratégias eficazes: (1) Ofereça migração de dados assistida e gratuita; (2) Disponibilize treinamentos curtos (vídeos de 5-10 minutos) no modelo que contadores consomem; (3) Garanta período de operação paralela de 2-3 meses; (4) Apresente depoimentos de contadores da mesma cidade ou região que já fizeram a transição. Um piloto gratuito de 60 dias em um cliente pequeno dentro do escritório demonstra o valor sem risco."),
    ]
)

# 5294 — Consulting: desenvolvimento de produtos digitais
art(
    "consultoria-de-desenvolvimento-de-produtos-digitais-e-product-management",
    "Consultoria de Desenvolvimento de Produtos Digitais e Product Management | ProdutoVivo",
    "Como estruturar e escalar uma consultoria de desenvolvimento de produtos digitais e product management: metodologias, posicionamento, captação e modelos de receita.",
    "Consultoria de Desenvolvimento de Produtos Digitais e Product Management",
    "Empresas de todos os setores constroem produtos digitais e precisam de expertise em product management. Veja como monetizar esse conhecimento como consultor.",
    [
        ("O Mercado de Product Management e Consultoria de Produto",
         "Product Management tornou-se uma das funções mais valorizadas da economia digital. Empresas não-tecnológicas — bancos, varejistas, indústrias — estão construindo produtos digitais internamente e precisam de mentoria e processos de produto que grandes techs têm de sobra mas elas nunca desenvolveram. Consultorias de produto que ajudam essas empresas a estruturar times, processos e estratégia de produto encontram demanda crescente com tickets premium — o mercado de consultoria em produto digital cresce 25% ao ano no Brasil."),
        ("Portfólio de Serviços: da Estratégia ao Time de Produto",
         "Organize o portfólio em quatro camadas: (1) Product Discovery — entendimento de usuários, mapeamento de oportunidades, definição de bets estratégicos; (2) Estruturação de times — contratação e onboarding de PMs, definição de papéis (PM, PO, Designer, Engenheiro), rituais e cerimônias ágeis; (3) Estratégia de produto — roadmap, OKR de produto, priorização (RICE, ICE, Kano), gestão de stakeholders; (4) Aceleração de entrega — revisão de processos de desenvolvimento, métricas de DORA, cultura de experimentação e A/B testing."),
        ("Diferenciação: Especialização por Tipo de Produto",
         "Um consultor que se apresenta como 'especialista em produtos digitais' enfrenta concorrência de centenas. Especializar-se em um tipo de produto cria vantagem competitiva: (a) Marketplaces e plataformas de dois lados; (b) SaaS B2B com complexidade de enterprise; (c) Produtos financeiros digitais (fintechs, banking-as-a-service); (d) Produtos de saúde digital (healthtech, telemedicina); (e) E-commerce e plataformas de venda. A especialização justifica cobrar 50-100% mais e facilita o marketing de conteúdo com cases específicos."),
        ("Captação: Conteúdo, Comunidade e Rede",
         "Product managers são uma comunidade ativa — Product Academy, ProductCon, meetups de PM em São Paulo e outras capitais. Publicar no LinkedIn sobre frameworks de produto, análises de cases de empresas conhecidas, e lições aprendidas em projetos (sem identificar clientes) gera audiência qualificada. Criar um conteúdo educativo gratuito de alta qualidade (newsletter, YouTube, podcast) posiciona o consultor como referência e gera inbound de qualidade. O boca-a-boca entre CPOs e VPs de Produto é extremamente eficiente — um cliente satisfeito indica 3-5 contatos."),
        ("Precificação: Projeto vs. Embedded vs. Fractional",
         "Três modelos funcionam bem em consultoria de produto: (1) Projeto — escopo definido, entregável claro (ex.: product discovery de R$40.000 em 6 semanas); (2) Embedded consultant — o consultor atua como PM temporário dentro da equipe do cliente (R$1.500-3.000/dia ou R$25.000-50.000/mês); (3) Fractional CPO — dedicação parcial (2-3 dias/semana) para supervisionar a estratégia de produto de uma startup ou scale-up (R$15.000-35.000/mês). O modelo Fractional CPO é o mais escalável pois permite atender múltiplos clientes simultaneamente com renda previsível."),
    ],
    [
        ("Qual a diferença entre Product Manager e Product Owner?",
         "Product Manager (PM) é responsável pela estratégia do produto — qual problema resolver, para quem, com qual proposta de valor, e como medir sucesso. Product Owner (PO) é um papel scrum focado na gestão do backlog e representação dos stakeholders junto ao time de desenvolvimento. Em times maduros, PM e PO são papéis separados; em empresas menores, uma mesma pessoa exerce ambos. Uma consultoria de produto costuma trabalhar no nível de PM — estratégia, discovery e métricas — enquanto o PO cuida da execução tática com o time de engenharia."),
        ("Como precificar um engagement de product discovery?",
         "Um product discovery típico custa R$25.000-80.000 e dura 4-8 semanas. Inclui: pesquisa com usuários (5-10 entrevistas qualitativas), análise de dados de uso existentes, benchmark competitivo, mapeamento de oportunidades (Opportunity Solution Tree ou Jobs-to-be-Done), e priorização de iniciativas com business case. O valor entregue — evitar construir o produto errado — frequentemente supera R$500.000 em desenvolvimento economizado. Apresente esse ROI ao cliente para justificar o investimento."),
        ("É necessário ter experiência em uma grande tech para ser consultor de produto?",
         "Experiência em grandes techs (Google, Meta, iFood, Nubank) adiciona credibilidade e acesso a redes valiosas, mas não é requisito absoluto. O que diferencia consultores de produto bem-sucedidos é a capacidade de diagnosticar problemas de produto rapidamente, facilitar conversas difíceis com stakeholders, e traduzir visão de negócio em direção de produto concreta. Consultores com histórico de 0 a 1 em startups ou transformação digital de empresas tradicionais têm ângulo de venda igualmente valioso."),
    ]
)

# ── Sitemap ───────────────────────────────────────────────────────────────────
slugs_5287 = [
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-da-qualidade-e-qms",
    "gestao-de-clinicas-de-infectologia-e-medicina-tropical",
    "vendas-para-o-setor-de-saas-de-hcm-e-gestao-de-recursos-humanos",
    "consultoria-de-governanca-de-ti-e-itil",
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-residuos-e-meio-ambiente",
    "gestao-de-clinicas-de-cirurgia-plastica-e-medicina-estetica-avancada",
    "vendas-para-o-setor-de-saas-para-escritorios-contabeis-e-contadores",
    "consultoria-de-desenvolvimento-de-produtos-digitais-e-product-management",
]
titles_5287 = [
    "Gestão de Negócios de Empresa de B2B SaaS de Gestão da Qualidade e QMS",
    "Gestão de Clínicas de Infectologia e Medicina Tropical",
    "Vendas para o Setor de SaaS de HCM e Gestão de Recursos Humanos",
    "Consultoria de Governança de TI e ITIL",
    "Gestão de Negócios de Empresa de B2B SaaS de Gestão de Resíduos e Meio Ambiente",
    "Gestão de Clínicas de Cirurgia Plástica e Medicina Estética Avançada",
    "Vendas para o Setor de SaaS para Escritórios Contábeis e Contadores",
    "Consultoria de Desenvolvimento de Produtos Digitais e Product Management",
]

sm_path = pathlib.Path(__file__).parent / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")
new_urls = "\n".join(
    f"  <url><loc>{DOMAIN}/blog/{s}/</loc><changefreq>monthly</changefreq><priority>0.6</priority></url>"
    for s in slugs_5287
)
sm_path.write_text(sm.replace("</urlset>", new_urls + "\n</urlset>"), encoding="utf-8")

# ── Trilha ────────────────────────────────────────────────────────────────────
tr_path = pathlib.Path(__file__).parent / "trilha.html"
tr = tr_path.read_text(encoding="utf-8")
new_items = "\n".join(
    f'    <li><a href="/blog/{s}/">{t}</a></li>'
    for s, t in zip(slugs_5287, titles_5287)
)
tr_path.write_text(tr.replace("</ul>", new_items + "\n  </ul>", 1), encoding="utf-8")

print("Done — batch 1902")
