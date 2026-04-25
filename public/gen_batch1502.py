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

# Article 4487 — B2B SaaS: Quality management and ISO standards
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-qualidade-e-normas-iso",
    title="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Qualidade e Normas ISO | ProdutoVivo",
    desc="Estratégias para escalar empresas de B2B SaaS especializadas em gestão de qualidade e conformidade com normas ISO, com foco em diferenciação, go-to-market e retenção.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Qualidade e Normas ISO",
    lead="Plataformas de gestão de qualidade e conformidade com normas ISO são SaaS de nicho com alta retenção e clientes de alto valor. Escalar um negócio nesse segmento exige profundo conhecimento do universo de gestão da qualidade, diferenciação por setor e estratégia de canais baseada em auditores e consultores de certificação.",
    sections=[
        ("Mercado de gestão de qualidade e oportunidade de SaaS",
         "Mais de 1 milhão de empresas no Brasil possuem certificação ISO 9001 ou estão em processo de certificação — e todas elas precisam de sistemas para gerenciar processos, documentos, não-conformidades, ações corretivas e auditorias internas. Além da ISO 9001, normas setoriais como ISO 14001 (ambiental), ISO 45001 (segurança do trabalho), IATF 16949 (automotiva) e ISO 27001 (segurança da informação) criam demandas específicas de conformidade que poucos SaaS generalistas atendem adequadamente. O mercado é fragmentado, com muitas empresas ainda usando planilhas e documentos Word para gestão do SGQ."),
        ("Funcionalidades essenciais para SaaS de gestão da qualidade",
         "Gestão de documentos e registros do Sistema de Gestão da Qualidade (com controle de versões, fluxo de aprovação e distribuição controlada), gestão de não-conformidades e reclamações de clientes (com registro, análise de causa raiz e plano de ação corretiva), planejamento e execução de auditorias internas (com checklists, achados e planos de ação), indicadores de qualidade (KPIs de processo, de produto e de satisfação de cliente) e gestão de treinamentos e competências são as funcionalidades nucleares que toda plataforma de SGQ deve oferecer. Módulos de gestão de fornecedores, calibração de equipamentos e controle estatístico de processo (CEP) são diferenciais de plataformas mais completas."),
        ("Segmentação por norma e por setor: a chave para a diferenciação",
         "O mercado de gestão de qualidade pode ser segmentado pela norma de referência (ISO 9001, IATF, ISO 13485 para dispositivos médicos, FSSC para alimentos) ou pelo setor (automotivo, saúde, alimentos, construção, tecnologia). Plataformas que especializam sua terminologia, seus modelos de documentos e seus checklists de auditoria para um setor específico têm vantagem competitiva significativa frente a soluções genéricas. Uma plataforma de SGQ para a indústria de alimentos, com módulos de HACCP e rastreabilidade, compete em um mercado mais definido e com menos concorrentes do que uma plataforma horizontal de qualidade."),
        ("Go-to-market: consultores de certificação e auditores como canal",
         "Consultores especializados em certificação ISO são o canal de distribuição mais eficiente para SaaS de gestão da qualidade: eles têm acesso e credibilidade com dezenas de empresas simultaneamente buscando certificação ou renovação. Desenvolver um programa de parceiros para consultores de certificação — com comissão recorrente, treinamento e materiais de apoio — é uma estratégia de go-to-market de alto leverage. Associações como a ABNT (Associação Brasileira de Normas Técnicas) e organismos de certificação (Bureau Veritas, SGS, Lloyd's Register) são parceiros estratégicos para ganhar visibilidade e credibilidade no setor."),
        ("Retenção e expansão em SaaS de gestão da qualidade",
         "A retenção é naturalmente alta em SaaS de SGQ: todos os documentos, registros e histórico de não-conformidades da empresa estão no sistema, e a migração é complexa e arriscada — especialmente durante auditorias de recertificação. O risco de churn ocorre quando a plataforma não evolui para atender novas versões das normas (como a revisão da ISO 9001:2015 ou futuras atualizações) ou quando uma fusão resulta em consolidação de sistemas. Expansão vem da adição de novas unidades certificadas, de novas normas gerenciadas na mesma plataforma e de módulos avançados como BI de qualidade e integração com ERPs.")
    ],
    faq_list=[
        ("Qual a diferença entre um software de SGQ e um software de gestão de qualidade genérico?",
         "Software de SGQ (Sistema de Gestão da Qualidade) é estruturado especificamente para atender aos requisitos das normas ISO — com módulos de documentos controlados, não-conformidades, ações corretivas e preventivas (CAPA), auditorias internas e indicadores de desempenho alinhados aos requisitos normativos. Software de gestão genérico não tem essa estrutura e exige customizações extensas para atender a uma auditoria de certificação."),
        ("Um SaaS de gestão da qualidade substitui a consultoria de certificação ISO?",
         "Não. O SaaS é uma ferramenta para operacionalizar e manter o SGQ no dia a dia. A consultoria de certificação ajuda a empresa a interpretar os requisitos da norma, a construir o sistema de gestão e a se preparar para as auditorias. Os dois são complementares — e a consultoria frequentemente recomenda (ou implementa) o SaaS como parte do projeto de certificação."),
        ("Como SaaS de gestão de qualidade se adapta a atualizações de normas?",
         "Plataformas bem gerenciadas lançam atualizações de módulos, checklists e templates quando as normas são revisadas, e comunicam essas mudanças proativamente para os clientes. Esse é um serviço de alto valor percebido — a empresa não precisa acompanhar as mudanças normativas por conta própria, pois o sistema evolui junto com os requisitos.")
    ]
)

# Article 4488 — Clinic: Andrology and men's health
art(
    slug="gestao-de-clinicas-de-andrologia-e-saude-masculina",
    title="Gestão de Clínicas de Andrologia e Saúde Masculina | ProdutoVivo",
    desc="Guia completo para gestão eficiente de clínicas especializadas em andrologia e saúde masculina, com foco em perfil de pacientes, infraestrutura, tecnologia e financeiro.",
    h1="Gestão de Clínicas de Andrologia e Saúde Masculina",
    lead="A andrologia e os serviços de saúde masculina atendem uma população historicamente resistente a buscar cuidados médicos preventivos — o que torna o marketing, a comunicação e a experiência do paciente especialmente críticos para o sucesso da clínica. Uma gestão eficiente combina excelência clínica, infraestrutura adequada e estratégias de captação adaptadas ao comportamento masculino.",
    sections=[
        ("Escopo de serviços e perfil dos pacientes",
         "Clínicas de andrologia e saúde masculina atendem condições como disfunção erétil, ejaculação precoce, hipogonadismo e deficiência de testosterona, infertilidade masculina (avaliação de espermograma, vasectomia, reversão de vasectomia), doenças da próstata (hiperplasia prostática benigna, rastreio de câncer de próstata com PSA e exame clínico), terapia de reposição hormonal masculina (TRT) e doenças sexualmente transmissíveis. O paciente típico é um homem entre 35 e 65 anos, frequentemente motivado por queixas específicas — disfunção erétil, redução da libido, sintomas do climatério masculino — mais do que por prevenção proativa."),
        ("Comunicação e marketing adaptados ao público masculino",
         "Homens têm menor propensão a buscar atendimento médico preventivo e frequentemente têm mais resistência a falar abertamente sobre saúde sexual. A comunicação da clínica deve ser direta, sem eufemismos excessivos, com linguagem que normaliza a busca por cuidados e enfatiza os benefícios práticos do tratamento (disposição, performance, qualidade de vida). Conteúdo digital em plataformas como YouTube (vídeos de especialistas respondendo dúvidas frequentes) e Instagram (conteúdo educativo sem sensacionalismo) é o principal canal de captação para esse público. O sigilo e a discrição no atendimento devem ser enfatizados em todas as comunicações."),
        ("Infraestrutura e serviços diagnósticos",
         "A clínica deve oferecer consulta com urologista ou andrologista, avaliação hormonal completa (testosterona total e livre, LH, FSH, prolactina, hemograma e perfil lipídico), espermograma e análise seminal avançada, avaliação urodinâmica (para disfunção miccional), ecografia de próstata e testículos com Doppler (para avaliação de fluxo vascular peniano em casos de disfunção erétil vascular) e biopsia de próstata quando indicada. Serviços de infertilidade masculina — coleta e análise seminal, criopreservação de espermatozoides — são um diferencial de clínicas especializadas em reprodução assistida do lado masculino."),
        ("Gestão da jornada do paciente e fidelização",
         "A jornada do paciente em andrologia frequentemente começa com vergonha ou desconforto em buscar ajuda. A clínica deve criar um ambiente de acolhimento desde o primeiro contato: agendamento discreto (online ou por WhatsApp sem necessidade de detalhar o motivo da consulta), recepção sem exposição desnecessária em sala de espera coletiva e comunicação empática em todos os touchpoints. A fidelização é alta quando o tratamento gera resultados percebidos — o que reforça a importância de acompanhamento ativo, reavaliação periódica e ajustes de tratamento quando necessário."),
        ("Financeiro e estratégias de receita em clínicas de andrologia",
         "Clínicas de andrologia têm um perfil financeiro favorável: muitos dos serviços mais demandados (terapia de reposição hormonal, tratamento de disfunção erétil, infertilidade) têm cobertura parcial ou inexistente pelos planos de saúde, o que cria um mercado particular de alto valor. Pacotes de acompanhamento de TRT (consulta + exames periódicos + ajuste de dose), programas de saúde masculina preventiva e pacotes de avaliação de fertilidade são modelos de receita recorrente que aumentam o LTV do paciente e a previsibilidade financeira da clínica.")
    ],
    faq_list=[
        ("Qual a diferença entre urologista e andrologista?",
         "A urologia é a especialidade médica que trata doenças do sistema urinário e do aparelho reprodutor masculino. A andrologia é uma subespecialidade da urologia focada especificamente na saúde reprodutiva e sexual masculina — infertilidade, disfunção sexual, hipogonadismo e alterações hormonais. Muitos urologistas têm formação adicional em andrologia; em clínicas especializadas, o médico se apresenta como andrologista."),
        ("Quais exames são fundamentais para rastreio de saúde masculina após os 40 anos?",
         "PSA (antígeno prostático específico) anual após os 45 anos (ou 40 para homens de alto risco), testosterona total sérica, hemograma completo, perfil lipídico e glicemia, pressão arterial e avaliação cardiovascular são os exames de rastreio recomendados. Homens com sintomas de hipogonadismo (fadiga, redução de libido, alterações de humor) devem incluir testosterona livre, LH, FSH e prolactina na avaliação hormonal inicial."),
        ("A terapia de reposição hormonal masculina (TRT) é segura?",
         "A TRT é segura e eficaz quando indicada por especialista, após avaliação cuidadosa de indicações, contraindicações e com monitoramento periódico. Contraindicações incluem câncer de próstata ativo, eritrocitose grave e desejo de fertilidade futura (pois a TRT suprime a espermatogênese). O acompanhamento regular com hemograma, PSA e avaliação cardiovascular é parte obrigatória do protocolo de TRT.")
    ]
)

# Article 4489 — SaaS sales: Transplant and post-transplant centers
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-centros-de-transplante-e-pos-transplante",
    title="Vendas para o Setor de SaaS de Gestão de Centros de Transplante e Pós-Transplante | ProdutoVivo",
    desc="Estratégias de vendas B2B para plataformas SaaS voltadas à gestão de centros de transplante e acompanhamento pós-transplante, com foco em ciclo de vendas e proposta de valor.",
    h1="Vendas para o Setor de SaaS de Gestão de Centros de Transplante e Pós-Transplante",
    lead="Centros de transplante e serviços de acompanhamento pós-transplante são ambientes de altíssima complexidade clínica, com protocolos rigorosos de imunossupressão, rastreio de rejeição e manejo de complicações infecciosas. Vender SaaS para esse segmento exige expertise clínica, capacidade técnica de integração e disposição para ciclos de venda longos em hospitais terciários.",
    sections=[
        ("Particularidades do cuidado pós-transplante e suas necessidades de gestão",
         "O acompanhamento de pacientes transplantados é um dos processos mais complexos da medicina: os pacientes permanecem em imunossupressão por toda a vida, com esquemas terapêuticos que precisam ser ajustados conforme parâmetros clínicos e laboratoriais. Monitorar níveis de imunossupressores (tacrolimus, ciclosporina, micofenolato), função do órgão transplantado (creatinina para rim, transaminases para fígado, BNP para coração), rastreio de infecções oportunistas e detecção precoce de rejeição aguda ou crônica são tarefas que exigem sistemas capazes de integrar dados de múltiplas fontes e alertar a equipe clínica de desvios de protocolo."),
        ("Perfil dos decisores e processo de compra em centros de transplante",
         "Os centros de transplante no Brasil são concentrados em hospitais de alta complexidade — universitários e grandes hospitais privados e filantrópicos — com regulação federal rigorosa (credenciamento pelo Ministério da Saúde via SNT). Os decisores são o coordenador médico do programa de transplante, o gestor hospitalar de TI e, em grupos hospitalares, o comitê de tecnologia corporativo. O processo de compra inclui avaliação de conformidade com protocolos do SNT, análise de integração com o prontuário hospitalar e negociação de contrato com cláusulas específicas de disponibilidade e suporte crítico."),
        ("Proposta de valor: protocolos, alertas e rastreabilidade",
         "O argumento central deve ser a automação de protocolos clínicos de pós-transplante: alertas automáticos para resultados laboratoriais fora do alvo (nível de tacrolimus, creatinina, citomegalovírus), lembretes de exames periódicos obrigatórios (biopsias de protocolo, sorologias), registro de ajustes de imunossupressor com rastreabilidade completa e geração de relatórios para auditorias do SNT. A redução do risco de rejeição não detectada precocemente — com impacto direto na sobrevida do enxerto e do paciente — é o argumento de maior impacto clínico e financeiro para os tomadores de decisão."),
        ("Estratégias de prospecção em centros de transplante",
         "O mercado de transplante no Brasil é altamente concentrado: há pouco mais de 300 centros credenciados, com grande concentração em São Paulo, Rio de Janeiro, Minas Gerais e Rio Grande do Sul. A prospecção deve ser altamente personalizada e baseada em relacionamento — participação no Congresso Brasileiro de Transplantes (CBT), publicações técnicas em revistas de transplante e parcerias com coordenadores de transplante de renome são os canais mais eficazes. Referências de outros centros de transplante que já usam o sistema são o ativo comercial mais valioso nesse segmento."),
        ("Suporte crítico e conformidade regulatória em programas de transplante",
         "Sistemas de gestão de transplante devem atender aos requisitos de documentação do SNT (Sistema Nacional de Transplantes), incluindo registros de captação de órgãos, listas de espera e resultados de transplantes. SLAs de alta disponibilidade (uptime de 99,95%), suporte 24/7 com resposta imediata para incidentes críticos e planos de contingência documentados são requisitos contratuais obrigatórios. A conformidade com LGPD — especialmente na gestão de dados de doadores e receptores — é pré-requisito não negociável.")
    ],
    faq_list=[
        ("Quais são os principais tipos de transplante gerenciados em centros credenciados no Brasil?",
         "Rim (o mais frequente, com mais de 6.000 transplantes por ano no Brasil), fígado (aproximadamente 2.000 por ano), coração, pulmão, pâncreas e medula óssea (transplante de células-tronco hematopoiéticas) são os principais tipos. Cada modalidade tem protocolos de acompanhamento distintos, com parâmetros laboratoriais e clínicos específicos."),
        ("Como um SaaS pode ajudar na gestão da fila de espera para transplante?",
         "Automatizando a atualização de dados dos pacientes na lista (situação clínica, exames atualizados, urgência), gerando alertas quando um paciente precisa de reavaliação para manutenção na lista e integrando com o BNAFAR e o SNT para notificação de órgãos disponíveis. A redução de erros e atrasos na comunicação com o SNT pode melhorar o acesso a órgãos para os pacientes da lista."),
        ("Qual a diferença entre o acompanhamento pós-transplante renal e o de outros órgãos?",
         "O transplante renal é o mais padronizado e protocolizado — com esquemas de imunossupressão bem definidos e biopsias de protocolo em momentos específicos. Fígado e coração têm protocolos distintos, com parâmetros laboratoriais e de imagem diferentes para avaliação de função e rejeição. Pulmão é o transplante com maior risco de complicações tardias (bronquiolite obliterante) e exige monitoramento de função pulmonar muito frequente. Um SaaS robusto deve suportar os protocolos de acompanhamento de múltiplas modalidades de transplante.")
    ]
)

# Article 4490 — Consulting: Customer experience and CX journey
art(
    slug="consultoria-de-experiencia-do-cliente-e-jornada-cx",
    title="Consultoria de Experiência do Cliente e Jornada CX | ProdutoVivo",
    desc="Como estruturar e posicionar uma consultoria especializada em experiência do cliente e jornada CX, com metodologias, ferramentas e estratégias para gerar impacto real nos negócios.",
    h1="Consultoria de Experiência do Cliente e Jornada CX",
    lead="A experiência do cliente (CX) tornou-se um dos principais vetores de diferenciação competitiva em mercados onde produto e preço estão cada vez mais comoditizados. Consultorias especializadas em CX ajudam as empresas a mapear, projetar e otimizar cada ponto de contato com o cliente — da descoberta ao pós-venda — para construir lealdade e impulsionar crescimento sustentável.",
    sections=[
        ("O que é CX e por que as empresas investem em consultoria",
         "Experiência do cliente (Customer Experience, CX) é a percepção total que um cliente tem de uma empresa ao longo de todas as interações — desde o primeiro anúncio visto até o suporte após a compra. Empresas líderes em CX têm maior NPS, menor churn, maior LTV e crescem mais rápido do que concorrentes com experiência mediana. Consultorias de CX são acionadas quando a empresa percebe que seus clientes estão insatisfeitos (alto churn, NPS baixo, reclamações recorrentes), quando quer se diferenciar da concorrência ou quando está lançando um novo produto ou canal e quer garantir uma experiência consistente desde o início."),
        ("Mapeamento da jornada do cliente: a base do diagnóstico",
         "O Customer Journey Map (mapa da jornada do cliente) é a ferramenta central da consultoria de CX: representa de forma visual cada etapa que o cliente percorre, os pontos de contato com a empresa em cada etapa, as expectativas e emoções do cliente em cada momento e os gaps entre o que a empresa entrega e o que o cliente espera. Construir um journey map preciso exige pesquisa com clientes reais (entrevistas, pesquisas de satisfação, análise de dados de comportamento) e não pode ser feito apenas com a perspectiva interna da empresa. Os momentos de verdade — os pontos de contato que têm maior impacto positivo ou negativo na percepção do cliente — são priorizados para intervenção."),
        ("Design de experiência e prototipagem de soluções",
         "Com o mapa de jornada e os momentos críticos identificados, a consultoria aplica metodologias de design de serviço para projetar soluções: Service Blueprint (que mapeia os processos internos que suportam cada touchpoint do cliente), Design Thinking para geração e teste de ideias e prototipagem rápida de novos fluxos de atendimento, produtos e comunicações. A co-criação com clientes reais no processo de design aumenta a aderência das soluções e reduz o risco de implementar melhorias que não impactam o que o cliente realmente valoriza."),
        ("Implementação de métricas e cultura de CX",
         "A consultoria deve apoiar a empresa na definição e implementação de um sistema de métricas de CX: NPS (Net Promoter Score) por etapa da jornada, CSAT (Customer Satisfaction Score) por ponto de contato, CES (Customer Effort Score) para avaliar facilidade de uso, e métricas de negócio correlacionadas (churn, LTV, taxa de recompra). Mais do que medir, é fundamental criar uma cultura de obsessão pelo cliente — com loops de feedback estruturados que levam insights de clientes até as equipes que tomam decisões de produto, processo e atendimento."),
        ("Modelo de negócio e diferenciação de consultorias de CX",
         "Consultorias de CX podem se especializar por setor (varejo, serviços financeiros, saúde, SaaS, hotelaria) ou por tipo de serviço (diagnóstico de jornada, design de serviço, implementação de métricas, treinamento de equipes de atendimento). Projetos de diagnóstico (journey mapping) são o serviço de entrada; projetos de redesign de experiência e acompanhamento de implementação geram receita recorrente. Certificações em metodologias reconhecidas (CX Professional da CXPA, Design Thinking da IDEO) e publicação de cases com resultados mensuráveis (aumento de NPS, redução de churn) são os principais ativos de credibilidade.")
    ],
    faq_list=[
        ("Qual a diferença entre CX e atendimento ao cliente?",
         "Atendimento ao cliente é uma das etapas da jornada — geralmente o suporte pós-venda. CX é a experiência total: inclui o marketing que atraiu o cliente, a facilidade de compra, o processo de entrega ou onboarding, o uso do produto e o suporte. Uma empresa pode ter um atendimento excelente e uma CX ruim, se o produto é difícil de usar ou o processo de compra é frustrante."),
        ("Como mensurar o impacto financeiro de melhorias em CX?",
         "Correlacionando NPS com churn e LTV: clientes promotores (NPS alto) têm churn significativamente menor e fazem mais indicações, reduzindo o CAC. Estudos da Bain & Company e da Harvard Business Review mostram que um aumento de 5 pontos no NPS está correlacionado com crescimento de receita de 2 a 7%, dependendo do setor. Modelos financeiros que traduzem melhorias de NPS em impacto de receita são ferramentas poderosas para justificar investimentos em CX."),
        ("Quanto tempo leva um projeto de mapeamento e redesign de jornada do cliente?",
         "Um projeto de diagnóstico (entrevistas com clientes, mapeamento de jornada, identificação de momentos críticos e recomendações) leva de 4 a 8 semanas. Um projeto completo de redesign de experiência — do diagnóstico à prototipagem, teste com clientes e plano de implementação — leva de 3 a 6 meses. O acompanhamento da implementação e a medição de resultados se estendem por 6 a 12 meses adicionais.")
    ]
)

# Article 4491 — B2B SaaS: Compliance and GRC platforms
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-plataformas-de-compliance-e-grc",
    title="Gestão de Negócios de Empresa de B2B SaaS de Plataformas de Compliance e GRC | ProdutoVivo",
    desc="Estratégias para escalar empresas de B2B SaaS especializadas em compliance e GRC (Governança, Risco e Compliance), com foco em diferenciação, go-to-market e retenção de clientes.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Plataformas de Compliance e GRC",
    lead="Plataformas de compliance e GRC (Governança, Risco e Compliance) são SaaS de alto valor para empresas que precisam gerenciar riscos regulatórios, operacionais e éticos de forma centralizada. Escalar um negócio nesse segmento exige diferenciação regulatória, estratégia de vendas enterprise e capacidade de demonstrar redução de risco como ROI.",
    sections=[
        ("Mercado de GRC e oportunidade para SaaS especializados",
         "O mercado global de GRC software supera US$ 30 bilhões e cresce mais de 12% ao ano, impulsionado pela crescente complexidade regulatória (LGPD, Lei Anticorrupção, normas do BACEN, ANS, CVM), pela digitalização dos processos de compliance e pela pressão de investidores e conselhos de administração por maior visibilidade sobre riscos corporativos. No Brasil, o mercado ainda é relativamente imaturo — com muitas empresas gerenciando compliance e riscos em planilhas — o que representa oportunidade para plataformas nativas que entendem o contexto regulatório brasileiro."),
        ("Funcionalidades nucleares de uma plataforma de GRC",
         "Gestão de riscos (mapeamento, avaliação, tratamento e monitoramento de riscos corporativos em um framework integrado), gestão de políticas e controles internos (com fluxo de aprovação, publicação e ateste de leitura por colaboradores), canal de denúncias com gestão de investigações (integrado à plataforma, com anonimato garantido), due diligence de terceiros (fornecedores, parceiros, agentes), gestão de contratos de compliance e monitoramento de indicadores regulatórios são os módulos que formam o núcleo de uma plataforma de GRC robusta. Integração com fontes externas de dados de risco (listas de sanções, PEPs, certidões de antecedentes) é um diferencial importante para due diligence."),
        ("Segmentação e posicionamento no mercado de compliance",
         "O mercado de GRC pode ser segmentado por porte (enterprise vs. PME) ou por setor regulado (financeiro, saúde, energia, construção, agronegócio). Empresas do setor financeiro — bancos, seguradoras, fintechs regulados pelo BACEN — têm as demandas mais específicas e os orçamentos mais altos para compliance. A LGPD criou demanda transversal por funcionalidades de gestão de dados pessoais e privacidade em plataformas de GRC de todos os setores. Posicionar a plataforma como o sistema de registro (system of record) para compliance reduz o churn e aumenta o valor percebido."),
        ("Go-to-market e vendas enterprise para plataformas de GRC",
         "O ciclo de vendas de GRC enterprise é longo (6 a 18 meses) e envolve múltiplos stakeholders: Chief Compliance Officer, Chief Risk Officer, CISO (para aspectos de segurança da informação), CFO e Conselho de Administração. A abordagem de vendas deve ser consultiva — demonstrando conhecimento do ambiente regulatório do cliente, não apenas funcionalidades do produto. Thought leadership (publicações, participação em eventos de compliance, parcerias com associações como o IBGC e a ANEFAC) é o principal canal de geração de leads qualificados nesse mercado."),
        ("Retenção e expansão em plataformas de GRC",
         "A retenção é alta em plataformas de GRC quando o sistema se torna o repositório central de todos os dados de risco, políticas e investigações da empresa — migrar esse histórico é custoso e arriscado do ponto de vista regulatório. Expansão vem da adição de novos módulos (novos regulamentos para conformidade, novos países para empresas multinacionais), do aumento de usuários com o crescimento da empresa e da integração com ERPs e sistemas de gestão de desempenho para correlacionar riscos com resultados operacionais.")
    ],
    faq_list=[
        ("O que é GRC e como ele se aplica na gestão empresarial?",
         "GRC (Governança, Risco e Compliance) é uma abordagem integrada que alinha a governança corporativa (estrutura de decisão e responsabilidade), a gestão de riscos (identificação e tratamento de ameaças e oportunidades) e o compliance (conformidade com leis e normas) em um framework unificado. Plataformas de GRC centralizam esses três pilares em um sistema único, eliminando silos e oferecendo visão integrada do perfil de risco da organização."),
        ("Qual a diferença entre uma plataforma de GRC e uma ferramenta de auditoria interna?",
         "Ferramentas de auditoria interna focam em planejamento, execução e registro de auditorias e são usadas principalmente pela função de auditoria interna. Plataformas de GRC são mais amplas: incluem a gestão de riscos corporativos, políticas de compliance, canal de denúncias, due diligence de terceiros e monitoramento de controles — abrangendo toda a organização, não apenas a função de auditoria."),
        ("LGPD exige uma plataforma de GRC específica?",
         "A LGPD não exige uma plataforma específica, mas determina que as empresas tenham estrutura para mapear dados pessoais, gerir consentimentos, registrar incidentes de segurança e responder a solicitações de titulares de dados. Muitas plataformas de GRC têm módulos específicos de privacidade e LGPD que automatizam esses processos e geram evidências de conformidade para fiscalizações da ANPD (Autoridade Nacional de Proteção de Dados).")
    ]
)

# Article 4492 — Clinic: Immunology and clinical allergy
art(
    slug="gestao-de-clinicas-de-imunologia-e-alergia-clinica",
    title="Gestão de Clínicas de Imunologia e Alergia Clínica | ProdutoVivo",
    desc="Guia completo para gestão eficiente de clínicas especializadas em imunologia e alergia clínica, com foco em infraestrutura, protocolos assistenciais, tecnologia e financeiro.",
    h1="Gestão de Clínicas de Imunologia e Alergia Clínica",
    lead="Clínicas de imunologia e alergia clínica atendem uma das condições de maior prevalência na população brasileira — rinite alérgica afeta mais de 25% dos brasileiros e asma tem prevalência de 10-12%. Uma gestão eficiente nessa especialidade garante qualidade assistencial, fluxo ágil de pacientes e sustentabilidade financeira em um ambiente de alta demanda.",
    sections=[
        ("Escopo de atendimento e condições tratadas",
         "Clínicas de imunologia e alergia clínica atendem rinite alérgica, sinusite crônica, asma brônquica, urticária e angioedema, dermatite atópica, alergia alimentar (incluindo anafilaxia), hipersensibilidade a medicamentos (como alergia à penicilina e a anti-inflamatórios), alergia a insetos (himenópteros) e imunodeficiências primárias (em centros de referência). O público é amplo — de lactentes com dermatite atópica a adultos com doença pulmonar obstrutiva crônica de base alérgica — o que exige capacidade de adaptação da abordagem clínica e da comunicação para diferentes faixas etárias e perfis."),
        ("Infraestrutura e testes diagnósticos essenciais",
         "A clínica de alergia deve ter infraestrutura para testes cutâneos de leitura imediata (prick test) para aeroalérgenos (pólen, ácaros, fungos, epitélios de animais) e alimentos, além de testes intradérmicos quando indicados. Para hipersensibilidade a medicamentos, testes de provocação oral (TPO) em ambiente controlado com monitoramento de reações são o padrão diagnóstico. A disponibilidade de epinefrina e equipamento de ressuscitação é obrigatória para qualquer clínica que realiza testes de provocação ou imunoterapia. Medidas objetivas de função pulmonar — espirometria, Peak Flow — são complementares para avaliação da asma."),
        ("Imunoterapia alérgeno-específica: gestão e logística",
         "A imunoterapia subcutânea (ITSC) ou sublingual (ITSL) é o único tratamento que modifica a doença alérgica, induzindo tolerância ao alérgeno. A imunoterapia subcutânea exige que o paciente compareça regularmente à clínica para aplicação das doses (fase de atualização) e depois mensalmente para doses de manutenção — por 3 a 5 anos. Gerenciar esse fluxo de pacientes em imunoterapia — agendamento de doses, controle de esquema, observação pós-aplicação de 30 minutos, registro de reações locais e sistêmicas — é um dos maiores desafios operacionais de clínicas de alergia de alto volume. Sistemas de prontuário com módulos específicos de imunoterapia reduzem significativamente o risco de erros e o tempo administrativo."),
        ("Gestão de urgências: anafilaxia e protocolos de emergência",
         "Clínicas de alergia têm risco real de reações anafiláticas durante testes de provocação e imunoterapia. Protocolos de emergência claros, treinamento da equipe para reconhecimento e tratamento da anafilaxia (com epinefrina intramuscular como primeira linha), kit de emergência sempre disponível e verificação periódica do vencimento dos medicamentos são obrigações não negociáveis. O registro de todas as reações — com gravidade, tratamento realizado e evolução — no prontuário é fundamental para a segurança clínica e para ajustes no protocolo de imunoterapia."),
        ("Gestão financeira e modelos de reembolso em imunologia e alergia",
         "Testes cutâneos, espirometria e consultas de alergia têm cobertura pelos principais planos de saúde. A imunoterapia subcutânea exige negociação específica com operadoras — a tabela TUSS prevê honorários para a aplicação e o monitoramento, mas a cobertura do extrato alergênico varia entre as operadoras. Clínicas que atendem imunoterapia em alto volume podem negociar protocolos de cobertura diretamente com as maiores operadoras, incluindo os extratos como parte do procedimento. O controle de estoque de extratos alergênicos — que têm validade limitada e precisam de refrigeração — é uma especificidade logística importante.")
    ],
    faq_list=[
        ("O que é imunoterapia alérgena e quem pode se beneficiar?",
         "Imunoterapia alérgena (vacina de alergia) é o único tratamento que modifica a história natural da doença alérgica, reduzindo a sensibilidade ao alérgeno e prevenindo o desenvolvimento de novos alérgenos e de asma em pacientes com rinite. É indicada para pacientes com rinite alérgica ou asma alérgica moderada a grave que não têm controle adequado apenas com medicamentos, e cuja alergia foi confirmada por testes cutâneos ou exames de sangue (IgE específica)."),
        ("Como saber se meu filho tem alergia alimentar ou intolerância alimentar?",
         "Alergia alimentar é uma resposta imunológica (mediada por IgE) a proteínas específicas de alimentos — com sintomas que vão de urticária e vômitos a anafilaxia, geralmente de início rápido após a ingestão. Intolerância alimentar (como intolerância à lactose) é uma reação não imunológica, geralmente com sintomas digestivos de início mais gradual. O diagnóstico diferencial é feito pelo alergista com base na história clínica, testes cutâneos, dosagem de IgE específica e teste de provocação oral quando necessário."),
        ("Rinite alérgica tem cura?",
         "Rinite alérgica não tem cura no sentido de eliminação permanente da predisposição genética à alergia. No entanto, com imunoterapia alérgena bem indicada e conduzida, muitos pacientes alcançam remissão prolongada dos sintomas e redução significativa da necessidade de medicamentos — com benefícios que podem persistir por anos após o término da vacina. O controle ambiental (redução da exposição aos alérgenos) e o tratamento farmacológico são a base do manejo para todos os pacientes.")
    ]
)

# Article 4493 — SaaS sales: Hypnotherapy and integrative therapy clinics
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-hipnoterapia-e-terapias-integrativas",
    title="Vendas para o Setor de SaaS de Gestão de Clínicas de Hipnoterapia e Terapias Integrativas | ProdutoVivo",
    desc="Estratégias de vendas B2B para plataformas SaaS voltadas à gestão de clínicas de hipnoterapia e terapias integrativas, com abordagem consultiva, argumentos de valor e retenção.",
    h1="Vendas para o Setor de SaaS de Gestão de Clínicas de Hipnoterapia e Terapias Integrativas",
    lead="Clínicas de hipnoterapia e terapias integrativas — que incluem práticas como meditação clínica, EMDR, terapia de vidas passadas, reiki terapêutico e constelação familiar — atendem um mercado em expansão, com crescente interesse por abordagens complementares de saúde mental e bem-estar. Vender SaaS para esse nicho exige sensibilidade à cultura do setor e proposta de valor adaptada às suas especificidades.",
    sections=[
        ("Perfil do mercado de terapias integrativas e complementares",
         "O mercado de Práticas Integrativas e Complementares em Saúde (PICS) cresceu significativamente no Brasil após a incorporação de 29 práticas pelo SUS (Portaria 849/2017) e pela crescente procura particular por abordagens como hipnoterapia, EMDR (Eye Movement Desensitization and Reprocessing), mindfulness clínico e terapias corporais. O profissional típico é um psicólogo, terapeuta holístico ou médico com formação complementar em práticas integrativas, que atua em consultório individual ou em clínicas multidisciplinares de saúde integrativa. O público buscado é adulto, com interesse em saúde mental, bem-estar e crescimento pessoal."),
        ("Dores operacionais de clínicas de terapias integrativas",
         "As principais dores são: dificuldade em gerenciar agendas com sessões de diferentes durações (hipnoterapia pode ter sessões de 60 a 90 minutos, meditação em grupo de 30 a 60 minutos), controle financeiro de sessões individuais e grupos terapêuticos com cobranças diferentes, ausência de sistema de prontuário adaptado ao contexto das terapias integrativas (sem a terminologia médica convencional), e dificuldade em comunicar com clientes entre sessões para reforço de práticas e acompanhamento de progresso."),
        ("Argumentos de valor para plataformas de gestão de clínicas integrativas",
         "Agenda online acessível 24h pelos clientes (com opção de escolha de terapeuta, modalidade e duração de sessão), cobranças automatizadas com link de pagamento enviado por WhatsApp, prontuário flexível (sem obrigatoriedade de estrutura médica tradicional, permitindo registros narrativos e observações de evolução no formato do terapeuta), comunicação automatizada com clientes (lembretes de sessão, envio de áudios de meditação guiada ou materiais entre sessões) e controle de pacotes de sessões com saldo restante são os diferenciais mais valorizados."),
        ("Canais de prospecção e comunidades de profissionais de saúde integrativa",
         "Grupos e comunidades de hipnoterapeutas (ABH — Associação Brasileira de Hipnose), psicólogos com formação em EMDR (EMDR Brasil), profissionais de mindfulness e meditação clínica e terapeutas holísticos no Instagram e YouTube são os canais mais eficazes. Conteúdo sobre gestão de consultório para terapeutas integrativas — como organizar finanças, como profissionalizar o atendimento, como fidelizar clientes — atrai leads qualificados com alto interesse em soluções de gestão. Parceiros de cursos de formação em terapias integrativas, que recomendam a plataforma para seus alunos ao final da formação, são um canal de baixo CAC e alta conversão."),
        ("Retenção e crescimento no segmento de terapias integrativas",
         "A retenção é alta quando o profissional incorpora a plataforma como centro da sua operação — agenda, prontuário e cobrança. O risco de churn é maior nos primeiros 60 dias, quando o hábito ainda não foi formado. Onboarding com tutoriais em vídeo curtos, suporte por WhatsApp e comunidade de usuários onde profissionais compartilham boas práticas aceleram a adoção. Crescimento vem quando o profissional abre espaço com múltiplos terapeutas, lança grupos terapêuticos com gestão de inscrições ou passa a vender cursos e mentorias pela plataforma.")
    ],
    faq_list=[
        ("Um SaaS de gestão de consultório genérico atende às necessidades de terapeutas integrativos?",
         "Parcialmente. Funcionalidades básicas como agenda e cobrança são comuns a qualquer SaaS de consultório. Mas terapeutas integrativos têm necessidades específicas: prontuário sem estrutura médica obrigatória, gestão de grupos terapêuticos, cobrança de pacotes e integração com ferramentas de comunicação para envio de materiais entre sessões. Plataformas que atendem especificamente esse perfil têm aderência muito maior."),
        ("Como a plataforma pode apoiar a comunicação entre terapeuta e cliente fora das sessões?",
         "Com módulos de comunicação integrada: envio de mensagens personalizadas, materiais em PDF (protocolos de meditação, registros de emoções, exercícios de respiração), áudios de meditação guiada ou links de vídeo — tudo dentro da plataforma, sem necessidade de aplicativos externos. Esse tipo de acompanhamento entre sessões aumenta significativamente a adesão ao processo terapêutico e a percepção de valor pelo cliente."),
        ("Hipnoterapia e EMDR precisam de prontuário formal?",
         "Psicólogos que praticam EMDR ou hipnose clínica são obrigados pelo CFP a manter prontuário psicológico conforme a Resolução CFP 01/2009. Terapeutas holísticos sem formação em psicologia não têm obrigação legal de prontuário formal, mas a documentação dos atendimentos é recomendada para proteção do próprio profissional e para continuidade do cuidado. Plataformas flexíveis atendem tanto os que precisam de prontuário formal quanto os que preferem um registro mais livre.")
    ]
)

# Article 4494 — Consulting: Growth strategy and scale-up
art(
    slug="consultoria-de-estrategia-de-crescimento-e-scale-up",
    title="Consultoria de Estratégia de Crescimento e Scale-Up | ProdutoVivo",
    desc="Como estruturar e posicionar uma consultoria especializada em estratégia de crescimento e scale-up, com metodologias, ferramentas e estratégias para ajudar empresas a crescer de forma acelerada e sustentável.",
    h1="Consultoria de Estratégia de Crescimento e Scale-Up",
    lead="Crescer de forma acelerada e sustentável é o desafio central de startups em fase de tração e scale-ups que buscam consolidar sua posição de mercado. Consultorias especializadas em estratégia de crescimento ajudam as empresas a identificar as alavancas certas, priorizar iniciativas com base em dados e construir os sistemas e processos necessários para escalar sem perder qualidade ou cultura.",
    sections=[
        ("O que diferencia consultoria de crescimento de consultoria estratégica tradicional",
         "Consultoria estratégica tradicional foca em diagnóstico de mercado, análise competitiva e definição de direcionamento de longo prazo — com entregáveis que frequentemente são relatórios e apresentações. Consultoria de crescimento e scale-up é mais operacional e orientada a experimentos: ajuda a empresa a identificar as alavancas de crescimento mais promissoras (aquisição, ativação, retenção, receita, referência — o framework AARRR de Dave McClure), priorizar hipóteses com base em dados, executar experimentos com ciclos rápidos e escalar o que funciona. O ciclo é: aprender → priorizar → executar → medir → iterar."),
        ("Diagnóstico de crescimento: identificando os gargalos reais",
         "O diagnóstico começa com análise de dados: funil de aquisição (de onde vêm os leads, qual a taxa de conversão em cada etapa), coortes de retenção (qual percentual de clientes está ativo após 30, 60 e 90 dias), análise de churn (quem cancela, quando e por quê), análise de expansão (quais clientes expandem, o que os diferencia dos que churn) e análise de referral (qual percentual de novos clientes vem de indicações). Esse diagnóstico revela onde está o gargalo de crescimento — frequentemente não onde a empresa acredita que está."),
        ("Priorização de iniciativas e metodologia de growth",
         "Com o diagnóstico em mãos, a consultoria facilita o processo de geração e priorização de hipóteses de crescimento usando frameworks como ICE Score (Impact, Confidence, Ease) ou RICE (Reach, Impact, Confidence, Effort). O backlog de experimentos de crescimento deve ser priorizado, executado com metodologia de teste A/B ou MVP e avaliado com métricas claras de sucesso definidas antes do início. A disciplina de documentar os aprendizados de cada experimento — inclusive os que não funcionaram — é fundamental para acelerar o ciclo de aprendizagem."),
        ("Construção de capabilities de crescimento na organização",
         "Além de entregar resultados imediatos, a consultoria de crescimento deve construir capacidades internas: formar um time de growth (com perfis de produto, dados, marketing e engenharia), implementar ferramentas de analytics e experimentação (Amplitude, Mixpanel, Google Analytics 4, Optimizely), criar processos de revisão de métricas e de reuniões de growth semanais. O objetivo é que a empresa internalize a metodologia de crescimento e continue executando ciclos de experimentação com autonomia após o término do projeto de consultoria."),
        ("Modelo de negócio e diferenciação de consultorias de crescimento",
         "Consultorias de crescimento trabalham melhor com empresas que já têm produto validado e alguma tração — mas estão presas em um platô ou querem acelerar a escala. Empresas que ainda estão buscando PMF (product-market fit) têm um desafio diferente. O modelo de negócio pode ser de projeto (diagnóstico + roadmap de crescimento em 4 a 8 semanas) ou de parceria (equipe embarcada por 3 a 12 meses, executando ciclos de experimentação com a equipe interna). Sucesso comprovado com resultados mensuráveis (crescimento de MRR, redução de churn, melhora de NRR) é o ativo de credibilidade mais valioso.")
    ],
    faq_list=[
        ("Qual a diferença entre growth hacking e consultoria de crescimento?",
         "Growth hacking é um conjunto de táticas e mentalidade — experimentação rápida, foco em métricas, criatividade para crescer com recursos limitados. Consultoria de crescimento aplica esse mindset de forma estruturada, com diagnóstico, priorização sistemática de iniciativas e construção de capabilities internas. Growth hacking sem estrutura gera muitos experimentos sem foco; consultoria de crescimento garante que os experimentos certos sejam executados no momento certo."),
        ("Quando uma startup está pronta para contratar consultoria de crescimento?",
         "Quando já tem produto validado com clientes pagantes (não apenas usuários gratuitos), tem dados suficientes para análise de funil e coortes e percebe que o crescimento está estagnado apesar de esforços em marketing e produto. Startups sem product-market fit confirmado precisam de consultoria de produto/estratégia antes de focar em crescimento — escalar sem PMF só acelera o churn."),
        ("Quais métricas são mais importantes para monitorar em um projeto de scale-up?",
         "MRR (Monthly Recurring Revenue) e sua taxa de crescimento MoM, NRR (Net Revenue Retention — acima de 110% indica expansão líquida), CAC payback (tempo para recuperar o custo de aquisição — abaixo de 12 meses é saudável), LTV/CAC (acima de 3x), churn mensal (abaixo de 2% para SaaS de qualidade) e cobertura do funil (volume de leads qualificados suficiente para alimentar o crescimento planejado) são as métricas essenciais do painel de crescimento.")
    ]
)

# ── Sitemap + trilha update ──────────────────────────────────────────────────
root = pathlib.Path(__file__).parent
slugs = [
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-qualidade-e-normas-iso",
     "Gestão de Negócios de Empresa de B2B SaaS de Gestão de Qualidade e Normas ISO"),
    ("gestao-de-clinicas-de-andrologia-e-saude-masculina",
     "Gestão de Clínicas de Andrologia e Saúde Masculina"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-centros-de-transplante-e-pos-transplante",
     "Vendas para o Setor de SaaS de Gestão de Centros de Transplante e Pós-Transplante"),
    ("consultoria-de-experiencia-do-cliente-e-jornada-cx",
     "Consultoria de Experiência do Cliente e Jornada CX"),
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-plataformas-de-compliance-e-grc",
     "Gestão de Negócios de Empresa de B2B SaaS de Plataformas de Compliance e GRC"),
    ("gestao-de-clinicas-de-imunologia-e-alergia-clinica",
     "Gestão de Clínicas de Imunologia e Alergia Clínica"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-hipnoterapia-e-terapias-integrativas",
     "Vendas para o Setor de SaaS de Gestão de Clínicas de Hipnoterapia e Terapias Integrativas"),
    ("consultoria-de-estrategia-de-crescimento-e-scale-up",
     "Consultoria de Estratégia de Crescimento e Scale-Up"),
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

print("Done — batch 1502")
