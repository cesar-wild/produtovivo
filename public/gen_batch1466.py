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


# Article 4415 — B2B SaaS: gestão de obras e construção civil
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-obras-e-construcao-civil",
    title="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Obras e Construção Civil",
    desc="Como escalar um SaaS B2B de gestão de obras e construção civil: mercado, funcionalidades, modelo de negócio e vendas para construtoras e incorporadoras.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Obras e Construção Civil",
    lead="O setor de construção civil brasileiro movimenta mais de R$ 500 bilhões anuais e historicamente opera com baixa digitalização. SaaS de gestão de obras que entregam controle de cronograma, orçamento, qualidade e comunicação em campo têm oportunidade enorme em um setor que começa a adotar tecnologia como diferencial competitivo.",
    sections=[
        ("O Mercado de Construção Civil e a Oportunidade de Digitalização", "A construção civil é um dos setores com menor índice de digitalização no Brasil — a maioria das construtoras ainda gerencia obras com planilhas, WhatsApp e registros em papel. Incorporadoras de médio porte, construtoras de galpões logísticos, empresas de obras de infraestrutura e reformas comerciais de grande porte são os segmentos com maior abertura para SaaS. A pandemia acelerou a adoção de ferramentas digitais ao dificultar o acompanhamento presencial de obras. Regulações como o BIM (Building Information Modeling) obrigatório para obras públicas acima de certo valor criam um ciclo de digitalização que abre portas para plataformas de gestão de obras."),
        ("Funcionalidades Essenciais para SaaS de Obras", "Uma plataforma de gestão de obras deve cobrir: cronograma de obra (linha do tempo, predecessores, caminho crítico), orçamento e controle de custos (previsto vs. realizado por etapa), medição de serviços (boletim de medição), diário de obra digital com fotos georreferenciadas, gestão de subcontratados e fornecedores de materiais, controle de qualidade com checklists por etapa, PPCI (Plano de Prevenção Contra Incêndios) e PCMSO/PPRA para segurança do trabalho, e comunicação centralizada entre escritório e campo via mobile. A usabilidade mobile é crítica — mestres de obras e engenheiros de campo precisam usar o sistema em canteiro, sem infraestrutura de TI."),
        ("Modelo de Negócio e Precificação em SaaS de Construção", "O modelo de precificação mais comum é por obra ativa (pay-per-project) ou por número de usuários simultâneos. Construtoras com portfólio de múltiplas obras simultâneas preferem contratos de plataforma com licença irrestrita. A sazonalidade do setor (volume de obras varia ao longo do ano e do ciclo econômico) cria desafios para MRR estável — contratos anuais com mínimo garantido e módulos adicionais por obra extras ajudam a suavizar a variabilidade. Para PMEs de construção, modelos de assinatura mensal mais acessíveis (R$ 300-800/mês) reduzem a barreira de entrada."),
        ("Estratégia de Vendas para Construtoras e Incorporadoras", "O ciclo de vendas em construção é tipicamente longo (60 a 120 dias) e envolve engenheiros de produção, diretores de operações e financeiro. A entrada mais eficaz é por engenheiros de obra ou gestores de projetos, que sentem a dor no dia a dia. Participação em feiras como Feicon, ExpoRevestir e CONSTRUÇÃO BRASIL, além de eventos do SINDUSCON e da CBIC, cria visibilidade no setor. Cases de redução de prazo de obra e de custo por m² com uso da plataforma são os argumentos mais convincentes para construtoras orientadas a resultado. Pilotos em uma obra específica antes da expansão para o portfólio completo da empresa reduzem o risco percebido pelo cliente."),
        ("Tendências: BIM, IoT em Canteiro e Construção Industrializada", "O BIM (Building Information Modeling) transforma a forma de projetar e gerenciar obras — e SaaS que integra com modelos BIM (IFC, Revit, Navisworks) agrega valor crescente à medida que a adoção de BIM cresce. IoT em canteiro — câmeras inteligentes, sensores de temperatura e umidade em concreto, rastreamento de equipamentos pesados — cria um fluxo de dados em tempo real que melhora a qualidade do decisões de gestão de obra. A construção industrializada (módulos pré-fabricados, steel frame, wood frame) cresce no Brasil e demanda SaaS que suporte o planejamento e controle específicos desse modo de produção, diferente da construção convencional."),
    ],
    faq_list=[
        ("Qual é a diferença entre software de gestão de obras e ERP de construção?",
         "Software de gestão de obras foca no controle operacional do canteiro — cronograma, qualidade, comunicação em campo, medições. ERPs de construção têm escopo mais amplo: financeiro, fiscal, RH, compras e obras integrados. Para PMEs, o software de gestão de obras é suficiente; empresas maiores podem precisar de integração entre os dois."),
        ("BIM é obrigatório para todas as obras no Brasil?",
         "O Decreto 10.306/2020 estabelece implantação progressiva do BIM em obras e serviços contratados pela administração pública federal. Para obras privadas, o BIM ainda é opcional, mas cada vez mais requisitado por incorporadoras de grande porte e exigido em concursos de arquitetura."),
        ("Como calcular o ROI de um SaaS de gestão de obras para uma construtora?",
         "O ROI pode ser calculado pela redução de retrabalho e desperdício de materiais (tipicamente 5-15% do custo de obra), pela redução de atrasos (que geram multas contratuais e custos indiretos) e pela melhora na produtividade da equipe de engenharia, que passa menos tempo consolidando informações e mais tempo tomando decisões."),
    ]
)

# Article 4416 — Clinic: endocrinologia adulto e tireoide
art(
    slug="gestao-de-clinicas-de-endocrinologia-adulto-e-tireoide",
    title="Gestão de Clínicas de Endocrinologia Adulto e Tireoide",
    desc="Guia de gestão para clínicas de endocrinologia adulto com foco em doenças da tireoide, diabetes tipo 2, obesidade e distúrbios hormonais.",
    h1="Gestão de Clínicas de Endocrinologia Adulto e Tireoide",
    lead="A endocrinologia adulto é uma das especialidades com maior demanda no Brasil, impulsionada pela epidemia de diabetes tipo 2, obesidade, doenças da tireoide e síndrome metabólica. A gestão eficiente dessas clínicas exige combinar acompanhamento longitudinal de pacientes crônicos com recursos tecnológicos e equipe multiprofissional que suporte a complexidade metabólica dos casos.",
    sections=[
        ("Epidemiologia e Demanda em Endocrinologia no Brasil", "O Brasil tem mais de 16 milhões de diabéticos diagnosticados e estima-se que outros 8 milhões não sabem que têm a doença. A obesidade afeta mais de 50% da população adulta, e as doenças da tireoide (hipotireoidismo, hipertireoidismo, nódulos e câncer de tireoide) afetam aproximadamente 60 milhões de brasileiros. Essa carga epidemiológica massiva cria uma demanda estrutural por endocrinologistas que supera amplamente a oferta — há estimativas de um endocrinologista para cada 50 mil habitantes, muito abaixo do necessário. Clinicas bem localizadas e com agendamento ágil terão ocupação plena com facilidade."),
        ("Mix de Serviços e Especialização Dentro da Endocrinologia", "Uma clínica de endocrinologia pode optar por atender toda a amplitude da especialidade (diabetes, tireoide, obesidade, osteoporose, adrenal, hipófise) ou especializar-se em subespecialidades de maior complexidade ou maior volume: centro de diabetes com educação estruturada (CDE), clínica de tireoide com biópsia por punção aspirativa (PAAF) ecoguiada, centro de obesidade com programa multidisciplinar (médico, nutricionista, psicólogo, educador físico), ou endocrinologia reprodutiva e infertilidade. A especialização permite precificação premium e diferenciação em mercados competitivos."),
        ("Gestão do Paciente Crônico e Longitudinalidade do Cuidado", "A endocrinologia é eminentemente longitudinal — pacientes com diabetes tipo 2, hipotireoidismo e síndrome metabólica são acompanhados indefinidamente. A gestão eficiente dessa longitudinalidade requer: prontuário eletrônico com evolução clínica estruturada e gráficos de tendência de exames (HbA1c, TSH, colesterol ao longo do tempo), sistema de agendamento de retornos automático baseado na última consulta, alertas para pacientes que não retornam há mais tempo do que o protocolo indica, e integração com laboratórios para importação automática de resultados. Pacientes engajados com o acompanhamento têm melhores desfechos e representam receita recorrente previsível para a clínica."),
        ("Tecnologia Assistencial: CGM, Telemedicina e Telemonitoramento", "Monitores contínuos de glicose (CGM — Continuous Glucose Monitoring) como o Freestyle Libre e Dexcom revolucionaram o manejo do diabetes. Clínicas que suportam o acompanhamento de CGM — com leitura e interpretação dos dados de monitoramento contínuo na consulta e entre consultas — entregam cuidado de qualidade superior. A telemedicina é especialmente adequada para retornos de ajuste de medicação em pacientes estáveis com diabetes ou hipotireoidismo, liberando as consultas presenciais para casos mais complexos e novos pacientes. Programas de educação em diabetes por grupos online (Zoom, Teams) são eficientes em escala e melhoram a adesão ao tratamento."),
        ("Gestão Financeira e Sustentabilidade da Clínica de Endocrinologia", "Clínicas de endocrinologia têm perfil de receita fortemente baseado em consultas (volume elevado de retornos) e procedimentos como PAAF de tireoide (alto ticket, baixo volume). A negociação com convênios deve garantir tabelas adequadas para consultas de primeira vez (mais longas e complexas) separadas das consultas de retorno. Programas de diabetes educacionais em grupo podem ser faturados como educação em saúde por algumas operadoras, criando fonte adicional de receita. A complementação com venda de insumos (sensores de glicose, canetas de insulina para pacientes sem convênio) pode representar receita adicional relevante em clínicas com grande volume de diabéticos."),
    ],
    faq_list=[
        ("Com que frequência um diabético tipo 2 controlado deve consultar o endocrinologista?",
         "Pacientes com diabetes tipo 2 bem controlado (HbA1c < 7%) geralmente são avaliados a cada 3 a 6 meses. Pacientes em ajuste de tratamento ou com complicações podem precisar de consultas mensais. Entre as consultas, o telemonitoramento de glicemia e pressão arterial via aplicativo pode complementar o acompanhamento."),
        ("Nódulo de tireoide sempre precisa de biópsia?",
         "Não. A indicação de biópsia (PAAF guiada por ultrassom) depende das características ultrassonográficas do nódulo (tamanho, ecotextura, vascularização, microcalcificações) avaliadas segundo sistemas de estratificação de risco como o TIRADS. A maioria dos nódulos benignos só precisa de acompanhamento ultrassonográfico periódico."),
        ("Qual é a diferença entre hipotireoidismo e hipotireoidismo subclínico?",
         "Hipotireoidismo é a deficiência clínica de hormônios tireoidianos, com TSH elevado e T4 livre baixo, causando sintomas como fadiga, ganho de peso e intolerância ao frio. Hipotireoidismo subclínico é a elevação isolada do TSH com T4 livre normal — muitas vezes assintomático e com indicação de tratamento individualizada pelo endocrinologista."),
    ]
)

# Article 4417 — SaaS sales: centros de radioterapia e oncologia radioterapeuta
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-centros-de-radioterapia-e-oncologia-radioterapeuta",
    title="Vendas para o Setor de SaaS de Gestão de Centros de Radioterapia e Oncologia Radioterapeuta",
    desc="Estratégias de vendas B2B para plataformas SaaS voltadas a centros de radioterapia, oncologia radioterápica e medicina nuclear oncológica.",
    h1="Vendas para o Setor de SaaS de Gestão de Centros de Radioterapia e Oncologia Radioterapeuta",
    lead="Centros de radioterapia são unidades de alta complexidade e altíssimo custo operacional — aceleradores lineares custam milhões e demandam rigor extremo em segurança, controle de qualidade e gestão de pacientes. SaaS que suportam a gestão administrativa e clínica desses centros enfrentam um comprador exigente e um ciclo de vendas longo, mas conquistam contratos de alto valor e retenção elevada.",
    sections=[
        ("O Setor de Radioterapia no Brasil e Sua Complexidade Operacional", "O Brasil conta com cerca de 350 centros de radioterapia, distribuídos desigualmente pelo território nacional — a maioria na região Sudeste. Esses centros operam aceleradores lineares (LINAC), tomografia computadorizada de simulação, sistemas de planejamento de tratamento (TPS) e sistemas de controle de qualidade dosimétrica. A habilitação pelo Ministério da Saúde como CACON ou como serviço autônomo de radioterapia, a licença da CNEN (Comissão Nacional de Energia Nuclear) e a acreditação pelo CBR (Colégio Brasileiro de Radiologia) são requisitos regulatórios que tornam o ambiente do setor altamente regulado e o comprador muito criterioso em relação a novas tecnologias."),
        ("Proposta de Valor do SaaS em Centros de Radioterapia", "As necessidades de gestão em centros de radioterapia incluem: agendamento de simulação e tratamento com controle de disponibilidade de máquina (LINAC), gestão do prontuário radioterápico (prescrição, planejamento aprovado, registros de frações realizadas), controle de qualidade e dosimetria (registros de QA diário, semanal e mensal exigidos pela CNEN), faturamento de sessões para SUS e convênios privados com os códigos SIGTAP corretos, e relatórios de produção para habilitação e acreditação. A integração com os sistemas de planejamento de tratamento (Eclipse da Varian, Monaco da Elekta) e com registros eletrônicos de tratamento (ARIA, MOSAIQ) é o diferencial máximo para centros que querem unificar dados clínicos e administrativos."),
        ("Ciclo de Vendas e Stakeholders em Centros de Radioterapia", "O processo de venda em centros de radioterapia envolve: radioterapeuta (médico especialista — usuário e avaliador clínico principal), físico médico (avalia integração com sistemas de dosimetria e QA), gestor administrativo (avalia custo-benefício e faturamento), TI (avalia segurança e integração técnica) e Diretoria (aprova o investimento). O ciclo pode durar de 6 a 18 meses em grandes centros. A estratégia de entrada mais eficaz é por meio do físico médico ou do gestor administrativo — os dois com maior dor imediata. Demonstrações técnicas com simulação de um dia de trabalho real no centro são mais convincentes do que apresentações genéricas."),
        ("Canais de Acesso ao Mercado de Radioterapia", "Os canais mais relevantes incluem: Sociedade Brasileira de Radioterapia (SBRT), Associação Brasileira de Física Médica (ABFM), congressos de oncologia (SBOC, ASCO Brasil), feiras de equipamentos médicos (HOSPITALAR, FIME). Parceiros estratégicos são os fabricantes e distribuidores de LINAC (Varian/Siemens Healthineers, Elekta) — que têm acesso privilegiado a todos os centros que compram ou renovam seus equipamentos. Propostas de parceria de distribuição com fabricantes de equipamentos de radioterapia são uma das formas mais eficazes de ampliar o alcance de mercado de forma acelerada."),
        ("Retenção e Expansão de Conta em Centros de Radioterapia", "A retenção em centros de radioterapia é estruturalmente elevada — a migração de um sistema de gestão acumulado com anos de prontuários radioterápicos e registros de QA é extremamente custosa e arriscada. Contratos de longo prazo (3 a 5 anos) com cláusulas de atualização de versão e suporte são o padrão. A expansão ocorre com novos módulos (tele-oncologia, portal do paciente, módulo de pesquisa clínica) e com a adição de novas unidades quando o centro de radioterapia expande para outras cidades ou estados. Manter qualidade de suporte técnico de nível alta e ciclos de atualização regulares com melhorias clínicas solicitadas pelos usuários são os principais drivers de renovação contratual."),
    ],
    faq_list=[
        ("O SaaS de gestão de radioterapia precisa de certificação da CNEN?",
         "Sistemas que registram dados dosimétricos ou de tratamento radioterápico devem ser validados segundo as normas da CNEN e do CFM para prontuários eletrônicos. A conformidade com IEC 62304 (software para dispositivos médicos) é um diferencial que facilita a aceitação por físicos médicos e gestores de centros regulados."),
        ("Como o SaaS pode ajudar centros de radioterapia a cumprir os requisitos de acreditação?",
         "Relatórios automáticos de QA (controle de qualidade de máquinas), registros de falhas e manutenção, documentação de treinamento da equipe e métricas de segurança do paciente (near misses, incidentes) são funcionalidades que facilitam a coleta de evidências para processos de acreditação como o da ASTRO APEx e do CBR."),
        ("Qual é o código de faturamento SUS para sessões de radioterapia?",
         "No SIGTAP (Sistema de Gerenciamento da Tabela de Procedimentos do SUS), sessões de radioterapia estão cadastradas em grupos específicos por modalidade técnica (radioterapia conformacional 3D, IMRT, VMAT, radiocirurgia estereotáctica). O código correto depende da técnica utilizada e deve ser registrado de acordo com o planejamento de tratamento aprovado."),
    ]
)

# Article 4418 — Consulting: inovação e portfolio de produtos
art(
    slug="consultoria-de-gestao-de-inovacao-e-portfolio-de-produtos",
    title="Consultoria de Gestão de Inovação e Portfolio de Produtos",
    desc="Como estruturar uma consultoria especializada em gestão de inovação e portfolio de produtos: metodologia, clientes-alvo e posicionamento de mercado.",
    h1="Consultoria de Gestão de Inovação e Portfolio de Produtos",
    lead="Empresas que cresceram com um produto de sucesso frequentemente travam quando tentam inovar — falta processo estruturado, cultura de experimentação e governança de portfolio de inovação. Consultores especializados em inovação e gestão de portfolio ajudam organizações a criar pipelines de inovação sustentáveis e a tomar melhores decisões sobre onde investir.",
    sections=[
        ("O Problema da Inovação Nas Empresas Estabelecidas", "Empresas estabelecidas enfrentam o dilema do inovador — o modelo que as tornou bem-sucedidas cria inércia que dificulta a inovação disruptiva. Os sintomas são reconhecíveis: comitês que matam ideias antes de serem testadas, projetos de inovação que concorrem com o core business pelos mesmos recursos, falta de métricas adequadas para projetos exploratórios e cultura de aversão ao fracasso que impede experimentação genuína. O consultor de inovação traz metodologias, frameworks e experiência externa para criar as condições organizacionais que permitem inovar de forma sistemática, não episódica."),
        ("Metodologias e Frameworks de Gestão de Inovação", "O consultor de inovação deve dominar múltiplos frameworks e saber escolher o mais adequado para cada contexto: Design Thinking para ideação centrada no usuário, Lean Startup para validação acelerada de hipóteses de negócio, Jobs-to-be-Done para entendimento profundo das necessidades do cliente, Three Horizons Framework (McKinsey) para balanceamento de portfolio de inovação entre core, adjacente e transformacional, e Stage-Gate para gestão estruturada de projetos de inovação incremental. A expertise do consultor está em selecionar e adaptar frameworks ao contexto cultural e estratégico de cada cliente — não em aplicar o mesmo modelo a todos."),
        ("Governança de Portfolio de Inovação", "A governança de portfolio define como a empresa decide onde investir em inovação — quais apostas fazer, como alocar recursos entre projetos exploratórios e incrementais, e como desacelerar ou encerrar projetos que não avançam conforme esperado. Ferramentas como métricas de inovação por horizonte (MRR de novos produtos, número de experimentos ativos, taxa de kill de projetos), comitês de inovação com poder de decisão real e orçamentos protegidos de inovação (ringfenced) que não disputam com o orçamento operacional são elementos de governança que o consultor ajuda a implementar."),
        ("Cultura de Inovação e Desenvolvimento de Capacidades Internas", "A maior contribuição de um bom consultor de inovação não é o projeto que ele lidera — é a capacidade de inovar que ele desenvolve na organização. Programas de capacitação em Design Thinking, Lean Startup e experimentação rápida transformam equipes internas em agentes de inovação. Laboratórios de inovação (innovation labs) internos, programas de intraempreendedorismo (hackathons internos, bootcamps de produto) e parcerias com ecossistema externo (startups, universidades, aceleradoras) são mecanismos que o consultor ajuda a estruturar e operacionalizar."),
        ("Desenvolvimento da Prática de Consultoria de Inovação", "O consultor de inovação deve construir autoridade por meio de publicações, palestras e projetos de referência que demonstrem impacto real — não apenas frameworks bonitos. Participação em eventos de inovação corporativa (IEC, Cubo, Distrito, HSM Inovação), publicações em Harvard Business Review Brasil e MIT Sloan Management Review, e parceria com aceleradoras e fundos de venture capital consolidam a reputação. Especializar-se em setores específicos (inovação em saúde, inovação financeira, inovação industrial) permite precificação premium e acesso a cases mais relevantes para cada vertical."),
    ],
    faq_list=[
        ("Qual é a diferença entre P&D e gestão de inovação?",
         "P&D (Pesquisa & Desenvolvimento) é uma função específica focada no desenvolvimento tecnológico de produtos e processos. Gestão de inovação é mais ampla: abrange ideação, validação de mercado, desenvolvimento, escala e criação de cultura e processos organizacionais que sustentam a inovação de forma sistemática ao longo do tempo."),
        ("Como medir o ROI de investimentos em inovação?",
         "O ROI de inovação é medido em múltiplos horizontes: inovação incremental (melhoria de margens e retenção de clientes) tem ROI calculável em 12-24 meses; inovação adjacente (novos mercados) tem ROI visível em 2-5 anos; inovação transformacional (novos modelos de negócio) pode ter horizonte de 5-10 anos. Métricas intermediárias como número de experimentos ativos, taxa de progresso de estágios e percentual de receita de produtos lançados nos últimos 3 anos ajudam a avaliar a saúde do pipeline de inovação."),
        ("Como criar um laboratório de inovação corporativo que realmente funcione?",
         "Labs de inovação falham quando são decorativos — espaços físicos criativos sem mandato, orçamento ou conexão com a estratégia do negócio. Labs que funcionam têm: mandato claro do C-suite, orçamento dedicado e protegido, equipe com perfil de empreendedor (não apenas gestor), métricas de aprendizado (não apenas de resultado) e canais formais de transferência de inovações validadas para o negócio principal."),
    ]
)

# Article 4419 — B2B SaaS: gestão de propriedades e mercado imobiliário
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-propriedades-e-mercado-imobiliario",
    title="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Propriedades e Mercado Imobiliário",
    desc="Como escalar um SaaS B2B de gestão de propriedades e mercado imobiliário: imobiliárias, incorporadoras, fundos imobiliários e property managers.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Propriedades e Mercado Imobiliário",
    lead="O mercado imobiliário brasileiro movimenta trilhões em patrimônio e é gerido por dezenas de milhares de imobiliárias, administradoras de imóveis, incorporadoras e gestores de fundos imobiliários. SaaS que automatizam a gestão de contratos, locação, condomínios e transações imobiliárias têm um mercado vasto e com grande potencial de digitalização.",
    sections=[
        ("Segmentos do Mercado Imobiliário e Suas Necessidades de SaaS", "O mercado imobiliário tem vários segmentos com necessidades distintas de software: imobiliárias de locação e venda (gestão de carteira, CRM imobiliário, publicação automática em portais como ZAP e Viva Real), administradoras de condomínios (cobranças, assembleias, gestão de prestadores, aplicativo do condômino), incorporadoras (gestão de leads de pré-lançamento, contratos de compra e venda, obra e entrega), fundos imobiliários e property managers (gestão de portfólio, contratos de locação corporativa, relatórios para cotistas). Cada segmento tem compradores, fluxos de trabalho e métricas específicos que o produto de SaaS deve suportar."),
        ("Funcionalidades Core para Imobiliárias e Administradoras", "Para imobiliárias, as funcionalidades essenciais incluem: CRM para gestão de leads e clientes compradores/locatários, carteira de imóveis com portal do proprietário, integração com portais de anúncio (Viva Real, ZAP, OLX), gestão de contratos de locação com reajuste automático pelo IGPM ou IPCA, emissão de boletos de aluguel e repasse ao proprietário, e relatório de receitas por imóvel. Para administradoras de condomínios, o foco é em assembleias digitais, prestação de contas transparente ao síndico e condôminos, e gestão de manutenção preventiva e corretiva. A conformidade com a legislação de locação (Lei 8.245/91) e condomínios (Lei 4.591/64) é requisito básico."),
        ("Precificação e Modelo de Receita em PropTech SaaS", "O modelo de precificação varia por segmento: imobiliárias pagam por número de imóveis na carteira (R$ 5-20/imóvel/mês), administradoras de condomínio pagam por unidade condominial gerenciada (R$ 8-25/unidade/mês), e fundos imobiliários e property managers pagam por portfólio gerenciado. Modelos de comissão sobre transações (percentual dos aluguéis processados) são atrativos para imobiliárias em crescimento que preferem custo variável. A receita recorrente por carteira de imóveis é altamente previsível — imóveis não saem da carteira do dia para a noite e as renovações de contrato de locação são automáticas."),
        ("Go-to-Market e Canais de Distribuição no Mercado Imobiliário", "Os principais canais incluem: CRECI (Conselhos Regionais de Corretores de Imóveis), SECOVI (Sindicatos das Empresas de Compra, Venda, Locação), ABADI (Administradoras de Imóveis), feiras como EXPO REAL ESTATE e CONECTA IMOBI, e grupos de imobiliárias e síndicos nas redes sociais. Parcerias com cartórios de registro de imóveis e seguradoras (seguro-fiança, seguro de aluguel) criam distribuição cruzada e completam a proposta de valor. Plataformas de portais imobiliários (Viva Real, ZAP) são tanto parceiros de integração quanto potenciais concorrentes que vendem soluções próprias para imobiliárias."),
        ("Tendências: Proptech, Tokenização e IA no Imobiliário", "O mercado imobiliário está sendo transformado por proptech de múltiplas dimensões: IA para avaliação automatizada de imóveis (AVMs), tokenização de imóveis via blockchain para liquidez de ativos antes ilíquidos, plataformas de aluguel de curta duração (Airbnb, Booking) que exigem gestão integrada com as carteiras de locação convencional, e assinatura eletrônica de contratos que elimina a necessidade de ir ao cartório para muitas transações. SaaS que se posiciona à frente dessas tendências e integra com plataformas emergentes do ecossistema proptech consolida liderança e dificulta a substituição por soluções concorrentes."),
    ],
    faq_list=[
        ("O SaaS de gestão de locação precisa emitir boletos bancários registrados?",
         "Sim. A emissão de boletos bancários para cobrança de aluguel exige integração com bancos credenciados pelo Banco Central. A maioria dos SaaS de imobiliária integra com bancos via API (Boleto Bancário Registrado) e com meios de pagamento digitais (Pix) para facilitar o pagamento pelos locatários."),
        ("Como o SaaS pode ajudar administradoras de condomínio a realizar assembleias digitais?",
         "Módulos de assembleia digital permitem convocar condôminos por e-mail/WhatsApp, coletar procurações digitais, registrar presença e votos eletrônicos e gerar ata automaticamente. A legalidade das assembleias digitais foi consolidada pela Lei 14.010/2020 e pela reforma do Código Civil, tornando o recurso amplamente aceito."),
        ("Qual é a diferença entre CRM imobiliário e CRM genérico para imobiliárias?",
         "CRM imobiliário tem funcionalidades específicas do setor: integração com portais de anúncio, funil de vendas adaptado ao ciclo imobiliário (busca, visita, proposta, contrato, registro), histórico de imóveis visitados por cada cliente e matching automático de imóveis para perfis de compradores cadastrados. CRMs genéricos precisam ser altamente customizados para suportar esses fluxos específicos."),
    ]
)

# Article 4420 — Clinic: dermatologia adulto e cirurgia dermatológica
art(
    slug="gestao-de-clinicas-de-dermatologia-adulto-e-cirurgia-dermatologica",
    title="Gestão de Clínicas de Dermatologia Adulto e Cirurgia Dermatológica",
    desc="Guia completo de gestão para clínicas de dermatologia adulto: mix de serviços, equipe, equipamentos estéticos e sustentabilidade financeira.",
    h1="Gestão de Clínicas de Dermatologia Adulto e Cirurgia Dermatológica",
    lead="A dermatologia é uma das especialidades com maior combinação de demanda clínica e estética no Brasil. Clínicas de dermatologia adulto gerenciam desde acne e psoríase até cirurgias de Mohs e procedimentos estéticos de alto valor. A gestão eficiente dessa diversidade de serviços é um diferencial competitivo crucial.",
    sections=[
        ("Perfil de Demanda em Dermatologia Adulto no Brasil", "A dermatologia atende condições prevalentes em toda a população — acne (que afeta mais de 85% dos adolescentes e jovens adultos), dermatite atópica, psoríase, rosácea, alopecia e infecções fúngicas. Ao mesmo tempo, procedimentos estéticos dermatológicos — toxina botulínica, preenchimentos, lasers, peelings e bioestimuladores de colágeno — representam parcela crescente da receita de clínicas privadas. O câncer de pele, o mais comum no Brasil, cria demanda constante para diagnóstico (dermatoscopia, biopsia) e tratamento (excisão cirúrgica, cirurgia de Mohs para cânceres localizados em áreas críticas). Esse mix amplo de serviços torna a gestão da clínica de dermatologia ao mesmo tempo rica em oportunidades e desafiadora em precificação."),
        ("Mix de Serviços: Clínico, Cirúrgico e Estético", "A dermatologia adulto oferece três grandes pilares de serviço: clínico (consultas, diagnóstico por dermatoscopia e videodermatoscopia, tratamentos de doenças dermatológicas), cirúrgico (excisão de lesões, cirurgia de Mohs, curetagem, criocirurgia) e estético médico (toxina botulínica, preenchimentos com ácido hialurônico, lasers para rejuvenescimento e manchas, peelings, radiofrequência, microagulhamento). O mix ideal depende do posicionamento desejado — clínicas que querem manter credibilidade científica equilibram os três pilares, evitando tornar-se percebidas exclusivamente como clínicas estéticas."),
        ("Equipamentos Dermatológicos e Gestão do Parque Tecnológico", "A dermatologia é uma especialidade intensiva em equipamentos. Dermatoscópios digitais e sistemas de mapeamento corporal de nevos (como FotoFinder, MoleMax) são essenciais para diagnóstico de melanoma. Lasers para fotodepilação, rejuvenescimento (Er:YAG, CO2 fracionado), tratamento de hipercromias e vascular requerem investimentos de R$ 100 mil a R$ 500 mil por equipamento. A gestão do parque tecnológico deve incluir: planejamento de depreciação e renovação (lasers ficam obsoletos em 5-7 anos), manutenção preventiva contratada, treinamento da equipe e cálculo do break-even de cada equipamento em termos de procedimentos necessários por mês."),
        ("Precificação de Procedimentos Estéticos e Gestão Comercial", "Procedimentos estéticos não têm tabela de convênio — são 100% particulares e sujeitos a precificação de mercado. A clínica deve estabelecer tabela de preços baseada em custo de insumos (toxina, ácido hialurônico), tempo médico e de enfermagem, depreciação de equipamentos e margem desejada. Pacotes de procedimentos (ex: protocolo de 3 sessões de laser + consulta) com precificação diferenciada incentivam o comprometimento do paciente com o tratamento completo e melhoram o resultado clínico. A recepção deve ser treinada em vendas consultivas — entendendo as metas estéticas do paciente e apresentando opções de tratamento de forma adequada."),
        ("Marketing Digital e Posicionamento de Clínica de Dermatologia", "Dermatologia é uma das especialidades com maior potencial de marketing digital — Instagram e TikTok são plataformas ideais para demonstrar procedimentos, resultados antes e depois e educar o público sobre cuidados com a pele. O Conselho Federal de Medicina permite divulgação de procedimentos e resultados desde que realizada com ética e sem sensacionalismo. Conteúdo educativo sobre proteção solar, câncer de pele, cuidados com a pele em diferentes fases da vida e desmistificação de procedimentos estéticos atraem seguidores qualificados e geram agendamentos espontâneos. Parcerias com dermocosmético marcas (La Roche-Posay, Isdin, SVR) para events e samplings dentro da clínica criam experiência de valor para pacientes."),
    ],
    faq_list=[
        ("Com que frequência adultos devem fazer consulta de rotina com dermatologista?",
         "A SBD (Sociedade Brasileira de Dermatologia) recomenda consulta anual de rotina para adultos com histórico familiar de melanoma, fototipos baixos (pele clara), histórico de queimaduras solares graves ou múltiplos nevos atípicos. Para o público geral, consulta a cada 2 anos é adequada para rastreamento de câncer de pele."),
        ("Cirurgia de Mohs é coberta por convênios de saúde?",
         "Sim. A cirurgia de Mohs (cirurgia micrográfica) tem código CBHPM e é coberta pela maioria dos planos de saúde quando indicada para carcinomas basocelulares e espinocelulares em localização de alto risco (face, orelhas, lábios, genitália). A cobertura pode variar conforme o plano e deve ser verificada com a operadora previamente."),
        ("Toxina botulínica e preenchimentos são procedimentos médicos ou estéticos?",
         "São procedimentos médicos estéticos, privativos de médicos no Brasil (segundo o CFM). Podem ser realizados por dermatologistas, cirurgiões plásticos e outros especialistas habilitados. A regulamentação proíbe a realização por profissionais não médicos em procedimentos que envolvam injeção."),
    ]
)

# Article 4421 — SaaS sales: oftalmologia adulto e cirurgia refrativa
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-oftalmologia-adulto-e-cirurgia-refrativa",
    title="Vendas para o Setor de SaaS de Gestão de Clínicas de Oftalmologia Adulto e Cirurgia Refrativa",
    desc="Guia de vendas B2B para plataformas SaaS voltadas a clínicas de oftalmologia adulto, centros de cirurgia refrativa e serviços de glaucoma e retina.",
    h1="Vendas para o Setor de SaaS de Gestão de Clínicas de Oftalmologia Adulto e Cirurgia Refrativa",
    lead="Clínicas de oftalmologia adulto gerenciam fluxos elevados de consultas de rotina, procedimentos diagnósticos complexos e cirurgias refrativas e de catarata. SaaS adaptados às especificidades da especialidade — com integração a equipamentos diagnósticos e suporte ao faturamento de alto volume — têm grande oportunidade neste mercado.",
    sections=[
        ("O Mercado de Oftalmologia e Suas Especificidades", "A oftalmologia no Brasil é uma especialidade de alto volume e alto valor — o país realiza mais de 600 mil cirurgias de catarata e dezenas de milhares de cirurgias refrativas por ano. Clínicas variam de consultórios individuais de rotina a centros de excelência com múltiplos oftalmologistas subespecializados (retina, glaucoma, córnea, estrabismo, plástica ocular). O faturamento de cirurgias de catarata, a principal fonte de receita de muitos centros, é fortemente dependente de credenciamento com convênios e de gestão eficiente do processo de autorização e guia de internação — processos que SaaS bem estruturados podem automatizar e otimizar significativamente."),
        ("Funcionalidades Essenciais para Clínicas de Oftalmologia", "As funcionalidades mais valorizadas incluem: integração com equipamentos diagnósticos (tonômetro, campimetria, topografia, OCT, retinografia — exportação automática de laudos), prontuário oftalmológico com campos específicos (acuidade visual, refração, pressão intraocular, fundo de olho), agendamento com diferenciação por tipo de consulta (primeira vez, retorno, pré-operatório, pós-operatório), gestão do fluxo cirúrgico (lista de espera para cirurgia de catarata, agendamento em centro cirúrgico hospitalar, autorização de convênio), faturamento de procedimentos ambulatoriais e cirúrgicos com TUSS correto, e relatório de produção por oftalmologista e por procedimento."),
        ("Abordagem de Venda e Perfil do Decisor", "Em consultórios individuais, o próprio oftalmologista é o decisor — preocupado com facilidade de uso, custo e qualidade do suporte. Em clínicas com múltiplos médicos, há um gerente administrativo responsável pela gestão de faturamento e operações. Em centros de oftalmologia de grande porte (com 10+ médicos e cirurgias diárias), o processo de seleção envolve TI, financeiro, médico chefe e diretoria. A demonstração mais convincente mostra como o sistema automatiza a exportação de laudos do OCT e da campimetria para o prontuário, eliminando transcrição manual — este é o ponto de dor mais universal em clínicas de oftalmologia."),
        ("Integrações com Equipamentos e Ecosistema de Diagnóstico", "A integração com equipamentos de diagnóstico oftalmológico via DICOM (Digital Imaging and Communications in Medicine) e HL7 é o diferencial técnico mais valorizado. Equipamentos como o OCT (Heidelberg, Zeiss, Optovue), topógrafo corneal (Pentacam, Orbscan), campímetro (Zeiss HFA, Octopus) e retinógrafo devem exportar laudos automaticamente para o prontuário. Parcerias com fabricantes e distribuidores de equipamentos (Zeiss, Alcon, Johnson & Johnson Vision) criam oportunidade de distribuição conjunta — o SaaS integrado ao equipamento que o médico já usa é percebido como parte da solução, não como um sistema adicional."),
        ("Retenção e Expansão em Clínicas de Oftalmologia", "A retenção em SaaS de oftalmologia é facilitada pela profundidade da integração com equipamentos — migrar o sistema significa reconfigurar todas as integrações diagnósticas, um processo doloroso que os centros evitam. Módulos de expansão incluem: portal do paciente com acesso a laudos e prescrições de óculos, telemedicina para retornos de rotina, módulo de refracionamento (para integração com ótica própria ou parceira) e analytics de produtividade por médico e por equipamento. Clínicas que crescem e abrem novas unidades ou subespecialidades (retina, glaucoma) expandem naturalmente o contrato do SaaS."),
    ],
    faq_list=[
        ("O SaaS de oftalmologia precisa suportar o padrão DICOM para integração com equipamentos?",
         "Sim. DICOM é o padrão universal de imagens médicas, adotado por todos os grandes fabricantes de equipamentos oftalmológicos. Sem suporte a DICOM, o sistema não consegue importar automaticamente imagens de OCT, retinografias e topografias, o que é um deal-breaker para clínicas de médio e grande porte."),
        ("Como o SaaS pode ajudar na gestão da lista de espera para cirurgia de catarata pelo convênio?",
         "Módulos de gestão de lista de espera cirúrgica permitem registrar pacientes aguardando cirurgia, controlar o status de autorização do convênio, agendar automaticamente quando a autorização é liberada e enviar confirmação ao paciente. Esse processo, quando manual, é fonte de erros e atrasos que o SaaS elimina."),
        ("Cirurgia refrativa (LASIK) é coberta por planos de saúde?",
         "A maioria dos planos de saúde não cobre cirurgia refrativa para correção de miopia, astigmatismo e hipermetropia por considerá-la eletiva. Exceções incluem casos com alta ametropia que inviabiliza o uso de óculos ou lentes. Clínicas de cirurgia refrativa operam predominantemente no mercado particular, com financiamento próprio ou parceiros financeiros."),
    ]
)

# Article 4422 — Consulting: comunicação corporativa e gestão de crise de imagem
art(
    slug="consultoria-de-comunicacao-corporativa-e-gestao-de-crise-de-imagem",
    title="Consultoria de Comunicação Corporativa e Gestão de Crise de Imagem",
    desc="Como estruturar uma consultoria especializada em comunicação corporativa e gestão de crises de imagem: metodologia, clientes e diferenciação no mercado.",
    h1="Consultoria de Comunicação Corporativa e Gestão de Crise de Imagem",
    lead="Em um ambiente de hiperconectividade e redes sociais, crises de imagem corporativa podem emergir e escalar em horas. Empresas que não têm estratégia de comunicação estruturada e protocolo de gestão de crise ficam vulneráveis a danos reputacionais severos. Consultorias especializadas entregam tanto a prevenção quanto a resposta ágil quando a crise chega.",
    sections=[
        ("O Ambiente de Risco Reputacional no Brasil Digital", "Redes sociais, jornalismo investigativo digital e o ativismo de consumidores transformaram o ambiente de risco reputacional das empresas brasileiras. Uma reclamação viral no Twitter/X, um vídeo denunciando má conduta no TikTok, uma matéria investigativa no Reclame Aqui ou no Procon podem alcançar milhões de pessoas em horas — antes de a empresa ter tempo de preparar uma resposta estruturada. Setores como alimentação, aviação, bancos, saúde e varejo são especialmente suscetíveis a crises reputacionais pela natureza sensível dos produtos e serviços que oferecem e pelo alto volume de interações públicas diárias com consumidores."),
        ("Estrutura de Comunicação Corporativa Preventiva", "A melhor gestão de crise é a que evita a crise. A consultoria de comunicação corporativa preventiva inclui: diagnóstico de vulnerabilidades reputacionais (quais riscos a empresa enfrenta e o quanto está preparada para cada um), construção de narrativa corporativa (propósito, valores e posicionamento que orientam toda a comunicação), estruturação de canais de comunicação com stakeholders (investidores, colaboradores, clientes, imprensa, reguladores), treinamento de porta-vozes (media training) e criação de manual de crise com protocolos claros por tipo de ocorrência. Empresas com estrutura preventiva respondem a crises de forma mais controlada e saem delas com danos menores."),
        ("Gestão de Crise: Protocolo e Resposta Ágil", "Quando a crise acontece, os primeiros 60 a 120 minutos são decisivos. O protocolo de gestão de crise deve definir: quem decide (comitê de crise com C-suite, jurídico, comunicação e operações), como é avaliada a gravidade e o potencial de escalada, qual é a primeira declaração pública (geralmente uma nota de reconhecimento que evita o vácuo comunicativo), quais canais são ativados (site, redes sociais, assessoria de imprensa, comunicado interno) e como o monitoramento da crise é conduzido em tempo real. A consultoria gerencia o processo ao lado do cliente, sem substituí-lo — a liderança da empresa deve ser visible na crise."),
        ("Comunicação de Crise nas Redes Sociais", "Redes sociais exigem comunicação em tempo real — o silêncio é interpretado como confirmação ou indiferença. A estratégia nas redes durante uma crise inclui: resposta pública inicial rápida (menos de 2 horas), tom empático e responsável (sem defensividade ou atribuição de culpa a terceiros), atualização regular do público com informações concretas sobre as ações tomadas, e gestão de comentários negativos (moderação dentro dos limites legais, sem apagamento de críticas legítimas que amplificam a percepção de censura). Monitoramento de redes com ferramentas como Sprinklr, Hootsuite e Mention permite acompanhar o sentimento e a propagação em tempo real."),
        ("Construção e Diferenciação da Consultoria de Comunicação", "Consultorias de comunicação corporativa e crise se diferenciam por: portfólio de cases gerenciados (com discretion mas com resultados mensuráveis), rede de contatos na imprensa e em órgãos regulatórios, capacidade de operar 24/7 em situações de emergência e expertise setorial (saúde, financeiro, varejo, tecnologia têm dinâmicas de crise muito específicas). A especialização em comunicação para empresas de capital aberto (relações com investidores), comunicação ambiental/ESG e comunicação para o setor de saúde são nichos premium com demanda crescente e menor competição de consultorias generalistas."),
    ],
    faq_list=[
        ("Qual é o erro mais comum que empresas cometem durante uma crise de imagem?",
         "O silêncio ou a demora excessiva na resposta é o erro mais comum — e o mais prejudicial. Em um ambiente digital, cada hora de silêncio é interpretada como confirmação do problema ou indiferença. Emitir uma nota inicial rápida, mesmo sem todas as informações, demonstra responsabilidade e compra tempo para uma resposta mais completa."),
        ("Gestão de crise é diferente de assessoria de imprensa?",
         "Assessoria de imprensa é uma função permanente de relacionamento com veículos de comunicação e produção de conteúdo proativo. Gestão de crise é uma atividade reativa e temporária, ativada quando um evento ameaça a reputação da empresa. Na prática, a gestão de crise envolve comunicação com a imprensa, mas também com colaboradores, investidores, reguladores e o público em geral."),
        ("Como mensurar o impacto de uma crise de imagem e a eficácia da resposta?",
         "Métricas incluem: volume e sentimento de menções nas redes sociais antes e durante a crise, share of voice negativo vs. positivo, evolução do NPS durante e após a crise, retenção de clientes no período, impacto no share price (para empresas abertas) e tempo de normalização do volume de buscas negativas relacionadas à marca."),
    ]
)

# ── Sitemap + trilha ──────────────────────────────────────────────────────────
root = pathlib.Path(__file__).parent
slugs = [
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-obras-e-construcao-civil",
     "Gestão de Negócios de Empresa de B2B SaaS de Gestão de Obras e Construção Civil"),
    ("gestao-de-clinicas-de-endocrinologia-adulto-e-tireoide",
     "Gestão de Clínicas de Endocrinologia Adulto e Tireoide"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-centros-de-radioterapia-e-oncologia-radioterapeuta",
     "Vendas para o Setor de SaaS de Gestão de Centros de Radioterapia e Oncologia Radioterapeuta"),
    ("consultoria-de-gestao-de-inovacao-e-portfolio-de-produtos",
     "Consultoria de Gestão de Inovação e Portfolio de Produtos"),
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-propriedades-e-mercado-imobiliario",
     "Gestão de Negócios de Empresa de B2B SaaS de Gestão de Propriedades e Mercado Imobiliário"),
    ("gestao-de-clinicas-de-dermatologia-adulto-e-cirurgia-dermatologica",
     "Gestão de Clínicas de Dermatologia Adulto e Cirurgia Dermatológica"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-oftalmologia-adulto-e-cirurgia-refrativa",
     "Vendas para o Setor de SaaS de Gestão de Clínicas de Oftalmologia Adulto e Cirurgia Refrativa"),
    ("consultoria-de-comunicacao-corporativa-e-gestao-de-crise-de-imagem",
     "Consultoria de Comunicação Corporativa e Gestão de Crise de Imagem"),
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

print("Done — batch 1466")
