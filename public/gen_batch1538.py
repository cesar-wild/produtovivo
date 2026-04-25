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

# Article 4559 — B2B SaaS: event management / venues
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-eventos-e-venues",
    title="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Eventos e Venues",
    desc="Como construir e escalar uma empresa de B2B SaaS de gestão de eventos e venues no Brasil: produto, go-to-market, diferenciais e estratégias de crescimento sustentável.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Gestão de Eventos e Venues",
    lead="O mercado de eventos no Brasil movimenta mais de R$200 bilhões anuais, com festivais, shows, congressos, feiras, casamentos, eventos corporativos e esportivos. A complexidade operacional de um evento — da venda de ingressos ao credenciamento, do controle de fornecedores ao relatório financeiro pós-evento — cria demanda crescente por SaaS especializados que integrem toda a cadeia de gestão.",
    sections=[
        ("Panorama do Mercado de Event Tech no Brasil", "O Brasil tem uma cultura de eventos vibrante: mais de 590.000 eventos são realizados por ano, segundo a ABEOC. A digitalização do setor acelerou com a pandemia — plataformas de eventos virtuais e híbridos se consolidaram — mas eventos presenciais retornaram com força e com expectativas digitais elevadas. Plataformas como Sympla, Eventbrite e Ingresse dominam a venda de ingressos, mas a gestão operacional completa (fornecedores, equipe, logística, financeiro) ainda é fragmentada, criando espaço para SaaS de gestão end-to-end."),
        ("Produto: Da Venda de Ingressos à Operação do Evento", "Um SaaS de gestão de eventos completo cobre: criação e publicação de eventos com página customizada, venda de ingressos (integração com gateway de pagamento, split automático para co-realizadores), gerenciamento de credenciamento (QR Code, pulseiras RFID, check-in digital), gestão de fornecedores e contratos (palco, som, iluminação, catering), gestão de equipe e voluntários, comunicação com participantes (e-mail, WhatsApp, push), e relatório financeiro pós-evento. Plataformas que cobrem mais elos da cadeia têm maior LTV."),
        ("Segmentação e Verticalização por Tipo de Evento", "O mercado de eventos é muito heterogêneo — gestão de um casamento é completamente diferente de gestão de um festival de música ou de um congresso médico. A estratégia mais eficaz é verticalização: criar funcionalidades específicas para um segmento (conferências acadêmicas, eventos esportivos amadores, casamentos, eventos corporativos) e dominar esse nicho antes de expandir. Funcionalidades como gestão de submissão de abstratos (congresso), controle de categorias de corrida (esportivo) ou coordenação de fornecedores de cerimonial (casamento) diferenciam frente a plataformas genéricas."),
        ("Go-to-Market e Canais de Aquisição", "Produtores de eventos são melhor adquiridos via: marketplaces de eventos (aparecendo como solução recomendada), conteúdo educativo em YouTube e Instagram sobre gestão de eventos, parcerias com escolas de produção cultural e eventos, e presença em feiras do setor (BIENAL DE EVENTOS, ABAV). O CAC pode ser reduzido com modelo freemium para eventos pequenos — gratuito até X ingressos — criando base de usuários que eventualmente converte para planos pagos conforme o produtor cresce."),
        ("Métricas de Saúde do Negócio e Retenção", "As métricas mais relevantes são: GMV (Gross Merchandise Volume — valor total de ingressos processados), take rate (percentual retido sobre ingressos, tipicamente 3-8%), ARR de assinaturas de planos de gestão, NPS de produtores e NPS de participantes. Retenção é um desafio: produtores de eventos não profissionais têm baixa recorrência. A estratégia para aumentar LTV é focar em produtores profissionais e agências de eventos — que realizam múltiplos eventos por ano e têm necessidade contínua da plataforma.")
    ],
    faq_list=[
        ("Qual a diferença entre plataforma de venda de ingressos e software de gestão de eventos?", "Plataformas de ingressos (Sympla, Ingresse, Eventbrite) focam em descoberta e compra pelo participante — são marketplaces com funcionalidades básicas de gestão para o produtor. Software de gestão de eventos tem foco no produtor: gestão operacional completa (fornecedores, equipe, logística, financeiro), credenciamento avançado, comunicação com participantes e relatórios pós-evento. Muitos produtores profissionais usam as duas — ticket em marketplace + gestão em software especializado."),
        ("O que é credenciamento RFID em eventos e quando faz sentido?", "Credenciamento RFID usa pulseiras ou crachás com chip de radiofrequência para check-in rápido e controle de acesso em zonas do evento. Faz sentido para eventos com mais de 1.000 participantes ou com múltiplas zonas de acesso (backstage, camarotes, etc.). Elimina filas no check-in (identificação em menos de 1 segundo vs. 5-10 segundos no QR Code), permite controle de lotação por área em tempo real e habilita cashless payment — participantes carregam crédito na pulseira para compras dentro do evento."),
        ("Como plataformas de gestão de eventos monetizam além da venda de ingressos?", "Os modelos de monetização incluem: taxa sobre ingressos (percentual ou valor fixo por ingresso), assinatura mensal/anual para acesso às funcionalidades de gestão (independente de ingressos), módulos premium (credenciamento RFID, app do evento, transmissão ao vivo), marketplace de fornecedores de eventos (comissão sobre contratações via plataforma), e programas de publicidade dentro da plataforma de descoberta. A combinação de transacional e recorrente é a mais saudável financeiramente.")
    ]
)

# Article 4560 — Clinic management: urology / urogynecology
art(
    slug="gestao-de-clinicas-de-urologia-e-uroginecologia",
    title="Gestão de Clínicas de Urologia e Uroginecologia",
    desc="Guia prático para gestão de clínicas de urologia e uroginecologia: estrutura clínica, procedimentos, faturamento, gestão de pacientes crônicos e estratégias de crescimento.",
    h1="Gestão de Clínicas de Urologia e Uroginecologia",
    lead="Clínicas de urologia e uroginecologia atendem uma ampla gama de condições — desde infecções urinárias de repetição e cálculos renais até câncer de próstata, incontinência urinária e disfunções do assoalho pélvico. A gestão dessas clínicas combina alta rotatividade de consultas com procedimentos ambulatoriais especializados, faturamento complexo por convênio e crescente adoção de tecnologias cirúrgicas minimamente invasivas.",
    sections=[
        ("Estrutura e Escopo de Atendimento da Clínica Urológica", "Uma clínica de urologia de referência opera com consultórios equipados para cistoscopia flexível ambulatorial, sala de urofluxometria e estudo urodinâmico, sala de ecografia urológica (próstata, rins, bexiga), acesso a sala de pequenos procedimentos (biópsias prostáticas ecoguiadas, instilações intravesicais) e integração com centros cirúrgicos para procedimentos de maior porte (RTU, nefrectomia laparoscópica, prostatectomia robótica). A uroginecologia acrescenta avaliação funcional do assoalho pélvico e tratamentos de incontinência."),
        ("Gestão de Pacientes com Câncer de Próstata", "Câncer de próstata é o tumor mais frequente em homens no Brasil — com rastreamento via PSA, biópsia ecoguiada e seguimento pós-tratamento (cirúrgico, radioterápico ou vigilância ativa) que se estende por décadas. A gestão clínica deve contemplar: controle de PSA evolutivo, laudos de biópsia (sistema ISUP/Gleason), estadiamento (TNM), decisão compartilhada de tratamento e acompanhamento de desfechos oncológicos e funcionais (potência sexual, continência). Sistemas de prontuário com módulos de uro-oncologia estruturada agregam valor real."),
        ("Uroginecologia e Assoalho Pélvico: Demanda Crescente", "Incontinência urinária, prolapso genital e disfunções do assoalho pélvico afetam mais de 30% das mulheres brasileiras — e são condições subdiagnosticadas e subtratadas por estigma e desinformação. Clínicas que combinam uroginecologia com fisioterapia pélvica, pessários, injeção de toxina botulínica intravesical, slings e correção cirúrgica de prolapso têm portfólio completo e altamente diferenciado. A demanda cresce com o envelhecimento da população e o aumento da consciência sobre saúde da mulher."),
        ("Faturamento por Convênio em Urologia", "Urologia tem procedimentos de alto valor cobertos por convênios: cistoscopia, RTU de próstata e bexiga, nefrectomia laparoscópica, ureteroscopia, biópsia de próstata, instilações intravesicais de BCG para câncer de bexiga, colocação de sling para incontinência. O correto uso de tabela CBHPM, pré-autorização para procedimentos de alto custo, codificação TUSS de materiais especiais e gestão de glosas são fundamentais para maximizar o faturamento e a sustentabilidade financeira da clínica."),
        ("Marketing em Urologia: Branding Médico e Captação", "Urologia tem alta busca orgânica para temas como 'tratamento de pedra no rim', 'câncer de próstata', 'incontinência urinária' e 'vasectomia'. Conteúdo educativo em YouTube e Instagram — explicando procedimentos, sintomas e prevenção de doenças urológicas — posiciona o especialista como autoridade e gera captação contínua. Para uroginecologia, campanhas de conscientização sobre incontinência urinária em redes sociais têm altíssimo engajamento feminino e convertem bem em consultas.")
    ],
    faq_list=[
        ("Com que frequência homens acima de 45 anos devem fazer PSA?", "A Sociedade Brasileira de Urologia recomenda rastreamento anual com PSA e toque retal para homens a partir de 50 anos, ou a partir de 40-45 anos para homens com histórico familiar de câncer de próstata em parente de primeiro grau ou afrodescendentes (maior risco). O rastreamento deve ser uma decisão compartilhada entre médico e paciente, considerando expectativa de vida e preferências individuais sobre diagnóstico e tratamento."),
        ("O que é estudo urodinâmico e quando é indicado?", "Estudo urodinâmico é um conjunto de exames que avalia a função da bexiga e da uretra durante o armazenamento e a eliminação de urina. Inclui fluxometria, cistometria, eletromiografia do esfíncter e estudo pressão-fluxo. É indicado para avaliação de incontinência urinária antes de cirurgia, bexiga hiperativa refratária ao tratamento, disfunção miccional neurológica (pós-AVC, esclerose múltipla, lesão medular) e hiperplasia prostática com sintomas obstrutivos. O diagnóstico preciso pelo urodinâmico orienta o tratamento mais adequado."),
        ("Vasectomia é procedimento cirúrgico de alta complexidade que requer estrutura hospitalar?", "Não. A vasectomia pode ser realizada em consultório ou clínica ambulatorial, com anestesia local, em aproximadamente 20-30 minutos. É um procedimento de pequeno porte e baixo risco. Clínicas urológicas equipadas para pequenos procedimentos realizam vasectomias rotineiramente, com espermograma de controle após 12 semanas para confirmar azoospermia. O procedimento tem cobertura obrigatória pelos planos de saúde para pacientes com 2 filhos ou mais, ou com indicação clínica específica.")
    ]
)

# Article 4561 — SaaS sales for clinics: mental health / psychiatry
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-saude-mental-e-psiquiatria",
    title="Vendas para o Setor de SaaS de Gestão de Clínicas de Saúde Mental e Psiquiatria",
    desc="Estratégias de vendas B2B de SaaS para clínicas de saúde mental e psiquiatria: perfil do comprador, proposta de valor, ciclo de vendas e como crescer nesse mercado em expansão.",
    h1="Vendas para o Setor de SaaS de Gestão de Clínicas de Saúde Mental e Psiquiatria",
    lead="O Brasil enfrenta uma crise de saúde mental: mais de 30 milhões de pessoas têm transtornos de ansiedade, 12 milhões vivem com depressão, e a demanda por psiquiatria e psicologia clínica supera amplamente a oferta. Clínicas de saúde mental e psiquiatria crescem aceleradamente, e a complexidade do atendimento — prontuários sensíveis, múltiplos profissionais, telemedicina, planos de tratamento integrados — cria oportunidade real para SaaS especializado.",
    sections=[
        ("O Mercado de Saúde Mental e Sua Especificidade", "Clínicas de saúde mental atendem condições que exigem sigilo reforçado, continuidade de cuidado e equipe multidisciplinar: psiquiatras para diagnóstico e prescrição, psicólogos para psicoterapia individual e em grupo, assistentes sociais, terapeutas ocupacionais e enfermeiros especializados. A gestão dessas clínicas tem desafios únicos: prontuário altamente confidencial (regulação do CFM e do CFP sobre sigilo em saúde mental), agendamento de sessões recorrentes de longa duração, controle de medicação psiquiátrica controlada e gestão de crises."),
        ("Proposta de Valor do SaaS para Saúde Mental", "As principais necessidades de sistema em clínicas de saúde mental incluem: prontuário eletrônico com controle granular de acesso (apenas o profissional que atende vê o conteúdo clínico), módulo de telemedicina integrado para consultas remotas (a saúde mental foi um dos setores que mais abraçou a teleconsulta), gestão de prescrição de medicamentos controlados com rastreabilidade (receituário B, C e especial), agendamento de sessões recorrentes com notificação automática, e portal seguro do paciente para acesso a relatórios e atividades terapêuticas."),
        ("Perfil do Decisor e Abordagem Comercial", "Em clínicas de saúde mental pequenas e médias, o decisor é o psiquiatra ou psicólogo proprietário. Em centros maiores com múltiplos profissionais, há um coordenador administrativo. A abordagem deve começar pelas dores de privacidade e controle: 'Como você garante que apenas o profissional responsável acessa o conteúdo do prontuário de cada paciente?' e 'Como você emite as receitas de medicamentos controlados?' Essas perguntas expõem fragilidades que o SaaS resolve de forma direta."),
        ("Telemedicina e Expansão do Alcance em Saúde Mental", "A psiquiatria e psicologia são especialidades particularmente bem adaptadas à telemedicina: a consulta é eminentemente conversacional, sem necessidade de exame físico na maioria dos casos. Plataformas de saúde mental digital (Vittude, Zenklub, Psicologia Viva) demonstraram a viabilidade e o alcance do modelo. SaaS para clínicas que integra telemedicina nativa — com sala virtual segura, prontuário integrado e assinatura de receitas digitais — amplia o alcance do serviço e permite atender pacientes de outras regiões."),
        ("Conformidade com LGPD e CFM em Saúde Mental", "Dados de saúde mental são considerados dados sensíveis pela LGPD e têm proteções reforçadas — qualquer vazamento ou acesso não autorizado gera responsabilidade legal. Além da LGPD, o CFM (Resolução 1.605/2000) e o CFP têm regulamentações específicas sobre o prontuário psiquiátrico e psicológico. Um SaaS que demonstra conformidade com essas normas — com controles de acesso documentados, logs de auditoria, criptografia de dados e termos de processamento de dados adequados — tem argumento de venda poderoso junto a profissionais conscientes de sua responsabilidade regulatória.")
    ],
    faq_list=[
        ("Clínicas de psicologia e clínicas de psiquiatria precisam de sistemas diferentes?", "Psicologia e psiquiatria têm sobreposições e diferenças: ambas precisam de prontuário confidencial e agendamento de sessões recorrentes. Psiquiatria adiciona a necessidade de gestão de prescrição de controlados (receitas B, C e especial), CID-10/DSM-5 para diagnóstico, e integração com laboratórios para exames. Psicologia tem especificidades de testes psicológicos (armazenamento de resultados de escalas e testes padronizados) e relatórios para terceiros (laudos psicológicos). Um SaaS que atende ambos com módulos específicos por profissão tem mercado mais amplo."),
        ("Como garantir a confidencialidade do prontuário em uma clínica com múltiplos profissionais?", "O sistema deve ter controle de acesso por profissional: cada médico ou psicólogo acessa apenas os prontuários dos seus próprios pacientes. Equipes multidisciplinares podem ter acesso compartilhado configurado (o psiquiatra vê o que o psicólogo registrou, mas outros profissionais não). Logs de auditoria registram quem acessou cada prontuário e quando — essencial para conformidade com LGPD e para investigação de incidentes de privacidade."),
        ("Planos de saúde cobrem consultas de psicologia e psiquiatria?", "Psiquiatria tem cobertura obrigatória pela ANS em planos médico-hospitalares. Psicologia clínica também passou a ter cobertura obrigatória a partir da Resolução Normativa ANS 465/2021 e da Lei 14.454/2022, que obriga planos a cobrirem atendimento por psicólogo. O número mínimo de sessões garantidas e os critérios de acesso variam — consultar o rol de procedimentos da ANS e verificar o plano específico do paciente são etapas essenciais para orientá-lo corretamente.")
    ]
)

# Article 4562 — Consulting: executive leadership / CEO coaching
art(
    slug="consultoria-de-lideranca-executiva-e-coaching-de-ceo",
    title="Consultoria de Liderança Executiva e Coaching de CEO",
    desc="Como estruturar uma consultoria de liderança executiva e coaching de CEO: metodologias, portfólio de serviços, captação de clientes e como gerar impacto real em liderança de alto nível.",
    h1="Consultoria de Liderança Executiva e Coaching de CEO",
    lead="CEOs e líderes executivos estão entre os profissionais com maior impacto e, paradoxalmente, entre os mais isolados — difilmente recebem feedback genuíno, têm poucos pares com quem compartilhar dilemas reais e enfrentam pressões únicas de desempenho. Consultores e coaches de liderança executiva preenchem esse espaço, gerando impacto transformador tanto no líder quanto na organização que ele conduz.",
    sections=[
        ("O Mercado de Coaching Executivo e Consultoria de Liderança", "O mercado de coaching executivo cresceu significativamente no Brasil e globalmente, impulsionado pela reconhecida correlação entre liderança eficaz e desempenho organizacional. A demanda vem de empresas que patrocinam coaching para seus executivos-chave (C-suite, vice-presidentes, líderes de alta potencial) e de executivos que contratam individualmente. O ticket médio é elevado — R$5.000-30.000/mês por executivo atendido — e o mercado ainda tem baixa saturação de coaches verdadeiramente qualificados."),
        ("Diferença entre Coaching Executivo e Consultoria de Liderança", "Coaching executivo é um processo individualizado e confidencial: o coach não dá respostas — facilita a reflexão do executivo para que ele chegue às suas próprias conclusões, amplie sua autoconsciência e desenvolva novas capacidades de liderança. Consultoria de liderança tem escopo mais amplo: pode incluir diagnóstico de estilo de liderança com ferramentas (Hogan, 360°, DISC, Korn Ferry Leadership Architect), design de programas de desenvolvimento de liderança para múltiplos executivos, e aconselhamento estratégico sobre decisões de pessoas e cultura."),
        ("Metodologias e Ferramentas de Avaliação de Liderança", "As ferramentas mais utilizadas incluem: avaliação 360° (feedback anônimo de subordinados, pares e superiores), assessments de personalidade e estilo de liderança (Hogan HPI/HDS/MVPI, MBTI, DiSC, Big Five), inventários de competências de liderança (Korn Ferry Leadership Architect, CCL Benchmarks), e entrevistas estruturadas de incidentes críticos (BEI). A combinação de dados de avaliação com reflexão em coaching cria um processo de desenvolvimento robusto e personalizado."),
        ("Posicionamento e Captação de Clientes de Alto Nível", "Consultores de liderança executiva constroem clientela por reputação e relacionamento — muito raramente por marketing digital direto. O caminho mais eficaz é: trabalhar para empresas de grande porte através de departamentos de RH e de desenvolvimento de liderança, construir relacionamentos com headhunters (que recomendam coaches para executivos recém-colocados), publicar artigos em Harvard Business Review Brasil, MIT Sloan Management Review em Português, e participar de eventos exclusivos de CEOs (YPO, Vistage, AmCham CEO Councils)."),
        ("Modelos de Engajamento e Remuneração", "Coaching executivo é tipicamente contratado em programas de 6-12 meses com sessões quinzenais de 90 minutos — R$3.000-15.000 por sessão dependendo da experiência do coach e do nível do executivo. Contratos corporativos com empresas para coaching de múltiplos líderes têm valor total de R$100k-1M+. Consultoria de liderança para programas de desenvolvimento de pipeline (identificação e desenvolvimento de sucessores) é projeto de escopo fechado, tipicamente R$50-500k. Retainers de aconselhamento estratégico de CEO — R$20-80k/mês — são o serviço de maior valor e maior stickiness.")
    ],
    faq_list=[
        ("Qual a diferença entre coaching e mentoring para líderes executivos?", "Coaching foca no presente e futuro: o coach ajuda o executivo a identificar padrões limitantes, desenvolver novas perspectivas e alcançar objetivos específicos de liderança. O coach não precisa ter passado pelo mesmo papel. Mentoring é baseado em experiência compartilhada: o mentor (geralmente executivo mais sênior) compartilha sua jornada, oferece conselhos e abre portas com sua rede. Ambos são valiosos — coaching para desenvolvimento de competências, mentoring para navegação de carreira e acesso a redes."),
        ("Como um CEO pode avaliar se um coach executivo é qualificado?", "Credenciais relevantes incluem: certificações ICF (International Coaching Federation) no nível PCC ou MCC, formação específica em coaching executivo (CCL, IMD, INSEAD, Metasysteme), experiência como executivo (credibilidade experiencial) e supervisão contínua. Além das credenciais, o fit pessoal é fundamental — o executivo deve sentir segurança e desafio intelectual com o coach. Sessões introdutórias de 'química' antes do engajamento formal são prática padrão do mercado."),
        ("Empresas que patrocinam coaching para executivos têm direito a ver o conteúdo das sessões?", "Não. Coaching executivo é estritamente confidencial — o patrocinador (empresa) sabe que o programa está ocorrendo e pode acordar sobre objetivos gerais e indicadores de progresso observáveis, mas o conteúdo das sessões é sigiloso entre coach e coachee. Essa confidencialidade é condição para que o executivo seja genuinamente vulnerável e aberto no processo. Relatórios de progresso para a empresa, quando acordados, são sempre revisados e aprovados pelo executivo antes de serem compartilhados.")
    ]
)

# Article 4563 — B2B SaaS: school management / K12 edtech
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-escolar-e-edtech-k12",
    title="Gestão de Negócios de Empresa de B2B SaaS de Gestão Escolar e EdTech K12",
    desc="Como construir e escalar uma empresa de B2B SaaS de gestão escolar e EdTech K12 no Brasil: produto, mercado, estratégias de go-to-market e crescimento sustentável.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Gestão Escolar e EdTech K12",
    lead="O segmento de EdTech K12 (educação básica) é um dos maiores e mais complexos do mercado de tecnologia educacional no Brasil. Com mais de 180.000 escolas privadas e 150.000 públicas, a oportunidade para SaaS de gestão escolar, plataformas de aprendizagem e ferramentas pedagógicas digitais é enorme — mas também exige navegação cuidadosa de regulação, ciclos de venda longos e diversidade de perfis de clientes.",
    sections=[
        ("Panorama do Mercado de EdTech K12 no Brasil", "O sistema educacional brasileiro é vasto e diverso: 50 milhões de alunos na educação básica, das quais 16% em escolas privadas (cerca de 8 milhões). As escolas privadas pagam — são o mercado principal de SaaS de gestão escolar. O setor público, que é a maioria, tem acesso ao mercado via licitações e programas governamentais. Players como Blackboard, Google for Education e Microsoft Education dominam plataformas de aprendizagem, mas gestão escolar administrativa (ERP escolar, comunicação com famílias, secretaria digital) ainda tem muito espaço."),
        ("Produto: ERP Escolar, Plataforma de Aprendizagem e Comunicação", "Um SaaS de gestão escolar completo cobre: secretaria digital (matrícula, histórico escolar, boletim eletrônico, declarações e documentos), gestão financeira (mensalidades, negociação de inadimplência, bolsas e descontos), comunicação escola-família (notificações, agenda, recados, acompanhamento do aluno), plataforma de ensino (conteúdo digital, atividades, sala de aula virtual), e portais para alunos, professores, pais e diretores. A integração dessas camadas em uma única plataforma é o diferencial frente a soluções pontuais."),
        ("Segmentação: Escolas de Diferentes Portes e Redes", "Escolas privadas independentes de pequeno porte (até 500 alunos) priorizam solução acessível com secretaria, financeiro e comunicação. Redes de escolas (franquias, sistemas apostilados como Período, COC, Anglo) precisam de gestão centralizada multi-unidade com padronização de processos e analytics de rede. Escolas públicas via secretarias de educação requerem processo licitatório e conformidade com requisitos de dados do governo. Cada segmento tem necessidades, preços e processo de compra radicalmente distintos."),
        ("Go-to-Market e Ciclo de Venda para Escolas", "A venda para escolas privadas independentes tem ciclo de 1-3 meses e decisão do diretor ou mantenedor. Redes e secretarias de educação têm ciclos de 6-18 meses com comitês de decisão e licitações. Canais eficazes para escolas privadas incluem: associações de escolas (AICE, SINEPE), eventos pedagógicos (BETT Brasil, CIEE EdTech), parcerias com sistemas apostilados e editoras, e inbound via SEO ('sistema de gestão escolar', 'software para escola'). A demo com o diretor e a secretária — mostrando redução de trabalho manual — é decisiva."),
        ("Retenção e Churn em SaaS Escolar", "SaaS educacional tem naturalmente alta stickiness: migrar todos os dados de alunos, históricos, financeiro e usuários para outro sistema é traumático para a escola. Mas a gestão da renovação é crítica — escolas decidem no início do ano letivo (janeiro-fevereiro) se mantêm o sistema. Estratégias de retenção incluem: suporte dedicado durante o período de matrículas (setembro-dezembro), atualizações pedagógicas e regulatórias contínuas (BNCC, LGPD no ambiente escolar), e NPS medido com direção, secretaria e professores para identificar insatisfações antes do momento de renovação.")
    ],
    faq_list=[
        ("Qual a diferença entre um sistema de gestão escolar e uma plataforma de aprendizagem (LMS)?", "Sistema de gestão escolar (ERP escolar) gerencia processos administrativos: matrícula, boletim, histórico, financeiro, comunicação com famílias. LMS (Learning Management System) gerencia o processo de ensino e aprendizagem: conteúdo digital, atividades, avaliações, fóruns, salas de aula virtuais. Algumas plataformas integram as duas funcionalidades; outras são especializadas em uma. Para escolas que buscam digitalização completa, a integração entre ERP escolar e LMS — com dado do aluno centralizado — é a solução mais eficiente."),
        ("Como a LGPD impacta sistemas de gestão escolar que processam dados de menores?", "Dados de crianças e adolescentes são protegidos com exigências reforçadas pela LGPD: requerem consentimento específico dos responsáveis legais, devem ser tratados com o melhor interesse da criança, e têm restrições adicionais sobre compartilhamento. Sistemas escolares devem ter: termos de consentimento específicos para uso de dados de menores, controle de acesso rigoroso a dados pessoais de alunos, política de retenção clara (quanto tempo os dados ficam após o aluno sair), e rastreabilidade de uso de dados."),
        ("Escolas públicas podem contratar SaaS de gestão escolar diretamente?", "Escolas públicas não contratam diretamente — a contratação é feita pela Secretaria de Educação municipal ou estadual, via processo licitatório (pregão eletrônico ou concorrência, dependendo do valor). Isso exige que o SaaS esteja inscrito em sistemas de registro de preços, tenha certidões negativas de débito em dia e cumpra requisitos de interoperabilidade com sistemas do governo (INEP, MEC). O ticket por aluno/mês é menor que no privado, mas o volume de alunos de uma secretaria estadual pode gerar contratos milionários.")
    ]
)

# Article 4564 — Clinic management: vascular / endovascular surgery
art(
    slug="gestao-de-clinicas-de-cirurgia-vascular-e-endovascular",
    title="Gestão de Clínicas de Cirurgia Vascular e Endovascular",
    desc="Guia prático para gestão de clínicas de cirurgia vascular e endovascular: estrutura clínica, procedimentos, ultrassonografia vascular, faturamento e estratégias de crescimento.",
    h1="Gestão de Clínicas de Cirurgia Vascular e Endovascular",
    lead="Clínicas de cirurgia vascular e endovascular atendem condições de alta prevalência — varizes, insuficiência venosa crônica, aterosclerose periférica, aneurismas, tromboses e pé diabético — com crescimento impulsionado pelo envelhecimento da população e pela epidemia de diabetes. A gestão dessas clínicas combina consultas ambulatoriais de volume com procedimentos cirúrgicos eletivos e de urgência, além de laboratório vascular para diagnóstico por imagem.",
    sections=[
        ("Estrutura e Escopo da Clínica Vascular", "Uma clínica de cirurgia vascular de referência opera com consultório de avaliação clínica, laboratório vascular com ecodopplercolorido (ultrassonografia vascular para diagnóstico de tromboses, insuficiência venosa, avaliação pré-operatória de artérias e veias), sala de procedimentos ambulatoriais (escleroterapia, ablação endovenosa a laser ou radiofrequência para varizes, angioplastia periférica em centros hemodinâmicos próprios) e acesso a bloco cirúrgico para cirurgias abertas de maior porte (safenectomia, revascularização periférica, endoprótese)."),
        ("Varizes e Insuficiência Venosa: Principal Volume de Atendimento", "Varizes afetam mais de 35% da população adulta brasileira — são a principal demanda de clínicas vasculares. O tratamento moderno combina escleroterapia (para vasinhos), ablação endovenosa a laser ou radiofrequência (para veias safenas insuficientes, substituindo a safenectomia aberta) e flebectomia de varicosidades tributárias. O agendamento de procedimentos com diferentes durações e materiais, controle de retornos para avaliação de resultado (ecodoppler de controle) e comunicação com pacientes em seguimento compõem a operação clínica diária."),
        ("Pé Diabético e Revascularização: Complexidade e Urgência", "Pé diabético isquêmico é emergência vascular que demanda avaliação rápida e revascularização (angioplastia ou bypass) para salvar o membro. Clínicas vasculares de referência para pé diabético têm fluxo de urgência bem definido, equipe multidisciplinar com endocrinologista e podólogo, e acesso a sala hemodinâmica para angioplastia periférica urgente. O manejo adequado do pé diabético reduz amputações — a taxa de amputação é um indicador de qualidade que diferencia clínicas de referência."),
        ("Laboratório Vascular: Ecodoppler e Seu Papel na Gestão", "O laboratório vascular com ecodopplercolorido é ativo estratégico da clínica vascular: permite diagnóstico não invasivo de tromboses (TVP), insuficiência venosa (mapeamento de safenas), isquemia arterial crônica e aguda, avaliação de aneurismas e planejamento pré-operatório. Clínicas que têm laboratório próprio eliminam a dependência de serviços externos, têm controle da qualidade do exame, geram receita adicional e tornam o fluxo do paciente mais ágil e integrado. O ecodoppler é o exame de maior volume em clínicas vasculares."),
        ("Marketing e Captação em Cirurgia Vascular", "Captação em cirurgia vascular combina encaminhamentos médicos (clínicos, cardiologistas, endocrinologistas para pé diabético, dermatologistas para varizes) com marketing digital direto ao paciente. Pesquisas por 'tratamento de varizes', 'cirurgia vascular' e 'médico vascular em [cidade]' têm alto volume e intenção de compra clara. Conteúdo educativo sobre sintomas de insuficiência venosa, quando operar varizes e prevenção de trombose converte bem em agendamentos e posiciona a clínica como autoridade vascular regional.")
    ],
    faq_list=[
        ("Tratamento de varizes com laser é cobertura obrigatória dos planos de saúde?", "Depende da indicação clínica. Varizes com repercussão clínica documentada (insuficiência venosa crônica com edema, dermatite ocre, úlcera venosa) têm cobertura obrigatória pela ANS para tratamento cirúrgico. Varizes de caráter exclusivamente estético podem não ter cobertura. A ablação endovenosa a laser e por radiofrequência substitui a safenectomia aberta e tem cobertura crescente — mas nem todas as operadoras cobrem ainda. O laudo médico detalhando a indicação clínica é fundamental para autorização."),
        ("Como funciona a escleroterapia para vasinhos e o que pacientes devem esperar?", "Escleroterapia é o tratamento de escolha para vasinhos (telangiectasias) e veias reticulares: uma solução esclerosante (polidocanol ou glicose hipertônica) é injetada na veia com agulha finíssima, causando inflamação e fechamento da veia. Necessita de 2-4 sessões com intervalo de 4-6 semanas para resultado completo. Após a sessão, o paciente usa meia-calça elástica por 1-7 dias. É procedimento ambulatorial rápido (20-40 min), sem anestesia geral e com retorno imediato às atividades normais."),
        ("O que é trombose venosa profunda (TVP) e por que é urgência médica?", "TVP é a formação de coágulo em veias profundas, geralmente das pernas. O risco principal é a embolia pulmonar: o coágulo pode se desprender e atingir os pulmões — condição potencialmente fatal. TVP manifesta-se com dor, edema e calor na perna afetada. O diagnóstico é confirmado por ecodopplercolorido. O tratamento com anticoagulantes (heparina, rivaroxabana, apixabana) deve ser iniciado imediatamente. Clínicas vasculares com protocolo de atendimento urgente para suspeita de TVP salvam vidas e constroem reputação de referência.")
    ]
)

# Article 4565 — SaaS sales for centros: radiation therapy / radiation oncology
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-centros-de-radioterapia-e-oncologia-radioterapica",
    title="Vendas para o Setor de SaaS de Gestão de Centros de Radioterapia e Oncologia Radioterápica",
    desc="Estratégias de vendas B2B de SaaS para centros de radioterapia e oncologia radioterápica: perfil do comprador, proposta de valor, ciclo de vendas e diferenciação de produto.",
    h1="Vendas para o Setor de SaaS de Gestão de Centros de Radioterapia e Oncologia Radioterápica",
    lead="Centros de radioterapia são ambientes de altíssima regulação, tecnologia de ponta e complexidade operacional: aceleradores lineares, planejamento dosimétrico computadorizado, controle de qualidade rigoroso e protocolos de tratamento de precisão. Vender SaaS de gestão para esse nicho exige entender profundamente a física médica aplicada, os fluxos de planejamento e tratamento, e as exigências regulatórias da ANVISA e da CNEN.",
    sections=[
        ("Complexidade Operacional dos Centros de Radioterapia", "Centros de radioterapia operam aceleradores lineares (LINAC) ou equipamentos de braquiterapia, com físicos médicos, radio-oncologistas, técnicos em radioterapia e enfermeiros especializados. O fluxo de tratamento é altamente protocolado: consulta de indicação, planejamento dosimétrico (CT de simulação, contorno de volumes, cálculo de dose pelo TPS — Treatment Planning System), validação pelo físico médico, sessões de tratamento (1-40 sessões dependendo do protocolo), controles de qualidade diários dos equipamentos e acompanhamento de toxicidade. Cada etapa gera documentação crítica para segurança e rastreabilidade."),
        ("O Que o SaaS Pode Resolver em Radioterapia", "Os principais pontos de melhoria que um SaaS endereça incluem: gestão de agenda do LINAC (maximizar o uso do equipamento com blocos de tempo por tipo de tratamento, manutenção e controle de qualidade), rastreabilidade do paciente em cada etapa do fluxo (planejamento aprovado? QA do tratamento realizado? Toxicidade registrada?), integração com TPS (Pinnacle, Eclipse, Monaco) para recebimento automático de planos aprovados, e relatórios de produção e qualidade para a direção e para auditoria da ANVISA e CNEN."),
        ("Perfil do Comprador em Centros de Radioterapia", "Os decisores são o radio-oncologista chefe e o físico médico responsável técnico — profissionais com altíssima especificidade técnica que avaliam o sistema com critérios rigorosos de segurança e conformidade. O argumento de venda deve ser técnico e detalhado: mostrar a integração com TPS, os controles de qualidade suportados, os relatórios de dosimetria e os logs de auditoria de tratamentos. Uma demo genérica não funciona — é necessário adaptar completamente à realidade de radioterapia."),
        ("Precificação e Justificativa de Investimento", "Centros de radioterapia têm faturamento elevado: cada sessão de radioterapia fatura R$400-2.500 por convênio ou SUS (via APAC de alta complexidade). Um LINAC que opera 30-40 sessões por dia gera R$12.000-100.000 diários. Um SaaS de R$2.000-8.000/mês representa menos de 1% do faturamento mensal — e a justificativa pelo tempo economizado na gestão de agenda, controle de fluxo e preparação de auditorias torna o investimento trivial. O argumento de conformidade com ANVISA e CNEN é o mais poderoso."),
        ("Expansão para Centros Integrados de Oncologia", "Centros de radioterapia frequentemente integram serviços de quimioterapia ambulatorial, oncologia clínica e cuidados paliativos — formando centros integrados de oncologia. Um SaaS que cobre tanto o fluxo de radioterapia quanto a oncologia clínica adjacente torna-se a espinha dorsal digital do centro, aumentando o LTV e a resistência à troca. A integração entre os fluxos de radio e quimioterapia — especialmente em protocolos de radioquimioterapia concomitante — é funcionalidade de alto valor diferencial.")
    ],
    faq_list=[
        ("Quais regulações governam centros de radioterapia no Brasil?", "Centros de radioterapia são regulados pela ANVISA (RDC 330/2019 para serviços de radioterapia) e pela CNEN (Comissão Nacional de Energia Nuclear), que regula o uso de fontes radioativas. A ANVISA exige licença de operação, responsável técnico médico e físico médico, controles de qualidade documentados e rastreabilidade de tratamentos. A CNEN licencia o uso de fontes de braquiterapia e define requisitos de proteção radiológica. Um SaaS que gera documentação automática para auditorias dessas agências tem valor imenso para a conformidade."),
        ("O que é um TPS (Treatment Planning System) e como um SaaS de gestão se integra a ele?", "TPS é o software especializado que calcula a distribuição de dose de radiação no tumor e tecidos adjacentes a partir de imagens de CT de simulação — é o coração técnico da radioterapia moderna. Softwares como Pinnacle (Philips), Eclipse (Varian/Siemens) e Monaco (Elekta) são os TPS mais usados. Um SaaS de gestão integra com o TPS recebendo: a aprovação do plano (com doses prescritas), o schedule de sessões e os parâmetros de tratamento — garantindo que o que é entregue ao paciente corresponda ao que foi planejado."),
        ("Como a inteligência artificial está sendo aplicada na radioterapia?", "IA está transformando múltiplas etapas da radioterapia: contorno automático de estruturas anatômicas em CT de simulação (economizando horas de trabalho do físico e radio-oncologista), planejamento adaptativo (ajustando a dose às mudanças anatômicas do tumor durante o tratamento), predição de toxicidade (identificando pacientes com maior risco de efeitos adversos graves), e controle de qualidade automatizado de planos dosimétricos. Centros que adotam IA antes da concorrência têm vantagem competitiva em produtividade e qualidade de tratamento.")
    ]
)

# Article 4566 — Consulting: innovation management / R&D portfolio
art(
    slug="consultoria-de-gestao-da-inovacao-e-portfolio-de-pesquisa-e-desenvolvimento",
    title="Consultoria de Gestão da Inovação e Portfólio de Pesquisa e Desenvolvimento",
    desc="Como estruturar uma consultoria de gestão da inovação e portfólio de P&D: metodologias, serviços, captação de clientes industriais e corporativos e entrega de valor mensurável.",
    h1="Consultoria de Gestão da Inovação e Portfólio de Pesquisa e Desenvolvimento",
    lead="Inovar de forma estruturada — gerindo portfólio de P&D, acelerando o funil de inovação e convertendo ideias em produtos e serviços rentáveis — é uma das competências mais escassas e mais valorizadas nas organizações brasileiras. Consultorias especializadas em gestão da inovação têm papel crítico em ajudar empresas a transformar investimento em P&D em vantagem competitiva real e mensurável.",
    sections=[
        ("A Demanda por Gestão Estruturada de Inovação", "Empresas brasileiras investem em P&D e inovação, mas frequentemente sem estrutura de governança adequada: projetos que não têm critérios claros de go/no-go, portfólios desbalanceados (todos os ovos na mesma cesta tecnológica), funis que não convertem invenções em produtos comercializáveis e times que trabalham em silos sem conexão com as necessidades do mercado. Consultores de inovação trazem metodologia, disciplina e perspectiva externa para transformar esses investimentos em retorno."),
        ("Portfólio de Serviços de Consultoria de Inovação", "Os serviços mais demandados incluem: diagnóstico de maturidade de inovação (TRL assessment, análise de capacidade de P&D, benchmarking com indústria), design e implementação de sistema de gestão de ideias (ideation, seleção e priorização), estruturação de escritório de inovação (IHubs, Labs corporativos), gestão de portfólio de P&D com frameworks de Stage-Gate e Lean Startup adaptados ao corporativo, conexão com ecossistema de inovação aberta (startups, universidades, centros de pesquisa), e captação de incentivos fiscais para P&D (Lei do Bem, FINEP, FAPESP, EMBRAPII)."),
        ("Metodologias: Stage-Gate, Lean Startup e Open Innovation", "O Stage-Gate (Robert Cooper) é o framework mais consolidado para gestão de portfólio de NPD (New Product Development): divide o processo em estágios com portões de decisão go/kill/hold que filtram projetos com base em critérios pré-definidos de mercado, técnicos e financeiros. Para inovações mais radicais e incertas, abordagens Lean Startup (build-measure-learn) e Design Thinking são mais apropriadas. Open Innovation (Chesbrough) estrutura como a empresa colabora com parceiros externos — startups, universidades, fornecedores — para co-desenvolver inovações."),
        ("Captação de Clientes e Posicionamento da Consultoria", "Os principais clientes de consultoria de inovação são: empresas industriais de médio e grande porte que buscam modernizar seu P&D, empresas de serviços com investimento crescente em tecnologia, e órgãos de fomento que contratam consultoras para implementar programas de inovação em empresas apoiadas. A captação passa por eventos (Anpei, ABQ, Fórum da Indústria), ABIPTI, parcerias com agências como SENAI e SEBRAE, e publicações em revistas de gestão da inovação. Casos de sucesso com ROI documentado são o principal diferencial."),
        ("Incentivos Fiscais para P&D: Uma Especialização de Alto Valor", "A Lei do Bem (Lei 11.196/2005) permite que empresas do Lucro Real deduzam 60-80% dos gastos qualificados de P&D do Imposto de Renda, além de depreciação acelerada de equipamentos de pesquisa. A FINEP tem linhas de financiamento reembolsável e não reembolsável para projetos de inovação. Conhecer e ajudar empresas a captar esses incentivos é serviço de alto valor: uma empresa com R$5M em gastos de P&D pode economizar R$3M em impostos via Lei do Bem — pagando facilmente os honorários de consultoria com essa economia.")
    ],
    faq_list=[
        ("O que é o TRL (Technology Readiness Level) e como é usado na gestão de portfólio de P&D?", "TRL é uma escala de 1-9 que mede a maturidade tecnológica de uma inovação: TRL 1 é princípio científico observado, TRL 9 é sistema comprovado em operação em ambiente real. Gestão de portfólio usa TRL para balancear investimentos: pesquisa básica (TRL 1-3), desenvolvimento aplicado (TRL 4-6) e demonstração/implantação (TRL 7-9). Portfólios balanceados têm projetos em múltiplos TRLs — garantindo fluxo contínuo de inovações prontas para mercado e projetos de longo prazo que renovam o portfólio no futuro."),
        ("Como uma empresa pode aproveitar a Lei do Bem para financiar seus projetos de P&D?", "Para aproveitar a Lei do Bem, a empresa deve: estar no regime de Lucro Real, ter projetos que atendam ao conceito de P&D tecnológico (incerteza técnica, atividade sistemática, novidade), documentar adequadamente as atividades e gastos (horas de pesquisadores, materiais, depreciação de equipamentos) e reportar ao MCTI (Ministério da Ciência, Tecnologia e Inovações) anualmente. Uma consultoria especializada identifica quais atividades se qualificam, estrutura a documentação e maximiza o benefício fiscal legal."),
        ("Open Innovation funciona para empresas brasileiras de médio porte?", "Sim — com adaptações. Empresas de grande porte podem manter hubs de inovação próprios e conexões diretas com dezenas de startups. Para médias empresas, a abordagem mais eficaz é via programas estruturados: aceleradoras corporativas parceiras (como as geridas por Wayra, Telefonica, Liga Ventures), desafios de inovação abertos para startups em problemas específicos, e parcerias com ICTs (Institutos de Ciência e Tecnologia) como SENAI, INPI e universidades. O custo por conexão é muito menor do que manter estrutura interna de inovação aberta.")
    ]
)

# Update sitemap and trilha
root = pathlib.Path(__file__).parent
slugs = [
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-eventos-e-venues", "Gestão de Negócios de Empresa de B2B SaaS de Gestão de Eventos e Venues"),
    ("gestao-de-clinicas-de-urologia-e-uroginecologia", "Gestão de Clínicas de Urologia e Uroginecologia"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-saude-mental-e-psiquiatria", "Vendas para o Setor de SaaS de Gestão de Clínicas de Saúde Mental e Psiquiatria"),
    ("consultoria-de-lideranca-executiva-e-coaching-de-ceo", "Consultoria de Liderança Executiva e Coaching de CEO"),
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-escolar-e-edtech-k12", "Gestão de Negócios de Empresa de B2B SaaS de Gestão Escolar e EdTech K12"),
    ("gestao-de-clinicas-de-cirurgia-vascular-e-endovascular", "Gestão de Clínicas de Cirurgia Vascular e Endovascular"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-centros-de-radioterapia-e-oncologia-radioterapica", "Vendas para o Setor de SaaS de Gestão de Centros de Radioterapia e Oncologia Radioterápica"),
    ("consultoria-de-gestao-da-inovacao-e-portfolio-de-pesquisa-e-desenvolvimento", "Consultoria de Gestão da Inovação e Portfólio de Pesquisa e Desenvolvimento"),
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

print("Done — batch 1538")
