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

# ── Article 4975 ── B2B SaaS: gestão de despesas e viagens corporativas
art(
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-despesas-e-viagens-corporativas",
    "Gestão de Negócios de Empresa de B2B SaaS de Gestão de Despesas e Viagens Corporativas | ProdutoVivo",
    "Como construir e escalar um B2B SaaS de gestão de despesas e viagens corporativas. Estratégias de produto, go-to-market e diferenciação no mercado de T&E.",
    "Como Escalar um B2B SaaS de Gestão de Despesas e Viagens Corporativas",
    "Gestão de despesas e viagens corporativas (T&E — Travel & Expense) é um segmento de SaaS B2B com alta recorrência e baixo churn — uma vez integrado ao processo financeiro da empresa, é difícil de trocar. O problema é universal: funcionários guardam nota fiscal em papel, preenchem planilhas de reembolso manualmente, o financeiro reprocessa tudo, e o gestor não tem visibilidade do gasto em tempo real. É um processo doloroso que toda empresa com mais de 20 funcionários quer automatizar.",
    [
        ("O ciclo de despesas corporativas e onde o SaaS atua",
         "O ciclo completo de T&E começa na política de despesas (o que pode gastar, em quais categorias, com quais limites), passa pela solicitação de adiantamento, pela realização da despesa (voo, hotel, refeição, táxi), pelo registro da nota fiscal ou cupom, pela aprovação do gestor, pelo processamento financeiro (validação da NF, lançamento contábil, integração com ERP), e pelo reembolso ao funcionário. SaaS de despesas automatiza tudo isso — o funcionário tira foto da nota pelo app, o sistema lê o OCR e preenche os campos automaticamente, o gestor aprova pelo celular, e o financeiro recebe os dados já organizados."),
        ("Cartão corporativo + plataforma de despesas: o modelo integrado",
         "O modelo mais avançado combina cartão corporativo (físico ou virtual) com plataforma de despesas — cada transação no cartão cria automaticamente um lançamento na plataforma, o funcionário só precisa anexar a nota fiscal correspondente. Elimina quase todo o preenchimento manual e os adiantamentos em dinheiro. Empresas de cartão corporativo com plataforma integrada (como Swile, Flash, Conta Simples) competem com SaaS puro de despesas. Para um SaaS de despesas sem cartão próprio, parceria com emissor de cartão corporativo é o diferencial de integração."),
        ("Política de despesas: o coração da gestão de T&E",
         "Política de despesas define as regras que o sistema vai automaticamente verificar — limite de diária de hotel por cidade, teto de refeição por tipo de viagem, requer aprovação prévia para passagens acima de X reais, categorias permitidas por nível de colaborador. SaaS que permite configurar políticas granulares e aplica automaticamente (bloqueando ou sinalizando despesas fora da política) economiza horas do financeiro na revisão manual. Empresas que formalizam a política de despesas pela primeira vez via SaaS veem redução de 15 a 30% nos gastos de T&E."),
        ("Integrações críticas para SaaS de despesas",
         "ERP financeiro (SAP, Totvs, CIGAM, Omie) para lançamento automático das despesas aprovadas na contabilidade é a integração mais crítica — sem ela, o financeiro precisa redigitar. Integração com plataformas de viagens corporativas (ViajaNet Corporate, BCD Travel, Consulmark) para associar despesa ao pedido de viagem automaticamente. Leitura de NF-e via NF-e da SEFAZ ou DANFE/XML importado pelo funcionário. Exportação de relatórios no formato de cada banco para conciliação de cartão corporativo. Cada integração nativa elimina um processo manual do financeiro."),
        ("Go-to-market para SaaS de despesas corporativas",
         "CFOs, controllers e diretores financeiros de empresas com 50+ funcionários e times de campo (vendedores, técnicos, consultores) são os compradores-alvo. O processo de compra é bottom-up: funcionários reclamam do processo de reembolso → gestor escala para o financeiro → financeiro busca solução. Demo deve mostrar o antes e depois do processo — a foto da nota via app vs. a planilha do Excel. Parcerias com consultorias de processos financeiros e contadores são canais de indicação de alta qualidade."),
    ],
    [
        ("SaaS de despesas funciona para autônomos e MEIs?",
         "Para autônomos e MEIs, o controle de despesas é mais simples — geralmente querem registrar despesas do negócio para cálculo de imposto de renda (dedução de despesas operacionais). Aplicativos de controle financeiro pessoal/profissional (como Conta Azul, Nibo) atendem esse perfil com funcionalidades mais simples e preço menor. SaaS corporativo de T&E é adequado a partir de empresas com 15 a 20 funcionários que têm processo de reembolso estruturado. Para a faixa intermediária (5 a 15 funcionários), planos básicos com funcionalidade suficiente a preço acessível são o ideal."),
        ("Como o SaaS de despesas ajuda no compliance tributário?",
         "Despesas corporativas têm implicações tributárias — despesas sem nota fiscal não são dedutíveis do IRPJ/CSLL, e algumas despesas (como brindes e representação) têm tratamento específico. SaaS de despesas que exige nota fiscal para cada lançamento, categoriza corretamente para o plano de contas e exporta no formato do SPED Contábil garante que as despesas estejam documentadas e categorizadas corretamente para fins fiscais. Em uma auditoria da Receita Federal, o histórico digital de despesas com notas fiscais digitalizadas é muito mais robusto do que papeis em arquivo."),
        ("Qual o prazo típico para aprovação de reembolso com SaaS de despesas?",
         "Com SaaS de despesas bem implementado, o ciclo típico é: funcionário registra a despesa no app no mesmo dia → gestor recebe notificação e aprova em 1 a 2 dias úteis → financeiro processa em 1 a 2 dias → reembolso realizado em 1 a 3 dias úteis. Total: 3 a 7 dias úteis. Sem SaaS, o ciclo de reembolso em muitas empresas leva 15 a 30 dias — o funcionário aguarda a reunião mensal de fechamento para submeter a planilha. A redução de 20+ dias para menos de 1 semana é o argumento de employee experience mais poderoso."),
    ]
)

# ── Article 4976 ── Clinics: medicina de família e comunidade
art(
    "gestao-de-clinicas-de-medicina-de-familia-e-comunidade",
    "Gestão de Clínicas de Medicina de Família e Comunidade | ProdutoVivo",
    "Guia de gestão para clínicas de medicina de família e atenção primária à saúde: estrutura, longitudinalidade, faturamento e crescimento.",
    "Gestão de Clínicas de Medicina de Família: Como Construir um Modelo de Atenção Primária de Excelência",
    "Medicina de família e comunidade é a especialidade da atenção primária à saúde — o médico que cuida da família inteira ao longo do tempo, resolve os problemas mais comuns e coordena o cuidado com especialistas quando necessário. No setor privado, o crescimento de clínicas de medicina de família como alternativa às consultas de pronto-socorro e à fragmentação do cuidado especializado é uma das tendências mais importantes da saúde suplementar.",
    [
        ("O modelo de medicina de família no setor privado",
         "Medicina de família privada opera em dois modelos principais: clínicas de atenção primária com foco em longitudinalidade (o mesmo médico cuida dos mesmos pacientes ao longo do tempo, conhecendo o histórico completo) e medicina de concierge ou Direct Primary Care (DPC), onde o paciente paga uma mensalidade direta ao médico por acesso ilimitado e atendimento personalizado. O modelo de concierge é crescente no Brasil — médicos de família com 300 a 600 pacientes (vs. 2.000 a 3.000 no modelo convencional) que entregam atendimento de qualidade superior.",
         ),
        ("Longitudinalidade: o diferencial da especialidade",
         "Longitudinalidade é o cuidado contínuo ao longo do tempo — o médico de família conhece o paciente, sua história clínica, sua família, seus fatores de risco e suas preferências. Isso permite diagnósticos mais precisos (o médico percebe quando algo mudou), tratamentos mais aderentes (confiança no médico aumenta adesão) e prevenção mais eficaz (rastreamento de doenças crônicas, vacinação em dia, exames preventivos). Clínicas que constroem uma base de pacientes longitudinal têm churn muito menor e NPS muito maior do que as que atendem por consulta avulsa.",
         ),
        ("Gestão de agenda e prevenção em medicina de família",
         "Agenda de médico de família tem formato diferente de especialistas — consultas mais longas (20 a 30 minutos vs. 10 a 15 em especialidades), espaços para urgências do dia e mix de consultas de rotina e follow-up. Programa de saúde preventiva estruturado — rastreamento de câncer (mama, colo, cólon), diabetes, hipertensão, dislipidemia e depressão para todos os pacientes em faixas de risco — gera uma agenda programática que combina com as consultas demandadas espontaneamente. Pacientes em programa preventivo consultam mais frequentemente e têm maior LTV.",
         ),
        ("Faturamento em medicina de família",
         "Convênios remuneram mal a consulta de clínica médica/medicina de família — um dos menores tickets da tabela TUSS. Por isso, clínicas privadas de medicina de família frequentemente adotam: (1) modelo de assinatura mensal (R$ 200 a R$ 800/família/mês para acesso ilimitado ou um número definido de consultas), (2) combinação de convênio com consultas particulares de maior valor, ou (3) DPC (Direct Primary Care) sem convênio, com mensalidade direta ao médico. O modelo de assinatura tem MRR previsível e permite escalar a clínica de forma sustentável.",
         ),
        ("Marketing para clínicas de medicina de família",
         "A proposta de valor da medicina de família é contraintuitiva em um mercado acostumado a especialistas — educar o paciente sobre os benefícios do médico de referência é o trabalho de marketing central. Conteúdo sobre medicina preventiva, rastreamento de doenças crônicas, quando vai ao especialista vs. quando o médico de família resolve, e depoimentos de pacientes com histórico de cuidado de longo prazo são os formatos de maior conversão. Empresas que buscam benefícios de saúde diferenciados para colaboradores são um canal B2B promissor para clínicas de medicina de família.",
         ),
    ],
    [
        ("Médico de família pode substituir os especialistas?",
         "Não substitui, mas reduz a necessidade desnecessária de especialista. Estudos mostram que 70 a 80% dos problemas de saúde podem ser resolvidos pelo médico de família sem encaminhamento. Quando o encaminhamento é necessário, o médico de família coordena o cuidado — faz o resumo clínico, escolhe o especialista certo, acompanha o resultado e integra o tratamento especializado ao plano de cuidado geral do paciente. O especialista trata a doença específica; o médico de família cuida da pessoa inteira.",
         ),
        ("Direct Primary Care funciona no Brasil?",
         "DPC (Direct Primary Care) é um modelo onde o paciente paga diretamente ao médico uma mensalidade (R$ 150 a R$ 500/mês) por acesso ilimitado a consultas, comunicação por WhatsApp/telefone e exames básicos incluídos — sem intermediação de plano de saúde. No Brasil, o modelo ainda é incipiente mas crescente, especialmente em grandes centros. A ANVISA e o CFM não proíbem o modelo para pessoas físicas. A principal barreira é a cultura do plano de saúde — muitos pacientes não entendem por que pagar mensalidade para um médico se já têm convênio.",
         ),
        ("Medicina de família e urgência são incompatíveis?",
         "Não são incompatíveis, mas a ênfase é diferente. O médico de família resolve a maioria das urgências de baixa complexidade dos próprios pacientes — uma das vantagens do modelo é o acesso rápido quando algo acontece, com um médico que conhece o histórico. Para urgências graves (infarto, AVC, trauma) e urgências de pacientes sem médico de família, o pronto-socorro é indispensável. Clínicas de medicina de família com esquema de plantão (pelo menos telefônico ou de telemedicina) para urgências dos pacientes cadastrados têm NPS significativamente superior.",
         ),
    ]
)

# ── Article 4977 ── SaaS Sales: clínicas estéticas e spas
art(
    "vendas-para-o-setor-de-saas-de-clinicas-esteticas-e-spas",
    "Vendas para o Setor de SaaS de Clínicas Estéticas e Spas | ProdutoVivo",
    "Como vender SaaS para clínicas estéticas e spas no Brasil. Estratégias de prospecção, demonstração e fechamento no setor de beleza e bem-estar.",
    "Como Vender SaaS para Clínicas Estéticas e Spas",
    "O mercado de estética e bem-estar no Brasil é um dos maiores do mundo — clínicas estéticas, day spas, spas corporativos, centros de estética médica e clínicas de medicina estética são dezenas de milhares de estabelecimentos com necessidades específicas de SaaS: agendamento online, gestão de protocolos, controle de estoque de insumos e fidelização de clientes. O diferencial das clínicas estéticas é a experiência do cliente — e o SaaS que melhora essa experiência vende mais.",
    [
        ("O perfil do comprador de clínicas estéticas",
         "Dono de clínica estética no Brasil é tipicamente uma esteticista ou médica esteta que empreendeu — tem profundo conhecimento dos tratamentos mas frequentemente menos experiência com gestão. Valoriza software que seja fácil de usar, que melhore a experiência do cliente e que ajude a fidelizar. O ticket médio de clínica estética é R$ 200 a R$ 800 por sessão, com série de sessões (laser, sculptra, skinbooster) vendidas em pacotes — o sistema precisa gerenciar créditos de pacotes com precisão.",
         ),
        ("As dores de gestão específicas de clínicas estéticas",
         "Controle de pacotes de tratamento (cliente pagou por 10 sessões de laser, quantas já fez?) é a principal dor específica. Sem sistema, esteticistas controlam em cadernos ou planilhas que frequentemente mostram divergências. Outras dores: agendamento online para procedimentos com duração variável (laser de 30 min vs. drenagem de 90 min), controle de insumos de alto custo (ampolas de RF, materiais de limpeza de pele), prontuário de cliente com antes/depois de procedimentos e protocolos realizados, e programa de fidelidade com pontos por valor gasto.",
         ),
        ("Demo para clínicas estéticas: o que mostrar primeiro",
         "Comece pelo que é mais doloroso — o controle de pacotes. Mostre: venda de pacote de 10 sessões → desconto do crédito a cada sessão → saldo visível na tela a qualquer momento → alerta quando estiver nas últimas sessões para renovação. Depois mostre o agendamento online com duração correta por procedimento e o prontuário com fotos de antes/depois. Gestoras de clínicas estéticas ficam impressionadas com a organização visual que o sistema proporciona — especialmente se estavam usando grupos de WhatsApp para controlar agendas.",
         ),
        ("Prontuário eletrônico em clínicas estéticas: obrigatoriedade",
         "Para procedimentos realizados por médicos (medicina estética — toxina botulínica, preenchimento, lasers médicos), prontuário eletrônico com assinatura digital do médico é obrigação legal pelo CFM. Para procedimentos não médicos (esteticistas), o prontuário não é legalmente obrigatório mas é boa prática e diferencia a clínica. Documentar os protocolos realizados, os produtos usados, as reações observadas e as fotos de evolução protege a clínica em eventuais questionamentos do cliente e demonstra profissionalismo.",
         ),
        ("Prospecção em clínicas estéticas",
         "Instagram é o canal de descoberta de clínicas estéticas — o próprio cliente descobre via Instagram. Mas para vender SaaS para a clínica, o canal é diferente: visita presencial (o vendedor entra na clínica durante um horário de baixo movimento, faz uma demo no tablet e explica o ROI em 20 minutos), WhatsApp Business com vídeo de demo de 2 minutos, e indicações de distribuidores de insumos estéticos que já têm relacionamento com as clínicas. Feiras do setor (ESTETICADERM, Beauty Fair) são eventos de alta concentração de decisores.",
         ),
    ],
    [
        ("SaaS de clínica estética precisa ter módulo médico?",
         "Depende do perfil da clínica. Clínicas de estética que só realizam procedimentos não médicos (esteticistas) não precisam de prontuário médico com assinatura eletrônica qualificada. Clínicas de medicina estética com médicos (dermatologistas, biomédicos com formação específica, médicos estetas) precisam de prontuário eletrônico adequado à regulação CFM, com assinatura digital e possibilidade de prescrição eletrônica. Para clínicas mistas, o SaaS deve suportar os dois tipos de registro.",
         ),
        ("Programa de fidelidade em clínicas estéticas: vale a pena?",
         "Sim. Clientes de estética têm alta frequência de retorno — tratamentos de manutenção, pacotes de seguimento e novos procedimentos são vendas recorrentes para a mesma base. Programa de pontos por valor gasto (1 ponto = R$ 1, 100 pontos = R$ 10 de desconto no próximo procedimento) fideliza clientes e aumenta o ticket médio ao longo do tempo. Clientes fidelizados de clínicas estéticas têm LTV de 3 a 5x maior do que clientes pontuais. O SaaS que gerencia o programa automaticamente elimina a logística de cartões de papel e controles manuais.",
         ),
        ("Antes/depois de procedimentos estéticos: como registrar no sistema?",
         "O registro de fotos antes/depois nos prontuários é prática padrão em clínicas estéticas de qualidade — documenta a evolução do tratamento e é a prova mais poderosa de resultado. SaaS especializado permite: foto padronizada com iluminação e ângulo controlados (guidelines de posicionamento), armazenamento seguro com acesso restrito por paciente (LGPD), comparação lado a lado de antes/depois, e uso autorizado pelo paciente em marketing (consentimento informado integrado ao prontuário). A galeria de evolução de resultados é o principal argumento de marketing de clínicas estéticas.",
         ),
    ]
)

# ── Article 4978 ── Consulting: energia e eficiência energética
art(
    "consultoria-de-energia-e-eficiencia-energetica",
    "Consultoria de Energia e Eficiência Energética | ProdutoVivo",
    "Como estruturar e vender consultoria de energia e eficiência energética. Guia para consultores que atuam em mercado livre de energia, solar e eficiência energética.",
    "Consultoria de Energia e Eficiência Energética: Como Construir uma Prática Especializada",
    "Energia é um dos maiores custos operacionais de indústrias, comércios e grandes condomínios — e o Brasil tem um dos sistemas elétricos mais complexos do mundo, com mercado livre de energia, energia solar distribuída, leilões de energia renovável e tarifas de distribuidoras que poucas empresas entendem completamente. Consultores que dominam esse universo têm demanda crescente e projetos de alto ticket.",
    [
        ("O escopo da consultoria de energia",
         "Consultoria de energia abrange: migração para o mercado livre de energia (para consumidores elegíveis acima de 500 kW — desde 2024, o mercado foi expandido), diagnóstico e implementação de eficiência energética (redução do consumo sem redução de produção ou conforto), energia solar fotovoltaica (análise de viabilidade, dimensionamento, procurement), gestão energética continuada (monitoramento de consumo, análise de faturas, identificação de desvios), e compliance com programas de eficiência energética (Procel, certificações ISO 50001).",
         ),
        ("Mercado livre de energia: a maior oportunidade de consultoria",
         "O mercado livre de energia elétrica permite que consumidores acima de determinada potência contratada (500 kW desde jan/2024) negociem energia diretamente com produtores e comercializadores — em vez de pagar a tarifa da distribuidora local. A economia típica é de 10 a 25% na conta de energia. Um consumidor industrial com R$ 500.000/mês de conta de energia economiza R$ 50.000 a R$ 125.000/mês. Consultores que dominam a migração — contratos, câmaras de liquidação, lastro e sazonalização — cobram honorários de R$ 30.000 a R$ 200.000 pelo processo de migração.",
         ),
        ("Eficiência energética: diagnóstico e implementação",
         "Diagnóstico de eficiência energética (auditoria energética) mapeia onde a energia está sendo consumida, identifica oportunidades de redução (iluminação LED, motores eficientes, ar-condicionado de alta eficiência, isolamento térmico, ajuste de reativos) e quantifica o ROI de cada medida. Implementação de medidas de eficiência pode reduzir o consumo em 15 a 40% dependendo do perfil da instalação. Contratos de ESCo (Energy Service Company) — onde o consultor é remunerado com percentual da economia gerada — são modelos de venda de alto ticket com risco compartilhado.",
         ),
        ("Energia solar: consultoria de viabilidade e procurement",
         "Energia solar fotovoltaica cresceu exponencialmente no Brasil — mais de 40 GW instalados. Para empresas consumidoras, a análise de viabilidade (custo do sistema vs. economia na conta de energia, payback típico de 4 a 8 anos) é o primeiro projeto. Consultores que especificam o sistema correto (dimensionamento por consumo, tipo de conexão — autoconsumo local, autoconsumo remoto, geração compartilhada), conduzem o processo de licitação com fornecedores e gerenciam a implantação têm proposição de valor completa. A escolha do integrador solar certo é crítica — há muitas empresas de baixa qualidade no mercado.",
         ),
        ("Captação de clientes para consultoria de energia",
         "Diretores de operações, gerentes de facilities e CFOs de empresas industriais, comerciais de grande porte e redes de varejo são os compradores-alvo. A conta de energia é o argumento de abertura mais direto — 'posso reduzir sua conta de energia em 20%, você tem interesse em conversar?' é uma das abordagens frias com maior taxa de resposta em qualquer setor. ABRACE (Associação dos Grandes Consumidores), ABRACEEL (comercializadores), ABSOLAR (solar) e o CBEE (Conselho Brasileiro de Eficiência Energética) são comunidades setoriais.",
         ),
    ],
    [
        ("Quem pode migrar para o mercado livre de energia?",
         "Consumidores com demanda contratada igual ou superior a 500 kW (Grupo A — média tensão) são elegíveis para o mercado livre desde janeiro de 2024. A transição para abertura total do mercado (incluindo consumidores do Grupo B — baixa tensão) está prevista para 2028. Para migrar, o consumidor contrata uma comercializadora de energia e um consultor/representante para gerir o processo na CCEE (Câmara de Comercialização de Energia Elétrica). Empresas que migram para o mercado livre precisam de medidor bidirecional homologado pela distribuidora.",
         ),
        ("ISO 50001 é obrigatória?",
         "ISO 50001 (Sistema de Gestão de Energia) não é obrigatória para a maioria das empresas. É voluntária mas exigida como requisito de certificação para fornecedores de algumas grandes corporações (especialmente multinacionais com metas de ESG) e para participação em determinados programas de eficiência energética. A norma exige que a empresa implante um sistema de gestão energética (SGE) com política de energia, metas de redução de consumo, monitoramento contínuo e revisão periódica. A certificação tem custo de auditoria anual e manutenção, mas demonstra compromisso mensurável com eficiência energética.",
         ),
        ("Payback de energia solar para empresas: quanto tempo?",
         "O payback de sistemas fotovoltaicos para empresas no Brasil é tipicamente de 3 a 6 anos para sistemas comerciais e industriais, dependendo do tamanho do sistema, tarifa local, irradiação solar da região e custo de financiamento. Sistemas no Nordeste (maior irradiação) têm payback menor. Com financiamento pelo BNDES Finem (taxa subsidiada) ou Finame, o payback pode ser ainda mais rápido — o sistema se paga antes de acabar de ser financiado. Vida útil dos painéis é de 25 a 30 anos, com garantia de potência de 80% em 25 anos pelos fabricantes premium.",
         ),
    ]
)

# ── Article 4979 ── B2B SaaS: plataforma de engajamento de clientes
art(
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-plataforma-de-engajamento-de-clientes",
    "Gestão de Negócios de Empresa de B2B SaaS de Plataforma de Engajamento de Clientes | ProdutoVivo",
    "Como construir e escalar um B2B SaaS de plataforma de engajamento de clientes. Estratégias de produto, diferenciação e go-to-market.",
    "Como Escalar um B2B SaaS de Plataforma de Engajamento de Clientes",
    "Plataformas de engajamento de clientes (CEP — Customer Engagement Platform) combinam comunicação multicanal, automação comportamental e personalização em escala — são o coração do marketing digital moderno. E-mail marketing, SMS, push notifications, WhatsApp, in-app messages e pop-ups orquestrados por triggers comportamentais em tempo real são as capacidades que separam uma CEP de um simples disparador de e-mail.",
    [
        ("O que diferencia uma CEP de um simples e-mail marketing",
         "E-mail marketing básico envia o mesmo e-mail para toda a base em dia programado. Uma CEP dispara mensagens baseadas em comportamento em tempo real — o usuário abandonou o carrinho às 14h07 e recebe um WhatsApp às 14h37 com o carrinho recuperado. Visitou a página de plano premium 3 vezes essa semana? Recebe um e-mail com uma oferta de trial estendido. É o aniversário do cliente? Recebe mensagem personalizada com cupom de desconto válido por 24h. O gatilho comportamental + orquestração multicanal é o diferencial que transforma engajamento em receita.",
         ),
        ("Canais de engajamento que a plataforma deve suportar",
         "Para competir no mercado brasileiro, WhatsApp é obrigatório — via API oficial do WhatsApp Business (Meta). E-mail é o canal de maior volume e menor custo. SMS é usado para mensagens críticas (confirmação de pedido, código de verificação). Push notification para apps móveis mantém o usuário engajado sem precisar abrir o app. In-app messages para usuários ativos no produto. Cada canal tem seu lugar na jornada — WhatsApp para recuperação rápida (alta taxa de abertura), e-mail para conteúdo rico, SMS para urgência, push para ativação.",
         ),
        ("Segmentação e personalização em escala",
         "A qualidade de uma CEP é medida pela granularidade da segmentação — não só 'clientes que compraram nos últimos 30 dias' mas 'clientes que compraram tênis de corrida acima de R$ 300, visualizaram meias técnicas mais de 2 vezes, nunca compraram acessórios, e estão inativos há mais de 20 dias'. Combinação de atributos estáticos (perfil) com comportamento dinâmico (ações recentes) para criar segmentos acionáveis em tempo real é o diferencial técnico central. Machine learning para score de propensão de compra, churn e upsell é o próximo nível.",
         ),
        ("Mensurabilidade e atribuição: o ROI da plataforma",
         "Cada automação de engajamento deve ser mensurável — taxa de abertura, cliques, conversões, receita gerada diretamente da campanha. A/B testing nativo (testar assunto de e-mail, horário de envio, copy do WhatsApp) é funcionalidade obrigatória. Atribuição de receita a campanhas específicas — 'este fluxo de recuperação de carrinho gerou R$ 87.000 em receita no último mês' — é o argumento de ROI que justifica a renovação do contrato e o upsell de plano. CEPs que não entregam atribuição clara de receita perdem clientes para concorrentes que entregam.",
         ),
        ("Go-to-market para CEP B2B",
         "E-commerce de médio porte (R$ 5M a R$ 100M de GMV), SaaS, marketplaces e varejistas omnichannel são os segmentos de maior adoção. Heads de CRM, diretores de marketing digital e founders de e-commerce são os compradores-alvo. Demo deve mostrar uma automação configurada em tempo real — 'vou criar um fluxo de recuperação de carrinho agora, conectar WhatsApp e e-mail, e mostrar o ROI estimado baseado na sua taxa de abandono'. Parcerias com agências de performance digital (que fazem tráfego mas não têm CRM/engajamento) são canais de co-selling muito eficientes.",
         ),
    ],
    [
        ("CEP vs. CRM: qual a diferença e quando usar cada um?",
         "CRM (Customer Relationship Management) gerencia o relacionamento com clientes — histórico de interações, negociações, dados cadastrais, pipeline de vendas. CEP (Customer Engagement Platform) orquestra comunicações com clientes em escala baseadas em comportamento. São complementares: o CRM tem os dados do cliente; a CEP usa esses dados para se comunicar no momento certo pelo canal certo. Para B2B com ciclo de vendas longo, CRM é central. Para B2C com grandes bases de clientes e e-commerce, CEP é o investimento de maior impacto. Muitas empresas precisam dos dois integrados.",
         ),
        ("WhatsApp pode ser usado para marketing sem ser bloqueado?",
         "WhatsApp Business API (via parceiros oficiais da Meta, chamados BSPs — Business Solution Providers) permite envio de mensagens de marketing para opt-ins explícitos — usuários que aceitaram receber comunicações da empresa. Spam (envio em massa sem opt-in) resulta em bloqueio da conta. As boas práticas: opt-in claro antes de qualquer comunicação, fácil cancelamento de inscrição (responder 'sair'), relevância das mensagens (não enviar promoções irrelevantes), e frequência controlada. Taxas de abertura no WhatsApp chegam a 80 a 90% vs. 20 a 30% em e-mail — mas o canal precisa ser respeitado.",
         ),
        ("LGPD afeta as plataformas de engajamento?",
         "Sim, diretamente. Enviar comunicações de marketing por qualquer canal (e-mail, WhatsApp, SMS) requer base legal válida sob a LGPD — tipicamente o consentimento do titular (opt-in claro) ou legítimo interesse (para clientes existentes com relação comercial ativa). CEPs devem ter: registro de opt-in por canal com data e origem, mecanismo de opt-out em cada mensagem, gestão de preferências do usuário por canal, e exportação dos dados para atender solicitações de titulares (direito de acesso e exclusão). CEP que não tem esses controles cria passivo de compliance para seu cliente.",
         ),
    ]
)

# ── Article 4980 ── Clinics: cirurgia cardiovascular
art(
    "gestao-de-clinicas-de-cirurgia-cardiovascular",
    "Gestão de Clínicas de Cirurgia Cardiovascular | ProdutoVivo",
    "Guia de gestão para serviços de cirurgia cardiovascular: estrutura de centro cirúrgico cardíaco, faturamento e estratégias de excelência.",
    "Gestão de Serviços de Cirurgia Cardiovascular: Guia Completo",
    "Cirurgia cardiovascular é uma das especialidades de maior complexidade e maior ticket em toda a medicina — revascularização do miocárdio (bypass coronariano), substituição de válvulas cardíacas, cirurgias de aorta e tratamento cirúrgico de arritmias são procedimentos que salvam vidas e que exigem toda a infraestrutura de um hospital de alta complexidade. Para gestores de centros cardíacos, a combinação de excelência clínica e eficiência operacional é o desafio central.",
    [
        ("Estrutura de um serviço de cirurgia cardiovascular",
         "Um serviço de cirurgia cardiovascular completo exige: centro cirúrgico cardíaco com perfusionista (operador da circulação extracorpórea), UTI cardiovascular com cardiologistas intensivistas, equipe de cirurgiões cardiovasculares com subespecialização (adulto, pediátrico, aorta), hemodinâmica/laboratório de cateterismo (para diagnóstico e procedimentos percutâneos — stents coronarianos, TAVI), equipe de cardiologia clínica para preparo pré e pós-cirúrgico, e fisioterapia cardiorrespiratória para reabilitação. É um dos serviços mais caros de operar — mas com faturamento correspondentemente alto.",
         ),
        ("A interface entre cardiologia intervencionista e cirurgia cardiovascular",
         "A grande transformação da cardiologia nos últimos 20 anos foi o desenvolvimento de procedimentos percutâneos — stents coronarianos (via cateterismo, sem cirurgia aberta), TAVI (troca de válvula aórtica por cateter — indicado para idosos de alto risco cirúrgico), oclusão de orifícios septais, e ablação de arritmias. Para cirurgiões cardiovasculares, isso reduziu o volume de cirurgias eletivas mas não eliminou — revascularização coronariana cirúrgica ainda é superior em determinados perfis (doença multivascular, diabéticos). O Heart Team (decisão conjunta de cardiologistas e cirurgiões) é o padrão atual.",
         ),
        ("Faturamento em cirurgia cardiovascular",
         "Cirurgias cardiovasculares têm os maiores tickets da tabela TUSS — revascularização do miocárdio com circulação extracorpórea fatura de R$ 30.000 a R$ 100.000 entre honorários, taxas hospitalares, perfusionista, UTI e materiais (próteses valvulares, enxertos). TAVI (substituição de válvula aórtica por cateter) tem dispositivo de R$ 80.000 a R$ 150.000 mais honorários. A negociação de tabelas com convênios é crítica — valores pactuados abaixo do custo real comprometem a viabilidade do serviço. Serviços que trabalham com auditorias de faturamento rigorosas têm glosas muito menores.",
         ),
        ("Indicadores de qualidade em cirurgia cardíaca",
         "Mortalidade operatória ajustada por risco (comparada ao score EuroSCORE ou STS Score esperado), taxa de reoperação por sangramento, tempo médio de ventilação mecânica pós-operatória, taxa de infecção de ferida cirúrgica esternal, tempo de permanência em UTI cardiovascular e índice de satisfação do paciente são os KPIs centrais. Participação em bancos de dados nacionais e internacionais (Registro Brasileiro de Cirurgia Cardiovascular — RBCCV) permite benchmarking de qualidade e identificação de oportunidades de melhoria.",
         ),
        ("Captação de pacientes para cirurgia cardiovascular",
         "Cardiologistas clínicos e intervencionistas são os principais encaminhadores — a relação entre cardiologistas e o time cirúrgico é o capital mais importante de um serviço de cirurgia cardiovascular. Heart Teams formais (reuniões semanais de discussão de casos complexos entre cardiologistas e cirurgiões) são o modelo de colaboração que resulta em mais encaminhamentos e melhores decisões clínicas. Para centros de referência regional, a capacidade de receber transferências de outros hospitais de menor complexidade amplia significativamente o volume.",
         ),
    ],
    [
        ("Cirurgia de bypass coronariano vai desaparecer com os stents?",
         "Não. Apesar do enorme avanço dos stents coronarianos (angioplastia), a revascularização cirúrgica (bypass) ainda é superior em pacientes com doença multivascular (obstrução de 3 vasos coronarianos) e diabéticos — estudos SYNTAX, FREEDOM e outros demonstraram sobrevida e taxa de eventos cardiovasculares melhores com a cirurgia em longo prazo. Para doença de tronco de coronária esquerda, o bypass é frequentemente preferido. O stent avança continuamente, mas a cirurgia cardiovascular mantém indicações sólidas e insubstituíveis para determinados perfis de paciente.",
         ),
        ("O que é TAVI e quem é candidato?",
         "TAVI (Transcatheter Aortic Valve Implantation) é a substituição da válvula aórtica por via percutânea (cateter pela virilha) — sem cirurgia aberta com abertura do tórax e circulação extracorpórea. É indicado para pacientes com estenose aórtica grave que têm alto risco cirúrgico (idosos, múltiplas comorbidades). Com a expansão das indicações para pacientes de risco intermediário e baixo, o TAVI ganhou enorme volume. No Brasil, o procedimento é coberto por alguns convênios mas o dispositivo tem alto custo — o que limita o acesso. Centros com Heart Team experiente em TAVI são referências regionais.",
         ),
        ("Reabilitação cardíaca pós-cirurgia: é obrigatória?",
         "Reabilitação cardiovascular pós-cirurgia cardíaca não é legalmente obrigatória, mas é fortemente recomendada pelas diretrizes da SBC (Sociedade Brasileira de Cardiologia) e da ESC. Programas estruturados de reabilitação — exercício supervisionado, controle de fatores de risco, educação do paciente, suporte psicológico — reduzem mortalidade cardiovascular em 20 a 30% e reinternações em 25 a 35% em 1 ano. Centros cardíacos que oferecem reabilitação integrada têm melhores resultados clínicos, maior satisfação do paciente e geram receita adicional no pós-operatório.",
         ),
    ]
)

# ── Article 4981 ── SaaS Sales: autoescolas
art(
    "vendas-para-o-setor-de-saas-de-autoescolas",
    "Vendas para o Setor de SaaS de Autoescolas | ProdutoVivo",
    "Como vender SaaS para autoescolas no Brasil. Estratégias de prospecção, demonstração e fechamento no setor de habilitação veicular.",
    "Como Vender SaaS para Autoescolas",
    "O Brasil tem mais de 20.000 autoescolas (Centro de Formação de Condutores — CFCs) registradas, que formam milhões de novos condutores por ano. Gestão de alunos, controle de aulas práticas, gestão de instrutores e aulas teóricas, faturamento e integração com o DETRAN são dores operacionais de todas as autoescolas. É um mercado com compradores práticos, pouco digitalizados e com dor real de gestão.",
    [
        ("A operação de uma autoescola e os problemas de gestão",
         "Uma autoescola gerencia: matrículas de alunos com documentação (RG, CPF, laudo médico), agendamento de aulas teóricas (simulados, conteúdo de trânsito), agendamento de aulas práticas com instrutores e veículos específicos, controle de frequência e etapas do processo de habilitação, exames médicos e psicológicos, agendamento de exames no DETRAN, e cobrança em parcelas. Sem sistema, tudo isso é feito em cadernos, planilhas e WhatsApp — com confusão de agendamento, alunos que não sabem onde estão no processo e faturamento desorganizado.",
         ),
        ("Gestão de agenda de instrutores: a maior dor operacional",
         "Agenda de aulas práticas é o core do sistema de autoescola — cada instrutor tem disponibilidade específica, cada veículo tem agenda própria, e combinações erradas (mesmo aluno + instrutor, veículo + dia duplo) geram conflitos. Sistema de agendamento com visualização de disponibilidade por instrutor e veículo, agendamento pelo próprio aluno via app ou portal (reduzindo o trabalho da recepção), e histórico de aulas concluídas por aluno são as funcionalidades de maior impacto operacional.",
         ),
        ("Integração com DETRAN: o diferencial técnico",
         "Autoescolas precisam registrar no DETRAN o andamento de cada aluno — etapas concluídas, resultado de exames, agendamento de provas práticas. A integração automática com os sistemas de DETRAN estaduais (que têm diferentes sistemas e APIs) é complexa mas é o diferencial mais valorizado por autoescolas. Sem integração, o funcionário precisa acessar o sistema do DETRAN manualmente para cada aluno — processo lento e sujeito a erros. Cada estado tem sistema diferente, o que cria barreira de entrada mas também diferencial competitivo para quem investe na integração.",
         ),
        ("Demo para autoescolas",
         "Demo começa com a matrícula de um novo aluno — cadastro com documentos, contrato e parcelamento gerado automaticamente. Depois, agende uma aula prática no calendário do instrutor pelo app do aluno — mostre que o conflito de agendamento é impossível. Exiba o painel do aluno com seu progresso (etapas concluídas, pendentes, próxima aula agendada). Mostre o relatório financeiro por mês — parcelas recebidas, pendentes e inadimplentes. Para donos de autoescola, a visão financeira e o painel de progresso de todos os alunos são os momentos de maior impacto da demo.",
         ),
        ("Prospecção em autoescolas",
         "FENACFCS (Federação Nacional das Autoescolas) e sindicatos estaduais (SINDICESP em SP, SINDERJ no RJ) são pontos de acesso ao setor. Feiras estaduais de trânsito e eventos do DENATRAN concentram decisores. Visita presencial à autoescola durante horário de menor movimento (fim da tarde em dias de semana) é o canal de prospecção mais eficaz — o dono costuma estar presente e tem tempo para conversa. Indicações de outros donos de autoescola (o setor é colaborativo regionalmente) têm alta taxa de conversão.",
         ),
    ],
    [
        ("Autoescola precisa de NF-e ou NFS-e?",
         "Autoescolas prestam serviço de formação de condutores — emitem NFS-e (Nota Fiscal de Serviços Eletrônica) pelo sistema da prefeitura do município onde estão localizadas. Para venda de materiais (apostila, taxa de exame) pode haver NF-e de produto. A maioria das autoescolas ainda emite recibos ou NFS-e manualmente pelo sistema da prefeitura — sistema que integra a emissão automática de NFS-e após o faturamento de cada aluno economiza horas mensais e reduz erros.",
         ),
        ("Aluno pode cancelar a habilitação no meio do processo?",
         "Sim. O aluno pode desistir a qualquer momento, perdendo as aulas já realizadas. A relação de consumo entre aluno e autoescola é regulada pelo CDC — o contrato deve especificar claramente o que é pago por etapa e o que é reembolsável em caso de desistência. Muitas autoescolas praticam política de não reembolso de taxas pagas ao DETRAN (exames, CFO — Curso de Formação de Condutores) mas devolvem proporcional das mensalidades não utilizadas. Documentar isso no contrato e ter registro digital de cada aula realizada é a proteção jurídica da autoescola.",
         ),
        ("Quanto fatura uma autoescola por aluno?",
         "O ticket médio de habilitação (categoria B — carro) no Brasil varia de R$ 2.500 a R$ 5.000 dependendo da cidade. Em capitais como São Paulo e Rio, pode chegar a R$ 5.000 a R$ 8.000 com taxas de DETRAN incluídas. Uma autoescola de médio porte com 100 a 200 alunos ativos tem faturamento mensal de R$ 30.000 a R$ 80.000. A margem é pressionada pelo custo de manutenção da frota de veículos (depreciação, seguro, combustível) e pelos salários de instrutores qualificados, mas o segmento é consistentemente rentável com gestão eficiente.",
         ),
    ]
)

# ── Article 4982 ── Consulting: setor público e governo
art(
    "consultoria-de-setor-publico-e-governo",
    "Consultoria de Setor Público e Governo | ProdutoVivo",
    "Como estruturar e vender consultoria para o setor público e governo. Guia para consultores que atuam em gestão pública, licitações e transformação digital do Estado.",
    "Consultoria de Setor Público e Governo: Como Construir uma Prática Especializada",
    "Setor público é um dos maiores mercados de consultoria do Brasil — municípios, estados, autarquias, empresas públicas e o governo federal investem bilhões em contratação de serviços de consultoria anualmente. Gestão de políticas públicas, transformação digital do Estado, modelagem de concessões e PPPs, análise de impacto regulatório e reforma administrativa são projetos de alto ticket que exigem consultores com conhecimento profundo do ambiente jurídico e político brasileiro.",
    [
        ("O escopo da consultoria para o setor público",
         "Consultoria pública abrange: planejamento estratégico governamental (PPA — Plano Plurianual, planos setoriais), análise e avaliação de políticas públicas (eficácia e eficiência de programas), transformação digital de serviços públicos (digitalização de processos, governo eletrônico, ciência de dados para gestão pública), modelagem e estruturação de PPPs (Parcerias Público-Privadas) e concessões, gestão de projetos de investimento público (PAC, programas habitacionais), e fortalecimento institucional de órgãos e entidades.",
         ),
        ("Licitação e contratação pública: como consultores acessam o mercado",
         "A maioria dos contratos de consultoria com o setor público passa por licitação pública — modalidades como Tomada de Preços, Concorrência, Pregão Eletrônico ou dispensa de licitação para valores menores (Lei 14.133/2021). Para participar, a empresa de consultoria precisa: (1) CNPJ ativo e idoneidade comprovada, (2) habilitação técnica (acervo técnico de serviços similares), (3) capacidade econômico-financeira (balanços, certidões negativas), e (4) regularidade fiscal. Consultoras individuais (profissionais liberais) frequentemente participam como contratadas diretamente por dispensa de licitação ou via cooperativas.",
         ),
        ("Transformação digital do Estado: o maior mercado atual",
         "Transformação digital de serviços públicos é o segmento de maior crescimento em consultoria pública — desde digitalização de serviços (emissão digital de certidões, licenciamentos online, saúde digital) a implementação de governo como plataforma, Open Government Data e uso de inteligência artificial para políticas públicas. Experiências como o GOV.BR federal, plataformas estaduais e municipais de serviços digitais geraram demanda por consultores que combinem expertise em design de serviços públicos, tecnologia e gestão de mudança em ambientes complexos.",
         ),
        ("PPPs e concessões: consultoria de alto ticket",
         "Modelagem de PPPs (Parcerias Público-Privadas) e concessões é um dos segmentos de maior ticket em consultoria pública — projetos de R$ 500.000 a R$ 5.000.000 de honorários. A consultora modela a estrutura financeira da concessão (TIR do concessionário, tarifas, aportes públicos), elabora o edital, conduz os estudos de viabilidade e assessora no processo de licitação. O pipeline é dependente de ciclos de investimento do governo (pré-eleição e pós-eleição são os picos), mas projetos de infraestrutura (saneamento, mobilidade, energia, saúde) têm demanda constante.",
         ),
        ("Captação em setor público: diferenças do mercado privado",
         "No mercado público, a relação com servidores técnicos (secretários, diretores, equipe de planejamento) é mais importante do que com o político eleito — os servidores têm continuidade entre governos e são os catalisadores de projetos. Participação em congressos de gestão pública (Congresso CONSAD, CLAD — Congresso Internacional da gestão pública) e relação com escolas de governo (FGV-EAESP, ENAP, IUPERJ) são canais de networking. Publicação de artigos acadêmicos e policy briefs sobre temas de política pública credencia o consultor como referência.",
         ),
    ],
    [
        ("Consultor pode trabalhar com setor público como pessoa física?",
         "Sim, com algumas restrições. Contratos de consultoria individual (pessoa física) com o setor público são possíveis por dispensa de licitação para valores abaixo dos limites da Lei 14.133/2021 (R$ 59.904 para serviços comuns em 2024) ou via contratos de prestação de serviços técnicos especializados de natureza singular que admitem contratação direta. Para projetos maiores, a consultora precisa ser pessoa jurídica para participar de licitações. Muitos consultores optam por abrir uma empresa (LTDA ou SS) para poder participar do mercado público sem limitação de valor.",
         ),
        ("A Lei 14.133/2021 (Nova Lei de Licitações) mudou muito o mercado?",
         "A Nova Lei de Licitações (Lei 14.133/2021) trouxe mudanças significativas: nova modalidade (Diálogo Competitivo para objetos de alta complexidade), critérios ampliados de habilitação técnica, maior ênfase em planejamento pré-licitação (Estudo Técnico Preliminar e Termo de Referência mais robustos), e obrigatoriedade de uso do PNCP (Portal Nacional de Contratações Públicas). Para consultoras, a exigência de maior documentação de habilitação e os prazos mais longos de licitação aumentam o custo de participação, mas também elevam a barreira de entrada para concorrentes menos estruturados.",
         ),
        ("Há conflito de interesse em trabalhar para o setor público e privado ao mesmo tempo?",
         "Não em geral, mas com cuidados específicos. Um consultor que trabalha para o governo em uma regulação setorial não pode assessorar empresas reguladas pelo mesmo órgão em questões que envolvam a regulação em que participou — seria conflito de interesse vedado. Fora disso, trabalhar para o setor público e privado simultaneamente é prática comum em consultoria. A vedação à lei específica do servidor público aplica-se a servidores — consultores contratados por projeto não são servidores e têm liberdade de atuação maior.",
         ),
    ]
)

# ── Sitemap + trilha update ──
import re

sitemap_path = pathlib.Path(__file__).parent / "sitemap.xml"
trilha_path  = pathlib.Path(__file__).parent / "trilha.html"

slugs = [
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-despesas-e-viagens-corporativas",
    "gestao-de-clinicas-de-medicina-de-familia-e-comunidade",
    "vendas-para-o-setor-de-saas-de-clinicas-esteticas-e-spas",
    "consultoria-de-energia-e-eficiencia-energetica",
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-plataforma-de-engajamento-de-clientes",
    "gestao-de-clinicas-de-cirurgia-cardiovascular",
    "vendas-para-o-setor-de-saas-de-autoescolas",
    "consultoria-de-setor-publico-e-governo",
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

print("Done — batch 1746")
