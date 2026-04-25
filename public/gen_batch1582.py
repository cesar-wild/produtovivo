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

# Article 4647 — B2B SaaS: API management and developer platforms
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-apis-e-plataformas-para-desenvolvedores",
    title="Gestão de Negócios de Empresa de B2B SaaS de Gestão de APIs e Plataformas para Desenvolvedores",
    desc="Como estruturar e escalar uma empresa de B2B SaaS de gestão de APIs e plataformas para desenvolvedores: modelo de negócio, diferenciação, go-to-market e métricas de crescimento.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Gestão de APIs e Plataformas para Desenvolvedores",
    lead="O crescimento da economia de APIs transformou a gestão de integração em infraestrutura crítica de negócio. Plataformas de API management e developer experience atendem tanto grandes empresas que precisam governar dezenas de APIs internas quanto startups que monetizam dados e funcionalidades via API.",
    sections=[
        ("O Mercado de API Management e Developer Platforms",
         "O mercado de API management inclui gateways de API (que gerenciam tráfego, autenticação e rate limiting), portais de desenvolvedores (documentação, sandbox e onboarding de parceiros), plataformas de integração iPaaS (que conectam sistemas sem código), ferramentas de monitoramento de API e platforms como serviço (PaaS) para desenvolvedores. Players como Kong, Apigee (Google), AWS API Gateway, MuleSoft e soluções brasileiras atendem segmentos distintos. O mercado cresce impulsionado pela adoção de microsserviços, pela necessidade de integração entre sistemas legados e cloud, e pelo crescimento de ecosistemas de parceiros baseados em API."),
        ("Diferenciação em API Management SaaS",
         "Os diferenciadores relevantes incluem: developer experience superior (documentação automática via OpenAPI/Swagger, sandbox interativo, SDKs gerados automaticamente), governança de API (versionamento, deprecação controlada, contratos de API), observabilidade avançada (latência, erros e uso por endpoint e por consumidor), segurança de API (detecção de ataques como injection e scraping, mTLS, OAuth 2.0 nativo), e monetização de API (billing por chamada, por volume ou por feature para empresas que vendem acesso via API). A facilidade para desenvolvedores — quanto tempo leva para fazer a primeira chamada de API com sucesso — é o critério de adoção mais decisivo."),
        ("Modelo de Receita em API Management SaaS",
         "O modelo varia por segmento: para API gateway, cobrança por volume de chamadas processadas (R$ por milhão de requests) com tier gratuito para low volume. Para portais de desenvolvedor e iPaaS, mensalidade por número de integrações ativas, usuários ou ambientes. Enterprise plan com SLA garantido, suporte dedicado e deployment on-premise ou VPC privada costuma representar 60% a 80% da receita em plataformas maduras. Monetização de API como produto — em que a plataforma cobra pelos dados ou funcionalidades que o cliente expõe via API para seus parceiros — é modelo de negócio emergente com alto potencial."),
        ("Go-to-Market para Developer Platforms",
         "O desenvolvedor é o usuário e o principal influenciador da compra — a estratégia de PLG (Product-Led Growth) dominante nesse mercado começa por converter desenvolvedores individuais que adotam a ferramenta em projetos pessoais ou side projects. Content marketing técnico (tutoriais, exemplos de código, integrações com frameworks populares), presença ativa no GitHub e Stack Overflow, e programa de desenvolvedores com plano gratuito robusto são os pilares de aquisição. O upsell acontece quando o projeto cresce: o desenvolvedor que começou free precisa de mais volume, SLA empresarial ou recursos de equipe — e a decisão de compra vai para o gestor de engenharia ou CTO."),
        ("Métricas Críticas em Developer Platforms",
         "As métricas de produto incluem time-to-first-call (quanto tempo um novo desenvolvedor leva até fazer a primeira chamada de API com sucesso — a métrica de ativação mais crítica), volume de chamadas por cliente (indicador de engajamento e valor gerado), número de integrações ativas (que cria switching cost), e taxa de erro de API por cliente (indicador de saúde do serviço). As métricas de negócio incluem MRR, NRR (expansão natural conforme o volume cresce), churn e CAC por canal de aquisição (PLG versus enterprise sales). Developer platforms com PLG bem executado têm CAC estruturalmente muito baixo — o produto se vende para os usuários finais sem equipe de vendas no início.")
    ],
    faq_list=[
        ("O que é um API gateway e por que ele é necessário?",
         "Um API gateway é a camada intermediária entre clientes (apps, parceiros, serviços internos) e os serviços de backend. Ele centraliza autenticação e autorização, rate limiting, logging, transformação de requests e roteamento. Sem um gateway, cada serviço precisa implementar essas funcionalidades individualmente — gerando duplicação de código e inconsistência de segurança. Em arquiteturas de microsserviços, o gateway é componente obrigatório."),
        ("iPaaS é a mesma coisa que API management?",
         "Não — iPaaS (Integration Platform as a Service) foca em conectar sistemas e automatizar fluxos de dados entre aplicações (como o Zapier ou MuleSoft para empresas). API management foca em expor, governar e monitorar APIs que outros sistemas ou parceiros consomem. As duas categorias se complementam: iPaaS consome APIs, API management governa quais APIs estão disponíveis e como são acessadas."),
        ("Como monetizar dados via API?",
         "Defina o produto de dados que tem valor para terceiros (dados históricos, dados em tempo real, scores analíticos, dados geoespaciais), estruture em uma API bem documentada com autenticação e rate limiting, escolha o modelo de preço (por chamada, por volume mensal, por assinatura de tier), publique em um portal de desenvolvedor com sandbox e faturamento integrado. Marketplaces de dados como AWS Data Exchange e plataformas de Open Finance facilitam a distribuição.")
    ]
)

# Article 4648 — Clinic: Ophthalmology and refractive surgery
art(
    slug="gestao-de-clinicas-de-oftalmologia-e-cirurgia-refrativa",
    title="Gestão de Clínicas de Oftalmologia e Cirurgia Refrativa",
    desc="Guia completo de gestão para clínicas de oftalmologia e cirurgia refrativa: fluxo assistencial, equipamentos, gestão de cirurgias eletivas e indicadores de performance.",
    h1="Gestão de Clínicas de Oftalmologia e Cirurgia Refrativa",
    lead="A oftalmologia combina atendimento de alta demanda por condições prevalentes — miopia, glaucoma, catarata, degeneração macular — com procedimentos cirúrgicos de alta tecnologia como LASIK, cirurgia de catarata com lente premium e implante de lente fácica. A gestão eficiente exige infraestrutura técnica sofisticada e fluxo clínico bem estruturado.",
    sections=[
        ("Abrangência da Oftalmologia Clínica e Cirúrgica",
         "A oftalmologia ambulatorial atende: ametropias (miopia, hipermetropia, astigmatismo, presbiopia), glaucoma (a segunda causa de cegueira no Brasil, exigindo monitoramento crônico), catarata (a primeira causa de cegueira tratável, altamente prevalente acima dos 60 anos), degeneração macular relacionada à idade (DMRI), retinopatia diabética, estrabismo e ambliopia em crianças, e ceratocone e outras doenças da córnea. Subespecialidades como retina e vítreo, glaucoma, córnea, oculoplástica e estrabismo pediátrico criam nichos de referência de alto valor dentro da oftalmologia."),
        ("Infraestrutura e Equipamentos em Oftalmologia",
         "A clínica de oftalmologia requer investimento significativo em equipamentos diagnósticos: refratômetro automático, lâmpada de fenda, tonômetro (para pressão ocular), retinógrafo não midriático, tomografia de coerência óptica (OCT — para retina, nervo óptico e córnea), topografia de córnea (para avaliação pré-cirúrgica), campimetria computadorizada (campo visual — obrigatório no glaucoma) e ecógrafo ocular. Para cirurgia refrativa, a plataforma de laser excimer (LASIK, PRK) e o femtossegundo representam investimento de R$800 mil a R$2 milhões, justificado por alto volume cirúrgico."),
        ("Cirurgia Refrativa: O Produto de Alto Ticket da Oftalmologia",
         "Cirurgias refrativas (LASIK, LASEK, PRK, implante de lente fácica ICL) são procedimentos eletivos pagos diretamente pelo paciente — sem dependência de plano de saúde — com tickets de R$3.000 a R$8.000 por olho. A decisão de compra é altamente influenciada por conteúdo educativo sobre segurança, resultados e candidatura ao procedimento. SEO para 'cirurgia de miopia [cidade]', 'LASIK [cidade]' e 'quanto custa cirurgia olho laser' captura intenção de compra de alta conversão. Depoimentos e casos de resultado visual (antes e depois) são os conteúdos de maior conversão nesse nicho."),
        ("Gestão de Glaucoma e Condições Crônicas",
         "Glaucoma é uma das condições crônicas mais comuns em oftalmologia, exigindo acompanhamento semestral ou anual com campimetria e OCT para monitoramento da progressão. A gestão desse fluxo crônico — com lembretes de retorno, controle de exames periódicos em dia e adesão ao colírio — é semelhante à endocrinologia e cardiologia: protocolos estruturados que garantem que pacientes assintomáticos (glaucoma é silencioso no início) não sejam perdidos no seguimento. A retinopatia diabética, com acompanhamento anual ou semestral dependendo do grau, também gera fluxo crônico relevante em regiões com alta prevalência de diabetes."),
        ("Indicadores de Performance em Oftalmologia",
         "As métricas clínicas incluem taxa de complicações em cirurgias de catarata e refrativa (indicador de qualidade técnica e seleção de candidatos), acuidade visual pós-cirúrgica (resultado funcional), e taxa de progressão em glaucoma (indicador de qualidade do seguimento). As métricas de negócio incluem taxa de conversão de consulta para cirurgia refrativa (paciente que consulta sobre LASIK e fecha o procedimento), ticket médio por tipo de atendimento, e receita por equipamento de diagnóstico (OCT, campimetria — que devem pagar seu investimento em prazo razoável).")
    ],
    faq_list=[
        ("LASIK é seguro? Quem pode fazer?",
         "LASIK é um dos procedimentos cirúrgicos mais realizados no mundo com perfil de segurança excelente quando bem indicado. Os critérios de candidatura incluem: miopia, hipermetropia ou astigmatismo estável por pelo menos 12 meses, córnea com espessura adequada, ausência de ceratocone ou doenças da córnea, e idade mínima de 18 a 21 anos. A avaliação pré-operatória completa — topografia, paquimetria, aberrometria — é obrigatória para confirmar a candidatura."),
        ("Cirurgia de catarata tem cobertura pelo plano de saúde?",
         "Sim — a cirurgia de catarata é procedimento coberto por todos os planos de saúde quando há indicação clínica (redução de acuidade visual que impacta as atividades diárias). A lente intraocular monofocal padrão é coberta pelo plano; lentes premium (multifocais, tóricas para astigmatismo, de foco estendido EDOF) são cobradas como diferença de material, com custo adicional pago pelo paciente."),
        ("O que é OCT e para que serve em oftalmologia?",
         "OCT (Tomografia de Coerência Óptica) é um exame de imagem não invasivo que produz cortes transversais de alta resolução da retina, nervo óptico e córnea — comparável a uma 'ultrassonografia de alta definição' do olho. É essencial para diagnóstico e monitoramento de glaucoma (análise da camada de fibras nervosas), degeneração macular (detecção de fluido sub-retiniano), e avaliação pré e pós-operatória de cirurgias de retina.")
    ]
)

# Article 4649 — SaaS sales: Fleet management and telematics
art(
    slug="vendas-para-o-setor-de-saas-de-gestao-de-frotas-e-telematica",
    title="Vendas para o Setor de SaaS de Gestão de Frotas e Telemática",
    desc="Estratégias de vendas B2B para plataformas SaaS de gestão de frotas e telemática: como abordar gestores de logística, transportadoras e empresas de campo para fechar contratos.",
    h1="Vendas para o Setor de SaaS de Gestão de Frotas e Telemática",
    lead="Empresas com frotas de veículos — transportadoras, construtoras, utilities, distribuidoras — gastam fortunas em combustível, manutenção e acidentes evitáveis. Plataformas de gestão de frotas e telemática entregam ROI mensurável em semanas e têm ciclo de venda relativamente rápido quando o argumento financeiro está bem estruturado.",
    sections=[
        ("O Mercado de Fleet Management SaaS no Brasil",
         "O Brasil tem uma das maiores frotas de veículos comerciais do mundo — caminhões, vans, motos e veículos de passeio corporativos. O mercado de gestão de frotas inclui: rastreamento GPS em tempo real, telemática (telemetria de veículo — velocidade, RPM, frenagens bruscas, tempo de motor ligado), gestão de manutenção preventiva, controle de abastecimento e combustível, gestão de motoristas (jornada de trabalho, habilitação, treinamento), e roteirização e otimização de rotas. Players como Sascar, Veltec, Omnilink e soluções SaaS mais modernas competem com diferentes ênfases em rastreamento versus analytics."),
        ("O Decisor em Gestão de Frotas",
         "O decisor é o gerente de logística, o gerente de operações ou o diretor financeiro — dependendo do tamanho da frota e da empresa. Em transportadoras, o sócio-proprietário frequentemente toma a decisão diretamente. O gatilho de compra mais comum é um incidente recente (roubo de carga, acidente de trânsito, desvio de rota por motorista) ou uma análise de custo de combustível que revelou consumo acima do esperado. A abordagem de vendas mais eficaz começa pelo diagnóstico: 'Quantos veículos você tem? Qual o custo de combustível por mês? Você sabe quanto de combustível está sendo desperdiçado?' — as respostas constroem o business case."),
        ("ROI Mensurável e Proposta de Valor",
         "O ROI de plataformas de gestão de frotas é um dos mais mensuráveis no mercado B2B SaaS: redução de consumo de combustível de 10% a 20% por eliminação de marcha lenta excessiva, aceleração brusca e rotas ineficientes; redução de custo de manutenção por alertas preventivos que evitam quebras em rota; redução de sinistros de trânsito por monitoramento de comportamento do motorista; e recuperação de veículos roubados pelo rastreamento em tempo real. Uma frota de 50 caminhões que economiza R$200/mês por veículo em combustível gera R$120 mil/ano de economia — com payback da plataforma em semanas."),
        ("Ciclo de Venda e Instalação em Fleet SaaS",
         "O ciclo de venda é relativamente curto (2 a 6 semanas) para frotas menores, mas envolve um passo físico: a instalação do dispositivo de rastreamento no veículo. Parceiros instaladores certificados são parte do modelo de go-to-market — a plataforma vende e os instaladores credenciados fazem a instalação em todo o Brasil. O trial com instalação gratuita em 5 a 10 veículos por 30 dias é altamente eficaz — a empresa vê os dados de sua própria frota antes de pagar. Integrações com sistemas de TMS e ERP logístico aumentam o valor percebido e o switching cost."),
        ("Retenção e Expansão em Fleet Management",
         "A retenção em fleet management é alta: os dados históricos de telemática (comportamento de motoristas, histórico de manutenção, padrões de rota) têm valor crescente ao longo do tempo e são difíceis de migrar. A expansão acontece por adição de veículos conforme a frota cresce e por módulos adicionais (câmera de fadiga, gestão de abastecimento, roteirização avançada, integração com ERP). Empresas que crescem e expandem a frota geram expansão de receita natural — o NRR é estruturalmente alto nesse mercado.")
    ],
    faq_list=[
        ("Gestão de frotas reduz mesmo o consumo de combustível?",
         "Sim — estudos e dados de clientes consistentemente mostram redução de 10% a 25% no consumo de combustível após implementação de telemática. As alavancas são: eliminação de tempo de motor ocioso (veículo parado com motor ligado), correção de comportamento de aceleração e frenagem brusca (que aumentam o consumo), otimização de rotas para menor distância percorrida, e identificação de desvios não autorizados de rota."),
        ("Rastreamento de veículos é legal no Brasil?",
         "Sim — o rastreamento de veículos corporativos é legal quando os funcionários são informados sobre o monitoramento (cláusula no contrato de trabalho ou comunicado formal). A LGPD se aplica quando os dados de localização permitem identificar o motorista individualmente — o tratamento desses dados deve estar previsto na política de privacidade da empresa e ter base legal adequada (contrato de trabalho ou interesse legítimo do empregador)."),
        ("Qual é a diferença entre rastreamento GPS e telemática?",
         "Rastreamento GPS mostra a posição do veículo em tempo real — onde está, que rota fez, velocidade atual. Telemática vai além: coleta dados do veículo via OBD (diagnóstico a bordo) ou sensores dedicados — RPM, temperatura do motor, frenagens bruscas, tempo de aceleração, nível de combustível, erros mecânicos. Plataformas de telemática completa permitem análise de comportamento de motorista e manutenção preditiva baseada em dados reais do veículo.")
    ]
)

# Article 4650 — Consulting: Change management and organizational culture
art(
    slug="consultoria-de-gestao-da-mudanca-e-cultura-organizacional",
    title="Consultoria de Gestão da Mudança e Cultura Organizacional",
    desc="Como consultorias de gestão da mudança e cultura organizacional ajudam empresas a implementar transformações, reduzir resistência e construir culturas de alta performance.",
    h1="Consultoria de Gestão da Mudança e Cultura Organizacional",
    lead="Toda transformação organizacional — seja tecnológica, estratégica ou estrutural — falha ou tem sucesso dependendo de como as pessoas reagem à mudança. Consultorias de gestão da mudança e cultura organizacional estruturam o lado humano das transformações: comunicação, engajamento, desenvolvimento de lideranças e construção da cultura desejada.",
    sections=[
        ("Por Que a Gestão da Mudança é Crítica",
         "Estudos de gestão consistentemente mostram que 70% das transformações organizacionais não alcançam seus objetivos — e a causa dominante não é a estratégia ou a tecnologia, mas a resistência das pessoas à mudança. As raízes dessa resistência incluem: falta de comunicação clara sobre o porquê da mudança e o que muda para cada pessoa, percepção de perda de controle ou status, incerteza sobre competências necessárias na nova realidade, e falta de suporte da liderança intermediária que precisaria ser o principal agente da mudança. A consultoria de gestão da mudança estrutura intervenções específicas para cada uma dessas barreiras."),
        ("O Modelo ADKAR e Frameworks de Mudança",
         "O framework ADKAR (Awareness, Desire, Knowledge, Ability, Reinforcement) é um dos modelos mais utilizados para estruturar programas de gestão da mudança — cada letra representa uma condição que o indivíduo precisa atingir para adotar a mudança com sucesso. O modelo de Kotter (8 passos para liderar mudanças) é mais focado na organização como um todo — desde criar senso de urgência até ancorar mudanças na cultura. A consultoria escolhe o framework ou combina elementos conforme o tipo de mudança (tecnológica, estrutural, cultural) e o contexto organizacional, mas o trabalho real é na implementação prática — não na escolha do framework."),
        ("Diagnóstico de Cultura Organizacional",
         "O diagnóstico de cultura começa por entender a cultura atual — os valores, crenças e comportamentos que de fato governam o funcionamento da organização (que frequentemente diferem dos valores declarados nos murais). Ferramentas como pesquisas de clima, entrevistas qualitativas, focus groups e observação etnográfica mapeiam o estado atual. O gap entre a cultura atual e a cultura desejada pela liderança é o objeto de trabalho da consultoria. Culturas com alta distância hierárquica, aversão ao erro como punição e silos departamentais são os padrões mais comuns que impedem transformações e que exigem intervenções específicas."),
        ("Programas de Desenvolvimento de Liderança",
         "A liderança intermediária — gerentes e coordenadores — é o principal ponto de alavancagem em qualquer mudança cultural. São eles que traduzem a estratégia da diretoria em comportamento cotidiano das equipes, e são eles que mais resistem à mudança quando sentem ameaça ao seu status ou competência. Programas de desenvolvimento de liderança que combinam conteúdo (frameworks de liderança, comunicação, feedback, gestão de performance), prática supervisionada (coaching, simulações, grupos de aprendizagem entre pares) e accountability (metas de comportamento de liderança integradas ao processo de avaliação) são a intervenção mais impactante em transformações culturais."),
        ("Medindo Resultado em Cultura e Mudança",
         "A cultura é notoriamente difícil de medir — mas não impossível. Proxies quantitativos incluem: NPS de funcionários (eNPS), taxa de turnover voluntário (especialmente de high performers), absenteísmo, resultados de pesquisa de clima (por dimensão — autonomia, reconhecimento, comunicação, liderança), e indicadores de comportamento observável (frequência de feedback, uso de canais de comunicação, participação em iniciativas de melhoria). A consultoria define os indicadores de sucesso antes de começar, cria uma baseline e mede a evolução ao longo do programa — o que cria accountability real e diferencia consultorias sérias de consultores que entregam workshops e somem.")
    ],
    faq_list=[
        ("Gestão da mudança é diferente de RH?",
         "Gestão da mudança é uma disciplina focada em projetos específicos de transformação — uma implementação de ERP, uma reestruturação organizacional, uma fusão — com início, meio e fim. O RH opera de forma contínua gerenciando o ciclo de vida dos funcionários. Em grandes transformações, gestão da mudança e RH colaboram: o RH provê dados sobre a força de trabalho, gerencia os processos formais (desligamentos, redesenho de cargos), e a gestão da mudança cuida da comunicação, engajamento e adoção."),
        ("Qual é o ROI de um programa de cultura organizacional?",
         "O impacto financeiro de cultura é indireto mas mensurável: redução de turnover (o custo de substituir um funcionário é de 50% a 200% do seu salário anual), aumento de produtividade em equipes com alta confiança e psicologia segura, redução de absenteísmo, e aumento de NPS de clientes correlacionado com NPS de funcionários (empresas com funcionários mais engajados têm clientes mais satisfeitos). O McKinsey Global Institute estima que empresas com culturas de alta performance têm retorno ao acionista 60% superior ao longo de uma década."),
        ("Quanto tempo leva uma transformação cultural?",
         "Mudanças culturais genuínas levam de 2 a 5 anos — e esse horizonte precisa ser honestamente comunicado desde o início. Mudanças rápidas de 6 a 12 meses são possíveis em comportamentos específicos e observáveis (como práticas de feedback ou rituais de reunião), mas valores profundos e crenças implícitas mudam em ciclos mais longos. O risco é a ilusão de mudança — novos valores escritos na parede, workshop de cultura realizado, mas comportamentos reais inalterados.")
    ]
)

# Article 4651 — B2B SaaS: Real estate and property management
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-imobiliaria-e-administracao-de-imoveis",
    title="Gestão de Negócios de Empresa de B2B SaaS de Gestão Imobiliária e Administração de Imóveis",
    desc="Como estruturar e escalar uma empresa de B2B SaaS de gestão imobiliária e administração de imóveis: modelo de negócio, diferenciação, go-to-market e métricas de crescimento.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Gestão Imobiliária e Administração de Imóveis",
    lead="O mercado imobiliário brasileiro movimenta trilhões de reais em aluguéis, vendas e incorporações. Imobiliárias, administradoras de condomínios, incorporadoras e investidores de fundos imobiliários precisam de tecnologia para operar com eficiência em um setor ainda amplamente manual e fragmentado.",
    sections=[
        ("O Mercado de PropTech e Real Estate SaaS no Brasil",
         "O mercado de PropTech (Property Technology) no Brasil inclui: CRM para imobiliárias (gestão de leads, pipeline de vendas e locações), portais de listagem (Zap Imóveis, VivaReal, OLX), gestão de contratos e locações (com boleto automático, reajuste de IGP-M/IPCA, vistoria digital), administração de condomínios (arrecadação, assembleias digitais, comunicação com moradores), gestão de obras e incorporações (cronograma, contratos com construtoras, gestão de entregas), e plataformas de investimento imobiliário fracionado (fundos de CRI, LCI, crowdfunding imobiliário). O setor tem maturidade digital baixa — ainda há muitas imobiliárias e administradoras rodando em planilhas."),
        ("Diferenciação em Real Estate SaaS",
         "Os diferenciadores mais relevantes incluem: integração nativa com os portais de listagem (para publicar imóveis em todos os portais com um clique), assinatura eletrônica de contratos de locação e venda (eliminando a necessidade de presença física para assinar), automação de cobrança de aluguel (boleto automático, PIX, gestão de inadimplência), vistoria digital do imóvel (com fotos, descrição de condições e assinatura digital), e integração com sistemas de garantia locatícia (fiança, título de capitalização, seguro fiança). Para administradoras de condomínio, a comunicação com moradores via aplicativo (reserva de espaços, comunicados, chamados de manutenção) é diferencial de adoção alto."),
        ("Modelo de Receita em Imob SaaS",
         "O modelo predominante combina mensalidade por usuário ou por número de imóveis administrados. Imobiliárias pequenas (até 50 imóveis em carteira) pagam de R$150 a R$400/mês; administradoras de porte médio (200 a 500 imóveis) pagam de R$800 a R$2.000/mês. Portais de listagem cobram por anúncio publicado ou por mensalidade de acesso. Para administradoras de condomínio, o modelo por número de unidades (de R$5 a R$15 por unidade/mês) cria receita proporcional ao tamanho do condomínio gerenciado. Serviços adjacentes como seguro fiança integrado (com comissionamento) e assessoria jurídica para inadimplência são fontes adicionais de receita."),
        ("Go-to-Market: Imobiliárias, Administradoras e Incorporadoras",
         "Os segmentos têm perfis de compra distintos: imobiliárias são pequenas e numerosas (o comprador é o dono da imobiliária, decisão rápida, sensível ao preço), administradoras de condomínio têm ticket maior e ciclo mais longo (envolve aprovação em assembleia de síndicos), e incorporadoras são grandes contas com ciclo de venda longo e exigências de integração e customização. CRECI (Conselho Regional de Corretores de Imóveis) e associações de classe imobiliária (Secovi, ABADI) são canais de acesso privilegiado. Parceria com contabilidades especializadas em gestão de imóveis e administradoras é canal de indicação eficiente."),
        ("Métricas de Saúde do Negócio em PropTech SaaS",
         "As métricas prioritárias incluem número de imóveis gerenciados pela plataforma (o principal indicador de escala e switching cost), GMV de aluguéis processados mensalmente, taxa de inadimplência dos contratos da carteira (indicador de qualidade da base de clientes), NPS de imobiliárias e administradoras usuárias, e NRR. O churn em imobiliárias é moderado — a migração de carteira de imóveis (contratos, histórico de pagamentos, documentos) é trabalhosa mas factível. Retenção é impulsionada pela profundidade de uso da plataforma: quanto mais funcionalidades o cliente usa, mais custoso é migrar.")
    ],
    faq_list=[
        ("O que é garantia locatícia e quais as opções disponíveis?",
         "Garantia locatícia é o instrumento que protege o proprietário no caso de inadimplência do inquilino. As modalidades mais comuns são: fiador (pessoa física que se responsabiliza pela dívida), caução (depósito de 1 a 3 meses de aluguel em conta vinculada), título de capitalização (o inquilino compra um título que funciona como caução com possibilidade de resgate), e seguro fiança (o inquilino paga uma apólice que garante o pagamento ao proprietário). A tendência é a substituição da fiança pessoal por garantias financeiras mais ágeis."),
        ("Como a tecnologia muda o processo de locação?",
         "A tecnologia digitaliza todo o funil: anúncio em múltiplos portais com um clique, tour virtual 3D, análise de crédito digital integrada (score, consulta de restrições, comprovação de renda via open finance), contrato de locação com assinatura eletrônica ICP-Brasil, vistoria de entrada com fotos e descrição registradas digitalmente, cobrança automática de aluguel via boleto ou PIX, e gestão de manutenção via chamado no aplicativo do morador. O processo que levava semanas de ida e vinda em papel passa a acontecer em dias ou horas."),
        ("Administradora de condomínio precisa de software específico?",
         "Sim — software de gestão de condomínio especializado resolve problemas específicos: geração automática de boletos de condomínio com rateio por fração ideal ou cotas iguais, controle de inadimplência de condôminos, gestão de prestadores de serviço e contratos de manutenção, organização de assembleias digitais com votação registrada, e comunicação com moradores via aplicativo. Excel e sistemas genéricos não atendem essas necessidades com segurança — o risco de erros em arrecadação e de problemas em assembleias é alto sem ferramenta adequada.")
    ]
)

# Article 4652 — Clinic: Dermatology and aesthetics
art(
    slug="gestao-de-clinicas-de-dermatologia-e-estetica-medica",
    title="Gestão de Clínicas de Dermatologia e Estética Médica",
    desc="Guia de gestão para clínicas de dermatologia e estética médica: organização do fluxo clínico e estético, gestão de procedimentos, marketing e indicadores de performance.",
    h1="Gestão de Clínicas de Dermatologia e Estética Médica",
    lead="A dermatologia combina medicina de alta complexidade — câncer de pele, psoríase, dermatoses imunológicas — com procedimentos estéticos de alta demanda e ticket elevado. Clínicas que estruturam bem os dois fluxos capturam mercado crescente e constroem receita diversificada e resiliente.",
    sections=[
        ("Abrangência da Dermatologia Clínica e Estética",
         "A dermatologia clínica trata: câncer de pele (melanoma, carcinoma basocelular e espinocelular — o Brasil tem alta incidência por radiação UV intensa), acne (condição de altíssima prevalência em adolescentes e adultos), psoríase e eczema (doenças crônicas com necessidade de acompanhamento contínuo), infecções cutâneas (fungos, herpes, impetigo), urticária e dermatites de contato, e doenças do cabelo e couro cabeludo (alopecia androgenética, tricotilomania, dermatite seborreica). A dermatologia estética inclui aplicação de toxina botulínica, preenchimentos com ácido hialurônico, peelings químicos, laser e luz intensa pulsada, bioestimuladores de colágeno e tratamentos para manchas e envelhecimento cutâneo."),
        ("A Dupla Receita: Clínico e Estético",
         "A clínica de dermatologia que atende tanto dermatologia clínica quanto estética tem estrutura de receita mais resiliente: a dermatologia clínica gera fluxo constante de atendimento pelo plano de saúde com ticket menor mas volume alto; a dermatologia estética gera procedimentos particulares de ticket alto (R$500 a R$3.000 por procedimento) com margem superior. A dermatologia clínica alimenta a estética — pacientes que vêm tratar acne, manchas ou câncer de pele frequentemente tornam-se clientes de procedimentos estéticos da mesma médica em quem confiam. A gestão de agendas separadas (plano versus particular) com precificação clara é essencial para otimizar o mix de receita."),
        ("Equipamentos Estéticos: Investimento e Retorno",
         "Equipamentos de laser (CO2 fracionado, Nd:YAG, diodo para fotodepilação), luz intensa pulsada (IPL), radiofrequência, ultrassom microfocado (HIFU) e equipamentos de criolipolise representam investimentos de R$80 mil a R$500 mil por equipamento. O retorno é calculado pelo volume de procedimentos necessários para pagar o equipamento: um laser CO2 fracionado a R$200 mil pago em 24 meses precisa gerar R$8.300/mês acima do custo operacional — o que corresponde a aproximadamente 8 a 12 sessões mensais ao preço de mercado. O leasing de equipamentos é alternativa ao investimento à vista — reduz o CAPEX inicial mas eleva o custo fixo mensal."),
        ("Marketing em Dermatologia e Estética",
         "O CFM (Conselho Federal de Medicina) regula a publicidade médica — antes e depois de procedimentos, garantias de resultado e depoimentos de pacientes são proibidos para médicos. Dentro dessas restrições, conteúdo educativo funciona muito bem: informações sobre cuidados com a pele, proteção solar, identificação de câncer de pele, tipos de procedimentos e o que esperar de cada um. Instagram e YouTube com conteúdo dermatológico de qualidade constroem autoridade e atraem público interessado. SEO local para 'dermatologista [cidade]', 'tratamento de manchas [cidade]' e 'botox [cidade]' captura intenção de busca direta. Programas de fidelidade para procedimentos estéticos recorrentes (toxina botulínica a cada 4 a 6 meses, peelings mensais) criam receita previsível."),
        ("Indicadores de Performance em Dermatologia",
         "As métricas clínicas incluem taxa de identificação de câncer de pele em estágio inicial (indicador de qualidade do rastreamento), NPS de pacientes e taxa de aderência ao seguimento em condições crônicas. As métricas de negócio incluem receita por tipo de procedimento estético (para otimizar mix de equipamentos e capacitações), taxa de recorrência de pacientes estéticos (frequência de retorno), ticket médio por atendimento estético, e taxa de conversão de consulta clínica para procedimento estético. A gestão do ciclo de retorno para manutenção de procedimentos estéticos — toxina botulínica, preenchimento, peelings — é o principal driver de receita recorrente na estética médica.")
    ],
    faq_list=[
        ("Com que frequência devo ir ao dermatologista?",
         "A recomendação padrão é uma consulta anual para avaliação de toda a pele (mapeamento de pintas e lesões) para adultos sem fatores de risco. Pessoas com histórico pessoal ou familiar de câncer de pele, pele muito clara, histórico de queimaduras solares ou uso de imunossupressores devem consultar com frequência maior (a cada 6 meses). Quem usa protetor solar diariamente e evita exposição solar sem proteção tem menor risco, mas não dispensa o acompanhamento regular."),
        ("Toxina botulínica tem efeitos permanentes?",
         "Não — o efeito da toxina botulínica é temporário, durando de 3 a 6 meses dependendo da área tratada, dose e metabolismo individual. Após esse período, a musculatura retorna à função normal e as rugas de expressão voltam gradualmente. A aplicação regular ao longo de anos pode ter efeito preventivo sobre rugas permanentes — a musculatura menos contraída ao longo do tempo previne rugas estáticas mais profundas."),
        ("Como identificar câncer de pele?",
         "A regra ABCDE do melanoma: A (assimetria — a lesão tem formato irregular), B (borda irregular ou mal definida), C (cor heterogênea — manchas dentro da lesão), D (diâmetro maior que 6 mm), E (evolução — crescimento, mudança de cor ou sangramento recente). Qualquer lesão nova, que cresce ou muda deve ser avaliada por dermatologista. O diagnóstico definitivo é feito por dermatoscopia e, quando indicado, biópsia.")
    ]
)

# Article 4653 — SaaS sales: Legal tech and contract management
art(
    slug="vendas-para-o-setor-de-saas-de-legaltech-e-gestao-de-contratos",
    title="Vendas para o Setor de SaaS de LegalTech e Gestão de Contratos",
    desc="Estratégias de vendas B2B para plataformas SaaS de legaltech e gestão de contratos: como abordar departamentos jurídicos, escritórios de advocacia e compliance para fechar contratos.",
    h1="Vendas para o Setor de SaaS de LegalTech e Gestão de Contratos",
    lead="O mercado jurídico brasileiro é um dos maiores do mundo em número de advogados e volume de litígios. Plataformas de legaltech atendem desde automação de contratos e gestão de processos judiciais até due diligence com IA. Vender para o jurídico exige credibilidade, paciência e entendimento das especificidades do setor.",
    sections=[
        ("O Mercado de LegalTech no Brasil",
         "O mercado brasileiro de legaltech inclui: automação de contratos e documentos jurídicos (geradores de cláusulas, templates inteligentes), gestão de processos judiciais (acompanhamento de publicações do Diário Oficial, prazos processuais, controle de audiências), plataformas de assinatura eletrônica qualificada (com certificado ICP-Brasil — requisito em alguns atos jurídicos formais), gestão de contratos corporativos (repositório, vencimentos, obrigações, renovações), due diligence e revisão de documentos com IA, e plataformas de ODR (Online Dispute Resolution) para mediação e arbitragem digital. O CFJ (Conselho Federal de Justiça) e os portais de tribunais são fontes de integração obrigatória para ferramentas de acompanhamento processual."),
        ("O Decisor Jurídico: Advogados e Gestores de Jurídico",
         "O comprador varia por segmento: em escritórios de advocacia, o sócio-gestor é o decisor — conservador, focado em produtividade da equipe e risco de segredos de negócio. Em departamentos jurídicos corporativos, é o General Counsel ou diretor jurídico, com preocupação com LGPD, conformidade regulatória e integração com sistemas corporativos. Em startups e PMEs sem jurídico interno, é o CEO ou CFO buscando reduzir dependência de consultoria externa para contratos padrão. O jurídico é notoriamente avesso a risco — vende-se segurança (dados protegidos, contratos válidos, prazos não perdidos) antes de eficiência."),
        ("Proposta de Valor em LegalTech",
         "Os argumentos centrais incluem: redução de risco por não perder prazos processuais críticos (uma intimação não respondida pode gerar sentença desfavorável em revelia), automação de tarefas repetitivas que consomem tempo de advogados qualificados (geração de contratos padrão, preenchimento de petições, pesquisa de jurisprudência), visibilidade do portfólio de contratos (vencimentos que passam despercebidos, obrigações não cumpridas, renovações automáticas indesejadas), e conformidade com LGPD em contratos com fornecedores e clientes (inventário de dados pessoais nos contratos). O ROI é calculado em horas de advogado economizadas e em riscos evitados."),
        ("Ciclo de Venda e Conformidade no LegalTech",
         "O ciclo de venda é longo (2 a 6 meses para jurídicos corporativos) e envolve revisão técnica da segurança e privacidade da plataforma — a due diligence reversa pelo próprio cliente jurídico. Certificações como ISO 27001, SOC 2 e conformidade LGPD são pré-requisitos para contratar com grandes jurídicos corporativos. Trials com dados fictícios (não dados reais de clientes) são a forma mais comum de POC — o advogado não quer seus dados em uma plataforma desconhecida antes de assinar um NDA. Referências de escritórios de grande porte ou departamentos jurídicos conhecidos são diferenciais decisivos."),
        ("Retenção e Expansão em LegalTech SaaS",
         "A retenção em plataformas de gestão de contratos é naturalmente alta: o repositório de contratos históricos, os alertas de vencimento configurados e os workflows de aprovação construídos criam dependência operacional. A expansão acontece por novos usuários (mais advogados ou áreas da empresa), por módulos adicionais (de gestão de contratos para automação de documentos, de automação para due diligence com IA), e por integração com mais sistemas do cliente (ERP, CRM, ferramentas de assinatura). O churn é impulsionado pela troca de General Counsel — o novo gestor jurídico frequentemente quer avaliar as ferramentas do zero.")
    ],
    faq_list=[
        ("Assinatura eletrônica tem validade em contratos comerciais?",
         "Sim — a MP 2.200-2/2001 e a Lei 14.063/2020 garantem validade jurídica a documentos assinados eletronicamente no Brasil. Assinatura qualificada (com certificado digital ICP-Brasil) tem validade equivalente à assinatura manuscrita para qualquer ato jurídico. Assinatura simples (por email ou clique) é válida para contratos comerciais privados e é aceita pela maioria dos tribunais quando há evidência de autoria e integridade do documento."),
        ("O que é automação de contratos e quando usar?",
         "Automação de contratos usa templates com campos variáveis que são preenchidos automaticamente a partir de dados do cliente ou de um formulário — gerando um contrato personalizado em segundos em vez de horas de edição manual. Funciona bem para contratos de alto volume com estrutura padronizada (contratos de prestação de serviço, NDAs, contratos de locação). Não substitui a revisão jurídica em contratos complexos e negociados individualmente."),
        ("LGPD impacta a gestão de contratos?",
         "Sim — contratos frequentemente contêm dados pessoais de pessoas físicas (nome, CPF, endereço, dados bancários de sócios e representantes). A LGPD exige que esses dados sejam tratados com base legal adequada, armazenados com segurança e descartados quando não mais necessários. Plataformas de gestão de contratos conformes com LGPD devem ter controle de acesso por usuário, criptografia de documentos em repouso, log de acesso e política de retenção configurável.")
    ]
)

# Article 4654 — Consulting: Compensation and HR strategy
art(
    slug="consultoria-de-remuneracao-e-estrategia-de-pessoas",
    title="Consultoria de Remuneração e Estratégia de Pessoas",
    desc="Como consultorias de remuneração e estratégia de pessoas ajudam empresas a estruturar planos de cargos, salários e benefícios competitivos para atrair e reter talentos.",
    h1="Consultoria de Remuneração e Estratégia de Pessoas",
    lead="Remuneração inadequada é a primeira causa de desligamento voluntário de talentos. Consultorias de remuneração e estratégia de pessoas ajudam empresas a estruturar planos de cargos e salários competitivos, desenhar programas de incentivo de curto e longo prazo, e criar a estratégia de pessoas que suporta os objetivos de negócio.",
    sections=[
        ("Por Que a Estratégia de Remuneração Importa",
         "Remuneração abaixo do mercado gera turnover alto de talentos críticos — o que tem custo direto (recrutamento, onboarding, perda de produtividade no período de ramp-up) e custo indireto (conhecimento perdido, projetos atrasados, desgaste da equipe remanescente). Remuneração acima do mercado sem critério degrada a rentabilidade e cria iniquidade interna percebida. A consultoria de remuneração usa pesquisas salariais de mercado (Mercer, Towers Watson, Catho, Glassdoor, GPTW) para posicionar cada cargo em relação ao mercado e criar faixas salariais que equilibrem competitividade e sustentabilidade financeira."),
        ("Estrutura de Cargos e Salários",
         "A estrutura de cargos e salários organiza todos os cargos da empresa em uma hierarquia de complexidade e responsabilidade — cada cargo tem um nível (que determina sua faixa salarial) baseado em critérios como escopo de responsabilidade, impacto no negócio, complexidade de decisão e nível de autonomia. A consultoria utiliza metodologias de avaliação de cargos (Hay, Mercer, ou metodologia proprietária) para garantir equidade interna — que cargos de mesma complexidade tenham faixas salariais equivalentes, independente de departamento. O resultado é um plano de cargos e salários que serve de base para decisões de promoção, reajuste e admissão."),
        ("Remuneração Variável e Incentivos de Curto Prazo",
         "Remuneração variável inclui bônus por resultado (baseado em metas individuais, de time ou da empresa), participação nos lucros (PLR — Participação nos Lucros e Resultados, com regras específicas para dedução tributária), comissão de vendas, e prêmios por projetos ou objetivos específicos. O design do plano de incentivo é crítico: métricas mal escolhidas criam comportamentos indesejados (vendedor que prioriza volume sobre margem, por exemplo). A consultoria desenha o plano com métricas alinhadas à estratégia, metas calibradas para serem desafiadoras mas atingíveis (para motivar sem frustrar), e comunicação clara das regras."),
        ("Stock Options, Phantom Shares e Incentivos de Longo Prazo",
         "Incentivos de longo prazo (ILP) — stock options, ações restritas, phantom shares, participação societária — são usados para reter talentos estratégicos com horizonte de permanência de 3 a 5 anos e para alinhar os interesses dos executivos com a criação de valor para o acionista. Em startups e scale-ups, stock options são componente essencial do pacote de compensação para competir com salários de grandes empresas. A consultoria estrutura o plano de ILP com regras de vesting (maturação do direito ao longo do tempo), cliff (período mínimo antes de qualquer vesting), gatilhos de aceleração e tratamento tributário adequado para minimizar a carga fiscal do beneficiário."),
        ("Estratégia de Pessoas Integrada ao Negócio",
         "A estratégia de pessoas vai além da remuneração: inclui o planejamento de força de trabalho (quais capacidades o negócio vai precisar em 2 a 3 anos?), a estratégia de recrutamento e seleção para cada perfil crítico, os programas de desenvolvimento de competências técnicas e de liderança, a gestão de performance (ciclos de avaliação, feedback, planos de desenvolvimento individual), e a estratégia de clima e engajamento. A consultoria de pessoas ajuda a empresa a ter uma visão integrada e coerente dessas dimensões — em vez de iniciativas de RH desconectadas que não se reforçam mutuamente.")
    ],
    faq_list=[
        ("Como saber se os salários da minha empresa estão competitivos?",
         "Compare com pesquisas salariais de mercado por função, nível hierárquico e setor. Fontes confiáveis incluem pesquisas da Mercer, Towers Watson, Catho Carreira e Salários, Glassdoor e GPTW. Compare o posicionamento da empresa em relação à mediana do mercado (P50) e ao P75 (as empresas que mais pagam). Uma empresa que quer atrair os melhores talentos precisa pagar acima da mediana — geralmente entre P50 e P75 para cargos críticos."),
        ("O que é PLR e como estruturá-la corretamente?",
         "PLR (Participação nos Lucros e Resultados) é um programa de remuneração variável regulado pela Lei 10.101/2000, que permite pagar valores adicionais ao salário com dedução tributária para a empresa (desde que negociado com o sindicato ou comissão de funcionários). Para ser dedutível, a PLR deve ter regras previamente negociadas, metas objetivas mensuráveis e periodicidade máxima semestral (no máximo dois pagamentos por ano). PLR bem estruturada motiva funcionários, alinha interesses com resultado da empresa e reduz a carga tributária sobre remuneração."),
        ("Stock option é melhor que salário mais alto?",
         "Depende do perfil do profissional e do estágio da empresa. Para profissionais que acreditam no potencial de valorização da empresa e podem assumir risco, stock options com upside significativo podem ser mais atraentes do que salário incrementalmente maior. Para profissionais com compromissos financeiros que priorizam estabilidade, salário competitivo é mais importante. O melhor pacote combina salário acima da mediana do mercado com stock options que complementam sem substituir a remuneração base.")
    ]
)

# ── Sitemap & trilha updates ──────────────────────────────────────────────────
root = pathlib.Path(__file__).parent
slugs = [
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-apis-e-plataformas-para-desenvolvedores", "Gestão de Negócios de Empresa de B2B SaaS de Gestão de APIs e Plataformas para Desenvolvedores"),
    ("gestao-de-clinicas-de-oftalmologia-e-cirurgia-refrativa", "Gestão de Clínicas de Oftalmologia e Cirurgia Refrativa"),
    ("vendas-para-o-setor-de-saas-de-gestao-de-frotas-e-telematica", "Vendas para o Setor de SaaS de Gestão de Frotas e Telemática"),
    ("consultoria-de-gestao-da-mudanca-e-cultura-organizacional", "Consultoria de Gestão da Mudança e Cultura Organizacional"),
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-imobiliaria-e-administracao-de-imoveis", "Gestão de Negócios de Empresa de B2B SaaS de Gestão Imobiliária e Administração de Imóveis"),
    ("gestao-de-clinicas-de-dermatologia-e-estetica-medica", "Gestão de Clínicas de Dermatologia e Estética Médica"),
    ("vendas-para-o-setor-de-saas-de-legaltech-e-gestao-de-contratos", "Vendas para o Setor de SaaS de LegalTech e Gestão de Contratos"),
    ("consultoria-de-remuneracao-e-estrategia-de-pessoas", "Consultoria de Remuneração e Estratégia de Pessoas"),
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

print("Done — batch 1582")
