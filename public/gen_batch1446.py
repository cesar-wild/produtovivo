import os, json

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
<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','{pixel}');fbq('track','PageView');</script>
<style>
body{{font-family:Arial,sans-serif;margin:0;padding:0;color:#222;}}
header{{background:#1a1a2e;color:#fff;padding:16px 24px;}}
header a{{color:#e0e0ff;text-decoration:none;font-weight:bold;font-size:1.2rem;}}
main{{max-width:860px;margin:40px auto;padding:0 20px;}}
h1{{font-size:2rem;color:#1a1a2e;}}
.lead{{font-size:1.1rem;color:#444;margin-bottom:28px;}}
h2{{color:#16213e;margin-top:32px;}}
.faq{{background:#f5f7ff;border-radius:8px;padding:24px;margin-top:40px;}}
.faq h2{{color:#1a1a2e;margin-top:0;}}
.faq-item{{margin-bottom:18px;}}
.faq-item h3{{margin:0 0 6px;color:#16213e;}}
footer{{text-align:center;padding:24px;color:#888;font-size:.9rem;margin-top:60px;border-top:1px solid #eee;}}
footer a{{color:#555;}}
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
<footer><p>&copy; 2025 ProdutoVivo. <a href="/blog/">Blog</a> | <a href="/">Home</a></p></footer>
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
        schema_faqs.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
    schema = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": schema_faqs}, ensure_ascii=False)
    html = TMPL.format(title=title, desc=desc, url=url, pixel=PIXEL,
                       h1=h1, lead=lead, body=body_html, faqs=faqs_html, schema=schema)
    out_dir = os.path.join(BASE, slug)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

# Article 4375 — B2B SaaS: gestão de qualidade e rastreabilidade na indústria de alimentos
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-qualidade-e-rastreabilidade-na-industria-de-alimentos",
    title="Gestão de Negócios para SaaS de Qualidade e Rastreabilidade na Indústria de Alimentos | ProdutoVivo",
    desc="Como escalar um SaaS de gestão de qualidade e rastreabilidade para a indústria de alimentos: produto, vendas e compliance ANVISA e SIF.",
    h1="Gestão de Negócios para SaaS de Qualidade e Rastreabilidade na Indústria de Alimentos",
    lead="Indústrias de alimentos têm exigências de qualidade e rastreabilidade entre as mais rigorosas de qualquer setor — ANVISA, SIF (Serviço de Inspeção Federal), FSSC 22000, BRC e BRCGS definem padrões que precisam ser documentados e auditados continuamente. SaaS especializados nesse segmento têm oportunidade enorme em um mercado ainda dominado por planilhas.",
    sections=[
        ("Mercado e Oportunidade para SaaS de Qualidade em Alimentos",
         "A indústria de alimentos e bebidas é o maior setor industrial do Brasil, respondendo por mais de 10% do PIB. Empresas que exportam ou fornecem para grandes redes de varejo (Carrefour, Pão de Açúcar, Atacadão, Assaí) são frequentemente exigidas a obter certificações como ISO 22000, BRCGS ou FSSC 22000. A gestão dessas certificações — documentação de APPCC (Análise de Perigos e Pontos Críticos de Controle), registros de CCP (Pontos Críticos de Controle), rastreabilidade de lote e gestão de não-conformidades — é altamente demandante e muito mal atendida por ERPs genéricos."),
        ("Produto: Rastreabilidade e Gestão de APPCC",
         "Os requisitos funcionais essenciais incluem: rastreabilidade bidirecional de lotes (rastrear do insumo ao produto final e vice-versa — fundamental para simulacros e recalls), registro de CPPs com limites críticos e ações corretivas automáticas quando desviados, gestão de non-conformidades com análise de causa raiz e CAPA (Corrective and Preventive Action), controle de temperatura de câmaras frias com alertas de desvio, gestão de auditorias internas e externas com checklists digitais, e suporte a regimes de inspeção SIF/SIE/SIM com geração de relatórios regulatórios."),
        ("Vendas para a Indústria de Alimentos: Perfil do Comprador",
         "O decisor de compra é o gestor de qualidade (SQMS — Senior Quality Manager) ou o diretor de operações. A indústria de alimentos tem ciclos de compra de 3 a 6 meses para decisões de sistema de gestão de qualidade, com avaliação técnica rigorosa (funcionalidades de APPCC, integração com ERPs como SAP e TOTVS, validação de rastreabilidade com simulacro). Feiras setoriais como Fispal Food Service, FISPAL Tecnologia e ExpoPharma são canais de prospecção concentrada. Certificadoras (Bureau Veritas, SGS, DNV) são parceiros de distribuição estratégicos."),
        ("Compliance com ANVISA, SIF e Certificações Internacionais",
         "O quadro regulatório da indústria de alimentos brasileira inclui: ANVISA (regulamentos técnicos de identidade e qualidade, RDCs de boas práticas de fabricação), SIF/DIPOA (inspeção de carnes e derivados), MAPA (agropecuária e bebidas), e certificações voluntárias mas exigidas pelo mercado: ISO 22000, FSSC 22000 (preferida por grandes redes de varejo globais), BRCGS (British Retail Consortium Global Standards) e IFS. SaaS que suportam os requisitos de múltiplas normas simultaneamente (módulos específicos por norma) têm vantagem competitiva significativa."),
        ("Retenção e Expansão em SaaS de Qualidade Industrial",
         "A stickiness é naturalmente alta: dados históricos de rastreabilidade (obrigados a manter por norma por anos), histórico de auditorias e não-conformidades e a integração com o processo produtivo criam lock-in legítimo. A expansão acontece por novas unidades produtivas, módulos adicionais (gestão de fornecedores de matéria-prima, controle de laboratório interno, gestão de calibração de equipamentos) e integração com sistemas de ERP e MES (Manufacturing Execution System). Contratos plurianuais com SLAs de compliance são preferidos pelo segmento."),
    ],
    faq_list=[
        ("O que é APPCC e por que é central na gestão de qualidade de alimentos?",
         "APPCC (Análise de Perigos e Pontos Críticos de Controle), ou HACCP em inglês, é um sistema preventivo de controle de segurança de alimentos que identifica, avalia e controla perigos significativos para a segurança do alimento (biológicos, químicos e físicos). É a base das normas ISO 22000, FSSC 22000 e BRCGS. No Brasil, a RDC ANVISA 60/2019 e a Portaria MAPA 127/2009 exigem APPCC para determinadas categorias de alimentos."),
        ("O que é rastreabilidade bidirecional e por que é importante?",
         "Rastreabilidade bidirecional permite rastrear um produto em dois sentidos: 'trace forward' (do insumo ao produto final distribuído) e 'trace back' (do produto final aos insumos de origem). No caso de um recall ou surto de doença transmitida por alimento, a rastreabilidade bidirecional permite identificar rapidamente quais lotes foram afetados e recolhê-los do mercado com o menor impacto possível. Normas como BRCGS e FSSC 22000 exigem que o simulacro de rastreabilidade seja concluído em menos de 4 horas."),
        ("SaaS de qualidade funciona para pequenas indústrias de alimentos artesanais?",
         "Sim, com adaptações. Pequenos produtores artesanais que precisam obter SIF ou certificação para exportar têm as mesmas obrigações de documentação de APPCC e rastreabilidade, mas em escala menor. Soluções com planos de entrada acessíveis (R$ 300-600/mês) e interface simplificada são adequadas para microindústrias com até 20 funcionários. O valor entregue é a digitalização dos registros obrigatórios que hoje são feitos em papel, com risco de perda e dificuldade de auditoria."),
    ]
)

# Article 4376 — Clinic: oncologia clínica e imunoterapia
art(
    slug="gestao-de-clinicas-de-oncologia-clinica-e-imunoterapia",
    title="Gestão de Clínicas de Oncologia Clínica e Imunoterapia | ProdutoVivo",
    desc="Como gerenciar clínicas de oncologia clínica com foco em imunoterapia: protocolos de infusão, OPME oncológico, gestão financeira e captação.",
    h1="Gestão de Clínicas de Oncologia Clínica e Imunoterapia",
    lead="Oncologia clínica é uma das especialidades de maior complexidade e custo na medicina brasileira. O surgimento de imunoterapias, terapias-alvo e tratamentos orais revolucionou o manejo do câncer, mas aumentou exponencialmente a complexidade da gestão clínica e financeira das clínicas oncológicas.",
    sections=[
        ("Panorama da Oncologia Clínica e Imunoterapia no Brasil",
         "O Brasil registra mais de 700.000 novos casos de câncer por ano (INCA). A oncologia clínica abrange desde o diagnóstico e estadiamento até o tratamento com quimioterapia, imunoterapia, terapias-alvo orais e hormonioterapia. Imunoterapia com inibidores de checkpoint (pembrolizumabe, nivolumabe, atezolizumabe, durvalumabe) tornou-se padrão de tratamento em múltiplos tumores sólidos, mas os custos são extremamente elevados (R$ 20.000-80.000/mês por paciente) e a gestão de autorização junto a convênios e via judicial é complexa."),
        ("Gestão de Sala de Infusão Oncológica",
         "O coração de uma clínica de oncologia clínica ambulatorial é a sala de infusão. A gestão eficiente envolve: agendamento de poltronas de infusão com controle de tempo por protocolo (infusões podem durar de 30 minutos a 8 horas), gestão de farmácia oncológica com preparação de quimioterápicos em cabine de segurança biológica (conforme RDC ANVISA 220/2004), controle de temperatura de armazenamento de medicamentos sensíveis, e monitoramento de reações durante a infusão com kit de anafilaxia disponível. Farmacêutico responsável pela farmácia oncológica é obrigatório."),
        ("Gestão de Protocolos e Ciclos de Tratamento",
         "Cada paciente oncológico segue um protocolo de tratamento específico (definido por tipo de tumor, estadiamento e biomarcadores): FOLFOX, FOLFIRI, AC-T, TC, pembrolizumabe em monoterapia ou combinado. O sistema de gestão precisa suportar: cadastro de protocolos com doses calculadas por m² de SC (superfície corporal) ou por mg/kg, ajustes de dose por toxicidade (redução ou suspensão baseada em critérios CTCAE), ciclos de tratamento com intervalos programados e alertas de data de próxima infusão, e histórico de toxicidades por tipo e grau."),
        ("Autorização de Imunoterapia e Terapias-Alvo",
         "Imunoterapias e terapias-alvo têm custo mensal que pode ultrapassar R$ 60.000 — tornando a autorização por convênio a atividade de maior impacto financeiro da clínica. O processo envolve: laudo médico detalhado com indicação baseada em guidelines (NCCN, ESMO, INCA), resultado de biomarcadores (PD-L1, MSI, TMB, EGFR, ALK, ROS1, HER2, BRCA), estudo de caso de custo-efetividade quando solicitado pela operadora, e recursos sistemáticos contra negativas. Clínicas com equipe dedicada de autorização têm receita substancialmente superior às que não têm."),
        ("Sustentabilidade Financeira em Oncologia Ambulatorial",
         "Oncologia clínica tem modelo financeiro complexo: receita de honorários médicos (consultas e supervisão de infusão), receita de sala de infusão (taxa de infusão por hora ou por protocolo), e medicamentos (quando faturados pela clínica, com margem sobre custo do fármaco). O risco de inadimplência é menor que em outros segmentos (tratamentos contínuos geram comprometimento do paciente), mas a negociação com convênios é crítica — clínicas que não negociam valores adequados de imunoterapia trabalham no prejuízo em cada sessão."),
    ],
    faq_list=[
        ("Qual a diferença entre imunoterapia e quimioterapia no tratamento do câncer?",
         "Quimioterapia age diretamente nas células tumorais, interferindo na divisão celular — mas também afeta células normais de crescimento rápido (cabelo, mucosas, medula). Imunoterapia com inibidores de checkpoint (anti-PD-1, anti-PD-L1, anti-CTLA-4) remove os freios do sistema imunológico, permitindo que as próprias células T do paciente reconheçam e destruam o tumor. Os efeitos colaterais da imunoterapia são diferentes (irAEs — immune-related adverse events) e podem afetar qualquer órgão, exigindo reconhecimento e manejo específicos."),
        ("RDC 220/2004 da ANVISA exige farmacêutico em clínicas que preparam quimioterápicos?",
         "Sim. A RDC 220/2004 determina que o preparo de antineoplásicos injetáveis seja realizado por farmacêutico responsável técnico, em área física exclusiva com cabine de segurança biológica (classe II tipo B2 ou tipo A2), com controles de acesso, equipamentos de proteção e descarte específico de resíduos classe D (perigosos). A regulamentação protege tanto os profissionais de saúde expostos quanto a qualidade e esterilidade do medicamento preparado."),
        ("Como uma clínica de oncologia pode estruturar o processo de judicialização de medicamentos?",
         "O processo envolve: documentação completa do caso clínico (prontuário, laudos de patologia e biomarcadores, guidelines que suportam a indicação), negativa formal do plano de saúde (requisito para ação judicial), orientação ao paciente para buscar advogado especializado em saúde ou defensorias públicas (que têm programas de judicialização de saúde), e liminar (tutela de urgência) que em oncologia é frequentemente concedida em 24-48h pela urgência do tratamento. Clínicas que estruturam esse fluxo reduzem o tempo sem tratamento e fidelizam pacientes e familiares."),
    ]
)

# Article 4377 — SaaS sales: centros de oncologia e radioterapia
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-centros-de-oncologia-e-radioterapia",
    title="Vendas de SaaS para Centros de Oncologia e Radioterapia | ProdutoVivo",
    desc="Como vender SaaS de gestão para centros de radioterapia oncológica: abordagem, compliance CNEN e integração com sistemas de planejamento de RT.",
    h1="Vendas de SaaS para Centros de Oncologia e Radioterapia",
    lead="Centros de radioterapia oncológica são estabelecimentos de alta complexidade técnica e regulatória, com equipamentos de alto custo e processos rigorosos de controle de qualidade. Vender SaaS para esse segmento requer entender os fluxos específicos de RT (radioterapia) e as exigências da CNEN e da SBR.",
    sections=[
        ("Perfil do Mercado de Radioterapia no Brasil",
         "O Brasil tem aproximadamente 300 centros de radioterapia ativos, com concentração em capitais e grandes centros urbanos — resultando em acesso muito desigual entre regiões. A radioterapia é indicada em mais de 50% dos casos de câncer em algum momento do tratamento, seja com intenção curativa (radical), adjuvante ou paliativa. Aceleradores lineares (Linacs) são os equipamentos dominantes, com acesso crescente a tecnologias como VMAT (Volumetric Modulated Arc Therapy), SBRT/SABR (radiocirurgia extracraniana) e radioterapia com feixes de prótons em centros de referência."),
        ("Requisitos Específicos de Software para Centros de Radioterapia",
         "Um centro de RT opera com múltiplos sistemas especializados: TPS (Treatment Planning System — sistemas como Eclipse, Monaco, RayStation), OIS (Oncology Information System — Aria, Mosaiq), sistema de verificação de posicionamento e IGRT (Image Guided RT) e controle de qualidade (QA) de equipamentos. O SaaS de gestão precisa integrar esses sistemas para: registrar a prescrição do radioterapeuta, acompanhar os fracionamentos realizados (alertas de sessions concluídas vs. prescritas), registrar toxicidades agudas (CTCAE) e gerenciar retornos de acompanhamento pós-RT."),
        ("Abordagem de Prospecção no Segmento de Radioterapia",
         "O decisor de compra é o radioterapeuta-chefe (diretor clínico) ou o físico médico responsável. Prospecção eficaz: eventos da SBRT (Sociedade Brasileira de Radioterapia), CBR (Congresso Brasileiro de Radiologia), parcerias com distribuidores de equipamentos de radioterapia (Varian, Elekta, Accuray) que indicam software de gestão a novos centros, e marketing de conteúdo sobre controle de qualidade de RT e compliance CNEN. O ciclo de vendas é de 3 a 6 meses pela complexidade técnica e pela necessidade de integração com os sistemas de RT existentes."),
        ("Compliance CNEN e Controle de Qualidade em Radioterapia",
         "Centros de radioterapia são regulados pela CNEN (Norma CNEN NN 6.10) que exige: físico médico responsável, programa de garantia de qualidade documentado (calibração diária e periódica do acelerador, IMRT QA por paciente), registro de doses entregues vs. prescritas por fração, plano de emergência radiológica e relatórios periódicos à CNEN. SaaS que automatizam os registros de controle de qualidade e geram relatórios regulatórios eliminam trabalho manual significativo dos físicos médicos e reduzem o risco de não-conformidades em inspeções."),
        ("Expansão de Receita e Módulos de Alto Valor",
         "Módulos com maior uptake após conversão: gestão de consultas de radioterapeuta (agendamento de simulação, planejamento e fracionamento), portal do paciente para acompanhamento de sessões e comunicação com a equipe, telemedicina para teleconsultas de seguimento pós-RT, integração com prontuário oncológico para continuidade do cuidado (o mesmo paciente frequentemente recebe quimio e RT), e analytics de controle de qualidade com alertas de desvio de dose vs. prescrito. Para centros com múltiplos Linacs e volumes acima de 50 pacientes/dia, soluções de agendamento otimizado de sala e equipamento são diferencial importante."),
    ],
    faq_list=[
        ("O que é VMAT (Volumetric Modulated Arc Therapy) e quais as vantagens sobre técnicas convencionais?",
         "VMAT é uma técnica avançada de radioterapia em que o acelerador linear gira em arco em torno do paciente enquanto modula continuamente a dose, otimizando a conformação ao tumor e a proteção de órgãos críticos. As principais vantagens são: tratamento mais rápido (2-3 minutos vs. 15-20 minutos de IMRT estática), conformação de dose superior, redução de dose em órgãos de risco e melhor conforto para o paciente. VMAT está disponível na maioria dos Linacs modernos (Varian TrueBeam, Elekta Unity, Siemens)."),
        ("Físico médico é obrigatório em centros de radioterapia no Brasil?",
         "Sim, a Norma CNEN NN 6.10 exige físico médico responsável pelo programa de garantia de qualidade de todo serviço de radioterapia. O físico médico é responsável pela calibração dos equipamentos, aprovação dos planos de tratamento e controle de qualidade das doses entregues. O CRBM (Conselho Regional de Biomedicina) e o CRFi (Conselho Regional de Física) regulam a atuação profissional dos físicos médicos no Brasil."),
        ("SaaS de gestão pode integrar com o sistema Aria ou Mosaiq de radioterapia?",
         "Sim, via interface HL7 FHIR ou protocolos proprietários documentados pelos fabricantes (Varian Aria e Elekta Mosaiq têm APIs disponíveis). A integração permite sincronização de cadastro de pacientes, prescrições de RT, status de frações realizadas e dados de dose. A qualidade e o esforço de implementação dessa integração é um diferencial técnico crítico para SaaS que atendem centros de radioterapia — não ter essa integração significa entrada manual de dados duplicada, o que é inaceitável para equipes de alta ocupação."),
    ]
)

# Article 4378 — Consulting: due diligence e valuation de empresas
art(
    slug="consultoria-de-due-diligence-e-valuation-de-empresas",
    title="Consultoria de Due Diligence e Valuation de Empresas | ProdutoVivo",
    desc="Como estruturar e posicionar uma consultoria de due diligence e valuation para M&A, captação de investimento e processos de sucessão empresarial.",
    h1="Consultoria de Due Diligence e Valuation de Empresas",
    lead="Due diligence e valuation são serviços de alta demanda em transações de M&A, captação de capital (VC, PE, CVM 476), IPOs e processos de sucessão familiar. Consultorias especializadas nessa área precisam combinar expertise financeira, jurídica e setorial para entregar análises que suportem decisões de alto impacto.",
    sections=[
        ("Mercado de M&A e Demanda por Due Diligence no Brasil",
         "O mercado de M&A no Brasil movimenta mais de R$ 200 bilhões por ano em transações, com participação crescente de private equity, venture capital e compradores estratégicos. Cada transação requer due diligence em múltiplas frentes — financeira, fiscal, jurídica, operacional, comercial e ambiental — além de valuation do negócio-alvo. A demanda por consultoras independentes de DD e valuation cresce com: o aumento de fusões no mercado médio, a profissionalização de empresas familiares que atraem PE, e o crescimento de transações de startups com fundos de VC."),
        ("Due Diligence Financeira: Escopo e Entregáveis",
         "A due diligence financeira analisa a qualidade e sustentabilidade dos resultados financeiros históricos e projetados do alvo: ajustes de EBITDA (normalização de receitas e despesas não recorrentes), análise de capital de giro e sazonalidade, qualidade da receita (concentração de clientes, recorrência, contratualização), estrutura de dívida e passivos contingentes, e projeções financeiras com avaliação de premissas. O relatório de DD financeira é o documento central de uma transação — fundamenta o valuation e orienta as negociações de representations & warranties do SPA (Share Purchase Agreement)."),
        ("Valuation: Metodologias e Aplicações",
         "As metodologias de valuation mais usadas em transações de M&A incluem: DCF (Discounted Cash Flow — fluxo de caixa descontado, principal método de valor intrínseco), múltiplos de mercado comparáveis (EV/EBITDA, EV/Receita — benchmarking com pares públicos e transações comparáveis), e método de ativos líquidos ajustados (para empresas com grande base de ativos). Em transações de startups, múltiplos de crescimento (ARR múltiple, GMV múltiple) e análise de benchmark de rodadas comparáveis são os métodos dominantes. A combinação de metodologias em uma 'football field' de valuation mostra o range de valor."),
        ("Due Diligence Fiscal e Jurídica: Passivos Contingentes",
         "A due diligence fiscal mapeia passivos tributários históricos e potenciais: autos de infração abertos, discussões administrativas e judiciais, diferenças de regime tributário, benefícios fiscais em risco de questionamento e passivos de FGTS e INSS. A jurídica mapeia contratos relevantes (cláusulas de change of control), processos judiciais e trabalhistas, propriedade intelectual e regulatório setorial. O discovery de passivos contingentes na DD determina o ajuste do preço de compra (representations & warranties, earn-out, escrow) para proteção do comprador."),
        ("Monetização e Posicionamento da Consultoria de DD",
         "Due diligence financeira de empresa de médio porte (R$ 50-300M de faturamento) custa de R$ 80.000 a R$ 250.000. Valuation independente para transação de R$ 50M a R$ 300M custa de R$ 30.000 a R$ 100.000. Em transações maiores (acima de R$ 500M), os honorários de DD podem ultrapassar R$ 500.000. A combinação de DD financeira + valuation + suporte na negociação do SPA é o portfólio completo que diferencia consultoras independentes das divisões de transações de grandes firmas (Big Four, boutiques de IB). A especialização setorial (saúde, agro, tecnologia, educação) permite cobrar prêmio e acelerar o trabalho."),
    ],
    faq_list=[
        ("O que é EBITDA ajustado e por que é central no valuation de empresas privadas?",
         "EBITDA ajustado é o EBITDA (Earnings Before Interest, Taxes, Depreciation and Amortization) normalizado para refletir a capacidade de geração de caixa recorrente e sustentável do negócio — excluindo itens não recorrentes (despesas extraordinárias, ganhos de venda de ativos, eventos únicos) e remuneração de sócios acima do mercado. Em empresas privadas, o EBITDA ajustado é o ponto de partida para o valuation por múltiplos (EV/EBITDA), que compara o valor da empresa com o valor de empresas similares."),
        ("Quais são os principais riscos identificados em due diligences de empresas brasileiras?",
         "Os riscos mais frequentes incluem: passivos fiscais não provisionados (especialmente ICMS, PIS/COFINS e tributação de operações não documentadas), passivos trabalhistas de funcionários informais ou mal categorizados como PJ, contratos com clientes sem exclusividade ou com cláusulas de rescisão fácil que comprometem a receita pós-transação, dependência excessiva de sócios-fundadores que saem na transação, e questões ambientais em empresas industriais ou rurais."),
        ("Valuation por múltiplos ou DCF é mais adequado para startups brasileiras?",
         "Para startups em crescimento acelerado (crescimento acima de 50% aa), valuation por múltiplos de ARR (Annual Recurring Revenue) ou GMV é mais prático — compara com rodadas recentes de empresas similares no mercado de VC brasileiro e regional. DCF é mais adequado para empresas em fase de maturidade com fluxo de caixa previsível. Startups em estágio inicial (pré-receita) são valuadas por benchmarks de mercado, tamanho do mercado endereçável e qualidade do time — métricas mais qualitativas do que quantitativas."),
    ]
)

# Article 4379 — B2B SaaS: plataforma de dados e integração de sistemas
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-plataforma-de-dados-e-integracao-de-sistemas",
    title="Gestão de Negócios para SaaS de Plataforma de Dados e Integração de Sistemas | ProdutoVivo",
    desc="Como escalar um B2B SaaS de plataforma de dados e integração de sistemas (iPaaS): produto, vendas enterprise e retenção em mercado técnico.",
    h1="Gestão de Negócios para SaaS de Plataforma de Dados e Integração de Sistemas",
    lead="iPaaS (Integration Platform as a Service) e plataformas de dados são categorias de SaaS de alto valor técnico e estratégico. Empresas com múltiplos sistemas legados e necessidade de integração de dados em tempo real são o cliente ideal — e o problema é pervasivo em praticamente toda organização de médio e grande porte.",
    sections=[
        ("Mercado de iPaaS e Integração de Dados no Brasil",
         "Praticamente toda empresa de médio porte tem um problema de integração: o CRM não conversa com o ERP, o e-commerce não sincroniza com o estoque, o sistema de RH não atualiza o BI. Integrações ponto-a-ponto em código se tornam impraticáveis com o crescimento do número de sistemas. iPaaS resolve esse problema com conectores prontos (APIs) e fluxos de integração configuráveis sem código ou com baixo código. Players globais como MuleSoft, Boomi, Zapier e Make (Integromat) dominam o espaço; há espaço para soluções nacionais com foco em sistemas brasileiros (TOTVS, Sankhya, Omie, Conta Azul, VTEX)."),
        ("Produto: Conectores, ETL e Dados em Tempo Real",
         "Os diferenciais de produto que mais importam: biblioteca de conectores para sistemas brasileiros relevantes (ERPs nacionais, bancos via Open Finance, plataformas de e-commerce como Shopify e VTEX, marketplaces como Mercado Livre e Amazon), motor de transformação de dados (ETL/ELT) com suporte a mapeamento complexo de campos, streaming de dados em tempo real para casos de uso de inventário e preços, e interface no-code/low-code que permite que analistas de negócio (não apenas devs) configurem integrações. Monitoramento de integrações com alertas de falha e painel de saúde é indispensável."),
        ("Vendas para CIOs e Arquitetos de Sistemas",
         "O comprador de iPaaS é o CIO, arquiteto de sistemas ou gerente de TI. O ciclo de vendas é de 3 a 9 meses para enterprise, com POC técnico (demonstração com os sistemas do cliente) como passo decisivo. O argumento mais eficaz é o custo de integrações customizadas em código: 'cada integração ponto-a-ponto custa entre R$ 30.000 e R$ 150.000 em desenvolvimento + manutenção — a plataforma permite criar a mesma integração em 1-2 dias, e gerenciar dezenas delas no mesmo lugar'. A redução de time-to-integration de semanas para horas é tangível e mensurável."),
        ("Modelo de Negócio e Precificação de iPaaS",
         "Modelos de precificação comuns: por número de tarefas/operações executadas por mês (Zapier/Make), por número de conexões ativas (número de integrações), por volume de dados processados (GB/mês), ou por usuário da plataforma. Para enterprise, pricing por capacidade contratada (número de integrações + volume + SLA de suporte) com contratos anuais é o mais comum. A camada de serviços profissionais (implementação, design de integrações complexas) é fonte de receita adicional relevante no segmento enterprise — frequentemente 30-50% do ARR de software."),
        ("Retenção e Expansão em SaaS de Integração",
         "iPaaS tem uma das maiores taxas de retenção do universo SaaS: quando as integrações estão rodando, ninguém quer migrar — o custo de refazer todas as integrações é proibitivo. A expansão acontece naturalmente: cada novo sistema adotado pelo cliente cria demanda por novas integrações na plataforma. NRR acima de 130% é comum no segmento. O risco de churn é maior nos primeiros 90 dias (antes da primeira integração em produção) — onboarding técnico acelerado é crítico para sobreviver a esse período."),
    ],
    faq_list=[
        ("O que é iPaaS e como difere de uma integração ponto-a-ponto via API?",
         "iPaaS (Integration Platform as a Service) é uma plataforma centralizada que gerencia múltiplas integrações entre sistemas, com conectores prontos, monitoramento, versionamento e interface visual de configuração. Integração ponto-a-ponto via API é código escrito especificamente para conectar dois sistemas — funciona para uma conexão, mas torna-se difícil de manter com dezenas de sistemas. iPaaS resolve o problema de escala: uma plataforma para todas as integrações, com visibilidade centralizada e menos dependência de desenvolvimento manual."),
        ("No-code iPaaS é adequado para integrações corporativas complexas?",
         "No-code/low-code iPaaS (como Zapier, Make, n8n) é excelente para integrações simples de médio volume (até algumas centenas de operações/hora). Para integrações corporativas de alto volume (milhares de eventos/segundo), transformações de dados complexas ou integrações com sistemas legados sem API REST moderna, plataformas enterprise (MuleSoft, Boomi, Azure Integration Services) são mais adequadas. O mercado está convergindo — plataformas enterprise adicionam interfaces low-code, e plataformas no-code adicionam capacidades enterprise."),
        ("ETL e iPaaS são a mesma coisa?",
         "Não exatamente. ETL (Extract, Transform, Load) é um processo focado em movimentação de dados em lote para analytics — tipicamente pipelines de dados que alimentam data warehouses e BI. iPaaS é mais amplo: foca na integração operacional em tempo real entre sistemas (não apenas mover dados, mas orquestrar processos de negócio entre sistemas). Muitas plataformas modernas de dados (Fivetran, Airbyte, dbt) são especializadas em ETL/ELT, enquanto iPaaS como MuleSoft ou Boomi cobrem tanto integração operacional quanto pipelines de dados."),
    ]
)

# Article 4380 — Clinic: neonatologia e unidade de cuidados intermediários neonatais
art(
    slug="gestao-de-clinicas-de-neonatologia-e-unidade-de-cuidados-intermediarios-neonatais",
    title="Gestão de Clínicas de Neonatologia e Unidade de Cuidados Intermediários Neonatais | ProdutoVivo",
    desc="Como gerenciar serviços de neonatologia e UCINco: fluxo de alta complexidade, tecnologia assistencial, equipe e sustentabilidade financeira.",
    h1="Gestão de Clínicas de Neonatologia e Unidade de Cuidados Intermediários Neonatais",
    lead="Neonatologia é uma das especialidades pediátricas de maior complexidade técnica e emocional. UCINs (Unidades de Cuidados Intermediários Neonatais) e UTINs (Unidades de Terapia Intensiva Neonatal) requerem gestão rigorosa de equipe, tecnologia e protocolos para garantir os melhores desfechos em recém-nascidos prematuros e de alto risco.",
    sections=[
        ("Panorama da Neonatologia no Brasil",
         "O Brasil tem taxas de prematuridade acima da média mundial — cerca de 12% dos nascimentos são prematuros, gerando demanda expressiva por serviços de neonatologia intensiva e intermediária. A mortalidade neonatal reduziu significativamente com a expansão de UTINs e a implementação de protocolos como o Método Canguru (contato pele a pele precoce) e o cuidado centrado na família. O cuidado ao prematuro extremo (abaixo de 28 semanas) requer equipe altamente especializada e tecnologia de alta complexidade (ventilação de alta frequência, surfactante, fototerapia de alta intensidade)."),
        ("Estrutura e Fluxo da UCIN e UTIN",
         "A diferença entre UCIN (Unidade de Cuidados Intermediários Neonatais) e UTIN (UTI Neonatal) é o nível de complexidade assistencial: a UTIN atende prematuros extremos e recém-nascidos criticamente doentes com suporte ventilatório invasivo, acesso venoso central e monitoração contínua; a UCIN atende prematuros tardios e RNs estáveis que não precisam mais de UTI mas ainda requerem suporte (oxigenioterapia, sonda nasogástrica, fototerapia). A transição adequada de UTIN para UCIN e desta para alojamento conjunto é um marcador de eficiência assistencial."),
        ("Tecnologia Assistencial e Equipamentos em Neonatologia",
         "Investimentos essenciais incluem: incubadoras de dupla parede (controle de temperatura e umidade), berços de calor radiante para procedimentos, ventiladores neonatais com modalidades de alta frequência oscilatória (VAFO), monitores multiparamétricos com tendência de SpO2, FC, FR e PA, bombas de infusão de alta precisão para medicações de alto risco (dobutamina, prostaglandina, morfina), equipamentos de fototerapia de alta intensidade para hiperbilirrubinemia e sistema de infusão venosa umbilical. O sistema de monitoração centralizada (central de enfermagem) é crítico para segurança em unidades com múltiplos leitos."),
        ("Equipe e Protocolos de Segurança do Paciente",
         "A equipe de UTIN inclui: neonatologista (pediatra com residência em neonatologia), médico de suporte (pediatria geral ou residente), enfermeiro especializado em neonatologia, técnico de enfermagem com treinamento específico, fisioterapeuta neonatal (ventilação e fisioterapia respiratória), fonoaudiólogo (sucção e deglutição em prematuros) e assistente social. A relação de enfermeiro por leito de UTIN recomendada é de 1:2 (um enfermeiro para cada dois pacientes). Protocolos de segurança — bundles de prevenção de IPCS, lesão por pressão em prematuro, extravasamento de acesso venoso periférico — são indispensáveis."),
        ("Faturamento, Convênios e Sustentabilidade de Serviços Neonatais",
         "UTIN e UCIN têm faturamento complexo: a diária de UTIN tem código específico no rol ANS, com valores variáveis por convênio. Além da diária, procedimentos como punção lombar, cateterismo umbilical, surfactante, transfusões e exsanguinotransfusão têm códigos separados. O alto custo de operação (equipamentos, medicamentos de alto custo como surfactante a R$ 8.000/frasco, equipe 24h) requer negociação rigorosa de tabelas com convênios. Serviços SUS-referenciados (portaria MS de alta e média complexidade neonatal) têm financiamento via FAEC (Fundo de Ações Estratégicas e Compensação)."),
    ],
    faq_list=[
        ("O que é o Método Canguru e quais são os benefícios comprovados?",
         "O Método Canguru é a prática de manter o recém-nascido prematuro ou de baixo peso em contato pele a pele com os pais, em posição vertical sobre o peito, de forma prolongada e contínua. Benefícios comprovados por evidências: estabilização da temperatura corporal (o calor do corpo do pai/mãe regula a temperatura do RN), ganho de peso mais rápido, redução do tempo de internação em UTIN, maior taxa de aleitamento materno, redução da dor em procedimentos e melhora do vínculo afetivo. O MS brasileiro implantou o MC em 3 etapas, com início ainda na UTIN."),
        ("Qual é a relação de leitos de UTIN recomendada por 1.000 nascidos vivos?",
         "A OMS recomenda de 3 a 5 leitos de UTI Neonatal por 1.000 nascidos vivos. No Brasil, a cobertura é heterogênea: regiões Sul e Sudeste têm cobertura próxima ao recomendado; regiões Norte e Nordeste têm déficit significativo. O Ministério da Saúde tem programas de expansão de UTIN em regiões deficitárias (Rede Cegonha e outros programas de atenção perinatal)."),
        ("Surfactante exógeno é coberto pelo SUS?",
         "Sim. O surfactante exógeno (Curosurf, Survanta, Calfactant) é disponibilizado pelo SUS para recém-nascidos prematuros com síndrome do desconforto respiratório (SDR). O tratamento via SUS é via APAC de alta complexidade neonatal, com protocolo específico do Ministério da Saúde. O custo de um frasco de surfactante é de R$ 6.000 a R$ 10.000 — tornando o acesso pelo SUS fundamental para a maioria das famílias."),
    ]
)

# Article 4381 — SaaS sales: clínicas de odontopediatria e ortodontia infantil
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-odontopediatria-e-ortodontia-infantil",
    title="Vendas de SaaS para Clínicas de Odontopediatria e Ortodontia Infantil | ProdutoVivo",
    desc="Como vender SaaS de gestão para clínicas de odontopediatria e ortodontia infantil: abordagem, gestão financeira e expansão de receita.",
    h1="Vendas de SaaS para Clínicas de Odontopediatria e Ortodontia Infantil",
    lead="Odontopediatria e ortodontia infantil são especializações odontológicas com alto índice de fidelização — crianças que iniciam o acompanhamento na infância podem se tornar pacientes por décadas. Vender SaaS para esse segmento exige entender a dinâmica familiar do atendimento e a gestão de tratamentos ortodônticos de longa duração.",
    sections=[
        ("Perfil do Mercado de Odontopediatria e Ortodontia no Brasil",
         "Odontopediatria atende crianças desde o nascimento (frenotomia lingual neonatal, erupção dentária) até a adolescência, com foco em prevenção, cárie dentária e hábitos bucais deletérios (chupeta, sucção digital). Ortodontia infantil abrange aparelhos funcionais ortopédicos (placa de Hawley, bionator, facemask) e aparelho ortodôntico fixo a partir dos 11-12 anos. Tratamentos ortodônticos duram de 18 a 36 meses com consultas mensais — gerando receita recorrente previsível e alta fidelização da família ao consultório."),
        ("Necessidades Específicas de Software para Odontopediatria e Ortodontia",
         "Os requisitos mais valorizados incluem: prontuário com odontograma pediátrico (dentes decíduos e permanentes, marcação de tratamentos realizados e planejados), gestão de contratos de ortodontia (contrato de serviço com valor total, parcelamento e controle de pagamentos mensais ao longo de 2-3 anos), envio de lembretes automatizados para consultas mensais de ajuste (taxa de falta em ortodontia é alta — lembretes reduzem em 30-40%), galeria de fotos de progresso ortodntico, e agendamento com slots diferenciados por tipo de procedimento (urgência, avaliação, ajuste, contenção)."),
        ("Abordagem de Prospecção para o Segmento",
         "O decisor é o odontopediatra ou ortodontista proprietário da clínica. Prospecção eficaz: presença no CONBRAP (Congresso Brasileiro de Ortodontia e Ortopedia Facial), SBO (Sociedade Brasileira de Ortodontia), ABOi (Associação Brasileira de Odontopediatria), Instagram e YouTube (onde odontopediatras e ortodontistas são muito ativos — conteúdo de marketing pessoal para captação de pacientes), e parcerias com distribuidores de materiais ortodônticos (Morelli, GAC, 3M Unitek) que indicam software à rede de clientes."),
        ("Faturamento de Ortodontia: Contratos de Longo Prazo",
         "Tratamentos ortodônticos são vendidos como um pacote (ex: R$ 3.500 a R$ 8.000 por tratamento completo), com pagamento parcelado em mensalidades de R$ 150 a R$ 400/mês durante o tratamento. O sistema precisa controlar: valor total contratado, parcelas pagas e em aberto, inadimplência por paciente, e gerar alertas para cobranças. O controle de inadimplência é crítico — em ortodontia, o profissional já realizou grande parte do tratamento antes da detecção de inadimplência, tornando o controle preventivo indispensável."),
        ("Expansão de Receita e Módulos de Valor Agregado",
         "Módulos com maior interesse após conversão: marketing de indicação automatizado (envio de convite para indicação de família após 90 dias de tratamento satisfatório), pesquisa de satisfação pós-avaliação inicial para identificar melhorias no processo de conversão, telemedicina para teleconsultas de urgência (dor, braquete solto) para triagem antes da consulta presencial, e plataforma de educação do paciente com vídeos sobre higiene ortodôntica e alimentos permitidos — reduz as urgências por higiene inadequada durante o tratamento."),
    ],
    faq_list=[
        ("A que idade uma criança deve ter a primeira consulta com odontopediatra?",
         "A Academia Americana de Odontopediatria (AAPD) e a ABOi recomendam a primeira consulta ao nascer o primeiro dente decíduo (em média aos 6 meses) ou até 1 ano de idade. A consulta precoce tem foco em prevenção: orientação aos pais sobre higiene bucal do bebê, cuidados com a chupeta e mamadeira, e identificação de freio lingual curto (anquiloglossia) que pode afetar a amamentação."),
        ("Aparelho ortodôntico em crianças é recomendado a partir de que idade?",
         "Aparelhos funcionais ortopédicos (que aproveitam o crescimento ativo para corrigir discrepâncias esqueléticas como maxila retruída ou mandíbula projetada) têm maior eficácia entre 7 e 11 anos (fase de crescimento ativo). Aparelhos fixos convencionais (brackets) são iniciados geralmente após a erupção dos dentes permanentes, em torno dos 11-13 anos. O ortodontista avalia caso a caso — alguns problemas (mordida cruzada posterior, atresia maxilar) requerem tratamento precoce."),
        ("Contratos de ortodontia precisam de registro em cartório?",
         "Não é obrigatório por lei, mas contratos de serviço odontológico com valor relevante se beneficiam de formalização para proteção de ambas as partes. O CFO (Conselho Federal de Odontologia) recomenda que contratos odontológicos contenham: identificação das partes, descrição do tratamento, valor total e forma de pagamento, prazo estimado, e responsabilidades de cada parte. Contratos digitais assinados com certificado ICP-Brasil têm validade jurídica plena."),
    ]
)

# Article 4382 — Consulting: gestão de projetos ágeis e transformação Scrum/Kanban
art(
    slug="consultoria-de-gestao-de-projetos-ageis-e-transformacao-para-scrum-e-kanban",
    title="Consultoria de Gestão de Projetos Ágeis e Transformação Scrum e Kanban | ProdutoVivo",
    desc="Como estruturar uma consultoria de agilidade e gestão de projetos com Scrum e Kanban: treinamentos, coaching ágil e transformações corporativas.",
    h1="Consultoria de Gestão de Projetos Ágeis e Transformação Scrum e Kanban",
    lead="Agilidade corporativa e frameworks como Scrum, Kanban e SAFe são demandas crescentes em organizações que precisam aumentar a velocidade de entrega e a adaptabilidade. Consultorias de agilidade têm mercado robusto tanto em empresas de tecnologia quanto em setores tradicionais em transformação digital.",
    sections=[
        ("Mercado e Oportunidade para Consultoria de Agilidade",
         "A adoção de metodologias ágeis cresceu exponencialmente no Brasil na última década, impulsionada pela transformação digital e pela necessidade de times de tecnologia entregarem valor mais rapidamente. O mercado de consultoria de agilidade abrange: treinamentos (certificações CSM, PSM, PSPO, SAFe), coaching ágil para times e lideranças, Agile Transformation para toda a organização (não apenas TI), e consultoria de fluxo de trabalho com Kanban para operações não-tecnológicas. O potencial de escala via programas de treinamento é uma das maiores vantagens do segmento."),
        ("Scrum vs. Kanban: Aplicações e Diferenças",
         "Scrum é um framework iterativo com sprints (ciclos fixos de 1-4 semanas), papéis definidos (Scrum Master, Product Owner, Developers) e cerimônias estruturadas (Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective). É mais adequado para times de desenvolvimento de produto com escopo evolutivo. Kanban é um método de gestão de fluxo com visualização de trabalho em andamento, limites de WIP (Work In Progress) e foco em fluxo contínuo — mais adequado para operações de suporte, manutenção e fluxos com demanda variável. A consultoria avalia qual abordagem melhor se adapta ao contexto de cada equipe."),
        ("Coaching Ágil: Individual, de Time e Organizacional",
         "O coaching ágil opera em três níveis: individual (coaching de Scrum Masters, Product Owners e líderes de TI para desenvolver capacidades ágeis), de time (facilitação de cerimônias, identificação e remoção de impedimentos, desenvolvimento de práticas de engenharia como TDD e CI/CD), e organizacional (alinhamento de estrutura, governança, orçamento e métricas com princípios ágeis). A Academy of Agile Coaching (AoAC) e o ICAgile definem padrões de competência para coaches ágeis. A certificação ICP-ACC (ICAgile Certified Professional in Agile Coaching) é o nível básico reconhecido."),
        ("SAFe e Agilidade em Escala para Grandes Organizações",
         "Para organizações com dezenas ou centenas de times ágeis, frameworks de agilidade em escala são necessários: SAFe (Scaled Agile Framework — o mais adotado no Brasil), LeSS (Large-Scale Scrum) e Spotify Model (modelo de squads, chapters e tribes). SAFe adiciona elementos de planejamento de Program Increment (PI Planning), Agile Release Trains (ARTs) e governança lean para coordenar múltiplos times. Implementações de SAFe em grandes corporações brasileiras (bancos, telecomunicações, indústrias) são projetos de 12 a 36 meses com equipes de 10 a 30 coaches ágeis."),
        ("Monetização e Posicionamento da Consultoria de Agilidade",
         "Treinamentos e certificações (CSM, PSPO, SAFe) são vendidos por turma de R$ 3.000 a R$ 6.000 por participante — alto volume e margem atraente. Coaching ágil de time é contratado em retainers mensais de R$ 8.000 a R$ 20.000 por time. Transformações ágeis organizacionais custam de R$ 200.000 a R$ 2.000.000 dependendo do escopo e da duração. A capacidade de oferecer os três tipos de serviço (treinamento + coaching + transformação) cria sinergias — participantes de treinamento viram clientes de coaching, e coaching de times evolui para transformação organizacional."),
    ],
    faq_list=[
        ("Qual a diferença entre Scrum Master e Agile Coach?",
         "Scrum Master atua dentro de um time específico, garantindo que o time entenda e adote Scrum, facilitando cerimônias e removendo impedimentos. Agile Coach tem escopo mais amplo: trabalha com múltiplos times, lideranças e a organização, com foco em transformação cultural e sistêmica. O Agile Coach também pode trabalhar com frameworks não-Scrum (Kanban, SAFe, LeSS) e com dimensões de agilidade de negócio além da engenharia. A maturidade e experiência exigida do Agile Coach é significativamente maior."),
        ("Agilidade funciona para setores não-tecnológicos como RH, financeiro e marketing?",
         "Sim — o Kanban é especialmente eficaz para operações de serviço e suporte (RH, financeiro, atendimento ao cliente) onde o fluxo é contínuo e imprevisível. Times de marketing adotam Scrum ou metodologias adaptadas (Marketing Scrum, Agile Marketing). A chave é adaptar os princípios ao contexto — não aplicar mecanicamente o Scrum de desenvolvimento de software a operações que têm natureza diferente. Consultorias que entendem as nuances setoriais entregam melhores resultados."),
        ("Quanto tempo leva uma transformação ágil corporativa?",
         "Transformações ágeis reais levam de 18 a 36 meses para mudança cultural sustentável. Iniciativas de 6-12 meses podem implantar práticas ágeis em times de TI, mas transformação da cultura de decisão, orçamento e governança requer mais tempo. O maior fator de sucesso é o comprometimento da liderança sênior — transformações lideradas de baixo para cima (bottom-up apenas) frequentemente estagnam no nível médio de gestão."),
    ]
)

# ── Sitemap & trilha updates ──────────────────────────────────────────────────
import pathlib

root = pathlib.Path(__file__).parent

slugs = [
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-qualidade-e-rastreabilidade-na-industria-de-alimentos",
     "Gestão de Negócios para SaaS de Qualidade e Rastreabilidade na Indústria de Alimentos"),
    ("gestao-de-clinicas-de-oncologia-clinica-e-imunoterapia",
     "Gestão de Clínicas de Oncologia Clínica e Imunoterapia"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-centros-de-oncologia-e-radioterapia",
     "Vendas de SaaS para Centros de Oncologia e Radioterapia"),
    ("consultoria-de-due-diligence-e-valuation-de-empresas",
     "Consultoria de Due Diligence e Valuation de Empresas"),
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-plataforma-de-dados-e-integracao-de-sistemas",
     "Gestão de Negócios para SaaS de Plataforma de Dados e Integração de Sistemas"),
    ("gestao-de-clinicas-de-neonatologia-e-unidade-de-cuidados-intermediarios-neonatais",
     "Gestão de Clínicas de Neonatologia e Unidade de Cuidados Intermediários Neonatais"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-odontopediatria-e-ortodontia-infantil",
     "Vendas de SaaS para Clínicas de Odontopediatria e Ortodontia Infantil"),
    ("consultoria-de-gestao-de-projetos-ageis-e-transformacao-para-scrum-e-kanban",
     "Consultoria de Gestão de Projetos Ágeis e Transformação Scrum e Kanban"),
]

sitemap_path = root / "sitemap.xml"
sm = sitemap_path.read_text(encoding="utf-8")
new_urls = "".join(f"<url><loc>https://produtovivo.com.br/blog/{s}/</loc></url>\n" for s, _ in slugs)
sitemap_path.write_text(sm.replace("</urlset>", new_urls + "</urlset>"), encoding="utf-8")

trilha_path = root / "trilha.html"
tr = trilha_path.read_text(encoding="utf-8")
new_items = "".join(f'<li><a href="/blog/{s}/">{t}</a></li>\n' for s, t in slugs)
trilha_path.write_text(tr.replace("</ul>", new_items + "\n</ul>", 1), encoding="utf-8")

print("Done — batch 1446")
