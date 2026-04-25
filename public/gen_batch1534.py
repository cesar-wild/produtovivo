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

# Article 4551 — B2B SaaS: legal management / legal tech
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-juridica-e-legal-tech",
    title="Gestão de Negócios de Empresa de B2B SaaS de Gestão Jurídica e Legal Tech",
    desc="Como construir e escalar uma empresa de B2B SaaS de gestão jurídica e legal tech no Brasil: produto, diferenciação, go-to-market e estratégias de crescimento rentável.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Gestão Jurídica e Legal Tech",
    lead="O setor jurídico brasileiro está em transformação acelerada: mais de 1 milhão de advogados, escritórios de todos os portes e departamentos jurídicos corporativos buscam soluções tecnológicas para gestão de processos, contratos, compliance e automação de documentos. O mercado de Legal Tech no Brasil é enorme e ainda fragmentado, criando oportunidade para SaaS especializados com proposta de valor clara.",
    sections=[
        ("Dimensionando o Mercado de Legal Tech no Brasil", "O Brasil tem mais de 1,3 milhão de advogados registrados na OAB e dezenas de milhares de escritórios de advocacia — do solo prático ao escritório com centenas de sócios. Além disso, empresas de médio e grande porte mantêm departamentos jurídicos internos (In-house) que gerenciam contratos, litígios e compliance. Legal Tech abrange: gestão de processos judiciais, CLM (Contract Lifecycle Management), automação de documentos, due diligence assistida por IA, e plataformas de resolução online de disputas."),
        ("Produto: Gestão de Processos, CLM e Automação", "Para escritórios de advocacia, as funcionalidades core incluem: gestão de prazos processuais (integração com sistemas do Judiciário via web scraping ou APIs do CNJ), gestão de clientes e casos (CRM jurídico), controle financeiro de honorários e contingências, e automação de documentos (petições, contratos, pareceres) com templates configuráveis. Para departamentos jurídicos corporativos, CLM (gestão do ciclo de vida de contratos) é a prioridade: repositório centralizado, alertas de vencimento, fluxo de aprovação e analytics de portfólio de contratos."),
        ("Inteligência Artificial no Setor Jurídico", "IA está transformando o trabalho jurídico: revisão automática de contratos (identificação de cláusulas de risco, desvios de padrão), pesquisa jurisprudencial assistida (busca semântica em decisões de tribunais), predição de resultados processuais (com base em histórico de decisões por tipo de caso, juiz e comarca), e geração de minutas e resumos com LLMs. SaaS que incorporam IA jurídica responsável — com rastreabilidade das fontes e revisão humana obrigatória — têm diferencial competitivo crescente."),
        ("Go-to-Market: Escritórios vs. Corporativo", "O mercado se divide em dois segmentos com dinâmicas distintas: escritórios de advocacia (volume alto, ticket médio a alto, foco em gestão de processos e honorários, decisão rápida do sócio principal) e departamentos jurídicos corporativos (volume menor, ticket alto, foco em CLM e compliance, ciclo de venda longo com procurement e TI envolvidos). Escritórios são melhor adquiridos via inbound, eventos da OAB e referências entre advogados. Corporativos exigem vendas enterprise consultivas e RFPs."),
        ("Métricas de Negócio e Retenção em Legal Tech", "Legal Tech tem naturalmente alta stickiness: escritórios que inserem todos os processos e dados de clientes em um sistema dificilmente migram. As métricas mais relevantes são ARR, NRR (esperado alto para jurídico), CAC por segmento e time-to-value (quanto tempo leva para o advogado ver valor real no sistema). O principal risco de churn é o onboarding: escritórios que não concluem a migração de dados históricos tendem a abandonar o produto nas primeiras semanas.")
    ],
    faq_list=[
        ("O que é CLM e por que é prioritário para departamentos jurídicos corporativos?", "CLM (Contract Lifecycle Management) é a gestão integrada do ciclo de vida de contratos: da solicitação e minuta à negociação, aprovação, assinatura digital, execução e renovação. Departamentos jurídicos corporativos gerenciam centenas ou milhares de contratos simultâneos — sem CLM, contratos vencem sem renovação, cláusulas comprometedoras passam despercebidas e o tempo de advogados é consumido em buscas manuais. CLM transforma contratos em ativo gerenciado estrategicamente."),
        ("Legal Tech com IA pode substituir advogados?", "Não — e o posicionamento correto de Legal Tech é de augmentation, não de substituição. IA agiliza tarefas repetitivas (revisão de contratos padrão, pesquisa jurisprudencial, geração de minutas simples), liberando advogados para trabalho de maior valor: estratégia processual, negociação, aconselhamento jurídico complexo e relacionamento com clientes. Escritórios que adotam IA jurídica responsavelmente entregam mais valor com a mesma equipe — não reduzem advogados."),
        ("Como um SaaS jurídico se integra com os tribunais brasileiros?", "Os tribunais brasileiros disponibilizam consulta de processos via Diário da Justiça eletrônico, portais de consulta pública e, progressivamente, APIs do CNJ (DataJud). SaaS jurídicos fazem monitoramento de prazos via scraping dos portais de cada tribunal ou via integração com serviços como o JusBrasil e Escavador, que centralizam dados processuais de múltiplos tribunais. A integração com o e-SAJ (TJ-SP) e o PJe é estratégica para os maiores mercados estaduais.")
    ]
)

# Article 4552 — Clinic management: rheumatology / autoimmune diseases
art(
    slug="gestao-de-clinicas-de-reumatologia-e-doencas-autoimunes",
    title="Gestão de Clínicas de Reumatologia e Doenças Autoimunes",
    desc="Guia prático para gestão de clínicas de reumatologia e doenças autoimunes: estrutura clínica, gestão de pacientes crônicos, medicamentos biológicos e estratégias de crescimento.",
    h1="Gestão de Clínicas de Reumatologia e Doenças Autoimunes",
    lead="Clínicas de reumatologia atendem pacientes com artrite reumatoide, lúpus eritematoso sistêmico, espondiloartropatias, síndrome de Sjögren, esclerodermia e outras doenças autoimunes de caráter crônico e sistêmico. A gestão dessas clínicas exige acompanhamento longitudinal cuidadoso, manejo de medicamentos de alto custo (biológicos e imunossupressores) e equipe preparada para o impacto sistêmico das doenças reumáticas.",
    sections=[
        ("Perfil Epidemiológico e Demanda por Reumatologia", "Doenças reumáticas afetam mais de 15 milhões de brasileiros, mas a reumatologia é uma especialidade com oferta restrita de profissionais — principalmente no interior do país. Artrite reumatoide sozinha afeta cerca de 1,3 milhão de pessoas no Brasil, e a prevalência de doenças autoimunes aumenta com o envelhecimento da população. A demanda reprimida por consultas reumatológicas é estrutural e cria oportunidade para clínicas bem posicionadas expandirem sua capacidade de atendimento."),
        ("Fluxo Clínico e Gestão de Pacientes Crônicos", "Pacientes reumatológicos necessitam de acompanhamento regular: consultas trimestrais a semestrais para avaliação de atividade de doença, ajuste terapêutico, monitoração de toxicidade de medicamentos (hemograma, função hepática e renal para metotrexato, hidroxicloroquina e biológicos), e avaliação de comorbidades (cardiovascular, osteoporose, saúde ocular). Prontuários com índices de atividade de doença (DAS-28 para AR, SLEDAI para lúpus, BASDAI para espondilite) estruturados são essenciais para acompanhamento objetivo."),
        ("Gestão de Medicamentos Biológicos e de Alto Custo", "Biológicos para artrite reumatoide (anti-TNF como adalimumabe, etanercepte; abatacepte; rituximabe; tocilizumabe) e para outras doenças autoimunes têm custo mensal de R$3.000-15.000 por paciente. O acesso via plano de saúde exige laudos detalhados, comprovação de falha a DMARDs sintéticos convencionais e renovações periódicas. Via SUS, o CEAF (Componente Especializado da Assistência Farmacêutica) cobre vários biológicos mediante protocolo específico do Ministério da Saúde. Gestão documental rigorosa é fundamental para garantir o acesso."),
        ("Telemedicina e Ampliação do Alcance em Reumatologia", "A reumatologia é especialidade com escassez geográfica severa — pacientes do interior podem esperar meses por consulta presencial. Telemedicina permite ao reumatologista urbano atender pacientes de outras regiões, com consultas de acompanhamento remotas para casos estáveis e sem inflamação articular ativa. Parcerias com centros de infusão locais — para aplicação de biológicos IV prescritos pelo reumatologista via telemedicina — ampliam o alcance sem exigir presença física do especialista."),
        ("Marketing e Captação via Rede de Encaminhamentos", "Reumatologia é especialidade de encaminhamento: clínicos gerais, médicos de família, ortopedistas e ginecologistas identificam sinais de doença autoimune e referenciam para o especialista. Construir relacionamento com esses profissionais — visitas, eventos de atualização, newsletter com casos clínicos — é a estratégia de captação mais eficaz. Conteúdo educativo sobre sintomas de artrite, lúpus e fibromialgia para o público leigo em redes sociais cria consciência e captação direta de pacientes com suspeita diagnóstica.")
    ],
    faq_list=[
        ("Qual a diferença entre artrite reumatoide e artrose (osteoartrite)?", "Artrite reumatoide é uma doença autoimune sistêmica: o sistema imune ataca as articulações causando inflamação, dor, rigidez matinal e destruição articular progressiva se não tratada. Afeta principalmente articulações pequenas das mãos e pés, simetricamente. Osteoartrite (artrose) é degenerativa: desgaste da cartilagem articular com o envelhecimento, sobrecarga ou trauma, sem componente autoimune significativo. O tratamento é completamente diferente — reumatologista trata AR; ortopedista e reumatologista tratam artrose."),
        ("Os medicamentos biológicos para artrite reumatoide têm cobertura obrigatória pelos planos de saúde?", "Biológicos incluídos no PCDT (Protocolo Clínico e Diretrizes Terapêuticas) do Ministério da Saúde têm cobertura obrigatória pelos planos de saúde conforme resolução da ANS, desde que o paciente cumpra os critérios do protocolo (falha a pelo menos dois DMARDs sintéticos). Planos mais limitados (ambulatoriais) podem ter cobertura restrita — pacientes com plano insuficiente frequentemente recorrem à via judicial ou ao CEAF do SUS."),
        ("Como o índice DAS-28 é utilizado no acompanhamento de artrite reumatoide?", "O DAS-28 (Disease Activity Score com 28 articulações) é uma ferramenta padronizada que mede a atividade da artrite reumatoide combinando número de articulações edemaciadas e dolorosas, VHS ou PCR e avaliação global do paciente. Escore abaixo de 2,6 indica remissão, entre 2,6-3,2 baixa atividade, acima de 5,1 alta atividade. Acompanhar o DAS-28 em cada consulta objetifica a avaliação clínica, justifica decisões terapêuticas e documenta a resposta ao tratamento — essencial para laudos de biológicos.")
    ]
)

# Article 4553 — SaaS sales for centros: plastic / reconstructive surgery
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-centros-de-cirurgia-plastica-e-reparadora",
    title="Vendas para o Setor de SaaS de Gestão de Centros de Cirurgia Plástica e Reparadora",
    desc="Estratégias de vendas B2B de SaaS para centros de cirurgia plástica e reparadora: perfil do comprador, proposta de valor, ciclo de vendas e como crescer nesse nicho especializado.",
    h1="Vendas para o Setor de SaaS de Gestão de Centros de Cirurgia Plástica e Reparadora",
    lead="O Brasil é líder mundial em número de cirurgias plásticas realizadas anualmente, com mais de 1,5 milhão de procedimentos por ano. Centros de cirurgia plástica estética e reparadora combinam consultórios de alta sofisticação, salas cirúrgicas próprias ou em clínicas dia, e gestão de pacientes em jornadas pré e pós-operatórias meticulosas. SaaS especializado cria valor real em cada etapa dessa cadeia.",
    sections=[
        ("O Mercado Brasileiro de Cirurgia Plástica", "O Brasil realiza mais cirurgias plásticas por habitante do que qualquer outro país do mundo. Lipoaspiração, mamoplastia, rinoplastia, blefaroplastia e abdominoplastia lideram o volume, mas há crescimento significativo em procedimentos reparadores (reconstrução mamária pós-mastectomia, correção de deformidades congênitas, grandes queimados). Cirurgiões plásticos trabalham tanto em consultórios privados quanto em hospitais e clínicas dia — e todos necessitam de gestão eficiente do ciclo paciente."),
        ("Proposta de Valor do SaaS para Cirurgia Plástica", "As principais necessidades de gestão em cirurgia plástica são: fotodocumentação padronizada do paciente (fotos pré e pós-operatórias com protocolo de posicionamento), consentimento informado digital específico por procedimento, gestão do fluxo pré-operatório (avaliação clínica, exames pré-anestésicos, liberação do anestesista), agendamento de sala cirúrgica, controle de OPME (implantes mamários, próteses, materiais de sutura especiais) e acompanhamento pós-operatório estruturado com registro de curativo e evolução."),
        ("Abordagem Comercial ao Cirurgião Plástico", "O cirurgião plástico é proprietário do consultório e decisor único. É profissional muito ocupado — cirurgias longas, consultas densas — e valoriza extremamente a praticidade e a agilidade do suporte. A abordagem mais eficaz é direta e focada na dor: 'Como você registra hoje as fotos pré e pós dos seus pacientes? Como controla os termos de consentimento?' Sistemas de fotodocumentação padronizada são frequentemente o hook inicial — uma funcionalidade que gera 'uau' imediato e abre a conversa para o restante do produto."),
        ("Fotodocumentação e Segurança Jurídica em Cirurgia Plástica", "Fotodocumentação sistemática — com fotos padronizadas em ângulos específicos por procedimento, data e hora registradas, vinculadas ao prontuário do paciente — é ao mesmo tempo ferramenta clínica (avaliação de resultado, comparação pré/pós) e proteção jurídica (em caso de litígio, comprova o resultado obtido e a qualidade do procedimento). Cirurgiões que perderam ações por ausência de documentação adequada são os mais receptivos a sistemas que resolvem essa fragilidade."),
        ("Expansão para Clínicas Dia e Anestesistas Parceiros", "Cirurgiões plásticos que operam em clínicas dia próprias têm necessidades adicionais: gestão da sala cirúrgica (blocos de tempo, compatibilidade de cirurgias), coordenação com anestesistas parceiros (escalas, disponibilidade), controle de materiais do centro cirúrgico e faturamento dos procedimentos. Um SaaS que abraça esse ecossistema — incluindo módulo para anestesistas e para a gestão do centro cirúrgico — cria valor de plataforma que vai muito além do sistema de consultório individual.")
    ],
    faq_list=[
        ("Cirurgias plásticas estéticas têm cobertura por planos de saúde?", "Cirurgias estéticas (realizadas exclusivamente por motivo estético) não têm cobertura obrigatória por planos de saúde. Cirurgias reparadoras — reconstrução mamária pós-mastectomia (obrigatória por lei federal 9.797/1999), correção de deformidades congênitas, cirurgias após acidentes, cirurgia bariátrica e suas consequências (remoção de excesso de pele) — têm cobertura obrigatória conforme rol da ANS. A distinção estética vs. reparadora é frequentemente objeto de disputas com operadoras."),
        ("Como SaaS de fotodocumentação se diferencia de usar o celular ou câmera convencional?", "Sistemas de fotodocumentação específicos para cirurgia plástica oferece: protocolo de ângulos padronizados com guia visual na tela (garantindo consistência entre fotos pré e pós), vinculação automática ao prontuário do paciente com data/hora e assinatura digital, armazenamento criptografado conforme LGPD, busca por paciente e comparação lado a lado pré/pós, e rastreabilidade completa de acesso. Celulares armazenam fotos fora do prontuário, sem controle de acesso, misturadas com fotos pessoais — uma fragilidade jurídica e de privacidade."),
        ("O que são OPME em cirurgia plástica e como gerenciar?", "OPME (Órteses, Próteses e Materiais Especiais) em cirurgia plástica incluem principalmente próteses de silicone mamário, próteses de glúteo, expansores, telas de reparo de hérnias em abdominoplastia e materiais de fixação. Cada OPME deve ter registro ANVISA, rastreabilidade de lote, termo de consentimento específico e registro no prontuário. Para procedimentos cobertos por convênio, a OPME deve ser autorizada previamente — processo que um SaaS de gestão organiza e agiliza significativamente.")
    ]
)

# Article 4554 — Consulting: cybersecurity / information security risk
art(
    slug="consultoria-de-gestao-de-riscos-ciberneticos-e-seguranca-da-informacao",
    title="Consultoria de Gestão de Riscos Cibernéticos e Segurança da Informação",
    desc="Como estruturar uma consultoria de gestão de riscos cibernéticos e segurança da informação: serviços, metodologias, captação de clientes e entrega de valor em um mercado de alta demanda.",
    h1="Consultoria de Gestão de Riscos Cibernéticos e Segurança da Informação",
    lead="Com ataques de ransomware a hospitais e infraestrutura crítica, vazamentos de dados milionários e a LGPD exigindo demonstração de proteção de dados pessoais, a demanda por consultoria de segurança da informação e gestão de riscos cibernéticos nunca foi tão alta no Brasil. Empresas de todos os setores precisam de especialistas que ajudem a avaliar, mitigar e gerenciar ameaças cibernéticas antes que se tornem incidentes.",
    sections=[
        ("Panorama de Ameaças e Oportunidade de Mercado", "O Brasil é um dos países mais atacados do mundo em cibercrimes: ataques de ransomware a hospitais, empresas de energia e infraestrutura crítica crescem a cada ano; phishing e BEC (Business Email Compromise) causam prejuízos bilionários. A LGPD (Lei 13.709/2018) impõe responsabilidade jurídica às organizações por vazamentos de dados pessoais, criando incentivo financeiro e regulatório para investimento em segurança da informação. Consultorias especializadas têm backlog crescente e mercado em expansão estrutural."),
        ("Portfólio de Serviços: Do Diagnóstico à Resposta a Incidentes", "Os serviços mais demandados incluem: assessment de maturidade de segurança (baseado em frameworks como NIST CSF, CIS Controls, ISO 27001), pentest (testes de penetração autorizados para identificar vulnerabilidades), gestão de vulnerabilidades, implementação de SOC (Security Operations Center), DLP (Data Loss Prevention), gestão de identidade e acesso (IAM), treinamento de conscientização em segurança para colaboradores, resposta a incidentes (IR) e forense digital pós-ataque. LGPD compliance e privacidade de dados são serviços de grande demanda no momento."),
        ("Metodologias e Frameworks de Referência", "O mercado de segurança tem frameworks consagrados: ISO 27001/27002 para sistemas de gestão de segurança, NIST Cybersecurity Framework para avaliação de maturidade, CIS Controls para priorização de controles técnicos, MITRE ATT&CK para mapeamento de táticas e técnicas de ataque, e OWASP para segurança de aplicações web. Consultores que dominam múltiplos frameworks e sabem selecionar o mais adequado para cada contexto (regulado, financeiro, saúde, industrial) têm diferencial significativo."),
        ("Posicionamento e Captação de Clientes", "A captação em segurança da informação ocorre principalmente por: licitações e RFPs de grandes empresas e governo, relacionamento com CISOs e equipes de TI, eventos setoriais (CISO Summit, Mind the Sec, Roadsec, BSides), e indicação de incidentes recentes. Especializações verticais — saúde (HIPAA, LGPD em dados sensíveis), financeiro (BACEN Resolução 4.658, PCI-DSS), governo (LGPD no setor público, ISMS governamental) — aumentam a relevância e o ticket médio. Provas de conceito em projetos menores (assessment inicial) são a porta de entrada mais eficaz."),
        ("Modelo de Negócio e Remuneração", "Consultorias de segurança trabalham com projetos de escopo definido (pentest, assessment ISO 27001, resposta a incidentes) e contratos de serviço contínuo: vCISO (CISO virtual, R$15-50k/mês), monitoramento de SOC, gestão de vulnerabilidades contínua. Certificações reconhecidas (CISSP, CEH, CISM, OSCP, ISO 27001 Lead Auditor) são credenciais essenciais para posicionamento e cobrança de honorários premium. O mercado ainda tem déficit de profissionais qualificados — quem tem expertise documentada não falta trabalho.")
    ],
    faq_list=[
        ("O que é um pentest e quando uma empresa deve realizá-lo?", "Pentest (teste de penetração) é uma simulação controlada de um ataque cibernético, realizada por profissionais autorizados para identificar vulnerabilidades antes que atacantes reais as explorem. Deve ser realizado: antes do lançamento de sistemas críticos, após mudanças significativas na infraestrutura, anualmente como prática de higiene de segurança, e imediatamente após suspeita de comprometimento. É serviço obrigatório para certificações como PCI-DSS e fortemente recomendado pela ISO 27001."),
        ("A LGPD exige que empresas tenham consultor de segurança da informação?", "A LGPD exige que organizações que processam dados pessoais em larga escala nomeiem um DPO (Data Protection Officer / Encarregado de Dados) e adotem medidas técnicas e administrativas de segurança adequadas ao risco. A lei não especifica quais medidas, criando demanda por consultores que ajudem a interpretar o que é 'adequado' para cada contexto. A ANPD (Autoridade Nacional de Proteção de Dados) pode investigar e multar organizações com medidas insuficientes."),
        ("Qual a diferença entre segurança da informação e cibersegurança?", "Segurança da informação é o conceito mais amplo: proteger informações em qualquer forma (digital, física, verbal) contra confidencialidade, integridade e disponibilidade comprometidas. Cibersegurança é um subconjunto focado especificamente na proteção de sistemas digitais, redes e dados em ambientes conectados. Na prática, as áreas se sobrepõem enormemente, e a maioria das consultorias abrange ambas — mas algumas se especializam em OT security (tecnologia operacional), segurança de nuvem ou segurança de aplicações.")
    ]
)

# Article 4555 — B2B SaaS: real estate management / proptech
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-imobiliaria-e-proptech",
    title="Gestão de Negócios de Empresa de B2B SaaS de Gestão Imobiliária e Proptech",
    desc="Como construir e escalar uma empresa de B2B SaaS de gestão imobiliária e proptech no Brasil: produto, mercado, diferenciação, go-to-market e estratégias de crescimento sustentável.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Gestão Imobiliária e Proptech",
    lead="O mercado imobiliário brasileiro é um dos maiores da América Latina e está em plena digitalização. Imobiliárias, administradoras de condomínios, incorporadoras e gestores de fundos imobiliários buscam soluções SaaS que otimizem captação de imóveis, gestão de contratos, relacionamento com inquilinos e proprietários, e análise de portfólio. O espaço de Proptech no Brasil ainda tem enorme margem de crescimento.",
    sections=[
        ("Panorama do Mercado de Proptech no Brasil", "O setor imobiliário representa cerca de 13% do PIB brasileiro, com mais de 40.000 imobiliárias e centenas de administradoras de imóveis e condomínios. A digitalização avança em todos os segmentos: portais de anúncio (Zap, VivaReal, OLX) digitalizaram a busca; assinatura digital (DocuSign, ClickSign) eliminou papel nos contratos; sistemas de gestão de condomínio (Sinco, Super Lógica, Albatross) automatizaram boletos e assembleias. Mas ainda há muito espaço para soluções especializadas."),
        ("Produto: CRM Imobiliário, Gestão de Contratos e Administração", "O CRM imobiliário é o núcleo para imobiliárias: gestão de carteira de imóveis, funil de captação de clientes, agendamento e registro de visitas, propostas e contratos digitais. Para administradoras de imóveis (locação), as funcionalidades prioritárias são gestão de contratos de locação, emissão de boletos, repasse para proprietários, vistoria digital de entrada e saída, e portal para inquilinos e proprietários. Para condomínios: portal do condômino, gestão de assembleia virtual, ocorrências e orçamentos de serviços."),
        ("Go-to-Market e Segmentação do Mercado Imobiliário", "O mercado imobiliário se divide em segmentos com dinâmicas distintas: imobiliárias de compra e venda (foco em CRM de vendas e captação de imóveis), administradoras de locação (foco em automação de cobranças e relacionamento com proprietários/inquilinos), incorporadoras (foco em gestão de empreendimentos e vendas de lançamento), e gestão de condomínios (foco em portal do morador, assembleias e contratos de manutenção). Cada segmento tem necessidades e compradores distintos — foco inicial em um segmento é a estratégia mais eficaz."),
        ("Integrações e Ecossistema Proptech", "Integrações essenciais para Proptech no Brasil incluem: portais de anúncio (Zap, VivaReal) via XML/API para publicação automática de imóveis, sistemas de assinatura digital (ClickSign, DocuSign), plataformas de cobrança e split de pagamento (Iugu, Pagar.me), bureaus de crédito para análise de inquilinos (Serasa, SPC, Quod), e sistemas de gestão de construtoras para administração de lançamentos imobiliários. O ecossistema é rico e a posição de hub integrador agrega valor."),
        ("Tendências e Oportunidades Emergentes em Proptech", "Tendências que criam novas oportunidades incluem: iBuying (compra e revenda direta de imóveis com avaliação algorítmica), tokenização imobiliária (cotas de imóveis em blockchain), aluguel por temporada gerenciado (concorrência com Airbnb), home staging virtual com IA (tour 3D e fotografia imobiliária automatizada) e gestão de FIIs (Fundos de Investimento Imobiliário) com analytics de portfólio. Startups de Proptech que antecipam essas tendências e constroem produto antes da demanda massiva se tornam líderes de mercado.")
    ],
    faq_list=[
        ("Qual a diferença entre software de gestão imobiliária para imobiliária e para administradora de condomínio?", "São segmentos com necessidades completamente distintas. Software para imobiliária foca em captação de imóveis, gestão de leads de compradores/locatários, funil de negócios e contratos de compra/locação. Software para condomínio foca em emissão de boletos de condomínio, rateio de despesas, gestão de funcionários (porteiros, zeladores), assembleias virtuais e comunicação com moradores. Muitas empresas tentam atender ambos com o mesmo produto — mas os compradores, funcionalidades e preços são muito diferentes."),
        ("Como Proptech pode usar IA para avaliação automatizada de imóveis (AVM)?", "AVM (Automated Valuation Model) usa dados de transações imobiliárias históricas, características do imóvel (área, localização, padrão de acabamento, andar) e variáveis de mercado (taxa de juros, demanda regional) para estimar o valor de mercado com algoritmos de machine learning. No Brasil, a escassez de dados transacionais públicos é um desafio — mas portais como Zap e VivaReal acumularam enormes bases históricas. AVMs são usados por fintechs imobiliárias, bancos para avaliação de garantias e plataformas de iBuying."),
        ("O que é assinatura eletrônica de contratos imobiliários e qual sua validade jurídica no Brasil?", "Assinatura eletrônica tem validade jurídica no Brasil pela MP 2.200-2/2001 e pela Lei 14.063/2020. Existem três níveis: simples (login + senha), avançada (com biometria ou certificado eletrônico privado) e qualificada (com certificado digital ICP-Brasil). Para contratos imobiliários de locação, assinatura eletrônica simples ou avançada tem validade suficiente. Para escrituras de compra e venda, ainda há exigência de reconhecimento em cartório — embora haja avanços na digitalização do processo notarial.")
    ]
)

# Article 4556 — Clinic management: infectious diseases / complex infections
art(
    slug="gestao-de-clinicas-de-infectologia-e-doencas-infecciosas-complexas",
    title="Gestão de Clínicas de Infectologia e Doenças Infecciosas Complexas",
    desc="Guia prático para gestão de clínicas de infectologia e doenças infecciosas complexas: estrutura clínica, gestão de patologias crônicas, HIV, hepatites e estratégias de crescimento.",
    h1="Gestão de Clínicas de Infectologia e Doenças Infecciosas Complexas",
    lead="Clínicas de infectologia atendem pacientes com HIV/AIDS, hepatites virais, tuberculose, infecções fúngicas sistêmicas e outras doenças infecciosas de alta complexidade. Além do atendimento clínico especializado, essas clínicas frequentemente têm papel de referência regional, coordenando com serviços de saúde pública e garantindo acesso a medicamentos e tratamentos de alto custo.",
    sections=[
        ("Perfil de Atendimento em Clínicas de Infectologia", "Infectologistas atendem um espectro amplo de condições: desde infecções agudas graves (meningite, endocardite, abscessos de difícil manejo) que requerem avaliação hospitalar pontual, até doenças crônicas de longa duração — HIV/AIDS, hepatite C crônica, HTLV, histoplasmose disseminada em imunodeprimidos. O perfil de pacientes crônicos — HIV em TARV, hepatites B e C em tratamento — gera uma carteira estável de acompanhamento ambulatorial com consultas regulares e exames periódicos de monitoração."),
        ("Gestão de Pacientes com HIV em TARV", "Pessoas vivendo com HIV (PVHIV) em terapia antirretroviral (TARV) necessitam de acompanhamento semestral com carga viral e contagem de CD4, avaliação de adesão ao tratamento, monitoração de efeitos adversos (dislipidemia, resistência à insulina, toxicidade renal e hepática dos ARVs), vacinações específicas e rastreamento de infecções oportunistas e comorbidades (tuberculose latente, HPV, hepatites virais coinfecções). Prontuários com histórico de esquemas ARV, mutações de resistência e resultados longitudinais de carga viral são essenciais."),
        ("Hepatites Virais: Tratamento e Acesso a Medicamentos", "A hepatite C crônica hoje tem cura com antivirais de ação direta (AAD) — sofosbuvir/daclatasvir, sofosbuvir/velpatasvir — com taxa de resposta virológica sustentada de 95-99%. O acesso via SUS (CEAF) requer diagnóstico confirmado, genotipagem e avaliação de fibrose hepática (elastografia ou biópsia). Clínicas de infectologia e hepatologia coordenam esse processo — com gestão documental cuidadosa para garantir o acesso ao tratamento e acompanhamento pós-cura."),
        ("Biossegurança e Precauções de Controle de Infecção", "Clínicas de infectologia têm exigências específicas de biossegurança: sala de espera com ventilação adequada para pacientes bacilíferos (TB pulmonar), precauções de contato para doenças multirresistentes, protocolos de descarte de resíduos infectantes (Grupo A da PGRSS), e treinamento da equipe para precauções padrão e precauções específicas. A conformidade com a RDC ANVISA 222/2018 para gerenciamento de resíduos de saúde e com as normas ABNT de biossegurança são requisitos operacionais."),
        ("Marketing e Posição de Referência Regional", "Clínicas de infectologia constroem reputação por especialidade e complexidade de casos atendidos. A captação vem principalmente de encaminhamentos hospitalares (casos difíceis de identificar durante internação), de serviços de saúde pública (SAEs — Serviços de Assistência Especializada em HIV) que fazem referência para casos complexos, e de médicos de família que identificam infecções fora do seu escopo de manejo. A atuação como referência regional ou estadual em um tipo específico de infecção (micoses endêmicas, infecções por parasitos raros, doenças importadas) diferencia a clínica.")
    ],
    faq_list=[
        ("O tratamento de HIV e hepatite C pode ser obtido gratuitamente pelo SUS?", "Sim. O Brasil tem um dos programas públicos de HIV mais respeitados do mundo: todos os medicamentos antirretrovirais (ARVs) são fornecidos gratuitamente pelo SUS via UDMs (Unidades Dispensadoras de Medicamentos). Para hepatite C, os antivirais de ação direta (sofosbuvir/daclatasvir e sofosbuvir/velpatasvir) são fornecidos pelo CEAF mediante diagnóstico e protocolo clínico. A clínica privada complementa com consultas especializadas, exames e manejo de complicações."),
        ("Como funciona a contagem de CD4 no acompanhamento do HIV?", "CD4 são linfócitos T auxiliadores — células do sistema imune que o HIV progressivamente destrói. A contagem de CD4 indica o estado do sistema imune: acima de 500/mm³ é considerado normal, abaixo de 200/mm³ define AIDS. Com TARV eficaz, a carga viral cai a indetectável e o CD4 se recupera. O monitoramento semestral de carga viral e CD4 guia decisões sobre TARV e profilaxias de infecções oportunistas — documentado no prontuário longitudinal do paciente."),
        ("Qual a diferença entre hepatite B e hepatite C no contexto do tratamento e acompanhamento?", "Hepatite B não tem cura com os tratamentos atuais, mas pode ser controlada com análogos nucleosídeos (tenofovir, entecavir) que suprimem o vírus indefinidamente — tratamento longo ou vitalício. Hepatite C tem cura com AADs em 8-12 semanas de tratamento — uma revolução terapêutica recente. Ambas requerem monitoração de fibrose hepática (risco de cirrose e hepatocarcinoma) e rastreamento de complicações com ultrassonografia e AFP semestral em casos de cirrose estabelecida.")
    ]
)

# Article 4557 — SaaS sales for clinics: orthopedics / traumatology
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-ortopedia-e-traumatologia",
    title="Vendas para o Setor de SaaS de Gestão de Clínicas de Ortopedia e Traumatologia",
    desc="Estratégias de vendas B2B de SaaS para clínicas de ortopedia e traumatologia: perfil do comprador, proposta de valor, ciclo de vendas, objeções e como crescer nesse nicho.",
    h1="Vendas para o Setor de SaaS de Gestão de Clínicas de Ortopedia e Traumatologia",
    lead="A ortopedia e traumatologia é uma das especialidades cirúrgicas mais demandadas no Brasil, combinando alta rotatividade de consultas, procedimentos ambulatoriais, cirurgias eletivas e atendimentos de urgência. Clínicas ortopédicas têm necessidades específicas de gestão — controle de OPME (implantes metálicos, próteses articulares), imagens de raio-X e RM integradas ao prontuário, e acompanhamento pós-operatório estruturado — que criam oportunidade para SaaS especializado.",
    sections=[
        ("Conhecendo a Operação de Clínicas de Ortopedia", "Clínicas de ortopedia atendem desde consultas de primeiro atendimento para lesões agudas (entorses, fraturas, rupturas ligamentares) até pacientes crônicos com artrose, escoliose, pé diabético e patologias do manguito rotador. A gestão inclui: agendamento diferenciado (consultas curtas de retorno vs. primeiras consultas com anamnese detalhada), integração com serviços de imagem (laudos de raio-X, tomografia e ressonância no prontuário), controle de gessoteca e órteses, e agendamento de centro cirúrgico para procedimentos eletivos."),
        ("Proposta de Valor do SaaS para Ortopedia", "As funcionalidades mais valorizadas incluem: prontuário ortopédico com diagramas corporais para marcação de lesões, visualizador de imagens DICOM integrado (raio-X, tomografia, RM diretamente no prontuário sem exportar para CD), controle de OPME por cirurgia (placas, parafusos, próteses com rastreabilidade de lote e número de série), agenda com diferenciação de tipo de consulta, modelo de prontuário por queixa principal (ombro, joelho, coluna, quadril) e fotodocumentação de feridas cirúrgicas no pós-operatório."),
        ("Perfil do Decisor e Abordagem de Vendas", "O ortopedista proprietário de clínica é decidido e prático — valoriza demonstrações objetivas que mostrem como o sistema economiza seu tempo. Perguntas de abertura eficazes: 'Como você visualiza hoje as imagens de raio-X durante a consulta?', 'Como você controla quais implantes foram usados em cada cirurgia?', 'Como é seu pós-operatório — você consegue ver rapidamente a evolução de um paciente de cirurgia de quadril feita há 3 meses?' Cada resposta revela uma dor que o SaaS endereça diretamente."),
        ("Gestão de OPME em Ortopedia: Uma Dor Real e Cara", "OPME em ortopedia inclui implantes de alta complexidade e alto custo: sistemas de osteossíntese (placas e parafusos de titânio), implantes de coluna vertebral (cages, parafusos pediculares), próteses de joelho e quadril (R$15.000-60.000 por conjunto). A gestão inadequada gera: perda de rastreabilidade (risco legal e sanitário), cirurgias realizadas sem implante autorizado pelo convênio (glosa garantida), ou estoque de implantes descartados após validade. SaaS que resolve esses problemas tem ROI imediato e inegável."),
        ("Expansão para Esporte e Medicina do Esporte", "Muitas clínicas de ortopedia têm subespecialidade em medicina do esporte — atendendo atletas amadores e profissionais. Esse segmento tem características específicas: protocolos de retorno ao esporte pós-lesão, avaliação funcional com testes específicos (Hop Test, Y-Balance, FMS), periodização da reabilitação com fisioterapeuta e preparador físico. SaaS que suporte esses protocolos diferenciados amplia o valor para clínicas que atendem o público esportivo — um segmento de alto ticket e alta lealdade.")
    ],
    faq_list=[
        ("Como SaaS pode ajudar a reduzir glosas de OPME em clínicas de ortopedia?", "Glosas de OPME ocorrem quando: o implante não foi previamente autorizado pelo convênio, o código TUSS faturado não corresponde ao implante utilizado, a rastreabilidade de lote está incompleta, ou a nota fiscal do OPME não acompanhou a guia. Um SaaS que integra o controle de OPME ao faturamento — confirmando autorização antes da cirurgia, associando lote ao procedimento e gerando a guia com os códigos corretos — elimina as causas mais comuns de glosa de OPME."),
        ("O que é um visualizador DICOM e por que é importante para uma clínica de ortopedia?", "DICOM é o formato padrão de imagens médicas (raio-X, tomografia, RM, ultrassom). Um visualizador DICOM integrado ao prontuário permite ao ortopedista abrir a imagem diretamente no sistema durante a consulta, fazer medições (ângulos de Cobb para escoliose, ângulo de Wiberg para quadril), comparar exames ao longo do tempo e importar laudos. Sem integração, o médico depende de CDs físicos ou sistemas separados — perda de tempo e risco de exame errado sendo visualizado."),
        ("Clínicas de ortopedia menores (2-3 médicos) precisam de SaaS especializado?", "Sim — especialmente pelo controle de OPME e de imagens. Mesmo clínicas pequenas realizam cirurgias com implantes que exigem rastreabilidade. A diferença é o ticket e as funcionalidades do plano: clínicas pequenas se beneficiam de planos básicos com prontuário ortopédico, controle de OPME e agenda, sem necessidade de módulos avançados de analytics ou integração com sistemas hospitalares complexos. O ponto de entrada acessível é estratégico para ganhar mercado de volume.")
    ]
)

# Article 4558 — Consulting: digital transformation for industry / Industry 4.0
art(
    slug="consultoria-de-transformacao-digital-para-industrias-e-industria-4-0",
    title="Consultoria de Transformação Digital para Indústrias e Indústria 4.0",
    desc="Como estruturar uma consultoria de transformação digital para indústrias e Indústria 4.0: serviços, metodologias, captação de clientes industriais e entrega de resultados mensuráveis.",
    h1="Consultoria de Transformação Digital para Indústrias e Indústria 4.0",
    lead="A Indústria 4.0 — com IoT industrial, manufatura inteligente, gêmeos digitais, robótica colaborativa e IA aplicada à produção — está reconfigurando a competitividade industrial global. No Brasil, indústrias de todos os portes buscam consultores que ajudem a navegar essa transformação de forma estruturada, priorizando investimentos com maior impacto e integrando tecnologias sem paralisar a operação.",
    sections=[
        ("Contexto da Transformação Industrial no Brasil", "A indústria brasileira enfrenta pressão crescente de competitividade: custos de energia e mão de obra, concorrência de importados e exigências crescentes de sustentabilidade e rastreabilidade de cadeias. A digitalização da produção — via MES (Manufacturing Execution System), IoT industrial (IIoT), PLCs e SCADA conectados, e analytics de chão de fábrica — é a resposta estratégica para aumentar produtividade, reduzir desperdício e ganhar flexibilidade. O gap de adoção entre líderes e seguidores cria oportunidade para consultores que dominam o caminho."),
        ("Portfólio de Serviços de Consultoria Industrial 4.0", "Os serviços mais demandados incluem: diagnóstico de maturidade digital (Industry 4.0 Maturity Index, IMPULS Foundation), mapeamento de fluxo de valor com identificação de oportunidades de automação e digitalização, implementação de IIoT (sensores, PLCs, gateways, plataformas de dados), projetos de gêmeo digital para simulação de linha de produção, implementação de MES, analytics de OEE (Overall Equipment Effectiveness) em tempo real, e programas de capacitação de operadores e lideranças para a cultura digital."),
        ("Metodologias: Lean 4.0 e Roadmap de Digitalização", "A abordagem mais eficaz combina Lean Manufacturing (eliminação de desperdício, melhoria contínua) com tecnologias digitais — o chamado Lean 4.0 ou Smart Lean. O diagnóstico começa pelo mapeamento de fluxo de valor (VSM) para identificar onde a digitalização agrega mais impacto. O roadmap de digitalização prioriza projetos por ROI esperado e viabilidade técnica, criando uma trajetória de quick wins nos primeiros 6-12 meses que constroem confiança para investimentos maiores."),
        ("Captação de Clientes Industriais e Credibilidade", "A captação de projetos industriais passa por: associações setoriais (FIESP, CNI, FIERGS), agências de fomento à inovação (SENAI, SEBRAE, FINEP), eventos industriais (HANNOVER MESSE Brasil, Expo Manufactura, Automação Industrial Brasil) e relacionamento com fabricantes de equipamentos (Siemens, Rockwell, Schneider Electric) que indicam consultores de digitalização. Cases documentados — com métricas de produtividade, OEE e redução de custos — são o principal ativo de marketing para indústrias."),
        ("Modelos de Remuneração e Tipos de Engajamento", "Projetos de transformação industrial variam de diagnósticos focados (R$50-200k) a programas de digitalização de 12-24 meses (R$500k-5M+ para grandes fábricas). O modelo de fee by results — honorário parcialmente atrelado à melhoria de OEE ou redução de desperdício — é cada vez mais demandado por diretores industriais que querem garantia de entrega. Contratos de sustentação pós-implantação (R$20-60k/mês) para manutenção de sistemas digitais e evolução contínua do roadmap garantem receita recorrente.")
    ],
    faq_list=[
        ("O que é OEE e por que é a métrica central da Indústria 4.0?", "OEE (Overall Equipment Effectiveness) mede a eficiência real de equipamentos de produção combinando Disponibilidade (percentual do tempo que o equipamento operou quando deveria), Performance (velocidade real vs. velocidade nominal) e Qualidade (percentual de peças boas). OEE de 85% é considerado world class; a média da indústria fica em 60-65%. Cada ponto percentual de melhoria em OEE representa ganho direto de capacidade produtiva sem investimento em novos equipamentos — o ROI mais imediato da digitalização industrial."),
        ("O que é um gêmeo digital (digital twin) e como beneficia indústrias?", "Um gêmeo digital é uma réplica virtual de um ativo físico (máquina, linha de produção, fábrica inteira) alimentada por dados em tempo real de sensores IoT. Permite simular mudanças antes de implementá-las no mundo real (novos produtos, novos processos), monitorar o dessgaste e prever falhas com manutenção preditiva, otimizar parâmetros de processo para maximizar qualidade e minimizar consumo de energia. É a tecnologia com maior potencial de impacto em produtividade para grandes instalações industriais."),
        ("Como uma indústria de médio porte deve iniciar sua jornada de digitalização?", "O ponto de partida mais eficaz é um projeto piloto de IIoT com coleta de dados de OEE em uma célula de produção crítica. Com dados reais de disponibilidade, performance e qualidade, o time de produção visualiza perdas pela primeira vez de forma estruturada — e o ROI da digitalização torna-se tangível. A partir desse piloto, o roadmap se constrói com confiança: onde expandir a coleta de dados, quais algoritmos aplicar e quais integrações com ERP priorizar.")
    ]
)

# Update sitemap and trilha
root = pathlib.Path(__file__).parent
slugs = [
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-juridica-e-legal-tech", "Gestão de Negócios de Empresa de B2B SaaS de Gestão Jurídica e Legal Tech"),
    ("gestao-de-clinicas-de-reumatologia-e-doencas-autoimunes", "Gestão de Clínicas de Reumatologia e Doenças Autoimunes"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-centros-de-cirurgia-plastica-e-reparadora", "Vendas para o Setor de SaaS de Gestão de Centros de Cirurgia Plástica e Reparadora"),
    ("consultoria-de-gestao-de-riscos-ciberneticos-e-seguranca-da-informacao", "Consultoria de Gestão de Riscos Cibernéticos e Segurança da Informação"),
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-imobiliaria-e-proptech", "Gestão de Negócios de Empresa de B2B SaaS de Gestão Imobiliária e Proptech"),
    ("gestao-de-clinicas-de-infectologia-e-doencas-infecciosas-complexas", "Gestão de Clínicas de Infectologia e Doenças Infecciosas Complexas"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-ortopedia-e-traumatologia", "Vendas para o Setor de SaaS de Gestão de Clínicas de Ortopedia e Traumatologia"),
    ("consultoria-de-transformacao-digital-para-industrias-e-industria-4-0", "Consultoria de Transformação Digital para Indústrias e Indústria 4.0"),
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

print("Done — batch 1534")
