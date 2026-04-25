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

# Article 4383 — B2B SaaS: cibersegurança e gestão de identidade e acesso
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-ciberseguranca-e-gestao-de-identidade-e-acesso",
    title="Gestão de Negócios para SaaS de Cibersegurança e Gestão de Identidade e Acesso | ProdutoVivo",
    desc="Como escalar um SaaS de cibersegurança e IAM (Identity and Access Management) no Brasil: produto, vendas para CISOs e retenção.",
    h1="Gestão de Negócios para SaaS de Cibersegurança e Gestão de Identidade e Acesso",
    lead="Cibersegurança é um dos mercados de maior crescimento no Brasil, impulsionado por ataques ransomware, exigências da LGPD e a expansão da superfície de ataque com trabalho remoto e cloud. SaaS de cibersegurança com foco em IAM (Identity and Access Management) atendem uma das necessidades mais críticas das organizações modernas.",
    sections=[
        ("Mercado de Cibersegurança e IAM no Brasil",
         "O Brasil é um dos países mais atacados por ransomware e phishing no mundo — e o investimento em cibersegurança cresce proporcionalmente, superando R$ 12 bilhões ao ano. IAM (Gestão de Identidade e Acesso) é a camada fundamental de qualquer arquitetura de segurança: controla quem tem acesso a quais sistemas, com qual nível de permissão e com que autenticação. SSO (Single Sign-On), MFA (Multi-Factor Authentication), PAM (Privileged Access Management) e RBAC (Role-Based Access Control) são as funcionalidades centrais dessa categoria."),
        ("Posicionamento de Produto em Cibersegurança SaaS",
         "O espectro de produtos de cibersegurança é amplo. Para um SaaS nacional se posicionar, é necessário escolher um nicho: IAM para PMEs (SSO + MFA com onboarding simplificado), PAM para proteção de acesso privilegiado (administradores de sistemas, DBAs), CASB (Cloud Access Security Broker) para gestão de shadow IT e acesso a SaaS corporativo, ou gestão de vulnerabilidades e patching. O diferencial competitivo de produtos nacionais é frequentemente o suporte em português, conformidade específica com LGPD e integração com sistemas locais como Active Directory e diretórios de RH brasileiros."),
        ("Vendas para CISOs e Times de Segurança",
         "O comprador de soluções de cibersegurança é o CISO (Chief Information Security Officer) ou o gerente de segurança da informação. A venda é técnica e consultiva — o comprador avalia funcionalidades específicas, compatibilidade com a arquitetura existente e postura de segurança do próprio produto. Provas de conceito (POCs) com dados e usuários reais são indispensáveis. Canais de distribuição eficientes: integradores de segurança (MSSPs — Managed Security Service Providers), VADs (Value-Added Distributors) especializados em segurança e participação em eventos como Security Summit e Cyber Security Summit Brasil."),
        ("Compliance com LGPD e Regulatórios Setoriais",
         "LGPD (Lei Geral de Proteção de Dados) é um driver de compra crescente: a lei exige que organizações controlem o acesso a dados pessoais, registrem quem acessou o quê e quando, e implementem medidas técnicas de proteção. IAM é a camada técnica que viabiliza o cumprimento desses requisitos. Adicionalmente, setores regulados como financeiro (BACEN 4.658/2018), saúde (ANVISA, CFM) e defesa têm exigências específicas de controle de acesso. SaaS de IAM com funcionalidades específicas para conformidade regulatória têm argumento de venda mais forte nesses setores."),
        ("Modelos de Negócio e Crescimento em Cibersegurança SaaS",
         "Precificação comum em IAM SaaS: por usuário/mês (R$ 15-50 por usuário para PME, R$ 50-200 para enterprise com funcionalidades avançadas), com camadas de preço baseadas em funcionalidades (MFA apenas vs. SSO + MFA + PAM). Contratos anuais com desconto de 15-25% vs. mensal são padrão no segmento. A expansão de receita acontece por aumento de usuários (crescimento natural do cliente) e módulos adicionais (do MFA básico para PAM enterprise). NRR acima de 120% é comum em SaaS de segurança bem gerenciados — clientes raramente saem de soluções de IAM implantadas."),
    ],
    faq_list=[
        ("O que é MFA e por que é considerado a proteção mais eficaz contra invasões de conta?",
         "MFA (Multi-Factor Authentication) exige que o usuário prove sua identidade com dois ou mais fatores independentes: algo que ele sabe (senha), algo que ele tem (token, app autenticador, SMS) e algo que ele é (biometria). Estudos do Google e Microsoft mostram que MFA bloqueia mais de 99,9% de ataques automatizados de comprometimento de conta — mesmo quando a senha do usuário está vazada. É a contramedida com melhor relação custo-benefício em cibersegurança."),
        ("O que é PAM (Privileged Access Management) e por que é crítico?",
         "PAM controla o acesso de usuários privilegiados — administradores de sistemas, DBAs, DevOps — que têm permissões amplas em sistemas críticos. O roubo ou abuso de credenciais privilegiadas é a causa de mais de 80% dos incidentes de segurança graves. PAM resolve isso com: cofre de senhas para credenciais privilegiadas (vault), gravação de sessões privilegiadas (sessão recording), aprovação de acesso just-in-time (acesso apenas quando necessário e por tempo limitado) e análise de comportamento anômalo de usuários privilegiados."),
        ("LGPD exige que empresas implementem controles específicos de IAM?",
         "A LGPD não especifica tecnologias, mas exige medidas técnicas e administrativas para proteger dados pessoais contra acessos não autorizados (Art. 46). Na prática, a implementação de IAM — especialmente MFA para acesso a sistemas com dados pessoais, RBAC para limitar o acesso por função e logs de auditoria de acesso — é a forma mais direta de demonstrar conformidade com esse artigo. A ANPD (Autoridade Nacional de Proteção de Dados) avalia medidas técnicas adotadas em investigações de incidentes."),
    ]
)

# Article 4384 — Clinic: cirurgia bariátrica e metabólica multidisciplinar
art(
    slug="gestao-de-clinicas-de-cirurgia-bariatrica-e-metabolica-multidisciplinar",
    title="Gestão de Clínicas de Cirurgia Bariátrica e Metabólica Multidisciplinar | ProdutoVivo",
    desc="Como gerenciar clínicas de cirurgia bariátrica e metabólica: equipe multidisciplinar, protocolos pré e pós-operatórios, OPME e sustentabilidade financeira.",
    h1="Gestão de Clínicas de Cirurgia Bariátrica e Metabólica Multidisciplinar",
    lead="Cirurgia bariátrica e metabólica é uma das áreas de maior crescimento da cirurgia no Brasil, com mais de 72.000 procedimentos realizados por ano. Clínicas especializadas precisam gerenciar equipes multidisciplinares extensas, protocolos rigorosos de preparo e acompanhamento, e processos de autorização complexos com convênios.",
    sections=[
        ("Panorama da Cirurgia Bariátrica no Brasil",
         "O Brasil é o 2º país do mundo em número de cirurgias bariátricas realizadas, atrás apenas dos EUA. A obesidade afeta mais de 26% dos adultos brasileiros, criando uma demanda crescente por intervenção cirúrgica — especialmente para pacientes com IMC acima de 35 com comorbidades (DM2, HAS, apneia, dislipidemia) ou IMC acima de 40. O bypass gástrico em Y de Roux (BGYR) e o sleeve gástrico são os procedimentos mais realizados. A cirurgia metabólica para DM2 com IMC entre 30 e 35 está ganhando reconhecimento e indicações baseadas em evidências."),
        ("Equipe Multidisciplinar Obrigatória e Fluxo de Preparo",
         "A resolução CFM 2.131/2015 exige equipe multidisciplinar para cirurgia bariátrica: cirurgião bariátrico, clínico geral ou endocrinologista, nutricionista com experiência em bariátrica, psicólogo ou psiquiatra (avaliação psicológica pré-operatória obrigatória) e anestesiologista habilitado para cirurgia de alto risco. O preparo pré-operatório inclui: perda de peso pré-cirúrgica, controle de comorbidades, endoscopia digestiva alta, polissonografia (SAOS é muito prevalente em obesos), ecocardiograma e avaliações multidisciplinares com no mínimo 6 meses de acompanhamento."),
        ("Gestão de OPME e Materiais Cirúrgicos Bariátricos",
         "Os materiais cirúrgicos utilizados em cirurgia bariátrica laparoscópica incluem: grampeador linear (stapler) com cargas específicas para diferentes espessuras de tecido, trocárteres de 5 e 12mm, fio de sutura de reforço de grampo (Peri-Strips, SeamGuard), balão intragástrico (para casos de preparo pré-cirúrgico ou tratamento conservador inicial) e malha para hérnia hiatal (frequentemente presente em candidatos à bariátrica). O custo de OPME por procedimento varia de R$ 5.000 a R$ 15.000 dependendo dos materiais utilizados e da complexidade técnica."),
        ("Acompanhamento Pós-operatório de Longo Prazo",
         "O acompanhamento pós-bariátrica é tão importante quanto a cirurgia: retornos programados em 1 semana, 1 mês, 3 meses, 6 meses e anualmente por toda a vida. A suplementação vitamínica e mineral é obrigatória e vitalícia (polivitamínico, cálcio, vitamina D, B12, ferro — em doses superiores ao recomendado para população geral). Monitoramento de doenças relacionadas à absorção (anemia, hipoproteinemia, hipovitaminose D, hiperparatireoidismo secundário) por exames laboratoriais periódicos. Grupos de apoio pós-bariátrica (presenciais ou online) aumentam a adesão às mudanças de comportamento."),
        ("Faturamento, Convênios e Sustentabilidade Financeira",
         "A cirurgia bariátrica tem cobertura obrigatória pelo rol ANS para indicações específicas (IMC ≥ 40 ou IMC ≥ 35 com comorbidades). O processo de autorização com convênios envolve: relatório da equipe multidisciplinar, confirmação de 2 anos de tratamento conservador prévio (exigência de muitos convênios), laudos de comorbidades e documentação completa de todos os profissionais envolvidos. O prazo de autorização varia de 15 a 60 dias. Clínicas com equipe dedicada de autorização têm aprovação mais rápida e menos negativas."),
    ],
    faq_list=[
        ("Qual a diferença entre bypass gástrico e sleeve gástrico?",
         "Bypass gástrico em Y de Roux (BGYR) cria uma pequena bolsa gástrica e desvia parte do intestino delgado, gerando restrição alimentar e má absorção de calorias e nutrientes. Resultados superiores em perda de peso e remissão de DM2. Sleeve gástrico é a retirada de 80% do estômago, deixando um 'tubo' vertical — apenas restritivo, sem má absorção. Sleeve tem menor complexidade técnica, menor taxa de complicações de longo prazo e é reversível (bypass não é). A escolha depende do perfil clínico do paciente."),
        ("Cirurgia bariátrica tem cobertura por plano de saúde no Brasil?",
         "Sim. A ANS inclui cirurgia bariátrica no rol de procedimentos obrigatórios para: IMC ≥ 40 sem comorbidades ou IMC ≥ 35 com comorbidades relacionadas à obesidade (DM2, HAS, apneia, dislipidemia, osteoartrose severa). Na prática, muitos planos exigem documentação extensa, período de acompanhamento prévio e aprovação por auditores, o que pode atrasar o processo por meses. Clínicas que domina o processo de autorização reduzem esse tempo significativamente."),
        ("Suplementação vitalícia após bariátrica é realmente necessária?",
         "Sim, indispensável. O bypass gástrico reduz drasticamente a absorção de vitaminas e minerais, especialmente ferro, vitamina B12, cálcio, vitamina D e ácido fólico. Sem suplementação adequada, deficiências graves se desenvolvem nos primeiros 1-2 anos — anemia ferropriva, neuropatia por deficiência de B12 e osteopenia/osteoporose por falta de cálcio e vitamina D são complicações evitáveis com acompanhamento correto. Mesmo com sleeve (que tem menor má absorção), a suplementação é fortemente recomendada."),
    ]
)

# Article 4385 — SaaS sales: centros de acupuntura e medicina tradicional chinesa
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-centros-de-acupuntura-e-medicina-tradicional-chinesa",
    title="Vendas de SaaS para Centros de Acupuntura e Medicina Tradicional Chinesa | ProdutoVivo",
    desc="Como vender SaaS de gestão para centros de acupuntura e medicina tradicional chinesa: abordagem, prontuário específico e expansão de receita.",
    h1="Vendas de SaaS para Centros de Acupuntura e Medicina Tradicional Chinesa",
    lead="Acupuntura e medicina tradicional chinesa (MTC) crescem em adoção no Brasil — com mais de 15.000 acupunturistas registrados e cobertura obrigatória por planos de saúde. Vender SaaS para esse segmento exige entender a lógica diagnóstica da MTC e as necessidades específicas de registro e faturamento.",
    sections=[
        ("Perfil do Mercado de Acupuntura e MTC no Brasil",
         "Acupuntura é reconhecida pelo CFM como especialidade médica e pelo CFO, COFFITO, CFF, CRN e CRP como prática integrativa para médicos, fisioterapeutas, farmacêuticos, nutricionistas e psicólogos. O Brasil tem a maior comunidade de acupunturistas da América Latina. A PNPIC (Política Nacional de Práticas Integrativas e Complementares) do Ministério da Saúde incluiu acupuntura e outras práticas de MTC no SUS. Planos de saúde são obrigados pela ANS a cobrir acupuntura para indicações específicas (dor crônica, enxaqueca, lombalgia)."),
        ("Necessidades Específicas de Software para MTC e Acupuntura",
         "O prontuário de MTC tem linguagem e lógica distintas da medicina convencional: diagnóstico energético por meridianos, síndromes da MTC (deficiência de Yin do Rim, estagnação de Qi do Fígado, etc.), pontos de acupuntura utilizados por sessão (com nomenclatura alfanumérica internacional — ST36, LR3, CV12), técnicas utilizadas (agulhamento seco, moxa, ventosaterapia, acupressão), e evolução energética do paciente ao longo das sessões. Sistemas genéricos de prontuário não suportam essa terminologia — sistemas especializados em MTC têm vantagem decisiva."),
        ("Abordagem de Prospecção no Segmento",
         "O decisor é o acupunturista proprietário da clínica ou o gestor de um centro integrativo multiprofissional. Prospecção eficaz: eventos de acupuntura e MTC (SAME — Simpósio de Acupuntura Médica e Energética, FABRAAC — Federação Brasileira de Acupuntura), grupos de acupunturistas no Instagram e WhatsApp, associações como SIMBAH, ABEN e FAAB, e parceiros de ensino de acupuntura que recomendam software aos alunos recém-formados. O argumento de faturamento com convênio (geração de guias TISS para acupuntura coberta) é um gatilho de urgência para clínicas que ainda não faturam planos."),
        ("Faturamento de Acupuntura por Planos de Saúde",
         "A cobertura de acupuntura pela ANS exige faturamento no padrão TISS com código específico de acupuntura, diagnóstico CID e solicitação médica (para pacientes de plano). Muitos acupunturistas perdem receita por não dominar o processo de faturamento de planos. SaaS que automatiza a geração de guias TISS para acupuntura e controla o status de autorização e pagamento transforma esse processo — e é o argumento de ROI mais imediato para o profissional. A combinação de prontuário especializado em MTC + faturamento de convênio é o pacote mais diferenciado do mercado."),
        ("Expansão de Receita e Módulos de Valor Agregado",
         "Módulos de maior interesse após conversão: agendamento online para sessões de acupuntura (frequência semanal ou bissemanal — geração de agendamentos recorrentes), lembrete automático de sessão (taxa de falta em acupuntura é alta — 15-25%), plataforma de telemedicina para teleconsultas de MTC (regulamentada para médicos acupunturistas), gestão de pacotes de sessões (venda de pacote de 10 sessões com preço especial — common em acupuntura), e módulo de fitoterapia chinesa para clínicas que trabalham com fitoterápicos da MTC."),
    ],
    faq_list=[
        ("Acupuntura tem cobertura por plano de saúde no Brasil?",
         "Sim. A ANS determina cobertura obrigatória de acupuntura com finalidade analgésica para indicações específicas, conforme RN ANS 465/2021. As indicações incluem: dor crônica (lombalgia, cervicalgia, cefaleia), enxaqueca, náuseas e vômitos pós-quimioterapia, entre outras. O processo de cobertura requer solicitação médica e, em muitos casos, autorização prévia do plano."),
        ("Profissionais não-médicos podem praticar acupuntura legalmente no Brasil?",
         "Sim, com regulamentação específica. A acupuntura pode ser praticada por: médicos (especialidade reconhecida pelo CFM), fisioterapeutas (resolução COFFITO), dentistas (resolução CFO — apenas em região orofacial), farmacêuticos (resolução CFF), nutricionistas (resolução CFN — apenas para fins nutricionais) e psicólogos (resolução CFP). Cada conselho define o escopo e as limitações da prática para sua categoria profissional."),
        ("Qual é o número médio de sessões em um tratamento de acupuntura?",
         "Depende da condição tratada: condições agudas (torcicolos, dores agudas) respondem em 3-5 sessões; condições crônicas (lombalgias, dores neuropáticas, enxaqueca) requerem 10-20 sessões para resultado consistente; condições funcionais (síndrome do intestino irritável, ansiedade, insônia) geralmente exigem de 10 a 30 sessões em ciclos periódicos. A acupuntura para doenças crônicas é frequentemente um tratamento de manutenção com sessões mensais ou bimestrais após a fase intensiva inicial."),
    ]
)

# Article 4386 — Consulting: gestão de pessoas e cultura de alta performance
art(
    slug="consultoria-de-gestao-de-pessoas-e-cultura-de-alta-performance",
    title="Consultoria de Gestão de Pessoas e Cultura de Alta Performance | ProdutoVivo",
    desc="Como estruturar uma consultoria de gestão de pessoas e cultura de alta performance: diagnóstico, OKRs, avaliação de desempenho e engajamento.",
    h1="Consultoria de Gestão de Pessoas e Cultura de Alta Performance",
    lead="Gestão de pessoas e cultura organizacional são alavancas estratégicas que diferenciam empresas de alta performance das demais. Consultorias especializadas nessa área têm demanda crescente de organizações que buscam alinhar estratégia, cultura e pessoas para atingir resultados superiores e sustentáveis.",
    sections=[
        ("Diagnóstico de Saúde Organizacional e Clima",
         "O diagnóstico é o ponto de partida de qualquer engajamento de consultoria de RH estratégico. Pesquisas de clima e engajamento (eNPS, pulse surveys), entrevistas com lideranças e colaboradores, análise de dados de RH (turnover por área e senioridade, tempo até produtividade de novos contratados, absenteísmo, NPS interno) e avaliação de práticas de gestão de pessoas criam o quadro completo da saúde organizacional. O benchmark com o setor e com empresas de alta performance orienta prioridades de intervenção."),
        ("OKRs e Sistemas de Gestão de Performance",
         "OKRs (Objectives and Key Results) são o framework de definição e acompanhamento de metas mais adotado por empresas de alto crescimento. A consultoria implanta OKRs em cascata — da estratégia corporativa aos times e indivíduos — e desenvolve a disciplina de revisão periódica (weekly check-ins, quarterly reviews). Além de OKRs, a implantação de avaliação de desempenho eficaz (calibração, feedback 360°, distinção de top performers) e de planos de desenvolvimento individuais (PDIs) compõem o sistema de gestão de performance de alta qualidade."),
        ("Gestão da Remuneração e Benefícios Competitivos",
         "Remuneração é um dos maiores drivers de atração e retenção de talentos — e um dos mais mal gerenciados em empresas de médio porte. A consultoria estrutura: bandas salariais por nível e função (job grading), benchmark de remuneração com mercado (pesquisas da Mercer, Hay, Catho, Glassdoor), política de remuneração variável (PLR, bônus por performance, comissionamento), e pacote de benefícios competitivos (plano de saúde e odontológico, VR/VA, seguro de vida, previdência privada, stock options). Transparência salarial moderada (bandas divulgadas internamente) reduz percepção de injustiça e conflitos."),
        ("Recrutamento, Onboarding e Retenção de Talentos",
         "A qualidade do recrutamento determina a qualidade da organização — clichê, mas verdadeiro. A consultoria estrutura: processo seletivo com múltiplas etapas (triagem, entrevista de competências, case, fit cultural, referências), onboarding estruturado de 90 dias com rituais de imersão na cultura e expectativas claras de performance, e programa de mentoring e buddy para novos contratados. A retenção de top performers requer reconhecimento não-monetário (visibilidade em projetos estratégicos, promoção acelerada, acesso a lideranças sêniors) além de remuneração competitiva."),
        ("Monetização e Posicionamento da Consultoria de Pessoas",
         "Projetos de diagnóstico de clima e RH custam de R$ 30.000 a R$ 100.000. Implantação de OKRs + sistema de performance custa de R$ 80.000 a R$ 250.000. Reestruturação de remuneração e benefícios de R$ 60.000 a R$ 180.000. Retainers mensais de CHRO fracionado (Chief Human Resources Officer fracionado — serviço de RH estratégico sem contratação de executivo full-time) geram R$ 8.000 a R$ 20.000/mês. A especialização em setor (tech, saúde, agro, varejo) permite cobrar prêmio e acelerar o impacto dos projetos."),
    ],
    faq_list=[
        ("O que é eNPS e como é calculado?",
         "eNPS (Employee Net Promoter Score) é a adaptação do NPS para medir o engajamento dos colaboradores: 'Em uma escala de 0 a 10, qual a probabilidade de você recomendar esta empresa como um ótimo lugar para trabalhar?' Promotores (9-10) menos detratores (0-6) dividido pelo total de respondentes = eNPS. Scores acima de 50 indicam alta lealdade dos colaboradores. É simples de aplicar mensalmente (pulse survey de 1 pergunta) e permite rastrear tendência ao longo do tempo — útil para identificar deterioração de clima antes que se transforme em turnover."),
        ("OKRs funcionam para empresas de médio porte ou são apenas para grandes tecnológicas?",
         "OKRs funcionam em qualquer organização que precise alinhar esforços em torno de objetivos claros e mensuráveis. A adaptação para empresas de médio porte envolve: simplificação (3-5 objetivos por equipe, não dezenas), ciclos mais curtos (trimestrais ou bimestrais) e maior tolerância a ajustes de meta durante o ciclo. A armadilha mais comum é transformar OKRs em mais uma burocracia de relatório sem impacto real nas decisões e alocação de recursos — o antídoto é liderança comprometida com os OKRs nas decisões do dia a dia."),
        ("CHRO fracionado é uma tendência no Brasil?",
         "Sim, crescente. Empresas de R$ 20 a R$ 150M de faturamento frequentemente não justificam um CHRO senior full-time (custo de R$ 30.000 a R$ 80.000/mês de salário + encargos), mas precisam de visão estratégica de RH além do DP operacional. O CHRO fracionado (ou VP de Pessoas fracionado) atende essa necessidade com 2-4 dias por mês de dedicação, trazendo experiência de grandes organizações a um custo de R$ 8.000 a R$ 20.000/mês — uma fração do custo de um executivo full-time."),
    ]
)

# Article 4387 — B2B SaaS: gestão hoteleira e hospitality
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-hoteleira-e-hospitality",
    title="Gestão de Negócios para SaaS de Gestão Hoteleira e Hospitality | ProdutoVivo",
    desc="Como escalar um SaaS de gestão hoteleira e hospitality no Brasil: produto PMS, canais de distribuição, vendas para redes e retenção.",
    h1="Gestão de Negócios para SaaS de Gestão Hoteleira e Hospitality",
    lead="O setor de hospitalidade brasileiro está em recuperação acelerada pós-pandemia, com demanda crescente por tecnologia de gestão hoteleira. SaaS de PMS (Property Management System) e ferramentas de revenue management têm oportunidade expressiva em um mercado com alta fragmentação e baixa penetração tecnológica.",
    sections=[
        ("Mercado Hoteleiro Brasileiro e Oportunidade para SaaS",
         "O Brasil tem mais de 30.000 meios de hospedagem cadastrados no Ministério do Turismo, da pousada de 5 quartos ao grande resort. A grande maioria ainda usa sistemas legados ou planilhas — especialmente hotéis independentes e pequenas redes regionais. O crescimento do turismo doméstico e a expansão de redes nacionais (Slaviero, Intercity, Wish, Nacional Inn) criam demanda por sistemas modernos de gestão. A integração com OTAs (Online Travel Agencies — Booking.com, Expedia, Airbnb para pousadas) via channel manager é a integração mais crítica para hotéis modernos."),
        ("Produto: PMS, Channel Manager e Revenue Management",
         "O núcleo de um SaaS hoteleiro é o PMS (Property Management System): reservas, check-in/check-out, gerenciamento de quartos, faturamento de diárias e serviços adicionais. Integrado ao PMS, o channel manager sincroniza disponibilidade e preços em tempo real com as OTAs (evitando overbooking), e o motor de reservas diretas (booking engine) no site do hotel reduz a dependência das OTAs (e suas comissões de 15-25%). Revenue management (definição dinâmica de tarifas por demanda, ocupação e sazonalidade) é o módulo de maior impacto em receita."),
        ("Vendas para Gerentes Gerais e Proprietários de Hotéis",
         "O decisor de compra em hotéis independentes é o proprietário ou o gerente geral; em redes, é o diretor de TI ou de operações. A venda para independentes é mais rápida (2-6 semanas) e menos técnica; para redes, o ciclo é de 3 a 9 meses com avaliação de múltiplos sistemas e demonstrações em propriedades piloto. Eventos como a Equipotel (maior feira de hotelaria da América Latina) e a ABIH (Associação Brasileira da Indústria de Hotéis) são canais de prospecção de alta concentração. Parcerias com consultores de hospitalidade e franquias hoteleiras ampliam o alcance."),
        ("Integrações Críticas: OTAs, Revenue e Financeiro",
         "As integrações mais críticas para um SaaS hoteleiro: channel manager com Booking.com, Expedia e Airbnb (via API direta ou agregador como SiteMinder, Omnibees, Omnibooker), integração com sistemas de ponto de venda (PDV) de restaurante e spa, plataforma de pagamento integrada (Cielo, Stone, PagSeguro para pagamento de diárias na chegada), e integração contábil com ERP para faturamento de serviços e conciliação bancária. Cada integração adicional aumenta o valor entregue e o lock-in do cliente."),
        ("Métricas e Retenção em SaaS Hoteleiro",
         "Métricas-chave do setor: RevPAR (Revenue Per Available Room — a métrica mais importante de revenue management), ocupação média, ADR (Average Daily Rate — tarifa média por quarto vendido) e TRevPAR (receita total por quarto disponível). SaaS que disponibilizam dashboards com esses indicadores em tempo real e comparação com períodos anteriores entregam valor imediato ao gestor hoteleiro. A retenção é alta quando o sistema está integrado com as OTAs e o histórico de reservas — migrar de PMS é uma das tarefas mais disruptivas que um hotel pode fazer."),
    ],
    faq_list=[
        ("O que é RevPAR e por que é a principal métrica de performance hoteleira?",
         "RevPAR (Revenue Per Available Room) é a receita de hospedagem dividida pelo total de quartos disponíveis no período — não apenas os quartos vendidos. RevPAR = Ocupação × ADR (tarifa média). É a métrica que melhor resume a performance de revenue management porque captura o trade-off entre ocupação e tarifa: um hotel pode ter 100% de ocupação com tarifa muito baixa (RevPAR baixo) ou 60% de ocupação com tarifa alta (RevPAR alto). Comparar o RevPAR com o conjunto competitivo (comp set) revela se o hotel está ganhando ou perdendo participação de mercado."),
        ("Channel manager é obrigatório para hotéis que vendem em OTAs?",
         "Não obrigatório por lei, mas praticamente indispensável para hotéis com mais de 10 quartos que vendem em múltiplas OTAs. Sem channel manager, o hotel precisa atualizar manualmente a disponibilidade em cada canal cada vez que uma reserva entra — processo propenso a erros e overbooking. Com channel manager integrado ao PMS, qualquer reserva em qualquer canal atualiza automaticamente a disponibilidade em todos os outros canais em segundos."),
        ("Qual é o ticket médio de um SaaS de PMS hoteleiro no Brasil?",
         "Para pousadas e hotéis pequenos (até 30 quartos), de R$ 200 a R$ 500/mês com funcionalidades básicas de reserva e front desk. Para hotéis de médio porte (30-100 quartos) com channel manager e revenue management, de R$ 500 a R$ 1.500/mês. Para grandes hotéis e redes (acima de 100 quartos ou múltiplas propriedades), de R$ 1.500 a R$ 8.000/mês com módulos avançados, integrações e suporte dedicado. Implementação é cobrada separadamente, de R$ 2.000 a R$ 20.000 dependendo do porte."),
    ]
)

# Article 4388 — Clinic: oftalmologia pediátrica e estrabismo
art(
    slug="gestao-de-clinicas-de-oftalmologia-pediatrica-e-estrabismo",
    title="Gestão de Clínicas de Oftalmologia Pediátrica e Estrabismo | ProdutoVivo",
    desc="Como gerenciar clínicas de oftalmologia pediátrica e estrabismo: fluxo de triagem, ambliopia, cirurgia de estrabismo e gestão multidisciplinar.",
    h1="Gestão de Clínicas de Oftalmologia Pediátrica e Estrabismo",
    lead="Oftalmologia pediátrica e subespecialidade de estrabismo atendem desde o bebê com leucocória suspeita até o adulto com diplopiae e desalinhamento ocular. A triagem visual de crianças, o tratamento de ambliopia e as cirurgias de estrabismo requerem protocolos específicos e equipe treinada.",
    sections=[
        ("Panorama da Oftalmologia Pediátrica no Brasil",
         "Doenças oculares na infância têm alta prevalência: ambliopia (olho preguiçoso) afeta 2-4% das crianças, estrabismo 4%, erros refrativos (hipermetropia, miopia, astigmatismo) até 20% em algumas faixas etárias. O diagnóstico precoce é crítico — ambliopia tratada antes dos 7-8 anos tem resolução completa na maioria dos casos; não tratada, causa perda visual permanente. O Programa de Saúde do Escolar inclui triagem visual, mas a execução é heterogênea — clínicas privadas de oftalmologia pediátrica atendem a demanda reprimida da saúde pública."),
        ("Fluxo Clínico: Triagem, Diagnóstico e Tratamento de Ambliopia",
         "O fluxo clínico começa com a triagem: fotoscreening (aparelhos como Spot Vision Screener, Plusoptix) em crianças de 1 a 4 anos que não cooperam com exames convencionais, seguido de refração sob cicloplégica (colírios cicloplégicos que relaxam a acomodação para medir a refração real da criança). O tratamento de ambliopia envolve: óculos de correção do erro refrativo (tratamento de primeira linha) + oclusão do olho dominante com tampão oftálmico ou atropina penalização. O controle do tratamento é baseado em acuidade visual seriada, exigindo retornos frequentes (mensais) e sistema de agendamento de seguimento estruturado."),
        ("Cirurgia de Estrabismo: Gestão e Fluxo Cirúrgico",
         "A cirurgia de estrabismo é realizada ambulatorialmente (frequentemente em hospital-dia), sob anestesia geral em crianças e sedação ou anestesia local em adultos. Gestão do fluxo cirúrgico inclui: avaliação pré-operatória completa (medida do ângulo de desvio em múltiplas posições do olhar, avaliação da visão binocular), planejamento cirúrgico com cálculo das alças de recessão e ressecção, gestão de agendamento em sala cirúrgica (cada procedimento leva 30 a 90 minutos) e acompanhamento pós-operatório rigoroso (1 semana, 1 e 3 meses). Taxas de sucesso de 80-90% em primeira cirurgia são esperadas em mãos experientes."),
        ("Adaptação de Óculos Pediátricos e Ótica Integrada",
         "Clínicas de oftalmologia pediátrica com ótica integrada têm vantagem competitiva significativa: a prescrição de óculos é imediatamente transformada em produto (sem o risco de o paciente ir a outra ótica com receita incorreta ou óculos de baixa qualidade). A gestão da ótica pediátrica exige: estoque de armações adequadas para crianças de 0 a 14 anos, lentes com tratamento antirreflexo e proteção UV obrigatórias para crianças, adaptação especializada para bebês (armações com hastes em silicone que prendem atrás da orelha) e controle de garantia de armações e lentes."),
        ("Captação e Fidelização em Oftalmologia Pediátrica",
         "A captação vem de pediatras que encaminham crianças com suspeita de déficit visual, pais preocupados com posicionamento anômalo dos olhos (estrabismo), e programas de triagem visual em escolas. A fidelização é natural — crianças em tratamento de ambliopia retornam mensalmente por 1 a 3 anos, e acompanhamento anual para controle refrativo é recomendado até a estabilidade refratométrica (geralmente na adolescência). Famílias com mais de um filho frequentemente levam todos os filhos ao mesmo oftalmologista pediátrico de confiança."),
    ],
    faq_list=[
        ("Ambliopia tem cura completa?",
         "Sim, quando diagnosticada e tratada precocemente. Antes dos 7-8 anos (período crítico de plasticidade visual), a ambliopia responde bem ao tratamento — oclusão do olho dominante + correção óptica do olho ambliópico. A recuperação pode ser completa (acuidade visual normal em ambos os olhos). Após os 9-10 anos, a plasticidade visual diminui e os resultados são parciais. Em adultos, o tratamento tem eficácia muito limitada — daí a importância da triagem visual nos primeiros anos de vida."),
        ("A cirurgia de estrabismo é definitiva?",
         "Na maioria dos casos, sim — uma única cirurgia bem indicada e executada corrige o desalinhamento ocular de forma permanente. Taxas de sucesso de 80-90% em primeira cirurgia são esperadas para estrabismos horizontais simples. Casos de estrabismo vertical, padrões oblíquos e reoperações têm taxas de sucesso menores. Uma segunda cirurgia é necessária em aproximadamente 15-20% dos casos para ajuste fino do alinhamento."),
        ("A partir de que idade crianças podem usar óculos?",
         "Óculos podem e devem ser prescritos a partir do nascimento quando necessário — bebês com alta hipermetropia ou astigmatismo significativo precisam de óculos precocemente para desenvolver visão normal e evitar ambliopia. Existem armações especialmente desenvolvidas para recém-nascidos e lactentes. O mais cedo a criança usar óculos com prescrição correta, melhor para o desenvolvimento visual."),
    ]
)

# Article 4389 — SaaS sales: clínicas de fonoaudiologia clínica e transtornos da fala
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-fonoaudiologia-clinica-e-transtornos-da-fala",
    title="Vendas de SaaS para Clínicas de Fonoaudiologia Clínica e Transtornos da Fala | ProdutoVivo",
    desc="Como vender SaaS de gestão para clínicas de fonoaudiologia: abordagem ao fonoaudiólogo, prontuário específico e expansão de receita.",
    h1="Vendas de SaaS para Clínicas de Fonoaudiologia Clínica e Transtornos da Fala",
    lead="Fonoaudiologia clínica atende uma ampla gama de condições — dislexia, gagueira, disfagia, atraso de linguagem, transtornos do espectro autista — com alta demanda crescente. Vender SaaS para esse segmento requer entender os protocolos de avaliação e terapia fonoaudiológica e a integração com equipes multiprofissionais.",
    sections=[
        ("Perfil do Mercado de Fonoaudiologia no Brasil",
         "O Brasil tem mais de 80.000 fonoaudiólogos registrados no CFFa (Conselho Federal de Fonoaudiologia), atuando em clínicas, escolas, hospitais e serviços de saúde pública. As áreas de maior demanda incluem: linguagem infantil (atraso de linguagem, gagueira, distúrbios fonológicos), motricidade orofacial (deglutição atípica, respiração oral, mordida aberta), disfagia (em idosos e pós-AVC), voz (disfonias em professores e cantores) e audiologia clínica (adaptação de aparelhos auditivos, reabilitação auditiva)."),
        ("Necessidades Específicas de Software para Fonoaudiologia",
         "O prontuário fonoaudiológico precisa suportar: avaliações padronizadas com scores (ABFW para linguagem, TFono para fonologia, MBGR para motricidade orofacial, Escala de FOIS para disfagia), registro de sessões de terapia com objetivos e metas individualizadas, evolução por competência (fonemas adquiridos, palavras em vocabulário, escores de fluência), relatórios para equipe multiprofissional (psicólogo, pedagogos, médicos) e para família, e suporte a teleatendimento fonoaudiológico (regulamentado pelo CFFa desde 2020)."),
        ("Abordagem de Prospecção para o Segmento",
         "O decisor é o fonoaudiólogo proprietário do consultório ou clínica. A prospecção mais eficaz combina: eventos da área (CBFono — Congresso Brasileiro de Fonoaudiologia), grupos de fonoaudiólogos no Instagram e Facebook, parcerias com escolas e clínicas de reabilitação que indicam software aos profissionais da rede, e marketing de conteúdo voltado a gestão de consultório para fonoaudiólogos (tema de alto interesse na categoria). Fonoaudiólogos recém-formados são um público receptivo — estão criando consultório do zero e buscam referências."),
        ("Integração com Equipes Multiprofissionais e Relatórios",
         "A fonoaudiologia frequentemente atua em equipes multiprofissionais para: TEA (Transtorno do Espectro Autista — com psicólogo, terapeuta ocupacional e pedagogo), reabilitação pós-AVC (com fisioterapeuta, terapeuta ocupacional, neurologista), disfagia hospitalar (com nutricionista e médico) e voz profissional (com otorrinolaringologista). SaaS que suportam compartilhamento de prontuário e relatórios multiprofissionais, e integração com equipes de centros de reabilitação, têm diferencial relevante para fonoaudiólogos que atuam nesses contextos."),
        ("Expansão de Receita e Módulos de Valor",
         "Módulos com maior interesse após conversão: agendamento online com lembretes automáticos (reduz faltas em terapias longas), teleatendimento fonoaudiológico integrado (para atendimento remoto regulamentado), portal dos pais (comunicação com responsáveis sobre progresso e atividades para casa), gestão de convênios com faturamento de sessões fonoaudiológicas (cobertura obrigatória pela ANS para alguns diagnósticos), e plataforma de atividades digitais para terapia em casa (exercícios de fala, linguagem e motricidade enviados digitalmente para o paciente praticar entre sessões)."),
    ],
    faq_list=[
        ("Plano de saúde cobre fonoaudiologia no Brasil?",
         "Sim. A ANS determina cobertura de avaliação e terapia fonoaudiológica para diagnósticos específicos: TEA (Transtorno do Espectro Autista — cobertura de sessões ilimitadas após a Lei 14.254/2021), disfagia, disfonias, atraso de linguagem, afasia pós-AVC, entre outros. A cobertura é variável por plano — alguns limitam o número de sessões anuais, outros cobrem ilimitado conforme necessidade clínica documentada."),
        ("Teleatendimento fonoaudiológico é permitido no Brasil?",
         "Sim, regulamentado pelo CFFa (Resolução CFFa 590/2020 e atualizações posteriores). A fonoteletrapia pode ser realizada por videoconferência para diagnósticos e públicos específicos — é especialmente eficaz para linguagem oral, fluência e voz. Para avaliações que requerem análise direta (disfagia orofaríngea, adaptação de aparelho auditivo), o atendimento presencial ainda é necessário ou recomendado."),
        ("Com que frequência devem ser realizadas sessões de terapia fonoaudiológica?",
         "A frequência ideal depende da condição: para atraso de linguagem e transtornos fonológicos, 2 sessões semanais de 45-50 minutos são o padrão de maior eficácia — consistência e frequência são chave para o aprendizado motor e linguístico. Para disfagia hospitalar aguda, pode ser diária ou mais frequente. Para voz e gagueira em adultos, 1-2 sessões semanais são adequadas. A duração total do tratamento varia de 6 meses a 3 anos dependendo da condição e da resposta individual."),
    ]
)

# Article 4390 — Consulting: gestão da experiência do funcionário e employee engagement
art(
    slug="consultoria-de-gestao-da-experiencia-do-funcionario-e-employee-engagement",
    title="Consultoria de Gestão da Experiência do Funcionário e Employee Engagement | ProdutoVivo",
    desc="Como estruturar uma consultoria de Employee Experience (EX) e engajamento: diagnóstico, jornada do colaborador e programas de reconhecimento.",
    h1="Consultoria de Gestão da Experiência do Funcionário e Employee Engagement",
    lead="Employee Experience (EX) é uma das disciplinas mais estratégicas de RH no contexto atual, onde atrair e reter talentos é tão crítico quanto atrair e reter clientes. Consultorias especializadas em EX ajudam organizações a criar ambientes onde as pessoas queiram trabalhar e dar o melhor de si.",
    sections=[
        ("O Conceito de Employee Experience e Sua Importância Estratégica",
         "Employee Experience é o conjunto de percepções, sentimentos e memórias que um colaborador acumula ao longo de sua jornada na organização — desde o recrutamento até o offboarding. Empresas com EX superior têm: 4x mais lucro, 2x mais receita e 40% menos rotatividade que a média, segundo estudos do Jacob Morgan e Gallup. No Brasil, a escassez de talentos especializados em tecnologia, saúde e áreas técnicas torna a EX uma vantagem competitiva real na guerra por talentos."),
        ("Jornada do Colaborador: Mapeamento e Pontos de Intervencão",
         "A jornada do colaborador começa no employer branding (antes mesmo de se candidatar) e passa por: recrutamento e seleção, oferta e onboarding, desenvolvimento e crescimento, dia a dia de trabalho, gestão de performance, reconhecimento, e eventually offboarding (saída com ou sem boa experiência). A consultoria mapeia cada etapa identificando momentos de verdade (touchpoints críticos), pesquisa a percepção atual em cada ponto e prioriza intervenções de maior impacto na retenção e engajamento."),
        ("Programas de Reconhecimento e Pertencimento",
         "Reconhecimento é o segundo maior driver de engajamento (após propósito e autonomia), segundo pesquisas do Gallup. A consultoria estrutura: programas de reconhecimento entre pares (peer recognition), celebração de marcos de carreira e conquistas de time, rituais de feedback positivo em reuniões de equipe, e programas de reconhecimento formal vinculados à performance. Além do reconhecimento, iniciativas de Diversidade, Equidade e Inclusão (DEI) e de pertencimento (belonging) são pilares crescentes de EX que a consultoria ajuda a implementar de forma autêntica e sistemática."),
        ("Mensuração de EX e Employee Listening",
         "Employee Listening é a prática de coletar continuamente a voz do colaborador via múltiplos canais: pulse surveys mensais (3-5 perguntas sobre engajamento e bem-estar), pesquisa de clima anual completa, entrevistas de saída (exit interviews) e permanência (stay interviews — o que faria você sair?), fóruns abertos com lideranças e canais de feedback anônimos. O diferencial de uma consultoria de EX é transformar esses dados em insights acionáveis e prioridades de investimento — não apenas relatórios de benchmark."),
        ("Monetização e Posicionamento da Consultoria de EX",
         "Projetos de mapeamento da jornada do colaborador e diagnóstico de EX custam de R$ 40.000 a R$ 120.000. Programas de transformação de EX (12-18 meses) de R$ 200.000 a R$ 600.000. Implementação de plataformas de employee listening (Qualtrics, Culture Amp, Officevibe) com curadoria de insights de R$ 30.000 a R$ 80.000 + setup da plataforma. Retainers de Chief Experience Officer fracionado de R$ 10.000 a R$ 25.000/mês. Especialização em setor tecnológico (startups, scaleups) ou em empresas em rápido crescimento são nichos com maior disposição a pagar."),
    ],
    faq_list=[
        ("Qual a diferença entre Employee Experience e Employee Engagement?",
         "Employee Engagement mede o nível de comprometimento e energia do colaborador com o trabalho e a organização — é um resultado. Employee Experience é o conjunto de fatores (cultura, liderança, ferramentas, espaço físico, desenvolvimento) que produzem esse resultado. Foco em EX é uma abordagem sistêmica e proativa; foco em engagement sem EX é tratar o sintoma sem a causa."),
        ("Stay interviews são mais eficazes que exit interviews?",
         "Sim, porque chegam antes do ponto de não-retorno. Exit interviews coletam informações de quem já decidiu sair — tarde demais para reter esse colaborador. Stay interviews (conversas estruturadas com colaboradores valorizados sobre o que os mantém e o que os faria sair) identificam fatores de risco de perda enquanto ainda há tempo de agir. A melhor prática é realizar stay interviews semestrais com colaboradores-chave em posições críticas."),
        ("Como medir o ROI de investimentos em Employee Experience?",
         "Os principais indicadores de retorno incluem: redução de turnover (custo de substituição de um colaborador é de 50-200% do salário anual), redução do tempo até produtividade plena de novos contratados, aumento de eNPS (associado a maior retenção e produtividade), redução de absenteísmo e presenteísmo, e melhora de resultados de negócio correlacionados com engajamento (produtividade por colaborador, NPS de clientes, velocidade de inovação). Empresas que documentam essas métricas antes e depois das intervenções constroem o caso de ROI de forma convincente."),
    ]
)

# ── Sitemap & trilha updates ──────────────────────────────────────────────────
import pathlib

root = pathlib.Path(__file__).parent

slugs = [
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-ciberseguranca-e-gestao-de-identidade-e-acesso",
     "Gestão de Negócios para SaaS de Cibersegurança e Gestão de Identidade e Acesso"),
    ("gestao-de-clinicas-de-cirurgia-bariatrica-e-metabolica-multidisciplinar",
     "Gestão de Clínicas de Cirurgia Bariátrica e Metabólica Multidisciplinar"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-centros-de-acupuntura-e-medicina-tradicional-chinesa",
     "Vendas de SaaS para Centros de Acupuntura e Medicina Tradicional Chinesa"),
    ("consultoria-de-gestao-de-pessoas-e-cultura-de-alta-performance",
     "Consultoria de Gestão de Pessoas e Cultura de Alta Performance"),
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-hoteleira-e-hospitality",
     "Gestão de Negócios para SaaS de Gestão Hoteleira e Hospitality"),
    ("gestao-de-clinicas-de-oftalmologia-pediatrica-e-estrabismo",
     "Gestão de Clínicas de Oftalmologia Pediátrica e Estrabismo"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-fonoaudiologia-clinica-e-transtornos-da-fala",
     "Vendas de SaaS para Clínicas de Fonoaudiologia Clínica e Transtornos da Fala"),
    ("consultoria-de-gestao-da-experiencia-do-funcionario-e-employee-engagement",
     "Consultoria de Gestão da Experiência do Funcionário e Employee Engagement"),
]

sitemap_path = root / "sitemap.xml"
sm = sitemap_path.read_text(encoding="utf-8")
new_urls = "".join(f"<url><loc>https://produtovivo.com.br/blog/{s}/</loc></url>\n" for s, _ in slugs)
sitemap_path.write_text(sm.replace("</urlset>", new_urls + "</urlset>"), encoding="utf-8")

trilha_path = root / "trilha.html"
tr = trilha_path.read_text(encoding="utf-8")
new_items = "".join(f'<li><a href="/blog/{s}/">{t}</a></li>\n' for s, t in slugs)
trilha_path.write_text(tr.replace("</ul>", new_items + "\n</ul>", 1), encoding="utf-8")

print("Done — batch 1450")
