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

# ── Article 4967 ── B2B SaaS: agendamento e reservas online
art(
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-agendamento-e-reservas-online",
    "Gestão de Negócios de Empresa de B2B SaaS de Agendamento e Reservas Online | ProdutoVivo",
    "Como construir e escalar um B2B SaaS de agendamento e reservas online. Estratégias de produto, verticais e go-to-market para o mercado de scheduling.",
    "Como Escalar um B2B SaaS de Agendamento e Reservas Online",
    "Agendamento online é um dos mercados de SaaS mais horizontais e competitivos — salões de beleza, clínicas, academias, consultórios, restaurantes, professores, consultores e centenas de outros negócios precisam de uma solução para permitir que clientes agendem horários online sem depender de ligações e WhatsApp. É um mercado de altíssimo volume mas com pressão de preço intensa — diferenciação por vertical e integrações é a chave.",
    [
        ("O problema de agendamento que o SaaS resolve",
         "Negócios que dependem de agendamento manual enfrentam: recepcionistas sobrecarregadas com ligações, clientes que mandam mensagem no WhatsApp às 23h sem resposta, cancelamentos de última hora sem confirmação prévia, agenda vazia por falta de lembretes automáticos, e impossibilidade de agendar fora do horário comercial. SaaS de agendamento resolve tudo isso: página de agendamento pública, confirmação automática, lembretes por SMS/WhatsApp/email, gestão de cancelamentos, e dashboard de ocupação da agenda."),
        ("Verticais de maior demanda",
         "Saúde e bem-estar (clínicas, consultórios, psicólogos, nutricionistas, dentistas) é o maior mercado — agenda lotada é crítica e o custo de não-comparecimento é alto. Beleza e estética (salões, barbearias, spas, clínicas estéticas) têm alta frequência de agendamento e ticketing menor. Educação (professores particulares, escolas de idioma, tutores) precisam de agendamento recorrente de aulas. Serviços profissionais (consultores, advogados, coaches) usam agendamento para reuniões e sessões. Cada vertical tem nuances de workflow — especializar o produto para um deles é a estratégia de diferenciação."),
        ("Funcionalidades que diferenciam plataformas de agendamento",
         "Página de agendamento personalizável (com logo, cores e serviços da empresa), regras de antecedência (mínimo de horas para agendar, janela de cancelamento sem penalidade), gestão de múltiplos profissionais e salas, agendamento recorrente (sessão toda segunda-feira às 14h), integração com Google Calendar e Outlook para sincronização bidirecional, pagamento antecipado no agendamento para reduzir no-show, fila de espera automática para horários lotados, e relatórios de ocupação e receita por profissional são os diferenciais avançados."),
        ("Redução de no-show: o ROI principal do SaaS de agendamento",
         "No-show (cliente que não aparece e não avisa) é o principal problema de negócios baseados em agenda — cada horário vazio é receita perdida irrecuperável. Lembretes automáticos por WhatsApp 24h e 2h antes do horário reduzem no-show em 40 a 70%. Confirmação ativa via link (cliente confirma ou cancela) 48h antes libera o horário para outro cliente. Cobrança antecipada ou política de cancelamento com taxa reduz no-show em sessões de alto valor (terapia, coaching, procedimentos estéticos). Calcular a receita recuperada de no-shows é o argumento de ROI mais poderoso na venda."),
        ("Go-to-market para SaaS de agendamento",
         "PLG com freemium (1 profissional, X agendamentos/mês gratuitos) é o modelo dominante — Calendly, Acuity Scheduling, Simply Book.me usam esse modelo. Para o mercado brasileiro, o diferencial é integração nativa com WhatsApp Business API (o canal de comunicação dominante no Brasil), página de agendamento em português perfeito, e suporte em PT-BR. Parceria com associações de profissionais de saúde, beleza e educação para planos com desconto é canal de crescimento de volume. Marketplace de agendamento (como Doctoralia para médicos) é modelo alternativo de distribuição."),
    ],
    [
        ("SaaS de agendamento precisa integrar com WhatsApp?",
         "No Brasil, sim — é praticamente obrigatório. WhatsApp é o canal de comunicação dominante entre pequenas empresas e clientes brasileiros. Lembretes de agendamento por WhatsApp têm taxa de abertura muito superior a SMS e email. Integração com WhatsApp Business API para envio de confirmações, lembretes e links de cancelamento é o diferencial competitivo mais valorizado no mercado brasileiro de scheduling. Plataformas que só enviam por email perdem para concorrentes que enviam por WhatsApp."),
        ("Como cobrar antecipadamente no agendamento?",
         "Cobrança antecipada no agendamento funciona via integração com gateway de pagamento (Stripe, PagSeguro, Mercado Pago) — o cliente paga no momento de agendar via Pix, cartão ou boleto. O valor é retido até a realização do serviço. Se o cliente cancela dentro da política, recebe reembolso; fora da política, paga a taxa de cancelamento. A implementação técnica é simples mas a política comercial precisa ser comunicada claramente no momento do agendamento para não criar atritos. Negócios de alto ticket (terapia, coaching) têm a maior adoção desse modelo."),
        ("Agendamento online reduz a necessidade de recepcionista?",
         "Agendamento online automatiza a entrada de agendamentos — elimina parte das chamadas telefônicas e mensagens de WhatsApp para marcar horário. Mas não elimina a recepcionista inteiramente: o acolhimento presencial, gestão de situações especiais, check-in e cobrança ainda são humanos. Em clínicas e consultórios menores, pode viabilizar reduzir uma recepcionista em meio período ou realocar o tempo para atividades de maior valor (atendimento presencial, faturamento). O ROI real é em produtividade e satisfação do cliente, não em eliminação de pessoal."),
    ]
)

# ── Article 4968 ── Clinics: cirurgia geral e videolaparoscopia
art(
    "gestao-de-clinicas-de-cirurgia-geral-e-videolaparoscopia",
    "Gestão de Clínicas de Cirurgia Geral e Videolaparoscopia | ProdutoVivo",
    "Guia de gestão para clínicas de cirurgia geral e videolaparoscopia: estrutura ambulatorial, procedimentos de alto valor e estratégias de crescimento.",
    "Gestão de Clínicas de Cirurgia Geral e Videolaparoscopia: Guia Completo",
    "Cirurgia geral é uma das especialidades com maior amplitude de atuação — abrange cirurgias do aparelho digestivo, parede abdominal, mamas, tireoide, procedimentos de urgência e videolaparoscopia (colecistectomia laparoscópica, apendicectomia, reparação de hérnia). Para gestores, é uma especialidade de alto volume cirúrgico e crescente demanda por procedimentos minimamente invasivos.",
    [
        ("Escopo e diferenciação em cirurgia geral",
         "Cirurgia geral abrange: colecistectomia laparoscópica (vesícula — o procedimento laparoscópico mais realizado no mundo), herniorrafia (reparo de hérnias inguinais, umbilicais, ventrais — com e sem tela), apendicectomia, cirurgia do aparelho digestivo (gastrectomias, colectomias), cirurgia de mama (diagnóstica e oncológica), cirurgia da tireoide e paratireoide, e proctologia (para cirurgiões gerais com interesse em coloproctologia). O portfólio diversificado é a força da especialidade — o cirurgião geral raramente fica sem agenda."),
        ("Videolaparoscopia: o pilar técnico moderno",
         "Videolaparoscopia (cirurgia minimamente invasiva via câmera e instrumentos por pequenas incisões) revolucionou a cirurgia geral — colecistectomia laparoscópica tem alta em menos de 24 horas vs. 3 a 5 dias na cirurgia aberta. Cirurgiões gerais que dominam a videolaparoscopia avançada (colectomia laparoscópica, fundoplicatura, gastrectomia laparoscópica) têm diferencial técnico significativo. Robótica (Da Vinci) adiciona mais uma camada de diferenciação técnica para hospitais de referência."),
        ("Ambulatório cirúrgico: fonte de receita e independência",
         "Clínica de cirurgia geral com ambulatório cirúrgico próprio — sala cirúrgica para procedimentos sob anestesia local ou sedação leve (pequenas herniorrafias, lipomas, cistos sebáceos, pequenos procedimentos de parede abdominal) — aumenta a autonomia e a receita sem depender de agenda hospitalar. O investimento em sala cirúrgica ambulatorial (R$ 200.000 a R$ 500.000) é recuperado em 12 a 24 meses em uma clínica com volume adequado. A conveniência para o paciente (sem internação, custo menor) também é um diferencial competitivo."),
        ("Faturamento em cirurgia geral",
         "Colecistectomia laparoscópica é o procedimento mais comum e remunerado em cirurgia geral — código TUSS bem estabelecido, mas negociação de valor com convênios varia muito. Herniorrafia com tela tem cobrança diferenciada quando o material (tela) é cobrado separadamente como OPME. Cirurgias oncológicas (gastrectomia, colectomia, tireoidectomia) têm remuneração mais alta e frequentemente incluem equipe de auxiliares com seus próprios honorários. Procedimentos ambulatoriais têm fluxo de caixa mais rápido e previsível do que cirurgias hospitalares."),
        ("Marketing para cirurgiões gerais",
         "Médicos encaminhadores são o canal principal — clínicos gerais, gastroenterologistas, endocrinologistas (tireoide) e oncologistas encaminham cirurgias. Relação próxima com pronto-socorros e UPAs para referência de cirurgias de urgência (apendicite, abdômen agudo) é um fluxo complementar importante. Para pacientes diretos, Google com busca local por hérnias, vesícula e cirurgias abdominais tem alto volume. Conteúdo educativo sobre quando operar hérnias, recuperação de colecistectomia e cirurgia da tireoide tem boa tração em plataformas digitais."),
    ],
    [
        ("Toda hérnia precisa de cirurgia?",
         "Nem toda hérnia precisa de cirurgia imediata. Hérnias assintomáticas (sem dor, sem complicação) em idosos com alto risco cirúrgico podem ser observadas. Hérnias encarceradas (conteúdo preso mas com circulação preservada) ou estranguladas (sem circulação — emergência) precisam de cirurgia imediata. Para a maioria dos adultos saudáveis com hérnia sintomática, a cirurgia eletiva é recomendada antes de complicações. Hérnias inguinais tendem a aumentar ao longo do tempo — operar eletivamente tem menor risco do que esperar uma emergência."),
        ("Colecistectomia laparoscópica tem muitas complicações?",
         "Colecistectomia laparoscópica é uma das cirurgias com melhor perfil de segurança — taxa de complicações maiores abaixo de 1% em centros experientes. A complicação mais temida é a lesão de via biliar (corte acidental do ducto biliar comum), que ocorre em menos de 0,5% dos casos com técnica adequada. Alta hospitalar em 24 horas, retorno às atividades em 7 a 14 dias e cicatrizes mínimas (3 a 4 pequenos orifícios) tornam o procedimento muito bem aceito pelos pacientes."),
        ("Cirurgia robótica vale o custo no Brasil?",
         "Cirurgia robótica (sistema Da Vinci) oferece visualização 3D de alta definição e instrumentos articulados que superam a videolaparoscopia convencional em precisão — especialmente útil em cirurgias de espaços confinados (pelve, mediastino). O custo é significativamente superior ao laparoscópico — consommables por cirurgia de R$ 3.000 a R$ 8.000, mais o investimento em equipamento (R$ 7 a R$ 15 milhões) ou locação hospitalar. No Brasil, poucos hospitais têm o sistema e poucos convênios cobrem o diferencial de custo. Para centros de referência em cirurgia oncológica e urológica, vale o investimento."),
    ]
)

# ── Article 4969 ── SaaS Sales: hotéis e pousadas
art(
    "vendas-para-o-setor-de-saas-de-hoteis-e-pousadas",
    "Vendas para o Setor de SaaS de Hotéis e Pousadas | ProdutoVivo",
    "Como vender SaaS para hotéis, pousadas e meios de hospedagem no Brasil. Estratégias de prospecção, demonstração de ROI e fechamento.",
    "Como Vender SaaS para Hotéis e Pousadas",
    "O setor de hospedagem brasileiro tem mais de 30.000 meios de hospedagem registrados — hotéis urbanos, pousadas, resorts, flats e apart-hotéis. Property Management System (PMS), channel manager, motor de reservas e gestão de revenue são SaaS fundamentais que muitos estabelecimentos ainda operam de forma manual ou com sistemas desatualizados. É um mercado com compradores acessíveis e dor operacional claramente definida.",
    [
        ("O stack de SaaS essencial para meios de hospedagem",
         "PMS (Property Management System) é o sistema central — gestão de reservas, check-in/check-out, ocupação de quartos, faturamento e relatórios operacionais. Channel Manager sincroniza a disponibilidade e tarifas em tempo real com as OTAs (Booking.com, Expedia, Airbnb) — evita overbooking e trabalho manual de atualização. Motor de reservas próprio no site permite reservas diretas sem comissão de OTA. Revenue Management System analisa demanda e sugere a tarifa ideal por data. A maioria das pousadas pequenas usa só o PMS; hotéis maiores usam o stack completo."),
        ("O decisor no setor de hospedagem",
         "Dono ou gerente geral decide em pousadas e hotéis pequenos (até 50 quartos). Em hotéis de rede, há gerente de reservas e diretor de operações como compradores técnicos, e diretor geral ou financeiro como aprovador. Dono de pousada é frequentemente um empreendedor que foi hóspede apaixonado pelo negócio — não tem background técnico mas entende de hospitalidade. Conecte o SaaS ao que importa para ele: mais reservas diretas (sem pagar comissão de OTA), operação mais eficiente e hóspedes mais satisfeitos."),
        ("Como demonstrar um PMS para hospedagem",
         "Demo começa pelo fluxo completo de reserva: nova reserva no Booking.com → aparece automaticamente no PMS → quarto bloqueado no channel manager → recibo automático por email para o hóspede → check-in no dia (confirmação de identidade, chave) → lançamento de consumos durante a estadia → check-out com geração automática da fatura → NF-e emitida. Mostre o painel de ocupação com calendário visual — o dono de pousada entende instantaneamente a utilidade de ver todos os quartos e reservas em uma tela."),
        ("Objeções no setor de hospedagem",
         "'Já uso planilha do Excel' — mostre o risco de overbooking e o tempo que leva atualizar manualmente 5 OTAs. 'Sistema caro' — calcule o custo de uma comissão de OTA (15 a 25%) vs. o custo do motor de reservas próprio por 1 ano. 'Difícil de aprender' — ofereça treinamento incluído e suporte por WhatsApp. 'Tenho um sistema mais barato' — compare funcionalidades, especialmente integração com OTAs e channel manager. Pousadas que migram para um PMS moderno relatam 20 a 40% de aumento em reservas diretas em 12 meses."),
        ("Expansão em clientes de hospedagem",
         "PMS é o módulo central que abre a porta para: channel manager integrado (expansão natural se a pousada ainda gerencia OTAs manualmente), motor de reservas no site (para aumentar reservas diretas), CRM de hóspedes (histórico, preferências, campanha de retorno), gestão de F&B (restaurante e bar do hotel), e controle financeiro integrado. Hotéis que digitalizam toda a operação — da reserva à saída — têm NPS altíssimo e não trocam de sistema. O LTV de um hotel como cliente é de 5 a 10 anos com expansão de módulos."),
    ],
    [
        ("Channel manager é obrigatório para pousadas?",
         "Para pousadas que anunciam em mais de uma OTA simultaneamente (Booking.com + Airbnb + Expedia), channel manager é praticamente obrigatório — sem ele, o risco de overbooking é alto e a atualização manual de disponibilidade e tarifas consome horas por dia. Para pousadas que usam apenas uma OTA ou têm lotação quase sempre máxima por indicação, o channel manager tem menos urgência. A regra prática: se você perde tempo atualizando tarifas e disponibilidade manualmente em múltiplos canais, o channel manager paga em semanas."),
        ("OTA vs. reserva direta: qual é mais vantajosa para o hotel?",
         "Reserva direta (pelo site ou telefone, sem OTA) é sempre mais vantajosa financeiramente — sem comissão de 15 a 25% para a plataforma. Mas OTAs trazem demanda incremental que o hotel não conseguiria capturar sozinho — especialmente de turistas internacionais e viajantes que descobrem o hotel pela plataforma. A estratégia ideal é usar OTAs como canal de descoberta (aceitar preço de paridade) e investir em converter hóspedes OTA em clientes diretos para a próxima estadia — via e-mail de follow-up, programa de fidelidade e benefícios exclusivos em reserva direta."),
        ("Revenue management é para hotéis grandes apenas?",
         "Revenue management — ajustar tarifas dinamicamente com base em demanda, ocupação e eventos locais — é praticado manualmente por qualquer proprietário de pousada que cobra mais no Carnaval e nas férias de julho. SaaS de revenue management automatiza e otimiza esse processo com dados históricos e modelos preditivos. Para pousadas pequenas, a versão simplificada (regras de tarifa por ocupação e sazonalidade no PMS) já gera resultado. Para hotéis de médio e grande porte, um RMS dedicado pode aumentar a receita por quarto disponível (RevPAR) em 10 a 20%."),
    ]
)

# ── Article 4970 ── Consulting: varejo e transformação do retail
art(
    "consultoria-de-varejo-e-transformacao-do-retail",
    "Consultoria de Varejo e Transformação do Retail | ProdutoVivo",
    "Como estruturar e vender consultoria de varejo e transformação do retail. Guia para consultores que atuam em estratégia, operações e omnichannel.",
    "Consultoria de Varejo e Transformação do Retail: Como Construir uma Prática Especializada",
    "Varejo é um dos setores mais dinâmicos e desafiadores para consultoria — digitalização acelerada, consumidor omnichannel, competição com marketplaces e pressão de margem são desafios simultâneos que varejistas de todos os portes enfrentam. Consultores com experiência em estratégia de varejo, operações de loja, e-commerce e trade marketing têm demanda crescente de redes regionais a grupos nacionais.",
    [
        ("O escopo da consultoria de varejo",
         "Consultoria de varejo abrange: estratégia de canal (omnichannel, physical e digital integration), operações de loja (produtividade de vendedores, gestão de estoque na loja, visual merchandising), e-commerce e marketplace (estratégia de canais digitais, gestão de mídia paga no varejo), pricing e promoções (estratégia de precificação competitiva, calendário promocional), supply chain de varejo (gestão de estoque, reposição, gestão de fornecedores), e análise de dados de varejo (vendas por loja, sell-through, curva ABC de produtos)."),
        ("Varejo omnichannel: a transformação central do setor",
         "O consumidor moderno pesquisa online e compra na loja, ou compra online e retira na loja, ou devolve online o que comprou offline. Varejistas que não integram esses canais perdem vendas e satisfação do cliente. Projetos de consultoria omnichannel incluem: integração de estoque único para online e offline (ship from store), click-and-collect operacional, integração de programas de fidelidade entre canais, pricing consistente entre canais, e experiência de cliente unificada (histórico de compras disponível em qualquer ponto de contato)."),
        ("Métricas de varejo: o vocabulário do consultor",
         "Ticket médio, conversão de loja (% de visitantes que compram), vendas por metro quadrado, giro de estoque, GMROI (retorno sobre o investimento de estoque), sell-through (% do estoque vendido no período), shrinkage (perda de inventário por furto e erros), NPS de loja e e-commerce, custo de aquisição de cliente digital e LTV são as métricas centrais do varejo. Consultores que chegam com essas métricas calculadas para o cliente na primeira reunião demonstram expertise instantaneamente."),
        ("Varejo alimentar vs. varejo de moda vs. varejo de eletro: diferenças para o consultor",
         "Cada segmento de varejo tem dinâmicas distintas. Varejo alimentar: alta frequência, margens baixas, gestão rigorosa de validade e frescor, competição com price. Varejo de moda: sazonalidade intensa, gestão de coleções, sell-through crítico para evitar liquidação, curadoria de produtos diferencia mais do que preço. Varejo de eletro/eletrônicos: ticket alto, competição intensa com e-commerce, financiamento é parte central da proposta de valor. Consultor especializado em um dos três tem profundidade superior ao generalista."),
        ("Captação de clientes para consultoria de varejo",
         "Diretores de operações, CDOs (Chief Digital Officers) e CEOs de redes varejistas regionais são os compradores-alvo. ABEVAR (Associação Brasileira de Empresas de Varejo), ABComm (e-commerce), NRF (National Retail Federation — evento global com comunidade brasileira ativa) e eventos de varejo como Latam Retail Show são espaços de networking premium. Publicação de estudos de benchmark de varejo (conversion rates por categoria, custos de e-commerce por segmento) são iscas de lead de alta qualidade."),
    ],
    [
        ("Ship from store funciona para varejistas pequenos?",
         "Ship from store (usar o estoque da loja física para fulfillment de pedidos online) funciona melhor para redes com múltiplas lojas que têm estoque disperso geograficamente — permite entregas mais rápidas e reduz custos de frete. Para varejistas com uma ou duas lojas, o benefício é menor e a operação adiciona complexidade ao dia a dia da equipe de loja. A implementação exige integração de sistemas (OMS, WMS de loja, ERP) e treinamento intensivo da equipe. Para redes regionais com mais de 10 lojas, o ROI em redução de frete e aumento de conversão geralmente justifica o projeto."),
        ("Como varejistas pequenos competem com marketplaces?",
         "Varejistas pequenos que tentam competir com Mercado Livre e Amazon em preço puro perdem sempre — os marketplaces têm escala, logística e poder de negociação superiores. A estratégia vencedora é diferenciação: especialização em uma categoria onde o varejista tem expertise superior (consultores especialistas que o marketplace não tem), experiência de loja excepcional (atendimento, ambiente, conveniência local), produtos exclusivos ou marcas não disponíveis nos marketplaces, e comunidade de clientes fidelizados. Nicho + experiência superior + relacionamento vencem commodity + preço."),
        ("Qual o maior erro de varejistas na digitalização?",
         "O maior erro é digitalizar processos sem integrar canais — criar um e-commerce separado da loja física, com estoques diferentes, preços diferentes, promoções diferentes e histórico de cliente separado. O cliente percebe a desconexão como falta de profissionalismo e incoerência de marca. Digitalização bem feita começa pela integração de dados (estoque único, cadastro único de cliente, programa de fidelidade unificado) e depois adiciona os canais digitais sobre essa base integrada. A ordem importa: dados primeiro, canais depois."),
    ]
)

# ── Article 4971 ── B2B SaaS: helpdesk e suporte de TI
art(
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-helpdesk-e-suporte-de-ti",
    "Gestão de Negócios de Empresa de B2B SaaS de Helpdesk e Suporte de TI | ProdutoVivo",
    "Como construir e escalar um B2B SaaS de helpdesk e suporte de TI. Estratégias de produto, precificação e go-to-market para o mercado de ITSM.",
    "Como Escalar um B2B SaaS de Helpdesk e Suporte de TI",
    "Helpdesk e ITSM (IT Service Management) é um dos segmentos de SaaS B2B mais maduros — toda empresa com equipe de TI ou suporte ao cliente precisa de um sistema para gerenciar chamados, SLAs e base de conhecimento. Zendesk, ServiceNow e Freshdesk dominam o enterprise, mas há espaço enorme para SaaS brasileiros no mercado de PMEs que precisam de funcionalidade sólida com preço em reais e suporte local.",
    [
        ("O problema que helpdesk SaaS resolve",
         "Sem helpdesk dedicado, solicitações chegam por e-mail, WhatsApp, telefone e Teams simultaneamente — nada tem prioridade, nada é rastreado, nada tem SLA. Tickets somem no inbox lotado do técnico. O gestor não sabe quantos chamados estão abertos, qual o tempo médio de resolução nem quais problemas são mais frequentes. Helpdesk resolve: canal único de entrada (com captura automática de qualquer canal), triagem e priorização por tipo e urgência, distribuição para o técnico certo, SLA com alertas de vencimento, e base de conhecimento para autoatendimento."),
        ("ITSM além do básico: ITIL e gestão de serviços",
         "ITIL (Information Technology Infrastructure Library) é o framework de melhores práticas de ITSM — define processos como gestão de incidentes, problemas, mudanças e ativos de TI. SaaS de ITSM que implementa processos ITIL — gestão de mudanças com CAB (Change Advisory Board), gestão de problemas (root cause analysis), CMDB (Configuration Management Database de ativos) — atende o mercado enterprise e médio que precisa de compliance e governança de TI. É a camada de diferenciação que justifica ticket 3x maior do que helpdesk básico."),
        ("Segmentação: helpdesk de TI vs. helpdesk de atendimento ao cliente",
         "Helpdesk de TI (ITSM) serve equipes internas de TI gerenciando chamados de funcionários — problemas com computador, acesso a sistemas, solicitações de software. Helpdesk de atendimento ao cliente (CX) serve equipes de suporte gerenciando chamados de clientes — reclamações, dúvidas, solicitações pós-venda. Os dois mercados têm sobreposição de funcionalidades mas personas distintas. Zendesk domina o CX; ServiceNow domina o ITSM enterprise. Para SaaS brasileiro, especializar em um dos dois é mais eficiente do que tentar cobrir ambos."),
        ("Precificação de SaaS de helpdesk",
         "Por agente (técnico/atendente) é o modelo dominante em helpdesk — Zendesk, Freshdesk, Jira Service Management cobram por usuário administrador. Modelo por volume de tickets (R$ X por ticket resolvido) é alternativa para equipes pequenas com volume variável. Para ITSM enterprise, mensalidade por módulo com implementação cobrada separadamente é comum. PMEs brasileiras pagam R$ 50 a R$ 200 por agente por mês. Plano gratuito com até 5 agentes é estratégia de entrada eficaz para capturar startups que crescem para clientes pagantes."),
        ("Go-to-market para SaaS de helpdesk",
         "PLG com trial gratuito é o modelo dominante — a maioria dos compradores quer testar antes de comprar. Google Ads para termos de busca de problema ('sistema de chamados de TI', 'helpdesk grátis', 'software de suporte') captura demanda ativa com alta intenção de compra. Conteúdo sobre ITIL, SLA, gestão de chamados e melhores práticas de suporte gera tráfego orgânico qualificado. Parcerias com MSPs (Managed Service Providers) que gerenciam TI de PMEs são canais de distribuição de altíssimo valor — o MSP implanta o helpdesk para todos os seus clientes."),
    ],
    [
        ("Helpdesk e CRM são ferramentas diferentes?",
         "Helpdesk gerencia suporte pós-venda — tickets abertos por clientes ou usuários, resolução de problemas, SLAs de atendimento. CRM gerencia relacionamento comercial — leads, oportunidades, histórico de negociações. As ferramentas têm visões complementares do cliente: CRM tem o histórico de compras e contratos; helpdesk tem o histórico de suporte e satisfação. Integração entre os dois — o agente de suporte vê o histórico comercial do cliente ao abrir um ticket — é a experiência ideal. Zendesk e Salesforce têm integração nativa; para SaaS menores, Zapier/Make conectam os dois."),
        ("SLA em helpdesk: como configurar corretamente?",
         "SLA (Service Level Agreement) em helpdesk define o tempo máximo para primeira resposta e para resolução de cada ticket, por prioridade. Exemplo: crítico (serviço fora) — resposta em 1h, resolução em 4h; alto — resposta em 4h, resolução em 1 dia útil; médio — resposta em 1 dia, resolução em 3 dias. O sistema monitora automaticamente e alerta o técnico e o gestor quando o prazo está próximo de vencer. SLA configurado corretamente e seguido rigorosamente é o principal indicador de qualidade de um time de suporte."),
        ("Base de conhecimento reduz chamados de suporte?",
         "Sim, significativamente. Base de conhecimento (KB) bem construída com artigos de FAQ, tutoriais e guias de resolução de problemas comuns pode reduzir o volume de chamados em 20 a 40%. O mecanismo é o autoatendimento — o usuário encontra a resposta no KB antes de abrir um ticket. Ferramentas de helpdesk modernas mostram artigos sugeridos automaticamente quando o usuário começa a descrever o problema. KB é o investimento de longo prazo que mais reduz o custo por ticket — cada artigo criado atende dezenas ou centenas de usuários sem esforço adicional."),
    ]
)

# ── Article 4972 ── Clinics: neonatologia e medicina neonatal
art(
    "gestao-de-clinicas-de-neonatologia-e-medicina-neonatal",
    "Gestão de Clínicas de Neonatologia e Medicina Neonatal | ProdutoVivo",
    "Guia de gestão para serviços de neonatologia e medicina neonatal: estrutura de UTI neonatal, faturamento e estratégias de excelência assistencial.",
    "Gestão de Serviços de Neonatologia e Medicina Neonatal: Guia Completo",
    "Neonatologia é a especialidade pediátrica dedicada ao recém-nascido — especialmente os prematuros e neonatos com doenças graves. Unidades de Terapia Intensiva Neonatal (UTINs) são serviços de alta complexidade que exigem gestão especializada, equipe multiprofissional treinada e infraestrutura de ponta. Para gestores hospitalares e médicos neonatologistas que gerenciam serviços, compreender a complexidade operacional e assistencial é fundamental.",
    [
        ("Estrutura de uma UTIN e serviço de neonatologia",
         "Serviços de neonatologia são estratificados por nível de complexidade: Nível I (berçário de cuidados mínimos para RN saudáveis a termo), Nível II (cuidados intermediários para RN moderadamente prematuros e enfermos), e Nível III (UTIN para RN extremamente prematuros e criticamente doentes). UTIN Nível III exige: neonatologistas 24 horas, enfermeiros especializados em neonatologia, fisioterapeutas respiratórios, nutricionistas para suporte nutricional neonatal, fonoaudiólogas para aleitamento, e tecnologia avançada (ventiladores de alta frequência, monitorização contínua, ecógrafo beira de leito)."),
        ("Gestão de qualidade em neonatologia: indicadores e benchmarks",
         "Indicadores de qualidade neonatal são rigorosamente monitorados: taxa de mortalidade neonatal por faixa de peso (ajustada por risco), taxa de infecção primária de corrente sanguínea associada a cateter (IPCS-CVC — meta: abaixo de 1/1000 dias cateter), uso de corticosteróide antenatal em prematuros (meta acima de 90%), taxa de aleitamento materno exclusivo na alta, e taxa de retinopatia da prematuridade em RN de muito baixo peso. Participação em redes de benchmarking neonatal (Vermont Oxford Network, Rede Brasileira de Pesquisas Neonatais) permite comparar indicadores com centros de excelência."),
        ("Cuidado centrado na família: o padrão moderno de UTIN",
         "Cuidado centrado na família (CCF) em UTIN é o modelo que inclui os pais como parceiros ativos no cuidado do recém-nascido — não apenas visitantes. Inclui: acesso irrestrito dos pais 24 horas, método canguru (contato pele a pele entre bebê e pai/mãe), participação dos pais nos cuidados diários (troca de fralda, banho, alimentação), reuniões de evolução com a família, e apoio psicossocial. CCF melhora os resultados clínicos do bebê e a experiência da família — e diferencia o serviço de neonatologia no mercado."),
        ("Faturamento em serviços de neonatologia",
         "UTINs são serviços de alto custo e alto faturamento — o custo diário de uma diária de UTIN Nível III com ventilação mecânica é de R$ 3.000 a R$ 8.000 pelos convênios. O faturamento correto exige: codificação precisa da diária pelo nível de complexidade (UTI III vs. UCINCo vs. UCINCa), registro de todos os procedimentos realizados (punções venosas, intubações, instalações de cateter, transfusões), faturamento de materiais de alto custo (surfactante, CPAP, monitores específicos), e revisão de contas para evitar glosas. Um dia de UTIN mal faturado pode representar R$ 1.000 a R$ 3.000 de perda."),
        ("Captação e referência em neonatologia",
         "Neonatologia não capta pacientes diretamente — neonatos doentes chegam via maternidade do hospital ou transferidos de outras unidades. Gestores de UTINs precisam: (1) garantir que a maternidade do próprio hospital encaminha todos os prematuros e RN enfermos para a UTIN (integração com obstetrícia); (2) posicionar a UTIN como referência regional para receber transferências de hospitais sem UTIN; (3) construir relacionamento com obstetras e perinatologistas de toda a região que sabem, com antecedência, que vão precisar de UTIN para gestações de risco."),
    ],
    [
        ("Qual o menor prematuro que pode sobreviver?",
         "Com os avanços em medicina neonatal, bebês prematuros a partir de 22 a 23 semanas de gestação podem sobreviver em centros de excelência, embora com taxas de sobrevivência muito baixas e alto risco de sequelas. A viabilidade prática começa em torno de 24 a 25 semanas. A partir de 28 semanas, a taxa de sobrevivência supera 90% em centros especializados. A qualidade do cuidado neonatal intensivo — técnica de ventilação, nutrição parenteral, controle de infecção, cuidado centrado na família — é o determinante mais importante dos resultados além da idade gestacional."),
        ("Surfactante é um tratamento recente?",
         "Surfactante exógeno para tratamento da síndrome do desconforto respiratório (SDR) do prematuro foi introduzido na prática clínica nos anos 1990 e representa um dos maiores avanços em neonatologia — reduziu dramaticamente a mortalidade neonatal por SDR. Surfactante é uma substância lipoproteica que reveste os alvéolos pulmonares e evita seu colapso — prematuros não produzem suficiente, causando dificuldade respiratória grave. A administração de surfactante artificial (poractant alfa, beractant) combinada com ventilação não invasiva (CPAP/NHFV) é o padrão de cuidado atual."),
        ("O que é retinopatia da prematuridade e como prevenir?",
         "Retinopatia da prematuridade (ROP) é uma doença da retina que afeta prematuros de muito baixo peso, causada pelo crescimento anormal de vasos sanguíneos na retina imatura. Pode levar à cegueira se não tratada. A prevenção começa no controle rigoroso da saturação de oxigênio na UTIN (evitar hiperóxia). Todo prematuro abaixo de 1500g ou abaixo de 32 semanas deve ser rastreado por oftalmologista com experiência em ROP a partir da 4ª semana de vida. Laser e anti-VEGF intravítreo são os tratamentos disponíveis para casos avançados."),
    ]
)

# ── Article 4973 ── SaaS Sales: autopeças e oficinas mecânicas
art(
    "vendas-para-o-setor-de-saas-de-autopecas-e-oficinas-mecanicas",
    "Vendas para o Setor de SaaS de Autopeças e Oficinas Mecânicas | ProdutoVivo",
    "Como vender SaaS para autopeças e oficinas mecânicas no Brasil. Estratégias de prospecção, demonstração de ROI e fechamento no setor automotivo.",
    "Como Vender SaaS para Autopeças e Oficinas Mecânicas",
    "O setor automotivo de pós-venda no Brasil é imenso — mais de 100.000 oficinas mecânicas e 50.000 lojas de autopeças formam um mercado em grande parte ainda analógico. Ordens de serviço no papel, estoque de peças em cadernos, precificação de mão de obra por memória e fluxo de caixa gerenciado em planilhas são a realidade de muitas oficinas. SaaS que resolve esses problemas enfrenta um mercado com compradores práticos e ROI imediato.",
    [
        ("O perfil do dono de oficina mecânica",
         "Dono de oficina mecânica no Brasil é tipicamente um ex-mecânico que virou empreendedor por competência técnica — entende de carro mas raramente tem formação em gestão. Compra por dor concreta: 'não sei o que tenho em estoque', 'mecânico faz o serviço e eu não sei cobrar', 'cliente vem reclamar que cobrei errado'. Avessa a sistemas complexos que atrapalham o trabalho diário. A demonstração precisa ser simples, prática e mostrar que o sistema não é mais complicado do que o problema que resolve."),
        ("Os SaaS mais procurados por oficinas",
         "Gestão de ordens de serviço (OS) com registro de diagnóstico, peças utilizadas e mão de obra é o produto central. Controle de estoque de peças (PEPS, reposição automática, consulta de preço de tabela). Histórico de veículos por placa/chassi (fundamental para relacionamento com cliente recorrente). Gestão financeira básica (contas a pagar e receber, fluxo de caixa). Emissor de NF-e de serviços. CRM de clientes com agendamento de revisões preventivas. Cada módulo é vendável como pacote ou individually."),
        ("Como fazer demo para oficinas e autopeças",
         "Demonstrate com o fluxo real do dia: cliente chega, cria OS pelo celular ou tablet na bancada com o mecânico, lista os serviços e peças, imprime a OS aprovada pelo cliente, ao terminar fecha a OS com os valores finais e emite a NF-e. Mostre a busca de placa que preenche automaticamente o histórico do veículo. Mostre o alerta de estoque baixo de filtro de óleo — peça mais girada em qualquer oficina. A praticidade do mobile (sem papel, sem planilha) é o ponto de impacto central da demo."),
        ("Autopeças: necessidades específicas",
         "Loja de autopeças tem necessidades adicionais às oficinas: catálogo de peças com referência cruzada (peça de montadora vs. paralela vs. importada), precificação por lista de preço com margem configurável, gestão de pedidos para fornecedores/distribuidores, controle de estoque por código de peça com múltiplas unidades de medida, e gestão de crédito para mecânicos e clientes frequentes que compram a prazo. Integração com catálogos de referência online (Tec Ally, TecDoc) é o diferencial para autopeças maiores."),
        ("Prospecção em oficinas e autopeças",
         "Visita pessoal é o canal mais eficaz — oficinas raramente procuram software ativamente. Um vendedor que vai à oficina, faz uma demo no tablet em 15 minutos e resolve um problema real fecha mais do que qualquer campanha digital. Associações do setor (Sindirepa — Sindicato Nacional da Indústria de Reparação de Veículos, FENABRAVE para concessionárias, distribuidoras de autopeças como Genuine Parts/NAPA) são canais de acesso ao setor. WhatsApp Business com vídeos curtos de demo de 2 a 3 minutos converteu bem para este perfil de comprador."),
    ],
    [
        ("NF-e de serviços em oficinas mecânicas: é obrigatória?",
         "Emissão de NFS-e (Nota Fiscal de Serviços Eletrônica) é obrigatória para oficinas mecânicas prestadoras de serviço, conforme legislação municipal (cada município tem seu sistema). Para venda de peças, NF-e de produto (modelo 55) é obrigatória acima dos limites de MEI. Oficinas que vendem serviço + peça emitem documentos separados ou NF-e conjugada dependendo da UF. Muitas oficinas informais ainda não emitem NF-e regularmente — SaaS que facilita a emissão por QR code e integração com a prefeitura local é um argumento de regularização fiscal que ressoa com quem quer crescer."),
        ("Gestão de garantia em oficinas: como funciona?",
         "Oficinas são obrigadas por lei (CDC) a oferecer garantia de 90 dias nos serviços prestados e nas peças instaladas. Controlar qual serviço foi feito em qual veículo, com quais peças e por qual mecânico é essencial para gestão de garantia — sem esse histórico, a oficina não consegue verificar se a reclamação é procedente. SaaS com histórico completo por veículo (placa + chassi) e OS detalhada permite resolver reclamações de garantia em segundos, aumentando a satisfação do cliente e reduzindo conflitos."),
        ("Quanto custa um SaaS para oficina mecânica?",
         "Sistemas de gestão para oficinas mecânicas no Brasil variam de R$ 100 a R$ 500 por mês para planos básicos a intermediários. Sistemas mais completos com módulo de NF-e, integração com catálogo de peças e múltiplos usuários chegam a R$ 800 a R$ 1.500/mês. Para o perfil de oficina de médio porte (3 a 10 mecânicos, R$ 50.000 a R$ 200.000 de faturamento mensal), um sistema de gestão bem utilizado recupera seu custo em redução de cobranças incorretas e controle de estoque em poucos meses."),
    ]
)

# ── Article 4974 ── Consulting: imobiliário e real estate
art(
    "consultoria-de-imobiliario-e-real-estate",
    "Consultoria de Imobiliário e Real Estate | ProdutoVivo",
    "Como estruturar e vender consultoria imobiliária e de real estate. Guia para consultores que atuam em desenvolvimento imobiliário, FIIs e mercado de capitais imobiliário.",
    "Consultoria Imobiliária e de Real Estate: Como Construir uma Prática de Alto Valor",
    "O mercado imobiliário brasileiro movimenta mais de R$ 200 bilhões por ano em lançamentos e transações. Desenvolvimento imobiliário, análise de viabilidade, gestão de portfólio de imóveis corporativos e assessoria em FIIs (Fundos de Investimento Imobiliário) são nichos de consultoria de alto ticket que combinam conhecimento jurídico, financeiro e de mercado. É um setor cíclico mas com demanda estrutural permanente.",
    [
        ("O escopo da consultoria imobiliária",
         "Consultoria de real estate abrange: análise de viabilidade de incorporação imobiliária (estudo de VGV, custos de construção, análise de mercado local, TIR do empreendimento), assessoria em M&A imobiliário (aquisição e venda de carteiras de imóveis, due diligence), gestão de portfólio de imóveis corporativos (otimização de ocupação, renegociação de contratos de locação, sale-leaseback), estruturação de FIIs (Fundos de Investimento Imobiliário) e CRIs, e consultoria de placemaking e desenvolvimento urbano."),
        ("Análise de viabilidade: a porta de entrada do desenvolvimento",
         "Incorporadoras compram terrenos e desenvolvem empreendimentos baseados em análise de viabilidade — VGV (Valor Geral de Vendas) projetado, custo de construção (CUB + BDI), custo do terreno, despesas de lançamento e comercialização, e TIR esperada do projeto. Consultores que fazem análise de viabilidade com rigor financeiro e conhecimento de mercado local (pesquisa de velocidade de vendas, preço por m² na região, demanda de perfil de produto) têm demanda consistente de incorporadoras regionais e investidores imobiliários. Honorários: R$ 30.000 a R$ 200.000 por análise."),
        ("FIIs: consultoria no mercado imobiliário de capitais",
         "FIIs (Fundos de Investimento Imobiliário) são veículos de investimento coletivo em imóveis — do FII de shopping center ao FII de galpões logísticos. Consultores de FIIs assessoram: estruturação de novos fundos (definição de estratégia, regulamento, seleção de ativos), análise de portfólio de FIIs existentes para gestoras, due diligence de ativos imobiliários para FIIs, e consultoria de fusões e aquisições entre FIIs. Com mais de 400 FIIs listados na B3 e crescimento acelerado de FIIs de tijolo e papel, é um nicho de consultoria financeiro-imobiliária de alto valor."),
        ("Sale-leaseback corporativo: oportunidade de consultoria",
         "Sale-leaseback é a operação em que uma empresa vende seu imóvel corporativo para um investidor (ou FII) e permanece como inquilina com contrato de longo prazo. É uma forma de liberar capital imobilizado no imóvel para reinvestir no negócio. Consultores que estruturam sale-leasebacks trabalham com empresas que possuem imóveis próprios mas preferem capital de giro a patrimônio imobilizado — especialmente interessante em períodos de juros elevados quando o custo de capital é alto. Honorários: 1 a 2% do valor da transação."),
        ("Captação de clientes para consultoria imobiliária",
         "Incorporadoras regionais, family offices com patrimônio imobiliário, gestoras de FIIs, fundos de private equity imobiliário e grandes corporações com portfólio de imóveis são os compradores-alvo. ABRAINC (Associação Brasileira de Incorporadoras Imobiliárias), ABECIP, SECOVI e eventos como REALMATCH e o Congresso Internacional do Mercado Imobiliário são espaços de networking premium. Publicação de análises de mercado imobiliário por cidade e segmento (residencial, logístico, corporativo) são iscas de lead de alta qualidade para gestores e incorporadores."),
    ],
    [
        ("VGV é o principal indicador de um lançamento imobiliário?",
         "VGV (Valor Geral de Vendas) é o faturamento total do empreendimento se todas as unidades forem vendidas pelo preço de tabela — é o indicador de tamanho do projeto. Mas não é o indicador de rentabilidade. O que importa para o incorporador é a margem líquida (VGV menos todos os custos) e a TIR (Taxa Interna de Retorno) do investimento. Um VGV alto com margem baixa é pior do que um VGV menor com margem alta. Análise de viabilidade séria sempre calcula TIR, payback e ponto de equilíbrio de vendas — não só o VGV."),
        ("FII de papel vs. FII de tijolo: qual a diferença?",
         "FII de tijolo investe diretamente em imóveis físicos — shoppings, galpões logísticos, escritórios, hospitais, hotéis — e recebe renda de aluguel. FII de papel investe em títulos de dívida imobiliária — CRIs (Certificados de Recebíveis Imobiliários) e LCIs (Letras de Crédito Imobiliário) — e recebe juros desses títulos. FIIs de tijolo têm renda mais previsível mas menor liquidez dos ativos subjacentes. FIIs de papel têm maior sensibilidade à taxa de juros (quando Selic sobe, o yield do papel sobe e o preço do FII cai). Ambos são isentos de IR para pessoas físicas nos dividendos."),
        ("Due diligence imobiliária: o que analisa?",
         "Due diligence imobiliária analisa: situação jurídica do imóvel (matrícula, ônus e gravames, regularidade de IPTU, ITR, débitos condominiais), situação ambiental (área de preservação permanente, passivo ambiental), situação urbanística (zoneamento, potencial construtivo, aprovações pendentes), vistoria técnica de edificações existentes (laudos de estrutura, elétrica, hidráulica), e análise de contratos de locação existentes (prazo, valor, índice, cláusulas de rescisão). Uma due diligence completa custa R$ 20.000 a R$ 100.000 dependendo da complexidade — e pode salvar transações de dezenas de milhões."),
    ]
)

# ── Sitemap + trilha update ──
import re

sitemap_path = pathlib.Path(__file__).parent / "sitemap.xml"
trilha_path  = pathlib.Path(__file__).parent / "trilha.html"

slugs = [
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-agendamento-e-reservas-online",
    "gestao-de-clinicas-de-cirurgia-geral-e-videolaparoscopia",
    "vendas-para-o-setor-de-saas-de-hoteis-e-pousadas",
    "consultoria-de-varejo-e-transformacao-do-retail",
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-helpdesk-e-suporte-de-ti",
    "gestao-de-clinicas-de-neonatologia-e-medicina-neonatal",
    "vendas-para-o-setor-de-saas-de-autopecas-e-oficinas-mecanicas",
    "consultoria-de-imobiliario-e-real-estate",
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

print("Done — batch 1742")
