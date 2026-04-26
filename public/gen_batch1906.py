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
<!-- Schema FAQ -->
<script type="application/ld+json">{faq_schema}</script>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Segoe UI',sans-serif;color:#1a1a1a;background:#fff}}
header{{background:#0a7c4e;padding:18px 24px}}
header a{{color:#fff;font-size:1.4rem;font-weight:700;text-decoration:none}}
nav{{background:#085f3b;padding:8px 24px;font-size:.85rem}}
nav a{{color:#cde8d8;text-decoration:none;margin-right:16px}}
.hero{{background:linear-gradient(135deg,#0a7c4e,#14a86a);color:#fff;padding:56px 24px 44px;text-align:center}}
.hero h1{{font-size:2rem;max-width:780px;margin:0 auto 16px;line-height:1.3}}
.hero p{{font-size:1.1rem;max-width:640px;margin:0 auto;opacity:.92}}
main{{max-width:820px;margin:40px auto;padding:0 20px 60px}}
h2{{font-size:1.35rem;color:#0a7c4e;margin:36px 0 12px;border-left:4px solid #0a7c4e;padding-left:12px}}
p{{line-height:1.8;margin-bottom:16px;color:#333}}
.faq{{background:#f4faf7;border-radius:10px;padding:28px 24px;margin:44px 0}}
.faq h2{{border:none;padding:0;margin-bottom:20px;font-size:1.25rem}}
details{{margin-bottom:14px;border:1px solid #c3ddd1;border-radius:8px;padding:14px 16px;background:#fff}}
summary{{font-weight:600;cursor:pointer;color:#085f3b;list-style:none}}
summary::-webkit-details-marker{{display:none}}
details p{{margin:10px 0 0;color:#444;font-size:.97rem}}
.cta{{background:#0a7c4e;color:#fff;border-radius:12px;padding:36px 28px;text-align:center;margin:48px 0}}
.cta h2{{color:#fff;border:none;padding:0;margin-bottom:12px;font-size:1.4rem}}
.cta p{{color:#d4f0e4;margin-bottom:22px}}
.cta a{{background:#fff;color:#0a7c4e;font-weight:700;padding:14px 32px;border-radius:8px;text-decoration:none;font-size:1rem}}
footer{{background:#085f3b;color:#a8d5bf;text-align:center;padding:22px;font-size:.85rem}}
footer a{{color:#a8d5bf}}
</style>
</head>
<body>
<header><a href="/">ProdutoVivo</a></header>
<nav>
  <a href="/">Home</a>
  <a href="/blog/">Blog</a>
  <a href="/guia-produto-digital/">Guia</a>
  <a href="/trilha.html">Trilha</a>
</nav>
<div class="hero">
  <h1>{h1}</h1>
  <p>{lead}</p>
</div>
<main>
{sections_html}
<div class="faq">
  <h2>Perguntas Frequentes</h2>
  {faq_html}
</div>
<div class="cta">
  <h2>Pronto para escalar seu negócio digital?</h2>
  <p>O ProdutoVivo ensina infoprodutores brasileiros a criar, lançar e vender produtos digitais que geram receita recorrente.</p>
  <a href="/">Quero Começar Agora</a>
</div>
</main>
<footer>
  <p>&copy; 2025 <a href="/">ProdutoVivo</a> — Todos os direitos reservados.</p>
</footer>
</body>
</html>"""


def art(slug, title, desc, h1, lead, sections, faq_list):
    url = f"{DOMAIN}/blog/{slug}/"
    faq_items = []
    for q, a in faq_list:
        faq_items.append({"@type": "Question", "name": q,
                          "acceptedAnswer": {"@type": "Answer", "text": a}})
    faq_schema = json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
                              "mainEntity": faq_items}, ensure_ascii=False)
    sections_html = ""
    for heading, body in sections:
        sections_html += f"<h2>{heading}</h2>\n<p>{body}</p>\n"
    faq_html = ""
    for q, a in faq_list:
        faq_html += f"<details><summary>{q}</summary><p>{a}</p></details>\n"
    html = TMPL.format(title=title, desc=desc, url=url, pixel=PIXEL,
                       faq_schema=faq_schema, h1=h1, lead=lead,
                       sections_html=sections_html, faq_html=faq_html)
    out = pathlib.Path(BASE) / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"  {slug}")


# ── Batch 1906 — articles 5295–5302 ──────────────────────────────────────────

# 5295 — B2B SaaS: InsurTech / gestão de seguros e corretoras
art(
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-insurtech-e-gestao-de-seguros",
    "Gestão de Negócios de Empresa de B2B SaaS de InsurTech e Gestão de Seguros | ProdutoVivo",
    "Aprenda a construir e escalar um B2B SaaS de InsurTech e gestão de seguros: oportunidades, produto, go-to-market e crescimento no mercado segurador brasileiro.",
    "Gestão de Negócios de Empresa de B2B SaaS de InsurTech e Gestão de Seguros",
    "O mercado segurador brasileiro cresce 12% ao ano e está em plena transformação digital. Conheça as oportunidades para um SaaS no setor de seguros.",
    [
        ("O Mercado de Seguros e a Revolução InsurTech",
         "O Brasil é o 7º maior mercado segurador do mundo, com prêmios totais superiores a R$400 bilhões anuais. Corretoras de seguros, seguradoras e gestoras de benefícios operam com sistemas legados de 20-30 anos e processos altamente manuais. A regulação da SUSEP avançou significativamente nos últimos anos com o sandbox regulatório e abertura de seguros embedded, criando um ambiente favorável para InsurTechs que digitalizam desde a distribuição até a gestão de sinistros."),
        ("Segmentos de Produto em InsurTech B2B",
         "As principais oportunidades de produto para InsurTech B2B: (1) Plataforma de gestão para corretoras — CRM específico para seguros, comparador de apólices, gestão de renovações e comissões; (2) Core system moderno para seguradoras — apólices, sinistros, cobrança em cloud; (3) API de seguros embedded — permite que varejistas, fintechs e empresas não-seguradoras ofereçam seguros como produto adjacente; (4) Analytics e precificação — modelos preditivos de risco para subscrição mais precisa; (5) Gestão de sinistros automatizada — IA para análise de documentos e liquidação ágil."),
        ("Go-to-Market: Corretoras como Ponto de Entrada",
         "Corretoras são o canal de distribuição de seguros por excelência — há mais de 100.000 corretores habilitados no Brasil. Uma plataforma SaaS para corretoras tem ICP claro: corretoras com 2-20 corretores que gerenciam múltiplas seguradoras e perdem tempo com planilhas de renovação. O produto resolve dores imediatas (perder renovações por falta de controle, erros de comissão, dificuldade de comparar apólices) e a adoção inicial pode se dar via freemium ou trial de 30 dias sem fricção."),
        ("Modelo de Receita e Precificação",
         "Modelos que funcionam no setor: (a) Por corretora/usuário ativo — R$150-500/mês para corretoras pequenas, escalando para R$5.000-20.000/mês para corretoras médias com múltiplas filiais; (b) Revenue share sobre prêmios digitalizados — adequado para plataformas de seguros embedded, típico 0.5-1.5% do prêmio; (c) Licença enterprise para seguradoras — R$50.000-300.000/mês para um core system moderno substituindo legado. O segmento de corretoras médias (R$1.000-8.000/mês) é o sweet spot de crescimento mais rápido."),
        ("Regulação SUSEP e Abertura do Mercado",
         "O sandbox regulatório da SUSEP (Circular 598/2021) criou um ambiente de experimentação onde InsurTechs podem testar modelos inovadores com regime simplificado por até 2 anos. O Open Insurance (OPIN) — equivalente segurador do Open Banking — permite que plataformas acessem dados de apólices via APIs padronizadas com consentimento do segurado. Essas iniciativas criam janelas de oportunidade para InsurTechs que constroem em cima da nova infraestrutura regulatória antes que os grandes players legados se adaptem."),
    ],
    [
        ("InsurTech precisa de autorização da SUSEP para operar?",
         "Depende do modelo. Plataformas SaaS que vendem software para corretoras e seguradoras (sem distribuir seguros diretamente) geralmente não precisam de autorização da SUSEP. Plataformas que atuam como corretora digital ou distribuidora de seguros precisam de habilitação como corretor de seguros pessoa jurídica (SUSEP/CNSeg). O sandbox regulatório permite testar modelos inovadores de distribuição por 24 meses com regime simplificado — ideal para InsurTechs que querem validar antes de obter licença plena."),
        ("Qual o maior desafio técnico de um SaaS de seguros?",
         "Integração com as seguradoras é o maior desafio técnico — cada seguradora tem sua API (ou falta de API) com formatos distintos para cotação, emissão e sinistros. Construir um hub de integração que normaliza essas diferenças é o maior diferencial técnico de plataformas de corretoras. Seguradoras que oferecem APIs REST modernas (Youse, Pier, Kakau) são mais simples de integrar; seguradoras tradicionais exigem web scraping ou conectores proprietários específicos por produto."),
        ("Como o Open Insurance impacta o desenvolvimento de SaaS para o setor?",
         "O OPIN padroniza APIs para dados de apólices de vida, previdência e capitalização, permitindo que segurados autorizem o compartilhamento dos seus dados com plataformas terceiras. Para InsurTechs, isso significa acesso a dados de portfólio de clientes para oferecer comparações de cobertura, identificar gaps de proteção e propor upgrades. Plataformas que constroem sobre as APIs do OPIN ganham acesso a dados que antes eram silos fechados de cada seguradora, habilitando produtos de gestão de portfólio segurador sem precedentes."),
    ]
)

# 5296 — Clinic: gastroenterologia e doenças digestivas
art(
    "gestao-de-clinicas-de-gastroenterologia-e-doencas-digestivas",
    "Gestão de Clínicas de Gastroenterologia e Doenças Digestivas | ProdutoVivo",
    "Guia completo para gestão de clínicas de gastroenterologia: estrutura de endoscopia, equipe, credenciamento, captação de pacientes e crescimento sustentável.",
    "Gestão de Clínicas de Gastroenterologia e Doenças Digestivas",
    "Gastroenterologia combina alta demanda por endoscopia e colonoscopia com consultas clínicas recorrentes. Saiba como estruturar uma clínica lucrativa nessa especialidade.",
    [
        ("Gastroenterologia no Brasil: Demanda e Oportunidade",
         "Doenças digestivas afetam 30-40% da população adulta brasileira — síndrome do intestino irritável, DRGE, doença inflamatória intestinal, hepatites e rastreamento de câncer colorretal. A endoscopia e colonoscopia são procedimentos de alta demanda e ticket expressivo (R$600-1.800 por exame no particular), tornando a gastroenterologia uma das especialidades com maior potencial de receita por hora de trabalho médico. O rastreamento de câncer colorretal recomendado a partir dos 45 anos cria uma onda contínua de demanda por colonoscopias."),
        ("Sala de Endoscopia: o Coração da Clínica Gastroenterológica",
         "O investimento central de uma clínica de gastroenterologia é a sala de endoscopia: equipamento de videoscopia (gastroscópio + colonoscópio) custa R$150.000-400.000 novo, ou R$60.000-150.000 recondicionado com certificação. A sala deve atender normas Anvisa com área de processamento de endoscópios (limpeza, desinfecção de alto nível), sala de recuperação pós-sedação com monitoração, e suporte de anestesiologia para procedimentos com sedação consciente. O retorno sobre o equipamento acontece em 12-24 meses com agenda adequada."),
        ("Modelos de Receita em Gastroenterologia",
         "A clínica gastroenterológica tem três pilares de receita: (1) Endoscopia diagnóstica e terapêutica — maior ticket (R$600-1.800/exame), requer sala equipada; (2) Colonoscopia de rastreamento — alta demanda, protocolo padronizado, agenda previsível; (3) Consultas clínicas de acompanhamento — pacientes com doença inflamatória intestinal, hepatite B/C crônica, DRGE, SII retornam a cada 3-6 meses gerando receita recorrente. A combinação dos três cria fluxo financeiro equilibrado entre receita de alto valor (endoscopia) e recorrente (consultas)."),
        ("Credenciamento com Planos e Política de Procedimentos",
         "Credenciamento para endoscopia e colonoscopia com planos de saúde exige CNES com habilitação em endoscopia digestiva, equipamento certificado e RT especialista (título SOBED). Negocie tabelas específicas para procedimentos endoscópicos — muitos planos pagam por tabela CBHPM com coeficientes reduzidos; identifique quais planos remuneram melhor na sua cidade e priorize esses credenciamentos. Mantenha uma política clara de agendamento de particular para procedimentos urgentes que planos demoram a autorizar."),
        ("Marketing para Gastroenterologistas: Captação e Fidelização",
         "O gastroenterologista se beneficia de dois tipos de marketing: (1) Conteúdo educativo sobre saúde digestiva (sintomas de alerta de câncer colorretal, cuidados com o intestino, dieta para DRGE) no Instagram e YouTube — educa e gera autoridade; (2) SEO local para 'gastroenterologista [cidade]' e 'colonoscopia particular [bairro]' — captura busca de intenção imediata. Parcerias com clínicos gerais e internistas para encaminhamentos são o canal mais eficiente — ofereça retorno detalhado por escrito para fidelizar o médico encaminhador."),
    ],
    [
        ("Qual o investimento para abrir uma clínica de endoscopia?",
         "Uma clínica de endoscopia básica (1 sala, 1 endoscópio + 1 colonoscópio) requer R$400.000-900.000 de investimento total: equipamentos de videoscopia (R$150.000-400.000), obras e adequações da sala (R$100.000-250.000), autoclaves e equipamentos de processamento (R$50.000-100.000), e capital de giro para os primeiros 6 meses. Com 3-4 procedimentos/dia de segunda a sexta, a receita mensal bruta de R$60.000-120.000 viabiliza o retorno do investimento em 2-4 anos."),
        ("Anestesista é obrigatório para colonoscopia?",
         "A colonoscopia pode ser realizada sem sedação (apenas com analgesia tópica) ou com sedação consciente administrada pelo próprio endoscopista em alguns estados, ou com anestesia geral supervisionada por anestesiologista. A Resolução CFM 2.174/2017 estabelece requisitos para sedação em procedimentos endoscópicos. Na prática, a maioria dos pacientes prefere colonoscopia com sedação — a presença do anestesiologista é um diferencial de conforto que aumenta a aceitação do exame e justifica ticket maior."),
        ("Como expandir de consultório para clínica de endoscopia?",
         "A transição do consultório para uma estrutura com sala de endoscopia começa com a validação da demanda: se você já encaminha 15+ pacientes/mês para endoscopia em outras clínicas, a internalização é financeiramente viável. O modelo mais comum de expansão é sociedade com outro gastroenterologista — compartilham o investimento do equipamento e turnos de agenda, reduzindo o ponto de equilíbrio pela metade. Alternativamente, alugar horas de sala em uma clínica já estruturada é o caminho de menor risco para começar."),
    ]
)

# 5297 — SaaS Sales: agtech e agronegócio digital
art(
    "vendas-para-o-setor-de-saas-de-agtech-e-agronegocio-digital",
    "Vendas para o Setor de SaaS de AgTech e Agronegócio Digital | ProdutoVivo",
    "Estratégias de vendas B2B para SaaS de AgTech e agronegócio digital: como prospectar produtores rurais, cooperativas e distribuidores agrícolas e fechar contratos.",
    "Vendas para o Setor de SaaS de AgTech e Agronegócio Digital",
    "O agronegócio brasileiro responde por 25% do PIB e está em plena digitalização. Aprenda a vender SaaS para produtores rurais, cooperativas e indústria agrícola.",
    [
        ("O Agronegócio Digital: Tamanho e Oportunidade",
         "O Brasil é um dos maiores produtores agrícolas do mundo, com mais de 5 milhões de estabelecimentos rurais e um setor que movimenta R$2,5 trilhões anuais. A adoção de tecnologia no campo é heterogênea: grandes produtores de soja, milho e cana no Cerrado já são altamente tecnificados; pecuaristas de corte de médio porte e pequenos produtores de frutas e hortaliças ainda operam com processos manuais. A AgTech brasileira cresce 35% ao ano em investimentos, mas a penetração de SaaS no campo ainda é baixa, criando espaço enorme para novos entrantes com produto adequado à realidade do campo."),
        ("Segmentação do Mercado AgTech",
         "O mercado AgTech se divide por elo da cadeia: (1) Produção rural — gestão de fazenda (safras, insumos, maquinário, financeiro agrícola), monitoramento de lavoura via satélite/drone, gestão de rebanho; (2) Cooperativas e traders — gestão de recebimento de grãos, contratos, classificação e armazenagem; (3) Distribuição de insumos — gestão de revendas agrícolas, CRM para representantes, crédito rural; (4) Indústria e agroindústria — rastreabilidade, gestão de qualidade, supply chain agrícola. Cada segmento tem ICP, canal e ciclo de venda distintos."),
        ("Prospecção no Campo: Canais e Abordagem",
         "Chegar ao produtor rural exige presença onde ele está: feiras agropecuárias (Agrishow, ExpoZebu, Show Rural Coopavel), cooperativas locais que reúnem centenas de produtores, revendas de insumos que têm relacionamento diário com o campo, e associações rurais como CNA, Famasul, Faesp. No digital, YouTube com conteúdo técnico agropecuário tem audiência massiva de produtores — parceiros agrônomos e influencers do agro são canais de aquisição de baixo custo. WhatsApp é o principal canal de comunicação com o campo — suporte e onboarding via WhatsApp são mandatórios."),
        ("Demo e Adoção: Adaptando para o Contexto Rural",
         "A demo de SaaS agrícola precisa ser adaptada à realidade do campo: funciona offline (conectividade rural é intermitente), interface simples para uso em tablet/celular com luva, dados da fazenda do próprio cliente (mapa de talhões, histórico de safra) para gerar identificação imediata. Pilotos gratuitos de 1 safra completa (3-6 meses) têm muito maior conversão que trials de 30 dias — o produtor precisa ver o software ao longo de todo o ciclo produtivo para avaliar o valor real. Envolva um agrônomo parceiro no onboarding do piloto."),
        ("Modelos de Receita e Barreiras de Adoção",
         "Modelos que funcionam no agro: por hectare manejado, por cabeça de gado monitorada, por tonelada recebida (cooperativas), ou por assinatura mensal/anual simples. Preço por hectare é transparente e fácil de calcular pelo produtor — uma fazenda de 1.000 ha pagando R$2/ha/mês gera R$2.000/mês, facilmente justificado por 1 saca de soja economizada em perdas ou insumos. A maior barreira de adoção é o hábito: o produtor que 'sempre fez assim' precisa ver casos de sucesso de vizinhos e colegas antes de mudar. Invista em comunidade e casos documentados regionalmente."),
    ],
    [
        ("SaaS agrícola precisa funcionar offline?",
         "Sim, para uso no campo é essencial. A conectividade rural no Brasil ainda é limitada — muitas fazendas têm 2G intermitente ou dependem de internet via satélite com latência alta. O app precisa sincronizar dados quando há conexão e continuar funcionando com todas as funcionalidades principais offline. Essa é uma das maiores barreiras técnicas para SaaS agrícola e um dos maiores diferenciais para quem resolve bem."),
        ("Como lidar com a sazonalidade do agronegócio nas vendas de SaaS?",
         "O ciclo de vendas no agro acompanha o ciclo agrícola: o melhor momento para vender soluções de gestão de safra é entre o plantio da safra anterior e o planejamento da próxima (geralmente março-junho no Centro-Oeste para soja). Evite abordar o produtor na época de colheita ou plantio — ele está 100% focado na operação. Crie um calendário de prospecção alinhado ao calendário agrícola das culturas que seu produto atende, e use os períodos de entressafra para demonstrações e fechamentos."),
        ("Qual a taxa de churn esperada em SaaS agrícola?",
         "SaaS agrícola bem executado tem churn anual de 10-18% — mais alto que enterprise SaaS, mas reduzível com onboarding dedicado e suporte técnico de campo. O principal motivo de churn é abandono por não-uso (o produtor assina mas nunca adota de fato). Combata isso com um onboarding presencial ou via WhatsApp intensivo nos primeiros 90 dias, garantindo que o produtor registre pelo menos uma safra completa no sistema — após isso, o churn cai dramaticamente pelo valor dos dados históricos acumulados."),
    ]
)

# 5298 — Consulting: cultura organizacional e employer branding
art(
    "consultoria-de-cultura-organizacional-e-employer-branding",
    "Consultoria de Cultura Organizacional e Employer Branding | ProdutoVivo",
    "Como estruturar e escalar uma consultoria de cultura organizacional e employer branding: metodologias, posicionamento, captação e modelos de receita para consultores de RH estratégico.",
    "Consultoria de Cultura Organizacional e Employer Branding",
    "Cultura e marca empregadora são diferenciais competitivos mensuráveis. Saiba como posicionar sua consultoria nesse mercado de alto valor.",
    [
        ("Por que Cultura Organizacional Virou Prioridade Estratégica",
         "A 'guerra por talentos' elevou cultura organizacional e employer branding ao topo da agenda do CHRO. Empresas percebem que salário não retém mais sozinho — candidatos pesquisam a empresa no Glassdoor e LinkedIn antes de aceitar ofertas, e colaboradores que não se identificam com a cultura pedem demissão mesmo com remuneração competitiva. O custo de turnover elevado (1-2x o salário anual por substituição) torna o investimento em cultura demonstravelmente rentável, abrindo espaço para consultorias que quantificam esse ROI."),
        ("Portfólio de Serviços: Diagnóstico, Ativação e Marca",
         "Organize o portfólio em três trilhas: (1) Diagnóstico de cultura — pesquisa de clima, análise de cultura atual vs. desejada, mapeamento de brechas e plano de evolução cultural; (2) Ativação de cultura — workshops de lideranças, redesenho de rituais organizacionais, programas de reconhecimento, integração de cultura nos processos de RH (recrutamento, onboarding, avaliação de desempenho); (3) Employer Branding — posicionamento da empresa como empregador de escolha, estratégia de conteúdo no LinkedIn e Glassdoor, campanha de EVP (Employee Value Proposition), e gestão da reputação em plataformas de candidatos."),
        ("Diferenciação: Dados e Métricas de Cultura",
         "A maioria das consultorias de cultura entrega 'workshops inspiracionais' que não se traduzem em mudança mensurável. Diferencie-se entregando cultura baseada em dados: use ferramentas de people analytics para medir engajamento, NPS interno (eNPS), índices de retenção por grupo, tempo de preenchimento de vagas e custo por contratação. Clientes que veem métricas de cultura melhorando trimestre a trimestre pagam mais e renovam contratos por anos. Construa um dashboard de cultura que o cliente acessa continuamente, não apenas no relatório final."),
        ("Captação e Posicionamento",
         "CHROs e People Directors são os decisores primários. LinkedIn com conteúdo sobre tendências de cultura (quiet quitting, gestão de equipes remotas, diversidade e inclusão) e cases concretos de transformação cultural gera audiência qualificada. Parcerias com consultorias de T&D, headhunters e plataformas de RH criam referências cruzadas. Participação em CONARH, RH Summit e eventos de People Analytics posiciona o consultor como referência. O primeiro cliente geralmente vem da rede pessoal — invista tempo em construir credibilidade antes de escalar."),
        ("Precificação e Modelos de Engajamento",
         "Projetos de diagnóstico de cultura custam R$25.000-80.000 (4-8 semanas). Programas de ativação cultural duram 6-12 meses e custam R$100.000-350.000. Employer branding como serviço pode ser contratado em modelo de retainer mensal (R$8.000-25.000/mês) para empresas que precisam de gestão contínua da marca empregadora. Empresas em processo de IPO, M&A ou rebranding têm necessidade urgente de employer branding e disposição a pagar premium — esses momentos de transição são gatilhos de compra poderosos."),
    ],
    [
        ("Como medir o ROI de um projeto de cultura organizacional?",
         "Métricas de ROI de cultura: redução de turnover voluntário (cada ponto percentual a menos economiza milhares em custos de substituição), melhora no eNPS (relacionada com produtividade e recomendação da empresa a conhecidos), redução no tempo médio de preenchimento de vagas (indica melhora na marca empregadora), e aumento na taxa de aceitação de ofertas. Estabeleça baselines antes do projeto e meça 6-12 meses depois para demonstrar impacto concreto."),
        ("Employer branding funciona para empresas fora de São Paulo?",
         "Sim, e frequentemente com resultados melhores. Empresas em cidades do interior competem por talentos locais que têm menos opções — uma forte marca empregadora regional pode ser decisiva para atrair e reter os melhores profissionais locais, evitando que migrem para grandes centros. O employer branding regional foca em diferenciais como qualidade de vida, estabilidade, impacto na comunidade local e oportunidades de crescimento em empresa de referência regional."),
        ("Cultura organizacional pode ser mudada em 6 meses?",
         "Mudanças profundas de cultura levam 2-4 anos. Em 6 meses, é possível criar consciência sobre os valores desejados, iniciar mudanças de comportamento em lideranças e implementar rituais e processos que reforcem a nova cultura. A metáfora certa é 'jardinagem, não construção civil' — cultura evolui continuamente com consistência e paciência, não em um projeto com início e fim. Consultorias que prometem 'transformação cultural em 3 meses' raramente entregam mudança sustentável."),
    ]
)

# 5299 — B2B SaaS: field service management
art(
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-field-service-management",
    "Gestão de Negócios de Empresa de B2B SaaS de Field Service Management | ProdutoVivo",
    "Como construir e escalar um B2B SaaS de field service management: mercado, funcionalidades, go-to-market e crescimento no setor de serviços técnicos em campo.",
    "Gestão de Negócios de Empresa de B2B SaaS de Field Service Management",
    "Empresas com equipes técnicas em campo perdem eficiência sem digitalização. Descubra como construir um SaaS de field service management escalável.",
    [
        ("O Mercado de Field Service Management no Brasil",
         "Field service management (FSM) abrange qualquer empresa que despache técnicos para atender clientes em campo: manutenção de elevadores, instalação e reparo de equipamentos industriais, assistência técnica de linha branca, serviços de telecomunicações, utilities (energia, gás, água), HVAC, segurança eletrônica e dedetização. No Brasil, o mercado de FSM é estimado em R$5 bilhões, com mais de 500.000 técnicos de campo que ainda dependem de papel, Excel e WhatsApp para receber ordens de serviço e reportar o trabalho realizado."),
        ("Funcionalidades Core de um FSM SaaS",
         "O produto central deve cobrir: criação e distribuição automática de ordens de serviço (OS); geolocalização e roteirização de técnicos em tempo real; app mobile offline para técnicos (Android/iOS) com checklist de execução, assinatura digital do cliente e upload de fotos; gestão de contratos de manutenção preventiva com disparos automáticos; controle de peças e estoque de campo; SLA e tempo de resposta com alertas de vencimento; e portal do cliente para acompanhamento em tempo real. Cada funcionalidade resolve uma ineficiência concreta do dia a dia operacional."),
        ("ICP e Estratégia de Go-to-Market",
         "O ICP são empresas com 10-200 técnicos em campo que ainda gerenciam operações via Excel/WhatsApp. Segmentos de entrada mais acessíveis: assistência técnica de eletrodomésticos, manutenção de ar-condicionado, instalação de sistemas de segurança, e dedetizadoras. Esses segmentos têm menor resistência à mudança, ciclo de venda curto (30-60 dias) e podem pagar R$200-2.000/mês. Segmentos enterprise (utilities, telecom, elevadores) têm ticket maior (R$20.000-150.000/mês) mas ciclo de venda de 6-12 meses com RFP."),
        ("Precificação por Técnico e Modelo de Expansão",
         "Precificação mais comum: por técnico ativo/mês (R$150-500 por técnico, dependendo do plano). Uma empresa com 20 técnicos paga R$3.000-10.000/mês — facilmente justificado por 1-2 horas de produtividade adicional por técnico por dia. O upsell natural ocorre quando a empresa cresce sua equipe técnica: cada técnico adicional gera receita incremental automática. Módulos premium de BI operacional, integração com ERP e portal white-label para clientes finais elevam o ARPU de contas maduras."),
        ("Vantagem Competitiva: Integrações e Ecossistema",
         "FSM SaaS se torna mais valioso quando integrado com o ecossistema do cliente: ERPs (SAP, TOTVS, Bling), sistemas de NF-e para faturamento automático de OS, plataformas de pagamento para cobranças em campo, e ferramentas de comunicação (WhatsApp Business API para notificações de agendamento ao cliente final). Integrações nativas com as ferramentas mais usadas pelo segmento-alvo criam lock-in e reduzem churn — o custo de migrar um FSM integrado ao ERP e ao faturamento é muito alto para o cliente."),
    ],
    [
        ("FSM SaaS compete com módulos de ERP como TOTVS?",
         "ERPs como TOTVS oferecem módulos de field service, mas com funcionalidades limitadas e interface pouco adaptada para técnicos em campo. Um FSM especializado entrega app mobile offline robusto, roteirização inteligente, checklists configuráveis por tipo de serviço e experiência de cliente (portal de acompanhamento) que ERPs raramente alcançam. A estratégia ideal é posicionar o FSM como complemento do ERP, integrando dados de OS e estoque com o TOTVS sem substituí-lo."),
        ("App mobile para técnicos precisa ser nativo ou pode ser PWA?",
         "Para field service, app nativo (React Native ou Flutter) é fortemente recomendado sobre PWA, principalmente por: funcionamento offline confiável (cache de OS, fotos, checklists sem conexão), acesso à câmera e GPS com performance nativa, notificações push em tempo real, e experiência mais fluida em dispositivos variados que técnicos usam. A diferença de experiência entre um app nativo bem construído e um PWA é percebida imediatamente por técnicos em campo — e a adoção depende de o app ser agradável de usar."),
        ("Como convencer uma empresa a abandonar o Excel + WhatsApp para FSM?",
         "Mostre o custo invisível do modelo atual: OS perdida ou duplicada (1-3% de faturamento perdido), tempo de gerente coordenando por WhatsApp (2-4 horas/dia), dificuldade de provar para o cliente que o serviço foi realizado sem evidências digitais, e impossibilidade de analisar histórico de OS para melhorar a operação. Um piloto de 30 dias com 5 técnicos e acompanhamento próximo gera dados concretos de ganho de eficiência que fecham o contrato com o gestor operacional."),
    ]
)

# 5300 — Clinic: pneumologia e medicina respiratória
art(
    "gestao-de-clinicas-de-pneumologia-e-medicina-respiratoria",
    "Gestão de Clínicas de Pneumologia e Medicina Respiratória | ProdutoVivo",
    "Guia para gestão de clínicas de pneumologia: estrutura de espirometria, equipe, credenciamento, tratamento de asma e DPOC, e estratégias de crescimento.",
    "Gestão de Clínicas de Pneumologia e Medicina Respiratória",
    "Doenças respiratórias afetam 30% dos brasileiros. Saiba como estruturar uma clínica de pneumologia rentável e com impacto clínico duradouro.",
    [
        ("Panorama das Doenças Respiratórias no Brasil",
         "Asma, DPOC, rinite e pneumonias são as doenças respiratórias mais prevalentes no Brasil, impactando 30-35 milhões de pessoas. A prevalência de tabagismo (11% da população adulta), a poluição urbana em grandes centros e as condições climáticas diversas do país criam demanda contínua por pneumologistas. Além das doenças crônicas, a pneumologia se expande para: síndrome do sono (apneia), nódulos pulmonares (rastreamento de câncer de pulmão), e telemedicina respiratória, diversificando as fontes de receita."),
        ("Estrutura Física e Equipamentos Essenciais",
         "Uma clínica de pneumologia básica precisa de: espirómetro para testes de função pulmonar (espirometria) — equipamento indispensável, custa R$15.000-50.000; oxímetro de pulso e fluxômetro; acesso ou parceria com serviço de polissonografia para avaliação de apneia do sono; e articulação com laboratório de bronco e lavado broncoalveolar para casos de maior complexidade. Uma cabine de prova de função pulmonar completa (R$80.000-150.000) adiciona precisão diagnóstica e aumenta o ticket médio por consulta."),
        ("Serviços de Alto Valor: Polissonografia e Sono",
         "A medicina do sono é uma extensão natural da pneumologia com altíssima demanda e baixa oferta de especialistas. O serviço de polissonografia (exame de sono) pode ser estruturado na própria clínica (2-4 leitos, investimento R$200.000-400.000) ou terceirizado para clínicas parceiras. A apneia do sono não tratada está associada a hipertensão, diabetes e acidente vascular cerebral — o mercado de CPAP (aparelho de pressão positiva para apneia) gera receita de locação/venda de equipamentos além das consultas. Uma clínica de sono bem posicionada pode faturar R$80.000-200.000/mês com 2 leitos ocupados 5 noites por semana."),
        ("Reabilitação Pulmonar: Receita Recorrente e Diferenciação",
         "Programas de reabilitação pulmonar para DPOC, fibrose pulmonar e pós-COVID são serviços de alto valor que geram receita recorrente. Um programa estruturado (2-3 sessões semanais por 8-12 semanas) com fisioterapeuta respiratório, exercícios supervisionados e acompanhamento nutricional tem ticket de R$1.200-3.500 por paciente. Diferenciar a clínica com reabilitação pulmonar estruturada atrai encaminhamentos de pneumologistas que não têm essa infraestrutura, além de criar um diferencial competitivo claro no mercado local."),
        ("Captação de Pacientes e Parcerias Estratégicas",
         "A pneumologia se beneficia de encaminhamentos de clínicos gerais, cardiologistas, alergologistas e otorrinolaringologistas. Construa uma rede ativa de parceiros com retorno detalhado por escrito e disponibilidade para tira-dúvidas rápido. No digital, conteúdo educativo sobre saúde respiratória (como usar o inalador corretamente, sinais de alerta de DPOC, efeitos do tabagismo) no Instagram e YouTube gera audiência qualificada. SEO local para 'pneumologista [cidade]' e 'tratamento apneia do sono [cidade]' captura pacientes com intenção ativa."),
    ],
    [
        ("Espirometria pode ser realizada por qualquer médico?",
         "A espirometria pode ser solicitada por qualquer médico, mas a interpretação adequada requer treinamento específico — pneumologistas e alergologistas têm a formação mais completa. A realização técnica do exame pode ser feita por técnico de função pulmonar treinado ou fisioterapeuta respiratório sob supervisão médica. Clínicas que oferecem espirometria com laudo emitido por pneumologista têm um diferencial de qualidade reconhecido por clínicos encaminhadores."),
        ("Como é o tratamento de DPOC em uma clínica pneumológica?",
         "O tratamento de DPOC (Doença Pulmonar Obstrutiva Crônica) é crônico e multidisciplinar: broncodilatadores de longa duração (LABA + LAMA), corticoides inalatórios quando indicados, cessação do tabagismo, vacinação (influenza, pneumococo), reabilitação pulmonar e acompanhamento de exacerbações. Pacientes com DPOC moderada a grave consultam 3-4 vezes ao ano e eventualmente necessitam de oxigenoterapia domiciliar, criando um fluxo de receita recorrente previsível para a clínica pneumológica."),
        ("Vale a pena montar serviço de polissonografia dentro da clínica?",
         "Sim, se houver demanda local suficiente. Um serviço de polissonografia com 2 leitos, operando 5 noites/semana, realiza 10 exames/semana — 40/mês. Com ticket médio de R$1.500-2.500 por polissonografia particular, a receita bruta mensal alcança R$60.000-100.000. O payback do investimento em infraestrutura (R$200.000-400.000) ocorre em 3-8 meses com ocupação adequada. O maior desafio é a captação inicial — parcerias com otorrinolaringologistas, cardiologistas e endocrinologistas que encaminham casos de apneia são essenciais."),
    ]
)

# 5301 — SaaS Sales: construção civil e engenharia
art(
    "vendas-para-o-setor-de-saas-de-construcao-civil-e-engenharia",
    "Vendas para o Setor de SaaS de Construção Civil e Engenharia | ProdutoVivo",
    "Estratégias de vendas B2B para SaaS de construção civil e engenharia: como prospectar construtoras, incorporadoras e escritórios de engenharia e fechar contratos.",
    "Vendas para o Setor de SaaS de Construção Civil e Engenharia",
    "A construção civil movimenta R$600 bilhões no Brasil e está se digitalizando aceleradamente. Veja como vender SaaS para esse mercado de alto potencial.",
    [
        ("O Setor de ConTech no Brasil",
         "Construction Technology (ConTech) é o segmento de startups e SaaS voltado à digitalização da construção civil. O setor brasileiro de construção responde por 7% do PIB, tem mais de 200.000 empresas formalizadas e é historicamente sub-digitalizado — 70% das construtoras ainda usam Excel como principal ferramenta de gestão. Os principais desafios do setor que abrem oportunidade para SaaS: gestão de obras com atrasos crônicos, estouro de orçamento, comunicação deficiente entre escritório e campo, e dificuldades com compliance de saúde e segurança do trabalho (NRs)."),
        ("Mapeando os Compradores no Setor de Construção",
         "O ecossistema de compradores é diverso: incorporadoras (vendem imóveis, contratam construtoras), construtoras (executam obras residenciais, comerciais, industriais), empreiteiras de especialidade (estrutura, elétrica, hidráulica), escritórios de arquitetura e engenharia (projetos BIM, gestão de documentos técnicos), e fiscalizadoras/gerenciadoras (PMIS — Project Management Information Systems). Cada segmento tem dores específicas: incorporadoras querem gestão financeira de múltiplos empreendimentos; construtoras buscam controle de obras; escritórios precisam de gestão de projetos e documentos técnicos."),
        ("Abordagem de Vendas: Eventos e Relacionamento",
         "Construção civil é um setor de relacionamento intenso — decisões de compra de software são influenciadas por indicações de pares. Presença em eventos como Expo REVESTIR, FEICON BATIMAT, Constru Tech e Simpósios do IBGC gera exposição qualificada. Associações como CBIC, Sinduscon e AELO reúnem decisores. Conteúdo técnico para engenheiros e gestores de obras (YouTube, LinkedIn) cria autoridade. Parcerias com ERPs de construção civil (Sienge, Volare, Obra Prima) para módulos complementares são canais de distribuição poderosos."),
        ("Demo para Construtoras: Mostrando ROI Concreto",
         "O engenheiro de obras é cético — quer ver o software funcionando no contexto de canteiro, não em demos genéricas. Simule o fluxo real: abertura de OS de manutenção, registro de não-conformidade com foto geolocalizada, checklist de inspeção de qualidade, diário de obra digital, e relatório de avanço físico-financeiro para a diretoria. Quantifique o valor: uma construtora que reduce re-trabalho em 15% economiza R$200.000-500.000 em uma obra de R$5M — ROI imediato que justifica qualquer SaaS de R$2.000-15.000/mês."),
        ("Ciclo de Vendas e Expansão de Contratos",
         "O ciclo de vendas em construção civil é moderado: PMEs decidem em 30-60 dias; médias construtoras em 60-120 dias; grandes incorporadoras com múltiplas obras podem levar 6-12 meses. O contrato inicial geralmente cobre uma obra específica — depois expande para todas as obras ativas à medida que a adoção cresce. Construtoras que usam o software em 3+ obras simultâneas raramente churnam — os dados históricos de obras anteriores (orçamentos, padrões de custo, produtividades) se tornam um ativo estratégico que nenhuma empresa abre mão facilmente."),
    ],
    [
        ("Qual o principal diferencial de um SaaS de gestão de obras?",
         "Integração campo-escritório em tempo real é o diferencial mais valorizado. A capacidade de o mestre de obras registrar uma ocorrência no celular e o diretor de engenharia ver na tela do escritório imediatamente — com foto, geolocalização e responsável — elimina o principal gargalo de informação da construção. Funcionalidades BIM (integração com modelos 3D) são diferenciais para construtoras médias e grandes que já trabalham com BIM como exigência de grandes incorporadoras e contratos públicos."),
        ("SaaS de construção precisa ter módulo BIM?",
         "Não necessariamente para PMEs, mas é um diferencial crescente. BIM (Building Information Modeling) é obrigatório em licitações federais acima de determinado valor (Decreto 9.983/2019) e adotado por incorporadoras de médio e grande porte. Para construtoras que já têm BIM implantado, um SaaS que integra com modelos BIM (IFC, Revit, ArchiCAD) para gestão de obras é muito mais valioso que um sistema isolado. Para PMEs iniciando digitalização, focar em gestão de obras sem BIM é a abordagem mais acessível."),
        ("Como vender SaaS de construção para obras do setor público?",
         "Obras públicas demandam conformidade com processos de licitação (Lei 14.133/2021 — Nova Lei de Licitações), relatórios específicos para órgãos de controle (TCU, TCE) e rastreabilidade de medições e pagamentos. SaaS com módulo de gestão de contratos públicos (cronograma físico-financeiro, boletins de medição, reajuste de preços por índices SINAPI) atende uma demanda específica e de alto ticket — contratos públicos de grande porte têm verba de gestão que permite pagar R$15.000-50.000/mês por plataformas bem especializadas."),
    ]
)

# 5302 — Consulting: liderança e desenvolvimento executivo
art(
    "consultoria-de-lideranca-e-desenvolvimento-executivo",
    "Consultoria de Liderança e Desenvolvimento Executivo | ProdutoVivo",
    "Como estruturar e escalar uma consultoria de liderança e desenvolvimento executivo: metodologias, posicionamento, captação de clientes e modelos de receita.",
    "Consultoria de Liderança e Desenvolvimento Executivo",
    "Líderes eficazes multiplicam resultados organizacionais. Saiba como monetizar sua expertise em desenvolvimento de liderança como consultor ou coach executivo.",
    [
        ("O Mercado de Desenvolvimento de Liderança no Brasil",
         "O investimento em desenvolvimento de liderança é o maior item de orçamento de T&D nas empresas brasileiras de médio e grande porte — estima-se que R$4 bilhões sejam gastos anualmente em programas de liderança, coaching executivo e assessments. A demanda aumenta em momentos de crescimento organizacional (quando líderes técnicos precisam desenvolver habilidades de gestão de pessoas), transformação cultural, fusões e aquisições, e expansão geográfica. Consultorias que entregam resultados mensuráveis em comportamento de liderança têm contratos de alto valor e longa duração."),
        ("Portfólio de Serviços: do Coaching ao Programa Corporativo",
         "Organize o portfólio em três níveis: (1) Coaching executivo individual — sessões 1:1 com executivos de C-suite e gerentes sênior, pacotes de 6-12 meses; (2) Programas de desenvolvimento de liderança — journeys estruturadas para grupos de líderes (ex.: 'Programa de Líderes de Alta Performance' para 20 gestores em 8 meses); (3) Assessments e diagnóstico de liderança — 360° feedback, DiSC, MBTI, Hogan, CliftonStrengths para mapeamento de perfil e gaps de desenvolvimento. Cada linha tem público, ticket e processo de venda distinto."),
        ("Diferenciação: Evidências e Resultados de Negócio",
         "O mercado de desenvolvimento de liderança é saturado de coaches sem credenciais robustas. Diferencie-se com: certificações reconhecidas (ICF ACC/PCC/MCC, credenciais em ferramentas de assessment como Hogan e DiSC); foco em resultados de negócio mensuráveis (não apenas 'bem-estar do líder', mas 'aumento de engajamento do time' e 'melhora de NPS de liderança no 360°'); e especialização em um contexto específico (líderes de tecnologia, lideranças femininas, executivos em transição de cargo). A especialização atrai um ICP mais definido e justifica preço premium."),
        ("Vendas: Acesso ao C-Suite e Decisores de RH",
         "Acessar C-suite para coaching executivo requer introduções por referência — CEOs e diretores não respondem cold outreach para coaching. Construa reputação via: publicações em veículos de negócios (Harvard Business Review Brasil, MIT Sloan Management Review Brasil), participação como palestrante em fóruns executivos (HSM, Amcham, IBGC), e programa de RH como porta de entrada (o CHRO compra para a liderança). Um primeiro coachee bem-servido indica naturalmente outros executivos da mesma rede — 80% dos contratos de coaching executivo vêm de indicações."),
        ("Precificação e Escalabilidade",
         "Coaching executivo individual: R$1.500-5.000 por sessão de 90 min; pacotes anuais de R$40.000-150.000 por executivo. Programas de grupo de 20 líderes: R$180.000-600.000 por programa de 8 meses. Assessments de liderança: R$3.000-8.000 por participante (inclui instrumento, relatório e devolutiva). Para escalar sem depender apenas de horas do consultor sênior, crie programas digitais (cursos online de liderança), licencie ferramentas de assessment para RHs parceiros, e forme uma equipe de coaches associados que operam sob sua metodologia e marca."),
    ],
    [
        ("Preciso ser certificado ICF para atuar como coach executivo?",
         "A certificação ICF (International Coaching Federation) não é legalmente obrigatória no Brasil, mas é o padrão de credibilidade do mercado corporativo. CHROs de grandes empresas frequentemente exigem ICF ACC ou PCC como critério mínimo para contratação de coaches para executivos. A certificação ICF exige horas de treinamento em programa acreditado, horas de prática supervisionada e aprovação em exame. Investir na credencial é fundamental para acessar contratos corporativos de alto valor."),
        ("Coaching executivo e mentoria são a mesma coisa?",
         "Não. Coaching é um processo estruturado focado no desenvolvimento do coachee — o coach faz perguntas poderosas para que o executivo encontre suas próprias respostas e desenvolva autoconsciência e novos comportamentos. Mentoria envolve um mentor mais experiente que compartilha conhecimento, experiência e orientação diretiva. Ambas são valiosas e complementares: mentoria transmite know-how específico; coaching desenvolve capacidade de pensar e agir de forma mais eficaz independentemente."),
        ("Como estruturar um programa de liderança para 50 gestores?",
         "Um programa de liderança para grupos grandes combina: módulos de conteúdo (workshops mensais de 8 horas em liderança situacional, feedback, comunicação executiva, gestão de conflitos); coaching em trios (grupos de 3 gestores em sessões de peer coaching quinzenais, supervisionadas pelo consultor); projetos de impacto (cada gestor aplica aprendizados em um desafio real do seu time); e acompanhamento de dados (360° no início e no final, eNPS do time de cada gestor antes e depois). O formato híbrido presencial + digital é o mais aceito pós-pandemia."),
    ]
)

# ── Sitemap ───────────────────────────────────────────────────────────────────
slugs_5295 = [
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-insurtech-e-gestao-de-seguros",
    "gestao-de-clinicas-de-gastroenterologia-e-doencas-digestivas",
    "vendas-para-o-setor-de-saas-de-agtech-e-agronegocio-digital",
    "consultoria-de-cultura-organizacional-e-employer-branding",
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-field-service-management",
    "gestao-de-clinicas-de-pneumologia-e-medicina-respiratoria",
    "vendas-para-o-setor-de-saas-de-construcao-civil-e-engenharia",
    "consultoria-de-lideranca-e-desenvolvimento-executivo",
]
titles_5295 = [
    "Gestão de Negócios de Empresa de B2B SaaS de InsurTech e Gestão de Seguros",
    "Gestão de Clínicas de Gastroenterologia e Doenças Digestivas",
    "Vendas para o Setor de SaaS de AgTech e Agronegócio Digital",
    "Consultoria de Cultura Organizacional e Employer Branding",
    "Gestão de Negócios de Empresa de B2B SaaS de Field Service Management",
    "Gestão de Clínicas de Pneumologia e Medicina Respiratória",
    "Vendas para o Setor de SaaS de Construção Civil e Engenharia",
    "Consultoria de Liderança e Desenvolvimento Executivo",
]

sm_path = pathlib.Path(__file__).parent / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")
new_urls = "\n".join(
    f"  <url><loc>{DOMAIN}/blog/{s}/</loc><changefreq>monthly</changefreq><priority>0.6</priority></url>"
    for s in slugs_5295
)
sm_path.write_text(sm.replace("</urlset>", new_urls + "\n</urlset>"), encoding="utf-8")

# ── Trilha ────────────────────────────────────────────────────────────────────
tr_path = pathlib.Path(__file__).parent / "trilha.html"
tr = tr_path.read_text(encoding="utf-8")
new_items = "\n".join(
    f'    <li><a href="/blog/{s}/">{t}</a></li>'
    for s, t in zip(slugs_5295, titles_5295)
)
tr_path.write_text(tr.replace("</ul>", new_items + "\n  </ul>", 1), encoding="utf-8")

print("Done — batch 1906")
