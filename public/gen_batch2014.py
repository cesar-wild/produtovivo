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
<script type="application/ld+json">{schema}</script>
<!-- Facebook Pixel -->
<script>
!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','{pixel}');fbq('track','PageView');
</script>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Segoe UI',sans-serif;background:#f9f9f9;color:#222;line-height:1.7}}
header{{background:#0a7c4e;padding:18px 24px}}
header a{{color:#fff;text-decoration:none;font-weight:700;font-size:1.3rem}}
.container{{max-width:860px;margin:0 auto;padding:32px 20px}}
h1{{font-size:2rem;color:#0a7c4e;margin-bottom:16px}}
.lead{{font-size:1.1rem;margin-bottom:28px;color:#444}}
h2{{font-size:1.4rem;color:#0a7c4e;margin:28px 0 10px}}
p{{margin-bottom:16px}}
.faq{{background:#fff;border-left:4px solid #0a7c4e;padding:16px 20px;margin:14px 0;border-radius:4px}}
.faq strong{{display:block;margin-bottom:6px}}
.cta{{background:#0a7c4e;color:#fff;padding:28px;text-align:center;border-radius:8px;margin-top:40px}}
.cta a{{color:#fff;font-weight:700;text-decoration:underline}}
footer{{text-align:center;padding:24px;font-size:.85rem;color:#777}}
</style>
</head>
<body>
<header><a href="https://produtovivo.com.br">ProdutoVivo</a></header>
<div class="container">
<h1>{h1}</h1>
<p class="lead">{lead}</p>
{sections}
<h2>Perguntas Frequentes</h2>
{faqs}
<div class="cta">
<p>Quer aprender a vender infoprodutos digitais e construir renda recorrente?</p>
<p><a href="https://produtovivo.com.br">Conheça o ProdutoVivo — o guia completo para infoprodutores brasileiros.</a></p>
</div>
</div>
<footer>&copy; 2025 ProdutoVivo. Todos os direitos reservados.</footer>
</body>
</html>"""


def art(slug, title, desc, h1, lead, sections, faq_list):
    url    = f"{DOMAIN}/blog/{slug}/"
    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faq_list
        ]
    }, ensure_ascii=False)
    sec_html = ""
    for heading, body in sections:
        sec_html += f"<h2>{heading}</h2>\n<p>{body}</p>\n"
    faq_html = ""
    for q, a in faq_list:
        faq_html += f'<div class="faq"><strong>{q}</strong>{a}</div>\n'
    html = TMPL.format(title=title, desc=desc, url=url, pixel=PIXEL,
                       schema=schema, h1=h1, lead=lead,
                       sections=sec_html, faqs=faq_html)
    out = pathlib.Path(BASE) / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"  {slug}")


# ── Article 5511 — B2B SaaS: CMS e Gestão de Conteúdo Headless ──
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-cms-e-gestao-de-conteudo-headless",
    title="Gestão de Negócios para Empresas de B2B SaaS de CMS e Gestão de Conteúdo Headless | ProdutoVivo",
    desc="Estratégias de gestão para empresas B2B SaaS de CMS headless e gestão de conteúdo: crescimento, diferenciação e mercado. Guia para infoprodutores.",
    h1="Gestão de Negócios para Empresas de B2B SaaS de CMS e Gestão de Conteúdo Headless",
    lead="Content Management Systems (CMS) headless são a infraestrutura de conteúdo digital de empresas que precisam publicar em múltiplos canais simultâneos. Para infoprodutores que atendem mercados de tecnologia editorial e digital, entender como essas empresas operam e crescem é oportunidade de conteúdo altamente técnico e estratégico.",
    sections=[
        ("O Mercado de CMS Headless e Gestão de Conteúdo Digital",
         "CMS headless separa o backend de gerenciamento de conteúdo (onde você cria e organiza conteúdo) do frontend de apresentação (como o conteúdo é exibido). Em vez de renderizar HTML diretamente, um headless CMS entrega conteúdo via API para qualquer canal — site, aplicativo mobile, SmartTV, IoT, chatbot. Esse modelo substituiu os CMS monolíticos tradicionais (WordPress, Drupal) em empresas que precisam de omnichannel real. O mercado de headless CMS cresce acima de 20% ao ano, impulsionado pela proliferação de canais digitais e pela adoção de arquiteturas Jamstack e composable commerce."),
        ("Proposta de Valor e Posicionamento no Mercado",
         "A proposta de valor central do headless CMS é: velocidade de entrega de conteúdo (sites estáticos pré-renderizados carregam em milissegundos), flexibilidade total de frontend (os desenvolvedores usam React, Vue, Angular ou qualquer framework sem restrições), escalabilidade para picos de tráfego (API entrega conteúdo sob demanda sem sobrecarregar servidor de CMS), e publicação omnichannel nativa. Diferenciadores entre players incluem: experiência de edição para não-técnicos (redatores e marketeiros precisam de interface intuitiva), riqueza de tipos de conteúdo e referências cruzadas, e ecossistema de integrações com DAM, PIM e plataformas de commerce."),
        ("Go-to-Market: Desenvolvedores, Marketing Ops e CTOs",
         "O CMS headless tem duplo buyer: desenvolvedores que implementam a solução (querem API bem documentada, SDKs em múltiplas linguagens, trial rápido) e marketing/editorial que cria o conteúdo (querem interface intuitiva, workflows de aprovação e preview em tempo real). O CTO ou VP de Engenharia aprova o contrato enterprise. Estratégia developer-first — documentação excelente, tutoriais no YouTube, presença em GitHub, comunidade no Discord — é o caminho mais eficiente para construir base de adoção que depois converte em contratos corporativos."),
        ("Pricing, Escalabilidade e Modelos de Receita",
         "CMS headless é tipicamente precificado por volume de registros de conteúdo, por número de chamadas de API por mês, por usuário de editor ou por combinação desses fatores. Plano free para projetos pessoais e startups (limitado em registros ou chamadas de API) é o padrão do mercado — onboarding sem custo que converte em planos pagos conforme o projeto cresce. Enterprise pricing é baseado em chamadas de API ilimitadas, ambientes adicionais (staging, produção), SLA garantido e suporte dedicado. NRR acima de 130% é comum porque crescimento de tráfego e conteúdo do cliente naturalmente empurra para planos maiores."),
        ("Tendências: Composable DXP e IA de Conteúdo",
         "A evolução do headless CMS é a DXP (Digital Experience Platform) composable: orquestração de múltiplas soluções best-of-breed (CMS + CDN + personalização + search + commerce) via APIs, em vez de uma suite monolítica. AI de conteúdo — geração automática de variações de texto, tradução automática, otimização de SEO e personalização de conteúdo por segmento de audiência — está sendo integrada nos principais CMS headless como feature nativa. Infoprodutores que educam equipes de marketing e desenvolvimento sobre arquitetura headless e IA editorial têm audiência crescente em um dos segmentos de maior transformação digital."),
    ],
    faq_list=[
        ("CMS headless é melhor que WordPress para todos os casos?",
         "Não para todos. WordPress continua excelente para sites simples, blogs e projetos onde um único canal (site web) é suficiente e a equipe não tem desenvolvedores para implementar frontend personalizado. CMS headless brilha quando há múltiplos canais (site + app + outros), quando performance extrema é crítica, ou quando o conteúdo precisa alimentar sistemas além do site (e-commerce, chatbots, displays digitais)."),
        ("O que é Jamstack e como se relaciona com headless CMS?",
         "Jamstack (JavaScript + APIs + Markup) é uma arquitetura de desenvolvimento web que pré-gera páginas estáticas no build time usando dados de APIs (incluindo headless CMS) e as serve via CDN. O resultado são sites ultra-rápidos e seguros. Headless CMS é o fornecedor de conteúdo ideal para sites Jamstack: o conteúdo fica na API do CMS, e frameworks como Next.js, Gatsby e Nuxt buscam e renderizam no build."),
        ("Como migrar de WordPress para headless CMS?",
         "A migração envolve: exportar conteúdo do WordPress (posts, páginas, mídias), modelar os tipos de conteúdo no headless CMS de destino, importar o conteúdo via API ou ferramentas de migração, reimplementar o frontend no framework escolhido (Next.js é o mais popular para esse uso), e configurar redirecionamentos para preservar SEO. O processo é complexo e tipicamente leva 2-6 meses dependendo do volume de conteúdo e da complexidade do frontend."),
    ]
)

# ── Article 5512 — Clinic: Pneumologia Pediátrica e Asma Infantil ──
art(
    slug="gestao-de-clinicas-de-pneumologia-pediatrica-e-asma-infantil",
    title="Gestão de Clínicas de Pneumologia Pediátrica e Asma Infantil | ProdutoVivo",
    desc="Guia de gestão para clínicas de pneumologia pediátrica e asma infantil: modelo assistencial, educação de pacientes, tecnologia e crescimento. Para infoprodutores da saúde.",
    h1="Gestão de Clínicas de Pneumologia Pediátrica e Asma Infantil",
    lead="A pneumologia pediátrica e o manejo especializado da asma infantil formam uma subespecialidade de altíssima demanda no Brasil, país com uma das maiores prevalências de asma do mundo. Para infoprodutores da saúde, entender a gestão dessas clínicas significa explorar um nicho com pacientes crônicos, família engajada e forte componente educacional.",
    sections=[
        ("A Pneumologia Pediátrica no Contexto Brasileiro",
         "O Brasil tem prevalência de asma entre as mais altas do mundo — afetando entre 10-20% das crianças em diferentes regiões, com São Paulo liderando as estatísticas. Além da asma, a pneumologia pediátrica abrange bronquiolite viral aguda (principal causa de hospitalização em lactentes), pneumonias de repetição, bronquiectasias, fibrose cística, doenças pulmonares intersticiais em crianças, síndrome do respirador bucal e avaliação de roncos e apneia obstrutiva do sono pediátrica. A diversidade de condições e a alta prevalência de asma criam demanda contínua por serviços especializados que vão além da consulta de pediatria geral."),
        ("Gestão Multidisciplinar da Asma na Criança",
         "O manejo ideal da asma pediátrica é multidisciplinar: pneumologista pediátrico para diagnóstico e prescrição, enfermeiro educador para ensino do uso correto de dispositivos inalatórios, fisioterapeuta respiratório para reabilitação pulmonar, alergologista para identificação de desencadeantes e imunoterapia, e psicólogo para manejo do impacto emocional em crianças com asma grave. Programas estruturados de educação em asma — ensinando criança, pais e escola a reconhecer e responder a crises — reduzem internações em 30-50% em estudos internacionais. Clínicas que investem nessa estrutura multidisciplinar têm resultados superiores e diferencial competitivo claro."),
        ("Diagnóstico e Tecnologia em Pneumologia Pediátrica",
         "Espirometria é o exame padrão-ouro para diagnóstico e acompanhamento da asma (limitada a crianças cooperativas acima de 5-6 anos), complementada por testes de broncodilatação e broncoprovocação. Em lactentes e crianças pequenas, oscilometria e pletismografia corporal permitem avaliação funcional sem colaboração ativa. Óxido nítrico exalado (FeNO) avalia inflamação eosinofílica das vias aéreas, guiando o uso de corticosteroides inalatórios. Polissonografia pediátrica avalia distúrbios respiratórios do sono. Clínicas que investem nesse portfólio diagnóstico se posicionam como referência técnica que atrai casos complexos de toda a região."),
        ("Educação em Asma e Engajamento de Famílias",
         "A educação em asma é componente terapêutico fundamental, não acessório. Crianças e pais que entendem os gatilhos da asma, reconhecem os sinais de agravamento e dominam a técnica inalatória correta têm controle da doença muito superior. Consultas educacionais estruturadas, grupos de educação em asma para famílias, materiais didáticos adaptados para diferentes idades e planos de ação individualizados para crises são ferramentas que a clínica deve incorporar. Envolvimento da escola — orientação de professores sobre asma e emergências — é diferencial que melhora adesão e segurança da criança."),
        ("Modelo de Negócio e Crescimento em Pneumologia Pediátrica",
         "Pneumologia pediátrica combina alta recorrência (asma é condição crônica com retornos regulares), procedimentos diagnósticos de valor agregado (espirometria, FeNO, polissonografia) e potencial de expansão para serviços complementares (fisioterapia respiratória, imunoterapia para alergias respiratórias). A construção de referência entre pediatras da região — através de comunicação ativa dos resultados clínicos, disponibilidade para segunda opinião e resposta rápida a casos urgentes — é o principal motor de crescimento por encaminhamentos. Infoprodutores que criam conteúdo educativo para pais de crianças asmáticas têm audiência massiva nas redes sociais."),
    ],
    faq_list=[
        ("Como saber se meu filho tem asma ou é só bronquite?",
         "'Bronquite' em crianças é frequentemente asma não diagnosticada. Se a criança tem 3 ou mais episódios de tosse ou chiado por ano, especialmente desencadeados por resfriado, exercício ou exposição a pó e animais, ou se há história familiar de asma e alergia, avaliação por pneumologista pediátrico ou alergologista é indicada. O diagnóstico de asma em crianças pequenas é clínico; em maiores de 5 anos, a espirometria confirma."),
        ("Corticoide inalatório prejudica o crescimento da criança?",
         "Em doses baixas a moderadas, os corticosteroides inalatórios modernos têm efeito mínimo sobre o crescimento — muito inferior ao impacto de asma mal controlada, que por si causa retardo de crescimento. O benefício do controle adequado da asma supera amplamente o risco de impacto no crescimento nas doses terapêuticas habituais. O pneumologista pediátrico monitora crescimento e ajusta doses para usar a menor dose eficaz."),
        ("Com que frequência crianças com asma devem consultar o pneumologista pediátrico?",
         "Para asma bem controlada: a cada 3-6 meses. Para asma moderada ou grave: a cada 1-3 meses até estabilização. Em agudizações: avaliação imediata. Além das consultas regulares, revisão anual da técnica inalatória e do plano de ação é fundamental — estudos mostram que a maioria das famílias perde a técnica correta ao longo do tempo sem revisão regular."),
    ]
)

# ── Article 5513 — SaaS Sales: Clínicas de Reabilitação e Dependência Química ──
art(
    slug="vendas-para-o-setor-de-saas-de-clinicas-de-reabilitacao-e-dependencia-quimica",
    title="Vendas para o Setor de SaaS de Clínicas de Reabilitação e Dependência Química | ProdutoVivo",
    desc="Como vender SaaS para clínicas de reabilitação e dependência química no Brasil: tomadores de decisão, dores operacionais e estratégias. Guia para infoprodutores.",
    h1="Vendas para o Setor de SaaS de Clínicas de Reabilitação e Dependência Química",
    lead="Clínicas de reabilitação, comunidades terapêuticas e centros de tratamento de dependência química formam um segmento de saúde com necessidades específicas de gestão e crescente demanda por digitalização. Para infoprodutores e consultores de vendas B2B SaaS, esse nicho tem compradores motivados por compliance regulatório e eficiência operacional.",
    sections=[
        ("O Mercado de Reabilitação e Dependência Química no Brasil",
         "O Brasil tem mais de 2.000 comunidades terapêuticas e centros de tratamento de dependência química registrados, atendendo dependentes de álcool, crack, cocaína, maconha e outras drogas. O setor é regulado pela ANVISA e pelos CAPS-AD (Centros de Atenção Psicossocial — Álcool e Drogas) do SUS, com forte componente de entidades filantrópicas e religiosas além dos serviços privados. A crescente prevalência do uso de drogas no Brasil, combinada com maior consciência sobre o caráter de doença da dependência química, aumenta a demanda por serviços especializados e de qualidade."),
        ("Dores Operacionais e Demanda por Tecnologia",
         "Clínicas e comunidades terapêuticas enfrentam: gestão de prontuários de internos com histórico de tratamento, controle de medicação (dispensação, administração e registro), gestão financeira de mensalidades e convênios, comunicação com familiares (parte essencial do tratamento), controle de saídas e passes terapêuticos, relatórios para CONAD, SENAD e órgãos regulatórios, e gestão de equipe multidisciplinar (psiquiatras, psicólogos, assistentes sociais, terapeutas ocupacionais). Sistemas de gestão específicos para reabilitação eliminam papelada, reduzem erros de medicação e facilitam a conformidade regulatória."),
        ("Tomadores de Decisão e Abordagem Comercial",
         "Em comunidades terapêuticas e clínicas menores, o diretor geral ou o coordenador clínico decide a compra. Em grupos maiores de reabilitação privada, há envolvimento do financeiro e, às vezes, de TI. O ciclo de vendas é de 2-6 semanas para unidades independentes. A abordagem deve reconhecer a natureza sensível do setor: compradores são movidos por missão além do lucro, e a proposta de valor deve incluir como o sistema melhora a qualidade do cuidado e facilita o acolhimento das famílias — não apenas a eficiência operacional. Referências de outras clínicas e comunidades do mesmo segmento (especialmente religiosas ou filosóficas similares) têm peso enorme na decisão."),
        ("Conformidade Regulatória e Documentação Obrigatória",
         "Clínicas de reabilitação têm obrigações regulatórias específicas: prontuário do paciente seguindo resolução CFM, registro de dispensação de psicotrópicos seguindo portaria ANVISA, relatórios para CONAD e SENAD, habilitação do CRAS (Centro de Referência de Assistência Social) para comunidades terapêuticas beneficiadas pelo fundo federal, e conformidade com a Lei 10.216/2001 (Lei da Reforma Psiquiátrica). Sistemas que automatizam a geração desses documentos e relatórios, com alertas de vencimento de habilitações e renovações, são argumento de conformidade poderoso para gestores que temem auditorias."),
        ("Tendências: Telemedicina em Reabilitação e Pós-Alta",
         "A telemedicina está transformando o acompanhamento pós-alta em dependência química: grupos de apoio online, consultas psiquiátricas remotas e aplicativos de acompanhamento de sobriedade criam continuidade do cuidado após a internação — fase crítica onde a maioria das recaídas ocorre. Plataformas que integram gestão da internação com módulo de pós-alta e acompanhamento familiar criam diferencial de resultados clínicos que melhora a reputação da clínica e o boca a boca positivo. Infoprodutores que abordam a digitalização do cuidado em dependência química têm audiência crescente num tema de enorme relevância social."),
    ],
    faq_list=[
        ("Qual a diferença entre comunidade terapêutica e clínica de reabilitação?",
         "Comunidades terapêuticas (CTs) são entidades predominantemente residenciais de caráter social, filantrópico ou religioso, que usam a convivência comunitária como instrumento terapêutico principal. Clínicas de reabilitação são estabelecimentos de saúde com equipe médica e clínica estruturada, podendo oferecer desintoxicação, tratamento psiquiátrico e suporte clínico mais intensivo. Ambas podem ser complementares na trajetória de tratamento do dependente."),
        ("SaaS para reabilitação precisa de conformidade com LGPD?",
         "Sim, com atenção redobrada. Dados de saúde são dados sensíveis na LGPD, e dados de dependência química são especialmente delicados — vazamentos podem estigmatizar pacientes e gerar danos irreparáveis. O fornecedor SaaS deve oferecer contrato de processamento de dados (DPA), criptografia em repouso e em trânsito, log de auditoria de acessos e políticas claras de retenção e exclusão de dados. Gestores de CTs e clínicas devem exigir essas garantias antes de contratar qualquer sistema."),
        ("Comunidades terapêuticas podem usar recursos do governo para tecnologia?",
         "Sim. CTs habilitadas pelo SENAD e credenciadas pelo Ministério da Cidadania recebem recursos do fundo específico (FUNAD/SENAD). Esses recursos podem ser utilizados para melhorias operacionais, incluindo sistemas de gestão, desde que haja previsão no plano de trabalho aprovado. O gestor deve verificar as regras específicas da habilitação da sua CT para confirmar a utilização."),
    ]
)

# ── Article 5514 — Consulting: Estratégia de Entrada em Novos Mercados ──
art(
    slug="consultoria-de-estrategia-de-entrada-em-novos-mercados-e-market-entry",
    title="Consultoria de Estratégia de Entrada em Novos Mercados e Market Entry | ProdutoVivo",
    desc="Como estruturar consultoria de estratégia de entrada em novos mercados: metodologias, análise de oportunidades, go-to-market e precificação. Guia para infoprodutores.",
    h1="Consultoria de Estratégia de Entrada em Novos Mercados e Market Entry",
    lead="Expansão para novos mercados é uma das decisões estratégicas mais complexas e de maior risco em empresas de crescimento. Para infoprodutores e consultores estratégicos, a consultoria de market entry combina análise rigorosa de mercado com design de go-to-market adaptado ao contexto específico de cada expansão.",
    sections=[
        ("Por Que Market Entry Requer Consultoria Especializada",
         "A entrada em novos mercados — sejam geográficos (nova cidade, estado ou país) ou de segmento (novo vertical ou tipo de cliente) — envolve riscos e incertezas que a equipe interna raramente consegue avaliar com objetividade. Viés de confirmação, falta de dados locais, superestimação do tamanho do mercado e subestimação de competidores locais são armadilhas clássicas. O consultor de market entry traz perspectiva externa, metodologia de análise rigorosa, acesso a dados de mercado e experiência em expansões anteriores — reduzindo o risco de a empresa investir pesadamente em mercado que não tem a tração esperada."),
        ("Análise de Oportunidade e Dimensionamento de Mercado",
         "A análise de market entry começa pela quantificação da oportunidade: TAM (Total Addressable Market), SAM (Serviceable Addressable Market) e SOM (Serviceable Obtainable Market) no novo mercado, análise da concorrência local (diretos, indiretos e substitutos), mapeamento das barreiras de entrada (regulação, relacionamentos estabelecidos, custo de aquisição de clientes), e análise das diferenças culturais e de comportamento do novo cliente vs. o mercado atual. Fontes primárias (entrevistas com potenciais clientes e canais no novo mercado) são tão importantes quanto fontes secundárias (relatórios, dados do IBGE, estudos setoriais)."),
        ("Design do Go-to-Market para o Novo Mercado",
         "O go-to-market do novo mercado raramente é cópia do mercado de origem. O consultor de market entry ajuda a definir: qual segmento atacar primeiro (beachhead strategy — escolher o nicho onde a proposta de valor é mais diferenciada e o ciclo de vendas mais curto), qual modelo de entrada é mais eficiente (escritório próprio, parceria com empresa local, distribuidor, agente ou aquisição), qual adaptação da proposta de valor é necessária para o contexto local, e qual é o plano de investimento mínimo para teste do mercado antes de comprometer recursos maiores."),
        ("Piloto, Validação e Decisão de Escalar",
         "A abordagem mais eficiente de market entry é o piloto controlado: entrar em escala reduzida com orçamento limitado, definir métricas de sucesso claras (CPL, taxa de conversão, NPS dos primeiros clientes, tempo de onboarding), estabelecer prazo de avaliação (tipicamente 6-12 meses) e critérios explícitos de decisão entre escalar, pivotar ou retirar. Esse approach lean de expansão reduz drasticamente o custo de falha — descobrir que o mercado não tem o potencial esperado depois de R$50k investidos é muito melhor que depois de R$2M. O consultor acompanha o piloto, analisa os dados e suporta a decisão com evidências."),
        ("Expansão Regional no Brasil: Especificidades e Oportunidades",
         "No Brasil, expansão para novos estados ou regiões tem especificidades únicas: diferenças culturais relevantes (nordeste vs. sudeste vs. sul têm preferências e comportamentos de compra distintos), variações na infraestrutura logística, diferenças na intensidade da competição regional (muitos nichos têm players fortes em São Paulo mas mercado vazio no Norte e Centro-Oeste), e considerações tributárias de ICMS e substituição tributária que afetam preços e margens. Consultores com experiência em expansão nacional brasileira entregam value específico que generalistas internacionais não conseguem replicar."),
    ],
    faq_list=[
        ("Como saber se vale a pena entrar em um novo mercado?",
         "O framework básico: o mercado é grande o suficiente para justificar o investimento? Nossa proposta de valor é diferenciada o suficiente para capturar share contra competidores estabelecidos? Temos os recursos (capital, pessoas, tempo) para sustentar a entrada até o break-even? As respostas precisam vir de dados, não de intuição. Um diagnóstico de market entry bem feito responde essas três perguntas com evidências suficientes para uma decisão fundamentada."),
        ("Qual a diferença entre expansão geográfica e expansão de segmento?",
         "Expansão geográfica mantém o produto/serviço essencialmente igual, mas adapta go-to-market para um novo local — novos canais, nova equipe de vendas, adaptações culturais na comunicação. Expansão de segmento leva o produto a um tipo de cliente novo — pode exigir adaptações de produto, nova proposta de valor e abordagem comercial diferente. Segmento tende a ser mais complexo porque exige mais mudanças no produto e na mensagem; geográfico, quando a proposta de valor é similar, é mais replicável se a execução for adaptada ao contexto local."),
        ("Qual o erro mais comum em estratégias de market entry?",
         "Subestimar o tempo e o custo de aquisição de clientes no novo mercado. Empresas habitualmente transferem sua taxa de conversão do mercado de origem para o novo mercado e ficam surpresas quando é 2-5x pior — porque no mercado de origem há brand awareness acumulado, referências existentes e histórico de relacionamentos. O novo mercado exige reinvestimento na construção de credibilidade e reputação, que leva tempo. O planejamento financeiro do market entry deve prever explicitamente esse custo de bootstrapping do novo mercado."),
    ]
)

# ── Article 5515 — B2B SaaS: Cibersegurança e Proteção de Endpoints ──
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-ciberseguranca-e-protecao-de-endpoints",
    title="Gestão de Negócios para Empresas de B2B SaaS de Cibersegurança e Proteção de Endpoints | ProdutoVivo",
    desc="Estratégias de gestão para empresas B2B SaaS de cibersegurança e proteção de endpoints: crescimento, diferenciação e mercado. Guia para infoprodutores.",
    h1="Gestão de Negócios para Empresas de B2B SaaS de Cibersegurança e Proteção de Endpoints",
    lead="Plataformas de cibersegurança e proteção de endpoints são infraestrutura crítica de defesa para empresas de todos os portes. Para infoprodutores e consultores que atendem o mercado de segurança digital, entender como empresas nesse espaço crescem e competem é essencial para criar conteúdos técnicos de alto valor.",
    sections=[
        ("O Mercado de Cibersegurança B2B SaaS",
         "O mercado global de cibersegurança supera US$200 bilhões e cresce acima de 12% ao ano, impulsionado pela escalada de ataques de ransomware, phishing e comprometimento de credenciais. No Brasil, ataques ransomware a empresas e órgãos públicos cresceram mais de 200% em 3 anos. A proteção de endpoints — laptops, desktops, servidores e dispositivos móveis corporativos — é a camada de defesa mais crítica e o maior mercado de segurança empresarial. Plataformas como CrowdStrike, SentinelOne, Microsoft Defender e Carbon Black dominam o enterprise; há espaço crescente para soluções mid-market e SMB com propostas mais acessíveis."),
        ("EDR, XDR e a Evolução da Proteção de Endpoints",
         "A geração atual de proteção de endpoints evoluiu de antivírus baseado em assinatura para EDR (Endpoint Detection and Response): detecção comportamental de ameaças desconhecidas, investigação automática de incidentes e resposta orquestrada. O XDR (Extended Detection and Response) amplia a visibilidade além do endpoint para incluir rede, nuvem e e-mail em uma plataforma unificada de detecção e resposta. Plataformas que oferecem XDR simplificam a operação de segurança — reduzindo o número de ferramentas e consoles que analistas de SOC precisam gerenciar — e têm argumento de consolidação muito persuasivo junto a CISOs."),
        ("Go-to-Market: CISOs, IT Managers e MSSPs",
         "O mercado de cybersecurity SaaS tem dois canais principais: vendas diretas a CISOs e diretores de TI (para enterprise e mid-market) e canal indireto via MSSPs — Managed Security Service Providers — que gerenciam segurança para clientes menores. O MSSP é um multiplicador poderoso: um parceiro MSSP com 100 clientes SMBs pode gerar ARR significativo com um único contrato de distribuição. Construir programa de parceiros robusto para MSSPs — com margem atrativa, treinamento técnico e ferramentas de gestão multi-tenant — é frequentemente o go-to-market mais eficiente para plataformas que miram o mercado SMB."),
        ("Compliance, LGPD e Segurança como Argumento Regulatório",
         "A LGPD tornou a segurança da informação obrigação legal para empresas brasileiras: violações de dados têm multas de até 2% do faturamento (máximo R$50M por infração), além de danos reputacionais. O consultor de segurança que conecta proteção de endpoints a conformidade com LGPD, GDPR, PCI DSS e normas setoriais (BACEN para bancos, ANVISA para saúde) converte a conversa de custo para risco legal e regulatório — argumento muito mais convincente para CEOs e CFOs que não falam linguagem técnica de segurança."),
        ("Tendências: IA em Segurança e Consolidação de Plataformas",
         "IA é o frontier mais ativo em cibersegurança: detecção de anomalias com machine learning que identifica comportamentos maliciosos sem assinaturas conhecidas, análise de threat intelligence em escala para correlacionar indicadores de comprometimento globais, e geração automática de respostas a incidentes reduzindo o MTTD/MTTR (tempo de detecção e resposta). A tendência de consolidação — empresas preferem 1-2 plataformas abrangentes a 10-15 ferramentas pontuais — favorece players com portfólio amplo e integrado. Plataformas que adicionam capacidades adjacentes (SIEM, SOAR, gestão de vulnerabilidades) ao EDR core capturam mais wallet share por cliente."),
    ],
    faq_list=[
        ("Antivírus tradicional ainda serve para proteger empresas?",
         "Para ameaças simples e conhecidas, sim. Mas para ransomware sofisticado, ataques fileless e comprometimento de credenciais — as ameaças que realmente causam danos críticos — antivírus baseado em assinatura tem taxa de detecção muito inferior ao EDR comportamental. Empresas com dados sensíveis, obrigações regulatórias ou dependência crítica de TI devem evoluir para EDR como mínimo de proteção adequada."),
        ("Qual o custo típico de proteção de endpoints para PMEs?",
         "Soluções EDR mid-market custam de R$15 a R$60 por endpoint por mês, dependendo do número de dispositivos e do nível de suporte. Uma empresa com 100 endpoints pode implementar proteção EDR de qualidade por R$1.500 a R$6.000/mês — muito menos que o custo médio de um incidente de ransomware (R$500k a R$5M em recuperação, tempo parado e dano reputacional). O argumento de ROI em segurança é sempre comparar o custo de proteção com o custo esperado de um incidente."),
        ("MSSPs são uma boa opção para empresas sem equipe de TI de segurança?",
         "Sim, especialmente para PMEs. Um MSSP oferece monitoramento 24/7, resposta a incidentes, gestão de patches e relatórios de compliance por um valor mensal fixo — substituindo a necessidade de contratar analistas de segurança internos (caros e escassos no mercado). Certifique-se de que o MSSP tem SLA claro de tempo de resposta a incidentes e transparência sobre quais ferramentas usa na prestação do serviço."),
    ]
)

# ── Article 5516 — Clinic: Cardiologia Pediátrica e Cardiopatias Congênitas ──
art(
    slug="gestao-de-clinicas-de-cardiologia-pediatrica-e-cardiopatias-congenitas",
    title="Gestão de Clínicas de Cardiologia Pediátrica e Cardiopatias Congênitas | ProdutoVivo",
    desc="Guia de gestão para clínicas de cardiologia pediátrica e cardiopatias congênitas: modelo assistencial, tecnologia, financiamento e crescimento. Para infoprodutores da saúde.",
    h1="Gestão de Clínicas de Cardiologia Pediátrica e Cardiopatias Congênitas",
    lead="A cardiologia pediátrica e o tratamento de cardiopatias congênitas representam uma das especialidades médicas de maior complexidade e impacto emocional. Para infoprodutores da saúde, entender a gestão de centros nessa área significa explorar um nicho de excelência técnica com demanda crescente por serviços de referência.",
    sections=[
        ("A Cardiologia Pediátrica no Brasil",
         "As cardiopatias congênitas afetam cerca de 1% de todos os nascidos vivos no Brasil — aproximadamente 30.000 novos casos por ano. Desde defeitos simples como comunicação interatrial (CIA) e comunicação interventricular (CIV) até malformações complexas como Tetralogia de Fallot e transposição das grandes artérias, o espectro de condições exige equipe altamente especializada e estrutura hospitalar robusta. O Brasil tem déficit histórico de centros de cardiologia congênita de referência — a maioria concentrada em capitais — criando oportunidade para serviços de qualidade em centros regionais com telemedicina e parcerias com centros terciários."),
        ("Equipe Multidisciplinar e Estrutura Assistencial",
         "Um centro de referência em cardiopatias congênitas exige equipe multidisciplinar: cardiologistas pediátricos, cirurgiões cardíacos pediátricos, intensivistas pediátricos cardíacos, ecocardiografistas especializados em cardiopatias congênitas, hemodinamicistas pediátricos, enfermeiros especializados, perfusionistas, anestesiologistas cardíacos pediátricos e psicólogos para suporte a famílias. A complexidade cirúrgica — operações em recém-nascidos com coração do tamanho de uma ameixa — exige treinamento especializado e volume mínimo de procedimentos para manutenção da habilidade técnica."),
        ("Diagnóstico Pré-natal e Acolhimento de Famílias",
         "O diagnóstico pré-natal de cardiopatia congênita por ecocardiografia fetal (entre 18-22 semanas de gestação) permite planejamento do parto em centro com infraestrutura adequada e aconselhamento familiar antes do nascimento. O acolhimento da família após o diagnóstico é momento crítico: comunicação clara e empática sobre a condição, o prognóstico e o plano de tratamento faz diferença enorme na adesão ao tratamento e no bem-estar familiar. Centros de referência que estruturam programas de aconselhamento genético integrado, suporte psicológico e grupos de famílias com cardiopatias congênitas criam diferencial assistencial e humano único."),
        ("Modelo de Negócio e Financiamento em Cardiologia Congênita",
         "Cardiopatias congênitas têm cobertura obrigatória pelos planos de saúde para procedimentos no ROL ANS. Cirurgias cardíacas pediátricas têm custo elevadíssimo — envolvendo UTI neonatal/pediátrica, UTI cardíaca, sala cirúrgica especializada, equipamentos de circulação extracorpórea e internação prolongada — com reembolso frequentemente insuficiente pelas operadoras. Muitos centros de referência operam no modelo público-privado, com SUS financiando parte dos casos via AIH. A negociação com planos de saúde requer argumentação técnica sólida sobre custo-efetividade do tratamento cirúrgico precoce vs. complicações de longo prazo."),
        ("Telemedicina e Acesso a Referência em Cardiologia Congênita",
         "A telemedicina democratiza o acesso à cardiologia pediátrica de referência: teleconsultas com especialistas em centros terciários para casos diagnosticados em cidades sem especialista local, laudos de ecocardiograma fetal remoto para obstetrizes em regiões sem cardiologista pediátrico, e acompanhamento pós-operatório remoto de pacientes que retornam para suas cidades após cirurgia em centro de referência. Infoprodutores que criam conteúdo educativo para pais de crianças com cardiopatias congênitas — explicando condições, tratamentos e o que esperar — têm audiência apaixonada e extremamente engajada nesse universo."),
    ],
    faq_list=[
        ("Cardiopatia congênita sempre precisa de cirurgia?",
         "Não. Muitas cardiopatias leves, como CIA pequena e CIV pequena, fecham espontaneamente sem intervenção. Outras, como estenose pulmonar leve, são monitoradas e só tratadas se progredir. Cardiopatias graves, como Tetralogia de Fallot e transposição das grandes artérias, requerem correção cirúrgica — geralmente no primeiro ano de vida. O cardiologista pediátrico define o momento e o tipo de intervenção mais adequado para cada caso."),
        ("O SUS cobre cirurgia cardíaca pediátrica para cardiopatias congênitas?",
         "Sim. O SUS cobre cirurgias cardíacas para cardiopatias congênitas através dos centros de referência credenciados. A fila de espera varia por região e pela complexidade do caso — casos urgentes têm prioridade. Famílias em regiões sem centro de referência podem receber auxílio para transporte e acomodação via protocolos de transferência interestaduais."),
        ("Como é o desenvolvimento de crianças com cardiopatias congênitas corrigidas?",
         "A maioria das crianças com cardiopatias congênitas corrigidas cirurgicamente tem desenvolvimento normal ou próximo do normal. Algumas condições mais complexas podem deixar sequelas que requerem acompanhamento cardiológico ao longo da vida, restrições esportivas específicas ou novas intervenções na adolescência ou idade adulta. O cardiologista pediátrico acompanha o desenvolvimento cardíaco e orienta sobre atividades físicas, gravidez (para adolescentes) e transição para o cardiologista de adultos."),
    ]
)

# ── Article 5517 — SaaS Sales: Parques Aquáticos, Temáticos e de Entretenimento ──
art(
    slug="vendas-para-o-setor-de-saas-de-parques-aquaticos-tematicos-e-entretenimento",
    title="Vendas para o Setor de SaaS de Parques Aquáticos, Temáticos e de Entretenimento | ProdutoVivo",
    desc="Como vender SaaS para parques aquáticos, temáticos e locais de entretenimento no Brasil: tomadores de decisão, dores operacionais e estratégias. Guia para infoprodutores.",
    h1="Vendas para o Setor de SaaS de Parques Aquáticos, Temáticos e de Entretenimento",
    lead="O mercado de lazer e entretenimento no Brasil — parques aquáticos, parques temáticos, cinemas, teatros, boliches e centros de entretenimento familiar — é um segmento em crescimento com necessidades específicas de gestão de bilheteria, experiência do visitante e operações. Para infoprodutores e consultores de vendas B2B SaaS, esse nicho combina sazonalidade interessante com dores operacionais claras.",
    sections=[
        ("O Mercado de Entretenimento e Parques no Brasil",
         "O Brasil tem mais de 200 parques aquáticos e temáticos, milhares de cinemas, teatros, casas de shows, boliches, arenas de esportes indoor e centros de entretenimento familiar. O mercado de lazer cresce com o aumento da renda e a valorização da experiência como forma de consumo — especialmente entre gerações millennials e Z. Parques aquáticos têm sazonalidade intensa (pico no verão), mas desenvolvem estratégias de temporadas temáticas e eventos para mitigar a queda no inverno. A gestão de experiência do visitante — do ingresso online à saída satisfeita — é o diferencial competitivo central nesse mercado."),
        ("Dores Operacionais e Oportunidades para SaaS",
         "As principais dores de parques e locais de entretenimento incluem: venda de ingressos online com controle de capacidade máxima e filas por horário, gestão de passes e pacotes (anual, VIP, combos de ingresso + alimentação), controle de acesso com catracas e validação de QR codes, gestão de lockers e aluguel de equipamentos, análise de visitante por horário e atrativo (para alocar equipe eficientemente), programa de fidelidade para visitantes recorrentes, e integração com sistemas de PDV de alimentação e merchandise interno. Sistemas que automatizam esses fluxos reduzem filas, aumentam receita por visitante e melhoram NPS."),
        ("Tomadores de Decisão e Ciclo de Compra",
         "Em parques independentes de médio porte, o diretor geral ou o gerente de operações lidera a decisão, com influência do TI e do financeiro. Em redes de entretenimento, a decisão é centralizada na matriz. O ciclo de vendas é de 2-4 meses, com período de implantação planejado para a baixa temporada (inverno). Demonstrações que simulam a operação do parque — venda online de ingressos, controle de acesso no pico de horário, relatórios de visitação por atrativo — convertem muito mais que apresentações de funcionalidades em slides."),
        ("Estratégias de Penetração no Mercado de Entretenimento",
         "Associações como ADIBRA (Associação dos Distribuidores de Parques Aquáticos do Brasil) e ABILUMI (Associação Brasileira de Iluminação e Entretenimento) reúnem decisores setoriais. Feiras como ATREX e eventos de turismo de negócios são pontos de encontro relevantes. Conteúdo especializado — como melhorar experiência do visitante, como aumentar receita por visitante com upsell digital, como usar dados de visitação para otimizar operações — atrai gestores do setor via SEO e LinkedIn. Cases de parques que aumentaram visitação ou NPS após adoção do sistema são o argumento de venda mais poderoso."),
        ("Tendências: Experiência Imersiva, App do Visitante e Revenue Management",
         "Parques e locais de entretenimento investem em experiência imersiva: AR/VR integrado às atrações, personalização via app do visitante (roteiro sugerido com base em preferências, alertas de fila em tempo real, upgrade de ingresso dinâmico), e gamificação (missões no parque, recompensas por visitas). Revenue management — precificação dinâmica por dia da semana, horário e sazonalidade, similar ao de hotéis e companhias aéreas — está chegando ao setor de parques, com tecnologia SaaS que ajusta preços automaticamente para maximizar ocupação e receita. Infoprodutores que educam sobre essas inovações têm audiência crescente no setor."),
    ],
    faq_list=[
        ("Qual o ticket médio de SaaS de gestão para parques?",
         "Varia muito com o porte: parques pequenos (até 50.000 visitantes/ano) pagam R$300 a R$1.000/mês. Parques médios: R$1.000 a R$5.000/mês. Grandes parques e redes: R$5.000 a R$30.000/mês, com implantação adicional de R$20k a R$200k. O ROI é mensurável: redução de filas no acesso (que aumenta percepção de qualidade e NPS), upsell digital no momento da compra (que pode aumentar receita por visitante em 15-25%) e insights de operação que reduzem desperdício de equipe."),
        ("Controle de acesso por QR code funciona em parques com alto volume de visitantes?",
         "Sim, com infraestrutura adequada. Leitores de QR code de alta velocidade (menos de 0,5 segundos por validação) com servidores locais (não dependentes de internet em tempo real) suportam fluxos de 1.000-3.000 entradas por hora por catraca. A chave é o planejamento correto de número de catracas e a integração entre sistema de venda e sistema de controle de acesso para evitar gargalos no pico."),
        ("Como a sazonalidade afeta a estratégia de vendas de SaaS para parques?",
         "A sazonalidade é real: parques aquáticos têm 60-70% da receita concentrada em 4-5 meses. Para SaaS, isso significa: (1) abordar no inverno, quando gestores têm tempo para avaliar e implementar; (2) oferecer plano com desconto nos meses de baixa temporada ou preço fixo anual; (3) mostrar como o sistema ajuda a monetizar o inverno com eventos temáticos e estratégias de captação para a temporada seguinte."),
    ]
)

# ── Article 5518 — Consulting: Gestão de Terceiros e Outsourcing Estratégico ──
art(
    slug="consultoria-de-gestao-de-terceiros-e-outsourcing-estrategico",
    title="Consultoria de Gestão de Terceiros e Outsourcing Estratégico | ProdutoVivo",
    desc="Como estruturar consultoria de gestão de terceiros e outsourcing estratégico: metodologias, frameworks de decisão, governança e precificação. Guia para infoprodutores e consultores.",
    h1="Consultoria de Gestão de Terceiros e Outsourcing Estratégico",
    lead="A decisão de terceirizar processos ou funções — e como governar eficientemente os fornecedores terceirizados — é desafio estratégico central para empresas que buscam foco no core business sem perder controle sobre qualidade e custo. Para infoprodutores e consultores, esse é um nicho com demanda constante e metodologia sofisticada.",
    sections=[
        ("O Framework Make vs. Buy vs. Partner",
         "A decisão de outsourcing começa com o framework fundamental Make vs. Buy vs. Partner: desenvolver internamente (make), terceirizar completamente (buy/outsource) ou criar parceria estratégica (partner). O critério central é a relevância estratégica da atividade: processos que são core competence devem ser desenvolvidos internamente; processos que são necessários mas não diferenciados podem ser terceirizados para liberação de recursos para o core; atividades onde a empresa precisa de acesso a expertise ou capacidade não disponível internamente favorecem parcerias. O erro mais comum é terceirizar atividades estratégicas por redução de custo imediata, comprometendo capacidade diferenciadora de longo prazo."),
        ("Seleção, Contratação e Governança de Fornecedores",
         "A qualidade do outsourcing é determinada pela qualidade do processo de seleção: RFP bem estruturada com critérios claros, due diligence de capacidade técnica e financeira do fornecedor, análise de referências com clientes similares, e negociação de SLAs, KPIs, penalidades e mecanismos de saída. O contrato de outsourcing deve prever: escopo claro e mecanismo de gestão de mudanças de escopo, métricas de desempenho com periodicidade de avaliação, plano de continuidade em caso de falha do fornecedor, e termos de encerramento que preservem o acesso a dados e a capacidade de transição para outro fornecedor."),
        ("Gestão de Desempenho e Relacionamento com Fornecedores",
         "Outsourcing sem governança ativa se deteriora: fornecedores otimizam para seus próprios interesses quando não há acompanhamento rigoroso. A governança de fornecedores inclui reuniões de desempenho com cadência definida (operacional semanal, tática mensal, estratégica trimestral), dashboard de KPIs em tempo real, mecanismo de escalonamento de problemas com SLA de resolução, e revisão anual do contrato com benchmarking de mercado. O consultor de gestão de terceiros implementa esses processos e frequentemente atua como facilitador das relações fornecedor-cliente em momentos de tensão."),
        ("Riscos de Outsourcing e Estratégias de Mitigação",
         "Os principais riscos de outsourcing incluem: dependência excessiva de um único fornecedor (lock-in), perda de capacidade interna de avaliar a qualidade do serviço terceirizado, vazamentos de dados e propriedade intelectual, descontinuidade do fornecedor (falência, fusão, mudança de estratégia) e conflitos de interesse. A mitigação passa por: diversificação de fornecedores em processos críticos, manutenção de capacidade mínima interna para supervisão técnica, acordos robustos de confidencialidade e proteção de dados, e planos de contingência (BCP) que incluam transição de fornecedores."),
        ("Tendências: Outsourcing de IA, Offshore e Near-Shore",
         "O outsourcing de processos baseados em IA — onde fornecedores especialistas treinam e operam modelos de linguagem, visão computacional e automação inteligente para os clientes — é o crescimento mais acelerado no setor. Near-shore para o Brasil — contratar equipes de tecnologia em países da América Latina com fuso horário compatível e custo inferior ao dos EUA — é modelo crescente para empresas norte-americanas e abertura para prestadores brasileiros. Consultores que dominam a estratégia de outsourcing no contexto de IA e trabalho remoto global têm proposta de valor atual e diferenciada no mercado corporativo."),
    ],
    faq_list=[
        ("BPO e outsourcing são a mesma coisa?",
         "BPO (Business Process Outsourcing) é um tipo específico de outsourcing onde processos de negócio inteiros são delegados a terceiros — exemplos clássicos são BPO de RH (folha de pagamento, benefícios), BPO financeiro (contas a pagar/receber) e BPO de atendimento ao cliente (call center). Outsourcing é o termo mais amplo que inclui BPO, ITO (outsourcing de TI), outsourcing de manufatura e outros. BPO é sempre outsourcing, mas outsourcing não é sempre BPO."),
        ("Como calcular o TCO (Total Cost of Ownership) de uma decisão de outsourcing?",
         "TCO de outsourcing inclui: custo direto do contrato com o fornecedor, mais custo interno de gestão do fornecedor (horas da equipe dedicadas à governança), custo de transição inicial (migração de processos, treinamento do fornecedor), custo de risco (seguro, provisão para penalidades por falha do fornecedor) e custo de saída (caso precise trocar de fornecedor no futuro). Compare com o TCO de manutenção interna do processo — que inclui salários, benefícios, overhead, tecnologia e desenvolvimento contínuo da equipe."),
        ("Outsourcing de TI prejudica a capacidade de inovação?",
         "Pode, se mal estruturado. Terceirizar totalmente o desenvolvimento de software significa perder capacidade de iterar rapidamente, de construir conhecimento interno sobre o produto e de atrair talentos técnicos que querem trabalhar em produto, não em serviço. A abordagem mais equilibrada é manter o core do produto internamente e terceirizar capacidades periféricas — infraestrutura, qualidade, dados — onde a especialização do fornecedor supera o custo de manter internamente."),
    ]
)

# ── Sitemap update ──
sm_path = pathlib.Path(__file__).parent / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")
new_urls = ""
for slug in [
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-cms-e-gestao-de-conteudo-headless",
    "gestao-de-clinicas-de-pneumologia-pediatrica-e-asma-infantil",
    "vendas-para-o-setor-de-saas-de-clinicas-de-reabilitacao-e-dependencia-quimica",
    "consultoria-de-estrategia-de-entrada-em-novos-mercados-e-market-entry",
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-ciberseguranca-e-protecao-de-endpoints",
    "gestao-de-clinicas-de-cardiologia-pediatrica-e-cardiopatias-congenitas",
    "vendas-para-o-setor-de-saas-de-parques-aquaticos-tematicos-e-entretenimento",
    "consultoria-de-gestao-de-terceiros-e-outsourcing-estrategico",
]:
    new_urls += f"\n  <url><loc>{DOMAIN}/blog/{slug}/</loc></url>"
sm_path.write_text(sm.replace("</urlset>", new_urls + "\n</urlset>"), encoding="utf-8")

# ── Trilha update ──
tr_path = pathlib.Path(__file__).parent / "trilha.html"
tr = tr_path.read_text(encoding="utf-8")
new_items = ""
for slug, label in [
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-cms-e-gestao-de-conteudo-headless", "CMS e Gestão de Conteúdo Headless SaaS"),
    ("gestao-de-clinicas-de-pneumologia-pediatrica-e-asma-infantil", "Pneumologia Pediátrica e Asma Infantil"),
    ("vendas-para-o-setor-de-saas-de-clinicas-de-reabilitacao-e-dependencia-quimica", "Clínicas de Reabilitação e Dependência Química SaaS"),
    ("consultoria-de-estrategia-de-entrada-em-novos-mercados-e-market-entry", "Estratégia de Entrada em Novos Mercados e Market Entry"),
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-ciberseguranca-e-protecao-de-endpoints", "Cibersegurança e Proteção de Endpoints SaaS"),
    ("gestao-de-clinicas-de-cardiologia-pediatrica-e-cardiopatias-congenitas", "Cardiologia Pediátrica e Cardiopatias Congênitas"),
    ("vendas-para-o-setor-de-saas-de-parques-aquaticos-tematicos-e-entretenimento", "Parques Aquáticos, Temáticos e de Entretenimento SaaS"),
    ("consultoria-de-gestao-de-terceiros-e-outsourcing-estrategico", "Gestão de Terceiros e Outsourcing Estratégico"),
]:
    new_items += f'\n    <li><a href="{DOMAIN}/blog/{slug}/">{label}</a></li>'
tr_path.write_text(tr.replace("</ul>", new_items + "\n  </ul>", 1), encoding="utf-8")

print("Done — batch 2014")
