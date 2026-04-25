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
body{{font-family:sans-serif;margin:0;padding:0;color:#222}}
header{{background:#0a7c4e;padding:16px 24px}}
header a{{color:#fff;text-decoration:none;font-size:1.3rem;font-weight:700}}
main{{max-width:860px;margin:40px auto;padding:0 20px}}
h1{{font-size:2rem;color:#0a7c4e}}
h2{{font-size:1.3rem;color:#065f3a;margin-top:32px}}
p{{line-height:1.7}}
.lead{{font-size:1.1rem;color:#444}}
.faq{{background:#f4faf7;border-left:4px solid #0a7c4e;padding:20px 24px;margin-top:40px}}
.faq h2{{margin-top:0}}
.faq-item{{margin-bottom:20px}}
.faq-item h3{{margin-bottom:4px;color:#065f3a}}
footer{{text-align:center;padding:32px;color:#777;font-size:.9rem;margin-top:60px}}
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

# Article 4567 — B2B SaaS: gym / fitness management
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-academia-e-fitness",
    title="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Academia e Fitness",
    desc="Como construir e escalar uma empresa de B2B SaaS de gestão de academia e fitness no Brasil: produto, go-to-market, retenção e estratégias de crescimento sustentável.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Academia e Fitness",
    lead="O setor fitness brasileiro é um dos maiores do mundo, com mais de 35.000 academias e estúdios de pequeno e grande porte. A gestão de academias — com controle de membros, mensalidades, agendamento de aulas, controle de acesso e retenção de clientes — é um campo maduro de SaaS com players consolidados, mas ainda com muito espaço para inovação e especialização por nicho.",
    sections=[
        ("Panorama do Mercado de SaaS para Academias no Brasil", "O Brasil é o segundo maior mercado fitness do mundo em número de academias, atrás apenas dos EUA. O perfil do setor é muito diverso: grandes redes (SmartFit, Bodytech, Bio Ritmo) com centenas de unidades e requisitos enterprise, franquias de nicho (CrossFit boxes, estúdios de pilates, studios de yoga) e academias independentes de pequeno porte que são a maioria do mercado. Players como Tecnofit, EVO e Wellz dominam segmentos específicos — há espaço para soluções verticalizadas por tipo de academia."),
        ("Produto: Core Funcionalidades de SaaS para Academias", "As funcionalidades essenciais incluem: gestão de membros (cadastro, planos, renovações, inadimplência), cobranças automatizadas (débito automático, PIX, cartão de crédito recorrente), controle de acesso por catracas e torniquetes via cartão, QR Code ou biometria, agendamento de aulas coletivas com controle de vagas, gestão de personal trainers (agenda, clientes, comissões), avaliações físicas digitais, e relatórios de receita, churn e frequência de alunos por período."),
        ("Nichos de Mercado e Oportunidades de Especialização", "A especialização vertical cria diferenciação real: studios de pilates precisam de agendamento por aparelho (reformer, chair, cadillac) com controle de vagas por tipo de equipamento; CrossFit boxes precisam de gestão de WODs e turmas com capacidade limitada; academias de natação precisam de gestão de raia e horários de piscina; estúdios de yoga valorizam agendamento flexível e gestão de assinaturas ilimitadas. Soluções que cobrem essas especificidades com profundidade vencem a competição de plataformas genéricas."),
        ("Engajamento, Retenção e Combate ao Churn", "Churn é o maior desafio das academias: entre 30-50% dos novos alunos abandonam nos primeiros 3 meses. SaaS que ajuda academias a combater isso — com alertas de frequência baixa, comunicação automática de reengajamento, programas de desafio e gamificação, e relatórios de comportamento do aluno — se torna parceiro estratégico, não apenas ferramenta operacional. O NPS do aluno, a taxa de renovação de planos e a frequência média semanal são métricas que o sistema deve monitorar e ajudar a melhorar."),
        ("Go-to-Market e Canais de Aquisição", "Academias independentes são melhor adquiridas via inbound (SEO para 'sistema para academia', 'software de gestão de academia'), parcerias com distribuidores de catracas e equipamentos de fitness (bundle de equipamento + software), e influenciadores do setor fitness (personal trainers com audiência no Instagram). Franquias exigem abordagem diferente: o franqueador decide o sistema para toda a rede, com venda direta ao franqueador e implementação para todas as unidades — um contrato com potencial de expansão exponencial.")
    ],
    faq_list=[
        ("Qual funcionalidade de SaaS tem maior impacto na retenção de alunos de academia?", "A maior alavanca é o monitoramento de frequência com ação proativa: quando um aluno não vai à academia por mais de 7-10 dias, o sistema dispara automaticamente uma mensagem personalizada de reengajamento. Academias que implementam esse recurso relatam redução de 15-25% no churn precoce. Segundo impacto maior é o agendamento de aulas — alunos que se comprometem com uma aula específica têm 3x mais probabilidade de frequentar do que aqueles sem compromisso."),
        ("Como funciona a integração de SaaS com catracas de controle de acesso?", "Catracas se integram via protocolo serial (RS-485) ou TCP/IP com o servidor do sistema de gestão. Quando um aluno se apresenta na catraca (cartão magnético, QR Code, tag RFID ou biometria facial), a catraca consulta o sistema em tempo real para verificar se a mensalidade está em dia e o acesso é válido. O sistema registra a entrada com data/hora — gerando histórico de frequência do aluno. Integrações modernas operam via API REST em tempo real, sem necessidade de servidor local."),
        ("É viável um SaaS de academia competir com Tecnofit e EVO?", "Competição frontal é difícil — esses players têm base instalada grande e funcionalidades maduras. A estratégia mais eficaz é a verticalização: construa o melhor SaaS para studios de pilates, ou para boxes de CrossFit, ou para academias de natação. Funcionalidades específicas do nicho — que os generalistas não têm — criam fidelidade. À medida que o nicho é conquistado, a expansão para outros segmentos adjacentes é mais viável do que atacar o mercado geral desde o início.")
    ]
)

# Article 4568 — Clinic management: gastroenterology / hepatology
art(
    slug="gestao-de-clinicas-de-gastroenterologia-e-hepatologia",
    title="Gestão de Clínicas de Gastroenterologia e Hepatologia",
    desc="Guia prático para gestão de clínicas de gastroenterologia e hepatologia: estrutura clínica, procedimentos endoscópicos, faturamento por convênio e estratégias de crescimento.",
    h1="Gestão de Clínicas de Gastroenterologia e Hepatologia",
    lead="Clínicas de gastroenterologia e hepatologia atendem uma das especialidades de maior demanda no sistema de saúde brasileiro: doenças do trato gastrointestinal, hepáticas e pancreáticas afetam dezenas de milhões de brasileiros. A gestão eficiente dessas clínicas combina alta rotatividade de consultas com procedimentos endoscópicos de alto valor, gestão de pacientes crônicos com hepatites e doença hepática, e faturamento complexo por convênio.",
    sections=[
        ("Escopo da Gastroenterologia e Hepatologia", "Gastroenterologistas atendem condições muito prevalentes: doença do refluxo gastroesofágico, dispepsia funcional, síndrome do intestino irritável, doença inflamatória intestinal (Crohn, retocolite ulcerativa), pólipos e câncer colorretal, cirrose e doença hepática gordurosa não alcoólica (DHGNA/MASLD), hepatites virais e neoplasias gastrointestinais. A hepatologia, como subespecialidade, foca em doenças hepáticas — frequentemente em conjunto com gastroenterologia — com demanda crescente dado o aumento da DHGNA associada à obesidade e síndrome metabólica."),
        ("Endoscopia Digestiva: Procedimentos e Gestão de Sala", "A endoscopia digestiva alta e a colonoscopia são os procedimentos de maior valor em gastroenterologia. A gestão da sala de endoscopia exige: agendamento de procedimentos com tempo de preparo do paciente (dieta e preparo intestinal), controle de disponibilidade de endoscópio e acessórios (pinças de biópsia, alças de polipectomia), limpeza e desinfecção de alto nível entre procedimentos (conforme regulação ANVISA), controle de arquivo e laudos de vídeo, e gestão de materiais descartáveis de alto custo (cápsulas endoscópicas, escopos ultrassonográficos)."),
        ("Gestão de Pacientes com Doença Hepática Crônica", "Pacientes com cirrose, hepatite B crônica em tratamento, DHGNA avançada e colangiopatias necessitam de acompanhamento rigoroso: ultrassonografia e alfafetoproteína semestral para rastreamento de hepatocarcinoma em cirróticos, exames laboratoriais periódicos (ALT, AST, GGT, coagulograma, albumina), controle de complicações (ascite, encefalopatia, varizes esofagianas — rastreio por endoscopia). Prontuários com histórico longitudinal de parâmetros hepáticos e registro de complicações são essenciais para decisão clínica."),
        ("Faturamento por Convênio em Gastroenterologia", "Gastroenterologia tem procedimentos bem cobertos por convênios: endoscopia digestiva alta, colonoscopia, polipectomia, biópsia guiada por EUS (ultrassonografia endoscópica), cápsula endoscópica, colangiografia endoscópica (CPRE) e tratamento de varizes esofagianas. A autorização prévia para colonoscopia (especialmente com sedação) e para procedimentos de alto custo como EUS e CPRE é etapa crítica. A correta codificação TUSS e a gestão de glosas por ausência de autorização ou laudos incompletos são atividades que demandam equipe de faturamento especializada."),
        ("Marketing e Captação em Gastroenterologia", "Gastroenterologia tem alta busca orgânica: 'colonoscopia preventiva', 'tratamento de refluxo', 'hepatologista' e 'endoscopia digestiva' têm volume expressivo. Conteúdo educativo sobre prevenção de câncer colorretal (colonoscopia de rastreamento), doença hepática gordurosa e cuidados com a saúde digestiva em redes sociais e YouTube converte bem em consultas. Parcerias com clínicos gerais, cardiologistas e endocrinologistas — que frequentemente identificam alterações hepáticas em pacientes diabéticos e dislipidêmicos — são canais eficazes de encaminhamento.")
    ],
    faq_list=[
        ("A partir de que idade é recomendada a colonoscopia de rastreamento?", "A Sociedade Brasileira de Coloproctologia e a Sociedade Brasileira de Endoscopia Digestiva recomendam colonoscopia de rastreamento para câncer colorretal a partir dos 45-50 anos para a população de risco médio, ou antes para pacientes com histórico familiar de câncer colorretal ou pólipos em parente de primeiro grau (rastreamento a partir dos 40 anos ou 10 anos antes do diagnóstico do familiar). Planos de saúde cobrem colonoscopia de rastreamento conforme o rol da ANS."),
        ("O que é DHGNA e por que sua prevalência está aumentando?", "DHGNA (Doença Hepática Gordurosa Não Alcoólica) — atualmente chamada MASLD (Metabolic Dysfunction-Associated Steatotic Liver Disease) — é o acúmulo de gordura no fígado sem consumo excessivo de álcool, associado à síndrome metabólica (obesidade, diabetes, hipertrigliceridemia, hipertensão). É a doença hepática mais prevalente no mundo, afetando 25-30% da população adulta brasileira. Sem tratamento (mudança de estilo de vida, controle metabólico), pode evoluir para cirrose e hepatocarcinoma — por isso o acompanhamento hepatológico é fundamental."),
        ("Como funciona a cápsula endoscópica e quando é indicada?", "A cápsula endoscópica é um dispositivo do tamanho de uma cápsula de remédio que contém câmera, luz e transmissor — o paciente engole, ela percorre todo o trato gastrointestinal (incluindo o intestino delgado, que endoscópio convencional não alcança) fotografando a mucosa e transmitindo imagens para um receptor externo. É indicada principalmente para investigação de sangramento obscuro de origem no intestino delgado, suspeita de doença de Crohn no intestino delgado e pólipos em síndromes polipomatosas hereditárias.")
    ]
)

# Article 4569 — SaaS sales for centros: integrative oncology / integrative medicine
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-centros-de-oncologia-integrativa-e-medicina-integrativa",
    title="Vendas para o Setor de SaaS de Gestão de Centros de Oncologia Integrativa e Medicina Integrativa",
    desc="Estratégias de vendas B2B de SaaS para centros de oncologia integrativa e medicina integrativa: perfil do comprador, proposta de valor, ciclo de vendas e como crescer nesse nicho.",
    h1="Vendas para o Setor de SaaS de Gestão de Centros de Oncologia Integrativa e Medicina Integrativa",
    lead="Centros de oncologia integrativa e medicina integrativa combinam tratamentos convencionais com práticas complementares — acupuntura, fitoterapia, meditação, nutrologia integrativa, musicoterapia e outras abordagens validadas para controle de sintomas e melhora da qualidade de vida de pacientes oncológicos e crônicos. A gestão desses centros é peculiar e cria demanda específica por SaaS que entenda o cuidado integrativo.",
    sections=[
        ("O Perfil dos Centros de Oncologia Integrativa", "Centros de oncologia integrativa atendem principalmente pacientes em tratamento de câncer que buscam suporte complementar: controle de náusea por quimioterapia (acupuntura, gengibre), redução de fadiga, manejo de ansiedade e depressão, suporte nutricional especializado e manutenção da qualidade de vida durante e após o tratamento. A equipe é multidisciplinar: oncologistas integrativo, acupunturistas, nutricionistas, psico-oncólogos, médicos com especialização em medicina integrativa. A complexidade coordenativa desse cuidado exige sistemas robustos."),
        ("Proposta de Valor do SaaS para Medicina Integrativa", "As necessidades de gestão mais relevantes incluem: prontuário multidisciplinar compartilhado com registros por especialidade (acupuntura, nutrição, psicologia), agenda visual por profissional e por modalidade de tratamento, gestão de planos de tratamento integrativo (combinando diferentes práticas com frequência e duração específicas), comunicação segura entre profissionais sobre o mesmo paciente, e relatórios de qualidade de vida (questionários PROs — Patient-Reported Outcomes — como FACT-G, SF-36) para avaliação de desfechos."),
        ("Abordagem de Vendas e Identificação de Dores", "O decisor em centros integrativos é geralmente o médico fundador — frequentemente com perfil acadêmico e de pesquisa — ou o gestor administrativo em centros maiores. A abordagem mais eficaz começa por explorar a complexidade da coordenação multidisciplinar: 'Como você garante que o nutricionista sabe o que o acupunturista registrou para o mesmo paciente?' e 'Como você controla os resultados dos questionários de qualidade de vida ao longo do tratamento?' Essas perguntas revelam lacunas que o SaaS preenche com valor claro."),
        ("Precificação e Modelo de Negócio", "Centros de medicina integrativa tendem a ser serviços de pagamento particular — poucas operadoras cobrem práticas integrativas além das listadas no rol da ANS (acupuntura e homeopatia). Isso significa que o cliente paga diretamente e é exigente em qualidade e resultados. O ticket das consultas e dos programas de tratamento é elevado — um programa mensal de suporte integrativo para paciente oncológico pode custar R$2.000-6.000/mês. O SaaS de R$500-2.000/mês é facilmente justificado por melhora na coordenação e na qualidade do atendimento."),
        ("Expansão para Centros de Medicina Preventiva e Longevidade", "A fronteira entre medicina integrativa e medicina de longevidade está se dissolvendo: centros que oferecem avaliações funcionais avançadas, programas de saúde personalizada e intervenções preventivas baseadas em biomarcadores estão crescendo rapidamente. SaaS que suporte o acompanhamento longitudinal de múltiplos biomarcadores (telômeros, inflamação, microbioma, genômica), planos de intervenção personalizados e comunicação frequente com o paciente entre consultas é o próximo passo natural para centros integrativos que migram para o modelo de longevidade.")
    ],
    faq_list=[
        ("Práticas integrativas são reconhecidas pelo CFM e pela ANS?", "O CFM reconhece diversas práticas integrativas como parte do exercício médico: acupuntura (Resolução CFM 1.455/1995), homeopatia, ozonioterapia, fitoterapia e outras. A ANS inclui acupuntura e homeopatia no rol de cobertura obrigatória para planos médico-hospitalares. O Ministério da Saúde tem a PNPIC (Política Nacional de Práticas Integrativas e Complementares no SUS) que reconhece 29 práticas. Centros integrativos que mantêm conformidade regulatória têm base legal sólida para seus serviços."),
        ("Como medir resultados em centros de medicina integrativa?", "A mensuração de resultados em medicina integrativa usa instrumentos validados de qualidade de vida: FACT-G (Functional Assessment of Cancer Therapy — General) para pacientes oncológicos, SF-36 para saúde geral, escalas de ansiedade (HAD, GAD-7) e depressão (PHQ-9), avaliações de fadiga (FACIT-F) e escalas de dor (EVA). Aplicar esses questionários periodicamente e monitorar a evolução no tempo — com gráficos comparativos — demonstra o impacto das intervenções integrativas e justifica o investimento do paciente."),
        ("Centros de medicina integrativa precisam de prontuário eletrônico específico ou podem usar um genérico?", "Prontuários genéricos raramente suportam as especificidades da medicina integrativa: registros de técnicas de acupuntura (pontos utilizados, número de agulhas, sensação de Deqi), fichas de fitoterapia com formulações personalizadas, registros de musicoterapia e arteterapia, avaliações funcionais de múltiplos domínios. Sistemas específicos ou plataformas altamente configuráveis — que permitem criar campos customizados por especialidade — oferecem muito mais valor. O CFM exige que o prontuário eletrônico seja completo e fidedigno, independente do tipo de prática registrada.")
    ]
)

# Article 4570 — Consulting: sustainable supply chain / reverse logistics
art(
    slug="consultoria-de-supply-chain-sustentavel-e-logistica-reversa",
    title="Consultoria de Supply Chain Sustentável e Logística Reversa",
    desc="Como estruturar uma consultoria de supply chain sustentável e logística reversa: serviços, metodologias, captação de clientes e como gerar valor mensurável em cadeias de suprimentos.",
    h1="Consultoria de Supply Chain Sustentável e Logística Reversa",
    lead="Pressões regulatórias, exigências de grandes varejistas e consumidores conscientes estão transformando a gestão de cadeia de suprimentos: sustentabilidade deixou de ser diferencial e se tornou requisito. Consultorias especializadas em supply chain sustentável e logística reversa têm oportunidade crescente de ajudar empresas a reduzir emissões, eliminar resíduos e criar processos circulares que geram valor econômico real.",
    sections=[
        ("O Contexto de Urgência para Supply Chain Sustentável", "Grandes varejistas globais (Walmart, Amazon, Carrefour) exigem dados de emissão de carbono de seus fornecedores brasileiros. O EUDR (Regulamento Europeu sobre Desmatamento) impõe rastreabilidade geoespacial para commodities. Fundos de investimento com critérios ESG avaliam a cadeia de suprimentos de seus portfolios. Regulações de logística reversa (Política Nacional de Resíduos Sólidos — Lei 12.305/2010) criam obrigações legais para fabricantes e importadores. Todas essas pressões convergem em demanda por consultores especializados em supply chains verdes."),
        ("Portfólio de Serviços de Consultoria Sustentável", "Os serviços mais demandados incluem: mapeamento e medição de emissões de GEE na cadeia de suprimentos (Scope 1, 2 e 3 — GHG Protocol), identificação de hot spots de impacto ambiental, estratégias de descarbonização de cadeia de suprimentos, estruturação de programas de logística reversa (pós-consumo), design de embalagens sustentáveis, certificações de cadeia de custódia (FSC para madeira e papel, RSPO para óleo de palma, Rainforest Alliance), e relatórios de sustentabilidade de cadeia para stakeholders e para GRI."),
        ("Metodologias: LCA, Economia Circular e S-LCA", "A Análise de Ciclo de Vida (LCA — Life Cycle Assessment) é a ferramenta padrão para quantificar impactos ambientais de produtos da extração de matérias-primas ao descarte. A Social LCA (S-LCA) acrescenta impactos sociais. Frameworks de economia circular (Ellen MacArthur Foundation) guiam o redesenho de sistemas de produto-serviço para eliminar resíduos por design. O GHG Protocol Corporate Value Chain Standard é a metodologia padrão para inventário de Scope 3. Dominar essas metodologias e suas ferramentas (SimaPro, Ecoinvent, OpenLCA) é o diferencial técnico da consultoria."),
        ("Captação de Clientes e Setores de Maior Demanda", "Os setores com maior demanda por consultoria de supply chain sustentável são: varejo de moda (fast fashion sob pressão de regulações de due diligence de cadeia), alimentos e bebidas (EUDR, certificações para mercado externo), eletroeletrônicos (obrigação de logística reversa por PNRS), petróleo e gás (escrutínio de Scope 3), e empresas que emitem relatórios GRI/SASB e precisam de dados de cadeia. A captação acontece via equipes de sustentabilidade corporativa, gestão de fornecedores e relações com investidores."),
        ("Logística Reversa: Da Obrigação Legal ao Negócio", "A PNRS (Lei 12.305/2010) obriga fabricantes, importadores, distribuidores e comerciantes de embalagens, eletroeletrônicos, pneus, óleo lubrificante, pilhas e baterias a estruturarem sistemas de logística reversa. Muitas empresas ainda estão em não conformidade — criando demanda imediata por diagnóstico e estruturação de programas. Além da conformidade, logística reversa bem desenhada gera valor: recuperação de materiais de alto valor (metais preciosos em eletrônicos), redução de custo de disposição de resíduos e diferenciação de marca por responsabilidade ambiental.")
    ],
    faq_list=[
        ("O que é Scope 3 e por que é o mais complexo de medir na cadeia de suprimentos?", "O GHG Protocol divide emissões em três escopos: Scope 1 (emissões diretas da empresa), Scope 2 (emissões da energia comprada) e Scope 3 (todas as demais emissões da cadeia de valor — fornecedores, transporte, uso do produto pelo cliente, descarte). Scope 3 é geralmente 70-90% da pegada de carbono de uma empresa, mas é o mais difícil de medir porque depende de dados de terceiros. Consultores de supply chain sustentável especializam-se em métodos de coleta, estimativa e validação de dados de Scope 3."),
        ("A logística reversa é obrigatória para todos os segmentos no Brasil?", "A PNRS e seus acordos setoriais tornaram a logística reversa obrigatória para: embalagens em geral (pós-consumo e pós-venda), embalagens de agrotóxicos, eletroeletrônicos, pilhas e baterias, pneus, óleos lubrificantes e lâmpadas fluorescentes. Para cada segmento, há um acordo setorial específico com metas e mecanismos definidos. Empresas que não cumprem podem ser autuadas pelo IBAMA e pelas autoridades estaduais de meio ambiente."),
        ("Como uma empresa pode transformar a logística reversa de custo em oportunidade de negócio?", "Logística reversa bem estruturada permite recuperar materiais de alto valor: cobre, alumínio, ouro e outros metais de eletroeletrônicos; PET e alumínio de embalagens; borracha de pneus. Empresas que criam parcerias com cooperativas de catadores para coleta, recicladores certificados para processamento e refinarias de metais preciosos para eletrônicos transformam o que seria custo de descarte em receita de venda de materiais secundários. Alguns setores como eletroeletrônicos têm potencial de recuperação de valor de 10-30% do custo do produto original.")
    ]
)

# Article 4571 — B2B SaaS: pharmacy / drugstore management
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-farmacias-e-drogarias",
    title="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Farmácias e Drogarias",
    desc="Como construir e escalar uma empresa de B2B SaaS de gestão de farmácias e drogarias no Brasil: produto, regulação, go-to-market e estratégias de crescimento em um mercado de alta demanda.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Farmácias e Drogarias",
    lead="O setor farmacêutico de varejo no Brasil tem mais de 90.000 farmácias e drogarias, e está em transformação acelerada: expansão de serviços farmacêuticos, programas de fidelização, integração com planos de saúde para desconto em medicamentos e crescimento do delivery. SaaS para farmácias precisa navegar regulações complexas da ANVISA, integrar com sistemas de prescrição eletrônica e entregar eficiência operacional real ao farmacêutico e ao proprietário.",
    sections=[
        ("Panorama do Mercado de SaaS para Farmácias", "O Brasil tem mais de 90.000 farmácias registradas — a maioria pequenas farmácias independentes ou redes regionais de pequeno porte. Redes grandes como Raia Drogasil, DPSP (Droga Raia/Drogasil) e Ultrafarma têm sistemas proprietários; o mercado de SaaS é a farmácia independente e a rede regional. Players como Pharma Systems, SisFarma e Universo estão estabelecidos, mas o mercado é fragmentado e há espaço para soluções com melhor UX e integração com novos canais (delivery, programas de desconto via convênio)."),
        ("Produto: Frente de Caixa, Estoque e Serviços Farmacêuticos", "As funcionalidades core para farmácias incluem: PDV com leitura de código de barras e integração com tabela BRASINDICE (atualização de preços de medicamentos), controle de estoque com curva ABC, gestão de medicamentos controlados (escrituração para SNGPC — Sistema Nacional de Gerenciamento de Produtos Controlados da ANVISA), integração com programas de desconto de laboratórios (Programa de Desconto de Medicamentos — PDM), emissão de NF-e e SAT/CF-e, e módulo de serviços farmacêuticos (aferição de pressão, glicemia, vacinação, aplicação de medicamentos)."),
        ("SNGPC e Compliance com a ANVISA", "O SNGPC é o sistema da ANVISA para controle de medicamentos sujeitos a controle especial — psicotrópicos, entorpecentes e outros. Farmácias que dispensam esses medicamentos devem registrar cada saída no SNGPC em tempo real. Falhas no SNGPC geram multas da ANVISA e podem resultar em cancelamento da licença de funcionamento. Um SaaS que integra nativamente com o SNGPC — registrando cada dispensação automaticamente, sem entrada manual — é requisito indispensável para farmácias com esses produtos."),
        ("Programas de Fidelização e Desconto em Medicamentos", "Laboratórios farmacêuticos mantêm programas de desconto para medicamentos de alto custo (oncológicos, biológicos) que exigem validação na farmácia no momento da compra. A integração com esses programas — via API dos laboratórios ou plataformas agregadoras — permite que a farmácia aplique o desconto automaticamente, sem processos manuais. Além disso, programas de fidelização próprios da farmácia (pontos, cashback) aumentam a frequência de compra e a lealdade do cliente, reduzindo a sensibilidade ao preço."),
        ("Go-to-Market e Expansão para Serviços Farmacêuticos", "Farmácias independentes são melhor adquiridas via associações (ABRAFARMA, SINCOFARMA), eventos do setor (FIFE, ExpoFarma) e parcerias com distribuidores farmacêuticos (que têm relacionamento direto com proprietários de farmácias). O crescimento dos serviços farmacêuticos — vacinação, testes rápidos, aferição de sinais vitais, orientação farmacêutica — cria demanda por módulos específicos de agendamento e registro de serviços. SaaS que abraça essa expansão além do PDV tradicional tem maior LTV e diferenciação competitiva.")
    ],
    faq_list=[
        ("O que é o SNGPC e como impacta a operação diária de uma farmácia?", "O SNGPC (Sistema Nacional de Gerenciamento de Produtos Controlados) é o sistema da ANVISA que rastreia a dispensação de medicamentos sujeitos a controle especial — antibióticos de venda restrita, psicotrópicos, entorpecentes e outros. Farmácias devem registrar cada dispensação em até 10 dias no SNGPC (ou imediatamente para maior conformidade). Um sistema de gestão integrado ao SNGPC registra automaticamente cada saída de controlado no sistema federal, eliminando escrituração manual e reduzindo o risco de inconsistências que geram multas da ANVISA."),
        ("Como funciona a integração com a tabela BRASINDICE em sistemas para farmácias?", "BRASINDICE é a tabela de preços máximos ao consumidor (PMC) de medicamentos, publicada mensalmente e regulada pela CMED/ANVISA. Sistemas de gestão de farmácia devem atualizar automaticamente os preços da tabela mensalmente — garantindo que a farmácia não venda medicamentos acima do PMC (infração sujeita a multa) e que os preços estejam sempre corretos. A atualização automática via integração com a BRASINDICE é funcionalidade básica que qualquer SaaS sério de farmácia deve oferecer."),
        ("Serviços farmacêuticos como vacinação e testes rápidos precisam de gestão específica?", "Sim. Vacinação em farmácia requer: agendamento com gestão de tipo de vacina e estoque de doses, registro do imunobiológico aplicado (nome, lote, validade, via de administração), emissão de comprovante de vacinação conforme RDC ANVISA 197/2017, e habilitação da farmácia como estabelecimento de vacinação. Testes rápidos requerem controle de estoque de kits por tipo de teste e registro de resultado por paciente. Módulos específicos nesses sistemas garantem compliance regulatório e qualidade assistencial.")
    ]
)

# Article 4572 — Clinic management: gynecology / obstetrics
art(
    slug="gestao-de-clinicas-de-ginecologia-e-obstetricia",
    title="Gestão de Clínicas de Ginecologia e Obstetrícia",
    desc="Guia prático para gestão de clínicas de ginecologia e obstetrícia: estrutura clínica, acompanhamento pré-natal, procedimentos, faturamento e estratégias de crescimento.",
    h1="Gestão de Clínicas de Ginecologia e Obstetrícia",
    lead="Clínicas de ginecologia e obstetrícia atendem mulheres ao longo de toda a vida reprodutiva e além, combinando consultas de saúde preventiva (preventivo, colposcopia, mamografia) com acompanhamento pré-natal, assistência ao parto e tratamento de patologias ginecológicas. A gestão dessas clínicas exige fluxos bem organizados para o pré-natal, integração com maternidades e controle de procedimentos ambulatoriais de alta demanda.",
    sections=[
        ("Estrutura e Perfil de Atendimento da Clínica Ginecológica", "Uma clínica de ginecologia e obstetrícia de referência opera com consultórios equipados para exame ginecológico (mesa ginecológica, colposcópio), sala de ultrassonografia obstétrica e pélvica, sala para procedimentos ambulatoriais (LEEP/CAF para tratamento de lesões cervicais, inserção de DIU, histeroscopia diagnóstica) e, em clínicas integradas, sala de parto para obstetras que atendem parto fisiológico em ambiente ambulatorial ou acesso a maternidade parceira para partos hospitalares."),
        ("Gestão do Pré-Natal: Fluxo e Prontuário", "O pré-natal é um serviço de alta fidelização: a gestante realiza 6-12 consultas mensais com o mesmo obstetra ao longo de 9 meses, gerando relacionamento de alta confiança. A gestão do pré-natal exige: controle do cronograma de consultas e exames (rastreamentos trimestrais conforme IG — Idade Gestacional), registro de ultrassonografias com morfológico e doppler, monitoração de ganho de peso, pressão e proteinúria, e preparação do plano de parto. Sistemas que automatizam lembretes de retorno e exames por IG reduzem faltas e melhoram a adesão ao pré-natal."),
        ("Ultrassonografia Obstétrica: Serviço Integrado de Alto Valor", "Ultrassonografias obstétricas — morfológico de primeiro e segundo trimestres, doppler das artérias uterinas, translucência nucal, ecocardiograma fetal — são exames de alto valor realizados com alta frequência ao longo do pré-natal. Clínicas que têm ultrassonografia própria capturam essa receita internamente, oferecem laudo imediato e tornam o serviço mais conveniente para a gestante. A integração do laudo ecográfico no prontuário do pré-natal é diferencial de qualidade assistencial."),
        ("Colposcopia, LEEP e Rastreamento de Câncer de Colo", "O rastreamento de câncer de colo uterino (Papanicolau trienal de 25 a 64 anos, conforme protocolo INCA) e o seguimento de lesões intraepiteliais (HSIL, LSIL) com colposcopia e LEEP (Loop Electrosurgical Excision Procedure) geram volume expressivo de procedimentos em clínicas ginecológicas. A gestão desse fluxo — resultado de preventivo, encaminhamento para colposcopia, realização de biópsia, resultado histopatológico, indicação de LEEP e seguimento pós-tratamento — requer prontuário com controle de rastreamento estruturado e alertas de retorno."),
        ("Marketing e Captação em Ginecologia", "Ginecologia tem captação híbrida: encaminhamento de clínicos gerais, médicos de família e pediatras (que encaminham pacientes adolescentes) e marketing digital direto à paciente. Conteúdo educativo sobre saúde da mulher — menopausa, endometriose, HPV e prevenção de câncer de colo, fertilidade — em redes sociais e YouTube tem engajamento muito alto com o público feminino. A reputação e os depoimentos de pacientes gestantes são o ativo de marketing mais poderoso para obstetras — e devem ser gerenciados ativamente via plataformas de avaliação online.")
    ],
    faq_list=[
        ("Quantas consultas de pré-natal são recomendadas e o que planos de saúde cobrem?", "O Ministério da Saúde recomenda mínimo de 6 consultas de pré-natal para gestações de baixo risco — uma por trimestre nas primeiras 28 semanas e a cada 15 dias no terceiro trimestre. Gestações de alto risco (gemelar, diabetes gestacional, hipertensão) requerem acompanhamento mais frequente. Planos de saúde têm cobertura obrigatória para pré-natal, parto e puerpério conforme o rol da ANS, incluindo as consultas, exames laboratoriais e ultrassonografias básicas."),
        ("O que é LEEP e quando é indicado no tratamento de lesões cervicais?", "LEEP (Loop Electrosurgical Excision Procedure) é um procedimento ambulatorial que usa um alça metálica com corrente elétrica para excisão de lesões intraepiteliais de alto grau (HSIL) do colo uterino — prevenindo a progressão para câncer. É realizado sob anestesia local no consultório, com recuperação rápida. A indicação baseia-se no resultado da colposcopia e biópsia confirmando HSIL persistente. O acompanhamento pós-LEEP com preventivo e colposcopia aos 6 e 12 meses é essencial para confirmar a cura e detectar recidivas."),
        ("Como uma clínica de ginecologia pode se diferenciar na captação de gestantes para o pré-natal?", "A captação de pré-natal acontece principalmente nos primeiros meses de gestação — quando a mulher descobre a gravidez e busca um obstetra. SEO para 'obstetra em [cidade]' e 'pré-natal [cidade]' é altamente eficaz. Diferenciais que influenciam a decisão: disponibilidade de ultrassonografia morfológica no mesmo local, participação com plano de saúde da gestante, serviço de plantão para dúvidas (WhatsApp ou aplicativo), e tour virtual pela clínica e pela maternidade parceira. Depoimentos de ex-pacientes são o fator de confiança mais decisivo.")
    ]
)

# Article 4573 — SaaS sales for clinics: geriatrics / elderly care
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-geriatria-e-cuidados-ao-idoso",
    title="Vendas para o Setor de SaaS de Gestão de Clínicas de Geriatria e Cuidados ao Idoso",
    desc="Estratégias de vendas B2B de SaaS para clínicas de geriatria e cuidados ao idoso: perfil do comprador, proposta de valor, ciclo de vendas e como crescer nesse mercado em expansão.",
    h1="Vendas para o Setor de SaaS de Gestão de Clínicas de Geriatria e Cuidados ao Idoso",
    lead="O envelhecimento acelerado da população brasileira — com mais de 35 milhões de pessoas acima de 60 anos hoje e projeção de 73 milhões em 2060 — cria demanda estrutural crescente por cuidados geriátricos especializados. Clínicas de geriatria, centros de dia para idosos e serviços de cuidadores domiciliares são um mercado em expansão que precisa de SaaS adaptado às especificidades do cuidado de longa duração do idoso.",
    sections=[
        ("O Mercado de Saúde do Idoso e Suas Particularidades", "O cuidado geriátrico especializado abrange muito além da consulta médica: avaliação geriátrica ampla (cognitiva, funcional, social, emocional), gestão de polifarmácia (idosos frequentemente usam 5-15 medicamentos), prevenção de quedas, gestão de síndromes geriátricas (delirium, sarcopenia, fragilidade), e cuidado continuado em diferentes settings — ambulatório, domicílio, centro de dia, instituição de longa permanência (ILPI). Cada modalidade tem necessidades de gestão específicas e distintas."),
        ("Proposta de Valor do SaaS para Geriatria", "Para clínicas ambulatoriais de geriatria, as necessidades prioritárias são: prontuário com avaliação geriátrica ampla estruturada (escalas de cognição — MEEM, MoCA; funcionalidade — Barthel, Lawton; risco de queda — Morse, Timed Up and Go; rastreio de depressão — GDS; avaliação de polifarmácia), gestão de retornos periódicos de idosos com múltiplas comorbidades, comunicação com familiares e cuidadores (que frequentemente são os interlocutores principais), e integração com outros profissionais da equipe multiprofissional geriátrica."),
        ("Perfil do Comprador e Abordagem Comercial", "O decisor em clínicas de geriatria é o geriatra proprietário ou o gestor de uma ILPI/centro de dia. A abordagem deve destacar as especificidades do cuidado geriátrico: 'Como você registra a evolução cognitiva de seus pacientes ao longo dos anos?', 'Como controla a polifarmácia — garantindo que o idoso não está tomando medicamentos contraindicados entre si?' e 'Como comunica intercorrências com a família do paciente?' Essas perguntas revelam dores concretas que o SaaS geriátrico resolve."),
        ("ILPIs e Centros de Dia: Necessidades Específicas", "Instituições de Longa Permanência para Idosos (ILPIs) têm necessidades de gestão distintas: controle de leitos e residentes, registros de enfermagem por turno, gestão de medicamentos (administração e controle de estoque de medicamentos por residente), relatórios regulatórios para a Vigilância Sanitária, comunicação com familiares sobre ocorrências e evolução. Centros de dia adicionam agendamento de atividades, refeições e transporte de idosos. SaaS que cobre essas necessidades específicas tem um mercado de ILPIs com mais de 3.000 unidades no Brasil."),
        ("Tendências: Cuidado Domiciliar e Tecnologia de Monitoramento", "Home care geriátrico cresce aceleradamente: famílias preferem que o idoso permaneça em casa com suporte especializado. Plataformas de gestão de cuidadores domiciliares — agendamento, registros de atendimento, controle de medicamentos, comunicação com a família e com o geriatra responsável — são produto de alta demanda. A integração com dispositivos de monitoramento (sensores de queda, monitoração de sinais vitais remotos, botões de emergência) cria um ecossistema de cuidado que o SaaS de gestão geriátrica pode orquestrar.")
    ],
    faq_list=[
        ("O que é avaliação geriátrica ampla e por que é diferente de uma consulta comum?", "Avaliação geriátrica ampla é uma avaliação multidimensional padronizada que examina: cognição (memória, atenção, funções executivas), humor (depressão, ansiedade), funcionalidade para AVDs (atividades de vida diária), mobilidade e equilíbrio (risco de queda), redes de suporte social, polifarmácia, nutrição e sensorial (visão, audição). É fundamentalmente diferente da consulta por queixa: o geriatra avalia o idoso como um todo, identificando vulnerabilidades que impactam a saúde mesmo que o paciente não as relate espontaneamente."),
        ("Planos de saúde cobrem consultas com geriatra e cuidados domiciliares?", "Consultas com geriatra em planos médico-hospitalares têm cobertura obrigatória pela ANS como especialidade médica. Home care (cuidados domiciliares com médico, enfermeiro ou fisioterapeuta) tem cobertura obrigatória em situações específicas (como substitutivo à internação hospitalar). Cuidadores de idosos não profissionais de saúde (auxiliares de cuidado) geralmente não são cobertos por planos. ILPIs não são cobertas por planos de saúde — são custeadas pela família ou por benefícios de assistência social."),
        ("Como SaaS pode ajudar a prevenir quedas em idosos acompanhados ambulatorialmente?", "Sistemas geriátricos com alertas de risco de queda — baseados em scores como Timed Up and Go e histórico de quedas prévias — permitem ao geriatra identificar os pacientes de maior risco e encaminhar para fisioterapia de equilíbrio, revisão de polifarmácia (retirada de medicamentos que aumentam risco de queda), adaptação do domicílio e prescrição de dispositivos auxiliares de marcha. O registro estruturado desses indicadores em cada consulta e a monitoração da evolução longitudinal são recursos que SaaS geriátrico específico oferece.")
    ]
)

# Article 4574 — Consulting: brand management / brand strategy
art(
    slug="consultoria-de-gestao-de-marcas-e-brand-strategy",
    title="Consultoria de Gestão de Marcas e Brand Strategy",
    desc="Como estruturar uma consultoria de gestão de marcas e brand strategy: serviços, metodologias, captação de clientes e como gerar valor mensurável em estratégia e posicionamento de marca.",
    h1="Consultoria de Gestão de Marcas e Brand Strategy",
    lead="Marcas são ativos intangíveis que representam valor bilionário para as maiores empresas do mundo — e fontes de vantagem competitiva duradoura para organizações de todos os tamanhos. Consultorias de gestão de marcas e brand strategy ajudam empresas a construir, revitalizar e proteger esse ativo, com metodologias estruturadas que conectam identidade de marca com estratégia de negócio e resultado financeiro.",
    sections=[
        ("A Proposta de Valor da Consultoria de Brand Strategy", "Brand strategy vai além de logo e identidade visual — abrange o posicionamento competitivo da marca, a proposta de valor única, a arquitetura de marca (master brand vs. submarcas), a cultura e os valores que a marca representa, e a experiência consistente que ela entrega em todos os pontos de contato. Empresas que investem em brand strategy estruturado têm maior pricing power (cobram mais pelo mesmo produto), menor CAC (a marca atrai clientes proativamente) e maior fidelização. Consultores que traduzem brand em resultado financeiro têm argumento irresistível."),
        ("Portfólio de Serviços: Do Diagnóstico à Implementação", "Os serviços mais demandados incluem: brand audit (diagnóstico de percepção de marca com pesquisa com consumidores, análise competitiva e benchmarking de marca), desenvolvimento de brand positioning (proposta de valor única, personalidade de marca, território de comunicação), brand architecture (organização de portfólio de marcas para máxima clareza e sinergia), brand guidelines (manual de marca completo), e brand activation (implementação da estratégia nos canais de comunicação e experiência do cliente). Revitalizações de marca (rebranding) são projetos de alto valor e alta visibilidade."),
        ("Metodologias e Frameworks de Brand Strategy", "Os frameworks mais utilizados incluem: Brand Identity Prism (Kapferer), Brand Key (Unilever), Brand Resonance Pyramid (Keller), Jobs-to-be-Done aplicado à marca e o Canvas de Proposta de Valor (Osterwalder). Pesquisas qualitativas (grupos focais, entrevistas de profundidade) e quantitativas (surveys de brand equity, NPS, net sentiment) geram dados que fundamentam as decisões de posicionamento. A combinação de rigor metodológico com criatividade estratégica é o que distingue brand consultants de agências de publicidade."),
        ("Posicionamento e Captação de Clientes", "Consultoras de brand strategy atendem desde startups que constroem marca do zero até grandes corporações em processos de rebranding ou expansão para novos mercados. A captação acontece por: relacionamento com diretores de marketing e CMOs, referências de projetos anteriores, publicações em portfólio com cases de transformação de marca, e presença em eventos de marketing (Fórum CMO, ABAD, ESPM Marketing). Cases com ROI documentado — aumento de brand equity, crescimento de market share, melhora no NPS — são o principal argumento de venda."),
        ("Tendências: Marca com Propósito e Brand Activism", "Marcas que têm posição clara sobre questões sociais e ambientais — diversidade, sustentabilidade, inclusão — constroem conexão mais profunda com consumidores jovens (Millennials e GenZ). O brand activism, quando autêntico e consistente com os valores reais da empresa, cria defensores apaixonados. Quando superficial, gera backlash severo. Consultores de brand strategy têm papel crítico em ajudar empresas a definir o propósito autêntico da marca e a comunicá-lo de forma coerente com a realidade operacional — diferenciando commitment genuíno de greenwashing ou purpose-washing.")
    ],
    faq_list=[
        ("Qual é a diferença entre brand strategy e identidade visual?", "Brand strategy é a camada estratégica: posicionamento competitivo, proposta de valor única, personalidade e valores da marca, arquitetura de portfólio. Identidade visual é a expressão gráfica da estratégia: logo, paleta de cores, tipografia, sistema de design. A identidade visual deve ser derivada da estratégia — não o contrário. Empresas que fazem rebranding apenas visual (novo logo, novas cores) sem revisar a estratégia subjacente frequentemente não obtêm o resultado esperado: a estética muda, mas a percepção de marca permanece igual."),
        ("Quanto tempo leva um projeto de brand strategy completo?", "Um processo de brand strategy completo — da pesquisa ao brand book — leva tipicamente 3-6 meses. Fases principais: imersão e pesquisa (4-6 semanas), análise e síntese de insights (2-3 semanas), desenvolvimento de posicionamento e conceito (4-6 semanas), validação com stakeholders (2-4 semanas) e entrega de brand book e guidelines (2-4 semanas). Projetos de rebranding maior, com mudança de nome ou arquitetura de marca complexa, podem levar 6-12 meses. Projetos menores — refresh de posicionamento para startup — podem ser conduzidos em 8-12 semanas."),
        ("Como medir o valor de uma marca (brand equity)?", "Brand equity pode ser medido por diferentes abordagens: financeira (prêmio de preço que a marca captura sobre genéricos, valor de marca em processos de M&A), de consumidor (Keller CBBE Pyramid — consciência, associações, qualidade percebida, lealdade) e de mercado (participação de mercado, NPS, índices de preferência). Ferramentas como o RepTrak, o BrandZ (WPP/Kantar) e pesquisas de brand tracking mensuram brand equity ao longo do tempo. Para PMEs, métricas mais simples — NPS, taxa de indicação, diferencial de preço sobre concorrentes — são suficientes para monitorar saúde da marca.")
    ]
)

# Update sitemap and trilha
root = pathlib.Path(__file__).parent
slugs = [
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-academia-e-fitness", "Gestão de Negócios de Empresa de B2B SaaS de Gestão de Academia e Fitness"),
    ("gestao-de-clinicas-de-gastroenterologia-e-hepatologia", "Gestão de Clínicas de Gastroenterologia e Hepatologia"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-centros-de-oncologia-integrativa-e-medicina-integrativa", "Vendas para o Setor de SaaS de Gestão de Centros de Oncologia Integrativa e Medicina Integrativa"),
    ("consultoria-de-supply-chain-sustentavel-e-logistica-reversa", "Consultoria de Supply Chain Sustentável e Logística Reversa"),
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-farmacias-e-drogarias", "Gestão de Negócios de Empresa de B2B SaaS de Gestão de Farmácias e Drogarias"),
    ("gestao-de-clinicas-de-ginecologia-e-obstetricia", "Gestão de Clínicas de Ginecologia e Obstetrícia"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-geriatria-e-cuidados-ao-idoso", "Vendas para o Setor de SaaS de Gestão de Clínicas de Geriatria e Cuidados ao Idoso"),
    ("consultoria-de-gestao-de-marcas-e-brand-strategy", "Consultoria de Gestão de Marcas e Brand Strategy"),
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

print("Done — batch 1542")
