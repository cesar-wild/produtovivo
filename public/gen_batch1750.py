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
<script type="application/ld+json">{faq_schema}</script>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Segoe UI',sans-serif;color:#1a1a1a;background:#f9f9f9}}
header{{background:#0a7c4e;color:#fff;padding:2rem 1rem;text-align:center}}
header h1{{font-size:1.8rem;max-width:800px;margin:0 auto}}
main{{max-width:800px;margin:2rem auto;padding:0 1rem}}
h2{{color:#0a7c4e;margin:1.5rem 0 .5rem}}
p{{line-height:1.7;margin-bottom:1rem}}
.faq{{background:#fff;border-left:4px solid #0a7c4e;padding:1rem;margin:1rem 0;border-radius:4px}}
.faq strong{{display:block;margin-bottom:.4rem}}
footer{{text-align:center;padding:2rem;font-size:.85rem;color:#666}}
a{{color:#0a7c4e}}
</style>
</head>
<body>
<header><h1>{h1}</h1></header>
<main>
<p>{lead}</p>
{sections_html}
<h2>Perguntas Frequentes</h2>
{faq_html}
</main>
<footer><p>&copy; 2025 ProdutoVivo &mdash; <a href="https://produtovivo.com.br">produtovivo.com.br</a></p></footer>
</body>
</html>"""

def art(slug, title, desc, h1, lead, sections, faq_list):
    url = f"{DOMAIN}/blog/{slug}/"
    sec_html = ""
    for sh, sp in sections:
        sec_html += f"<h2>{sh}</h2><p>{sp}</p>\n"
    faq_html = ""
    for q, a in faq_list:
        faq_html += f'<div class="faq"><strong>{q}</strong><p>{a}</p></div>\n'
    faq_schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq_list]
    }, ensure_ascii=False)
    html = TMPL.format(title=title, desc=desc, url=url, pixel=PIXEL,
                       h1=h1, lead=lead, sections_html=sec_html,
                       faq_html=faq_html, faq_schema=faq_schema)
    out = pathlib.Path(BASE) / slug
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(html, encoding="utf-8")
    print(f"  {slug}")

# ── Article 4983 ── B2B SaaS: gestão de contratos jurídicos (CLM)
art(
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-contratos-juridicos",
    "Gestão de Negócios de Empresa de B2B SaaS de Gestão de Contratos Jurídicos | ProdutoVivo",
    "Como construir e escalar um B2B SaaS de gestão de contratos jurídicos (CLM). Estratégias de produto, go-to-market e diferenciação.",
    "Como Escalar um B2B SaaS de Gestão de Contratos Jurídicos (CLM)",
    "Contract Lifecycle Management (CLM) é um dos segmentos de SaaS B2B com maior crescimento em jurídico corporativo — empresas gerenciam dezenas a milhares de contratos ativos, e sem sistema dedicado, contratos vencem sem que ninguém perceba, cláusulas problemáticas escapam da revisão e a busca por um contrato específico consome horas. Com LGPD e crescimento do compliance, CLM se tornou prioridade para jurídicos corporativos.",
    [
        ("O problema de CLM que planilhas não resolvem",
         "Empresas sem CLM enfrentam: renovação automática indesejada de contratos com fornecedores (ninguém percebeu que o contrato venceria e já renovou automaticamente com reajuste alto), não localização de um contrato específico quando há litígio, falta de padronização de cláusulas (cada contrato foi criado do zero por diferentes advogados), impossibilidade de analisar o portfólio de contratos como um todo (qual o valor total comprometido com contratos ativos?), e demora de semanas para aprovar e assinar um contrato simples. CLM resolve todos esses problemas."),
        ("Funcionalidades core de uma plataforma CLM",
         "Repositório centralizado de contratos com busca full-text (encontrar qualquer contrato por qualquer termo em segundos), alertas automáticos de vencimento (30, 60, 90 dias antes), fluxo de aprovação configurável (quem aprova contratos de que valor e tipo), templates de contratos com variáveis preenchíveis (padronização de linguagem jurídica), assinatura eletrônica integrada (ou integração com DocuSign/Clicksign), versionamento de minutas (histórico de todas as alterações e quem fez o quê), e extração de metadados por IA (parte contratante, valor, vigência, índice de reajuste) são as funcionalidades essenciais."),
        ("IA em CLM: extração automática e análise de risco",
         "A aplicação mais transformadora de IA em CLM é a extração automática de metadados — o contrato é carregado em PDF e a IA identifica as partes, valor, data de início, data de vencimento, índice de reajuste e cláusulas críticas sem intervenção humana. Revisão automática de contratos por IA (identificar cláusulas problemáticas ou ausentes em relação ao padrão da empresa) reduz o tempo de revisão jurídica. Para SaaS brasileiro de CLM, NLP treinado em português jurídico com terminologia contratual brasileira é o diferencial técnico central."),
        ("Segmentação do mercado de CLM",
         "Empresas com 100+ contratos ativos e time jurídico interno são o sweet spot. Sectores mais adotantes: tecnologia (contratos de SaaS, parceria, NDA), serviços (contratos de prestação de serviços com clientes e fornecedores), varejo (contratos de fornecedores, franquias, locação de lojas), e empresas com alto volume de contratos com consumidores (seguradoras, operadoras de plano de saúde, financeiras). Jurídicos corporativos de empresas com 200 a 5.000 colaboradores têm a maior disposição a pagar e o maior ganho de produtividade com CLM."),
        ("Go-to-market para SaaS de CLM",
         "General counsels, diretores jurídicos e responsáveis por compliance são os compradores-alvo. LinkedIn com conteúdo sobre governança contratual, riscos de contratos mal gerenciados e LGPD em contratos tem boa tração. Parcerias com associações jurídicas (OAB, ABJUD — Associação Brasileira do Jurídico de Empresas, IBGC para governança) são canais de credibilidade. Eventos como ABCIP (contratos públicos) e congresso da ABJUD concentram os decisores."),
    ],
    [
        ("CLM e assinatura eletrônica são a mesma coisa?",
         "Não. Assinatura eletrônica é uma funcionalidade (a capacidade de assinar digitalmente um documento). CLM é uma plataforma completa de gestão do ciclo de vida do contrato — desde a criação do template até a renovação ou encerramento, passando por aprovação, negociação, assinatura e monitoramento. Uma plataforma CLM tipicamente inclui assinatura eletrônica integrada ou integra com plataformas especializadas (DocuSign, Clicksign, Contraktor). Assinatura eletrônica sem CLM resolve apenas a etapa de assinatura — não o repositório, os alertas de vencimento nem o fluxo de aprovação."),
        ("Contratos digitais têm a mesma validade jurídica que contratos em papel?",
         "Sim. A Lei 14.063/2020 e a MP 2.200-2/2001 estabelecem a validade jurídica de documentos eletrônicos no Brasil. Contratos assinados eletronicamente com assinatura qualificada (certificado ICP-Brasil) têm presunção de autenticidade e validade equivalente à assinatura física com reconhecimento de firma. Contratos assinados com assinatura eletrônica avançada (sem certificado ICP-Brasil) são válidos entre partes que acordam mutuamente o uso. Para contratos de alto valor ou complexidade, recomenda-se assinatura qualificada."),
        ("Quanto tempo leva implementar uma plataforma CLM?",
         "Implementação de CLM varia de 2 a 12 semanas dependendo da complexidade. Para PMEs sem processos formalizados, um SaaS de CLM moderno pode ser configurado em 1 a 2 semanas — importar contratos existentes, configurar templates básicos e ativar alertas de vencimento. Para empresas com processos de aprovação complexos, integrações com ERP/CRM e necessidade de extração retroativa de metadados de milhares de contratos históricos, o projeto pode levar 3 a 6 meses. O maior risco de implementação é a resistência do time jurídico à mudança de processo."),
    ]
)

# ── Article 4984 ── Clinics: radiologia e diagnóstico por imagem
art(
    "gestao-de-clinicas-de-radiologia-e-diagnostico-por-imagem",
    "Gestão de Clínicas de Radiologia e Diagnóstico por Imagem | ProdutoVivo",
    "Guia de gestão para clínicas de radiologia e diagnóstico por imagem: estrutura, equipamentos, laudos digitais e estratégias de crescimento.",
    "Gestão de Clínicas de Radiologia e Diagnóstico por Imagem: Guia Completo",
    "Radiologia e diagnóstico por imagem é uma das especialidades médicas de maior demanda — praticamente qualquer doença requer algum tipo de imagem diagnóstica em algum momento. Raios-X, ultrassonografia, tomografia computadorizada, ressonância magnética, densitometria óssea e mamografia formam o portfólio básico de uma clínica de imagem. Para gestores, é um negócio de capital intensivo (equipamentos caros), alta produtividade (volume alto de exames) e laudos como produto final.",
    [
        ("Estrutura de uma clínica de diagnóstico por imagem",
         "Uma clínica de imagem completa oferece: raios-X digital (tórax, ossos, abdômen), ultrassonografia (abdominal, pélvica, tireoide, musculoesquelética, eco Doppler), mamografia digital, densitometria óssea (DEXA), tomografia computadorizada (TC) e ressonância magnética (RM). O investimento em equipamentos é elevado: RM de 1.5T custa R$ 2 a R$ 5 milhões, TC multicorte R$ 1 a R$ 3 milhões. A escala de exames é o fator determinante da rentabilidade — equipamentos caros precisam de volume alto para atingir o ponto de equilíbrio.",
         ),
        ("PACS e RIS: a infraestrutura digital de uma clínica de imagem",
         "PACS (Picture Archiving and Communication System) é o sistema de armazenamento e distribuição de imagens médicas digitais — onde as imagens são guardadas, acessadas e visualizadas pelos radiologistas. RIS (Radiology Information System) é o sistema de gestão operacional — agendamento, worklist de exames, laudos, faturamento e relatórios. A integração PACS+RIS é a espinha dorsal tecnológica de qualquer clínica de imagem moderna. Laudos entregues digitalmente em poucas horas, com link de acesso para o médico solicitante e para o paciente, são o padrão de qualidade esperado.",
         ),
        ("Teleradiologia: eficiência e acesso a especialistas",
         "Teleradiologia — laudos realizados remotamente por radiologistas — é prática consolidada no Brasil, especialmente em hospitais e clínicas fora dos grandes centros. Para clínicas de imagem que não têm radiologista próprio, a parceria com empresa de teleradiologia garante laudos em horário estendido (24/7) e acesso a especialistas em subespecialidades (neurorradiologia, radiologia musculoesquelética, radiologia pediátrica). Para clínicas que têm radiologistas, a teleradiologia complementa em horários de pico e finais de semana.",
         ),
        ("Faturamento em radiologia e imagem",
         "Exames de imagem têm faturamento por código TUSS com valores que variam muito: raios-X simples cobre R$ 30 a R$ 80, ultrassonografia R$ 80 a R$ 200, TC R$ 200 a R$ 600, RM R$ 400 a R$ 1.200 dependendo da região e do convênio. Contraste injetável (TC e RM com contraste) é faturado separadamente como material. Exames realizados em urgência (após 18h, fins de semana) têm adicional de urgência. Clínicas que ampliam o horário de funcionamento e oferecem laudos em menos de 2 horas têm diferencial competitivo no mercado de imagem.",
         ),
        ("Marketing para clínicas de diagnóstico por imagem",
         "Médicos solicitantes são o canal primário — cardiologistas, ortopedistas, oncologistas, reumatologistas e neurologists encaminham centenas de exames por mês cada. Construir relação com especialistas locais via visitas periódicas, laudos de qualidade reconhecida e comunicação ágil (laudo disponível em 2h) é o marketing mais eficaz. Para pacientes diretos, busca no Google por exame específico na cidade tem alta intenção de compra. Plataformas de agendamento de exames online (Doctoralia, Saúde Simples) ampliam o alcance de pacientes que chegam sem encaminhamento.",
         ),
    ],
    [
        ("RM aberta é inferior à RM fechada?",
         "RM aberta (ímã aberto, 0.35T a 1.0T) tem menor campo magnético do que a RM fechada de alto campo (1.5T ou 3T) — isso resulta em imagens de menor resolução e tempo de exame mais longo. Para pacientes claustrofóbicos, obesos (limitação de peso da mesa) ou crianças, a RM aberta é uma alternativa válida. Para diagnósticos que exigem alta resolução (neuroimagem, imagem cardíaca, musculoesquelético de detalhes finos), a RM fechada de 1.5T ou 3T é superior. Convênios raramente têm distinção de valor na tabela entre RM aberta e fechada — mas a qualidade diagnóstica importa para o médico solicitante.",
         ),
        ("Exames de imagem precisam de laudo médico?",
         "Sim. Exames de imagem devem ser laudados por médico especialista em radiologia e diagnóstico por imagem (com residência em radiologia ou título de especialista pela CBR — Colégio Brasileiro de Radiologia). O laudo radiológico é o produto médico final do exame — é documento médico com responsabilidade técnica do radiologista. Técnicos em radiologia realizam o exame (posicionam o paciente, operam o equipamento) mas não emitem laudos. Clinicas que entregam apenas imagens sem laudo médico estão em desconformidade com as normas do CFM.",
         ),
        ("Quanto custa um equipamento de ressonância magnética no Brasil?",
         "RM de 1.5T (o padrão mais comum para clínicas) custa entre R$ 2 e R$ 4 milhões incluindo instalação e blindagem magnética da sala. RM de 3T (alta resolução, para centros de referência e pesquisa) custa R$ 5 a R$ 8 milhões. O custo de instalação inclui a blindagem RF da sala (cage de Faraday) e o gradiente de campo — tipicamente R$ 500.000 a R$ 1.000.000 adicionais à compra do equipamento. Manutenção anual (contrato de preventiva e corretiva com o fabricante) representa 5 a 10% do valor do equipamento.",
         ),
    ]
)

# ── Article 4985 ── SaaS Sales: concessionárias de automóveis
art(
    "vendas-para-o-setor-de-saas-de-concessionarias-de-automoveis",
    "Vendas para o Setor de SaaS de Concessionárias de Automóveis | ProdutoVivo",
    "Como vender SaaS para concessionárias de automóveis no Brasil. Estratégias de prospecção, demonstração e fechamento no setor automotivo.",
    "Como Vender SaaS para Concessionárias de Automóveis",
    "O setor de concessionárias de automóveis no Brasil tem mais de 5.000 concessionárias de veículos novos e dezenas de milhares de revendas de usados. CRM de vendas de veículos, DMS (Dealer Management System), gestão de estoque de veículos, F&I (Finance & Insurance) e pós-vendas são SaaS específicos do setor com alto valor por cliente e baixo churn quando integrados à operação.",
    [
        ("O stack de sistemas de uma concessionária",
         "Concessionárias modernas operam com: DMS (Dealer Management System) — o ERP da concessionária, gerencia vendas, estoque, serviços e peças; CRM de vendas para gestão de leads e funil de vendas de veículos; plataforma de usados (avaliação de seminovos, publicação em plataformas como OLX, WebMotors, iCarros, Mercado Livre Autos); sistema de F&I (financiamento e seguros — onde está boa parte da margem da concessionária); e sistema de pós-vendas (agendamento de revisões, recall, satisfação do cliente). Cada sistema é vendável independentemente ou como suíte integrada.",
         ),
        ("CRM de concessionária: diferenças do CRM genérico",
         "CRM de concessionária tem especificidades que CRMs genéricos não cobrem: lead de test-drive (com veículo e horário agendado), histórico de conversas por veículo de interesse (não por empresa), processo de trade-in (avaliação do carro do cliente como parte do pagamento), múltiplas fontes de lead simultaneamente (site da concessionária, portais de veículos, Instagram, indicação), e integração com DMS para sincronizar o estoque de veículos disponíveis. Vendedores de concessionária são usuários diários — o app mobile robusto é requisito.",
         ),
        ("Como fazer demo de SaaS para concessionárias",
         "Demo começa pelo fluxo de um lead: cliente pede test-drive no site → lead aparece no CRM → vendedor recebe notificação e agenda o test-drive → visita registrada com veículos de interesse → proposta gerada com tabela de preço + F&I → follow-up automático após 3 dias sem resposta → negócio fechado registrado no DMS. Mostre o painel de leads por fonte (Google, portais, WhatsApp) e o funil de conversão por vendedor. Gestores de concessionária são orientados a resultados — mostre os números antes e depois.",
         ),
        ("Objeções em concessionárias",
         "'Já temos o sistema da montadora' — a maioria das montadoras exige um DMS padrão para dealerships autorizados, mas CRM, pós-vendas e gestão de usados podem ser complementados com soluções independentes. 'Investimento alto' — calcule: se um vendedor fecha mais 2 negócios por mês com CRM vs. sem (ticket médio de R$ 80.000, margem de R$ 3.000), são R$ 6.000 a mais de margem por vendedor por mês. 'Integração com o DMS' — verifique se há API disponível e apresente a integração como um diferencial do seu produto.",
         ),
        ("Prospecção em concessionárias",
         "FENABRAVE (Federação Nacional das Concessionárias de Veículos) e o Salão do Automóvel são pontos de acesso ao setor. Associações estaduais de concessionárias (ASSOBENS em São Paulo, por exemplo) organizam eventos e têm listas de associados. LinkedIn para diretores e gerentes de concessionárias. Visita presencial à concessionária durante horário de baixo movimento (segunda-feira ou início de tarde em dias úteis) com demo no tablet — gerentes de concessionária tomam decisão rápida quando o produto resolve uma dor real.",
         ),
    ],
    [
        ("DMS é obrigatório para concessionárias autorizadas?",
         "A maioria das montadoras (Volkswagen, GM, Toyota, Fiat-Stellantis) exige que suas concessionárias autorizadas usem sistemas DMS homologados pela montadora — isso garante integração com os sistemas de pedidos de veículos, garantias e recall. A exigência do DMS da montadora cria um gatekeeping de mercado — mas também deixa espaço para soluções complementares (CRM, pós-vendas, usados) que os DMS das montadoras frequentemente não cobrem bem. Para revendas de usados multi-marcas sem vínculo com montadora, a escolha de DMS é totalmente livre.",
         ),
        ("F&I representa que parte da margem da concessionária?",
         "F&I (Finance & Insurance) — receita de comissões de financiamentos e seguros vendidos junto ao veículo — representa tipicamente 20 a 35% da margem total de uma concessionária saudável. Com a compressão de margens na venda do veículo novo (pressão de preços e transparência de tabela FIPE), o F&I se tornou crítico para a rentabilidade. A concessionária que maximiza a taxa de financiamento pelos bancos credenciados e a penetração de seguros por veículo vendido tem margem muito superior às que dependem só da margem do veículo.",
         ),
        ("Vendas de carros por aplicativo estão substituindo as concessionárias?",
         "Marketplaces digitais (iCarros, OLX Autos, Webmotors) e fintechs de usados (Kavak, Carmax) mudaram o processo de pesquisa — o cliente chega à concessionária já informado sobre preços e modelos. Mas a experiência de compra física ainda é relevante para a maioria dos compradores de veículos novos — test-drive, negociação, personalização e confiança no vendedor são fatores que o digital não substitui completamente. Para usados simples e commoditizados, a digitalização avança mais rápido. Concessionárias que combinam excelência digital (leads qualificados, agendamento online) com experiência física superior têm vantagem competitiva.",
         ),
    ]
)

# ── Article 4986 ── Consulting: privacidade de dados e LGPD
art(
    "consultoria-de-privacidade-de-dados-e-lgpd",
    "Consultoria de Privacidade de Dados e LGPD | ProdutoVivo",
    "Como estruturar e vender consultoria de privacidade de dados e LGPD. Guia para consultores e DPOs que atuam em compliance de proteção de dados.",
    "Consultoria de Privacidade de Dados e LGPD: Como Construir uma Prática de Alto Valor",
    "A LGPD (Lei Geral de Proteção de Dados — Lei 13.709/2018) criou um mercado novo e crescente de consultoria de privacidade de dados. A ANPD (Autoridade Nacional de Proteção de Dados) tem aplicado multas e aumentado a fiscalização, tornando o compliance com LGPD uma prioridade real para empresas que tratam dados pessoais em escala. Para consultores com background jurídico, de TI ou de privacidade, é um nicho de honorários premium.",
    [
        ("O escopo da consultoria de privacidade de dados",
         "Consultoria de LGPD abrange: diagnóstico de maturidade de privacidade (gap analysis em relação à LGPD), mapeamento de dados pessoais tratados (quais dados, de quem, para que, por quanto tempo, com quem compartilhados), elaboração do Registro de Atividades de Tratamento (RAT — obrigatório pela LGPD), implantação de base legal para cada atividade de tratamento (consentimento, legítimo interesse, execução de contrato, etc.), elaboração e implantação de políticas de privacidade, e treinamento de equipes sobre LGPD e boas práticas de privacidade.",
         ),
        ("DPO como serviço (DPOaaS): modelo de negócio crescente",
         "A LGPD exige que controladores e operadores de dados indiquem um Encarregado de Dados (DPO — Data Protection Officer) para atuar como canal com a ANPD e com titulares de dados. Para PMEs que não têm estrutura para contratar um DPO interno, o modelo DPOaaS (DPO como serviço) é ideal — o consultor atua como DPO externo da empresa por uma mensalidade mensal (R$ 1.500 a R$ 10.000/mês dependendo do porte e complexidade). Um consultor de privacidade com 10 a 30 clientes DPOaaS tem receita recorrente previsível e alto LTV.",
         ),
        ("Resposta a incidentes de segurança: a maior urgência",
         "Incidentes de segurança envolvendo dados pessoais — vazamentos, ataques de ransomware, acesso indevido — geram obrigações específicas da LGPD: notificação à ANPD em prazo determinado (quando houver risco ou dano relevante), notificação aos titulares afetados, e medidas corretivas documentadas. Consultores de privacidade que dominam a gestão de incidentes — estruturar o Plano de Resposta a Incidentes antes do incidente e gerenciar a resposta quando ele ocorre — têm o serviço mais urgente e de maior valor da prática. Honorários de resposta a incidente variam de R$ 20.000 a R$ 200.000.",
         ),
        ("Além da LGPD: GDPR, ISO 27701 e privacidade by design",
         "Para empresas com operações internacionais, o GDPR (regulamento europeu equivalente) tem exigências ainda mais rigorosas. ISO 27701 é a extensão da ISO 27001 para Sistemas de Gestão de Informações de Privacidade — certificação que demonstra maturidade de privacidade. Privacy by design (privacidade integrada no desenvolvimento de produtos e sistemas desde o início, não como afterthought) é o princípio mais avançado de privacidade. Consultores que dominam o framework internacional têm proposta de valor para empresas que exportam ou têm investidores internacionais.",
         ),
        ("Captação de clientes para consultoria de privacidade",
         "Diretores jurídicos, responsáveis de TI/segurança e CEOs de empresas que tratam dados em escala (saúde, financeiro, marketing, varejo) são os compradores-alvo. Acidentes de privacidade na mídia criam janelas de oportunidade — quando uma empresa concorrente sofre multa da ANPD ou vaza dados, os concorrentes buscam consultoria imediatamente. IAPP (International Association of Privacy Professionals), ANPPD (Associação Nacional dos Profissionais de Privacidade de Dados) e eventos de segurança e privacidade (LGPD Summit, Security Leaders) são comunidades de referência.",
         ),
    ],
    [
        ("Toda empresa precisa de DPO?",
         "A LGPD exige que controladores e operadores nomeiem um Encarregado de Dados (DPO). Contudo, a ANPD publicou regulamentação que isenta microempresas e empresas de pequeno porte (EPPs) com tratamento de dados de baixo risco — se não realizarem tratamento em larga escala, tratamento de dados sensíveis ou de vulneráveis, nem perfilagem de pessoas. Para a maioria das PMEs que coletam dados básicos de clientes sem tratamento em escala, a nomeação formal é recomendável mas a ANPD ainda não fiscaliza rigorosamente esse segmento.",
         ),
        ("Qual a multa máxima prevista pela LGPD?",
         "A LGPD prevê sanções da ANPD que podem chegar a 2% do faturamento da empresa no Brasil no último exercício, limitado a R$ 50 milhões por infração. A ANPD também pode aplicar publicização da infração (divulgação pública da penalidade — dano reputacional frequentemente maior do que a multa financeira), bloqueio ou eliminação dos dados relacionados à infração, e suspensão parcial do banco de dados. A ANPD tem aplicado multas crescentes em 2024 e 2025, com o setor de saúde e financeiro sendo os mais fiscalizados.",
         ),
        ("Consentimento é sempre necessário para tratar dados pessoais?",
         "Não. A LGPD prevê 10 bases legais para tratamento de dados pessoais — o consentimento é apenas uma delas. Outras bases incluem: execução de contrato (dados necessários para cumprir um contrato com o titular), cumprimento de obrigação legal, interesse legítimo do controlador (desde que não prevaleça sobre os direitos do titular), proteção do crédito, tutela da saúde, e exercício regular de direitos. Para muitos usos de dados de clientes em relação comercial, a base 'execução de contrato' ou 'interesse legítimo' é mais adequada do que consentimento — que pode ser revogado a qualquer momento.",
         ),
    ]
)

# ── Article 4987 ── B2B SaaS: plataforma de NPS e pesquisa de satisfação
art(
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-plataforma-de-nps-e-pesquisa-de-satisfacao",
    "Gestão de Negócios de Empresa de B2B SaaS de Plataforma de NPS e Pesquisa de Satisfação | ProdutoVivo",
    "Como construir e escalar um B2B SaaS de plataforma de NPS e pesquisa de satisfação de clientes. Estratégias de produto, diferenciação e go-to-market.",
    "Como Escalar um B2B SaaS de Plataforma de NPS e Pesquisa de Satisfação",
    "NPS (Net Promoter Score) e pesquisa de satisfação de clientes são mercados de SaaS que crescem junto com a cultura de customer experience — empresas que antes mandavam pesquisa por e-mail uma vez por ano agora querem feedback em tempo real em cada touchpoint. SurveyMonkey, Qualtrics e Medallia dominam o enterprise, mas há espaço para SaaS brasileiro focado em PMEs e especialização por vertical.",
    [
        ("NPS vs. CSAT vs. CES: o portfólio de métricas de CX",
         "NPS (Net Promoter Score) mede a probabilidade de recomendação em escala de 0 a 10 — é o indicador de lealdade e satisfação geral mais usado globalmente. CSAT (Customer Satisfaction Score) mede a satisfação com uma interação específica (suporte, entrega, consulta). CES (Customer Effort Score) mede o esforço que o cliente teve para resolver um problema. Uma plataforma de feedback completa suporta os três formatos com triggers automáticos — NPS após 90 dias de uso, CSAT após cada atendimento de suporte, CES após resolução de problema. Cada métrica tem seu momento e propósito."),
        ("Triggers automáticos: NPS no momento certo",
         "NPS enviado no momento errado gera ruído — cliente recém-onboardado que ainda não usou o produto diz 7 sem saber bem por quê. Os triggers que geram insights mais acionáveis são: NPS transacional 24h após entrega ou onboarding concluído, NPS relacional após 90 dias de uso (maturidade suficiente para opinião formada), NPS pós-suporte 2h após resolução de ticket, e NPS de cancelamento imediatamente após a solicitação de churn. Cada trigger capta uma dimensão diferente da experiência e permite ações específicas."),
        ("Close the loop: transformar NPS em ação",
         "A maior diferença entre plataformas de NPS maduras e formulários simples é o close the loop — o processo de seguimento com cada respondente, especialmente detratores (0 a 6). Plataforma que facilita: alertas automáticos para o time de CS quando um detrator responde, template de resposta personalizado por nota, registro do follow-up e resolução do problema no histórico do cliente, e análise de quais problemas são mais frequentes entre detratores. NPS sem close the loop é dado coletado e ignorado — close the loop transforma NPS em ferramenta de retenção."),
        ("Análise de texto em feedbacks abertos",
         "A pergunta aberta que acompanha o NPS ('qual o principal motivo da sua nota?') gera os insights mais ricos — mas analisar centenas de respostas abertas manualmente é impraticável. NLP (Natural Language Processing) para análise de sentimento e categorização automática de temas (produto, suporte, preço, entrega) transforma texto livre em insights quantificáveis. 'Nos últimos 30 dias, 38% dos detratores mencionaram problema com suporte técnico' é um insight acionável que NPS sem análise de texto não entrega."),
        ("Go-to-market para SaaS de NPS e satisfação",
         "Customer success managers, heads de CX e diretores de marketing são os compradores-alvo. O produto pode ser vendido em PLG — freemium com até X respostas/mês gratuitas, conversão natural quando a empresa quer mais volume ou análises avançadas. Integração nativa com os sistemas mais usados (HubSpot, RD Station, Zendesk, Salesforce) é o diferencial de go-to-market — o NPS aparece no contexto onde o CS já trabalha, sem mudar de ferramenta. Eventos de CX (XP Summit, Customer Experience Brasil) concentram os compradores."),
    ],
    [
        ("Qual NPS é considerado bom?",
         "NPS varia de -100 a +100. Benchmarks gerais: acima de 70 é excelente (empresas como Apple, Netflix, Tesla nesse patamar em seus melhores momentos), 50 a 70 é muito bom, 30 a 50 é bom, 0 a 30 é ok mas há espaço para melhora, abaixo de 0 é crítico. O mais importante é comparar o NPS com o benchmark do seu setor — um NPS de 40 pode ser excelente em telecomunicações (onde a média é baixa) e insatisfatório em SaaS de alta performance (onde a média é 50+). Tendência ao longo do tempo importa mais do que a nota absoluta."),
        ("Quantas perguntas deve ter uma pesquisa de NPS?",
         "A pesquisa de NPS clássica tem apenas 2 perguntas: a nota de 0 a 10 (pergunta fechada) e a pergunta aberta de justificativa. Surveys mais longas têm taxas de resposta dramaticamente menores — cada pergunta adicional reduz a taxa de resposta em 10 a 15%. Para pesquisas relacionais mais aprofundadas, até 5 a 7 perguntas com NPS + dimensões adicionais (produto, suporte, valor) são aceitáveis. O princípio central: respeite o tempo do respondente, priorize qualidade de resposta sobre quantidade de dados coletados."),
        ("NPS prevê churn?",
         "NPS é correlacionado com churn mas não é um preditor perfeito. Detratores têm probabilidade maior de cancelar, mas nem todo detrator cancela — e nem todo churn é precedido por NPS baixo (alguns clientes cancelam silenciosamente sem expressar insatisfação). Para previsão de churn mais precisa, combine NPS com dados comportamentais de produto (uso, logins, features adotadas) e dados de relacionamento (tickets de suporte, NPS histórico). Modelos de machine learning que combinam NPS + comportamento têm precisão de predição de churn significativamente superior ao NPS isolado."),
    ]
)

# ── Article 4988 ── Clinics: medicina do viajante e vacinação
art(
    "gestao-de-clinicas-de-medicina-do-viajante-e-vacinacao",
    "Gestão de Clínicas de Medicina do Viajante e Vacinação | ProdutoVivo",
    "Guia de gestão para clínicas de medicina do viajante e centros de vacinação: estrutura, portfólio de vacinas, faturamento e crescimento.",
    "Gestão de Clínicas de Medicina do Viajante e Vacinação: Guia Completo",
    "Medicina do viajante e vacinação privada são especialidades de serviços de saúde preventiva com demanda crescente — viagens internacionais, vacinas não disponíveis no SUS, imunização corporativa e prevenção de doenças viagem-relacionadas formam um mercado de alto valor percebido pelo paciente. Clínicas especializadas em vacinas e saúde do viajante combinam consultoria personalizada, portfólio amplo de imunobiológicos e conveniência de acesso.",
    [
        ("Portfólio de vacinas e serviços de uma clínica de viajante",
         "Uma clínica de medicina do viajante completa oferece: consulta de medicina do viajante (avaliação de riscos específicos do destino, história de vacinação prévia, prescrição de quimioprofilaxia para malária quando indicado), vacinas do calendário nacional não disponíveis em farmácias (Febre Amarela, Meningocócica ACWY e B, Hepatite A e B, Febre Tifoide, Raiva pré-exposição, Encefalite Japonesa, Encefalite por Carrapato), e vacinas do calendário de adultos (Influenza, Pneumocócica, Herpes Zoster, HPV, dTpa). O portfólio amplo é o diferencial competitivo central.",
         ),
        ("Vacinação corporativa: o mercado B2B de imunização",
         "Empresas investem em vacinação corporativa para reduzir absenteísmo (funcionários vacinados contra influenza faltam menos no inverno), cumprir requisitos de viagens internacionais de colaboradores e demonstrar cuidado com saúde ocupacional. Campanhas de vacinação in-company (clínica leva estrutura de vacinação à empresa) são serviços de alto volume e logística padronizável. Convênios com empresas para vacinação de colaboradores e dependentes a preço corporativo são receita recorrente anual — a campanha de influenza se repete todo outono.",
         ),
        ("Faturamento em medicina do viajante e vacinação",
         "Vacinas privadas têm ticket médio por dose de R$ 80 a R$ 500 dependendo do imunobiológico — algumas vacinas importadas (Raiva humana, Encefalite por Carrapato) chegam a R$ 400 a R$ 600 por dose. Consulta de medicina do viajante fatura R$ 250 a R$ 600 particular. Campanha corporativa de influenza fatura por dose aplicada (R$ 60 a R$ 100) com volume de centenas a milhares de doses por empresa. Clínicas que têm câmara fria homologada pela ANVISA e estoque de imunobiológicos de difícil acesso têm vantagem competitiva sobre clínicas que trabalham sob pedido.",
         ),
        ("Regulação e licenciamento de centros de vacinação",
         "Clínicas de vacinação precisam de licença sanitária da vigilância epidemiológica municipal/estadual para armazenamento e aplicação de vacinas. Câmara fria com monitoramento contínuo de temperatura (2ºC a 8ºC) e alarme de desvio é requisito obrigatório. Registro de aplicação no RNDS (Rede Nacional de Dados em Saúde) ou sistema estadual de imunização é obrigatório para todas as vacinas aplicadas. Vacinas importadas para uso privado precisam de registro ou autorização especial da ANVISA (como as do programa autorizado da ANVISA para vacinas de viajante).",
         ),
        ("Marketing para clínicas de medicina do viajante",
         "Agências de viagens, empresas que enviam colaboradores para viagens internacionais, e associações de médicos que fazem missões humanitárias são canais B2B relevantes. Para pacientes, Google com busca por vacina específica ou destino ('vacina febre amarela SP', 'quimioprofilaxia malária') tem alta intenção de busca imediata antes de uma viagem. Conteúdo educativo sobre saúde em cada destino internacional (o que vacinar para Índia, África Subsaariana, Amazônia) tem boa tração orgânica e diferencia a clínica como autoridade no tema.",
         ),
    ],
    [
        ("Vacina de Febre Amarela pode ser tomada gratuitamente no SUS?",
         "Sim. A vacina de Febre Amarela está disponível gratuitamente no Calendário Nacional de Vacinação do SUS para residentes e viajantes para áreas de risco (boa parte do Brasil — praticamente todos os estados, exceto alguns municípios costeiros). Para viajantes que vão para países com exigência de certificado de Febre Amarela, a vacina do SUS gera certificado válido pela OMS (Certificado Internacional de Vacinação e Profilaxia — CIVP). Clínicas privadas oferecem a vacina por conveniência e agendamento mais rápido, mas não é obrigatória pagar por ela.",
         ),
        ("Quantas doses de vacina contra raiva são necessárias?",
         "Vacinação pré-exposição contra raiva (para viajantes a áreas de risco, veterinários, biólogos) consiste em 3 doses nos dias 0, 7 e 21 (ou 28). Após a série completa, é necessário verificar a soroconversão (titulação de anticorpos). A dose de reforço é recomendada a cada 2 a 5 anos para pessoas com exposição continuada. Em caso de exposição (mordida ou arranhão de animal suspeito), mesmo vacinados previamente, são necessárias 2 doses adicionais nos dias 0 e 3 — sem necessidade de imunoglobulina anti-rábica se vacinação prévia confirmada.",
         ),
        ("Clínica de viajante pode emitir certificado de vacinação internacional?",
         "Sim. O Certificado Internacional de Vacinação e Profilaxia (CIVP) pode ser emitido por serviços de saúde habilitados — inclui clínicas privadas credenciadas pela ANVISA e postos de vacinação do SUS. O CIVP é exigido para entrada em alguns países (Febre Amarela é a mais exigida). O certificado deve ser emitido no momento da vacinação, assinado por médico e com o selo da ANVISA. Clínicas privadas que emitem CIVP têm diferencial para viajantes internacionais que precisam do documento comprovando a vacinação.",
         ),
    ]
)

# ── Article 4989 ── SaaS Sales: sindicatos e entidades de classe
art(
    "vendas-para-o-setor-de-saas-de-sindicatos-e-entidades-de-classe",
    "Vendas para o Setor de SaaS de Sindicatos e Entidades de Classe | ProdutoVivo",
    "Como vender SaaS para sindicatos, federações, confederações e entidades de classe no Brasil. Estratégias adaptadas ao contexto associativo.",
    "Como Vender SaaS para Sindicatos e Entidades de Classe",
    "O sistema sindical e de representação de classe no Brasil tem mais de 11.000 sindicatos registrados, dezenas de federações e confederações, e centenas de conselhos de fiscalização profissional (CRM, CRA, CRO, CREA etc.). Gestão de filiados, cobrança de contribuição sindical, gestão de benefícios, comunicação com associados e gestão de acordos coletivos são dores operacionais que SaaS pode resolver. É um mercado subestimado com compradores acessíveis.",
    [
        ("O perfil do comprador em sindicatos e entidades",
         "Diretor-administrativo, tesoureiro e presidente de sindicato são os decisores em entidades menores. Em federações e confederações maiores, há equipe de TI e processos de compra mais formais. Diferente do setor privado, sindicatos têm restrições orçamentárias (dependem de contribuição sindical que oscilou após reforma trabalhista de 2017) e processos de aprovação colegiada (diretoria precisa aprovar despesas maiores). O pitch precisa enfatizar eficiência administrativa, não crescimento de receita — o objetivo é fazer mais com o orçamento existente.",
         ),
        ("As maiores dores de gestão em sindicatos",
         "Cadastro e gestão de filiados (quem está em dia, quem está inadimplente, histórico de filiação), cobrança de contribuição sindical e associativa (boletos, Pix, controle de inadimplência), comunicação com base (e-mail, SMS, WhatsApp para convocar assembleias e informar acordos coletivos), gestão de benefícios oferecidos aos filiados (plano de saúde negociado, descontos em farmácias, cursos de qualificação), e gestão de acordos coletivos de trabalho (datas de vigência, cláusulas específicas, histórico de negociações) são os problemas mais frequentes.",
         ),
        ("Como demonstrar SaaS para sindicatos",
         "Demo deve mostrar: cadastro de filiado com status de contribuição (adimplente/inadimplente), geração automática de boleto de anuidade, disparo de comunicado para todos os filiados de uma categoria por WhatsApp e e-mail, e painel de gestão de benefícios (filiado consulta se tem direito a desconto em farmácia). Mostre quanto tempo a secretaria economiza por mês sem digitar cartas de convocação ou controlar manualmente os pagamentos. Para diretores, mostre o relatório de adimplência da contribuição — frequentemente o maior problema de caixa do sindicato.",
         ),
        ("Conselhos de fiscalização profissional: mercado específico",
         "Conselhos regionais (CRM para médicos, CRA para administradores, CRO para dentistas, CREA para engenheiros) têm demanda específica: gestão de registro profissional (anuidades, certidões, atualização cadastral), fiscalização do exercício profissional, processo administrativo disciplinar, e portal do profissional para serviços digitais. São entidades de grande porte com receita estável (anuidade obrigatória de todos os profissionais registrados) e disposição a investir em tecnologia. Projetos de transformação digital em conselhos têm ticket de R$ 500.000 a R$ 3.000.000.",
         ),
        ("Prospecção em sindicatos e entidades",
         "CNC (Confederação Nacional do Comércio), CNI (Confederação Nacional da Indústria), CNT (Confederação Nacional do Transporte) e suas federações estaduais são os pontos de acesso ao sistema sindical patronal. Para sindicatos de trabalhadores, CUT, Força Sindical e UGT são as centrais. Conselhos profissionais têm encontros regionais frequentes. LinkedIn para diretores administrativos e tesoureiros. Participação em congressos de gestão sindical (quando existem regionalmente) ou em assembleias públicas de federações é canal de networking de baixo custo.",
         ),
    ],
    [
        ("A reforma trabalhista de 2017 afetou a receita dos sindicatos?",
         "Sim, significativamente. A Lei 13.467/2017 tornou facultativo o desconto da contribuição sindical (antes era obrigatório — 1 dia de salário de todos os trabalhadores uma vez por ano). Na prática, a receita de contribuição sindical de muitos sindicatos caiu 70 a 90%. Sindicatos que souberam migrar para o modelo de mensalidade voluntária dos filiados (com entrega de valor real em benefícios e representação) sobreviveram. Os que dependiam apenas da contribuição obrigatória enfrentaram crise grave. Essa crise torna a eficiência administrativa mais crítica do que nunca.",
         ),
        ("Sindicato pode investir em tecnologia com o orçamento disponível?",
         "Sim. Investimento em tecnologia de gestão administrativa é legítimo no orçamento sindical — reduz custos operacionais (menos pessoal para tarefas manuais) e melhora a entrega de serviços aos filiados (agilidade de atendimento, acesso digital a benefícios). A aprovação de despesas de tecnologia geralmente passa pela diretoria e, para valores maiores, pela assembleia geral. SaaS com mensalidade (despesa recorrente menor) é mais fácil de aprovar do que software com licença perpétua cara (investimento de capital único de maior valor).",
         ),
        ("Qual a diferença entre sindicato, federação e confederação?",
         "A estrutura sindical brasileira é piramidal. Sindicatos representam trabalhadores ou empregadores de uma categoria específica em um município ou região. Federações agrupam sindicatos de uma mesma categoria em um estado ou nível regional. Confederações agrupam federações no nível nacional por segmento amplo (comércio, indústria, transportes, agricultores). Acima de tudo estão as Centrais Sindicais (CUT, Força Sindical etc.) que representam trabalhadores de todas as categorias. Para vendedores de SaaS, sindicatos são os clientes individuais — federações e confederações são os canais de acesso a múltiplos sindicatos de uma vez.",
         ),
    ]
)

# ── Article 4990 ── Consulting: agronegócio e agricultura
art(
    "consultoria-de-agronegocio-e-agricultura",
    "Consultoria de Agronegócio e Agricultura | ProdutoVivo",
    "Como estruturar e vender consultoria especializada em agronegócio e agricultura. Guia para consultores que atuam em gestão rural, tecnologia agrícola e cadeia de valor.",
    "Consultoria de Agronegócio e Agricultura: Como Construir uma Prática Especializada",
    "O agronegócio brasileiro é um dos maiores do mundo — representa mais de 25% do PIB e é o maior exportador global de soja, carne bovina, frango, cana-de-açúcar e celulose. Produtores rurais de todos os tamanhos, cooperativas, agroindústrias e tradings enfrentam desafios de gestão, tecnologia e sustentabilidade que abrem espaço para consultoria especializada de alto valor.",
    [
        ("O escopo da consultoria de agronegócio",
         "Consultoria de agronegócio abrange: gestão de propriedades rurais (custos de produção, análise de resultado por talhão, planejamento de safra), tecnologia agrícola (agricultura de precisão, drones, sensoriamento remoto, automação de irrigação), gestão de cooperativas (governança, diversificação de receitas, verticalização da produção), cadeia de valor e comercialização (estratégias de hedge, contratos futuros na B3, acesso a mercado externo), e ESG no agronegócio (rastreabilidade, desmatamento zero, pegada de carbono, agricultura regenerativa).",
         ),
        ("Agricultura de precisão: a tecnologia que transforma a produção",
         "Agricultura de precisão usa tecnologia (GPS, sensores, drones, imagens de satélite, análise de solo) para mapear a variabilidade espacial do campo e aplicar insumos (fertilizantes, defensivos, sementes) na dose certa, no local certo, no momento certo — em vez de aplicar a dose uniforme em todo o talhão. Ganhos típicos: redução de 10 a 20% no custo de insumos (pela aplicação variável de taxa), aumento de 5 a 15% na produtividade por melhor gestão de fertilidade, e redução do impacto ambiental. Consultores que dominam a interpretação de mapas de variabilidade e implementação de aplicação a taxa variável têm demanda crescente.",
         ),
        ("Gestão de custos na fazenda: o projeto mais demandado",
         "Produtores rurais frequentemente não sabem qual o custo de produção por saca de soja ou por arroba de boi — o custo é misturado com despesas pessoais e não há separação entre resultado de diferentes atividades (soja, milho, pecuária). Consultores que implantam gestão de custos rigorosa — custo por talhão, custo por hectare por cultura, ponto de equilíbrio em preço de commodity — entregam resultado imediato: o produtor descobre que uma atividade é déficitária e pode racionalize seu portfólio. Honorários: R$ 2.000 a R$ 10.000/mês de retainer para propriedades médias e grandes.",
         ),
        ("ESG no agronegócio: oportunidade crescente",
         "Rastreabilidade de origem (provar que a soja foi produzida sem desmatamento), certificações de sustentabilidade (Rainforest Alliance, RTRS para soja, Bonsucro para cana), créditos de carbono de agricultura regenerativa e relatórios de ESG para tradings e exportadoras são demandas crescentes impulsionadas por exigências de mercados externos (especialmente Europa com o regulamento anti-desmatamento da UE — EUDR). Consultores que dominam os frameworks de rastreabilidade e certificação têm demanda crescente de produtores e cooperativas que exportam.",
         ),
        ("Captação de clientes em consultoria de agronegócio",
         "Cooperativas (COAMO, Copercampos, Copersucar), grandes produtores e SFPs (Special Purpose Farms) de fundos de investimento, agroindústrias e tradings são os clientes de maior ticket. Para produtores médios, associações rurais, sindicatos rurais (SRBs) e escritórios regionais do SENAR (Serviço Nacional de Aprendizagem Rural) são canais de acesso. Presença em feiras agropecuárias (Agrishow, ExpoLondrina, AgroBrasília) e publicação de análises de custos de produção por cultura e região são os melhores canais de captação no agronegócio.",
         ),
    ],
    [
        ("Consultoria de agronegócio exige formação em agronomia?",
         "Não necessariamente, mas a formação técnica agronômica é uma vantagem de credibilidade significativa junto a produtores rurais. Engenheiros agrônomos têm acesso mais fácil a produtores e podem prescrever insumos e práticas agronômicas diretamente. Administradores, economistas e contabilistas com especialização em agronegócio atuam bem em gestão de custos, financiamento rural e mercado de commodities. O consultor de agronegócio mais completo combina conhecimento técnico agronômico com gestão empresarial — as duas faces de uma operação rural eficiente.",
         ),
        ("O que é hedge de commodity agrícola?",
         "Hedge é a proteção do preço de uma commodity contra variações adversas de mercado. Um produtor de soja que vende parte da produção futura em contratos na B3 (Bolsa de Valores) a R$ 150 a saca no plantio garante essa receita independente de o preço cair para R$ 120 na colheita. O hedge elimina o risco de preço mas também elimina o potencial de ganho se o preço subir para R$ 180. Consultores que dominam estratégias de hedge (contratos futuros, opções, NDF) têm demanda de produtores médios e grandes que querem previsibilidade de receita.",
         ),
        ("Crédito de carbono em fazendas: como funciona?",
         "Fazendas que sequestram mais carbono do que emitem (pela recuperação de pastagens degradadas, reflorestamento, agricultura de baixo carbono — ABC Agricultura de Baixo Carbono) podem vender créditos de carbono para empresas que precisam compensar suas emissões. O mercado voluntário de carbono (VCM) precifica cada tonelada de CO2 equivalente sequestrado em US$ 5 a US$ 50 dependendo do tipo de projeto e certificação (Verra VCS, Gold Standard). Consultores que estruturam projetos de crédito de carbono para fazendas — certificação, MRV (Monitoramento, Reporte e Verificação), registro e comercialização — têm demanda crescente.",
         ),
    ]
)

# ── Sitemap + trilha update ──
import re

sitemap_path = pathlib.Path(__file__).parent / "sitemap.xml"
trilha_path  = pathlib.Path(__file__).parent / "trilha.html"

slugs = [
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-contratos-juridicos",
    "gestao-de-clinicas-de-radiologia-e-diagnostico-por-imagem",
    "vendas-para-o-setor-de-saas-de-concessionarias-de-automoveis",
    "consultoria-de-privacidade-de-dados-e-lgpd",
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-plataforma-de-nps-e-pesquisa-de-satisfacao",
    "gestao-de-clinicas-de-medicina-do-viajante-e-vacinacao",
    "vendas-para-o-setor-de-saas-de-sindicatos-e-entidades-de-classe",
    "consultoria-de-agronegocio-e-agricultura",
]

sm = sitemap_path.read_text(encoding="utf-8")
new_urls = ""
for s in slugs:
    new_urls += f"  <url><loc>{DOMAIN}/blog/{s}/</loc></url>\n"
sitemap_path.write_text(sm.replace("</urlset>", new_urls + "</urlset>"), encoding="utf-8")

tr = trilha_path.read_text(encoding="utf-8")
new_items = ""
for s in slugs:
    label = s.replace("-", " ").title()
    new_items += f'  <li><a href="/blog/{s}/">{label}</a></li>\n'
trilha_path.write_text(tr.replace("</ul>", new_items + "\n</ul>", 1), encoding="utf-8")

print("Done — batch 1750")
