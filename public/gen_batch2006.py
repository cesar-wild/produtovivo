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


# ── Article 5495 — B2B SaaS: Gestão de Acesso e Identidade (IAM) ──
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-acesso-e-identidade-iam",
    title="Gestão de Negócios para Empresas de B2B SaaS de Gestão de Acesso e Identidade (IAM) | ProdutoVivo",
    desc="Estratégias de gestão para empresas B2B SaaS de IAM e gestão de acesso e identidade: crescimento, diferenciação e mercado. Guia para infoprodutores.",
    h1="Gestão de Negócios para Empresas de B2B SaaS de Gestão de Acesso e Identidade (IAM)",
    lead="Plataformas de Identity and Access Management (IAM) são infraestrutura de segurança crítica para empresas que gerenciam acesso de colaboradores, clientes e parceiros a sistemas e dados. Para infoprodutores que atendem o mercado de segurança e TI corporativa, entender esse segmento SaaS revela oportunidades de conteúdo com alta demanda técnica e estratégica.",
    sections=[
        ("O Mercado de IAM e a Crescente Demanda por Identidade Digital",
         "Identity and Access Management (IAM) abrange autenticação (quem você é), autorização (o que você pode fazer) e gestão do ciclo de vida de identidades digitais. Com a proliferação de aplicações cloud, trabalho remoto e regulações como LGPD e GDPR, IAM passou de ferramenta técnica para imperativo de negócio. O mercado global de IAM supera US$15 bilhões e cresce acima de 13% ao ano. No Brasil, empresas de todos os portes enfrentam pressões de conformidade, ameaças de credential stuffing e ransomware, e necessidade de experiência de acesso simples e segura para colaboradores e clientes."),
        ("Segmentos de IAM: Workforce vs. Customer Identity",
         "IAM se divide em dois grandes segmentos: Workforce IAM (gerencia identidades de colaboradores — SSO, MFA, provisionamento automático de acesso baseado em cargo) e CIAM — Customer Identity and Access Management (gerencia identidades de clientes externos — cadastro, login social, autenticação passwordless, perfis de consentimento LGPD). Empresas SaaS de IAM podem focar em um ou nos dois segmentos. O CIAM tem crescimento mais rápido impulsionado pela digitalização de serviços financeiros, varejo e saúde, onde a experiência de login impacta diretamente conversão e retenção."),
        ("Modelo de Go-to-Market para IAM SaaS",
         "IAM tem ciclo de vendas complexo porque envolve TI, CISO, Compliance e, muitas vezes, o board em contas enterprise. O go-to-market mais eficiente combina: conteúdo técnico de alta qualidade (documentação, blogs de engenharia, guias de implementação) que atrai arquitetos e desenvolvedores, trials gratuitos para casos de uso específicos, parcerias com integradores de sistemas e consultorias de segurança que implementam a solução, e presença em eventos de segurança (GSEC, RSA Conference). O developer relations (DevRel) é investimento estratégico — desenvolvedores são os guardiões de adoção de IAM em empresas que constroem aplicações."),
        ("Diferenciais Competitivos: Passwordless, Zero Trust e Compliance",
         "Os diferenciadores mais valorizados em IAM SaaS incluem: autenticação passwordless (biometria, FIDO2, magic links) que elimina senhas e reduz drasticamente o risco de phishing, arquitetura Zero Trust que aplica verificação contínua em vez de confiar implicitamente em conexões internas, conectores prontos para integração com centenas de aplicações (Salesforce, SAP, Google Workspace, Active Directory), suporte nativo a LGPD/GDPR com gestão de consentimento e portabilidade de dados, e relatórios de auditoria detalhados para compliance com normas regulatórias. Plataformas que oferecem esses diferenciadores com experiência de usuário simples capturam mercado de alto crescimento."),
        ("Precificação, Expansão e NRR em IAM SaaS",
         "IAM SaaS é precificado por usuário ativo, por autenticação realizada ou por módulo funcional (SSO, MFA, CIAM separados). O modelo por usuário ativo alinha custo ao valor entregue e facilita a expansão natural conforme o cliente cresce. NRR acima de 120% é comum em IAM enterprise porque o crescimento de usuários, a adição de módulos de segurança avançados e a expansão para novos casos de uso (de workforce para CIAM, por exemplo) aumentam o ARR de cada conta. Churn é baixo pelo alto custo de migração — integrar IAM em dezenas de aplicações cria dependência operacional profunda."),
    ],
    faq_list=[
        ("Qual a diferença entre SSO e MFA?",
         "SSO (Single Sign-On) permite que o usuário acesse múltiplos sistemas com uma única autenticação — melhora experiência e centraliza controle de acesso. MFA (Multi-Factor Authentication) exige dois ou mais fatores para autenticar — aumenta a segurança exigindo algo que você sabe (senha) mais algo que você tem (token, smartphone) ou algo que você é (biometria). SSO e MFA são complementares: SSO melhora usabilidade, MFA reforça segurança, e juntos criam a base de uma estratégia de identidade robusta."),
        ("IAM é necessário para startups pequenas?",
         "Sim, desde cedo. A configuração de SSO e MFA desde os primeiros colaboradores evita o caos de gestão de senhas, facilita onboarding e offboarding (revogar acessos na demissão em segundos, não dias) e cria base de segurança para crescimento. Startups que captam investimento ou entram em processos de due diligence precisam demonstrar controles de acesso maduros. Soluções como Okta, Auth0 e Microsoft Entra têm planos acessíveis para empresas em crescimento."),
        ("O que é Zero Trust e como IAM suporta essa arquitetura?",
         "Zero Trust é o princípio de nunca confiar implicitamente em nenhum usuário, dispositivo ou conexão — verificar sempre, em vez de assumir que quem está 'dentro da rede' é confiável. IAM é o pilar central de Zero Trust: autenticação forte (MFA), autorização granular baseada em atributos (ABAC), monitoramento contínuo de sessões e análise de risco em tempo real. Implementar IAM robusto é o primeiro e mais impactante passo em direção a uma arquitetura Zero Trust."),
    ]
)

# ── Article 5496 — Clinic: Reprodução Humana Assistida e Fertilidade ──
art(
    slug="gestao-de-clinicas-de-reproducao-humana-assistida-e-fertilidade",
    title="Gestão de Clínicas de Reprodução Humana Assistida e Fertilidade | ProdutoVivo",
    desc="Guia de gestão para clínicas de reprodução humana assistida e fertilidade: modelo de negócio, regulação, tecnologia e crescimento no Brasil. Para infoprodutores da saúde.",
    h1="Gestão de Clínicas de Reprodução Humana Assistida e Fertilidade",
    lead="Clínicas de reprodução humana assistida (RHA) e tratamento de fertilidade representam um dos segmentos de mais rápido crescimento na medicina privada brasileira. Para infoprodutores e consultores da saúde, entender a gestão dessas clínicas significa explorar um mercado de alto ticket, alta recorrência emocional e crescente demanda.",
    sections=[
        ("O Mercado de Fertilidade no Brasil",
         "O Brasil realiza mais de 80 mil ciclos de Fertilização In Vitro (FIV) por ano, sendo o terceiro maior mercado de RHA do mundo. A postergação da maternidade — com média de idade das mães ao primeiro filho superando 29 anos nas capitais — e o aumento da infertilidade associada a estilo de vida impulsionam a demanda. O setor é predominantemente privado, com cobertura de planos de saúde ainda limitada para procedimentos de RHA, embora decisões judiciais ampliem progressivamente a obrigação de cobertura. Clínicas bem posicionadas têm crescimento acima de 15% ao ano."),
        ("Portfólio de Serviços e Modelo Assistencial",
         "Uma clínica de RHA completa oferece: investigação da fertilidade do casal (avaliação andrológica e ginecológica), indução de ovulação e IIU (Inseminação Intrauterina), FIV convencional e ICSI (injeção intracitoplasmática de espermatozoide), criopreservação de gametas e embriões (congelamento de óvulos para preservação da fertilidade), diagnóstico genético pré-implantacional (DGPI), doação de gametas (banco de sêmen e doação de óvulos) e gestação de substituição (barriga solidária, regulada pelo CFM). A diversidade de técnicas permite personalização do tratamento e maximização das taxas de sucesso."),
        ("Gestão da Jornada Emocional do Paciente",
         "Pacientes de fertilidade vivem uma das jornadas mais emocionalmente intensas da medicina. Ciclos fracassados, lutos gestacionais e a incerteza inerente aos tratamentos exigem equipe treinada em comunicação empática, suporte psicológico integrado e gestão cuidadosa de expectativas. Clínicas que investem em psicóloga especializada em reprodução, grupos de apoio e comunicação proativa sobre cada etapa do tratamento criam vínculo profundo com os pacientes e se destacam em mercado baseado fortemente em recomendações. A experiência do paciente é tão importante quanto a taxa de sucesso na fidelização e no crescimento por indicação."),
        ("Indicadores de Qualidade e Acreditação",
         "As métricas centrais de qualidade em RHA incluem: taxa de gravidez clínica por ciclo iniciado, taxa de nascidos vivos por transferência, taxa de gravidez múltipla (idealmente reduzida com transferência de embrião único), taxa de cancelamento de ciclos e taxa de criopreservação de embriões. O Registro Latino-Americano de Reprodução Assistida (RLA) e a SBRA (Sociedade Brasileira de Reprodução Assistida) publicam dados de referência. Clínicas que participam de programas de benchmarking externo e publicam suas taxas de sucesso de forma transparente constroem credibilidade diferenciada."),
        ("Tecnologia, IA e Tendências em Fertilidade",
         "Time-lapse incubators (monitoramento contínuo do desenvolvimento embrionário por vídeo) e algoritmos de IA para seleção do melhor embrião para transferência elevam as taxas de sucesso e criam diferencial tecnológico. A telemedicina para consultas de acompanhamento e orientação pré-ciclo amplia o acesso e reduz o número de deslocamentos ao consultório. Criopreservação de óvulos para fins de preservação da fertilidade por escolha pessoal (fertility preservation) é segmento de crescimento acelerado entre mulheres de 30-40 anos. Infoprodutores que abordam a intersecção de tecnologia reprodutiva e decisões de vida têm audiência massiva e engajada."),
    ],
    faq_list=[
        ("FIV é coberta pelos planos de saúde no Brasil?",
         "A ANS não obriga cobertura de FIV na maioria dos casos, mas decisões judiciais têm ampliado o acesso para casais com infertilidade comprovada e para pessoas solteiras e casais homoafetivos em alguns casos. A cobertura varia enormemente por operadora e apólice. Recomenda-se sempre verificar o contrato e, em caso de negativa, buscar orientação jurídica especializada em direito à saúde."),
        ("Qual a diferença entre IIU e FIV?",
         "IIU (Inseminação Intrauterina) deposita espermatozoides preparados diretamente no útero durante o período fértil — procedimento mais simples, menos invasivo e de menor custo. FIV (Fertilização In Vitro) fecunda óvulos fora do corpo e transfere embriões para o útero — indicada quando IIU falhou, há fatores tubários, endometriose moderada/severa ou fator masculino grave. A taxa de sucesso por ciclo da FIV é superior à da IIU."),
        ("Criopreservação de óvulos vale a pena como investimento no futuro?",
         "Para mulheres que desejam postergar a maternidade, o congelamento de óvulos antes dos 35 anos oferece taxas de sucesso significativamente melhores do que tentar engravidar naturalmente após os 40. O custo no Brasil varia de R$15k a R$40k (coleta + congelamento), mais armazenamento anual. O benefício precisa ser discutido individualmente com especialista em reprodução, considerando idade, reserva ovariana e contexto de vida da paciente."),
    ]
)

# ── Article 5497 — SaaS Sales: Cervejarias Artesanais e Produtores de Bebidas ──
art(
    slug="vendas-para-o-setor-de-saas-de-cervejarias-artesanais-e-produtores-de-bebidas",
    title="Vendas para o Setor de SaaS de Cervejarias Artesanais e Produtores de Bebidas | ProdutoVivo",
    desc="Como vender SaaS para cervejarias artesanais, vinícolas e produtores de bebidas no Brasil: tomadores de decisão, dores e estratégias. Guia para infoprodutores.",
    h1="Vendas para o Setor de SaaS de Cervejarias Artesanais e Produtores de Bebidas",
    lead="O Brasil tem mais de 1.500 cervejarias artesanais ativas e um mercado de bebidas premium em forte expansão. Para infoprodutores e consultores de vendas B2B SaaS, esse segmento combina paixão pelo produto com dores operacionais reais e crescente abertura à tecnologia.",
    sections=[
        ("O Mercado de Cerveja Artesanal e Bebidas Premium no Brasil",
         "O Brasil é o terceiro maior mercado de cerveja do mundo e vive uma revolução craft: mais de 1.500 cervejarias registradas no MAPA, crescimento de 15% ao ano e proliferação de estilos, marcas regionais e experiências de degustação. Além da cerveja, o mercado de vinhos, destilados artesanais (cachaça premium, gin, whisky nacional), kombuchas e bebidas funcionais cresce impulsionado pelo consumidor que valoriza origem, história e qualidade. Todos esses produtores compartilham desafios comuns de gestão de produção, estoque de insumos, controle de qualidade, distribuição e relacionamento com clientes B2B (bares, restaurantes, distribuidores)."),
        ("Dores Operacionais e Oportunidades para SaaS",
         "As principais dores de cervejarias e produtores de bebidas incluem: controle de receitas e rastreabilidade de lotes (essencial para recall e certificação), gestão de insumos (malte, lúpulo, levedura) com controle de estoque e custos de produção por lote, acompanhamento de fermentação e parâmetros de qualidade, gestão de pedidos de distribuidores e clientes diretos, emissão de NF-e com regimes tributários específicos (como substituição tributária do ICMS em bebidas) e análise de rentabilidade por produto e canal. ERP e sistemas de gestão específicos para bebidas resolvem essas dores com fluência que sistemas genéricos não oferecem."),
        ("Tomadores de Decisão no Setor de Bebidas",
         "Em cervejarias artesanais pequenas (até 5.000 hl/ano), o dono-cervejeiro decide tudo — e é apaixonado pelo produto mais do que pela gestão. Abordagem que respeita essa paixão e demonstra como o sistema libera tempo para inovar em receitas, em vez de perder horas em planilhas, conecta bem com esse perfil. Em produtores maiores e grupos de bebidas, há um gerente financeiro/administrativo e, às vezes, TI envolvidos na decisão. Certificações como REINPEÇO e adequação à legislação MAPA/ANVISA são argumentos de conformidade que ressoam com decisores mais formais."),
        ("Canais e Estratégias de Penetração no Mercado",
         "A comunidade de cervejeiros artesanais é altamente conectada: grupos no Telegram e Discord, eventos como Festival Brasileiro da Cerveja (Blumenau), CBA (Campeonato Brasileiro de Xadrez — confusão, é o Campeonato Brasileiro de Artesania Cervejeira), e associações como ABRACERVA são pontos de encontro privilegiados. Patrocínio de eventos, degustações em feiras com presença de demo do sistema, parceiros distribuidores de insumos que recomendam a plataforma e YouTube com conteúdo de gestão de cervejaria são canais eficazes. Vinícolas e produtores de destilados têm associações próprias (UVIBRA, IBRAC) com dinâmica similar."),
        ("Tendências: Direto ao Consumidor, Assinaturas e Exportação",
         "Cervejarias que desenvolvem canal D2C (direto ao consumidor) via assinatura mensal de cervejas, loja própria ou e-commerce crescem com margens superiores à distribuição tradicional. SaaS que integra gestão de produção com gestão de clube de assinatura e e-commerce cria valor imenso para esse modelo. A exportação de cervejas especiais brasileiras (especialmente com ingredientes nativos como jambu, cupuaçu, maracujá) cresce e exige controles de rastreabilidade internacionais. Plataformas que suportam essa complexidade exportadora têm mercado crescente no segmento premium."),
    ],
    faq_list=[
        ("Existe ERP específico para cervejarias no Brasil?",
         "Sim. Sistemas como BrewMan, Cervejeiro.com e módulos especializados de ERPs como TOTVS e Sankhya para bebidas atendem especificamente a cervejarias e produtores de bebidas. Funcionalidades essenciais incluem: gestão de receitas e escalabilidade de lotes, controle de fermentação, gestão de insumos por lote com rastreabilidade, emissão de NF-e com ICMS ST e integração com SPED fiscal."),
        ("Como o SaaS ajuda cervejarias a cumprir exigências regulatórias?",
         "O MAPA exige registro de cervejarias e de cada produto, controle de processos produtivos e rastreabilidade de lotes. A ANVISA e as SEABs estaduais têm requisitos adicionais. Sistemas de gestão que mantêm registros de produção, análises de qualidade por lote, controle de temperatura de fermentação e integração fiscal facilitam auditorias e renovações de registro. O custo de não conformidade (multa, interdição, recall) é muito maior que o custo do sistema."),
        ("Cervejarias artesanais têm orçamento para SaaS?",
         "Cervejarias acima de 500 hl/ano geralmente têm orçamento para sistemas de R$200 a R$800/mês. Microcervejarias menores são mais sensíveis ao preço, mas soluções básicas de R$80 a R$200/mês com controle de receitas e estoque têm ROI claro mesmo para operações pequenas. Planos gratuitos com upgrade pago são eficientes para adquirir cervejeiros em fase inicial que crescerão para planos maiores."),
    ]
)

# ── Article 5498 — Consulting: Key Accounts e Strategic Account Management ──
art(
    slug="consultoria-de-gestao-de-key-accounts-e-strategic-account-management",
    title="Consultoria de Gestão de Key Accounts e Strategic Account Management | ProdutoVivo",
    desc="Como estruturar consultoria de gestão de key accounts (KAM) e strategic account management: metodologias, entregáveis e mercado. Guia para infoprodutores e consultores.",
    h1="Consultoria de Gestão de Key Accounts e Strategic Account Management",
    lead="Key Account Management (KAM) é a disciplina que define como empresas gerenciam seus clientes mais estratégicos — aqueles que representam disproportionalmente mais receita, influência ou oportunidade de crescimento. Para infoprodutores e consultores de vendas B2B, dominar KAM é entrar num nicho de alta demanda corporativa e ticket elevado.",
    sections=[
        ("O que é Key Account Management e Por Que Importa",
         "Key Account Management é a abordagem estratégica e estruturada para desenvolver, proteger e expandir relações com os clientes mais valiosos de uma empresa. Diferente da gestão transacional de vendas, KAM foca no longo prazo: compreender profundamente o negócio do cliente, alinhar a proposta de valor aos seus objetivos estratégicos, coordenar múltiplos pontos de contato e criar valor compartilhado que vai além do produto ou serviço fornecido. Empresas que estruturam KAM profissionalmente tipicamente têm NRR 20-40 pontos percentuais maior em key accounts do que no restante da carteira."),
        ("Seleção de Key Accounts e Critérios Estratégicos",
         "A primeira decisão em KAM é a correta — quem são os key accounts? Os critérios vão além do volume de receita atual: incluem potencial de crescimento, valor estratégico (referência de mercado, acesso a novos segmentos), alinhamento cultural e de valores, probabilidade de parceria de longo prazo e custo de atendimento. Ferramentas como matriz de atratividade (valor do cliente × compatibilidade estratégica) ajudam a priorizar objetivamente. Tratar muitos clientes como key accounts dilui o investimento e resulta em KAM medíocre para todos — foco nos 5-15% que realmente importam é o caminho certo."),
        ("Estrutura e Competências do Key Account Manager",
         "O Key Account Manager (KAM) é um papel híbrido que exige competências de consultor estratégico, gerente de projetos e orquestrador interno. Diferente do vendedor transacional, o KAM se posiciona como parceiro de negócios — participando de reuniões de planejamento do cliente, trazendo insights de mercado e conectando as capacidades da sua empresa com as necessidades emergentes do cliente. O consultor de KAM apoia empresas na definição do perfil ideal do KAM, na estrutura de incentivos (não apenas por vendas, mas por crescimento e satisfação da conta), e no desenvolvimento das competências da equipe."),
        ("Account Plans: A Ferramenta Central do KAM",
         "O account plan é o documento estratégico que orienta todo o relacionamento com um key account: inclui análise profunda do negócio do cliente (estratégia, desafios, competidores, stakeholders-chave), histórico e status atual do relacionamento, mapa de oportunidades (upsell, cross-sell, novos departamentos), objetivos do relacionamento para 12-24 meses, iniciativas concretas com responsáveis e datas, e métricas de sucesso. Account plans vivos (atualizados regularmente e compartilhados com o cliente) transformam o KAM de ferramenta interna em base de diálogo estratégico com o cliente."),
        ("Métricas e ROI de Programas de KAM",
         "O sucesso do programa de KAM é medido por: crescimento de receita nas contas gerenciadas (vs. restante da carteira), NPS específico de key accounts, taxa de retenção e renovação de contratos, share of wallet (% da compra total do cliente capturada pela empresa), número de novas oportunidades identificadas e convertidas, e qualidade das relações medida por profundidade de contatos (quantos C-levels a empresa conhece no cliente). ROI de programas de KAM bem estruturados é tipicamente de 5-10x o investimento na função, tornando o argumento comercial para consultores de KAM muito favorável."),
    ],
    faq_list=[
        ("Toda empresa precisa de KAM ou apenas as grandes?",
         "Qualquer empresa B2B com clientes de alto valor e potencial estratégico se beneficia de KAM estruturado. Uma agência com 20 clientes pode precisar de KAM para seus 3-4 mais importantes tanto quanto uma enterprise com centenas de contas. O critério é: existe cliente que, se perdido, causaria impacto material no negócio? Se sim, KAM justifica o investimento."),
        ("Qual a diferença entre KAM e Customer Success?",
         "Customer Success foca no sucesso do cliente com o produto/serviço — adoção, valor percebido, redução de churn. KAM foca no crescimento estratégico da conta — expansão de receita, aprofundamento do relacionamento, posicionamento como parceiro estratégico. Em SaaS, CS cuida da saúde operacional da conta; KAM desenvolve o potencial estratégico. Nas maiores contas, os dois papéis trabalham em conjunto."),
        ("Como convencer lideranças a investir em um programa de KAM?",
         "Calcule o valor em risco: 'nossas 10 maiores contas representam 60% da receita — um churn de 2 delas destrói a meta anual'. Depois mostre o upside: 'aumentar share of wallet nessas contas em 20% equivale a toda a receita nova que planejamos para o ano'. O argumento defensivo (proteger receita existente) combinado com o ofensivo (crescer sem precisar de novos clientes) raramente falha para justificar investimento em KAM."),
    ]
)

# ── Article 5499 — B2B SaaS: Automação de Marketing ──
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-automacao-de-marketing",
    title="Gestão de Negócios para Empresas de B2B SaaS de Automação de Marketing | ProdutoVivo",
    desc="Estratégias de gestão para empresas B2B SaaS de automação de marketing: crescimento, diferenciação, PLG e mercado. Guia para infoprodutores.",
    h1="Gestão de Negócios para Empresas de B2B SaaS de Automação de Marketing",
    lead="Plataformas de automação de marketing são centrais na estratégia de crescimento de empresas B2B modernas. Para infoprodutores e consultores que atendem o mercado de martech e growth, entender como empresas nesse espaço crescem e se diferenciam é essencial para criar conteúdos de alto valor.",
    sections=[
        ("O Ecossistema de Marketing Automation SaaS",
         "Marketing automation envolve o uso de software para automatizar ações de marketing repetitivas — nurturing de leads por e-mail, pontuação de leads (lead scoring), segmentação dinâmica, personalização de site, gestão de campanhas multicanal e atribuição de receita. O mercado global supera US$6 bilhões e inclui players como HubSpot, Marketo, Pardot/Salesforce Marketing Cloud e RD Station no Brasil. A automação libera times de marketing para trabalho estratégico, enquanto mantém engajamento personalizado em escala com milhares de leads simultaneamente."),
        ("Diferenciação em Mercado Competitivo",
         "Com tantos players consolidados, novos entrantes e SaaS menores se diferenciam por: foco vertical (automação de marketing para e-commerce, para construtoras, para SaaS B2B), preço mais acessível que HubSpot/Marketo para PMEs, facilidade de uso superior para equipes sem analistas dedicados, integrações nativas com ferramentas populares no Brasil (RD Station, Hotmart, WhatsApp Business), e recursos de IA para geração de copy, personalização preditiva e análise de performance. O RD Station dominou o mercado brasileiro explorando exatamente essa combinação de localização e facilidade."),
        ("Modelo PLG e Inbound no Marketing Automation",
         "Ferramentas de marketing automation têm go-to-market naturalmente alinhado com inbound: a empresa demonstra sua expertise em marketing digital ao adquirir clientes pelos mesmos métodos que ensina. Blogs de referência, webinars educativos, calculadoras de ROI, templates de automação gratuitos e certificações de marketing digital criam audiência qualificada e posicionam a plataforma como referência. O freemium com limite de contatos é o modelo PLG mais eficiente: o cliente experimenta o valor real, cresce sua base de contatos e naturalmente migra para planos pagos."),
        ("Integração com CRM, Vendas e Revenue Operations",
         "Automação de marketing desconectada do CRM cria ilhas de dados que frustram times de vendas. Plataformas que oferecem integração nativa com Salesforce, HubSpot CRM, Pipedrive e CRMs locais têm vantagem competitiva clara. O alinhamento de marketing e vendas via revenue operations — shared data, shared pipeline definitions, shared attribution — é o tema mais quente em B2B SaaS e cria demanda por plataformas que facilitam essa visibilidade end-to-end. Empresas que posicionam sua plataforma como hub de revenue operations ampliam o TAM e o ticket médio."),
        ("IA Generativa e o Futuro do Marketing Automation",
         "A IA generativa está transformando marketing automation: geração automática de variações de e-mail, personalização de conteúdo em tempo real por segmento, criação de workflows de nurturing a partir de prompts em linguagem natural e análise preditiva de melhor horário de envio e canal por lead. Plataformas que integram IA generativa nativa (não como add-on) aceleram a produtividade dos times de marketing e reduzem o custo de produção de conteúdo — argumento poderoso para justificar migração de plataformas legadas. Infoprodutores que abordam a intersecção de IA e marketing automation têm audiência massiva e crescente."),
    ],
    faq_list=[
        ("Qual a diferença entre e-mail marketing e marketing automation?",
         "E-mail marketing é o envio de campanhas em massa para uma lista — broadcast de uma mensagem para todos. Marketing automation é personalizada e baseada em comportamento: o lead recebe a mensagem certa no momento certo com base em suas ações (abriu e-mail, visitou página, baixou material, atingiu lead score). Automação converte muito mais porque é relevante; e-mail marketing simples é cada vez menos efetivo com a saturação de caixas de entrada."),
        ("Marketing automation faz sentido para empresas pequenas?",
         "Sim, especialmente para empresas com processo de vendas consultivo e ciclo longo. Uma empresa com 3 vendedores que tem 500 leads em diferentes estágios do funil não consegue nutrir manualmente — a automação multiplica a capacidade sem aumentar a equipe. Para e-commerce, recuperação de carrinho abandonado e sequências pós-compra têm ROI imediato e comprovado mesmo em operações pequenas."),
        ("Como medir o ROI de marketing automation?",
         "Métricas centrais: taxa de conversão de leads por estágio, receita atribuída a campanhas automatizadas (com modelo de atribuição definido), redução do custo por lead qualificado, aumento da velocidade do pipeline (tempo de lead a cliente) e redução do trabalho manual da equipe de marketing. Compare a performance antes e após a automação para demonstrar impacto concreto ao financeiro."),
    ]
)

# ── Article 5500 — Clinic: Ortopedia Pediátrica e Medicina do Esporte Infanto-Juvenil ──
art(
    slug="gestao-de-clinicas-de-ortopedia-pediatrica-e-medicina-do-esporte-infanto-juvenil",
    title="Gestão de Clínicas de Ortopedia Pediátrica e Medicina do Esporte Infanto-Juvenil | ProdutoVivo",
    desc="Guia de gestão para clínicas de ortopedia pediátrica e medicina do esporte infanto-juvenil: modelo assistencial, captação, tecnologia e crescimento. Para infoprodutores da saúde.",
    h1="Gestão de Clínicas de Ortopedia Pediátrica e Medicina do Esporte Infanto-Juvenil",
    lead="A ortopedia pediátrica e a medicina do esporte voltada para crianças e adolescentes formam uma subespecialidade de crescente demanda no Brasil, impulsionada pela maior prática esportiva infanto-juvenil e pela maior conscientização dos pais sobre saúde musculoesquelética. Para infoprodutores da saúde, esse é um nicho com público muito engajado e dores específicas bem definidas.",
    sections=[
        ("O Campo da Ortopedia Pediátrica no Brasil",
         "A ortopedia pediátrica trata condições musculoesqueléticas desde o nascimento até a adolescência: displasia do desenvolvimento do quadril (DDQ), pé torto congênito, escoliose idiopática do adolescente, epifisiólises e fraturas em crescimento, doenças osteocondrosadas (Perthes, Osgood-Schlatter) e deformidades angulares e rotacionais dos membros inferiores. A medicina do esporte infanto-juvenil soma as lesões relacionadas à prática esportiva em placa de crescimento aberta — condição que diferencia o tratamento pediátrico do adulto. A combinação dessas especialidades é relativamente escassa no Brasil, criando oportunidade de posicionamento em centros de referência."),
        ("Diagnóstico e Tecnologia em Ortopedia Pediátrica",
         "O diagnóstico em ortopedia pediátrica usa amplamente a ultrassonografia (excelente para DDQ em recém-nascidos e guia de procedimentos sem radiação), radiografia com técnicas de proteção gonadal, ressonância magnética (padrão-ouro para lesões de cartilagem e placa de crescimento) e, crescentemente, análise tridimensional de marcha para planejamento cirúrgico em paralisia cerebral e outras condições neuromusculares. Softwares de planejamento cirúrgico 3D e impressão de guias personalizadas elevam a precisão em osteotomias complexas. A telemedicina é especialmente valiosa nessa especialidade para famílias do interior que precisam de segunda opinião de centros de referência urbanos."),
        ("Modelo de Negócio e Relacionamento com Famílias",
         "A clínica de ortopedia pediátrica atende uma díade — a criança-paciente e seus pais, que são os tomadores de decisão. A comunicação com os pais exige clareza sobre diagnóstico (frequentemente com uso de imagens e modelos anatômicos), realismo sobre prognóstico e plano de tratamento detalhado. Pais ansiosos por filhos com condições ortopédicas são excelentes divulgadores quando a experiência é positiva — o marketing boca a boca é o canal mais eficiente na pediatria. Parcerias com pediatras e clínicas pediátricas que encaminham casos são fundamentais para o fluxo de novos pacientes."),
        ("Medicina do Esporte na Criança e Adolescente",
         "A medicina do esporte voltada para atletas infanto-juvenis cresce com a profissionalização precoce do esporte no Brasil (futebol, natação, ginástica artística, vôlei). As lesões mais comuns incluem apofisites (Osgood-Schlatter no joelho, Sever no calcanhar), lesões de placa de crescimento em ombro de arremessadores, e overuse injuries em jovens atletas com treinamento excessivo. A prevenção é tão importante quanto o tratamento: programas de avaliação de risco pré-temporada, condicionamento físico adequado à maturidade biológica (não apenas cronológica) e orientação nutricional são serviços complementares de alto valor."),
        ("Crescimento e Posicionamento como Referência Regional",
         "Clínicas de ortopedia pediátrica que constroem reputação de referência regional atraem casos complexos de toda uma região, justificando investimento em tecnologia diagnóstica e cirúrgica diferenciada. Participação em congressos da SBOP (Sociedade Brasileira de Ortopedia Pediátrica), publicação científica de casos e séries, e programas de telemedicina que ampliam o alcance geográfico são estratégias de posicionamento de longo prazo. Infoprodutores que criam conteúdo educativo para pais — sobre prevenção de lesões esportivas em jovens, quando buscar especialista para dores de crescimento — têm audiência massiva e engajada nas redes sociais."),
    ],
    faq_list=[
        ("Quando a dor no joelho de um adolescente deve ser investigada por ortopedista?",
         "Dor persistente por mais de 2 semanas, dor que piora com atividade esportiva e não melhora com repouso, dor noturna, limitação funcional ou alteração de marcha são sinais de alerta que justificam avaliação ortopédica. Osgood-Schlatter (dor na tuberosidade tibial) é comum e benigno, mas diagnóstico diferencial com outras condições mais sérias exige exame clínico especializado."),
        ("Escoliose em adolescentes sempre precisa de cirurgia?",
         "Não. A grande maioria dos casos de escoliose idiopática do adolescente é leve (menos de 20°) e apenas requer acompanhamento periódico. Curvas de 20-45° em adolescentes em crescimento podem necessitar de colete ortopédico. Cirurgia é indicada geralmente para curvas acima de 45-50° em crescimento ativo ou progressão documentada. O manejo depende do ângulo de Cobb, do potencial de crescimento restante e da progressão documentada em consultas periódicas."),
        ("Com que frequência crianças atletas devem ser avaliadas por ortopedista?",
         "Para atletas competitivos treinando mais de 15 horas semanais, uma avaliação pré-temporada anual é recomendável — incluindo avaliação de maturidade biológica, análise de simetria muscular e identificação de riscos de overuse. Para atletas de recreação, avaliação quando surgem queixas ou antes de aumento significativo de carga de treinamento. A prevenção de lesões em jovens atletas é muito mais efetiva (e econômica) que o tratamento."),
    ]
)

# ── Article 5501 — SaaS Sales: Escritórios de Arquitetura e Engenharia ──
art(
    slug="vendas-para-o-setor-de-saas-de-escritorios-de-arquitetura-e-engenharia",
    title="Vendas para o Setor de SaaS de Escritórios de Arquitetura e Engenharia | ProdutoVivo",
    desc="Como vender SaaS para escritórios de arquitetura e engenharia no Brasil: tomadores de decisão, dores do setor, abordagem consultiva e estratégias. Guia para infoprodutores.",
    h1="Vendas para o Setor de SaaS de Escritórios de Arquitetura e Engenharia",
    lead="Escritórios de arquitetura, engenharia e construção (AEC) enfrentam desafios únicos de gestão de projetos, colaboração em equipe e controle financeiro. Para infoprodutores e consultores de vendas B2B SaaS, esse segmento oferece oportunidade crescente impulsionada pela digitalização do setor e pela adoção de BIM.",
    sections=[
        ("O Setor AEC e sua Transformação Digital",
         "O setor de Arquitetura, Engenharia e Construção (AEC) é um dos últimos grandes segmentos a digitalizar processos de gestão. Escritórios de arquitetura gerenciam múltiplos projetos simultâneos com equipes multidisciplinares, clientes exigentes, prazos apertados e margens pressionadas. A adoção de BIM (Building Information Modeling) como metodologia de projeto cria infraestrutura técnica que facilita integração com sistemas de gestão. O Brasil aprovou o Decreto BIM (10.306/2020) que exige BIM em obras públicas, acelerando a adoção e criando demanda por ferramentas de gestão integradas à metodologia."),
        ("Dores Específicas do Setor AEC para SaaS",
         "As principais dores de escritórios de arquitetura e engenharia incluem: controle de horas por projeto e rentabilidade por trabalho, gestão de briefings e revisões de projeto com histórico completo de alterações, aprovação de documentos e controle de versões de pranchas e especificações, gestão financeira de contratos (cronograma de medições, aditivos, reajustes), comunicação estruturada com clientes e equipes em múltiplos projetos, e integração entre projeto (BIM/CAD) e gestão (ERP/PM). Escritórios que não gerenciam essas dimensões perdem dinheiro invisível em horas não faturadas e retrabalho."),
        ("Tomadores de Decisão e Ciclo de Compra",
         "Em escritórios pequenos (1-10 profissionais), o sócio-fundador decide e geralmente acumula todas as funções. Em escritórios médios e grandes, há separação entre sócios técnicos (arquitetos/engenheiros) e gestores administrativos, com o financeiro ou administrativo liderando a avaliação de sistemas. O ciclo de vendas é de 2-8 semanas, com demonstração prática sendo o momento decisivo. Mostrar o controle de horas e rentabilidade por projeto em tempo real, com interface que arquitetos e engenheiros acharão palatável (não um ERP industrial), é o ponto de conversão crítico."),
        ("Integrações e Diferenciação no Mercado AEC",
         "SaaS voltado para AEC precisa integrar-se com as ferramentas de projeto que já são usadas: AutoCAD, Revit, SketchUp, ArchiCAD. Integrações que importam dados de projetos (listas de materiais, cronogramas) para o sistema de gestão eliminam re-digitação e criam valor imediato. Diferenciadores específicos para o setor incluem: gestão de pranchas e revisões com controle de versão, módulo de medições para obras com cálculo de aditivos, portal do cliente para aprovação de documentos e comunicação, e relatórios de rentabilidade por hora de trabalho por tipologia de projeto."),
        ("Tendências: BIM Gestão, IA e Construção 4.0",
         "A integração de BIM com gestão de projetos cria o conceito de BIM de gestão — usar o modelo digital não apenas para projeto, mas para planejamento de obra, controle de qualidade em campo e gestão de facilities pós-entrega. IA para estimativa automática de custos a partir de modelos BIM, drones para levantamento e monitoramento de obras, e realidade aumentada para visualização de projetos in loco são tecnologias emergentes que transformam o setor AEC. Infoprodutores que documentam e ensinam essas inovações para arquitetos e engenheiros têm audiência crescente num setor em acelerada transformação."),
    ],
    faq_list=[
        ("Existe software de gestão específico para escritórios de arquitetura?",
         "Sim. Plataformas como Monograph, Archioffice, Newforma (internacional) e soluções brasileiras como Obra Prima e Prime Projetos atendem especificamente escritórios AEC com funcionalidades de gestão de projetos, horas, documentos e financeiro adaptadas para a realidade do setor. ERPs genéricos exigem muita customização para atender adequadamente as especificidades de contratos de projeto por fases, controle de pranchas e gestão de clientes de obra."),
        ("Como convencer um arquiteto de que precisa de sistema de gestão?",
         "Pergunte: 'você sabe qual projeto é mais rentável por hora trabalhada?' ou 'quantas horas de retrabalho você teve no último mês por revisões de cliente?'. A maioria não tem essa visibilidade. Mostre que escritórios que controlam horas e rentabilidade por projeto tomam decisões de precificação muito melhores, evitam aceitar projetos que parecem grandes mas são ruins de margem, e crescem com mais consistência financeira."),
        ("BIM e gestão de projetos podem ser integrados?",
         "Sim, e essa integração é o futuro do setor. Plataformas como Autodesk Construction Cloud e Trimble Connect integram BIM com gestão de obras e documentos. No Brasil, a adoção ainda é incipiente mas cresce com a obrigatoriedade de BIM em obras públicas. Escritórios que dominam BIM de gestão — não apenas BIM de projeto — estão à frente na transformação digital do setor AEC."),
    ]
)

# ── Article 5502 — Consulting: Modelos de Negócio Inovadores e Business Model Innovation ──
art(
    slug="consultoria-de-modelos-de-negocio-inovadores-e-business-model-innovation",
    title="Consultoria de Modelos de Negócio Inovadores e Business Model Innovation | ProdutoVivo",
    desc="Como estruturar consultoria de modelos de negócio inovadores: metodologias, frameworks, aplicações e precificação. Guia para infoprodutores e consultores.",
    h1="Consultoria de Modelos de Negócio Inovadores e Business Model Innovation",
    lead="Business Model Innovation (BMI) é a capacidade de reinventar como uma empresa cria, entrega e captura valor — muitas vezes de forma mais impactante do que inovar apenas em produto ou tecnologia. Para infoprodutores e consultores estratégicos, esse nicho combina frameworks renomados com demanda crescente em empresas que precisam reinventar sua proposta de valor.",
    sections=[
        ("Por Que Inovar no Modelo de Negócio?",
         "As maiores disrupções de mercado das últimas décadas não foram resultado de tecnologia superior, mas de modelos de negócio inovadores: Uber não inventou o carro, inventou o marketplace de mobilidade; Netflix não inventou o vídeo, reinventou a distribuição com streaming por assinatura; Airbnb não construiu hotéis, criou plataforma de hospitality peer-to-peer. Empresas estabelecidas que não revisitam seus modelos de negócio periodicamente correm risco de serem disrompidas por entrantes que encontram formas mais eficientes de servir o mesmo cliente. O consultor de BMI ajuda empresas a antes de serem disrompidas, a se disromper."),
        ("Frameworks de Business Model Innovation",
         "O Business Model Canvas (Osterwalder & Pigneur) é o framework mais adotado globalmente: 9 blocos que descrevem como a empresa cria, entrega e captura valor — proposta de valor, segmentos de clientes, canais, relacionamento com clientes, fontes de receita, recursos-chave, atividades-chave, parcerias e estrutura de custos. Complementares ao Canvas, o Value Proposition Canvas aprofunda a relação entre proposta de valor e necessidades do cliente, e o VTDF (Value, Technology, Delivery, Finance) framework analisa inovação em cada dimensão separadamente. Ferramentas como UNITE Canvas e Strategy Map ampliam o repertório para projetos mais complexos."),
        ("Aplicando BMI: Do Diagnóstico à Experimentação",
         "Um projeto de BMI começa pelo diagnóstico do modelo atual: quais pressupostos sustentam o negócio hoje? Onde estão as vulnerabilidades (dependências perigosas, clientes concentrados, canais em declínio)? O passo seguinte é a exploração de alternativas: sessões de ideação com stakeholders, benchmark de modelos inovadores em outros setores, análise de jobs-to-be-done não atendidos pelo modelo atual. As alternativas mais promissoras são prototipadas em pilotos controlados antes de escalar — derisking a inovação do modelo de negócio com aprendizado validado, na lógica lean startup aplicada a BMI."),
        ("BMI em Setores Tradicionais: Indústria, Varejo e Serviços",
         "A maior oportunidade de BMI está em setores tradicionais onde modelos de décadas nunca foram questionados. Na indústria: migração de venda de produto para serviço recorrente (Product-as-a-Service, industrial IoT + manutenção preditiva). No varejo: omnichannel integrado, D2C e assinaturas. Em serviços profissionais: de cobrança por hora para resultado, de projeto pontual para parceria de longo prazo. Empresas que lideraram transformações de modelo de negócio em seus setores capturaram crescimento desproporcional — criando estudo de caso poderoso para consultores que documentam e abordam esse tema."),
        ("Construindo Prática de BMI como Infoprodutor ou Consultor",
         "Infoprodutores e consultores de BMI se diferenciam com metodologia proprietária baseada em frameworks consagrados mas com contribuição original — a 'assinatura metodológica' que personifica a abordagem. Cases documentados de transformações de modelo de negócio bem-sucedidas são o ativo comercial mais valioso. Cursos sobre Business Model Canvas, workshops de ideação de modelos de negócio e facilitação de sessões estratégicas são formatos com alta demanda corporativa e willingness-to-pay elevado, especialmente quando associados a resultados concretos documentados."),
    ],
    faq_list=[
        ("Business Model Innovation é diferente de inovação de produto?",
         "Sim, e em geral mais impactante. Inovação de produto melhora o que você entrega. BMI reinventa como você entrega, para quem, por quais canais e como captura valor. Uma empresa pode ter o produto mais inovador do mercado mas fracassar com modelo de negócio errado — e vice-versa. As maiores criações de valor corporativo da história recente (Amazon, Alibaba, Spotify) combinaram ambas, mas o modelo de negócio frequentemente foi o diferencial decisivo."),
        ("Como facilitar uma sessão de Business Model Canvas com equipes?",
         "Estruture em 3-4 horas com equipe multidisciplinar (máximo 8-10 pessoas): comece com o cliente — segmentos e proposta de valor (2 blocos), depois mapeie canais e relacionamento (2 blocos), em seguida fontes de receita, recursos e atividades-chave, parcerias e custos. Use post-its físicos ou Miro/Mural digitais. O facilitador deve fazer perguntas desafiadoras que questionem pressupostos — 'por que esse canal específico?', 'qual segmento pagaria mais por essa proposta?'. O Canvas é mais valioso pelo diálogo que gera do que pelo resultado estático."),
        ("Qual o risco de inovar no modelo de negócio em empresa estabelecida?",
         "O maior risco é o conflito com o modelo existente (innovator's dilemma): o novo modelo pode canibalizar receita atual, criar conflito com parceiros estabelecidos ou exigir capacidades que a empresa não tem. A forma de mitigar é criar unidade separada com autonomia para experimentar o novo modelo sem as restrições e os objetivos de curto prazo do core business. Quando o novo modelo valida seu potencial, integra-se ou coexiste com o legado em transição gradual."),
    ]
)

# ── Sitemap update ──
sm_path = pathlib.Path(__file__).parent / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")
new_urls = ""
for slug in [
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-acesso-e-identidade-iam",
    "gestao-de-clinicas-de-reproducao-humana-assistida-e-fertilidade",
    "vendas-para-o-setor-de-saas-de-cervejarias-artesanais-e-produtores-de-bebidas",
    "consultoria-de-gestao-de-key-accounts-e-strategic-account-management",
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-automacao-de-marketing",
    "gestao-de-clinicas-de-ortopedia-pediatrica-e-medicina-do-esporte-infanto-juvenil",
    "vendas-para-o-setor-de-saas-de-escritorios-de-arquitetura-e-engenharia",
    "consultoria-de-modelos-de-negocio-inovadores-e-business-model-innovation",
]:
    new_urls += f"\n  <url><loc>{DOMAIN}/blog/{slug}/</loc></url>"
sm_path.write_text(sm.replace("</urlset>", new_urls + "\n</urlset>"), encoding="utf-8")

# ── Trilha update ──
tr_path = pathlib.Path(__file__).parent / "trilha.html"
tr = tr_path.read_text(encoding="utf-8")
new_items = ""
for slug, label in [
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-gestao-de-acesso-e-identidade-iam", "Gestão de Acesso e Identidade (IAM) SaaS"),
    ("gestao-de-clinicas-de-reproducao-humana-assistida-e-fertilidade", "Reprodução Humana Assistida e Fertilidade"),
    ("vendas-para-o-setor-de-saas-de-cervejarias-artesanais-e-produtores-de-bebidas", "Cervejarias Artesanais e Produtores de Bebidas SaaS"),
    ("consultoria-de-gestao-de-key-accounts-e-strategic-account-management", "Gestão de Key Accounts e Strategic Account Management"),
    ("gestao-de-negocios-de-empresa-de-b2b-saas-de-automacao-de-marketing", "Automação de Marketing SaaS"),
    ("gestao-de-clinicas-de-ortopedia-pediatrica-e-medicina-do-esporte-infanto-juvenil", "Ortopedia Pediátrica e Medicina do Esporte Infanto-Juvenil"),
    ("vendas-para-o-setor-de-saas-de-escritorios-de-arquitetura-e-engenharia", "Escritórios de Arquitetura e Engenharia SaaS"),
    ("consultoria-de-modelos-de-negocio-inovadores-e-business-model-innovation", "Modelos de Negócio Inovadores e Business Model Innovation"),
]:
    new_items += f'\n    <li><a href="{DOMAIN}/blog/{slug}/">{label}</a></li>'
tr_path.write_text(tr.replace("</ul>", new_items + "\n  </ul>", 1), encoding="utf-8")

print("Done — batch 2006")
