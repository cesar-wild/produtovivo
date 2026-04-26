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
<link rel="canonical" href="{canonical}"/>
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
footer{{text-align:center;padding:2rem 1rem;font-size:.85rem;color:#666}}
a{{color:#0a7c4e}}
</style>
</head>
<body>
<header><h1>{h1}</h1></header>
<main>
<p><em>{lead}</em></p>
{sections_html}
<section class="faq-block">
<h2>Perguntas Frequentes</h2>
{faq_html}
</section>
</main>
<footer><p>&copy; 2025 ProdutoVivo &mdash; <a href="{domain}">produtovivo.com.br</a></p></footer>
</body>
</html>"""

def art(slug, title, desc, h1, lead, sections, faq_list):
    canonical = f"{DOMAIN}/blog/{slug}/"
    sections_html = "\n".join(f"<h2>{h}</h2><p>{p}</p>" for h, p in sections)
    faq_html = "\n".join(
        f'<div class="faq"><strong>{q}</strong><p>{a}</p></div>' for q, a in faq_list
    )
    schema = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": q,
                               "acceptedAnswer": {"@type": "Answer", "text": a}}
                              for q, a in faq_list]}
    html = TMPL.format(title=title, desc=desc, canonical=canonical, pixel=PIXEL,
                       faq_schema=json.dumps(schema, ensure_ascii=False),
                       h1=h1, lead=lead, domain=DOMAIN,
                       sections_html=sections_html, faq_html=faq_html)
    out = pathlib.Path(BASE) / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"  {slug}")

# ── BATCH 1842 — artigos 5167–5174 ──────────────────────────────────────────

# 5167 — B2B SaaS: Insurtech e Seguradoras
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-insurtech-e-seguradoras",
    title="Gestão de Negócios de Empresa de B2B SaaS de Insurtech e Seguradoras | ProdutoVivo",
    desc="Guia para escalar SaaS voltado para o mercado de seguros: corretoras, seguradoras e insurtechs. Vendas B2B, regulatório, precificação e retenção.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Insurtech e Seguradoras",
    lead="O mercado de seguros no Brasil movimenta mais de R$400 bilhões por ano e está em plena transformação digital. Insurtechs e plataformas SaaS para corretoras e seguradoras têm uma janela única de crescimento — mas precisam navegar um ambiente altamente regulado pela SUSEP.",
    sections=[
        ("O Ecossistema de Insurtech no Brasil",
         "O mercado de seguros brasileiro é dominado por grandes grupos como Porto Seguro, Bradesco Seguros e SulAmérica, mas o ecossistema de insurtechs cresce aceleradamente. Plataformas SaaS para o setor atendem múltiplos segmentos: sistemas de gestão para corretoras de seguros (CRM, cotação, emissão), plataformas de comparação e distribuição digital, ferramentas de underwriting automatizado com IA, sistemas de gestão de sinistros, e plataformas de análise de risco. Cada segmento tem regulação e requisitos técnicos específicos — o compliance com a SUSEP (Superintendência de Seguros Privados) é não-negociável."),
        ("Regulação e Compliance como Diferencial",
         "A regulação da SUSEP é ao mesmo tempo uma barreira de entrada e um diferencial competitivo para SaaS que já passou pela adequação. Plataformas que entregam compliance nativo — relatórios regulatórios automáticos, armazenamento de apólices conforme exigência legal, gestão de agentes corretores registrados na SUSEP — vendem mais facilmente para corretoras que temem autuações. O Sandbox Regulatório da SUSEP, criado em 2020, também abre espaço para insurtechs testarem produtos inovadores com supervisão regulatória flexível, reduzindo a barreira para novos entrantes com modelos disruptivos."),
        ("Ciclo de Vendas para Corretoras",
         "Corretoras de seguros são o principal cliente de SaaS no setor — há mais de 100 mil corretoras ativas no Brasil, a maioria de pequeno porte. O decisor é o próprio corretor ou seu sócio, e o critério de decisão é pragmático: integração com as principais seguradoras do mercado (Porto, Tokio Marine, Zurich), facilidade de uso para emissão e renovação de apólices, e custo-benefício claro. Estratégias de aquisição eficazes incluem parcerias com entidades do setor (FENACOR, sindicatos estaduais), presença em eventos como o CQCS (Congresso de Qualidade em Seguros), e campanhas de indicação entre corretores."),
        ("Precificação e Modelos de Receita",
         "Os modelos de precificação em SaaS para seguros incluem: mensalidade por usuário (adequado para corretoras com equipe), comissão sobre prêmio emitido pela plataforma (percentual das apólices processadas), e mensalidade escalonada por volume de apólices ativas. O modelo de comissão sobre prêmio alinha os incentivos com o crescimento do cliente, mas gera receita variável difícil de prever. A mensalidade fixa com teto de transações é mais previsível para o SaaS e mais fácil de justificar para corretoras menores. Plataformas que conseguem cobrar tanto mensalidade quanto taxa de transação para funcionalidades premium têm as maiores margens."),
        ("Retenção e Expansão no Mercado de Seguros",
         "Churn em SaaS para corretoras é baixo quando a plataforma está integrada ao dia a dia de emissão de apólices — o custo de troca inclui migrar histórico de clientes, reconfigurar integrações com seguradoras e retreinar a equipe. O maior risco de churn é a concorrência de sistemas próprios de grandes seguradoras que oferecem plataformas gratuitas para corretoras exclusivas. A resposta é multisseguradora: oferecer integração com o maior número possível de seguradoras para que o corretor independente nunca precise ser exclusivo. Expansão de receita vem de módulos adicionais: gestão financeira da corretora, portal do segurado, e automatização de renovações."),
    ],
    faq_list=[
        ("Quais integrações são essenciais para um SaaS de corretoras de seguros?",
         "As integrações prioritárias são com as maiores seguradoras do mercado (Porto Seguro, Bradesco, Tokio Marine, Zurich, SulAmérica) via APIs de cotação e emissão, com sistemas de emissão da SUSEP para registros obrigatórios, e com plataformas de comparação como Minuto Seguros e Youse. Integração com softwares de contabilidade (Omie, Conta Azul) para a gestão financeira da corretora é um diferencial relevante para corretoras de médio porte."),
        ("Como lidar com a concorrência de plataformas gratuitas de seguradoras?",
         "A resposta é independência e completude: a plataforma independente oferece visão consolidada de todos os ramos e seguradoras, enquanto sistemas próprios de seguradoras são limitados ao seu portfólio. O argumento de vendas é claro: um corretor que usa o sistema da Porto só vende Porto — um corretor que usa uma plataforma independente escolhe o melhor produto para cada cliente e tem muito mais capacidade de fidelizar sua carteira."),
        ("Como o ProdutoVivo ajuda profissionais do mercado de seguros?",
         "O guia ProdutoVivo ensina como transformar conhecimento técnico — planejamento de proteção patrimonial, seguros de vida e previdência, gestão de riscos empresariais — em cursos online e apps interativos. Corretores e consultores de seguros podem criar produtos digitais que educam seus clientes e prospectos, construindo autoridade e gerando leads qualificados para sua carteira."),
    ]
)

# 5168 — Clínica: Dermatologia e Estética Médica
art(
    slug="gestao-de-clinicas-de-dermatologia-e-estetica-medica",
    title="Gestão de Clínicas de Dermatologia e Estética Médica | ProdutoVivo",
    desc="Guia completo de gestão para clínicas de dermatologia e estética médica: mix de procedimentos, precificação, retenção de pacientes e marketing digital.",
    h1="Gestão de Clínicas de Dermatologia e Estética Médica",
    lead="Dermatologia é uma das especialidades médicas com maior potencial de receita complementar via procedimentos estéticos — lasers, toxina botulínica, preenchimentos, peelings. Clínicas que equilibram bem a dermatologia clínica com a estética médica constroem fluxo de caixa robusto e base de pacientes fidelizada.",
    sections=[
        ("O Mercado de Dermatologia e Estética Médica",
         "O Brasil é o segundo maior mercado de procedimentos estéticos do mundo, atrás apenas dos EUA. Dermatologistas têm uma posição privilegiada nesse mercado: são os únicos especialistas médicos com formação completa em saúde da pele, o que lhes permite atender tanto a demanda clínica (dermatites, psoríase, acne, câncer de pele) quanto a estética (rejuvenescimento, harmonização facial, tratamento corporal). Clínicas que combinam dermatologia clínica — que traz pacientes via convênios e encaminhamentos — com estética médica — que gera receita particular de alto ticket — têm o modelo de negócio mais robusto da especialidade."),
        ("Mix de Procedimentos e Gestão de Equipamentos",
         "A gestão de equipamentos é um dos maiores desafios financeiros em dermatologia estética: lasers fracionados, Nd:YAG, CO2, IPL, equipamentos de radiofrequência e ultrassom focado representam investimentos de R$150-500k cada. A decisão de comprar versus alugar deve considerar o volume de procedimentos necessários para amortizar o equipamento (geralmente 18-36 meses para equipamentos well-positioned). Clínicas que diversificam o portfólio de procedimentos — reduzindo a dependência de um único equipamento — têm maior resiliência operacional e capacidade de atender diferentes perfis de pacientes."),
        ("Precificação de Procedimentos Estéticos",
         "A precificação em estética médica é complexa: o mesmo procedimento (toxina botulínica, por exemplo) pode ser cobrado por área tratada, por unidade de produto, ou por sessão — e os preços variam enormemente por região e posicionamento da clínica. Estratégias eficazes incluem: precificar por resultado esperado (não só por insumo usado), criar pacotes de tratamento (combinando sessões de diferentes procedimentos para o mesmo objetivo estético) com desconto progressivo, e oferecer planos de manutenção anuais com preço diferenciado para fidelizar pacientes de retorno frequente."),
        ("Marketing Digital e Captação de Pacientes",
         "Dermatologia estética é uma das especialidades médicas mais ativas em marketing digital — Instagram e TikTok são os canais mais eficazes para mostrar resultados de procedimentos (sempre com consentimento do paciente e dentro das normas do CFM). Antes e depois, depoimentos em vídeo, e conteúdo educativo sobre cuidados com a pele têm alto engajamento. Google Ads para buscas de procedimentos específicos (botox, laser, peeling) converte bem quando combinado com landing pages otimizadas. O CRM deve gerenciar o ciclo de retorno — procedimentos de manutenção (toxina botulínica a cada 4-6 meses, preenchimentos a cada 12-18 meses) são lembretes programáveis que garantem receita recorrente."),
        ("Compliance e Regulação na Estética Médica",
         "A estética médica é um território com regulação em constante evolução. O CFM (Conselho Federal de Medicina) regulamenta quais procedimentos são exclusivos de médicos, e entidades como a SBD (Sociedade Brasileira de Dermatologia) publicam diretrizes de boas práticas. Clínicas que treinam a equipe regularmente em segurança de procedimentos, mantêm protocolos escritos e documentam consentimento informado detalhado têm menor exposição a processos no CRM e BO. A rastreabilidade de produtos (lotes de toxina botulínica, preenchimentos) é especialmente importante para recall de produtos e para defesa em eventuais queixas."),
    ],
    faq_list=[
        ("Como estruturar um programa de fidelidade para pacientes de estética médica?",
         "O modelo mais eficaz é baseado em créditos: cada procedimento realizado gera créditos que podem ser trocados por descontos em procedimentos futuros ou produtos de skincare. Alternativamente, planos anuais com sessões pré-pagas (ex: 4 sessões de toxina botulínica + 2 peelings por um valor fixo anual com 15% de desconto) garantem recorrência e previsibilidade de receita. A chave é que o paciente sinta que está sendo recompensado pela fidelidade — não apenas comprando antecipado."),
        ("Como lidar com a sazonalidade em clínicas de estética?",
         "Estética médica tem sazonalidade clara: pico de demanda em janeiro-março (verão/carnaval) e setembro-novembro (pré-festas de fim de ano). O contra-pico é abril-junho. Estratégias para suavizar a sazonalidade incluem: promoções de procedimentos de resultado gradual (lasers, bioestimuladores) nos meses fracos, campanhas de manutenção para pacientes que fizerem procedimentos no período de baixa, e diversificação para dermatologia clínica (que tem demanda mais constante durante o ano)."),
        ("Como o ProdutoVivo pode ajudar dermatologistas e esteticistas?",
         "O guia ProdutoVivo ensina como transformar expertise em cuidados com a pele em cursos online e apps interativos para pacientes e profissionais. Um dermatologista pode criar um programa digital de skincare personalizado, um curso de protocolo de tratamento de acne ou um app de acompanhamento de tratamento — gerando renda recorrente e construindo autoridade como referência na especialidade."),
    ]
)

# 5169 — SaaS Sales: Educação Básica (Escolas e Colégios)
art(
    slug="vendas-para-o-setor-de-saas-de-educacao-basica-escolas-e-colegios",
    title="Vendas para o Setor de SaaS de Educação Básica: Escolas e Colégios | ProdutoVivo",
    desc="Guia de vendas B2B para plataformas SaaS voltadas a escolas e colégios: como abordar diretores, demonstrar valor pedagógico e fechar contratos anuais.",
    h1="Vendas para o Setor de SaaS de Educação Básica: Escolas e Colégios",
    lead="O mercado de edtech para escolas de educação básica no Brasil tem mais de 180 mil estabelecimentos de ensino como potenciais clientes — da rede pública a colégios particulares de alto padrão. Vender SaaS para educação exige entender a cultura escolar e o ciclo orçamentário único desse setor.",
    sections=[
        ("O Mercado de SaaS para Educação Básica",
         "A tecnologia na educação básica cobre múltiplas categorias: sistemas de gestão escolar (ERP educacional com matrículas, notas, frequência, financeiro), plataformas de aprendizado adaptativo e conteúdo digital, comunicação escola-família (apps de recados, agenda digital), segurança escolar (controle de acesso, monitoramento), e ferramentas de gestão pedagógica para coordenadores. O mercado se divide entre rede pública (licitações, volumes altos, margens baixas, ciclos longos) e rede privada (decisão mais ágil, maior disposição a pagar por qualidade). SaaS para escolas privadas de médio e alto padrão oferece a melhor relação entre ticket e ciclo de venda."),
        ("O Ciclo Orçamentário das Escolas",
         "Escolas têm um ciclo orçamentário muito específico: as decisões de compra de tecnologia para o ano letivo seguinte são tomadas entre agosto e novembro do ano anterior. Esse é o momento em que diretores e mantenedores avaliam renovações de contrato e novas ferramentas. Chegar com uma proposta em fevereiro — no início do ano letivo — é quase sempre tarde demais. O planejamento de vendas para edtech precisa concentrar prospecção intensiva no segundo semestre e ter ciclos de nurturing longos para fechar no período de planejamento orçamentário."),
        ("Perfis de Decisão nas Escolas",
         "O processo de decisão em escolas envolve múltiplos stakeholders: o diretor pedagógico avalia o impacto no ensino e na experiência do aluno, o diretor administrativo avalia custo e integração com sistemas existentes, e o mantenedor (dono da escola ou congregação) aprova o investimento. Em redes de colégios, há também um responsável de TI corporativo. A venda eficaz mapeia todos os stakeholders desde o início, apresenta argumentos diferentes para cada perfil (pedagógico para o diretor pedagógico, ROI financeiro para o administrativo) e identifica o champion interno que vai defender a proposta perante o mantenedor."),
        ("Demonstração de Valor em Contexto Escolar",
         "A venda de SaaS para escolas falha quando é puramente técnica — demonstrar funcionalidades não convence um diretor pedagógico. O que converte é mostrar impacto concreto: 'com nossa plataforma, pais têm acesso em tempo real à frequência e notas, o que reduziu em 40% as ligações à secretaria nessa escola em SP'; 'o módulo de comunicação aumentou o NPS de pais em 25 pontos'. Casos de escolas similares (mesmo porte, mesmo modelo pedagógico, mesma região) são os argumentos mais poderosos. Pilotos gratuitos de 30-60 dias com uma turma ou série escolhida pela escola criam evidências locais antes do contrato completo."),
        ("Retenção e Expansão em SaaS para Escolas",
         "Churn em SaaS escolar é baixo por razões práticas: migrar dados de alunos, notas e histórico acadêmico é complexo e doloroso. Mas o risco real é renovação sem expansão — escolas que usam apenas funcionalidades básicas e nunca adotam módulos premium. Customer Success proativo que mostra novas funcionalidades antes da renovação, sessões de treinamento para novos professores e coordenadores no início de cada ano letivo, e relatórios de uso que mostram quanto a escola está aproveitando da plataforma são as melhores ferramentas de expansão de receita."),
    ],
    faq_list=[
        ("Como participar de licitações para vender SaaS para escolas públicas?",
         "O processo de licitação para escolas públicas exige: CNPJ ativo com certidões negativas, cadastro no portal de compras governamentais (Comprasnet federal, portais estaduais e municipais), proposta técnica e comercial dentro das exigências do edital, e capacidade de atender o volume contratado. O ciclo é longo (6-18 meses da publicação ao contrato) e o preço é o principal critério de seleção no pregão eletrônico. Para startups de SaaS, uma estratégia alternativa é forar a rede particular antes e usar esses contratos como referência para depois disputar licitações com credibilidade estabelecida."),
        ("Qual o ticket médio e modelo de precificação para SaaS escolar?",
         "O modelo de precificação mais aceito é por aluno matriculado: escolas de 200-500 alunos pagam tipicamente R$15-35/aluno/mês, escolas maiores negociam desconto por volume. Contratos anuais com pagamento antecipado ou parcelado são a norma, alinhando-se ao calendário orçamentário escolar. Redes de colégios (franquias, grupos educacionais) demandam precificação consolidada com desconto de volume significativo, mas representam contratos de alto valor e baixo custo marginal de suporte."),
        ("Como o ProdutoVivo ajuda educadores e gestores escolares?",
         "O guia ProdutoVivo ensina professores, coordenadores e especialistas em educação a transformar metodologias pedagógicas e conteúdos educativos em cursos online e apps interativos. Um educador experiente pode criar um produto digital — curso de formação de professores, metodologias ativas, gestão de sala de aula — e gerar renda recorrente como infoprodutor no mercado de educação."),
    ]
)

# 5170 — Consulting: Transformação Digital e Inovação Corporativa
art(
    slug="consultoria-de-transformacao-digital-e-inovacao-corporativa",
    title="Consultoria de Transformação Digital e Inovação Corporativa | ProdutoVivo",
    desc="Como estruturar uma consultoria de transformação digital e inovação para médias e grandes empresas: metodologia, entregáveis, precificação e resultados.",
    h1="Consultoria de Transformação Digital e Inovação Corporativa",
    lead="Transformação digital deixou de ser tendência para se tornar imperativo competitivo — e empresas de todos os setores buscam consultores capazes de guiar essa jornada de forma prática, com resultados mensuráveis e sem a teoria vaga que domina muitas iniciativas de inovação.",
    sections=[
        ("O Que É (e o Que Não É) Transformação Digital",
         "Transformação digital não é apenas comprar tecnologia ou digitalizar processos analógicos. É uma mudança profunda no modelo de negócio, na cultura organizacional e nos processos internos — habilitada por tecnologia. Consultores eficazes de transformação digital começam pelo diagnóstico de maturidade digital: onde a empresa está hoje em termos de dados, automação, experiência do cliente digital e cultura de inovação. Esse diagnóstico evita o erro mais comum: começar pela solução tecnológica antes de entender o problema de negócio. Empresas que compram ERPs, CRMs e plataformas de dados sem uma estratégia clara de adoção desperdiçam o investimento."),
        ("Metodologia de Diagnóstico de Maturidade Digital",
         "O modelo de maturidade digital mais usado em consultorias avalia cinco dimensões: estratégia (a liderança tem visão clara do papel do digital no negócio?), experiência do cliente (os touchpoints digitais são fluidos e integrados?), operações (os processos internos são automatizados e orientados por dados?), tecnologia e dados (a infraestrutura suporta inovação ágil?) e pessoas e cultura (o time tem as competências digitais necessárias?). O diagnóstico gera um roadmap de transformação com iniciativas priorizadas por impacto e esforço — o famoso '2x2 impact vs. effort' que orienta o plano de ação."),
        ("Design de Iniciativas de Inovação",
         "A entrega mais valorizada em consultoria de inovação é o design e facilitação de programas de inovação corporativa: hackathons internos, laboratórios de inovação (labs), programas de intraempreendedorismo e parcerias com startups (corporate venture e programas de open innovation). Consultores que dominam a facilitação de sprints de design thinking e lean startup dentro de corporações — adaptando a velocidade das startups ao contexto de governança das grandes empresas — têm alta demanda e contratos recorrentes. A chave é criar mecanismos de inovação que sobrevivam ao consultor: processos e rituais que a equipe interna adota como rotina."),
        ("Gestão da Mudança e Adoção Tecnológica",
         "Falhas de transformação digital raramente são técnicas — são humanas. A resistência à mudança, a falta de treinamento adequado e a ausência de comunicação clara sobre o 'porquê' das mudanças são as causas mais comuns de projetos que entregam tecnologia mas não entregam transformação. Consultores que integram gestão da mudança (change management) na sua metodologia — com planos de comunicação, treinamento por persona, rituais de feedback e mecanismos de reconhecimento para early adopters — entregam projetos com adoção muito superior. A metodologia ADKAR (Awareness, Desire, Knowledge, Ability, Reinforcement) é amplamente usada nesse contexto."),
        ("Precificação e Estrutura de Projetos",
         "Projetos de transformação digital variam enormemente em escopo: de um diagnóstico de maturidade (R$30-80k, 4-8 semanas) a um programa de transformação completo (R$500k-2M+, 12-24 meses). A estrutura mais comum é faseada: diagnóstico e roadmap (fase 1, menor investimento, menor risco para o cliente), implementação de iniciativas prioritárias (fase 2, maior valor, baseada nos resultados da fase 1), e sustentação e evolução (fase 3, retainer de acompanhamento). A progressão de fases naturalmente aumenta o engajamento e o faturamento por cliente ao longo do tempo."),
    ],
    faq_list=[
        ("Quais certificações e formações são relevantes para consultores de transformação digital?",
         "As mais reconhecidas no mercado brasileiro são: certificações em metodologias ágeis (SAFe, Scrum, Kanban), design thinking (IDEO U, Stanford d.school), gestão da mudança (PROSCI/ADKAR), cloud (AWS, Azure, Google Cloud) e análise de dados (Google Analytics, Power BI). MBA em Gestão da Inovação ou Transformação Digital em instituições como FGV, Insper ou USP reforça a credibilidade. Para atuação em grandes corporações, a experiência prévia em gestão interna (CTO, CDO, gerente de inovação) é frequentemente mais valorizada do que certificações."),
        ("Como evitar que projetos de transformação digital virem apenas 'implantação de software'?",
         "O antídoto é começar sempre pelo problema de negócio, nunca pela solução tecnológica. O contrato deve incluir entregáveis de processo e cultura — não apenas de tecnologia implantada. Métricas de sucesso devem incluir adoção (% de usuários ativos), mudança de comportamento (tempo economizado, decisões orientadas por dados) e impacto no negócio (receita, custo, NPS) — nunca apenas 'sistema implantado no prazo'."),
        ("Como o ProdutoVivo ajuda consultores de transformação digital?",
         "O guia ProdutoVivo ensina como transformar metodologias de inovação e transformação digital em cursos online e apps interativos para líderes empresariais. Um consultor de transformação digital pode criar um programa de capacitação em inovação para gerentes e diretores — gerando receita recorrente e construindo uma audiência de potenciais clientes de consultoria."),
    ]
)

# 5171 — B2B SaaS: Logística e Rastreamento de Frota
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-logistica-e-rastreamento-de-frota",
    title="Gestão de Negócios de Empresa de B2B SaaS de Logística e Rastreamento de Frota | ProdutoVivo",
    desc="Guia para escalar SaaS de logística e rastreamento de frota no Brasil: aquisição, precificação, expansão de receita e diferenciação em mercado competitivo.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Logística e Rastreamento de Frota",
    lead="O mercado de tecnologia para logística e gestão de frota no Brasil é um dos maiores da América Latina. Com mais de 1,5 milhão de veículos pesados e frotas corporativas de todos os tamanhos, o potencial de expansão para SaaS de rastreamento, roteirização e telemetria é imenso.",
    sections=[
        ("O Mercado de Tecnologia para Logística no Brasil",
         "A logística representa cerca de 12% do PIB brasileiro — e a ineficiência logística é um dos maiores problemas competitivos do país. SaaS para logística atende múltiplos segmentos: rastreamento e monitoramento de frota (GPS, telemetria, alertas de desvio de rota), roteirização inteligente (otimização de entregas com múltiplos pontos), gestão de motoristas e documentação (habilitações, CRLV, laudos), controle de combustível e manutenção preventiva, e integração com TMS (Transportation Management Systems) para operações complexas. Cada segmento tem diferentes ICPs e ciclos de venda."),
        ("Segmentação de Clientes e ICP",
         "O ICP em SaaS de frota varia do micro ao enterprise: empresas com 5-20 veículos (frotas leves corporativas, pequenas distribuidoras) são adquiridas com processo self-service ou inside sales de baixo custo; empresas com 20-200 veículos (transportadoras médias, redes de distribuição, frotas de serviços) exigem vendas consultivas com demonstração do ROI; acima de 200 veículos (grandes transportadoras, frotas industriais, agronegócio) o processo é enterprise com múltiplos stakeholders e integração complexa. Definir claramente qual segmento o produto atende melhor e concentrar a máquina de vendas nesse ICP é fundamental para eficiência de CAC."),
        ("Hardware, Software e o Modelo Híbrido",
         "A maioria das soluções de rastreamento de frota combina hardware (rastreador GPS instalado no veículo) com software (plataforma de monitoramento e analytics). Esse modelo híbrido cria complexidades: custo de instalação, logística de hardware, manutenção de dispositivos e gestão de conectividade (chips de dados). Empresas que conseguem terceirizar a instalação via rede de parceiros e simplificar o hardware (dispositivos plug-and-play) reduzem drasticamente o CAC e o custo de suporte. A tendência é de hardwares cada vez mais baratos e commoditizados, com diferenciação crescente na camada de software e analytics."),
        ("Precificação e Retenção",
         "O modelo de precificação mais comum é mensalidade por veículo monitorado, tipicamente R$30-150/veículo/mês dependendo dos módulos contratados e da qualidade do serviço. O churn está fortemente ligado à percepção de valor: frotas que recebem alertas críticos que evitam acidentes ou roubos raramente cancelam — o ROI é imediato e concreto. O maior risco de churn é a troca por concorrentes que oferecem preço menor — a resposta é diferenciar em qualidade de dados, tempo de atualização do GPS, confiabilidade do sistema e suporte técnico. SLAs de uptime e tempo de resposta de suporte são diferenciais de retenção em mercados competitivos."),
        ("Expansão de Receita e Cross-sell",
         "Clientes de rastreamento básico são os melhores candidatos para expansão para módulos premium: telemetria avançada (consumo de combustível por motorista, comportamento de condução, fadiga), gestão de manutenção preditiva, câmera embarcada (dashcam com IA para análise de comportamento de motorista), e integração com seguradores para desconto de apólice baseado em comportamento (usage-based insurance). Parcerias com seguradoras para oferecer desconto de seguro de frota para usuários da plataforma criam um benefício tangível que reduz churn e aumenta conversão de novos clientes."),
    ],
    faq_list=[
        ("Como competir com soluções de rastreamento de baixo custo (R$20-30/veículo)?",
         "Soluções de baixíssimo custo geralmente entregam rastreamento básico sem analytics, suporte precário e uptime questionável. A competição não é no preço — é no valor: mostrar com dados reais o custo de um veículo roubado sem recuperação eficaz, o custo de combustível desperdiçado por mau comportamento de motorista, e o valor de uma manutenção preventiva que evita uma quebra em estrada. O ROI de uma solução premium de R$100/veículo/mês se paga com a recuperação de 1% de eficiência em combustível em uma frota de 50 caminhões."),
        ("Qual a melhor forma de expandir para o segmento de agronegócio?",
         "O agronegócio tem uma frota enorme e específica: máquinas agrícolas (colheitadeiras, tratores), caminhões de transporte de grãos e implementos. A abordagem mais eficaz é especializar a plataforma para o calendário agrícola (rastreamento de máquinas na colheita, controle de horas de operação para manutenção) e buscar parcerias com revendedoras de máquinas agrícolas (Case IH, John Deere) que podem oferecer o SaaS como serviço complementar na venda dos equipamentos."),
        ("Como o ProdutoVivo ajuda profissionais de logística?",
         "O guia ProdutoVivo ensina como transformar expertise em gestão de frotas, logística e supply chain em cursos online e apps interativos para gestores e motoristas. Um especialista em logística pode criar treinamentos de redução de custo de frota, gestão de motoristas ou otimização de rotas — gerando renda como infoprodutor enquanto constrói autoridade no setor."),
    ]
)

# 5172 — Clínica: Nutrição Clínica e Funcional
art(
    slug="gestao-de-clinicas-de-nutricao-clinica-e-funcional",
    title="Gestão de Clínicas de Nutrição Clínica e Funcional | ProdutoVivo",
    desc="Guia de gestão para clínicas e consultórios de nutrição: modelos de atendimento, fidelização, telemedicina, planos alimentares digitais e marketing para nutricionistas.",
    h1="Gestão de Clínicas de Nutrição Clínica e Funcional",
    lead="Nutrição é uma das profissões da saúde com maior potencial de digitalização do atendimento. Nutricionistas que estruturam clínicas bem geridas — com mix inteligente de presencial e telemedicina, protocolos padronizados e marketing digital eficaz — constroem negócios escaláveis e de alta recorrência.",
    sections=[
        ("O Mercado de Nutrição no Brasil",
         "O Brasil tem mais de 130 mil nutricionistas registrados no CFN, mas a maioria atua de forma autônoma ou em ambientes hospitalares. O movimento de abertura de clínicas e consultórios particulares de nutrição cresce com o interesse crescente da população em saúde preventiva, longevidade e performance esportiva. Nichos com maior potencial de ticket premium incluem: nutrição oncológica, nutrição esportiva de alta performance, nutrição funcional e longevidade, nutrição materno-infantil e nutrição para doenças crônicas (diabetes, hipertensão, doença celíaca). A especialização em um nicho específico permite posicionamento como referência e preços superiores ao mercado genérico."),
        ("Modelos de Atendimento e Telemedicina",
         "A pandemia acelerou definitivamente a adoção da telenutrição (atendimento nutricional por teleconsulta), que é regulamentada pelo CFN desde 2020. O modelo híbrido — primeira consulta presencial para avaliação completa (bioimpedância, exames, histórico), com acompanhamentos mensais por teleconsulta — otimiza o tempo do nutricionista e a conveniência do paciente. Clínicas que adotam plataformas de telemedicina integradas ao prontuário nutricional eletrônico conseguem atender geografias além da cidade-sede, expandindo significativamente o potencial de mercado."),
        ("Protocolos, Planos Alimentares e Digitalização",
         "A padronização de protocolos clínicos é um dos maiores alavancadores de produtividade em clínicas de nutrição. Usar softwares de avaliação nutricional (Avanutri, NutroClinic, Dietbox) que automatizam a geração de planos alimentares a partir de parâmetros clínicos reduz o tempo por consulta e aumenta a qualidade percebida pelo paciente (planos impressos profissionalmente, com fotos de alimentos e lista de compras). A personalização dentro de um protocolo padronizado — ajustes para as preferências e rotina do paciente — é o equilíbrio ideal entre eficiência e qualidade de atendimento."),
        ("Fidelização e Recorrência",
         "Nutrição tem naturalmente alta recorrência: acompanhamentos mensais para pacientes em tratamento, consultas semestrais para manutenção de hábitos, e acompanhamento contínuo para atletas e pacientes com condições crônicas. Programas de acompanhamento por assinatura — um plano mensal que inclui teleconsulta, análise de exames e suporte por WhatsApp — transformam a consulta avulsa em receita recorrente previsível. Grupos de pacientes (presencial ou online, segmentados por objetivo: emagrecimento, gestação, performance) criam comunidade, aumentam o engajamento e têm custo marginal muito baixo por participante adicional."),
        ("Marketing Digital para Nutricionistas",
         "Nutricionistas têm um dos melhores potenciais de marketing de conteúdo entre os profissionais de saúde: receitas saudáveis, desmistificação de dietas modernas, orientações sobre leitura de rótulos e conteúdo sobre relação entre alimentação e condições de saúde específicas têm alto engajamento no Instagram, YouTube e TikTok. O conteúdo educativo de qualidade constrói audiência qualificada de potenciais pacientes. Especialização de nicho facilita muito o marketing: 'nutricionista especializada em nutrição esportiva para mulheres acima de 40' é muito mais fácil de posicionar do que 'nutricionista geral'."),
    ],
    faq_list=[
        ("Como precificar consultas de nutrição de forma competitiva?",
         "A precificação deve considerar: posicionamento (generalista vs. especialista), região, tempo de formação e especialização, e modelo de atendimento. Consultas de nutricionistas generalistas em grandes cidades variam de R$150-300 por consulta. Especialistas em nutrição funcional, oncológica ou esportiva de alta performance cobram R$400-800. Planos mensais de acompanhamento (teleconsulta + suporte) de R$300-600/mês têm a melhor relação entre recorrência e percepção de valor. Nunca precifique abaixo do custo de oportunidade do seu tempo — o mercado de nutrição premium valoriza especialização."),
        ("Como usar WhatsApp como ferramenta de acompanhamento sem consumir todo o tempo do nutricionista?",
         "O segredo é estabelecer regras claras desde a primeira consulta: horário de atendimento pelo WhatsApp (ex: segunda a sexta, 8h-18h), tipos de dúvidas respondidas pelo canal (questões rápidas sobre substituições alimentares, dificuldades de aderência), e o que demanda uma nova consulta (revisão de plano completa, análise de exames). Usar ferramentas como WhatsApp Business com respostas automáticas para horários fora do expediente e mensagens de lembrete programadas reduz a carga de trabalho sem prejudicar a experiência do paciente."),
        ("Como o ProdutoVivo pode ajudar nutricionistas a escalar seu negócio?",
         "O guia ProdutoVivo ensina nutricionistas a criar cursos online, e-books e apps interativos de orientação nutricional. Uma nutricionista especializada pode criar um programa digital de reeducação alimentar para emagrecer sem dieta restritiva, um guia de nutrição para atletas amadores, ou um app de receitas funcionais — gerando renda passiva recorrente e alcançando muito mais pessoas do que a agenda de consultas permite."),
    ]
)

# 5173 — SaaS Sales: Saúde e Hospitais
art(
    slug="vendas-para-o-setor-de-saas-de-saude-e-hospitais",
    title="Vendas para o Setor de SaaS de Saúde e Hospitais | ProdutoVivo",
    desc="Guia completo de vendas B2B para healthtech e SaaS hospitalar: como navegar processos de compra complexos, demonstrar ROI clínico e financeiro, e expandir em redes hospitalares.",
    h1="Vendas para o Setor de SaaS de Saúde e Hospitais",
    lead="Vender SaaS para hospitais é um dos ciclos de vendas mais longos e complexos do mercado B2B — mas também um dos mais rentáveis. Hospitais são clientes de alto LTV que raramente trocam de sistema depois de integrado. Entender o processo de compra hospitalar é o primeiro passo para uma estratégia de vendas eficaz nesse setor.",
    sections=[
        ("O Mercado de SaaS para Saúde no Brasil",
         "O mercado de saúde no Brasil inclui mais de 7.000 hospitais, 280 mil clínicas e ambulatórios, e um sistema de saúde suplementar com 47 milhões de beneficiários. As categorias de SaaS mais relevantes incluem: prontuário eletrônico (PEP/HIS), sistemas de gestão hospitalar (faturamento, estoque, agendamento), plataformas de telemedicina, ferramentas de analytics clínico e financeiro, sistemas de gestão de laboratórios (LIS), e plataformas de interoperabilidade entre sistemas de saúde. A regulação da ANVISA e os requisitos do CFM para prontuários eletrônicos criam barreiras de entrada que protegem players estabelecidos e exigem certificação para novos entrantes."),
        ("O Processo de Compra Hospitalar",
         "Compras de tecnologia em hospitais envolvem um processo formal e burocrático: comitê de tecnologia da informação (TI), aprovação da diretoria médica (para sistemas que afetam o workflow clínico), validação do setor financeiro (para sistemas de faturamento), e aprovação da governança corporativa em hospitais de maior porte. O processo típico para um sistema de HIS ou PEP dura de 12 a 24 meses, incluindo RFP (Request for Proposal), POC (Proof of Concept) com uma unidade piloto, e negociação de contrato. Vendedores de SaaS hospitalar precisam ter paciência e capacidade de gerenciar múltiplos stakeholders simultaneamente por meses."),
        ("Mapeamento de Stakeholders em Hospitais",
         "Os stakeholders em uma venda de SaaS hospitalar incluem: o CIO (Chief Information Officer) ou gerente de TI que avalia tecnicamente e frequentemente é o champion interno, o CMO (Chief Medical Officer) ou diretor médico que valida o impacto clínico e a resistência dos médicos, o CFO que analisa o ROI financeiro e o impacto no faturamento, a enfermagem sênior que avalia o impacto no workflow assistencial, e o CEO ou conselho que aprova investimentos acima de determinado threshold. Mapear quem influencia, quem decide e quem veta é fundamental — uma proposta aprovada pelo TI mas rejeitada pela diretoria médica não vai a lugar nenhum."),
        ("ROI em Healthtech: Dimensões Clínica e Financeira",
         "O ROI de SaaS hospitalar precisa ser demonstrado em duas dimensões: financeira e clínica. Financeiramente: redução de glosas (cobranças rejeitadas por convênios por erros de faturamento), aumento de produtividade administrativa, redução de estoque de medicamentos por melhor gestão, e redução de horas extras por otimização de escala. Clinicamente: redução de tempo de espera, melhora de adesão a protocolos, redução de eventos adversos preveníveis, e melhora de indicadores de qualidade (AHRQ, JCI). Hospitais que buscam certificação de qualidade (JCI, ONA) são compradores altamente motivados de tecnologia que suporte indicadores de qualidade."),
        ("Estratégias de Expansão em Redes Hospitalares",
         "A maior oportunidade em SaaS hospitalar é a expansão em redes: um cliente de 1 hospital que faz parte de uma rede de 10 hospitais é potencialmente um cliente de 10 hospitais. A estratégia é entregar excelência no hospital piloto, documentar os resultados, e apresentar o caso à liderança corporativa da rede. Plataformas que oferecem funcionalidades específicas para gestão de rede (consolidação de dados, benchmarking entre unidades, protocolos centralizados com adaptação local) têm argumento de expansão muito mais forte do que plataformas que só funcionam bem em unidades isoladas."),
    ],
    faq_list=[
        ("Como montar uma proposta de valor para sistemas de prontuário eletrônico em hospitais?",
         "A proposta de valor deve endereçar os três principais problemas de hospitais brasileiros: glosas (mostrar como o PEP reduz erros de faturamento e aumenta a taxa de aprovação de contas por convênios), retrabalho clínico (documentação duplicada, informações não encontradas rapidamente) e conformidade regulatória (LGPD, ANVISA, CFM). Use dados do mercado brasileiro: o índice médio de glosas hospitalares no Brasil é de 8-15% do faturamento — uma redução de 3 pontos percentuais em um hospital que fatura R$10M/mês representa R$3,6M/ano, muito maior que o custo do sistema."),
        ("Como lidar com médicos que resistem a mudar de prontuário?",
         "A resistência de médicos à mudança de sistema é a principal causa de fracasso em implementações de PEP. A estratégia mais eficaz é identificar os líderes de opinião clínica (chefes de serviço, médicos mais respeitados) e envolvê-los no processo de avaliação e customização do sistema. Quando os líderes clínicos são champions da solução, os demais médicos seguem. Treinamento hands-on (não slides), disponibilidade de suporte no início da implementação, e período de adaptação com o sistema antigo ainda disponível em paralelo reduzem significativamente a resistência."),
        ("Como o ProdutoVivo ajuda profissionais de saúde a complementar sua renda?",
         "O guia ProdutoVivo ensina médicos, enfermeiros, gestores hospitalares e profissionais de saúde a transformar seu conhecimento clínico e de gestão em cursos online e apps interativos. Um gestor hospitalar pode criar um curso de gestão de qualidade hospitalar, um médico especialista pode criar conteúdo de educação continuada para colegas — gerando renda adicional e posicionamento como referência em sua área."),
    ]
)

# 5174 — Consulting: Desenvolvimento de Liderança e Gestão de Talentos
art(
    slug="consultoria-de-desenvolvimento-de-lideranca-e-gestao-de-talentos",
    title="Consultoria de Desenvolvimento de Liderança e Gestão de Talentos | ProdutoVivo",
    desc="Como estruturar uma consultoria de desenvolvimento de liderança: programas de mentoria, trilhas de desenvolvimento, assessment de competências e ROI para empresas.",
    h1="Consultoria de Desenvolvimento de Liderança e Gestão de Talentos",
    lead="Desenvolvimento de liderança é uma das áreas de maior investimento corporativo em Recursos Humanos — e uma das com menor ROI comprovado quando mal executado. Consultores que combinam metodologia sólida com facilidade de grupo e mensuração de resultados constroem reputação que gera demanda recorrente de médias e grandes empresas.",
    sections=[
        ("O Mercado de Desenvolvimento de Liderança no Brasil",
         "Empresas brasileiras investem bilhões por ano em programas de treinamento e desenvolvimento de liderança — desde workshops pontuais de 8 horas até programas de 12 meses com coaching individual, treinamentos em grupo e projetos aplicados. O mercado inclui desde grandes players globais (DDI, Korn Ferry, Center for Creative Leadership) até consultoras independentes especializadas. O diferencial competitivo de consultoras independentes está na personalização e na proximidade com o cliente — algo difícil de replicar por grandes empresas com metodologias padronizadas globais."),
        ("Diagnóstico de Competências e Assessment",
         "Todo programa de desenvolvimento de liderança começa com um diagnóstico: quais são as competências críticas para a estratégia da empresa? Qual a distância entre as competências atuais dos líderes e o perfil desejado? As ferramentas mais usadas incluem: assessment 360° (avaliação pelos pares, subordinados e superiores), testes de perfil comportamental (DISC, MBTI, Hogan), entrevistas estruturadas de incidentes críticos (BEI), e análise de resultados de negócio atribuíveis ao comportamento de liderança. O diagnóstico é frequentemente vendido como projeto separado — e é o melhor funil de entrada para programas maiores de desenvolvimento."),
        ("Design de Programas de Desenvolvimento",
         "Programas eficazes de desenvolvimento de liderança combinam múltiplos formatos: workshops presenciais para construção de conceitos e prática em grupo, coaching individual para aplicação no contexto pessoal de cada líder, projetos aplicados que resolvem problemas reais da empresa usando as competências desenvolvidas, e peer learning circles (grupos de líderes que se reúnem para troca de experiências). A sequência importa: conceito, prática facilitada, aplicação no trabalho real, reflexão e consolidação. Programas que pulam a aplicação prática têm resultados muito inferiores aos que incluem projetos aplicados com mentoria."),
        ("Mensuração de Resultados e ROI",
         "A incapacidade de provar ROI é o maior problema de consultores de desenvolvimento de liderança — e uma enorme oportunidade para quem investe em mensuração. O modelo de Kirkpatrick (reação, aprendizado, comportamento, resultados) é o framework mais usado. Mensurar o nível 4 (resultados de negócio) requer definir indicadores de negócio atribuíveis ao comportamento de liderança antes do programa: turnover da equipe, eNPS (satisfação dos colaboradores com o líder), performance do time em OKRs, e aceleração de promoções de talentos identificados. Consultores que entregam relatórios de ROI baseados em dados convincem líderes de RH e CEOs a continuar investindo."),
        ("Modelos de Negócio e Precificação",
         "Programas de desenvolvimento de liderança são precificados por modalidade: workshop pontual (R$15-50k por turma de até 25 participantes), programa modular de 3-6 meses (R$80-300k dependendo do número de participantes e formato), retainer de coaching executivo individual (R$5-15k/mês por coachee), e licença de metodologia para uso interno do time de RH. A maior oportunidade de expansão de receita está em contratos de longo prazo: uma empresa que investe em um programa de desenvolvimento de gerentes em 2026 tende a continuar investindo no desenvolvimento de diretores em 2027 e no pipeline de líderes em 2028."),
    ],
    faq_list=[
        ("Quais certificações são mais valorizadas para consultores de desenvolvimento de liderança?",
         "As certificações mais reconhecidas no Brasil são: coaching executivo (ICF - International Coaching Federation, ACC/PCC/MCC), facilitação organizacional (IAF - International Association of Facilitators), e certificações em ferramentas de assessment (Hogan, DISC certificado, avaliador MBTI). Para credibilidade corporativa, MBA em RH, Gestão de Pessoas ou Comportamento Organizacional em instituições de prestígio complementa bem as certificações práticas. Experiência como executivo (liderando times de 50+ pessoas) frequentemente vale mais que certificações para vendas em grandes corporações."),
        ("Como estruturar um programa de mentoria corporativa?",
         "Um programa de mentoria corporativa eficaz tem 4 elementos: seleção cuidadosa de pares mentor-mentorado (compatibilidade de objetivos, não necessariamente mesma área), contrato claro de frequência e objetivos (tipicamente reuniões quinzenais por 6-12 meses), treinamento de mentores em técnicas de escuta ativa e perguntas poderosas, e rituais de grupo (encontros coletivos semestrais para compartilhar aprendizados). A plataforma tecnológica de suporte (matching, agendamento, registro de conversas) importa menos do que a qualidade do processo de seleção e treinamento dos mentores."),
        ("Como o ProdutoVivo ajuda consultores de liderança e coaches executivos?",
         "O guia ProdutoVivo ensina como transformar metodologias de desenvolvimento de liderança em cursos online, programas de mentoria digital e apps interativos para líderes. Um consultor de liderança pode criar um curso de autodesenvolvimento para gerentes de primeira viagem, um programa de coaching em grupo online, ou uma plataforma de trilha de liderança — gerando renda recorrente e alcançando líderes em todo o Brasil sem depender de projetos presenciais."),
    ]
)

# ── Sitemap update ────────────────────────────────────────────────────────────
sm_path = pathlib.Path(__file__).parent / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")
new_urls = "\n".join(
    f"  <url><loc>{DOMAIN}/blog/{s}/</loc></url>"
    for s in [
        "gestao-de-negocios-de-empresa-de-b2b-saas-de-insurtech-e-seguradoras",
        "gestao-de-clinicas-de-dermatologia-e-estetica-medica",
        "vendas-para-o-setor-de-saas-de-educacao-basica-escolas-e-colegios",
        "consultoria-de-transformacao-digital-e-inovacao-corporativa",
        "gestao-de-negocios-de-empresa-de-b2b-saas-de-logistica-e-rastreamento-de-frota",
        "gestao-de-clinicas-de-nutricao-clinica-e-funcional",
        "vendas-para-o-setor-de-saas-de-saude-e-hospitais",
        "consultoria-de-desenvolvimento-de-lideranca-e-gestao-de-talentos",
    ]
)
sm_path.write_text(sm.replace("</urlset>", new_urls + "\n</urlset>"), encoding="utf-8")

# ── Trilha update ─────────────────────────────────────────────────────────────
tr_path = pathlib.Path(__file__).parent / "trilha.html"
tr = tr_path.read_text(encoding="utf-8")
new_items = "\n".join(
    f'    <li><a href="{DOMAIN}/blog/{s}/">{label}</a></li>'
    for s, label in [
        ("gestao-de-negocios-de-empresa-de-b2b-saas-de-insurtech-e-seguradoras", "SaaS de Insurtech e Seguradoras"),
        ("gestao-de-clinicas-de-dermatologia-e-estetica-medica", "Clínica de Dermatologia e Estética"),
        ("vendas-para-o-setor-de-saas-de-educacao-basica-escolas-e-colegios", "SaaS de Educação Básica"),
        ("consultoria-de-transformacao-digital-e-inovacao-corporativa", "Consultoria de Transformação Digital"),
        ("gestao-de-negocios-de-empresa-de-b2b-saas-de-logistica-e-rastreamento-de-frota", "SaaS de Logística e Frota"),
        ("gestao-de-clinicas-de-nutricao-clinica-e-funcional", "Clínica de Nutrição Funcional"),
        ("vendas-para-o-setor-de-saas-de-saude-e-hospitais", "SaaS de Saúde e Hospitais"),
        ("consultoria-de-desenvolvimento-de-lideranca-e-gestao-de-talentos", "Consultoria de Liderança e Talentos"),
    ]
)
tr_path.write_text(tr.replace("</ul>", new_items + "\n  </ul>", 1), encoding="utf-8")

print("Done — batch 1842")
