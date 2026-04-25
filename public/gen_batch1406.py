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
<footer><p>&copy; 2025 ProdutoVivo &mdash; <a href="/blog/">Blog</a> | <a href="/trilha">Trilha Gratuita</a></p></footer>
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

# Article 4295 — B2B SaaS: gestão de segurança da informação e SIEM/SOC
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-seguranca-da-informacao-e-siem-soc",
    title="Gestão de Negócios para Empresas de B2B SaaS de Segurança da Informação e SIEM/SOC | ProdutoVivo",
    desc="Como escalar um negócio de B2B SaaS de segurança da informação, SIEM e SOC: modelo de receita, go-to-market e diferenciação competitiva.",
    h1="Gestão de Negócios para Empresas de B2B SaaS de Segurança da Informação e SIEM/SOC",
    lead="Segurança da informação é um dos segmentos de SaaS de maior crescimento global, impulsionado pelo aumento de ataques cibernéticos, pela LGPD e por regulamentações setoriais (BACEN, ANVISA, ANS). Empresas de SaaS de SIEM (Security Information and Event Management) e SOC-as-a-Service têm oportunidade de substituir equipes de segurança internas por serviços gerenciados, especialmente em PMEs e médias empresas sem capacidade de manter um SOC próprio.",
    sections=[
        ("Mercado de Cybersecurity SaaS no Brasil", "O mercado brasileiro de segurança da informação cresce a 15% ao ano, com o segmento de serviços gerenciados (MSSP — Managed Security Service Provider) crescendo ainda mais rápido. PMEs e médias empresas são o maior segmento desatendido: 70% não têm equipe dedicada de segurança e dependem de TI generalista para gerenciar ameaças que requerem especialização. SaaS de SIEM e SOC-as-a-Service democratizam o acesso a segurança de nível enterprise para esse segmento."),
        ("Modelo de Receita em Cybersecurity SaaS", "Os modelos mais comuns são: (1) Licença de plataforma SIEM por volume de eventos/dia ou por ativo monitorado (R$ 3 a R$ 15 por ativo/mês); (2) SOC-as-a-Service em retainer mensal — cobrindo monitoramento 24/7, resposta a incidentes e relatórios executivos (R$ 8.000 a R$ 50.000/mês dependendo do porte); (3) Avaliações e pentest sob demanda (R$ 20.000 a R$ 200.000 por projeto). Combine plataforma + serviço gerenciado para maximizar o MRR e reduzir o churn (clientes de SOC gerenciado churnam 5x menos que clientes de plataforma pura)."),
        ("Go-to-Market: CISO, TI e Compliance como Compradores", "O comprador principal é o CISO (Chief Information Security Officer) ou o Diretor de TI. Em empresas reguladas (bancos, operadoras de saúde, seguradoras), o compliance officer tem influência forte — o SIEM é frequentemente requisito de conformidade regulatória (Resolução BACEN 4.658/2018, LGPD). Canais eficientes incluem: integradores de TI (MSSPs menores que revendem a plataforma), associações de segurança (ISACA, ABISEG) e eventos do setor (Mind the Sec, H2HC)."),
        ("Diferenciação: IA e Automação de Resposta a Incidentes", "A IA é o principal driver de diferenciação no mercado de SIEM: detecção de anomalias comportamentais (UEBA — User and Entity Behavior Analytics) que identificam ameaças que regras estáticas não detectam, correlação automática de eventos de múltiplas fontes para reduzir falsos positivos, e SOAR (Security Orchestration, Automation and Response) para automatizar playbooks de resposta a incidentes. Plataformas com IA reduzem o MTTR (Mean Time to Respond) de horas para minutos — um argumento de ROI mensurável."),
        ("Conformidade Regulatória como Driver de Vendas", "Regulamentações como a LGPD, Resolução BACEN 4.658 (segurança cibernética em bancos), RDC ANVISA 204 (sistemas de informação em saúde) e ISO 27001 são os maiores drivers de compra de soluções de segurança no Brasil. Construa playbooks de conformidade por regulação (ex.: 'como o SIEM apoia a conformidade com a Resolução BACEN 4.658') e posicione a plataforma como ferramenta de evidência para auditorias — não apenas como ferramenta de segurança."),
    ],
    faq_list=[
        ("Qual é a diferença entre SIEM, SOC e MSSP?", "SIEM é a tecnologia — plataforma que coleta, correlaciona e analisa logs de segurança de múltiplas fontes para detectar ameaças. SOC (Security Operations Center) é a equipe e o processo — analistas de segurança que monitoram alertas do SIEM e respondem a incidentes. MSSP (Managed Security Service Provider) é o modelo de negócio — empresa que oferece SIEM + SOC como serviço gerenciado para clientes que não têm esses recursos internamente."),
        ("Quanto uma PME deve investir em segurança da informação?", "Benchmarks internacionais (Gartner, Forrester) indicam que empresas devem investir de 8 a 15% do orçamento de TI em segurança. Para PMEs, isso representa R$ 30.000 a R$ 150.000/ano em ferramentas e serviços. O custo médio de um incidente de ransomware no Brasil (downtime + recuperação + multas de LGPD) supera R$ 500.000 — tornando o investimento em segurança claramente justificável pelo risco evitado."),
        ("O que é SOAR e por que é importante para um SaaS de segurança?", "SOAR (Security Orchestration, Automation and Response) é a camada de automação que conecta o SIEM ao restante das ferramentas de segurança (firewall, EDR, ITSM) para automatizar respostas a incidentes. Quando o SIEM detecta um ataque de phishing, o SOAR automaticamente isola a máquina comprometida, bloqueia o IP do atacante no firewall e cria um ticket no ITSM — sem intervenção humana. Isso reduz o MTTR de horas para minutos, sendo o principal diferencial de produtividade para equipes de SOC."),
    ]
)

# Article 4296 — Clinic: ginecologia oncológica e colposcopia
art(
    slug="gestao-de-clinicas-de-ginecologia-oncologica-e-colposcopia",
    title="Gestão de Clínicas de Ginecologia Oncológica e Colposcopia | ProdutoVivo",
    desc="Guia de gestão para clínicas de ginecologia oncológica e colposcopia: estrutura assistencial, rastreamento de câncer ginecológico, faturamento e qualidade.",
    h1="Gestão de Clínicas de Ginecologia Oncológica e Colposcopia",
    lead="A ginecologia oncológica foca na prevenção, diagnóstico e tratamento de cânceres do trato genital feminino — câncer de colo de útero, endométrio, ovário e vulva. Clínicas especializadas nessa área desempenham papel crítico no rastreamento populacional (papanicolau, colposcopia e HPV) e no acompanhamento de pacientes com neoplasias intraepiteliais e cânceres em estágio inicial.",
    sections=[
        ("Portfolio de Serviços em Ginecologia Oncológica", "Uma clínica de ginecologia oncológica oferece: consultas clínicas, coleta de citologia oncótica (papanicolau), colposcopia com biópsia dirigida, histeroscopia diagnóstica e cirúrgica, LEEP/CAF (excisão eletrocirúrgica) para NIC (Neoplasia Intraepitelial Cervical), ultrassonografia transvaginal e solicitação de marcadores tumorais (CA-125, CEA, HE4). A combinação de rastreamento e diagnóstico avançado cria um fluxo contínuo de pacientes em diferentes estágios de acompanhamento."),
        ("Programa de Rastreamento de Câncer de Colo de Útero", "O Ministério da Saúde recomenda o papanicolau a partir dos 25 anos, com periodicidade anual por 2 anos consecutivos e depois trienalmente. Clínicas que implantam um programa de rastreamento ativo — com busca ativa de mulheres com exames em atraso, convênios com empresas e escolas para coleta coletiva e parceria com UBSs para contra-referência — criam um fluxo constante e previsível de novas pacientes. Cada mulher rastreada é uma potencial paciente de longo prazo."),
        ("Colposcopia e Biópsia: Fluxo Clínico e Gestão de Equipamentos", "O colposcópio é o equipamento central da ginecologia oncológica — permite visualização ampliada do colo uterino para identificar lesões suspeitas. A colposcopia com biópsia dirigida é o procedimento de maior rentabilidade (R$ 400 a R$ 1.200 por convênio), mas requer médico treinado com título de colposcopista pela FEBRASGO. Gerencie a agenda de colposcopia para maximizar a taxa de ocupação do colposcópio — cada aparelho suporta 4 a 6 procedimentos por turno."),
        ("Acompanhamento de Pacientes com NIC e Pós-Tratamento", "Pacientes com NIC II/III tratadas com LEEP precisam de seguimento intensivo: papanicolau + colposcopia a cada 6 meses por 2 anos, depois anual por mais 3 anos. Esse protocolo de seguimento de 5 anos gera receita recorrente e previsível por paciente. Implemente um sistema de lembretes automáticos (SMS, WhatsApp) para os exames de seguimento — a taxa de perda de seguimento em NIC é elevada (30 a 50% sem lembrete ativo), comprometendo o resultado clínico e a receita da clínica."),
        ("Captação e Parcerias Estratégicas para Ginecologia Oncológica", "Os principais canais de captação são: ginecologistas gerais (encaminham para colposcopia quando o papanicolau é alterado), UBSs e ambulatórios públicos (contra-referência de casos NIC II/III), laboratórios de citopatologia (que conhecem todas as mulheres com citologia alterada na região) e empresas para programas de saúde da mulher. A parceria com laboratórios citopatológicos — oferecendo colposcopia para mulheres com ASCUS, LSIL ou HSIL — é o canal de referência de maior volume e qualidade."),
    ],
    faq_list=[
        ("Qual é o protocolo atual de rastreamento de câncer de colo de útero no Brasil?", "O INCA recomenda: citologia oncótica dos 25 aos 64 anos, com periodicidade anual nos 2 primeiros anos consecutivos com resultados negativos, depois trienal. Para pacientes com imunossupressão (HIV, transplante, uso crônico de corticoide), o rastreamento é anual e pode incluir teste de HPV de alto risco. O teste de HPV primário (sem associação com papanicolau) ainda não é rotina na rede pública, mas tem evidência científica crescente para substituir ou complementar a citologia."),
        ("Quando uma paciente com papanicolau alterado deve ser encaminhada para colposcopia?", "Segundo as diretrizes FEBRASGO, encaminhar para colposcopia em: ASCUS com teste de HPV positivo para alto risco, LSIL em mulheres acima de 25 anos, HSIL, carcinoma e adenocarcinoma em qualquer situação, e glandular atípico de origem indeterminada. ASCUS com HPV negativo pode repetir a citologia em 12 meses. O encaminhamento correto e oportuno é crítico para o prognóstico — NIC III sem tratamento evolui para câncer invasivo em 10 a 30% dos casos em 5 anos."),
        ("Vale a pena oferecer vacinação contra HPV em uma clínica de ginecologia oncológica?", "Sim, especialmente para adolescentes e jovens adultos não vacinados (9 a 26 anos para meninas; 9 a 14 anos no programa público). A vacinação complementa o rastreamento citológico e representa uma oportunidade de educação das pacientes sobre prevenção do câncer de colo. No particular, as vacinas quadrivalente e nonavalente (Gardasil) têm ticket de R$ 700 a R$ 1.200 por dose — 3 doses para esquema completo — gerando receita significativa com alto valor percebido pela paciente."),
    ]
)

# Article 4297 — SaaS sales: clínicas de pneumologia adulto e função pulmonar
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-pneumologia-adulto-e-funcao-pulmonar",
    title="Vendas para SaaS de Gestão de Clínicas de Pneumologia Adulto e Função Pulmonar | ProdutoVivo",
    desc="Estratégias de vendas para SaaS de gestão de clínicas de pneumologia adulto e função pulmonar: como prospectar, demonstrar valor e fechar contratos.",
    h1="Vendas para SaaS de Gestão de Clínicas de Pneumologia Adulto e Função Pulmonar",
    lead="Clínicas de pneumologia adulto atendem condições respiratórias de alta prevalência — asma, DPOC, apneia do sono, pneumonias de repetição e câncer de pulmão — com um perfil operacional que combina consultas ambulatoriais de alta frequência, exames de função pulmonar complexos e seguimento de pacientes crônicos. Vender SaaS para esse segmento exige entender as particularidades clínicas e operacionais da especialidade.",
    sections=[
        ("Operações de uma Clínica de Pneumologia Adulto", "Uma clínica de pneumologia completa realiza: consultas clínicas (asma, DPOC, fibrose pulmonar, sarcoidose), espirometria forçada com broncodilatador, teste de difusão (DLCO), pletismografia corporal, teste de caminhada de 6 minutos, broncoscopia diagnóstica e terapêutica, e acompanhamento de pacientes em ventilação não-invasiva domiciliar (VNI) e oxigenoterapia de longa duração. Cada exame tem código específico de faturamento e frequência distinta de realização."),
        ("Mapeamento das Dores Operacionais do Pneumologista", "Abra a discovery investigando: como gerenciam os laudos de espirometria (papel ou digital? Integrado ao prontuário?), como controlam os pacientes em oxigenoterapia domiciliar (quem monitora a adesão e o reabastecimento de cilindros?), como faturam DLCO e pletismografia (alta taxa de glosa por documentação incompleta?) e como gerenciam a lista de pacientes aguardando broncoscopia (agenda de sala cirúrgica ou centro cirúrgico externo?). Cada resposta revela uma oportunidade de valor para o SaaS."),
        ("Demo: Espirometria Integrada e Prontuário de Função Pulmonar", "Demonstre: (1) integração com espirómetros (Jaeger, NDD, MIR) para importação automática dos laudos em PDF e dos valores numéricos para o prontuário; (2) prontuário com campos específicos para DPOC (classificação GOLD, CAT score, frequência de exacerbações) e asma (classificação GINA, controle da asma); (3) controle de oxigenoterapia domiciliar (lista de pacientes, receituário de oxigênio, datas de reavaliação); (4) faturamento de espirometria com código TUSS correto e documentação clínica vinculada para evitar glosa."),
        ("Proposta de Valor: Eficiência em Espirometria e Redução de Glosas", "O ROI principal para clínicas de pneumologia vem de: (1) eliminação do tempo de digitalização de laudos de espirometria (2 a 4 horas/semana de tempo técnico economizado); (2) redução de glosas em DLCO e pletismografia (que têm altas taxas de glosa por falta de indicação clínica documentada no prontuário — o SaaS popula automaticamente os campos obrigatórios); (3) aumento da taxa de retorno de pacientes crônicos (DPOC) via lembretes de consulta e exame. Calcule esses ganhos com dados do cliente para personalizar a proposta."),
        ("Expansão para Clínicas do Sono Integradas", "Pneumologistas são frequentemente os responsáveis pelo diagnóstico e tratamento da apneia obstrutiva do sono (SAOS). Clínicas de pneumologia que integram um laboratório de sono (polissonografia) expandem significativamente o portfólio e a receita. Se o SaaS também atende laboratórios de sono (como descrito em conteúdos anteriores), posicione-o como a plataforma que unifica toda a operação respiratória da clínica — da espirometria ao CPAP — em um único prontuário integrado."),
    ],
    faq_list=[
        ("Quais são os principais equipamentos de função pulmonar em uma clínica de pneumologia?", "Os equipamentos essenciais são: espirómetro (mede volumes e fluxos pulmonares — FEV1, CVF, relação FEV1/CVF), sistema de difusão (DLCO — mede a capacidade de transferência gasosa), pletismógrafo corporal (mede volumes pulmonares absolutos — CPT, VR), sistema de teste de caminhada de 6 minutos (oxímetro de pulso calibrado e pista medida) e sistema de pressões respiratórias máximas (PImax e PEmax). Cada equipamento requer calibração diária e manutenção preventiva semestral."),
        ("Como o SaaS pode apoiar o manejo de pacientes com DPOC?", "O prontuário especializado em DPOC deve incluir: registro do estágio GOLD (I a IV pela espirometria + sintomas), score CAT (COPD Assessment Test) em cada consulta, histórico de exacerbações com datas e hospitalização, controle da inaloterapia prescrita (nome, dose, técnica), espirometria anual para monitoramento da progressão e alertas de consulta anual. Esses dados estruturados permitem ao pneumologista identificar pacientes com DPOC de alto risco que precisam de intervenção antes de uma hospitalização."),
        ("Qual é o código TUSS correto para faturamento de espirometria em convênios?", "O código TUSS para espirometria simples é 40602540; para espirometria com broncodilatador (pré e pós) é 40602574; para difusão pulmonar (DLCO) é 40602582; para pletismografia é 40602566. É fundamental documentar no prontuário a indicação clínica e o diagnóstico de cada exame — operadoras frequentemente glosam espirometrias sem CID vinculado ao exame ou sem a indicação clínica descrita no laudo médico de solicitação."),
    ]
)

# Article 4298 — Consulting: gestão de portfólio de produtos
art(
    slug="consultoria-de-gestao-de-portfolio-de-produtos-e-inovacao",
    title="Consultoria de Gestão de Portfólio de Produtos e Inovação | ProdutoVivo",
    desc="Como estruturar e monetizar uma consultoria de gestão de portfólio de produtos e inovação: metodologias, ferramentas de priorização e entregáveis concretos.",
    h1="Consultoria de Gestão de Portfólio de Produtos e Inovação",
    lead="Empresas com múltiplos produtos enfrentam o desafio constante de alocar recursos limitados entre iniciativas concorrentes. Uma consultoria especializada em gestão de portfólio de produtos ajuda organizações a tomar decisões de investimento e desinvestimento baseadas em dados — eliminando projetos zumbi, acelerando apostas de alto potencial e construindo um portfólio equilibrado entre geração de caixa e inovação.",
    sections=[
        ("Diagnóstico do Portfólio Atual: Identificando Desbalanceamentos", "O diagnóstico começa com o mapeamento completo do portfólio em quatro dimensões: posição no ciclo de vida (introdução, crescimento, maturidade, declínio), contribuição financeira (margem e volume de receita por produto), alinhamento estratégico (quanto cada produto contribui para a visão de longo prazo) e recursos alocados (% do orçamento de P&D e comercial por produto). Portfólios desbalanceados geralmente têm excesso de produtos em declínio consumindo recursos que deveriam estar em produtos emergentes."),
        ("Frameworks de Priorização de Portfólio", "Os frameworks mais utilizados são: (1) Matriz BCG (Vaca Leiteira, Estrela, Ponto de Interrogação, Abacaxi) para análise de crescimento × participação de mercado; (2) Matriz de Attrattividade-Competitividade (GE-McKinsey) para portfólios complexos; (3) Bubble Chart de Inovação — posiciona cada projeto no eixo risco × retorno × tempo — para gestão de portfólio de P&D; (4) Weighted Scoring Model (modelo de pontuação ponderada) para comparar projetos em múltiplos critérios estratégicos de forma objetiva."),
        ("Rationalização de Portfólio: Eliminando Produtos Zumbi", "Produtos zumbi são aqueles que continuam no portfólio por inércia — sem volume significativo, com margens negativas ou sem alinhamento estratégico. A consultoria estrutura um processo de descontinuação: análise de rentabilidade real (incluindo custos ocultos de manutenção, suporte e estoque), plano de migração de clientes para produtos substitutos, comunicação estruturada com a base de clientes e liberação de recursos para investimento em produtos de alto potencial. Em média, empresas descobrem que 20 a 30% do portfólio pode ser racionalizado sem impacto material na receita total."),
        ("Gestão de Portfólio de Inovação: Balanceando Horizonte 1, 2 e 3", "O framework de Horizontes de McKinsey classifica iniciativas em: H1 (otimização do core — 70% dos recursos), H2 (extensões e adjacências — 20% dos recursos) e H3 (transformação — 10% dos recursos). A consultoria ajuda a calibrar esse balanço conforme a maturidade e os objetivos estratégicos da empresa. Empresas que apenas investem no H1 ficam vulneráveis à disrupção; as que investem muito no H3 sem sustentação do core comprometem o fluxo de caixa."),
        ("Entregáveis e Monetização da Consultoria de Portfólio", "Projetos de diagnóstico de portfólio custam R$ 80 mil a R$ 250 mil. Redesenho completo de portfólio com roadmap de descontinuação e lançamentos: R$ 200 mil a R$ 600 mil. Implantação de processo de gestão de portfólio (governança, ferramentas, rituais de decisão): R$ 150 mil a R$ 400 mil. Retainer mensal de acompanhamento de portfólio (R$ 20 mil a R$ 60 mil/mês) para empresas que querem suporte contínuo nas decisões de priorização. Indústria, bens de consumo e tecnologia são os setores de maior demanda."),
    ],
    faq_list=[
        ("Como decidir quando descontinuar um produto do portfólio?", "Descontinue quando: o produto tem margem de contribuição negativa por mais de 2 anos consecutivos sem perspectiva de recuperação, representa menos de 1% da receita total e não tem potencial de crescimento nos próximos 3 anos, consome recursos desproporcionais de suporte e manutenção em relação à sua receita, ou compete diretamente com produtos superiores do próprio portfólio sem diferenciação clara. A decisão de descontinuação deve ser baseada em dados financeiros e estratégicos, não em apego emocional ao produto."),
        ("O que é a teoria dos Horizontes de Inovação e como aplicar?", "Desenvolvido pela McKinsey, o modelo de 3 Horizontes classifica o portfólio de inovação em: H1 — iniciativas que melhoram o negócio atual (incremental, retorno em 1-2 anos); H2 — extensões e adjacências ao core (retorno em 2-5 anos); H3 — transformações e disrupções (retorno em 5+ anos). A distribuição ideal de investimentos varia por setor e maturidade da empresa, mas um ponto de partida comum é 70% no H1, 20% no H2 e 10% no H3. Empresas em setores de rápida mudança tecnológica devem alocar mais em H2 e H3."),
        ("Como alinhar o portfólio de produtos com a estratégia corporativa?", "Mapeie cada produto às prioridades estratégicas da empresa (mercados-alvo, proposta de valor, fontes de vantagem competitiva). Produtos que não contribuem para nenhuma prioridade estratégica são candidatos à descontinuação ou desinvestimento. Use um heat map visual que posicione cada produto em relação às prioridades estratégicas e ao potencial de crescimento — isso facilita as conversas de priorização com a alta liderança e torna a decisão de alocação de recursos mais transparente."),
    ]
)

# Article 4299 — B2B SaaS: supply chain management e procurement digital
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-supply-chain-e-procurement-digital",
    title="Gestão de Negócios para Empresas de B2B SaaS de Supply Chain e Procurement Digital | ProdutoVivo",
    desc="Como escalar uma empresa de B2B SaaS de supply chain management e procurement digital: modelo de receita, go-to-market e estratégias de crescimento.",
    h1="Gestão de Negócios para Empresas de B2B SaaS de Supply Chain e Procurement Digital",
    lead="Supply Chain Management (SCM) e Procurement Digital são categorias SaaS de alto valor em rápida adoção no Brasil, impulsionadas pela volatilidade de preços de insumos pós-pandemia, pela busca por eficiência em compras e pela digitalização de cadeias de suprimentos. Empresas de manufatura, varejo, agronegócio e saúde estão investindo massivamente em soluções que aumentem a visibilidade e o controle sobre suas cadeias de abastecimento.",
    sections=[
        ("Mercado de Supply Chain SaaS no Brasil", "O mercado brasileiro de software de supply chain cresce a 18% ao ano, partindo de uma base de penetração ainda baixa. A maioria das empresas de médio porte gerencia compras em planilhas ou em módulos de ERP desatualizados sem visibilidade em tempo real. A pandemia expôs a vulnerabilidade de cadeias monodependentes — isso acelerou a busca por ferramentas de gerenciamento de risco de fornecedores e diversificação de sourcing, criando demanda por SCM SaaS especializado."),
        ("Módulos Principais de um SCM SaaS", "As soluções mais demandadas incluem: (1) Procurement digital (e-procurement) — cotações eletrônicas, homologação de fornecedores, fluxo de aprovação de compras, contratos de fornecimento; (2) Gestão de estoque e armazém (WMS) — controle de entradas e saídas, lotes e validades, inventário cíclico; (3) Planejamento de demanda (demand planning) — forecast baseado em histórico de vendas e sazonalidade; (4) Gestão de transporte (TMS) — rastreamento de cargas, gestão de transportadoras, cálculo de frete. Cada módulo pode ser vendido separadamente ou em bundle."),
        ("Go-to-Market: Gerentes de Compras e Supply Chain", "O comprador principal é o Gerente/Diretor de Compras ou Supply Chain, com validação do CFO (ROI em redução de custos de compra) e do TI (integração com ERP). Em indústrias maiores, há uma área de Procurement com Gerentes de Categoria. Construa cases de ROI por vertical (ex.: 'indústria de alimentos que reduziu o ciclo de compra de 15 para 4 dias e economizou 8% no custo de insumos no primeiro ano') — a especificidade vertical aumenta a credibilidade e a taxa de conversão."),
        ("Diferenciação: Visibilidade e Resiliência da Cadeia", "O maior diferencial competitivo em SCM SaaS hoje é a visibilidade end-to-end — rastrear o status de pedidos e entregas em tempo real, monitorar riscos de fornecedores (financeiro, geopolítico, climático) e receber alertas proativos de disrupção antes que afetem a produção. Adicione funcionalidades de ESG supply chain (emissão de carbono por fornecedor, conformidade com trabalho decente) — crescente requisito de grandes clientes corporativos para aprovação de fornecedores."),
        ("Precificação e Expansão de Receita em SCM SaaS", "O modelo mais comum é por volume de transações (pedidos de compra ou NFs processadas/mês) ou por número de usuários do módulo de procurement. Para WMS, o modelo por galpão ou por SKU gerenciado. Ticket médio: R$ 5.000 a R$ 30.000/mês para PMEs; R$ 50.000 a R$ 200.000/mês para enterprises. A expansão natural ocorre quando o cliente ativa módulos adicionais — um cliente que começa com e-procurement frequentemente expande para WMS e TMS ao longo de 12 a 24 meses."),
    ],
    faq_list=[
        ("Qual é a diferença entre ERP com módulo de compras e um SaaS de procurement dedicado?", "O módulo de compras do ERP é genérico e cobre os processos básicos de P2P (purchase-to-pay). Um SaaS de procurement dedicado oferece: cotações eletrônicas multirronda com lances em tempo real, homologação digital de fornecedores com scoring automático, análise de gasto por categoria (spend analytics), integração com portais de fornecedores e relatórios de conformidade de compras. O SaaS especializado supera o ERP em profundidade funcional e usabilidade para a área de compras."),
        ("Como uma empresa deve começar a digitalizar seu processo de compras?", "Comece pelo mapeamento do processo atual: como as cotações são feitas hoje (e-mail, telefone, planilha?), quantos fornecedores competem por cada categoria, qual é o tempo médio de ciclo de compra (da requisição à entrega) e qual é a taxa de aderência aos preços negociados. Com esse diagnóstico, priorize o módulo de e-procurement (maior ROI imediato em redução de preço de compra por competição eletrônica) como ponto de entrada e expanda gradualmente para os outros módulos."),
        ("O SCM SaaS precisa integrar com o ERP do cliente?", "Sim, a integração com ERP é quase sempre requisito. As integrações essenciais são: (1) recebimento de requisições de compra do ERP → SaaS; (2) envio de pedidos de compra aprovados → ERP para geração de AP (accounts payable); (3) sincronização de cadastro de produtos e fornecedores (mestre de dados); (4) informações de recebimento (NF-e) → ERP para entrada de estoque. Ofereça conectores nativos para SAP, TOTVS, Sankhya e Protheus — os ERPs mais usados no mercado brasileiro de manufatura e varejo."),
    ]
)

# Article 4300 — Clinic: nefrologia ambulatorial e doença renal crônica
art(
    slug="gestao-de-clinicas-de-nefrologia-ambulatorial-e-doenca-renal-cronica",
    title="Gestão de Clínicas de Nefrologia Ambulatorial e Doença Renal Crônica | ProdutoVivo",
    desc="Guia de gestão para clínicas de nefrologia ambulatorial e doença renal crônica: estrutura assistencial, tratamento conservador, faturamento e qualidade clínica.",
    h1="Gestão de Clínicas de Nefrologia Ambulatorial e Doença Renal Crônica",
    lead="A doença renal crônica (DRC) afeta aproximadamente 10% da população brasileira adulta, sendo a hipertensão e o diabetes as principais causas. Clínicas de nefrologia ambulatorial desempenham papel fundamental no tratamento conservador da DRC — retardando a progressão para diálise — e no preparo e acompanhamento de pacientes em programa dialítico e transplantados renais.",
    sections=[
        ("Estrutura de Serviços em Nefrologia Ambulatorial", "Uma clínica de nefrologia ambulatorial oferece: consultas clínicas, avaliação e manejo de hipertensão resistente, tratamento conservador de DRC (dietoterapia, controle pressórico, anemia renal, distúrbio mineral ósseo), preparo para terapia renal substitutiva (TRS — diálise peritoneal, hemodiálise, transplante), acesso vascular (confecção de fístula arteriovenosa em parceria com cirurgião vascular) e acompanhamento de transplantados renais. Cada fase da DRC tem um protocolo específico e um perfil de remuneração distinto."),
        ("Tratamento Conservador da DRC: Equipe Multidisciplinar", "O tratamento conservador da DRC — especialmente nos estágios 3 e 4 (TFGe 15 a 60 ml/min) — é multidisciplinar: nefrologista (prescrição e monitoramento), nutricionista especializada em dieta para renais (restrição de proteína, fósforo, potássio e sódio), farmacêutico clínico (revisão de medicamentos nefrotóxicos) e assistente social (preparo psicossocial para a possibilidade de TRS). Clínicas que oferecem esse cuidado integrado têm melhores resultados clínicos e maior satisfação dos pacientes — e justificam maior remuneração por consulta multidisciplinar."),
        ("Faturamento: APAC de DRC, Convênios e Particular", "O faturamento de nefrologia ambulatorial combina consultas clínicas (convênio ou particular) com procedimentos específicos: APAC de acompanhamento de DRC no SUS (para pacientes em estágios 3-5), biópsia renal percutânea (guiada por US — procedimento de alto valor), e manejo de complicações (acesso peritoneal de cateter Tenckhoff em consulta especializada). Centros que realizam biópsias renais têm receita superior e se tornam referência regional para diagnóstico diferencial de nefropatias."),
        ("Preparo para Diálise e Transplante: Planejamento Longitudinal", "Pacientes com DRC estágio 4 e 5 devem ser preparados antecipadamente para TRS: educação sobre as modalidades (HD, DP, transplante preemptivo), confecção de fístula arteriovenosa pelo menos 6 meses antes da necessidade de hemodiálise, inscrição na lista de transplante renal via SNT (Sistema Nacional de Transplantes) e acompanhamento psicológico para aceitação da TRS. Clínicas que fazem esse preparo estruturado reduzem o início de diálise em caráter de urgência — melhorando os resultados e reduzindo custos hospitalares."),
        ("Captação: Clínicos Gerais, Cardiologistas e Endocrinologistas", "Os principais encaminhadores são: clínicos gerais e médicos de família (identificam proteinúria e elevação de creatinina nos exames de rotina), cardiologistas (hipertensão resistente com comprometimento renal) e endocrinologistas (diabetes com nefropatia diabética). Construa uma rede de referência com esses especialistas — oferecendo protocolo de triagem de DRC simplificado (calculadora de TFGe e ratio albumina:creatinina) para facilitar a identificação e o encaminhamento precoce."),
    ],
    faq_list=[
        ("Quais são os estágios da doença renal crônica e o que significam para a gestão clínica?", "A DRC é classificada pela KDIGO em 5 estágios pela TFGe: G1 (≥90) — normal com marcadores de dano renal; G2 (60-89) — levemente reduzida; G3a (45-59) e G3b (30-44) — moderadamente reduzida; G4 (15-29) — gravemente reduzida; G5 (<15) — falência renal. O estadiamento define a frequência de consultas, o protocolo de tratamento e o planejamento para TRS. Clínicas com sistema de alerta automático por estágio têm melhor continuidade do seguimento."),
        ("Como estruturar um programa de educação em TRS para pacientes com DRC avançada?", "Implante um Programa de Educação Pré-Diálise (EDTNA/ERCA guideline) com sessões educativas em grupo (3 a 5 pacientes) abordando: o que é TRS, diferenças entre HD e DP, o que é transplante renal e como funcionar a lista de espera, impacto da dieta e medicamentos, e aspectos emocionais e sociais da TRS. Sessões em grupo reduzem o custo por paciente, criam suporte mútuo entre os participantes e melhoram a tomada de decisão informada sobre a modalidade de diálise."),
        ("Vale a pena uma clínica de nefrologia realizar biópsias renais ambulatoriais?", "Sim, se houver demanda regional e o nefrologista tiver treinamento adequado em biópsia percutânea guiada por US. A biópsia renal ambulatorial tem vantagens sobre a hospitalar: menor custo, maior conveniência para o paciente e menor tempo de resultado. O investimento em ultrassom de alta resolução e material de biópsia (agulha automática tipo tru-cut) é baixo, e o faturamento por procedimento (R$ 800 a R$ 3.000 por convênio) tem payback rápido em clínicas com 2 a 3 biópsias por semana."),
    ]
)

# Article 4301 — SaaS sales: centros de cirurgia ambulatorial e day hospital
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-centros-de-cirurgia-ambulatorial-e-day-hospital",
    title="Vendas para SaaS de Gestão de Centros de Cirurgia Ambulatorial e Day Hospital | ProdutoVivo",
    desc="Como vender SaaS de gestão para centros de cirurgia ambulatorial e day hospital: abordagem consultiva, demonstração de valor e estratégias de fechamento.",
    h1="Vendas para SaaS de Gestão de Centros de Cirurgia Ambulatorial e Day Hospital",
    lead="Centros de cirurgia ambulatorial (CCAs) e day hospitals são estruturas de saúde que realizam procedimentos cirúrgicos e de alta complexidade sem internação prolongada. Esse modelo reduz custos hospitalares e melhora a experiência do paciente — e está em crescimento acelerado no Brasil, com mais de 2.000 unidades registradas na ANS. A gestão eficiente desses centros requer softwares especializados que integrem agendamento cirúrgico, sala operatória, SADT e faturamento de AIH e APAC.",
    sections=[
        ("Entendendo as Operações de CCAs e Day Hospitals", "Um CCA realiza procedimentos como: cirurgias oftalmológicas (catarata, estrabismo), ortopédicas (artroscopia, pequenas fraturas), ORL (adenoide, amígdala), ginecológicas (histeroscopia, laparoscopia diagnóstica), urológicas (litotripsia, cistoscopia) e gastroenterológicas (endoscopia, colonoscopia). O day hospital realiza procedimentos de maior complexidade com recuperação de 4 a 12 horas: quimioterapia, biópsias de medula, pequenas cirurgias oncológicas. O SaaS deve gerenciar salas cirúrgicas, SRPA (sala de recuperação pós-anestésica) e leitos de day clinic."),
        ("Mapeamento do Decisor em CCAs e Day Hospitals", "O decisor é o diretor clínico ou o administrador do CCA. Em CCAs vinculados a hospitais, envolve também o Superintendente Hospitalar. As prioridades do gestor de CCA são: taxa de ocupação das salas cirúrgicas (meta > 80%), tempo de giro de sala (entre procedimentos — meta < 20 minutos), taxa de cancelamento cirúrgico (meta < 5%) e faturamento de AIH/APAC sem glosa. Esses são os KPIs que devem guiar a demonstração do SaaS."),
        ("Demo: Agenda Cirúrgica e Controle de Sala Operatória", "Demonstre: (1) agenda cirúrgica por sala com visualização de bloqueios por cirurgião e por equipe de anestesia; (2) checklist digital de segurança cirúrgica (OMS) integrado ao prontuário; (3) controle de OPME (Órteses, Próteses e Materiais Especiais) com rastreabilidade de lote por procedimento; (4) registro de tempo de cirurgia, anestesia e recuperação para controle de produtividade; (5) faturamento de AIH para procedimentos do SUS e de conta hospitalar para convênios — com codificação automática de CBHPM/SIGTAP."),
        ("Faturamento de CCAs: AIH, APAC e Conta Hospitalar", "O faturamento de CCAs é complexo: procedimentos do SUS faturados via AIH (Autorização de Internação Hospitalar) ou APAC (alta complexidade e serviços de apoio diagnóstico), com tabelas SIGTAP; procedimentos por convênio faturados via conta hospitalar com tabela CBHPM; e OPME com nota fiscal separada e rastreabilidade obrigatória (código de barras do implante no prontuário). O SaaS deve automatizar esse processo — cada erro de codificação pode resultar em glosa de R$ 500 a R$ 20.000 por procedimento."),
        ("Proposta de Valor: Ocupação de Sala e Redução de Cancelamentos", "O maior impacto financeiro do SaaS em CCAs é no aumento da taxa de ocupação de salas cirúrgicas e na redução de cancelamentos. Demonstre: cada hora de sala cirúrgica ociosa representa R$ 800 a R$ 3.000 de receita perdida; uma redução de 5% na taxa de cancelamento em um CCA com 10 salas e 40 cirurgias/dia representa 2 cirurgias adicionais/dia = R$ 400 a R$ 1.000 adicionais/dia. Mostre como o SaaS reduz cancelamentos por: confirmação automática do paciente 48h antes, checklist de pré-operatório digital e alerta de pendências de autorização de convênio."),
    ],
    faq_list=[
        ("Quais são os requisitos regulatórios para um Centro de Cirurgia Ambulatorial no Brasil?", "CCAs devem seguir a RDC ANVISA 50/2002 (infraestrutura física) e RDC 36/2013 (segurança em serviços de saúde que realizam cirurgia), ter alvará sanitário específico para cirurgia ambulatorial, credenciamento junto às operadoras de saúde e ao SUS (para procedimentos cobertos), implementar o protocolo de cirurgia segura da OMS e manter registro de todos os OPME utilizados com rastreabilidade de lote. A ANVISA realiza inspeções periódicas para renovação do alvará."),
        ("Como o SaaS pode ajudar na gestão de OPME em CCAs?", "O módulo de OPME deve permitir: cadastro de todos os implantes com código ANVISA e lote, vinculação de cada OPME ao procedimento e ao paciente (para recall em caso de alerta do fabricante), controle de estoque consignado (dos fornecedores que deixam material no CCA sem cobrança antecipada), geração automática do termo de OPME para nota fiscal separada e relatórios de consumo por cirurgião e especialidade para negociação de volume com distribuidores."),
        ("Qual é o ticket médio de SaaS para CCAs de pequeno e médio porte?", "Para CCAs com 2 a 4 salas cirúrgicas e 20 a 60 procedimentos/semana, o ticket varia de R$ 2.000 a R$ 6.000/mês. CCAs com 5 a 10 salas, com módulo de faturamento SUS e convênios integrado, chegam a R$ 10.000 a R$ 25.000/mês. Day hospitals com leitos de internação de 4-24h e gestão de quimioterapia ambulatorial integrada podem alcançar R$ 30.000 a R$ 60.000/mês pela plataforma completa."),
    ]
)

# Article 4302 — Consulting: gestão de saúde e bem-estar corporativo
art(
    slug="consultoria-de-gestao-de-saude-e-bem-estar-corporativo",
    title="Consultoria de Gestão de Saúde e Bem-estar Corporativo | ProdutoVivo",
    desc="Como estruturar e escalar uma consultoria de gestão de saúde e bem-estar corporativo: programas de wellness, ROI de saúde e estratégias de engajamento de colaboradores.",
    h1="Consultoria de Gestão de Saúde e Bem-estar Corporativo",
    lead="Saúde e bem-estar corporativo migrou de benefício secundário para prioridade estratégica nas empresas que competem por talentos. Programas bem estruturados de saúde corporativa reduzem o absenteísmo, aumentam a produtividade e diminuem os custos com plano de saúde. Consultorias especializadas nessa área têm demanda crescente em empresas de todos os portes — com crescimento acelerado pós-pandemia pela consciência de saúde mental e física no ambiente de trabalho.",
    sections=[
        ("O Que Abrange a Consultoria de Saúde Corporativa", "A consultoria estrutura: (1) Diagnóstico de saúde populacional — análise do perfil epidemiológico dos colaboradores (utilizando dados anonimizados do plano de saúde), identificando as principais causas de afastamento e sinistralidade; (2) Design de programa de saúde e bem-estar — escolha de intervenções baseadas em evidência (rastreamento preventivo, gestão de crônicos, saúde mental, atividade física); (3) Implantação e gestão — plataformas de saúde digital, parcerias com clínicas e academias; (4) Medição de ROI — impacto em sinistralidade, absenteísmo e produtividade."),
        ("Diagnóstico de Saúde Populacional: Mapeando o Perfil de Risco", "O diagnóstico usa dados anonimizados e agregados do plano de saúde (sinistros por CID, utilização por faixa etária, custo por procedimento) e pesquisas de saúde com os colaboradores (estilo de vida, fatores de risco, saúde mental). O output é um perfil epidemiológico que revela: principais causas de custo no plano (doenças crônicas — hipertensão, diabetes, doenças cardiovasculares — respondem por 70 a 80% do custo em empresas maduras), grupos de alto risco e oportunidades de intervenção preventiva com maior potencial de redução de custo."),
        ("Programas de Saúde Baseados em Evidência", "As intervenções com maior ROI comprovado incluem: (1) Gestão de crônicos — acompanhamento de colaboradores com hipertensão, diabetes e dislipidemia por enfermeiro e médico dedicado, com exames e medicação facilitados (reduz hospitalização em 30 a 50%); (2) Saúde mental — programas de mindfulness, acesso facilitado à psicoterapia (EAP) e treinamento de líderes em saúde mental (reduz afastamentos por transtornos mentais em 25 a 40%); (3) Atividade física — subsídio de academia, grupos de corrida corporativa e desafios de passo (reduz obesidade e doenças cardiometabólicas)."),
        ("ROI de Saúde Corporativa: Calculando o Retorno", "O ROI de programas de saúde corporativa é medido em: redução de sinistralidade do plano de saúde (cada ponto percentual de redução na sinistralidade de um plano de R$ 10 milhões representa R$ 100 mil economizados), redução de absenteísmo (1 dia de falta de um colaborador custa entre 1,5 e 3x o custo diário de seu salário em perda de produtividade), redução de presenteísmo (trabalhadores adoentados presentes são 30 a 50% menos produtivos) e melhora do eNPS — saúde é o 3º benefício mais valorizado por colaboradores."),
        ("Estrutura Comercial e Entregáveis da Consultoria de Saúde", "Projetos de diagnóstico epidemiológico custam R$ 60 mil a R$ 200 mil. Design e implantação de programa de saúde: R$ 150 mil a R$ 500 mil. Gestão contínua do programa em retainer (monitoramento de indicadores, gestão de fornecedores de saúde, comunicação com colaboradores): R$ 20 mil a R$ 80 mil/mês. Parcerias com operadoras de saúde (que patrocinam programas de saúde para reduzir sua própria sinistralidade) são um modelo de co-financiamento que pode reduzir o custo do programa para a empresa-cliente."),
    ],
    faq_list=[
        ("Como medir o ROI de um programa de bem-estar corporativo?", "Defina métricas antes do programa: taxa de sinistralidade do plano de saúde (custo sinistros / prêmio pago), taxa de absenteísmo médico (dias de afastamento por colaborador/ano), resultado de pesquisa de saúde (% colaboradores com fatores de risco como obesidade, sedentarismo, tabagismo) e NPS de benefícios. Meça novamente após 12 e 24 meses. Programas bem gerenciados atingem ROI de R$ 2 a R$ 6 economizados para cada R$ 1 investido, com o maior retorno vindo da redução de hospitalização de crônicos."),
        ("Quais são os primeiros programas de saúde corporativa a implantar em uma empresa?", "Para empresas que estão começando, priorize pela relação impacto/custo: (1) Rastreamento preventivo anual (check-up executivo para todos os colaboradores — identifica riscos antes de virar sinistro); (2) Gestão de hipertensão e diabetes (as duas condições que mais geram custo no plano de saúde e absenteísmo); (3) Acesso à saúde mental (EAP com psicoterapia e apoio em crise — especialmente relevante pós-pandemia). Esses três programas têm evidência científica sólida de ROI positivo em 12 a 24 meses."),
        ("Como engajar colaboradores em programas de saúde e bem-estar?", "As estratégias de maior engajamento incluem: gamificação (desafios de passos, pontuação por participação em ações de saúde com recompensas), comunicação hiperpersonalizada (cada colaborador recebe comunicação baseada no seu perfil de risco), incentivos financeiros (desconto na coparticipação do plano para quem participa do programa de gestão de crônicos), liderança como modelo (diretores e gerentes participam visivelmente dos programas) e conveniência (exames na empresa, academia parceira próxima, teleconsulta disponível). Programas com essas características atingem 60 a 80% de engajamento."),
    ]
)

# ── sitemap.xml ───────────────────────────────────────────────────────────────
content = open('public/sitemap.xml').read()
new_urls = (
    '<url><loc>https://produtovivo.com.br/blog/gestao-de-negocios-de-empresa-de-b2b-saas-de-seguranca-da-informacao-e-siem-soc/</loc></url>'
    '<url><loc>https://produtovivo.com.br/blog/gestao-de-clinicas-de-ginecologia-oncologica-e-colposcopia/</loc></url>'
    '<url><loc>https://produtovivo.com.br/blog/vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-pneumologia-adulto-e-funcao-pulmonar/</loc></url>'
    '<url><loc>https://produtovivo.com.br/blog/consultoria-de-gestao-de-portfolio-de-produtos-e-inovacao/</loc></url>'
    '<url><loc>https://produtovivo.com.br/blog/gestao-de-negocios-de-empresa-de-b2b-saas-de-supply-chain-e-procurement-digital/</loc></url>'
    '<url><loc>https://produtovivo.com.br/blog/gestao-de-clinicas-de-nefrologia-ambulatorial-e-doenca-renal-cronica/</loc></url>'
    '<url><loc>https://produtovivo.com.br/blog/vendas-para-o-setor-de-saas-de-gestao-de-centros-de-cirurgia-ambulatorial-e-day-hospital/</loc></url>'
    '<url><loc>https://produtovivo.com.br/blog/consultoria-de-gestao-de-saude-e-bem-estar-corporativo/</loc></url>'
)
open('public/sitemap.xml', 'w').write(content.replace('</urlset>', new_urls + '</urlset>'))

# ── trilha.html ───────────────────────────────────────────────────────────────
content = open('public/trilha.html').read()
new_items = (
    '<li><a href="/blog/gestao-de-negocios-de-empresa-de-b2b-saas-de-seguranca-da-informacao-e-siem-soc/">Gestao De Negocios De Empresa De B2b Saas De Seguranca Da Informacao E Siem Soc</a></li>\n'
    '<li><a href="/blog/gestao-de-clinicas-de-ginecologia-oncologica-e-colposcopia/">Gestao De Clinicas De Ginecologia Oncologica E Colposcopia</a></li>\n'
    '<li><a href="/blog/vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-pneumologia-adulto-e-funcao-pulmonar/">Vendas Para O Setor De Saas De Gestao De Clinicas De Pneumologia Adulto E Funcao Pulmonar</a></li>\n'
    '<li><a href="/blog/consultoria-de-gestao-de-portfolio-de-produtos-e-inovacao/">Consultoria De Gestao De Portfolio De Produtos E Inovacao</a></li>\n'
    '<li><a href="/blog/gestao-de-negocios-de-empresa-de-b2b-saas-de-supply-chain-e-procurement-digital/">Gestao De Negocios De Empresa De B2b Saas De Supply Chain E Procurement Digital</a></li>\n'
    '<li><a href="/blog/gestao-de-clinicas-de-nefrologia-ambulatorial-e-doenca-renal-cronica/">Gestao De Clinicas De Nefrologia Ambulatorial E Doenca Renal Cronica</a></li>\n'
    '<li><a href="/blog/vendas-para-o-setor-de-saas-de-gestao-de-centros-de-cirurgia-ambulatorial-e-day-hospital/">Vendas Para O Setor De Saas De Gestao De Centros De Cirurgia Ambulatorial E Day Hospital</a></li>\n'
    '<li><a href="/blog/consultoria-de-gestao-de-saude-e-bem-estar-corporativo/">Consultoria De Gestao De Saude E Bem Estar Corporativo</a></li>'
)
open('public/trilha.html', 'w').write(content.replace('</ul>', new_items + '\n</ul>', 1))

print("Done — batch 1406")
