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

# ── BATCH 1838 — artigos 5159–5166 ──────────────────────────────────────────

# 5159 — B2B SaaS: RH e recrutamento
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-rh-e-recrutamento",
    title="Gestão de Negócios de Empresa de B2B SaaS de RH e Recrutamento | ProdutoVivo",
    desc="Guia completo para escalar uma empresa B2B SaaS focada em RH e recrutamento: vendas, churn, product-led growth e expansão de receita.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de RH e Recrutamento",
    lead="O mercado de HRtech cresce aceleradamente no Brasil: empresas que combinam tecnologia com expertise em recrutamento e seleção têm potencial enorme de expansão — mas exigem gestão especializada para crescer de forma sustentável.",
    sections=[
        ("O Mercado de HRtech B2B no Brasil",
         "Plataformas SaaS de RH e recrutamento atendem desde PMEs que precisam automatizar triagem de currículos até grandes corporações que buscam análises preditivas de turnover. O modelo B2B exige ciclos de vendas consultivos, demonstrações customizadas e integrações com ERPs e sistemas legados de folha de pagamento. Empresas que conseguem se posicionar como plataformas de gestão de pessoas — e não apenas ferramentas de triagem — conquistam contratos maiores e clientes mais fiéis."),
        ("Aquisição de Clientes e Ciclo de Vendas",
         "O processo de venda para RH corporativo envolve múltiplos stakeholders: o diretor de RH define a necessidade, o TI avalia a integração técnica, e o CFO aprova o orçamento. Estratégias eficazes incluem eventos de RH (CONARH, HR Summit), parcerias com consultorias de gestão de pessoas e conteúdo educativo para gestores de RH no LinkedIn. Um free trial com limite de vagas publicadas funciona como PLG para PMEs, enquanto demos personalizadas são indispensáveis para contas enterprise."),
        ("Precificação e Modelos de Receita",
         "Os modelos de precificação em HRtech variam bastante: por número de usuários ativos (RH + gestores), por vagas abertas simultâneas, por volume de candidatos processados, ou por módulos contratados (ATS, onboarding, avaliação de desempenho, people analytics). O modelo híbrido — mensalidade base mais consumo variável — é comum em plataformas de recrutamento. O desafio é precificar de forma que reflita o valor entregue: uma plataforma que reduz o tempo de contratação em 60% pode cobrar premium sobre soluções básicas de ATS."),
        ("Retenção e Expansão de Receita",
         "Churn em HRtech está fortemente correlacionado com adoção pelos gestores de linha — não apenas pelo RH central. Plataformas que treinam gestores a usar o sistema para aprovações de vagas, feedbacks e avaliações de desempenho criam stickiness muito maior. Customer Success focado em QBRs (Quarterly Business Reviews) com métricas de time-to-hire, custo-por-contratação e qualidade de contratação transforma o relacionamento de suporte para parceria estratégica. Expansão de receita vem de módulos adicionais: empresas que contratam só o ATS são convertidas para onboarding digital e depois para people analytics."),
        ("Desafios Técnicos e Diferenciais Competitivos",
         "Integração com portais de emprego (Catho, Indeed, LinkedIn Vagas) e ERPs (SAP, TOTVS) é requisito mínimo. O diferencial competitivo está em recursos avançados: matching por IA que avalia fit cultural além de competências técnicas, análises preditivas de performance de candidatos, relatórios de diversidade e inclusão (D&I) para compliance com ESG, e automações de comunicação com candidatos que melhoram a experiência de recrutamento. Empresas que lideram em NPS de candidatos conseguem atrair empresas preocupadas com employer branding."),
    ],
    faq_list=[
        ("Como estruturar o time de Customer Success em uma HRtech B2B?",
         "O modelo recomendado é segmentar por porte de cliente: CSMs low-touch para PMEs (atendimento via plataforma e webinars em grupo), CSMs mid-touch para médias empresas (reuniões mensais e QBRs), e CSMs high-touch para enterprise (reuniões semanais, project manager dedicado e relatórios customizados). O KPI principal é Net Revenue Retention (NRR), que deve incluir expansão de módulos e usuários."),
        ("Qual o maior erro de founders de HRtech ao tentar escalar?",
         "Tentar atender todos os segmentos simultaneamente — desde MEIs até multinacionais — sem uma proposta de valor clara para nenhum. A recomendação é dominar um nicho vertical primeiro (ex: varejo, saúde ou tecnologia) e construir cases de referência antes de expandir horizontalmente. Clientes de referência em nichos específicos valem mais do que dezenas de clientes genéricos para o processo de vendas enterprise."),
        ("Como o infoproduto ProdutoVivo ajuda gestores de HRtech?",
         "O guia ProdutoVivo ensina como usar IA para transformar documentação de processos — playbooks de onboarding, scripts de entrevista, políticas de RH — em cursos e apps interativos. Para HRtechs, isso significa criar academias de clientes que treinam os gestores a usar a plataforma e reduzem drasticamente o tempo de onboarding e churn por falta de adoção."),
    ]
)

# 5160 — Clínica: Oftalmologia e Visão
art(
    slug="gestao-de-clinicas-de-oftalmologia-e-saude-ocular",
    title="Gestão de Clínicas de Oftalmologia e Saúde Ocular | ProdutoVivo",
    desc="Estratégias de gestão para clínicas de oftalmologia: agendamento, equipamentos de alto custo, convênios e fidelização de pacientes com doenças crônicas oculares.",
    h1="Gestão de Clínicas de Oftalmologia e Saúde Ocular",
    lead="Clínicas de oftalmologia combinam procedimentos de alta complexidade — cirurgias refrativas, tratamentos de retina, catarata — com consultas de rotina de baixo ticket. Equilibrar essa operação exige gestão financeira sofisticada e protocolos clínicos rigorosos.",
    sections=[
        ("O Mercado de Oftalmologia no Brasil",
         "O Brasil tem um dos maiores mercados de cirurgia de catarata da América Latina e uma demanda crescente por procedimentos a laser (LASIK, PRK, LASEK). Ao mesmo tempo, doenças crônicas como glaucoma, degeneração macular relacionada à idade (DMRI) e retinopatia diabética garantem uma base de pacientes com retorno frequente. Clínicas que combinam procedimentos cirúrgicos eletivos (alto ticket, pagamento direto) com gestão de pacientes crônicos (volume, convênios) constroem fluxo de caixa mais estável e previsível."),
        ("Gestão de Equipamentos e Infraestrutura",
         "A oftalmologia é uma das especialidades médicas mais dependentes de equipamentos caros: tomógrafos de coerência óptica (OCT), retinógrafos, microscópios cirúrgicos, aparelhos de campo visual, lasers excimer. O ciclo de vida útil desses equipamentos e o custo de manutenção preventiva precisam estar no planejamento financeiro de longo prazo. Muitas clínicas adotam modelos de leasing ou parceria com fornecedores que incluem manutenção, reduzindo o capex inicial mas aumentando o custo fixo mensal. O ponto de equilíbrio por procedimento deve incluir a depreciação do equipamento."),
        ("Convênios, Particular e Modelo Híbrido",
         "A dependência excessiva de convênios com tabelas defasadas é um dos maiores riscos financeiros em oftalmologia. A tabela AMB (CBHPM), base da maioria dos convênios, não acompanha a inflação de insumos cirúrgicos e os custos de manutenção de equipamentos. Clínicas sustentáveis desenvolvem uma estratégia mista: procedimentos crônicos e de acompanhamento via convênio para garantir volume, e cirurgias eletivas (catarata premium com lentes multifocais, LASIK) cobradas no particular para margens mais altas. A negociação de valores diferenciados com operadoras para procedimentos cirúrgicos é essencial."),
        ("Captação e Fidelização de Pacientes",
         "A oftalmologia tem uma característica única: pacientes saudáveis só consultam para check-up ou renovar receita de óculos, mas se tornam clientes frequentes ao desenvolver doenças crônicas. Estratégias de captação incluem parcerias com clínicos gerais e endocrinologistas (que encaminham diabéticos para rastreio de retinopatia), campanhas de saúde ocular em empresas (check-up visual corporativo) e conteúdo educativo sobre prevenção de glaucoma. O CRM deve segmentar pacientes por patologia para campanhas de recall automatizadas: lembretes de retorno para glaucomatosos, DMRI e diabéticos."),
        ("Cirurgias Eletivas e Revenue Management",
         "Cirurgias refrativas (LASIK) e de catarata com lentes premium representam o maior potencial de receita por procedimento em oftalmologia. A venda dessas cirurgias exige um processo consultivo: o paciente precisa entender as opções (lente monofocal vs. multifocal vs. tórica), os benefícios de longo prazo e as condições de financiamento. Clinicas que oferecem financiamento próprio ou parceria com financeiras têm taxas de conversão até 40% maiores para cirurgias premium. Depoimentos em vídeo de pacientes pós-cirurgia e visitas à sala cirúrgica virtual (tour 360°) aumentam a confiança e reduzem a taxa de desistência."),
    ],
    faq_list=[
        ("Qual o tamanho mínimo de equipe para uma clínica de oftalmologia rentável?",
         "Para uma clínica com 1-2 oftalmologistas, o mínimo viável é: 1 recepcionista/agendadora, 1 técnico de oftalmologia (que realiza os exames preliminares — tonometria, acuidade visual, refração) e 1 auxiliar administrativo-financeiro. O técnico de oftalmologia é crucial para otimizar o tempo do médico: se o paciente chega com todos os exames básicos feitos, a consulta é mais curta e a capacidade de atendimento aumenta 30-50%."),
        ("Como criar um programa de fidelidade para pacientes de oftalmologia?",
         "O modelo mais eficaz é baseado em continuidade de cuidado: ofereça desconto progressivo no check-up anual para pacientes que retornam regularmente, crie um pacote de acompanhamento para doenças crônicas (glaucoma, DMRI) com consultas e exames periódicos a um preço fixo mensal, e use o app da clínica para enviar lembretes de retorno personalizados com conteúdo educativo sobre a condição do paciente."),
        ("Como o ProdutoVivo pode ajudar profissionais de oftalmologia?",
         "O guia ProdutoVivo ensina oftalmologistas e gestores de clínicas a transformar seu conhecimento especializado em cursos online e apps interativos. Um especialista em saúde ocular pode criar um programa de educação para pacientes diabéticos sobre prevenção de retinopatia, ou um curso de boas práticas de saúde ocular para empresas — gerando renda recorrente e posicionamento como autoridade."),
    ]
)

# 5161 — SaaS Sales: E-commerce e Lojas Virtuais
art(
    slug="vendas-para-o-setor-de-saas-de-e-commerce-e-lojas-virtuais",
    title="Vendas para o Setor de SaaS de E-commerce e Lojas Virtuais | ProdutoVivo",
    desc="Guia de vendas B2B para plataformas SaaS de e-commerce: como prospectar lojistas, demonstrar ROI e competir com soluções all-in-one como VTEX e Shopify.",
    h1="Vendas para o Setor de SaaS de E-commerce e Lojas Virtuais",
    lead="Vender SaaS para o ecossistema de e-commerce é simultaneamente um dos mercados mais aquecidos e mais competitivos do Brasil. Lojistas têm dezenas de opções em cada categoria — ERP, gestão de estoque, precificação, frete, CRM — e precisam de vendedores que entendam profundamente as dores operacionais do varejo digital.",
    sections=[
        ("O Ecossistema de Tecnologia para E-commerce",
         "O mercado de tecnologia para e-commerce no Brasil é fragmentado em dezenas de categorias: plataformas de loja virtual (VTEX, Shopify, Nuvemshop, Tray), ERPs especializados em varejo digital (Bling, Omie, Tiny), sistemas de gestão de estoque e armazém (WMS), ferramentas de precificação dinâmica, plataformas de frete e logística, soluções de CRM e marketing para lojistas, e ferramentas de analytics de conversão. Cada categoria tem players dominantes e dezenas de alternativas. O desafio do vendedor de SaaS é posicionar sua solução de forma clara num mercado onde o lojista já está saturado de propostas."),
        ("Perfil do Comprador e Processo de Decisão",
         "O decisor varia pelo porte da loja: no pequeno e-commerce (faturamento até R$1M/ano), o próprio dono toma todas as decisões e o critério principal é preço + facilidade de uso. No médio porte (R$1M-R$20M), entra um gerente de operações ou TI que avalia integrações e confiabilidade. No grande varejo digital (acima de R$20M), o processo de compra envolve comitê com TI, financeiro e operações, e demora meses. Estratégia de vendas eficaz segmenta claramente qual público-alvo atende e personaliza o processo de vendas para cada perfil."),
        ("Demonstração de ROI para Lojistas",
         "Lojistas avaliam SaaS por impacto direto em três métricas: aumento de conversão (mais vendas com o mesmo tráfego), redução de custos operacionais (menos tempo manual, menos erros de estoque, menos devoluções) e aumento de ticket médio (upsell, cross-sell, bundles). Vendedores eficazes chegam à demo com benchmarks do setor: 'lojas do seu porte que adotaram nossa solução reduziram o tempo de processamento de pedidos em X horas por dia' ou 'a taxa de abandono de carrinho caiu em média Y%'. Personalizar a simulação de ROI para os dados da loja do prospecto é o diferencial que converte demos em fechamentos."),
        ("Competição com Soluções All-in-One",
         "Plataformas como VTEX, Shopify e Nuvemshop oferecem ecossistemas completos de apps integrados, o que é ao mesmo tempo uma ameaça e uma oportunidade. Ameaça porque o lojista pode preferir uma solução nativa da plataforma. Oportunidade porque soluções especializadas geralmente entregam performance superior em casos de uso específicos. A estratégia é se tornar o melhor da categoria (precificação dinâmica, gestão de devoluções, CRM pós-venda) e construir integrações nativas com as plataformas dominantes. Ser listado no app store da VTEX ou Shopify é um canal de distribuição poderoso."),
        ("Estratégias de Retenção em SaaS para E-commerce",
         "Churn em SaaS para lojistas é fortemente sazonal: picos de churn ocorrem após períodos de baixa vendas (primeiro semestre), quando lojistas cortam custos. Estratégias de retenção incluem: demonstrar valor com relatórios mensais automáticos que mostram o ROI da plataforma, criar planos sazonais com preço reduzido no primeiro semestre para garantir fidelidade, e desenvolver funcionalidades de preparação para Black Friday que tornam o SaaS indispensável nos meses de maior volume. O NPS medido após Black Friday é o melhor indicador de saúde do cliente para e-commerce."),
    ],
    faq_list=[
        ("Qual a melhor estratégia para prospectar donos de e-commerce?",
         "A combinação mais eficaz é: LinkedIn Sales Navigator para lojas de médio porte (procurar 'gerente de e-commerce', 'head de operações'), grupos do Facebook de lojistas (Empreendedores do E-commerce, Lojistas VTEX), e eventos como E-commerce Brasil e fóruns de plataformas. Cold email funciona bem com personalização baseada na plataforma que a loja usa e no tamanho estimado (via SimilarWeb ou ferramentas de inteligência de mercado)."),
        ("Como lidar com objeções de preço em vendas para pequenos lojistas?",
         "A objeção de preço geralmente mascara insegurança sobre ROI. A resposta mais eficaz é uma calculadora de ROI personalizada: 'se nossa plataforma economizar 2 horas do seu dia em gestão de pedidos, a R$50/hora isso é R$200/semana — nosso plano custa R$297/mês, então você está no positivo em 6 semanas'. Oferecer trial de 14 dias sem cartão, com onboarding guiado, aumenta muito a taxa de conversão para PMEs."),
        ("Como o ProdutoVivo ajuda quem vende SaaS para e-commerce?",
         "O guia ProdutoVivo ensina como criar conteúdo estruturado — guias, tutoriais, materiais de onboarding — e transformá-los em apps interativos para educação de clientes. Para vendedores de SaaS para lojistas, isso significa criar academias de clientes que reduzem o tempo de onboarding, aumentam a adoção de features e diminuem o churn por falta de conhecimento da plataforma."),
    ]
)

# 5162 — Consulting: Fusões e Aquisições
art(
    slug="consultoria-de-fusoes-aquisicoes-e-due-diligence-empresarial",
    title="Consultoria de Fusões, Aquisições e Due Diligence Empresarial | ProdutoVivo",
    desc="Como estruturar uma consultoria de M&A e due diligence: metodologia, precificação, captação de mandatos e entrega de valor em transações empresariais.",
    h1="Consultoria de Fusões, Aquisições e Due Diligence Empresarial",
    lead="O mercado de fusões e aquisições (M&A) no Brasil movimenta bilhões de reais anualmente, mas é historicamente dominado por grandes bancos de investimento e boutiques financeiras. Consultores independentes com especialização setorial têm uma janela de oportunidade crescente no middle market, onde agilidade e custo competitivo valem mais do que o nome de um banco.",
    sections=[
        ("O Mercado de M&A no Middle Market Brasileiro",
         "Transações abaixo de R$50 milhões raramente chegam a grandes bancos de investimento — o ticket é pequeno para a estrutura de custo desses players. Esse middle market — pequenas e médias empresas que buscam sócios estratégicos, fundos de private equity ou sucessão familiar — é o nicho mais acessível para consultores independentes de M&A. A demanda é consistente: empreendedores que querem vender parcial ou totalmente, fundos que buscam plataformas de consolidação setorial, e empresas familiares sem herdeiros que precisam de desinvestimento organizado. Consultores com rede de relacionamento e especialização em um setor específico (saúde, agro, tecnologia) têm vantagem competitiva clara."),
        ("Metodologia de Due Diligence",
         "A due diligence é o coração do processo de M&A e a principal entrega de valor do consultor. O processo cobre quatro dimensões: financeira (análise de demonstrações contábeis, normalização de EBITDA, análise de fluxo de caixa e endividamento), legal (estrutura societária, contratos críticos, passivos trabalhistas e tributários, propriedade intelectual), operacional (processos, sistemas, dependências de pessoas-chave, fornecedores e clientes) e comercial (market share, pipeline de clientes, análise competitiva). Consultores que desenvolvem um framework próprio de due diligence — com templates, checklists e modelos financeiros — aumentam a eficiência e a qualidade percebida pelo cliente."),
        ("Captação de Mandatos e Posicionamento",
         "A captação de mandatos de M&A vem principalmente de três fontes: rede de advogados corporativos (que recebem demandas de clientes querendo vender ou comprar), fundos de private equity e family offices (que buscam assessores para originação de deals), e contadores e auditores (que conhecem empresas com EBITDA saudável mas sem plano de sucessão). Posicionamento de autoridade em setores específicos via LinkedIn, publicações em veículos especializados (Valor Econômico, Capital Aberto) e palestras em eventos setoriais constrói o pipeline de mandatos de médio prazo."),
        ("Estrutura de Honorários e Success Fee",
         "A precificação em consultoria de M&A tem dois componentes: um retainer mensal (que cobre o custo de assessoramento durante o processo, tipicamente R$15-50k/mês dependendo do porte) e um success fee percentual do valor da transação (geralmente 1-5% para transações de R$5-50M, com porcentagem decrescente em transações maiores). O retainer é importante porque processos de M&A duram 6-18 meses e o consultor precisa cobrir seus custos independentemente do fechamento. Estruturas com mínimo garantido e bônus por superar o valuation target alinham os incentivos com o vendedor."),
        ("Gestão do Processo e Negociação",
         "O papel do consultor no processo de M&A vai além da due diligence: inclui preparação do Information Memorandum (IM) que apresenta a empresa para compradores potenciais, organização do processo competitivo (teaser, NDA, IM, rodadas de ofertas), gestão da data room virtual, facilitação das negociações e coordenação com advogados para o fechamento. Consultores que entendem tanto a dimensão financeira quanto os aspectos psicológicos da negociação — especialmente em vendas de empresas familiares, onde há forte componente emocional — entregam resultados superiores e constroem reputação de excelência no mercado."),
    ],
    faq_list=[
        ("Quais certificações são relevantes para consultores de M&A no Brasil?",
         "As principais certificações são: CFA (Chartered Financial Analyst), CNPI (Certificado Nacional do Profissional de Investimento) da APIMEC, e MBA em Finanças Corporativas ou Gestão de Empresas em instituições reconhecidas. Para atuação em transações que envolvem securities (ações), o registro na CVM pode ser necessário dependendo da estrutura do mandato. Especialização setorial (ex: M&A em saúde ou agronegócio) muitas vezes vale mais que uma certificação genérica."),
        ("Como estimar o valuation de uma PME para uma transação de M&A?",
         "Os métodos mais usados no middle market são: múltiplo de EBITDA (tipicamente 4-8x para PMEs brasileiras, variando por setor e crescimento), fluxo de caixa descontado (DCF) para empresas com crescimento previsível, e transações comparáveis recentes no mesmo setor. O desafio em PMEs é normalizar o EBITDA: remover pró-labore acima do mercado, custos pessoais do sócio, e despesas não recorrentes. O valuation final é sempre resultado de negociação — os métodos são ponto de partida."),
        ("Como o ProdutoVivo pode ajudar consultores de M&A?",
         "O guia ProdutoVivo ensina como transformar metodologias de due diligence, checklists de preparação para venda e frameworks de valuation em cursos online e apps interativos de alto valor. Um consultor de M&A pode criar um produto digital ensinando empreendedores a preparar a empresa para uma transação — construindo pipeline qualificado de potenciais mandatos enquanto gera receita adicional."),
    ]
)

# 5163 — B2B SaaS: Arquitetura e Engenharia Civil
art(
    slug="gestao-de-negocios-de-empresa-de-b2b-saas-de-arquitetura-e-engenharia-civil",
    title="Gestão de Negócios de Empresa de B2B SaaS de Arquitetura e Engenharia Civil | ProdutoVivo",
    desc="Guia para escalar SaaS voltado para escritórios de arquitetura e engenharia: BIM, gestão de projetos, orçamentação e ciclo de vendas para AEC.",
    h1="Gestão de Negócios de Empresa de B2B SaaS de Arquitetura e Engenharia Civil",
    lead="O setor de Arquitetura, Engenharia e Construção (AEC) está passando por uma transformação digital profunda no Brasil, com adoção crescente de BIM, gestão de projetos colaborativa e orçamentação automatizada. SaaS para AEC tem um mercado em expansão, mas com ciclos de venda longos e resistência cultural à tecnologia.",
    sections=[
        ("O Mercado AEC e a Transformação Digital",
         "O mercado de construção civil representa cerca de 6-7% do PIB brasileiro e é historicamente um dos setores com menor adoção de tecnologia. Isso está mudando: a obrigatoriedade do BIM (Building Information Modeling) para obras públicas federais, estaduais e municipais — com prazos progressivos estabelecidos pelo Decreto 9.983/2019 — está forçando escritórios de arquitetura e construtoras a adotar softwares compatíveis. Isso cria uma demanda regulatória que facilita a venda de SaaS para AEC, especialmente para escritórios que precisam se adequar para participar de licitações públicas."),
        ("Categorias de SaaS para AEC",
         "O mercado de software para AEC se divide em: plataformas BIM (Revit, Archicad, e alternativas brasileiras como Edificius), ferramentas de gestão de projetos de construção (Procore, Sienge, Volare), software de orçamentação (Pini, Neogeo, TCPO), sistemas de gestão de obras (acompanhamento físico-financeiro, cronograma Gantt), plataformas de gestão documental de obras e ferramentas de realidade aumentada para visualização de projetos. Cada categoria tem casos de uso específicos e decisores diferentes dentro de uma construtora ou escritório."),
        ("Ciclo de Vendas e Adoção",
         "A venda de SaaS para arquitetos e engenheiros tem características peculiares: alta resistência à mudança (profissionais que trabalham com AutoCAD há 20 anos resistem a novas ferramentas), necessidade de demonstração prática (o produto precisa ser experimentado no workflow real), e influência forte de pares e líderes de opinião do setor. Estratégias eficazes incluem oferecer trial longo (30-60 dias), criar tutoriais baseados em projetos reais típicos do segmento-alvo, e conquistar early adopters com prestígio no setor para gerar recomendações. Participação em eventos como FEICON, EXPO REVESTIR e congressos do CAU e CREA é fundamental para brand awareness."),
        ("Integração e Interoperabilidade",
         "Um dos maiores desafios do SaaS para AEC é interoperabilidade: escritórios usam múltiplos softwares no mesmo projeto (CAD para detalhamento, Revit para BIM, MS Project para cronograma, Excel para orçamento). Soluções que se integram nativamente com os softwares já em uso têm muito menos atrito na adoção. O formato IFC (Industry Foundation Classes) é o padrão aberto de BIM — suportá-lo é requisito básico para qualquer solução que queira participar do ecossistema. Plataformas que centralizam dados de projeto de múltiplas origens (modelo BIM + orçamento + cronograma + documentos) criam o maior valor para o cliente."),
        ("Expansão de Receita e Upsell",
         "Uma vez dentro de um escritório de arquitetura ou construtora, o caminho de expansão de receita é modular: um cliente que começa com gestão de projetos pode expandir para gestão financeira de obras, depois para gestão de documentos e depois para BI e analytics. O modelo de venda por projeto ativo (que cresce com o faturamento da construtora) alinha o crescimento da receita do SaaS com o sucesso do cliente. Grandes construtoras com múltiplos escritórios regionais representam oportunidades de expansão horizontal após consolidar a referência em um escritório."),
    ],
    faq_list=[
        ("Qual o melhor perfil de vendedor para SaaS no setor AEC?",
         "O perfil ideal é um vendedor com formação ou experiência prévia em engenharia civil ou arquitetura — alguém que fala a linguagem do cliente e entende os problemas que o software resolve. Vendedores com background puramente comercial têm dificuldade em passar pela resistência técnica de arquitetos e engenheiros. Alternativamente, um modelo de vendas com engenheiro de pré-vendas (que faz as demos técnicas) apoiando um vendedor comercial funciona bem para tickets maiores."),
        ("Como lidar com pirataria de software em escritórios de arquitetura?",
         "A pirataria é comum em escritórios pequenos que usam versões não licenciadas de softwares caros. A resposta estratégica é precificar o SaaS de forma acessível para esse segmento (planos por usuário que cabem no orçamento de escritórios de 2-5 pessoas) e enfatizar os benefícios exclusivos da versão legítima: suporte técnico, atualizações, colaboração em nuvem e compliance para licitações públicas. A exigência de BIM em licitações públicas está convertendo usuários de versões piratas para licenças legítimas por necessidade regulatória."),
        ("Como o ProdutoVivo ajuda profissionais de AEC?",
         "O guia ProdutoVivo ensina arquitetos e engenheiros a transformar seu conhecimento técnico — projetos executivos, memoriais descritivos, metodologias de orçamentação — em cursos online e apps interativos de alto valor. Um especialista em BIM pode criar um treinamento de Revit para construtoras e gerar renda recorrente como infoprodutor, complementando ou até substituindo a renda de prestação de serviços."),
    ]
)

# 5164 — Clínica: Pediatria e Saúde Infantil
art(
    slug="gestao-de-clinicas-de-pediatria-e-saude-infantil",
    title="Gestão de Clínicas de Pediatria e Saúde Infantil | ProdutoVivo",
    desc="Guia de gestão para clínicas pediátricas: fidelização de famílias, protocolos de saúde preventiva, mix de convênios e particular, e marketing para pais.",
    h1="Gestão de Clínicas de Pediatria e Saúde Infantil",
    lead="A pediatria tem uma característica única: o cliente é a criança, mas o decisor e pagador são os pais. Clínicas pediátricas bem geridas constroem relacionamentos de décadas com famílias — desde o recém-nascido até a adolescência — criando uma base de receita recorrente e estável.",
    sections=[
        ("O Modelo de Negócio da Clínica Pediátrica",
         "Clínicas pediátricas operam em dois principais fluxos: atendimento de urgência (doenças agudas como infecções respiratórias, febre, gastroenterites) e saúde preventiva (puericultura, vacinas, acompanhamento de desenvolvimento). O fluxo de urgência gera volume e garante presença constante, mas é imprevisível e frequentemente realizado via convênio com margens apertadas. O acompanhamento de puericultura — consultas mensais no primeiro ano, semestrais depois — gera receita programável e oportunidade de construir vínculo com a família. Clínicas que transformam o atendimento agudo em relacionamento de puericultura têm LTV de família muito superior."),
        ("Calendário Vacinal e Serviços de Alto Valor",
         "O calendário vacinal é um dos principais motores de receita em clínicas pediátricas particulares e um differenciador competitivo importante. Vacinas do calendário SUS são oferecidas gratuitamente, mas as vacinas extras — meningocócica ACWY, varicela, HPV, rotavírus pentavalente, dengue — têm alto valor e representam decisão de compra consultiva que cabe ao pediatra orientar. Clínicas que oferecem pacotes de vacinação com preços competitivos, agendamento facilitado e registro digital do cartão de vacinação fidelizam as famílias no longo prazo. Serviços complementares como testes de alergia, nutrição pediátrica e fonoaudiologia infantil ampliam o ticket médio."),
        ("Marketing para Pais e Presença Digital",
         "Pais de primeira viagem são o público mais receptivo a conteúdo educativo sobre saúde infantil — e o mais propenso a pesquisar ativamente por pediatras de referência. Estratégias digitais eficazes incluem: canal no YouTube ou Instagram com dicas de desenvolvimento infantil, sono, alimentação e primeiros socorros; blog com respostas a perguntas frequentes de pais (que aparecem no Google); e grupos no WhatsApp para famílias de pacientes com informações sobre saúde sazonal. O Google Meu Negócio com avaliações positivas de pais é o fator mais importante para captação de novos pacientes por busca local."),
        ("Gestão de Convênios em Pediatria",
         "Pediatria é uma das especialidades com maior volume de atendimentos via convênio, o que cria pressão de margem. A estratégia é negociar valores diferenciados com as principais operadoras da região (especialmente para puericultura, que gera volume previsível), criar pacotes de saúde preventiva para o segmento particular (famílias sem convênio ou com convênio com carência), e identificar o teto máximo de atendimentos por convênio a partir do qual o custo marginal supera a receita. Algumas clínicas adotam modelo sem convênio, focando em particular com preços acessíveis — viável em regiões com boa renda média e serviço de qualidade diferenciado."),
        ("Ambiente e Experiência do Paciente",
         "Em pediatria, a experiência do paciente inclui necessariamente a experiência dos pais — e crianças que têm experiências positivas na clínica cooperam muito mais no atendimento. Salas de espera temáticas com brinquedos adequados por faixa etária, consultórios com elementos lúdicos, pediatras que se comunicam com as crianças (não apenas com os pais), e recepção acolhedora que minimiza o estresse da consulta criam uma experiência memorável que os pais compartilham espontaneamente. Programas de aniversário de pacientes (um cartão digital no aniversário da criança) são um toque de fidelização de baixo custo e alto impacto emocional."),
    ],
    faq_list=[
        ("Como estruturar um modelo de assinatura para puericultura?",
         "O modelo mais eficaz é um plano anual que inclui todas as consultas de puericultura programadas (geralmente 6-8 no primeiro ano, 4 no segundo, 2 após), um contato de telemedicina mensal para dúvidas rápidas, e desconto nas vacinas extras. Preço sugerido: R$200-400/mês, dependendo da região e posicionamento da clínica. O plano resolve dois problemas dos pais: previsibilidade de custos e acesso fácil ao pediatra sem precisar marcar consulta de urgência para dúvidas simples."),
        ("Como lidar com no-shows em clínicas pediátricas?",
         "No-shows são especialmente comuns em pediatria porque crianças que acordam com febre no dia da consulta de rotina ficam em casa. Estratégias eficazes: confirmação da consulta por WhatsApp 24h e 2h antes, política clara de reagendamento (sem taxa para remarcação com 24h de antecedência, taxa simbólica para no-show sem aviso), e lista de espera digital para preencher horários vazios com pacientes que aguardam encaixe."),
        ("Como o ProdutoVivo pode ajudar pediatras?",
         "O guia ProdutoVivo ensina pediatras e profissionais de saúde infantil a criar cursos e apps interativos para pais. Um pediatra pode desenvolver um curso de primeiros socorros para pais, um app de acompanhamento de desenvolvimento infantil, ou um programa de orientação de sono — todos com alto valor percebido e potencial de monetização como infoproduto."),
    ]
)

# 5165 — SaaS Sales: Agronegócio e Agtech
art(
    slug="vendas-para-o-setor-de-saas-de-agronegocio-e-agtech",
    title="Vendas para o Setor de SaaS de Agronegócio e Agtech | ProdutoVivo",
    desc="Estratégias de vendas para plataformas SaaS de agtech: como abordar produtores rurais, cooperativas e agroindústrias, demonstrar ROI agrícola e construir confiança no campo.",
    h1="Vendas para o Setor de SaaS de Agronegócio e Agtech",
    lead="O Brasil é uma potência agrícola e o agronegócio representa quase 30% do PIB. Mas vender tecnologia para o campo exige entender uma cultura comercial única — onde confiança e resultados práticos valem mais que apresentações corporativas e onde o ciclo de adoção tecnológica é mais lento do que em outros setores.",
    sections=[
        ("O Ecossistema de Agtech no Brasil",
         "O Brasil tem um dos ecossistemas de agtech mais dinâmicos do mundo, com startups que atendem desde pequenos agricultores familiares até grandes produtores de grãos com dezenas de milhares de hectares. As categorias de SaaS mais relevantes incluem: plataformas de gestão agrícola (monitoramento de safra, registro de aplicações, gestão de insumos), ferramentas de análise de solo e sensoriamento remoto (imagens de satélite, NDVI), sistemas de rastreabilidade e certificação (para exportação e supply chains de alimentos), plataformas de gestão financeira rural e marketplaces de insumos e crédito rural. Cada categoria tem um perfil de comprador diferente e demanda uma abordagem de vendas específica."),
        ("Perfil do Comprador no Agronegócio",
         "O decisor em propriedades rurais varia enormemente: o produtor familiar decide sozinho com base em confiança e custo-benefício imediato; a fazenda média a grande tem um gerente agrícola ou técnico que influencia e às vezes decide; as grandes operações agropecuárias têm diretores de TI e gestão que avaliam tecnologia corporativamente. Cooperativas e agroindústrias têm processos formais de compra com múltiplos stakeholders. A estratégia de vendas para agtech eficaz começa pela segmentação clara do ICP (perfil de cliente ideal) e adapta o processo de venda para cada perfil."),
        ("Construindo Confiança no Campo",
         "A maior barreira de vendas de SaaS no agronegócio não é preço — é desconfiança. Produtores rurais têm histórico de adotar tecnologias que não entregaram o prometido, sofreram problemas de conectividade ou tinham suporte deficiente. Estratégias que constroem confiança incluem: visitas de campo (o vendedor vai à propriedade, não só faz webinar), demonstração com os dados reais do produtor (usa coordenadas do talhão dele na demo), cases de produtores da mesma região e cultura com resultados mensuráveis, e indicações de técnicos agrícolas e agrônomos de confiança. A figura do agrônomo parceiro — que recomenda o software como ferramenta de trabalho — é o melhor canal de aquisição."),
        ("Adaptação ao Ciclo Agrícola",
         "O timing de vendas no agronegócio é ditado pelo calendário agrícola: produtores tomam decisões de tecnologia e investimento no período de entressafra, quando têm tempo para avaliar novas ferramentas. Vender durante o período de plantio ou colheita é praticamente impossível — o produtor está 100% focado na operação. O calendário de vendas deve mapear as janelas de decisão de cada cultura (soja, milho, cana, café, pecuária têm calendários distintos) e concentrar esforços de prospecção e demo nos meses corretos. Além disso, conectividade no campo ainda é limitada em muitas regiões — soluções com modo offline são um diferencial decisivo."),
        ("Modelos de Precificação para Agtech",
         "A precificação de SaaS para agronegócio mais bem aceita é por hectare monitorado ou por volume de produção — o produtor entende e aceita pagar mais quando produz mais. Modelos de assinatura mensal fixo funcionam para ferramentas de gestão financeira e contabilidade rural, onde o benefício é independente da safra. O período de trial alinhado ao ciclo agrícola (60-90 dias cobrindo pelo menos uma fase crítica da cultura) é mais eficaz do que trials de 14 dias. Parcerias com cooperativas para oferecer o SaaS como benefício da associação (custo subsidiado pela cooperativa) são um canal de distribuição de alto volume."),
    ],
    faq_list=[
        ("Como estruturar uma equipe de vendas para agtech cobrindo diferentes regiões agrícolas?",
         "O modelo mais eficaz é representantes regionais com expertise na cultura predominante da região: um vendedor especializado em soja no Mato Grosso, outro em cana-de-açúcar em SP/GO, outro em horticultura no Sul. Esses vendedores regionais se tornam referência no setor local, participam de eventos regionais (dias de campo, exposições agropecuárias) e constroem rede de agrônomos e técnicos. Complementar com time de inside sales para renovações e upsell de contas já estabelecidas."),
        ("Como mensurar e comunicar ROI para produtores rurais?",
         "O ROI em agtech deve ser traduzido em métricas que o produtor já usa: sacas por hectare ganhas, redução de custo de insumo por ha, horas economizadas por semana na gestão, e redução de perdas na colheita. Evite métricas tecnológicas abstratas. Um case que diz 'o produtor X na região Y economizou R$150/ha em insumos com nossa plataforma de monitoramento, com produção de 5.000ha isso representou R$750.000 em uma safra' é infinitamente mais persuasivo do que qualquer argumento técnico."),
        ("Como o ProdutoVivo ajuda profissionais de agtech?",
         "O guia ProdutoVivo ensina como transformar conhecimento técnico em agronegócio — manejo de culturas, gestão de fazenda, uso de tecnologias agrícolas — em cursos e apps interativos para produtores rurais. Um agrônomo ou especialista em agtech pode criar um treinamento premium para uso de plataformas específicas ou boas práticas de gestão rural, gerando receita recorrente como infoprodutor."),
    ]
)

# 5166 — Consulting: Planejamento Estratégico e OKRs
art(
    slug="consultoria-de-planejamento-estrategico-e-gestao-por-okrs",
    title="Consultoria de Planejamento Estratégico e Gestão por OKRs | ProdutoVivo",
    desc="Como estruturar uma consultoria de planejamento estratégico e implementação de OKRs: metodologia, entregáveis, precificação e resultados mensuráveis para PMEs.",
    h1="Consultoria de Planejamento Estratégico e Gestão por OKRs",
    lead="Planejamento estratégico e gestão por OKRs são duas das demandas mais consistentes de PMEs brasileiras que querem crescer de forma estruturada. Consultores que dominam essas metodologias e conseguem adaptá-las à realidade das empresas — sem a burocracia corporativa — têm demanda crescente e recorrente.",
    sections=[
        ("O Mercado de Consultoria Estratégica para PMEs",
         "PMEs com faturamento entre R$2M e R$50M são o mercado ideal para consultoria de planejamento estratégico e OKRs: grandes o suficiente para ter complexidade organizacional que justifica a metodologia, mas sem o orçamento ou a estrutura para contratar uma consultoria de médio porte como McKinsey ou Bain. Esse segmento tem crescimento consistente no Brasil, impulsionado pelo movimento de profissionalização de empresas familiares, aceleração de startups, e pressão por resultados mensuráveis de investidores e conselhos. Consultores independentes que cobram entre R$15-60k por projeto de planejamento estratégico têm um mercado acessível e subatendido."),
        ("Metodologia de Planejamento Estratégico",
         "A metodologia padrão de planejamento estratégico para PMEs inclui: diagnóstico (análise SWOT, análise de Porter, benchmarking competitivo, entrevistas com stakeholders), definição de visão e missão, análise de cenários, escolha de posicionamento estratégico, definição de objetivos de médio prazo e indicadores (KPIs), e criação do plano de ação com responsáveis e prazos. O diferencial do consultor independente é a capacidade de adaptar essa metodologia: simplificar o que não se aplica à empresa, aprofundar o que é crítico para o contexto específico, e garantir que o resultado final seja um documento acionável, não uma apresentação de 200 slides que fica na gaveta."),
        ("OKRs: Implementação Prática",
         "OKRs (Objectives and Key Results) é a metodologia de gestão de metas popularizada pelo Google e que chegou massivamente ao mercado brasileiro nos últimos anos. A implementação em PMEs tem desafios específicos: resistência cultural da equipe, dificuldade em definir KRs mensuráveis (times tendem a criar listas de tarefas disfarçadas de OKRs), e falta de cadência de revisão. Consultores que treinam a liderança a fazer good OKRs (ambiciosos mas atingíveis, focados em resultado e não atividade) e estabelecem a cadência de check-ins semanais e revisões trimestrais entregam o maior valor. O primeiro ciclo de OKRs deve ser simples e com vitórias rápidas para gerar confiança na metodologia."),
        ("Estrutura de Engajamento e Entregáveis",
         "Um projeto padrão de planejamento estratégico + OKRs tem três fases: diagnóstico (2-3 semanas, com entrevistas, workshops e análise de dados), construção (2-3 workshops com a liderança para definir visão, estratégia e primeiro ciclo de OKRs), e implementação (acompanhamento mensal por 3-6 meses para garantir adoção). Os entregáveis incluem: documento de planejamento estratégico, painel de OKRs configurado em ferramenta (Notion, Asana, Monday, Perdoo), playbook de gestão de OKRs para a equipe, e relatório de progresso no final de cada trimestre. Projetos com fase de acompanhamento têm NPS muito superior e geram mais indicações do que projetos de entrega única."),
        ("Precificação e Recorrência",
         "A estrutura de precificação mais eficaz para consultoria de planejamento estratégico e OKRs combina um projeto inicial (R$20-60k para a fase de diagnóstico + construção) com um retainer de acompanhamento (R$5-15k/mês para a fase de implementação). A recorrência é natural: empresas que adotam OKRs precisam de suporte no ciclo seguinte, especialmente quando expandem a metodologia para mais times. Consultores que se tornam parceiros estratégicos de longo prazo — participando das reuniões de liderança trimestralmente — têm LTV muito superior ao de projetos pontuais. A chave para essa recorrência é entregar resultados mensuráveis nos primeiros 90 dias."),
    ],
    faq_list=[
        ("Qual a diferença entre OKRs e metas tradicionais para uma PME?",
         "Metas tradicionais são geralmente numéricas, top-down e anuais (ex: crescer 30% em vendas). OKRs são ambiciosos, com múltiplas métricas de resultado (Key Results), revisados trimestralmente e construídos com participação da equipe — o que aumenta o engajamento e a clareza sobre o que precisa mudar no comportamento do time para alcançar o objetivo. Para PMEs, o maior benefício dos OKRs é criar alinhamento: todos na empresa sabem quais são as 3-5 prioridades do trimestre e como seu trabalho contribui para elas."),
        ("Como lidar com empresas que já tentaram OKRs e falharam?",
         "Falhas anteriores com OKRs geralmente têm causas conhecidas: KRs muito fáceis que não motivam mudança, falta de cadência de acompanhamento, ou liderança que não pratica o que prega. A abordagem recomendada é começar com um diagnóstico honesto do que deu errado, redesenhar o processo endereçando as causas raiz, e fazer um ciclo piloto com uma equipe pequena e motivada para criar um case interno de sucesso antes de expandir para a empresa toda."),
        ("Como o ProdutoVivo ajuda consultores de planejamento estratégico?",
         "O guia ProdutoVivo ensina como transformar metodologias de planejamento estratégico e OKRs em cursos online, templates e apps interativos. Um consultor pode criar um produto digital como 'OKRs para PMEs: guia passo a passo' ou 'Planejamento estratégico em 30 dias' — gerando renda passiva e construindo uma audiência qualificada de empresários que podem se tornar clientes de consultoria."),
    ]
)

# ── Sitemap update ────────────────────────────────────────────────────────────
sm_path = pathlib.Path(__file__).parent / "sitemap.xml"
sm = sm_path.read_text(encoding="utf-8")
new_urls = "\n".join(
    f"  <url><loc>{DOMAIN}/blog/{s}/</loc></url>"
    for s in [
        "gestao-de-negocios-de-empresa-de-b2b-saas-de-rh-e-recrutamento",
        "gestao-de-clinicas-de-oftalmologia-e-saude-ocular",
        "vendas-para-o-setor-de-saas-de-e-commerce-e-lojas-virtuais",
        "consultoria-de-fusoes-aquisicoes-e-due-diligence-empresarial",
        "gestao-de-negocios-de-empresa-de-b2b-saas-de-arquitetura-e-engenharia-civil",
        "gestao-de-clinicas-de-pediatria-e-saude-infantil",
        "vendas-para-o-setor-de-saas-de-agronegocio-e-agtech",
        "consultoria-de-planejamento-estrategico-e-gestao-por-okrs",
    ]
)
sm_path.write_text(sm.replace("</urlset>", new_urls + "\n</urlset>"), encoding="utf-8")

# ── Trilha update ─────────────────────────────────────────────────────────────
tr_path = pathlib.Path(__file__).parent / "trilha.html"
tr = tr_path.read_text(encoding="utf-8")
new_items = "\n".join(
    f'    <li><a href="{DOMAIN}/blog/{s}/">{label}</a></li>'
    for s, label in [
        ("gestao-de-negocios-de-empresa-de-b2b-saas-de-rh-e-recrutamento", "SaaS de RH e Recrutamento"),
        ("gestao-de-clinicas-de-oftalmologia-e-saude-ocular", "Clínica de Oftalmologia"),
        ("vendas-para-o-setor-de-saas-de-e-commerce-e-lojas-virtuais", "SaaS de E-commerce"),
        ("consultoria-de-fusoes-aquisicoes-e-due-diligence-empresarial", "Consultoria de M&A"),
        ("gestao-de-negocios-de-empresa-de-b2b-saas-de-arquitetura-e-engenharia-civil", "SaaS de AEC (Arquitetura/Engenharia)"),
        ("gestao-de-clinicas-de-pediatria-e-saude-infantil", "Clínica de Pediatria"),
        ("vendas-para-o-setor-de-saas-de-agronegocio-e-agtech", "SaaS de Agronegócio"),
        ("consultoria-de-planejamento-estrategico-e-gestao-por-okrs", "Consultoria de OKRs"),
    ]
)
tr_path.write_text(tr.replace("</ul>", new_items + "\n  </ul>", 1), encoding="utf-8")

print("Done — batch 1838")
