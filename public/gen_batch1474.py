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


# Article 4431 — B2B SaaS: plataforma de dados e data governance
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-plataforma-de-dados-e-data-governance",
    title="Gestão de Negócios de Empresa de B2B SaaS de Plataforma de Dados e Data Governance",
    desc="Como escalar um SaaS B2B de plataforma de dados e data governance: mercado, modelo de negócio, diferenciação técnica e estratégia de vendas.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Plataforma de Dados e Data Governance",
    lead="Com a explosão de dados gerados pelas empresas, a capacidade de gerenciar, governar e extrair valor dos dados tornou-se uma vantagem competitiva crítica. SaaS de plataforma de dados e data governance atendem desde a coleta e integração até a catalogação, qualidade e governança de dados — um mercado em crescimento acelerado no Brasil.",
    sections=[
        ("O Mercado de Data Management e Governance no Brasil", "A LGPD criou urgência nas empresas brasileiras para mapear, catalogar e governar seus dados pessoais — e esse movimento de conformidade abriu as portas para uma agenda mais ampla de data governance. Além da conformidade, empresas que querem ser data-driven precisam de fundações sólidas: dados confiáveis, integrados e com linhagem clara. O mercado de SaaS de dados no Brasil cresce em linha com a adoção de cloud computing — AWS, Azure e GCP estão presentes em mais empresas, criando infraestrutura sobre a qual plataformas de dados SaaS operam. Os principais segmentos compradores incluem serviços financeiros, varejo com omnichannel, indústria e healthtechs com dados clínicos."),
        ("Categorias de Produto no Ecossistema de Dados", "O ecossistema de data management é amplo e inclui: plataformas de integração de dados (ETL/ELT — Airbyte, Fivetran equivalentes), data warehouses e lakehouses (Snowflake, Databricks equivalentes), catálogos de dados e ferramentas de data discovery (DataHub, Alation equivalentes), ferramentas de qualidade de dados (Great Expectations, Monte Carlo equivalentes), plataformas de data governance (Collibra, Atlan equivalentes), e plataformas de observabilidade de dados. SaaS brasileiros competem em nichos específicos — customização para requisitos locais, suporte em português, integração com sistemas brasileiros (TOTVS, VTEX, SAP) e conformidade com LGPD são diferenciais relevantes."),
        ("Modelo de Negócio e Estratégia de Pricing", "Plataformas de dados B2B geralmente adotam pricing baseado em volume de dados processados, número de fontes de dados conectadas, ou número de usuários ativos. Modelos de marketplace (o cliente paga pelo uso de conectores específicos) são comuns em plataformas de integração. Para data governance, o pricing costuma ser por número de ativos de dados catalogados ou por usuário com acesso ao catálogo. O segmento enterprise tem disposição a pagar elevada — CIOs e Chief Data Officers reconhecem o custo da má governança de dados (erros de decisão, multas regulatórias, incidentes de segurança) e investem em soluções robustas."),
        ("Vendas Técnicas e o Papel do Data Engineer", "A venda de plataformas de dados é eminentemente técnica — o comprador inicial é frequentemente um data engineer, data architect ou Head of Data Engineering. Estratégias de PLG (Product-Led Growth) são muito eficazes: documentação técnica de alta qualidade, SDKs e CLIs bem construídos, plano gratuito com limite de fontes ou volume de dados, e comunidade ativa de usuários técnicos (Discord, Stack Overflow). O caminho de expansão é o crescimento orgânico dentro da empresa — um time começa a usar, outros times adotam, a plataforma se torna infraestrutura crítica e o contrato enterprise é formalizado."),
        ("Data Governance e LGPD: O Argumento Regulatório", "A LGPD (Lei Geral de Proteção de Dados) impõe obrigações de mapeamento de dados pessoais, registro de atividades de tratamento, gestão de consentimentos e resposta a solicitações de titulares. Plataformas de data governance que suportam a criação de inventário de dados pessoais, mapeamento de fluxo de dados (linhagem), controle de acesso por finalidade e relatórios de conformidade para a ANPD têm o argumento regulatório como acelerador de vendas. O DPO (Data Protection Officer) tornou-se um stakeholder relevante no processo de compra de plataformas de dados — frequentemente aliado à venda por ter interesse direto na conformidade que a plataforma proporciona."),
    ],
    faq_list=[
        ("O que é data lineage e por que é importante para data governance?",
         "Data lineage é o rastreamento de como os dados se movem e transformam ao longo de seus ciclos de vida — da origem (banco de dados transacional, API) até o destino (dashboard, relatório, modelo de IA). É fundamental para data governance porque permite entender o impacto de mudanças em dados upstream, identificar a origem de problemas de qualidade e demonstrar conformidade com regulações de rastreabilidade de dados pessoais."),
        ("Qual é a diferença entre data warehouse e data lakehouse?",
         "Data warehouse é otimizado para dados estruturados e consultas analíticas — ideal para relatórios e BI. Data lakehouse combina a flexibilidade do data lake (dados estruturados, semiestruturados e não estruturados) com as capacidades analíticas do data warehouse. Tecnologias como Delta Lake e Apache Iceberg habilitam o conceito de lakehouse sobre cloud storage de baixo custo."),
        ("LGPD exige uma ferramenta de data governance específica?",
         "A LGPD não especifica ferramentas, mas exige capacidades que plataformas de data governance suportam: registro de atividades de tratamento (Art. 37), resposta a solicitações de titulares (acesso, correção, exclusão — Art. 18) e relatório de impacto à proteção de dados (RIPD — Art. 38). Uma planilha pode atender o básico, mas ferramentas de data governance escalam melhor conforme o volume de dados e a complexidade do negócio crescem."),
    ]
)

# Article 4432 — Clinic: nefrologia adulto e hipertensão renal
art(
    slug="gestao-de-clinicas-de-nefrologia-adulto-e-hipertensao-renal",
    title="Gestão de Clínicas de Nefrologia Adulto e Hipertensão Renal",
    desc="Guia de gestão para clínicas de nefrologia adulto: doença renal crônica, hipertensão arterial sistêmica, diálise e transplante renal.",
    h1="Gestão de Clínicas de Nefrologia Adulto e Hipertensão Renal",
    lead="A nefrologia adulto atende pacientes com doenças renais crônicas — frequentemente decorrentes de diabetes e hipertensão —, hipertensão arterial de difícil controle, glomerulonefrites e doenças renais hereditárias. A gestão dessas clínicas exige equipe especializada, infraestrutura diagnóstica renal e articulação com serviços de diálise e transplante.",
    sections=[
        ("Epidemiologia e Demanda em Nefrologia no Brasil", "A Doença Renal Crônica (DRC) afeta mais de 10% da população adulta brasileira, com a maioria dos casos relacionados à diabetes e hipertensão — as duas doenças crônicas mais prevalentes no país. O diagnóstico precoce da DRC é crítico para retardar a progressão para diálise, mas a maioria dos casos é identificada tardiamente. O Brasil tem mais de 145 mil pacientes em diálise e a incidência cresce anualmente. A hipertensão arterial sistêmica afeta mais de 30% da população adulta e é a causa mais comum de encaminhamento ao nefrologista para investigação de hipertensão resistente ou acompanhamento de lesão de órgão-alvo renal."),
        ("Mix de Serviços em Clínicas de Nefrologia", "Uma clínica de nefrologia adulto completa oferece: consultório com avaliação nefrológica (estimativa de TFG, relação proteína/creatinina urinária, análise do sedimento urinário), controle de hipertensão com mapeamento pressórico (MAPA 24h), biópsia renal percutânea (com suporte de ultrassonografia ou tomografia), programa de nefrologia preventiva para pacientes de risco (diabéticos, hipertensos), acompanhamento de pré-diálise e planejamento de acesso vascular (fístula arteriovenosa), e parceria com centros de diálise e programas de transplante renal para os casos que evoluem para doença renal terminal."),
        ("Gestão do Paciente com DRC: Acompanhamento Longitudinal", "Pacientes com DRC em estágios 3-5 requerem acompanhamento frequente e altamente personalizado: controle rigoroso da pressão arterial (meta abaixo de 130/80 mmHg para diabéticos), tratamento da proteinúria (inibidores de ECA, ARA-II, SGLT-2 inibidores), manejo das complicações da DRC (anemia, doença óssea metabólica, acidose metabólica, distúrbios eletrolíticos) e dieta específica com restrição de potássio, fósforo e sódio com apoio de nutricionista renal. Prontuários eletrônicos que monitoram graficamente a evolução da TFG ao longo do tempo e alertam para piora são ferramentas valiosas no acompanhamento desses pacientes."),
        ("Hipertensão Arterial Resistente e Nefrologista como Especialista Referência", "A hipertensão arterial resistente — definida como pressão arterial não controlada com 3 ou mais anti-hipertensivos em doses máximas toleradas, incluindo diurético — é uma das principais razões de encaminhamento ao nefrologista. O nefrologista avalia causas secundárias de hipertensão (estenose de artéria renal, doença parenquimatosa renal, hiperaldosteronismo, feocromocitoma), otimiza a terapia anti-hipertensiva com atenção à função renal e, nos casos refratários, pode indicar procedimentos intervencionistas como a denervação simpática renal. Ser reconhecido como referência regional em hipertensão arterial resistente é uma estratégia de diferenciação para clínicas de nefrologia."),
        ("Sustentabilidade Financeira e Parcerias Estratégicas", "Clínicas de nefrologia têm boa base de receita recorrente — consultas frequentes de pacientes crônicos e procedimentos como biópsias renais e MAPA. A parceria com centros de hemodiálise e diálise peritoneal é fundamental — o nefrologista da clínica pode atuar como médico assistente dos pacientes da clínica que evoluem para diálise, mantendo o vínculo longitudinal e gerando receita pelo acompanhamento em diálise. Parcerias com hospitais para internação de crises renais agudas, síndrome nefrótica grave ou pré-operatório de transplante complementam o leque de serviços e fortalecem o posicionamento da clínica como referência renal regional."),
    ],
    faq_list=[
        ("Com que frequência pacientes com DRC devem consultar o nefrologista?",
         "A frequência depende do estágio da DRC: estágio 3 (TFG 30-59 ml/min) — consulta a cada 6 meses; estágio 4 (TFG 15-29) — a cada 3 meses; estágio 5 pré-diálise — mensalmente para planejamento do acesso vascular e escolha da modalidade de diálise. Em casos de descompensação aguda, a frequência é intensificada conforme a necessidade clínica."),
        ("O que é TFG e como é calculada?",
         "TFG (Taxa de Filtração Glomerular) estima a capacidade dos rins de filtrar o sangue. É calculada a partir da creatinina sérica, idade, sexo e raça usando equações como a CKD-EPI. Valores acima de 90 ml/min/1,73m² são considerados normais; abaixo de 60 ml/min por mais de 3 meses define DRC; abaixo de 15 ml/min indica necessidade de terapia renal substitutiva (diálise ou transplante)."),
        ("Qual a diferença entre hemodiálise e diálise peritoneal?",
         "Na hemodiálise, o sangue é filtrado externamente por uma máquina (rim artificial) 3 vezes por semana em sessões de 4 horas. Na diálise peritoneal, a filtração ocorre dentro do próprio abdome usando o peritônio como membrana filtrante, podendo ser realizada em casa. A escolha depende de fatores clínicos, estilo de vida e preferência do paciente — o nefrologista orienta essa decisão no planejamento pré-diálise."),
    ]
)

# Article 4433 — SaaS sales: medicina preventiva e check-up
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-centros-de-medicina-preventiva-e-check-up",
    title="Vendas para o Setor de SaaS de Gestão de Centros de Medicina Preventiva e Check-up",
    desc="Estratégias de vendas B2B para plataformas SaaS voltadas a centros de medicina preventiva, check-up executivo e programas de saúde corporativa.",
    h1="Vendas para o Setor de SaaS de Gestão de Centros de Medicina Preventiva e Check-up",
    lead="Centros de medicina preventiva e check-up executivo gerenciam pacientes que buscam rastreamento de doenças, avaliação de risco cardiovascular e monitoramento de saúde periódico. SaaS que automatizam o fluxo de check-up — da convocação ao relatório final integrado — têm demanda crescente nesse mercado de alto valor percebido.",
    sections=[
        ("O Mercado de Medicina Preventiva e Check-up no Brasil", "O check-up executivo e os programas de medicina preventiva crescem no Brasil impulsionados pelo mercado corporativo — empresas investindo em saúde dos colaboradores como estratégia de produtividade e retenção — e pelo crescimento da classe média que valoriza cuidados preventivos. Centros de check-up de alto padrão oferecem pacotes personalizados por faixa etária, sexo e fatores de risco, realizando exames laboratoriais extensos, avaliações de imagem (ecocardiograma, mamografia, colonoscopia), consultas com múltiplos especialistas e entrega de relatório médico integrado. O ticket médio de um check-up completo varia de R$ 2 mil a R$ 20 mil, dependendo da abrangência e do nível de personalização."),
        ("Necessidades Específicas de Gestão em Centros de Check-up", "O fluxo operacional de um centro de check-up é complexo: agendamento de múltiplos exames e consultas em um único dia ou em uma sequência otimizada, convocação automática de pacientes para check-ups periódicos, coordenação de diferentes especialistas e técnicos de exame na mesma visita, importação de resultados de laboratório e imagem no prontuário de forma centralizada, e geração do relatório médico integrado com recomendações individualizadas. SaaS que automatizam esse fluxo — especialmente a convocação periódica e a integração de resultados — entregam valor imediato e mensurável em eficiência operacional."),
        ("Proposta de Valor para Centros de Medicina Preventiva", "Os argumentos centrais de venda incluem: redução do tempo de geração do relatório integrado de check-up (de horas para minutos com consolidação automática de resultados), convocação automática de pacientes com base no protocolo de periodicidade (anual, bianual) sem depender de planilha manual, gestão de programas corporativos (controle de qual colaborador de cada empresa realizou o check-up, relatório agregado de saúde da população para o RH sem exposição de dados individuais), e portal do paciente para acesso digital ao relatório e histórico de exames ao longo dos anos."),
        ("Canais de Venda e Parcerias com Empresas Clientes", "Os canais mais eficazes incluem: operadoras de saúde que financiam check-up para clientes de planos premium, corretoras de benefícios que acessam RHs corporativos, associações de medicina do trabalho (ANAMT), eventos de saúde corporativa e grupos de gestores de RH. A venda B2B para empresas que contratam pacotes de check-up para executivos é o principal motor de crescimento dos grandes centros de medicina preventiva — contratos anuais com 50, 100 ou 500 check-ups garantem receita previsível e justificam investimento em SaaS de gestão especializado."),
        ("Retenção e Expansão em Centros de Check-up", "A retenção é naturalmente elevada porque o histórico comparativo de check-ups ao longo dos anos é o principal diferencial do serviço — ninguém muda de centro de saúde quando tem anos de exames consolidados em um único sistema. Módulos de expansão incluem: telemedicina para devolutiva do relatório de check-up (especialmente para clientes corporativos de outras cidades), wellness coaching integrado (nutricionista, psicólogo, educador físico para implementar as recomendações do relatório), e integração com wearables para monitoramento contínuo entre check-ups. A análise de tendências de saúde da população ao longo do tempo é uma funcionalidade de alto valor percebido para programas corporativos de saúde."),
    ],
    faq_list=[
        ("Com que frequência é recomendado fazer um check-up médico completo?",
         "A frequência depende da idade e dos fatores de risco. Em geral, um check-up completo é recomendado anualmente para adultos acima de 40 anos, a cada 2 anos para adultos entre 20 e 40 anos sem fatores de risco, e com maior frequência para pessoas com hipertensão, diabetes, histórico familiar de doença cardiovascular ou oncológica."),
        ("O SaaS de check-up pode integrar com laboratórios e clínicas de imagem externas?",
         "Sim. A integração com laboratórios via HL7/FHIR para importação automática de resultados e com clínicas de imagem via DICOM para laudos de ecocardiograma, mamografia e tomografia é uma das funcionalidades mais valorizadas — elimina a digitação manual de resultados e reduz erros no relatório integrado."),
        ("Como o SaaS ajuda centros de check-up a gerenciar programas corporativos?",
         "Por meio de dashboards que mostram quais colaboradores de cada empresa realizaram o check-up no período (sem expor dados individuais), alertas automáticos para gestores de RH sobre colaboradores com exames pendentes, e relatórios agregados de saúde populacional que o RH usa para planejar programas de saúde e avaliar o ROI do investimento em medicina preventiva."),
    ]
)

# Article 4434 — Consulting: gestão de processos de negócios e BPM
art(
    slug="consultoria-de-gestao-de-processos-de-negocios-e-bpm",
    title="Consultoria de Gestão de Processos de Negócios e BPM",
    desc="Como estruturar e desenvolver uma consultoria especializada em BPM (Business Process Management) e gestão de processos de negócios no Brasil.",
    h1="Consultoria de Gestão de Processos de Negócios e BPM",
    lead="Processos mal definidos, repletos de retrabalho e gargalos, custam às empresas brasileiras bilhões em ineficiência anualmente. Consultorias especializadas em BPM ajudam organizações a mapear, otimizar, automatizar e monitorar seus processos de negócio, criando bases sólidas para a excelência operacional e a transformação digital.",
    sections=[
        ("O Que é BPM e Por Que Importa para as Empresas", "BPM (Business Process Management) é uma disciplina de gestão que trata os processos de negócio como ativos organizacionais — a serem mapeados, documentados, otimizados e monitorados continuamente. Ao contrário da automação pontual de tarefas, o BPM olha para o processo como um todo: do gatilho (evento que inicia o processo) ao resultado esperado (entrega de valor ao cliente interno ou externo). Empresas que adotam BPM sistematicamente reduzem o tempo de ciclo de processos críticos, eliminam retrabalho e handoffs desnecessários, e criam base documentada que facilita a automação com tecnologia (RPA, IA, sistemas ERP)."),
        ("Mapeamento de Processos: Ferramentas e Abordagens", "O mapeamento de processos utiliza notações padronizadas — BPMN 2.0 (Business Process Model and Notation) é o padrão internacional mais adotado, mas fluxogramas e swimlane diagrams são adequados para processos mais simples. Ferramentas de modelagem incluem Bizagi, ARIS, Signavio (SAP), Camunda e draw.io para projetos menores. O mapeamento deve capturar não apenas o fluxo ideal (AS-SHOULD) mas o processo real, com suas variações, exceções e pontos de falha (AS-IS). A análise do AS-IS com dados reais (tempos de ciclo, taxas de erro, volume por caminho do processo) fornece evidências objetivas das oportunidades de melhoria."),
        ("Redesenho e Otimização de Processos", "O redesenho de processos (TO-BE) elimina as ineficiências identificadas no AS-IS: retrabalho (executar a mesma etapa mais de uma vez), espera (tempo sem agregação de valor entre etapas), movimentação desnecessária de informação (handoffs manuais que poderiam ser automatizados), sobre-processamento (verificações e aprovações além do necessário) e erros evitáveis (pela falta de padronização). A metodologia Lean é frequentemente integrada ao BPM para estruturar a eliminação de desperdícios. O redesenho deve ser validado com os executores do processo antes de ser implementado — quem faz o processo sabe de nuances que o mapeador de fora não capta facilmente."),
        ("Automação de Processos: RPA, BPMS e Low-Code", "BPM e automação são complementares. Após mapear e otimizar, a automação torna os processos mais rápidos e menos dependentes de execução manual. Ferramentas de automação incluem: BPMS (Business Process Management Systems — plataformas que executam processos modelados em BPMN, como Camunda, Flowable, Appian), RPA (Robotic Process Automation — automação de tarefas repetitivas em sistemas sem API, como Blue Prism, UiPath, Automation Anywhere) e plataformas low-code/no-code (que permitem criar fluxos de trabalho sem programação, como Power Automate, Kissflow, Pipefy). O consultor de BPM deve entender o escopo de cada tecnologia para indicar a mais adequada para cada processo."),
        ("Desenvolvimento da Prática e Certificações Relevantes", "Consultores de BPM se certificam pelo ABPMP (Association of Business Process Management Professionals) — a certificação CBPP (Certified Business Process Professional) é o padrão de referência da área. No Brasil, o BPM CBOK (Common Body of Knowledge do BPM) é a referência bibliográfica central. Participação em eventos da ABPMP Brasil, parceria com fornecedores de plataformas BPMS e especialização setorial (BPM para saúde, para serviços financeiros, para setor público) diferenciam o consultor e permitem desenvolvimento de verticais de alto valor."),
    ],
    faq_list=[
        ("Qual é a diferença entre BPM e automação de processos (RPA)?",
         "BPM é uma disciplina de gestão que mapeia, otimiza e governa processos de negócio. RPA é uma tecnologia que automatiza tarefas repetitivas. O BPM bem feito precede a automação — não adianta automatizar um processo ineficiente. BPM define O QUE automatizar e COMO o processo deve fluir; RPA e BPMS implementam A AUTOMAÇÃO do processo otimizado."),
        ("O que é BPMN e para que serve?",
         "BPMN (Business Process Model and Notation) é um padrão gráfico internacional para modelagem de processos de negócio. Usa símbolos padronizados (eventos, atividades, gateways, fluxos) que podem ser compreendidos tanto por profissionais de negócio quanto por desenvolvedores de TI. É a linguagem universal do BPM e é suportada pela maioria das ferramentas de modelagem e execução de processos."),
        ("Quanto tempo leva um projeto de BPM em uma empresa de médio porte?",
         "Projetos de mapeamento e otimização de um processo crítico levam de 6 a 12 semanas. Um programa de BPM corporativo — cobrindo os processos mais relevantes da empresa — pode durar de 6 a 18 meses, dependendo da abrangência e da velocidade de implementação das melhorias. A manutenção e melhoria contínua dos processos é um trabalho permanente."),
    ]
)

# Article 4435 — B2B SaaS: gestão de contratos e procurement
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-contratos-e-procurement",
    title="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Contratos e Procurement",
    desc="Como escalar um SaaS B2B de gestão de contratos e procurement: CLM (Contract Lifecycle Management), automação de compras e integração com ERPs.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Contratos e Procurement",
    lead="A gestão de contratos e procurement é um dos processos mais críticos e menos digitalizados nas empresas brasileiras. SaaS de CLM (Contract Lifecycle Management) e procurement digital substituem planilhas e e-mails por fluxos automatizados de aprovação, rastreamento de obrigações contratuais e controle de fornecedores — entregando governança e redução de riscos.",
    sections=[
        ("O Problema da Gestão Manual de Contratos e Compras", "Empresas brasileiras de médio porte gerenciam tipicamente centenas a milhares de contratos simultâneos — locação, fornecimento, prestação de serviço, parceria, software, trabalhistas — sem sistema centralizado. O resultado é: contratos esquecidos com renovação automática indesejada, vencimentos de garantias e SLAs não monitorados, compras emergenciais sem cotação adequada por falta de planejamento e fornecedores duplicados ou não qualificados. O custo dessa desorganização é alto: multas contratuais, pagamentos indevidos, perda de prazos e riscos de compliance. A digitalização desses processos via SaaS tem ROI imediato e mensurável."),
        ("CLM: Funcionalidades e Ciclo de Vida do Contrato", "Uma plataforma de CLM (Contract Lifecycle Management) cobre todo o ciclo do contrato: criação (templates pré-aprovados, editor de cláusulas com banco de termos padronizados), negociação (controle de versões, comentários e aprovações por partes), assinatura eletrônica (integrada, com ICP-Brasil quando necessário), armazenamento centralizado (repositório com busca por texto, partes, valor, data), alertas automáticos de vencimento e renovação, monitoramento de obrigações contratuais (SLAs, entregas, pagamentos) e relatórios de portfólio contratual para o jurídico, financeiro e compliance."),
        ("Procurement Digital: Automação de Compras e Gestão de Fornecedores", "A digitalização do procurement vai além do contrato — inclui o processo de compra completo: requisição de compra, cotação com múltiplos fornecedores (RFQ automatizado), comparativo de propostas, aprovação por alçada (compras acima de X reais precisam de aprovação do gerente; acima de Y, da diretoria), emissão de pedido de compra, recebimento e confirmação de entrega, e integração com o faturamento (nota fiscal recebida). Plataformas de procurement integradas com ERP (SAP, TOTVS, Oracle) eliminam a duplicidade de lançamento de dados e criam visibilidade em tempo real do comprometimento orçamentário de compras."),
        ("Modelo de Negócio e Estratégia de Vendas Enterprise", "Plataformas de CLM e procurement atendem um mercado amplo — de PMEs (onde o diferencial é a simplicidade e o custo) a enterprises (onde o diferencial é a robustez da integração com ERP e a segurança jurídica). A precificação típica é por usuário por mês ou por volume de contratos ativos. O ciclo de vendas em enterprises envolve jurídico, compras/procurement, financeiro e TI. A entrada mais eficaz é pelo gerente jurídico ou pelo CFO — ambos sentem diretamente o risco da gestão manual de contratos e têm autoridade ou influência para aprovar a compra do sistema."),
        ("Integração com Assinatura Eletrônica e Conformidade Legal", "A assinatura eletrônica é funcionalidade central de qualquer plataforma de contratos moderna. No Brasil, a MP 2.200-2/2001 e a Lei 14.063/2020 regulamentam as assinaturas eletrônicas — incluindo assinatura eletrônica simples (e-mail, SMS), avançada (com certificado digital não ICP-Brasil) e qualificada (ICP-Brasil). A plataforma de CLM deve oferecer múltiplos níveis de assinatura conforme o risco e o valor do contrato. Integrações com provedores de assinatura eletrônica reconhecidos (DocuSign, Clicksign, D4Sign, Autentique) são um caminho mais ágil do que desenvolver assinatura própria."),
    ],
    faq_list=[
        ("CLM e ERP são substituídos um pelo outro ou complementares?",
         "São complementares. ERPs gerenciam a execução financeira e operacional dos contratos (pagamentos, notas fiscais, pedidos). CLM gerencia o ciclo de vida jurídico-contratual — texto, cláusulas, obrigações, vencimentos. A integração entre CLM e ERP cria o fluxo completo: contrato assinado no CLM → pedido de compra gerado automaticamente no ERP → pagamento executado → confirmação registrada no CLM."),
        ("Assinatura eletrônica tem validade jurídica no Brasil para todos os tipos de contrato?",
         "Para a maioria dos contratos comerciais privados, sim — a assinatura eletrônica é válida desde que a identidade das partes seja verificável e o conteúdo do documento seja íntegro. Exceções incluem contratos que legalmente exigem escritura pública (imóveis, por exemplo) ou assinatura com testemunhas presenciais. Para dúvidas sobre casos específicos, a consulta ao jurídico é recomendada."),
        ("Como a plataforma de CLM pode ajudar a evitar renovações automáticas indesejadas?",
         "Alertas configuráveis de vencimento (90, 60, 30 dias antes do vencimento) notificam os responsáveis com antecedência suficiente para tomar uma decisão consciente sobre renovação ou encerramento. O dashboard de contratos com vencimento próximo dá visibilidade ao jurídico e ao financeiro sobre o portfólio contratual e evita surpresas de renovação automática não planejada."),
    ]
)

# Article 4436 — Clinic: medicina hiperbárica e feridas complexas
art(
    slug="gestao-de-clinicas-de-medicina-hiperbarica-e-tratamento-de-feridas-complexas",
    title="Gestão de Clínicas de Medicina Hiperbárica e Tratamento de Feridas Complexas",
    desc="Guia de gestão para clínicas de medicina hiperbárica, curativos avançados e tratamento especializado de feridas crônicas e complexas.",
    h1="Gestão de Clínicas de Medicina Hiperbárica e Tratamento de Feridas Complexas",
    lead="Centros de medicina hiperbárica e tratamento de feridas complexas atendem pacientes com úlceras diabéticas, lesões por pressão, pé diabético com risco de amputação, osteomielite crônica e lesões por radiação. São serviços de alta especialização técnica e impacto clínico direto na prevenção de amputações e na melhoria da qualidade de vida de pacientes com doenças crônicas.",
    sections=[
        ("O Mercado de Medicina Hiperbárica e Tratamento de Feridas no Brasil", "O Brasil tem mais de 16 milhões de diabéticos, e o pé diabético é a principal causa de amputação de membros inferiores no país — responsável por mais de 70 mil amputações anuais, a maioria evitável com tratamento especializado precoce. Além das feridas diabéticas, centros de tratamento de feridas atendem lesões por pressão (escaras) em pacientes acamados, úlceras venosas crônicas, feridas pós-radioterapia e osteomielite crônica. A medicina hiperbárica — oxigenoterapia hiperbárica (OHB) — é um recurso terapêutico adjuvante com indicações formais para pé diabético isquêmico, osteomielite refratária, lesões por radiação e intoxicação por monóxido de carbono."),
        ("Estrutura de um Centro de Medicina Hiperbárica", "A câmara hiperbárica é o equipamento central — disponível em modelos monopessoais (um paciente por sessão, mais acessíveis) e multipessoais (vários pacientes simultâneos, maior custo mas maior capacidade). A pressão usada nas sessões de OHB (tipicamente 2 a 3 ATA, com oxigênio 100%) exige câmaras certificadas pela ANVISA e manutenção rigorosa por técnicos especializados. Além da câmara, o centro deve ter: consultório médico para avaliação e indicação de OHB, sala de curativos com materiais avançados (coberturas de prata, NPWT — curativo a vácuo, substitutos dérmicos), e idealmente um laboratório de microbiologia próximo para culturas de feridas."),
        ("Equipe Multidisciplinar e Protocolos de Tratamento de Feridas", "O tratamento de feridas complexas é eminentemente multidisciplinar. A equipe ideal inclui médico especialista em medicina hiperbárica (com certificação pela SBMH — Sociedade Brasileira de Medicina Hiperbárica), enfermeiro especializado em estomaterapia (SEET — especialidade de enfermagem em feridas, estomias e incontinências), nutricionista (a nutrição é fundamental para a cicatrização — controle glicêmico, proteínas, zinco, vitamina C), fisioterapeuta (mobilização, tratamento de linfedema) e podólogo em centros que atendem pé diabético. Protocolos de avaliação inicial (índice tornozelo-braquial, cultura de ferida, estadiamento da lesão) e de seguimento garantem a qualidade e rastreabilidade do tratamento."),
        ("Fluxo de Pacientes e Gestão da Câmara Hiperbárica", "A gestão da câmara hiperbárica requer planejamento cuidadoso — as sessões de OHB duram de 60 a 90 minutos, com protocolo de pressurização e despressurização. O número de sessões por protocolo varia (20 a 40 sessões em dias consecutivos para pé diabético, por exemplo). A gestão da agenda da câmara deve otimizar a ocupação (pelo menos 80% de utilização para viabilidade financeira) e garantir a seleção rigorosa de pacientes elegíveis (contraindicações para OHB devem ser verificadas antes de iniciar o tratamento). A equipe de suporte técnico deve ser treinada em primeiros socorros e procedimentos de emergência específicos para ambiente hiperbárico."),
        ("Sustentabilidade Financeira e Reembolso de OHB", "A oxigenoterapia hiperbárica tem código TUSS e cobertura regulamentada pela ANS para indicações específicas (Rol de Procedimentos). A cobertura do SUS é via APAC para indicações habilitadas. A clínica deve verificar as indicações cobertas por cada operadora e estruturar o processo de autorização prévia de forma eficiente. O pé diabético, a principal indicação, tem cobertura ampla. Indicações como sequelas de radioterapia e osteomielite refratária podem exigir recursos de negativa. Curativos avançados (NPWT, substitutos dérmicos) têm valores elevados de insumo e precisam de estratégia de reembolso cuidadosa junto às operadoras."),
    ],
    faq_list=[
        ("Quais são as principais indicações da oxigenoterapia hiperbárica (OHB)?",
         "As indicações com maior nível de evidência incluem: pé diabético isquêmico com úlcera refratária, lesões por radiação (osteonecrose por rádio, cistite e proctite actínicas), osteomielite crônica refratária, intoxicação por monóxido de carbono, embolismo gasoso, síndrome de descompressão, e algumas feridas pós-cirúrgicas comprometidas. A indicação deve ser feita por médico especialista após avaliação criteriosa."),
        ("Quem pode se especializar em medicina hiperbárica no Brasil?",
         "A medicina hiperbárica é uma área de atuação médica reconhecida pelo CFM. Médicos de diversas especialidades (cirurgiões vasculares, ortopedistas, clínicos, endocrinologistas) podem se especializar por meio de cursos reconhecidos pela SBMH e pela SBMN (Sociedade Brasileira de Medicina Náutica). Enfermeiros especialistas em estomaterapia são os profissionais de enfermagem mais adequados para atuar em centros de feridas."),
        ("O tratamento de pé diabético pode evitar amputações?",
         "Sim. O tratamento multidisciplinar especializado — controle glicêmico rigoroso, revascularização quando indicada, desbridamento cirúrgico, curativos avançados, OHB e descarga de pressão adequada — pode evitar amputações em grande parte dos casos de pé diabético com úlcera. A rapidez no início do tratamento especializado é determinante — pacientes encaminhados tardiamente têm prognóstico mais reservado."),
    ]
)

# Article 4437 — SaaS sales: endoscopia digestiva alta e baixa
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-endoscopia-digestiva-alta-e-baixa",
    title="Vendas para o Setor de SaaS de Gestão de Clínicas de Endoscopia Digestiva Alta e Baixa",
    desc="Guia de vendas B2B para plataformas SaaS voltadas a clínicas e centros de endoscopia digestiva, colonoscopia e gastroenterologia endoscópica.",
    h1="Vendas para o Setor de SaaS de Gestão de Clínicas de Endoscopia Digestiva Alta e Baixa",
    lead="Centros de endoscopia digestiva realizam procedimentos de alto volume — endoscopias digestivas altas, colonoscopias, ecoendoscopias — com necessidade de gestão rigorosa de agenda, preparo de paciente, laudos estruturados e faturamento de procedimentos. SaaS especializados nesse segmento têm alto potencial de eficiência operacional e adoção.",
    sections=[
        ("O Mercado de Endoscopia Digestiva no Brasil", "A endoscopia digestiva é uma das especialidades médicas com maior volume de procedimentos no Brasil — estima-se mais de 10 milhões de endoscopias digestivas altas e colonoscopias realizadas anualmente. Rastreamento de câncer colorretal, investigação de sintomas digestivos, erradicação de H. pylori e tratamento endoscópico de pólipos e varizes esofagianas são as indicações mais comuns. Centros de endoscopia independentes, associados a clínicas de gastroenterologia ou integrados a hospitais têm perfis de gestão distintos — mas todos enfrentam o desafio comum do alto volume de procedimentos, necessidade de laudos estruturados e gestão do preparo intestinal dos pacientes."),
        ("Funcionalidades Críticas para Centros de Endoscopia", "As funcionalidades mais valorizadas incluem: agendamento de procedimentos com diferenciação por tipo (EDA, colonoscopia, ecoendoscopia, CPRE), confirmação automática e envio de orientações de preparo por WhatsApp, lista de espera com priorização por urgência clínica, laudos estruturados de endoscopia com banco de achados padronizados (polipectomia, gastrite H. pylori, varizes), integração com câmeras de videoendoscopia para captura de imagens diretamente no laudo, faturamento de procedimentos com TUSS correto (discriminando honorários, anestesia e materiais), e portal de acesso ao laudo para o paciente e para o médico solicitante."),
        ("Abordagem de Venda e Diferenciação da Demonstração", "A demonstração mais convincente para centros de endoscopia mostra o laudo estruturado com imagens de videoendoscopia integradas — o endoscopista vê imediatamente como o trabalho de documentação é reduzido de 20 minutos para 5 minutos por laudo. A integração direta com as câmeras de endoscopia (Olympus, Fujifilm, Karl Storz) via interface DICOM ou USB é o diferencial técnico mais diferenciador. Para gerentes administrativos, mostrar o painel de produtividade — procedimentos por médico, taxa de ocupação de sala, valores faturados por período — converte com eficácia ao demonstrar o controle financeiro que a plataforma proporciona."),
        ("Integrações Estratégicas no Ecossistema de Endoscopia", "As integrações mais relevantes incluem: videoendoscópios (Olympus, Fujifilm, Karl Storz — exportação de imagens e vídeos no laudo), sistema PACS para armazenamento de imagens médicas, laboratórios de patologia para resultados de biópsias realizadas no procedimento, integração com convênios via TISS para autorização eletrônica, e plataformas de telemedicina para segunda opinião de laudos de casos complexos (pólipo com displasia, lesão subepitelial). A integração com HIS hospitalares (quando o centro está dentro de um hospital) é frequentemente exigida pelas CTIs de hospitais parceiros."),
        ("Retenção e Crescimento em Centros de Endoscopia", "A retenção é elevada porque os laudos estruturados acumulados ao longo do tempo — especialmente o histórico de colonoscopia com fotos de pólipos e estadiamento de achados — criam um ativo que o médico não quer perder. Módulos de expansão incluem: aplicativo de preparo intestinal para o paciente (guia passo a passo, checklist de preparo, lembretes por push notification), analytics de qualidade endoscópica (taxa de detecção de adenoma — ADR — por médico, tempo de retirada no cólon), e integração com registros nacionais de pólipos colônicos para pesquisa clínica. Endoscopia realizada em day clinics e ambulatórios cirúrgicos de hospitais são mercados adjacentes onde o mesmo SaaS pode expandir com módulos específicos."),
    ],
    faq_list=[
        ("O SaaS de endoscopia pode integrar com câmeras de videoendoscopia de diferentes fabricantes?",
         "Sim. A integração via DICOM (para exportação de imagens estáticas e vídeos) é suportada pelos principais fabricantes (Olympus, Fujifilm, Karl Storz). Alguns fabricantes têm interfaces proprietárias adicionais. A integração direta com a câmera elimina a necessidade de fotografar a tela do monitor de endoscopia com câmera secundária — prática ainda comum em centros menos digitalizados."),
        ("O que é ADR (Adenoma Detection Rate) e por que é importante para centros de endoscopia?",
         "ADR é a taxa de detecção de adenomas (pólipos pré-cancerosos) pelo médico em colonoscopias de rastreamento. É o principal indicador de qualidade da colonoscopia — ADR abaixo de 25% (para homens) ou 15% (para mulheres) está associado a maior risco de câncer colorretal de intervalo. Centros de qualidade monitoram o ADR por médico e implementam estratégias de melhoria para aqueles abaixo do benchmark."),
        ("Como o sistema pode ajudar na gestão do preparo intestinal dos pacientes?",
         "Envio automático de orientações de preparo por WhatsApp (dieta, horário de uso do laxante, jejum), lembretes na véspera e no dia do exame, e check-list de confirmação de preparo na recepção reduzem a taxa de colonoscopias canceladas ou de baixa qualidade por preparo inadequado — uma das principais causas de retrabalho e insatisfação em centros de endoscopia."),
    ]
)

# Article 4438 — Consulting: gestão de parcerias e ecossistemas de negócios
art(
    slug="consultoria-de-gestao-de-parcerias-e-ecossistemas-de-negocios",
    title="Consultoria de Gestão de Parcerias e Ecossistemas de Negócios",
    desc="Como estruturar uma consultoria especializada em gestão de parcerias estratégicas e ecossistemas de negócios: metodologia, clientes e posicionamento.",
    h1="Consultoria de Gestão de Parcerias e Ecossistemas de Negócios",
    lead="Em uma economia de plataformas e ecossistemas, crescer sozinho é cada vez mais limitado. Empresas que sabem construir, gerenciar e escalar parcerias estratégicas crescem mais rápido e com menor custo. Consultores especializados em gestão de parcerias ajudam organizações a estruturar programas de parceiros, alianças estratégicas e ecossistemas de co-criação.",
    sections=[
        ("A Economia de Ecossistemas e a Importância das Parcerias", "Os modelos de negócio mais bem-sucedidos da última década — Apple, Amazon, Salesforce, Microsoft — são baseados em ecossistemas de parceiros que multiplicam o valor da plataforma central. No Brasil, essa dinâmica se reflete em startups que constroem marketplaces, SaaS que montam programas de parceiros (ISVs, consultores, revendedores) e grandes empresas que criam ecossistemas de inovação com startups e fornecedores. A gestão de parcerias é uma competência organizacional que vai muito além do departamento comercial — envolve estratégia, operações, produto e cultura."),
        ("Tipos de Parcerias e Estratégias de Ecossistema", "As parcerias podem ser classificadas por função: parcerias de distribuição (canais que vendem o produto da empresa — revendedores, distribuidores, agentes), parcerias tecnológicas (integrações, bundling de produtos complementares), parcerias de co-marketing (ações conjuntas de geração de demanda), parcerias de co-desenvolvimento (criação conjunta de produtos ou serviços), e alianças estratégicas (acordos de cooperação de longo prazo com exclusividade ou preferência). A consultoria deve ajudar a empresa a definir qual tipo de parceria é mais relevante para seus objetivos de crescimento e como estruturar cada tipo de forma que seja mutuamente benéfica."),
        ("Estruturação de Programas de Parceiros", "Um programa de parceiros estruturado define: critérios de qualificação e diferentes tiers (bronze, silver, gold, platinum — com benefícios e obrigações crescentes), ferramentas de suporte (portal de parceiros com materiais de vendas, treinamentos, registro de oportunidades, acesso a suporte técnico dedicado), modelo de compensação (comissão sobre vendas, desconto para revenda, lead sharing), métricas de desempenho por parceiro e por tier, e processo de gestão do relacionamento (channel manager dedicado por tier superior, touchpoints regulares, QBRs). Programas bem estruturados criam comprometimento dos parceiros e superam a receita do canal direto em empresas maduras."),
        ("Gestão de Ecossistemas de Inovação", "Grandes empresas e startups em crescimento criam ecossistemas de inovação — programas de aceleração corporativa, hubs de inovação aberta, programas de co-criação com fornecedores estratégicos. O consultor de ecossistemas ajuda a definir o propósito do ecossistema (o que a empresa ganha, o que os parceiros ganham), o modelo de governança (quem decide, como conflitos são resolvidos, como IP de co-criação é compartilhado), e os mecanismos de engajamento que mantêm os parceiros ativos e motivados ao longo do tempo. Ecossistemas sem governança clara frequentemente decaem — os parceiros perdem interesse quando não percebem valor consistente."),
        ("Desenvolvendo a Prática de Consultoria de Parcerias", "O consultor de parcerias e ecossistemas deve ter experiência prática em programas de parceiros — idealmente como líder de aliança ou channel em uma empresa de tecnologia ou serviços. A credibilidade vem de ter construído programas reais com resultados mensuráveis. Publicações sobre estratégia de ecossistemas, participação em eventos de partnerships (Partnership Leaders, ELG — Ecosystem-Led Growth) e rede no ecossistema de venture capital e startups ampliam a visibilidade e o acesso a clientes de alta qualidade."),
    ],
    faq_list=[
        ("Qual é a diferença entre canal de vendas e aliança estratégica?",
         "Canal de vendas é uma parceria de distribuição — o parceiro vende o produto da empresa para seus clientes em troca de comissão ou margem. Aliança estratégica é um acordo mais profundo — as empresas combinam capacidades, tecnologias ou acesso a mercado para criar valor que nenhuma das duas conseguiria sozinha. Alianças estratégicas geralmente envolvem integração de produto, co-desenvolvimento e comprometimento de longo prazo."),
        ("Como medir o sucesso de um programa de parceiros?",
         "Métricas chave incluem: receita gerada por parceiros (percentual do total), número de parceiros ativos vs. cadastrados (ativação), taxa de crescimento de receita por parceiro (expansão), NPS de parceiros (satisfação), número de deals fechados com participação de parceiro, e CAC de leads gerados por parceiros vs. canal direto. Programas de parceiros maduros geram 20-40% ou mais da receita total."),
        ("O que é ELG (Ecosystem-Led Growth) e como se diferencia do PLG?",
         "ELG (Ecosystem-Led Growth) é uma estratégia de crescimento que usa o ecossistema de parceiros como motor principal de aquisição, expansão e retenção de clientes. PLG (Product-Led Growth) usa o produto diretamente como motor de crescimento. ELG complementa tanto o PLG quanto o SLG (Sales-Led Growth) — os parceiros ampliam o alcance do produto e da força de vendas para mercados e segmentos onde a empresa não chegaria sozinha com custo viável."),
    ]
)

# ── Sitemap + trilha ──────────────────────────────────────────────────────────
root = pathlib.Path(__file__).parent
slugs = [
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-plataforma-de-dados-e-data-governance",
     "Gestão de Negócios de Empresa de B2B SaaS de Plataforma de Dados e Data Governance"),
    ("gestao-de-clinicas-de-nefrologia-adulto-e-hipertensao-renal",
     "Gestão de Clínicas de Nefrologia Adulto e Hipertensão Renal"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-centros-de-medicina-preventiva-e-check-up",
     "Vendas para o Setor de SaaS de Gestão de Centros de Medicina Preventiva e Check-up"),
    ("consultoria-de-gestao-de-processos-de-negocios-e-bpm",
     "Consultoria de Gestão de Processos de Negócios e BPM"),
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-contratos-e-procurement",
     "Gestão de Negócios de Empresa de B2B SaaS de Gestão de Contratos e Procurement"),
    ("gestao-de-clinicas-de-medicina-hiperbarica-e-tratamento-de-feridas-complexas",
     "Gestão de Clínicas de Medicina Hiperbárica e Tratamento de Feridas Complexas"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-endoscopia-digestiva-alta-e-baixa",
     "Vendas para o Setor de SaaS de Gestão de Clínicas de Endoscopia Digestiva Alta e Baixa"),
    ("consultoria-de-gestao-de-parcerias-e-ecossistemas-de-negocios",
     "Consultoria de Gestão de Parcerias e Ecossistemas de Negócios"),
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

print("Done — batch 1474")
