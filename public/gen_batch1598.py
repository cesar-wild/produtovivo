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

# Article 4679 — B2B SaaS: Construction and project management
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-construcao-e-gestao-de-obras",
    title="Gestão de Negócios de Empresa de B2B SaaS de Construção e Gestão de Obras",
    desc="Como estruturar e escalar uma empresa de B2B SaaS de construção e gestão de obras: modelo de negócio, diferenciação, go-to-market e métricas de crescimento no mercado de construtechs.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Construção e Gestão de Obras",
    lead="A construção civil brasileira é um dos setores menos digitalizados da economia — e por isso um dos com maior oportunidade para tecnologia. Plataformas de gestão de obras e construtechs têm mercado vasto entre construtoras, incorporadoras, engenheiras e gestores de facilities que ainda gerenciam projetos em planilhas e cadernos.",
    sections=[
        ("O Mercado de Construtech e Construction Management SaaS",
         "O mercado de construtechs inclui: plataformas de gestão de obras (cronograma, orçamento, avanço físico-financeiro), sistemas de gestão de documentação técnica (plantas, memoriais, RDOs — Relatórios Diários de Obra), ferramentas de controle de qualidade e conformidade (checklists de inspeção, não-conformidades, ensaios), plataformas de gestão de segurança do trabalho em obra (NR-18, treinamentos, EPI, CAT), sistemas de supply chain para construção (compras de materiais, contratos de empreiteiros), e soluções de BIM (Building Information Modeling) para projetos e compatibilização. Procore, PlanGrid, Buildertrend e soluções brasileiras como Sienge, Vitta, Obra Prima e Hyperon competem em diferentes segmentos."),
        ("Diferenciação em Construction SaaS",
         "Os diferenciadores mais relevantes incluem: app mobile para uso em obra sem internet (sincronização offline — fundamental dado que muitas obras têm conectividade precária), integração de foto e vídeo georreferenciado para registro do andamento da obra, fluxo de aprovação de medição de empreiteiros (automatizando um processo manual e suscetível a erros), gestão de não-conformidades com rastreamento até a resolução, relatório automático de curva S (avanço físico versus financeiro), e integração com ERPs do setor (TOTVS Construção, SAP). Para incorporadoras, a integração com CRM de vendas de unidades e com o sistema de repasse bancário é diferencial relevante."),
        ("Modelo de Receita em Construtech SaaS",
         "O modelo combina mensalidade por usuário ou por número de obras ativas. Pequenas construtoras (1 a 5 obras simultâneas) pagam de R$400 a R$1.500/mês; incorporadoras e construtoras médias (10 a 50 obras) pagam de R$3.000 a R$15.000/mês. Projetos de implementação para integrar a plataforma com sistemas legados e treinamento da equipe de obra são fontes de receita adicional de alto ticket. O modelo também pode ter base no valor de obra gerenciada (percentual do VGV — Valor Geral de Vendas da incorporação) — alinhando o preço ao tamanho do projeto."),
        ("Go-to-Market para Construtechs",
         "O comprador de construtech é o diretor de engenharia, o gerente de obras ou o sócio de construtoras menores. O setor tem forte cultura de relacionamento — vendas por indicação e presença em eventos setoriais (CBIC, FeiraConstruir, Expo Revestir) têm peso muito maior do que marketing digital. Parcerias com sindicatos da construção (Sinduscon) e associações de engenheiros (CONFEA/CREA) abrem portas de credibilidade. A abordagem consultiva — oferecendo diagnóstico dos processos atuais da construtora antes de apresentar a solução — funciona melhor nesse mercado conservador do que demo genérica."),
        ("Métricas de Saúde em Construction SaaS",
         "As métricas operacionais que o cliente monitorará: precisão do orçamento versus realizado (a plataforma deve reduzir as variações), percentual de avanço físico registrado no prazo (indicador de adoção do RDO digital), tempo de aprovação de medições de empreiteiros, e número de não-conformidades abertas versus fechadas. As métricas de negócio incluem número de obras ativas na plataforma por cliente (expansão natural conforme a construtora cresce), NRR e churn. A construção é cíclica — construtoras em ciclo baixo de obras reduzem assinaturas; plataformas com flexibilidade de pausa de obras sem cancelamento total retêm melhor nesses períodos.")
    ],
    faq_list=[
        ("O que é BIM e toda construtora precisa usar?",
         "BIM (Building Information Modeling) é a metodologia de trabalho com modelos digitais tridimensionais que integram informações de projeto, estrutura, instalações e quantitativos em um único modelo. Construtoras e incorporadoras de grande porte que trabalham com projetos complexos se beneficiam muito do BIM para compatibilização de projetos (detectar conflitos entre estrutura e hidráulica antes de construir) e para gestão de quantitativos. Para obras simples e residenciais de menor porte, o BIM ainda tem curva de adoção e custo de treinamento que superam o benefício imediato — mas a tendência é de adoção crescente em todos os segmentos."),
        ("O que é Relatório Diário de Obra (RDO) e por que digitalizá-lo?",
         "RDO é o registro diário do andamento da obra: mão de obra presente, atividades executadas, materiais recebidos, condições climáticas, ocorrências e fotos. É documento técnico obrigatório para acompanhamento da obra e fundamental em disputas contratuais — registra o que foi feito, quando e por quem. RDO em papel é trabalhoso, ilegível e se perde. RDO digital via app permite: preenchimento no celular em campo, fotos georreferenciadas integradas, sincronização automática com o sistema de gestão, e geração automática de relatório consolidado de progresso."),
        ("Como controlar o orçamento de uma obra em tempo real?",
         "O controle orçamentário em tempo real exige: orçamento analítico detalhado por serviço e insumo na plataforma, lançamento de todas as compras de material e medições de empreiteiros na plataforma conforme ocorrem, e comparação automática entre orçado e realizado por serviço. Desvios identificados precocemente permitem ação corretiva antes que o impacto seja irreversível — um serviço com custo 20% acima do orçado descoberto na metade da obra ainda permite renegociação ou ajuste de escopo.")
    ]
)

# Article 4680 — Clinic: Rheumatology and autoimmune diseases
art(
    slug="gestao-de-clinicas-de-reumatologia-e-doencas-autoimunes",
    title="Gestão de Clínicas de Reumatologia e Doenças Autoimunes",
    desc="Guia de gestão para clínicas de reumatologia e doenças autoimunes: fluxo assistencial, tratamentos biológicos, gestão de pacientes crônicos e indicadores de qualidade.",
    h1="Gestão de Clínicas de Reumatologia e Doenças Autoimunes",
    lead="A reumatologia trata doenças complexas e debilitantes — artrite reumatoide, lúpus, espondiloartrites, esclerose sistêmica — que exigem acompanhamento crônico especializado, acesso a medicamentos biológicos e integração multidisciplinar. Clínicas bem estruturadas oferecem cuidado de alto impacto para pacientes com necessidades complexas.",
    sections=[
        ("Abrangência da Reumatologia Clínica",
         "A reumatologia abrange mais de 200 doenças que afetam articulações, músculos, ossos e tecidos conjuntivos: artrite reumatoide (doença inflamatória crônica das articulações — a mais comum da especialidade), lúpus eritematoso sistêmico (doença autoimune multissistêmica que pode afetar rins, cérebro, coração e pulmões), espondiloartrites (incluindo espondilite anquilosante e artrite psoriásica), síndrome de Sjögren, miopatias inflamatórias, vasculites sistêmicas, esclerose sistêmica (esclerodermia), gota e outras artropatias microcristalinas, e osteoporose (com indicação de tratamento medicamentoso). Muitas dessas condições são crônicas e requerem acompanhamento trimestral ou semestral indefinido — gerando carteira estável de pacientes fidelizados."),
        ("Medicamentos Biológicos: Acesso e Gestão",
         "O avanço mais significativo da reumatologia nas últimas décadas foi o desenvolvimento de medicamentos biológicos (anti-TNF, anti-IL-6, anti-CD20, anti-CTLA4 e outros) que mudaram o prognóstico de doenças antes intratáveis. A gestão desses medicamentos é um aspecto crítico da prática reumatológica: são de alto custo (R$10.000 a R$80.000 por ano de tratamento), disponíveis no SUS via PCDT (Protocolos Clínicos e Diretrizes Terapêuticas) com documentação específica para solicitação, e disponíveis pela via judicial quando o SUS nega acesso. A clínica que domina o processo de solicitação de biológicos pelo SUS e orienta os pacientes agrega valor imenso — muitos pacientes chegam sem saber que têm direito ao tratamento gratuitamente."),
        ("Infusoterapia: Serviço de Alto Valor",
         "Vários medicamentos reumatológicos (rituximabe, abatacepte, belimumabe, tocilizumabe IV) são administrados por infusão endovenosa, que pode ser realizada na própria clínica com sala de infusão adequada. A infusoterapia ambulatorial é um serviço de alto valor clínico (paciente não precisa se internar) e de alta receita para a clínica (infusões faturadas por plano de saúde ou SUS). A sala de infusão requer: poltronas reclináveis, equipamento de monitoramento (oximetria, pressão arterial), kit de anafilaxia, enfermagem treinada e médico disponível. Constru ir essa infraestrutura transforma a clínica reumatológica em referência de tratamento especializado."),
        ("Multidisciplinaridade em Reumatologia",
         "O cuidado reumatológico é eminentemente multidisciplinar: fisioterapia (para preservar a função articular e reduzir a dor), terapia ocupacional (adaptações para atividades de vida diária em pacientes com limitações físicas), psicologia (impacto emocional de doenças crônicas incapacitantes), nutrição (dieta anti-inflamatória, controle de peso para reduzir carga articular), e enfermagem especializada em artrite (educação do paciente sobre a doença e o tratamento). Clínicas que integram essa equipe ou constroem rede de parceiros coordenados oferecem cuidado superior e retêm pacientes que de outra forma buscariam múltiplas clínicas separadas."),
        ("Indicadores de Performance em Reumatologia",
         "As métricas clínicas incluem percentual de pacientes com artrite reumatoide em remissão ou baixa atividade de doença (avaliado por scores como DAS28 ou CDAI), taxa de progressão radiológica (articulações com destruição progressiva apesar do tratamento), tempo entre diagnóstico e início de tratamento com DMARD (diagnóstico precoce e tratamento rápido são determinantes do prognóstico), e NPS de pacientes. As métricas de negócio incluem receita por infusão realizada, taxa de solicitações de biológico aprovadas pelo SUS (indicador de qualidade da documentação), e taxa de aderência ao seguimento crônico.")
    ],
    faq_list=[
        ("Artrite reumatoide tem cura?",
         "Não há cura para a artrite reumatoide, mas é uma doença muito bem controlável com o tratamento atual. O objetivo do tratamento moderno é a remissão — ausência de inflamação ativa — que pode ser mantida indefinidamente com medicação. Pacientes diagnosticados precocemente e tratados adequadamente têm qualidade de vida próxima à normal. O risco é o diagnóstico tardio — a janela de oportunidade terapêutica (primeiros meses da doença) é o momento em que o tratamento tem maior impacto no prognóstico a longo prazo."),
        ("O que são medicamentos biológicos em reumatologia?",
         "Medicamentos biológicos são proteínas produzidas por tecnologia de DNA recombinante que bloqueiam alvos específicos da inflamação — como o TNF-alfa, a interleucina 6, ou linfócitos B. São mais seletivos do que os imunossupressores convencionais, com melhor perfil de eficácia e efeitos adversos diferentes. São indicados para doenças com atividade moderada a grave que não responderam adequadamente ao tratamento convencional (metotrexato, hidroxicloroquina). O SUS cobre os biológicos aprovados em PCDT — o reumatologista prepara a documentação e solicita via RENAME."),
        ("Lúpus é uma doença grave?",
         "Lúpus é uma doença séria com espectro amplo de manifestações — de formas leves com apenas sintomas cutâneos e articulares a formas graves com envolvimento renal (nefrite lúpica), neurológico ou cardiovascular. O prognóstico melhorou enormemente com o tratamento atual — a maioria dos pacientes tem vida longa com doença controlada. O acompanhamento reumatológico regular é essencial para detectar precocemente surtos e envolvimento de órgãos nobres antes que causem dano permanente.")
    ]
)

# Article 4681 — SaaS sales: Insurance and insurtech
art(
    slug="vendas-para-o-setor-de-saas-de-seguros-e-insurtech",
    title="Vendas para o Setor de SaaS de Seguros e Insurtech",
    desc="Estratégias de vendas B2B para plataformas SaaS de seguros e insurtech: como abordar seguradoras, corretoras e gestores de risco para fechar contratos neste mercado regulado.",
    h1="Vendas para o Setor de SaaS de Seguros e Insurtech",
    lead="O mercado de seguros brasileiro é o quarto maior do mundo e está em digitalização acelerada. Insurtechs e plataformas SaaS para o setor desafiam operações legacy com tecnologia mais ágil, experiência do cliente superior e modelos de precificação mais precisos. Vender nesse mercado exige entendimento profundo da regulação e do perfil conservador do comprador.",
    sections=[
        ("O Mercado de Insurtech no Brasil",
         "O mercado de insurtech e SaaS para seguros inclui: plataformas de distribuição digital (comparadores de seguros, marketplaces de apólices), sistemas de gestão para corretoras de seguros (CRM de seguros, gestão de apólices, comissões e sinistros), ferramentas de precificação e análise de risco (com machine learning sobre dados de sinistro), plataformas de regulação e liquidação de sinistros (automatizando o ciclo do aviso ao pagamento), soluções de parametric insurance (pagamento automático baseado em parâmetros objetivos — chuva, temperatura — sem necessidade de aviso e regulação), e infraestrutura de backend para seguradoras (core insurance systems em cloud). O mercado é regulado pela SUSEP — qualquer plataforma que opera como seguradora ou intermediária precisa de autorização."),
        ("O Decisor em Seguros e Insurtech",
         "O decisor varia por segmento: em seguradoras, é o CTO ou diretor de tecnologia para sistemas core, e o CMO para plataformas de distribuição. Em corretoras, é o sócio-proprietário ou o gerente comercial (em corretoras maiores). Em gestoras de risco corporativo (risk managers), é o diretor financeiro ou o gerente de seguros corporativos. O comprador do setor de seguros é altamente conservador — um sistema que falha na emissão de apólice ou no pagamento de sinistro tem consequência regulatória imediata. Certificações (ISO 27001, SOC 2), SLA contratual e referências de outras seguradoras ou corretoras são pré-requisitos de credibilidade."),
        ("Proposta de Valor por Segmento",
         "Para corretoras: automação de processos manuais (cotação com múltiplas seguradoras em uma tela, geração automática de proposta e apólice, cobrança de prêmio, gestão de renovações), visibilidade da carteira (apólices a vencer, sinistros em aberto, comissões a receber), e CRM de relacionamento com cliente que aumenta a taxa de renovação e cross-sell. Para seguradoras: redução do tempo de emissão de apólice (de dias para minutos), automação do ciclo de sinistro (de aviso ao pagamento em dias em vez de semanas), e uso de dados alternativos para precificação mais precisa (telemática para auto, dados de sensores IoT para patrimonial)."),
        ("Ciclo de Venda e Compliance em Insurtech",
         "O ciclo de venda para sistemas core de seguradora é longo (12 a 24 meses) e envolve due diligence técnica, homologação regulatória e projeto piloto antes da migração completa. Para ferramentas de corretora, o ciclo é mais curto (1 a 3 meses) mas envolve integração com as seguradoras parceiras da corretora — que precisam aceitar a plataforma intermediária. A SUSEP publica regulações frequentes que impactam o setor (open insurance, sandbox regulatório, resolução sobre distribuição digital) — insurtechs que se mantêm atualizadas com o ambiente regulatório e comunicam proativamente os impactos ao cliente criam vantagem diferencial."),
        ("Retenção e Churn em Insurance SaaS",
         "Sistemas core de seguradora têm o maior switching cost do mercado financeiro — a migração de uma plataforma de emissão de apólices implica reprocessar todo o histórico de carteira, reintegrar todas as regras de produto e risco, e religar todos os canais de distribuição. A retenção é estruturalmente muito alta. Para plataformas de corretora, o churn é impulsionado pela saída de sócios fundadores e pela troca de sistema por indicação de corretoras pares. A retenção é construída por profundidade de adoção: quanto mais funcionalidades da plataforma o corretor usa ativamente, mais custoso e improvável é o cancelamento.")
    ],
    faq_list=[
        ("O que é open insurance e como ele impacta o setor?",
         "Open Insurance é o ecossistema regulado pela SUSEP que permite o compartilhamento de dados de seguros entre seguradoras, corretoras e plataformas autorizadas — com consentimento do cliente. Assim como o Open Finance transformou o setor bancário, o Open Insurance permitirá: portabilidade de histórico de sinistros (o cliente leva seu histórico para outra seguradora e obtém desconto na renovação), comparação de cobertura e preço com dados padronizados, e personalização de produtos baseada em dados consolidados de múltiplas seguradoras."),
        ("O que é seguro paramétrico?",
         "Seguro paramétrico é um modelo em que o pagamento é automático quando um parâmetro pré-definido é atingido — sem necessidade de aviso de sinistro, regulação e vistoria. Exemplos: seguro rural que paga automaticamente se a precipitação acumulada no mês for abaixo de X mm (índice de chuva medido por estação meteorológica certificada); seguro de viagem que paga automaticamente se o voo for cancelado (com base em dados da ANAC). O pagamento é rápido e sem burocracia — mas só funciona quando o parâmetro pode ser mensurado objetivamente e correlaciona bem com a perda real."),
        ("Corretora de seguros precisa de sistema especializado?",
         "Sim — corretoras com mais de 200 apólices em carteira precisam de sistema para: controlar datas de vencimento (apólice vencida sem renovação = cliente desprotegido e comissão perdida), gerenciar sinistros em andamento, controlar comissões a receber de cada seguradora, e fazer follow-up de propostas em aberto. Planilhas não escalam e geram erros que têm consequências para o cliente e para a corretora. Sistemas especializados para corretora custam de R$200 a R$800/mês e têm ROI imediato em uma ou duas renovações recuperadas.")
    ]
)

# Article 4682 — Consulting: Governance, risk and compliance
art(
    slug="consultoria-de-governanca-risco-e-compliance",
    title="Consultoria de Governança, Risco e Compliance",
    desc="Como consultorias de governança, risco e compliance (GRC) ajudam empresas a estruturar controles internos, gerenciar riscos e garantir conformidade regulatória.",
    h1="Consultoria de Governança, Risco e Compliance",
    lead="Governança deficiente, riscos não mapeados e não conformidade regulatória têm custo elevado — multas, litígios, perda de contratos e danos reputacionais irreversíveis. Consultorias de GRC ajudam empresas a construir a estrutura de controles, processos e cultura que previnem esses problemas de forma sistemática.",
    sections=[
        ("O Escopo da Consultoria de GRC",
         "A consultoria de GRC atua em três dimensões interligadas: Governança (estrutura de tomada de decisão — conselho de administração, comitês, alçadas de aprovação, políticas corporativas), Risco (identificação, avaliação e mitigação de riscos de negócio, operacionais, regulatórios e de reputação — com mapeamento de matriz de riscos e planos de resposta), e Compliance (conformidade com leis e regulações aplicáveis ao negócio — LGPD, Lei Anticorrupção, normas setoriais da ANVISA, ANS, BACEN, CVM, e outras). O GRC integrado é mais eficaz do que iniciativas isoladas — as três dimensões se reforçam mutuamente."),
        ("Programas de Integridade e Compliance Anticorrupção",
         "A Lei Anticorrupção brasileira (Lei 12.846/2013) responsabiliza objetivamente pessoas jurídicas por atos de corrupção praticados em seu benefício — mesmo sem prova de culpa dos dirigentes. O programa de integridade (compliance anticorrupção) é o principal fator de atenuação de penas previsto na lei. Um programa eficaz inclui: código de conduta e políticas claras, canal de denúncias confidencial e independente, due diligence de fornecedores e parceiros, treinamento periódico de funcionários, análise de risco de corrupção por processo e área de negócio, e monitoramento e auditoria interna. A consultoria estrutura o programa do zero ou avalia e aprimora programas existentes com base no PNLD e nos guias da CGU."),
        ("LGPD: Diagnóstico e Implementação",
         "A LGPD (Lei 13.709/2018) impõe obrigações às empresas que tratam dados pessoais — que na prática são todas as empresas. A consultoria de privacidade conduz: diagnóstico de dados (inventário de quais dados pessoais a empresa coleta, por que, onde armazena, quem acessa e por quanto tempo), análise de base legal para cada tratamento de dados, revisão de contratos com fornecedores que acessam dados pessoais (DPA — Data Processing Agreement), implementação de mecanismos de consentimento e de direitos dos titulares (acesso, correção, exclusão), e elaboração do plano de resposta a incidentes de segurança. A consultoria também apoia a nomeação e capacitação do DPO (Data Protection Officer)."),
        ("Gestão de Riscos: Mapeamento e Matriz",
         "A gestão de riscos estruturada começa pela identificação sistemática dos riscos que ameaçam os objetivos da empresa — riscos estratégicos (concorrência, disrução de mercado), operacionais (falha de processo, fraude interna, acidente), financeiros (inadimplência, câmbio, liquidez), regulatórios (multas, cassação de licença), e de reputação (crise de mídia, escândalo). Para cada risco identificado, a matriz avalia probabilidade e impacto — priorizando os riscos de alta probabilidade e alto impacto para mitigação prioritária. O resultado é o mapa de calor de riscos, que guia onde investir em controles e em seguros. A consultoria facilita workshops de risco com lideranças e constrói o processo de monitoramento contínuo."),
        ("Governança Corporativa para Empresas Familiares e Scale-ups",
         "Empresas familiares em transição para a segunda geração e scale-ups em rápido crescimento têm desafios específicos de governança: separação entre propriedade e gestão, conflito de interesses entre sócios, decisões tomadas informalmente sem registro e sem processo, e ausência de instâncias de supervisão independente. A consultoria estrutura: conselho de administração ou conselho consultivo (com membros independentes que trazem perspectiva externa), acordo de sócios (regras para resolução de conflitos, transferência de participação, saída de sócios), política de dividendos, e processos decisórios formalizados para investimentos e contratações acima de determinado valor. Governança sólida é pré-requisito para captação de investimento e para processos de M&A.")
    ],
    faq_list=[
        ("Programa de compliance é obrigatório por lei?",
         "A Lei Anticorrupção não torna o programa de integridade obrigatório — mas empresas que firmam contratos com o governo federal precisam ter programa de integridade certificado (Lei 12.846 e Decreto 11.129/2022 para contratos acima de determinado valor). Empresas reguladas (bancos, seguradoras, operadoras de saúde) têm obrigações específicas de compliance nos regulamentos setoriais. Independente de obrigação legal, empresas que crescem ou captam investimento são cobradas por investidores e parceiros estratégicos por terem programas de compliance estruturados."),
        ("Qual é a diferença entre auditoria interna e compliance?",
         "Auditoria interna avalia retrospectivamente se os controles e processos estão funcionando conforme projetado — é uma função de asseguração independente que reporta ao conselho de administração. Compliance é uma função prospectiva que orienta e monitora o comportamento da organização para prevenir não conformidades — reporta geralmente ao jurídico ou ao CEO. As duas funções são complementares: compliance estabelece os controles e a auditoria verifica se estão sendo seguidos."),
        ("Quando nomear um DPO (Data Protection Officer)?",
         "A LGPD exige DPO para controladores de dados — mas não especifica porte mínimo. Na prática, toda empresa que trata dados pessoais em escala (clientes, funcionários, fornecedores) deve ter um DPO ou função equivalente. O DPO pode ser interno (funcionário com dedicação parcial ou total) ou externo (consultoria especializada que presta o serviço de DPO as a Service). O DPO é o ponto de contato com a ANPD e com os titulares de dados, e deve ter independência funcional para reportar não conformidades sem represália.")
    ]
)

# Article 4683 — B2B SaaS: Retail and point of sale management
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-varejo-e-ponto-de-venda",
    title="Gestão de Negócios de Empresa de B2B SaaS de Varejo e Ponto de Venda",
    desc="Como estruturar e escalar uma empresa de B2B SaaS de varejo e ponto de venda (PDV): modelo de negócio, diferenciação, go-to-market e métricas de crescimento no mercado de retailtech.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Varejo e Ponto de Venda",
    lead="O varejo brasileiro tem mais de 6 milhões de estabelecimentos comerciais — a grande maioria ainda gerenciando vendas, estoque e finanças de forma manual ou com sistemas ultrapassados. Plataformas de PDV e gestão de varejo têm mercado imenso e demanda estrutural de modernização em todos os segmentos.",
    sections=[
        ("O Mercado de RetailTech e PDV SaaS no Brasil",
         "O mercado de retailtech inclui: sistemas de PDV (ponto de venda) com emissão de NFC-e (cupom fiscal eletrônico), gestão de estoque em tempo real, integração com meios de pagamento (maquininhas, Pix, carteiras digitais), plataformas de e-commerce integradas com o físico (omnichannel), ferramentas de gestão de loja (escala de funcionários, metas de vendedores, relatórios de performance), plataformas de fidelidade e CRM de varejo (programa de pontos, histórico de compras do cliente), e analytics de varejo (giro de estoque, curva ABC, margem por produto). O subsetor de varejo alimentar tem especificidades (pesagem, gestão de perecíveis, nota fiscal por peso) que criam nichos especializados."),
        ("Diferenciação em PDV SaaS",
         "Os diferenciadores mais relevantes incluem: funcionamento offline (PDV que trava quando cai a internet é inaceitável — o varejista não pode parar de vender), emissão de NFC-e e SAT fiscal integrados e atualizados com a legislação de cada estado, integração com múltiplos meios de pagamento (credenciadoras como Cielo, Stone, GetNet e Pix instantâneo), gestão de estoque integrada que desconta automaticamente cada venda, controle de multilojas com visão consolidada, e app móvel para inventário e gestão remota. Para supermercados e mercearias, integração com balança e leitor de código de barras de precisão são obrigatórios."),
        ("Modelo de Receita em Retail SaaS",
         "O modelo combina mensalidade por CNPJ (estabelecimento) com faixas por número de terminais ou usuários. Micro e pequenos varejistas (1 loja, 1 a 2 terminais) pagam de R$80 a R$300/mês; redes com 5 a 20 lojas pagam de R$1.500 a R$8.000/mês. Módulos adicionais como e-commerce integrado, fidelidade, analytics avançado e gestão de múltiplas unidades são cobrados incrementalmente. Take rate sobre meios de pagamento processados pela própria plataforma (modelo de pagamentos embedded) é modelo de receita adicional crescente — a plataforma vira a credenciadora ou o agregador de pagamentos do varejista."),
        ("Go-to-Market para Retail SaaS",
         "O varejista de pequeno porte compra pela indicação de outros varejistas ou de contabilidades que atendem o segmento — o boca a boca ainda é o canal mais eficiente nesse mercado. Canais de revendedores regionais (que instalam, treinam e suportam o sistema localmente) são fundamentais para atingir o varejo pulverizado fora das grandes cidades. Feiras de varejo (Apas Show para supermercados, NRF Brasil, Equipotel para hotelaria) são canais de visibilidade. Para redes de franquias, a venda top-down (para o franqueador que depois obriga ou recomenda o franchisado) é o modelo mais eficiente de escala."),
        ("Métricas de Saúde em Retail SaaS",
         "As métricas operacionais: volume de transações processadas por mês (indicador de engajamento e expansão), uptime do sistema (inaceitável abaixo de 99,5% para um PDV), e NPS de lojistas (especialmente crítico porque lojista insatisfeito reclama publicamente em grupos de WhatsApp e associações do setor). As métricas de negócio incluem receita por loja (ARPU), churn (que em varejo pequeno é alto por fechamento de estabelecimentos e rotatividade de dono), e NRR. Plataformas com modelo de pagamentos embedded têm NRR acima de 100% — o volume de pagamentos cresce com as vendas do varejista, gerando expansão de receita sem ação de vendas adicional.")
    ],
    faq_list=[
        ("O que é NFC-e e todo varejista é obrigado a emitir?",
         "NFC-e (Nota Fiscal de Consumidor Eletrônica) é o documento fiscal eletrônico emitido no varejo para consumidor final, com QR code para consulta. Substituiu o cupom fiscal em papel (ECF) na maioria dos estados. A obrigatoriedade varia por estado e por porte do estabelecimento — mas a tendência é de obrigatoriedade universal para todos os varejistas. Estabelecimentos que emitirem NF-e (para pessoa jurídica) em vez de NFC-e (para consumidor final) estão sujeitos a autuação fiscal."),
        ("Omnichannel é viável para pequenos varejistas?",
         "Omnichannel básico (loja física + loja online integrada com o mesmo estoque) já é viável para varejistas de médio porte com plataformas acessíveis (VTEX, Nuvemshop, WooCommerce integradas ao PDV). O desafio é operacional — gerir o mesmo estoque para dois canais sem ruptura ou overselling. Para varejistas muito pequenos, a presença no WhatsApp Business com catálogo integrado é uma versão simplificada e prática de omnichannel que não exige grande investimento tecnológico."),
        ("Como calcular o giro de estoque ideal para uma loja?",
         "Giro de estoque = Custo dos produtos vendidos / Estoque médio. Um giro de 12 significa que o estoque se renova uma vez por mês. O giro ideal varia por segmento: alimentos perecíveis precisam de giro alto (semanal ou diário), roupas têm giro de 4 a 6 por ano, eletrodomésticos têm giro de 3 a 4 por ano. Curva ABC classifica os produtos por contribuição de receita (A = 80% da receita, B = 15%, C = 5%) — os produtos A exigem reposição prioritária e os C devem ser avaliados para descontinuação se tiverem giro baixo.")
    ]
)

# Article 4684 — Clinic: Dentistry and oral health
art(
    slug="gestao-de-clinicas-de-odontologia-e-saude-bucal",
    title="Gestão de Clínicas de Odontologia e Saúde Bucal",
    desc="Guia completo de gestão para clínicas de odontologia e saúde bucal: organização do fluxo clínico, gestão de agendamento, precificação e indicadores de performance.",
    h1="Gestão de Clínicas de Odontologia e Saúde Bucal",
    lead="O Brasil tem o maior número de dentistas per capita do mundo — mas também um mercado enorme de saúde bucal com grande desigualdade de acesso. Clínicas odontológicas bem gerenciadas combinam atendimento de alta qualidade com eficiência operacional que sustenta crescimento e rentabilidade.",
    sections=[
        ("Abrangência da Odontologia Clínica",
         "A odontologia geral abrange: prevenção e profilaxia (limpeza, fluoretação, orientação de higiene), dentística restauradora (cáries, restaurações em resina e cerâmica), endodontia (tratamento de canal), periodontia (tratamento de gengiva — gengivite, periodontite), próteses (coroas, pontes, próteses totais e parciais removíveis), e extração de dentes (incluindo dentes do siso). Especializações como implantodontia (implantes osseointegrados), ortodontia (aparelhos fixos, removíveis e alinhadores), odontopediatria (crianças), cirurgia bucomaxilofacial, e odontologia estética (facetas, clareamento, lentes de contato dentais) criam subespecialidades de alto ticket e alta demanda."),
        ("Gestão de Agenda e Ocupação",
         "A rentabilidade de uma clínica odontológica é diretamente proporcional à taxa de ocupação da cadeira do dentista — cada horário vazio é receita perdida e custo fixo não coberto. A gestão eficiente de agenda inclui: confirmação de consultas 24 horas antes por WhatsApp automatizado (redução de faltas em 30% a 50%), lista de espera ativa para preencher cancelamentos de última hora, blocos de tempo reservados por tipo de procedimento (procedimentos longos em períodos específicos), e taxa de retorno para recall preventivo (contato com pacientes que estão há mais de 12 meses sem consulta). Softwares de gestão odontológica (Dental Office, Clinicorp, iDental) automatizam essas funcionalidades."),
        ("Implantes e Procedimentos de Alto Ticket",
         "Implantes osseointegrados são o procedimento de maior ticket em odontologia (R$3.000 a R$8.000 por implante) e de maior crescimento — o envelhecimento da população e a popularização da tecnologia expandiram significativamente o mercado. Clínicas com dentistas implantodontistas ou com parceria com especialistas têm acesso a esse mercado de alto valor. O processo de implante (cirurgia de implantação → período de osseointegração → coroa protética) dura 3 a 6 meses — gerando múltiplas visitas e receita recorrente por paciente. Marketing direcionado para pacientes com dentes ausentes ou próteses antigas que podem se beneficiar de implante tem alta taxa de conversão."),
        ("Planos Odontológicos e Particular: Mix e Gestão",
         "Clínicas que atendem planos odontológicos têm volume maior de pacientes mas ticket menor por procedimento — o plano paga tabela fechada que frequentemente não cobre o custo real do procedimento. Clínicas 100% particulares têm ticket maior mas precisam investir mais em captação de pacientes. O mix ideal depende da localização e do posicionamento da clínica: em regiões corporativas com muitos funcionários com plano odontológico, aceitar convênios gera volume que pode ser convertido em procedimentos particulares (implantes, estética — que não são cobertos pelo plano). A gestão financeira deve separar claramente a receita por convênio e particular para calcular a margem real de cada."),
        ("Indicadores de Performance em Odontologia",
         "As métricas essenciais incluem: taxa de ocupação de cadeira por dentista (percentual do tempo disponível com paciente atendido — meta acima de 75%), taxa de faltas e cancelamentos, ticket médio por atendimento, taxa de conversão de procedimentos de alto valor (paciente que consulta sobre implante ou ortodontia e fecha o orçamento), NPS de pacientes e taxa de retorno para recall (percentual de pacientes ativos que voltam para manutenção preventiva nos 12 meses). A análise por dentista — ocupação, ticket médio, taxa de conversão — permite identificar onde cada profissional pode melhorar e quais precisam de suporte em habilidades clínicas ou comerciais.")
    ],
    faq_list=[
        ("Com que frequência devo ir ao dentista?",
         "A recomendação padrão para adultos saudáveis sem problemas periodontais é uma consulta de prevenção a cada 6 meses — incluindo limpeza profissional, avaliação de cáries e orientação de higiene. Pacientes com doença periodontal ativa, diabetes (que aumenta o risco de periodontite), ou histórico de muitas cáries podem precisar de consultas trimestrais. Crianças devem iniciar as consultas ao erupcionar o primeiro dente (por volta de 1 ano de idade) para orientação dos pais e acompanhamento do desenvolvimento dentário."),
        ("Implante dental dói? Quanto tempo dura o processo?",
         "A cirurgia de implante é realizada com anestesia local — o paciente não sente dor durante o procedimento. O desconforto pós-operatório (inchaço e dor leve por 2 a 5 dias) é controlado com analgésicos comuns. O processo completo dura de 3 a 6 meses: 1 a 2 sessões para a cirurgia de implantação, período de osseointegração (o implante se une ao osso — 3 a 5 meses), e 1 a 2 sessões para a colocação da coroa protética. Em casos selecionados (carga imediata), a coroa pode ser colocada na mesma sessão da cirurgia."),
        ("Alinhadores são tão eficazes quanto aparelho fixo?",
         "Para a maioria dos casos de maloclusão leve a moderada, os alinhadores transparentes (Invisalign, 3M Clarity, fabricantes nacionais) têm eficácia comparável ao aparelho fixo convencional. Para casos complexos — discrepâncias esqueléticas graves, rotações dentárias severas, extrusões — o aparelho fixo ainda é mais eficaz. O grande diferencial dos alinhadores é estético (praticamente invisíveis) e de conforto (removíveis para comer e higiene). O custo costuma ser maior do que o aparelho fixo convencional.")
    ]
)

# Article 4685 — SaaS sales: Energy management and sustainability
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-energia-e-sustentabilidade",
    title="Vendas para o Setor de SaaS de Gestão de Energia e Sustentabilidade",
    desc="Estratégias de vendas B2B para plataformas SaaS de gestão de energia e sustentabilidade: como abordar gestores de facilities, ESG e operações para fechar contratos neste mercado em expansão.",
    h1="Vendas para o Setor de SaaS de Gestão de Energia e Sustentabilidade",
    lead="A agenda ESG e a alta dos custos de energia elétrica transformaram gestão de energia e sustentabilidade em prioridade estratégica. Plataformas SaaS para esse mercado entregam redução de custos mensurável e dados que alimentam relatórios de ESG cada vez mais exigidos por investidores e reguladores.",
    sections=[
        ("O Mercado de Energy Management e ESG SaaS",
         "O mercado inclui: plataformas de gestão de energia elétrica (monitoramento de consumo por medidor, identificação de desperdícios, alertas de anomalia), sistemas de gestão de carbono (cálculo de inventário de GEE — Gases de Efeito Estufa — por escopo 1, 2 e 3), plataformas de relatório de sustentabilidade (GRI, SASB, TCFD, CDP), ferramentas de gestão de água e resíduos, plataformas de compra de energia no mercado livre (migrando do mercado cativo para o livre para reduzir tarifas), e soluções de monitoramento de painéis solares fotovoltaicos. O mercado cresce impulsionado pela pressão ESG de investidores, pela exigência de clientes corporativos e pela obrigatoriedade crescente de relatórios de sustentabilidade para empresas de capital aberto."),
        ("O Decisor em Energia e Sustentabilidade",
         "O decisor varia por tipo de solução: para gestão de energia, é o gerente de facilities, o diretor de operações ou o CFO (que sente o custo de energia na DRE); para ESG e relatórios de sustentabilidade, é o diretor de sustentabilidade, o CFO ou o CEO (em empresas com pressão de investidores ou clientes corporativos). O gatilho mais comum para gestão de energia é a conta de luz acima do esperado ou a necessidade de redução de custos. Para ESG, o gatilho é uma solicitação de relatório por um investidor, cliente estratégico ou exigência regulatória."),
        ("Proposta de Valor em Energy & ESG SaaS",
         "Para gestão de energia: redução de 10% a 30% no custo de energia por identificação de desperdícios (equipamentos ligados fora do horário, ar-condicionado ineficiente, fator de potência ruim que gera multa na conta), payback geralmente de 3 a 12 meses. Para compra de energia no mercado livre: redução de 15% a 25% na tarifa de energia para consumidores elegíveis (acima de 500 kW de demanda contratada), com gestão de contratos e risco de preço pela plataforma. Para gestão de carbono: inventário de emissões auditável para relatórios de sustentabilidade, identificação das maiores fontes de emissão para priorizar reduções, e suporte para compra de créditos de carbono certificados para compensação."),
        ("Ciclo de Venda e ROI em Energia SaaS",
         "Para gestão de energia, o ciclo é curto (2 a 6 semanas) quando o CFO ou o facilities manager já tem o problema claro — a conta de energia alta é visível e o ROI de redução é calculável. A demo mais eficaz conecta os medidores de energia do prospect e mostra os dados reais em 30 minutos — o cliente vê imediatamente o padrão de consumo e as oportunidades de economia. Para compra de energia no mercado livre, o ciclo inclui análise da elegibilidade (perfil de consumo, tipo de ligação, vencimento do contrato atual) e negociação com comercializadoras de energia — mais técnico e com ciclo de 1 a 3 meses."),
        ("Retenção e Expansão em Energy & ESG SaaS",
         "Retenção em gestão de energia é alta quando o cliente integrou os medidores e tem dados históricos acumulados — que são necessários para análise de tendência e para relatórios anuais. Para ESG, uma vez que o primeiro inventário de GEE está na plataforma, o cliente precisa da plataforma para os anos seguintes (para mostrar evolução e manter a série histórica). A expansão acontece por adição de sites (novas unidades da empresa monitoradas), por novos módulos (de energia para carbono, de carbono para água e resíduos), e por integrações com plataformas de relato de sustentabilidade externos (CDP, B3 Sustentabilidade).")
    ],
    faq_list=[
        ("O que é mercado livre de energia e quem pode migrar?",
         "O mercado livre de energia permite que consumidores elegíveis comprem energia diretamente de geradores ou comercializadoras — sem passar pela distribuidora local — geralmente com tarifas menores. Com a abertura gradual regulada pela ANEEL, consumidores com demanda acima de 500 kW já podem migrar, e a tendência é de abertura para consumidores menores até 2028. A migração exige contrato com comercializadora, adequação da medição para smart meter e contrato de uso do sistema de distribuição (CUSD). A economia típica é de 15% a 25% versus o mercado cativo."),
        ("Como calcular o inventário de emissões de gases de efeito estufa?",
         "O inventário de GEE segue o Protocolo GHG (Greenhouse Gas Protocol), que classifica as emissões em 3 escopos: Escopo 1 — emissões diretas da empresa (frota própria, caldeiras, processos industriais); Escopo 2 — emissões indiretas por compra de energia elétrica (com base no fator de emissão da rede elétrica nacional); Escopo 3 — outras emissões indiretas (cadeia de fornecedores, viagens de negócio, resíduos, uso do produto pelo cliente). Plataformas de gestão de carbono coletam os dados de consumo de combustível, energia e outros insumos e aplicam os fatores de emissão correspondentes para calcular as toneladas de CO2 equivalente."),
        ("Crédito de carbono é suficiente para uma empresa ser neutra em carbono?",
         "Créditos de carbono devem ser o último recurso, não o primeiro. A ordem correta é: primeiro mensurar as emissões com precisão, depois reduzir as emissões reais (eficiência energética, mudança de modal de transporte, energia renovável), e compensar apenas as emissões residuais que não podem ser reduzidas com créditos de alta integridade (certificados VCS, Gold Standard, REDD+). Empresas que compram créditos sem reduzir as emissões reais estão praticando greenwashing — cada vez mais monitorado e criticado por investidores e reguladores.")
    ]
)

# Article 4686 — Consulting: M&A and corporate transactions
art(
    slug="consultoria-de-fusoes-e-aquisicoes-e-transacoes-corporativas",
    title="Consultoria de Fusões e Aquisições e Transações Corporativas",
    desc="Como consultorias de M&A e transações corporativas ajudam empresas a estruturar, negociar e executar fusões, aquisições, captações de investimento e desinvestimentos.",
    h1="Consultoria de Fusões e Aquisições e Transações Corporativas",
    lead="Fusões, aquisições, captações de investimento e desinvestimentos são momentos definidores na trajetória de uma empresa. Consultorias de M&A guiam os líderes por processos complexos, garantindo que a transação certa seja executada pelo valor certo, com estrutura adequada e proteção dos interesses do cliente.",
    sections=[
        ("O Escopo da Consultoria de M&A",
         "A consultoria de M&A atua em: sell-side (assessorando o vendedor em processos de venda de empresa ou captação de investimento), buy-side (assessorando o comprador na identificação de alvos, due diligence e negociação), fusões e joint ventures (estruturação de combinações estratégicas), levantamento de capital (Series A, B, C para startups; captação de dívida estruturada; acesso ao mercado de capitais via IPO ou emissão de debêntures), e reestruturação societária (compra de participação de sócios, reorganizações holding). O advisorfinanceiro de M&A atua no processo de ponta a ponta: da preparação da empresa para a transação até o fechamento (signing e closing)."),
        ("Valuation: Avaliação de Empresas",
         "O valuation é a fundação de qualquer transação — determinar o valor justo de uma empresa é parte arte e parte ciência. Os métodos mais utilizados incluem: DCF (Discounted Cash Flow — valor presente dos fluxos de caixa futuros projetados, com taxa de desconto refletindo o risco do negócio), múltiplos de mercado (EV/EBITDA, EV/Receita — comparando com empresas similares listadas ou transações comparáveis recentes), e método de ativos ajustados (para empresas com ativos físicos relevantes). Em SaaS e empresas de tecnologia, múltiplos de ARR (Annual Recurring Revenue) são os mais utilizados por investidores — tipicamente de 5x a 20x ARR dependendo da taxa de crescimento, NRR e eficiência. A consultoria conduz o valuation e constrói a narrativa que suporta o valor nos slides de pitch e na negociação."),
        ("O Processo de M&A: Sell-Side",
         "Um processo de venda estruturado (M&A Process) inclui: preparação (organização da documentação financeira, jurídica e operacional — data room), elaboração do teaser e CIM (Confidential Information Memorandum), abordagem e qualificação de potenciais compradores ou investidores, rodada de LOI (Letter of Intent — proposta não vinculante), due diligence aprofundada pelo comprador (2 a 8 semanas), negociação dos contratos definitivos (SPA — Share Purchase Agreement, ou SHA — Shareholders Agreement), e closing (efetivação da transação). O papel da consultoria é proteger o vendedor em cada etapa — garantindo múltiplos compradores em paralelo para manter poder de barganha, revisando todos os documentos e gerenciando o data room."),
        ("Due Diligence: O Processo de Verificação",
         "Due diligence é o processo de verificação realizado pelo comprador antes de fechar a aquisição — investigando financeiro, jurídico, tributário, operacional, tecnológico e recursos humanos da empresa-alvo. A consultoria do sell-side prepara a vendor due diligence (VDD) — que antecipa as perguntas do comprador, identifica e resolve issues previamente, e acelera o processo. Do lado buy-side, a consultoria coordena as diferentes frentes de due diligence (financeira, jurídica, tributária, técnica) e sintetiza os findings em um relatório de riscos que informa a decisão de compra e a negociação de representações e garantias no contrato."),
        ("Captação de Investimento para Scale-ups e Startups",
         "A captação de investimento (fundraising) para startups e scale-ups tem seu próprio processo: preparação do pitch deck e do data room (métricas, projeções financeiras, análise de mercado), abordagem de VCs e investidores estratégicos, gestão de termos de investimento (term sheet — negociação de valuation, anti-dilution, liquidation preference, direitos de voto), e negociação do SHA final. Consultorias de M&A com experiência em venture se diferenciam por ter network de investidores relevantes, entender o que cada fundo procura (tese de investimento, ticket, estágio) e saber posicionar a empresa para o investidor certo.")
    ],
    faq_list=[
        ("Quando devo contratar um assessor de M&A?",
         "O momento ideal é antes de iniciar qualquer conversa com potencial comprador ou investidor — o assessor prepara a empresa para a transação (organiza documentação, resolve issues, maximiza o valuation) e evita que o vendedor negocie de forma desinformada em uma conversa informal que pode comprometer o preço. Empresas que tentam vender sem assessor frequentemente aceitam o primeiro preço oferecido por falta de referência de mercado e de alternativas para criar competição entre compradores."),
        ("M&A serve apenas para grandes empresas?",
         "Não — o mercado de M&A de middle market (empresas com faturamento de R$20 milhões a R$500 milhões) é robusto e crescente no Brasil. Fundos de private equity buscam ativamente empresas de médio porte em setores com bom histórico (saúde, tecnologia, educação, serviços). Empresas familiares em transição de geração, founders que querem liquidez após anos de construção e empreendedores que receberam proposta de aquisição são os casos mais comuns de contratação de assessoria de M&A no middle market."),
        ("Quanto custa uma consultoria de M&A?",
         "Consultorias de M&A cobram sucesso fee (percentual do valor da transação, pago no closing) — geralmente de 2% a 5% para transações de médio porte. Pode haver retainer mensal (R$10.000 a R$50.000) para cobrir os custos de preparação durante o processo, abatido do sucesso fee no closing. Para startups em captação de investimento, a taxa de sucesso é de 3% a 5% do capital captado, às vezes combinada com warrants (direito de comprar ações da empresa a preço favorável).")
    ]
)

# ── Sitemap & trilha updates ──────────────────────────────────────────────────
root = pathlib.Path(__file__).parent
slugs = [
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-construcao-e-gestao-de-obras", "Gestão de Negócios de Empresa de B2B SaaS de Construção e Gestão de Obras"),
    ("gestao-de-clinicas-de-reumatologia-e-doencas-autoimunes", "Gestão de Clínicas de Reumatologia e Doenças Autoimunes"),
    ("vendas-para-o-setor-de-saas-de-seguros-e-insurtech", "Vendas para o Setor de SaaS de Seguros e Insurtech"),
    ("consultoria-de-governanca-risco-e-compliance", "Consultoria de Governança, Risco e Compliance"),
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-varejo-e-ponto-de-venda", "Gestão de Negócios de Empresa de B2B SaaS de Varejo e Ponto de Venda"),
    ("gestao-de-clinicas-de-odontologia-e-saude-bucal", "Gestão de Clínicas de Odontologia e Saúde Bucal"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-energia-e-sustentabilidade", "Vendas para o Setor de SaaS de Gestão de Energia e Sustentabilidade"),
    ("consultoria-de-fusoes-e-aquisicoes-e-transacoes-corporativas", "Consultoria de Fusões e Aquisições e Transações Corporativas"),
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

print("Done — batch 1598")
