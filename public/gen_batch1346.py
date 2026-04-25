import os, json

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
<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','{pixel}');fbq('track','PageView');</script>
<style>
body{{font-family:Arial,sans-serif;margin:0;padding:0;color:#222;}}
header{{background:#1a1a2e;color:#fff;padding:16px 24px;}}
header a{{color:#e0e0ff;text-decoration:none;font-weight:bold;font-size:1.2rem;}}
main{{max-width:860px;margin:40px auto;padding:0 20px;}}
h1{{font-size:2rem;color:#1a1a2e;}}
.lead{{font-size:1.1rem;color:#444;margin-bottom:28px;}}
h2{{color:#16213e;margin-top:32px;}}
.faq{{background:#f5f7ff;border-radius:8px;padding:24px;margin-top:40px;}}
.faq h2{{color:#1a1a2e;margin-top:0;}}
.faq-item{{margin-bottom:18px;}}
.faq-item h3{{margin:0 0 6px;color:#16213e;}}
footer{{text-align:center;padding:24px;color:#888;font-size:.9rem;margin-top:60px;border-top:1px solid #eee;}}
footer a{{color:#555;}}
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
<footer><p>&copy; 2025 ProdutoVivo &mdash; <a href="/blog/">Blog</a> | <a href="/trilha">Trilha Gratuita</a></p></footer>
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
        schema_faqs.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
    schema = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": schema_faqs}, ensure_ascii=False)
    html = TMPL.format(title=title, desc=desc, url=url, pixel=PIXEL,
                       h1=h1, lead=lead, body=body_html, faqs=faqs_html, schema=schema)
    out_dir = os.path.join(BASE, slug)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

art(
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-retailtech-e-comercio-inteligente",
    "Gestão de Negócios de Empresa de B2B SaaS de Retailtech e Comércio Inteligente | ProdutoVivo",
    "Guia completo para gestão de empresas de SaaS de retailtech — PDV inteligente, omnichannel, gestão de estoque e precificação dinâmica para varejo físico e digital.",
    "Gestão de Negócios de Empresa de B2B SaaS de Retailtech e Comércio Inteligente",
    "Retailtech transforma o varejo com tecnologia — desde PDV moderno e gestão de estoque inteligente até personalização de experiência e precificação dinâmica. SaaS que resolve os problemas reais de varejistas tem mercado enorme no Brasil.",
    [
        ("O Mercado de Retailtech: Varejo Físico, E-commerce e Omnichannel",
         "O varejo brasileiro movimenta mais de R$ 2 trilhões por ano — com uma transição acelerada para o omnichannel, onde o mesmo consumidor pesquisa online, compra na loja física, e troca pelo app. SaaS de retailtech atendem diferentes segmentos: PDV e gestão de loja (ponto de venda, controle de caixa, gestão de funcionários), e-commerce e marketplaces (plataformas de venda online, integração com Mercado Livre, Amazon, VTEX), e tecnologias de loja física (self-checkout, fila virtual, analytics de comportamento no ponto de venda). O maior mercado para SaaS é o varejo de médio porte (20-200 lojas) que precisa de tecnologia enterprise mas com custo de PME."),
        ("PDV Inteligente: Além da Gaveta de Dinheiro",
         "O PDV (Ponto de Venda) moderno vai muito além da gaveta e da impressora de cupom — é o hub operacional da loja: emissão de NFC-e (Nota Fiscal ao Consumidor eletrônica), integração com TEF para pagamentos, controle de estoque em tempo real a cada venda, gestão de fidelidade com CPF do cliente, e relatórios de desempenho por produto, vendedor e período. SaaS de PDV em nuvem têm vantagem sobre sistemas legados offline — atualização automática de alíquotas fiscais, backup em nuvem, e gestão remota de múltiplas unidades a partir de um dashboard central."),
        ("Gestão de Estoque e Reabastecimento Inteligente",
         "Ruptura de estoque (produto em falta no momento da compra) é o maior problema de varejo — custa em média 8-10% do faturamento em vendas perdidas. Por outro lado, excesso de estoque imobiliza capital e gera perdas por vencimento ou obsolescência. Sistemas de gestão de estoque com reabastecimento automático baseado em curva ABC, lead time do fornecedor, e sazonalidade histórica, reduzem a ruptura e o excesso simultaneamente. Integração com XML de NF-e para entrada automática de mercadorias elimina o processo manual mais propenso a erros no varejo."),
        ("Precificação Dinâmica e Inteligência de Mercado",
         "Precificação dinâmica — ajustar preços automaticamente com base em demanda, estoque, concorrência e margem desejada — era privilégio de grandes varejistas. SaaS de pricing inteligente democratizam essa capacidade para varejistas de médio porte: monitoramento automático de preços do concorrente (scraping de e-commerce), sugestão de preço ótimo que maximiza margem × giro, e regras de precificação por categoria e canal. Para perecíveis, precificação dinâmica baseada em data de vencimento reduz perdas por obsolescência em 30-50%."),
        ("Go-to-Market: Atacadistas, Franquias e Redes Regionais",
         "O canal mais eficaz para SaaS de retailtech são redes regionais de médio porte (20-100 lojas) e franqueadoras que precisam de consistência tecnológica entre franqueados. Franquias têm um desafio específico: garantir que todos os franqueados usem o mesmo sistema, com integração de dados para o franqueador enxergar desempenho consolidado. Atacadistas de distribuição (que vendem para varejistas de menor porte) são parceiros de canal eficazes — já têm o relacionamento e podem incluir o SaaS como serviço de valor agregado. Eventos como APAS Show, ABF Expo e Fecomércio são canais de networking essenciais."),
    ],
    [
        ("Qual e o ticket medio de SaaS de PDV para varejo?", "Para lojas independentes e pequenas redes (1-5 lojas): R$ 200-600/mes por loja. Para redes de medio porte (10-50 lojas): R$ 300-800/mes por loja com desconto por volume. Para redes maiores com modulos avancados de BI e gestao de categoria: R$ 500-1.500/mes por loja. O modelo mais comum e por unidade (loja ou CNPJ), o que cria crescimento natural da receita conforme a rede expande. Fee de implementacao varia de R$ 500-5.000 por loja dependendo da complexidade da integracao fiscal (SEFAZ estadual e regras de ICMS)."),
        ("Como SaaS de retailtech compete com sistemas legados como Microsiga e Linx?", "Linx e Microsiga Varejo dominam o mercado enterprise com integracao fiscal robusta, mas tem custo alto (R$ 1.000-5.000/mes por loja) e UX datada. O espaco para competir e em: redes de 5-30 lojas que cresceram usando Excel e sistemas basicos, setores verticais especificos (moda, farmacias, pet shops, materiais de construcao) onde experiencia setorial cria vantagem, e novas necessidades como omnichannel e integracao com marketplaces que sistemas legados suportam mal. Preco 50-70% menor com UX moderna e implementacao mais rapida sao os argumentos centrais."),
        ("Omnichannel e essencial para varejistas de medio porte?", "Sim — 70% dos consumidores brasileiros pesquisam online antes de comprar na loja fisica (comportamento ROPO: Research Online, Purchase Offline). Varejistas sem presenca digital perdem vendas para concorrentes com e-commerce. Mas omnichannel vai alem de ter um site — e ter estoque unificado (o produto da loja aparece disponivel no site), precificacao consistente entre canais, e logistica integrada (retirar na loja, devolver na loja compra online). SaaS que entregam essa unificacao de forma simples para varejistas de medio porte tem proposta de valor muito forte."),
    ]
)

art(
    "gestao-de-clinicas-de-oncologia-hematologica-e-linfomas",
    "Gestão de Clínicas de Oncologia Hematológica e Linfomas | ProdutoVivo",
    "Guia completo para gestão de clínicas de oncologia hematológica — leucemias, linfomas, mieloma múltiplo, protocolos de quimioterapia e transplante de medula óssea.",
    "Gestão de Clínicas de Oncologia Hematológica e Linfomas",
    "Oncologia hematológica trata cânceres do sangue — leucemias agudas e crônicas, linfomas de Hodgkin e não-Hodgkin, e mieloma múltiplo. São doenças de alta complexidade que exigem protocolos de quimioterapia específicos e acompanhamento intensivo.",
    [
        ("Protocolos de Quimioterapia em Hematologia: R-CHOP, ABVD e Hipercvad",
         "Oncologia hematológica tem protocolos de quimioterapia altamente específicos por diagnóstico e estadiamento: R-CHOP (rituximabe + ciclofosfamida + doxorrubicina + vincristina + prednisona) para linfoma difuso de grandes células B, ABVD (adriamicina + bleomicina + vinblastina + dacarbazina) para linfoma de Hodgkin, HiperCVAD (ciclofosfamida + vincristina + doxorrubicina + dexametasona alternado com metotrexato + citarabina) para leucemia linfoblástica aguda. Sistemas que registrem o protocolo completo — com cálculo de doses por SCq (superfície corpórea), datas de cada ciclo, e controle de toxicidade — são ferramentas de segurança críticas."),
        ("Controle de Toxicidade: Citopenia, Infecção e Toxicidade Orgânica",
         "Quimioterapia hematológica causa toxicidade intensa — mielossupressão profunda (neutropenia febril, anemia, plaquetopenia), cardiotoxicidade (antraciclinas), neurotoxicidade (vincristina), nefrotoxicidade e cistite hemorrágica (ciclofosfamida). O acompanhamento requer hemogramas frequentes (às vezes diários durante quimioterapia intensiva) e ajuste de dose ou adiamento de ciclo baseado nos nadir de neutrófilos e plaquetas. Sistemas que integrem os resultados laboratoriais, calculem automaticamente os nadir esperados por protocolo, e alertem para critérios de internação (neutropenia febril com ANC < 500), são ferramentas de segurança indispensáveis."),
        ("Terapias-Alvo e Imunoterapia em Hematologia",
         "A revolução terapêutica em hematologia oncológica vem das terapias-alvo e imunoterapia: imatinibe e nilotinibe para LMC (leucemia mieloide crônica) com monitoramento molecular de BCR-ABL, ibrutinibe e venetoclax para LLC (leucemia linfocítica crônica), rituximabe e obinutuzumabe para linfomas B, e CAR-T cell therapy para linfomas e leucemias refratárias. Sistemas que registrem a resposta molecular ao imatinibe (PCR quantitativa trimestral para BCR-ABL), o estadiamento de linfoma por critérios Lugano (PET-CT), e os eventos adversos específicos de cada terapia-alvo, têm valor clínico imenso."),
        ("Transplante de Medula Óssea: Avaliação e Seguimento",
         "Transplante de medula óssea (TMO) autólogo e alogênico é parte do tratamento de leucemias, linfomas recidivados e mieloma múltiplo. O processo envolve: avaliação pré-TMO (estadiamento da doença, avaliação cardiopulmonar, compatibilidade HLA no alogênico), condicionamento (quimioterapia mieloablativa), infusão do enxerto, e seguimento pós-TMO (pega do enxerto, doença do enxerto-versus-hospedeiro, reconstitução imune). Centros de TMO precisam de sistemas específicos para esse fluxo — com rastreamento do doador, controle de HLA, e monitoramento de enxerto versus hospedeiro."),
        ("Faturamento: Protocolos de QT de Alta Complexidade e APAC",
         "Quimioterapia hematológica é faturada via APAC (Autorização de Procedimentos de Alta Complexidade) para o SUS, com laudos específicos e renovações periódicas. Para convênios, os protocolos têm cobertura variável — rituximabe e terapias-alvo de alto custo frequentemente exigem autorização prévia com documentação detalhada. O faturamento correto de todos os medicamentos utilizados em cada ciclo (com apresentações, doses e vias de administração) é crítico — erros custam R$ 10.000-100.000 por ciclo em medicamentos não reembolsados."),
    ],
    [
        ("Quais sistemas sao mais usados em oncologia hematologica?", "Em centros de referencia, sistemas especializados em oncologia como Varian Aria, Elekta Mosaic (mais usados em radioterapia) e modulos de quimioterapia de sistemas hospitalares como Tasy e MV sao comuns. Para oncologia hematologica ambulatorial, ha lacuna importante de sistemas que integrem controle de protocolo de QT, monitoramento de toxicidade e registro de resposta molecular — a maioria usa prontuarios genéricos com workflows customizados. Essa lacuna representa oportunidade para SaaS especializado no nicho."),
        ("Como estruturar o controle de protocolos de quimioterapia em uma clinica de hematologia?", "Crie um catalogo de protocolos com doses padronizadas por SCq, intervalos entre ciclos, exames pre-ciclo obrigatorios (hemograma, funcao renal, ECG para cardiotoxicos), e criterios de reducao ou suspensao de dose por toxicidade. Para cada paciente em tratamento, gere automaticamente o calendario de ciclos e os pedidos de exames pre-ciclo. Antes de cada ciclo, o sistema deve verificar se os criterios de nadir foram atingidos e alertar para situacoes de risco (anemia, plaquetopenia, neutropenia). Essa verificacao automatica e o diferencial mais valorizado em sistemas de quimioterapia."),
        ("Qual e o ticket medio para SaaS de oncologia hematologica?", "O ticket para SaaS especializado em oncologia hematologica fica entre R$ 2.000 e R$ 8.000/mes para ambulatorios de quimioterapia de medio porte. Centros de transplante de medula ossea (TMO) com modulo especifico de gestao de transplante podem justificar tickets de R$ 6.000-15.000/mes. O churn e muito baixo — uma vez que o sistema acumula o historico de protocolos e toxicidades de pacientes em tratamento, a migracao e quase impossivel sem risco clinico."),
    ]
)

art(
    "vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-psicologia-adulto-e-terapia",
    "Vendas para o Setor de SaaS de Gestão de Clínicas de Psicologia Adulto e Terapia | ProdutoVivo",
    "Estratégias B2B para vender SaaS de gestão a clínicas de psicologia e terapia para adultos — como abordar psicólogos, apresentar valor e fechar contratos neste mercado em crescimento.",
    "Vendas para o Setor de SaaS de Gestão de Clínicas de Psicologia Adulto e Terapia",
    "O mercado de saúde mental cresceu exponencialmente após a pandemia. Psicólogos e clínicas de terapia buscam sistemas que automatizem agendamento, prontuário e cobrança, liberando mais tempo para o atendimento.",
    [
        ("Perfil do Decisor: Psicólogo Autônomo e Gestor de Clínica de Saúde Mental",
         "O mercado de psicologia tem dois perfis principais: psicólogos autônomos (que atendem 20-40 pacientes semanais em consultório próprio ou alugado) e clínicas multiprofissionais de saúde mental (com psicólogos, psiquiatras e outros profissionais). O psicólogo autônomo valoriza principalmente: agendamento online que reduz no-show, prontuário digital seguro conforme resolução do CFP, e cobrança simplificada (recibo, PIX integrado). A clínica multiprofissional precisa adicionalmente de gestão de equipe, faturamento de convênios, e relatórios gerenciais."),
        ("Prontuário Psicológico: Sigilo e Resolução CFP",
         "O prontuário psicológico tem requisitos éticos muito específicos definidos pelo CFP (Conselho Federal de Psicologia) — Resolução CFM 001/2009 e 004/2020. O prontuário deve ser mantido por 5 anos (10 anos para menores), com controle de acesso restrito (apenas o psicólogo responsável), e o sigilo profissional é absoluto — dados de sessões não podem ser compartilhados sem autorização expressa do paciente. Sistemas que implementam esses controles de forma clara — com log de acesso auditável, criptografia de dados e política de privacidade alinhada à LGPD — têm muito mais credibilidade junto ao CFP e aos psicólogos."),
        ("Redução de No-Show: Confirmação Automática e Lista de Espera",
         "No-show (paciente que não comparece à sessão sem aviso) é o maior problema financeiro do psicólogo autônomo — uma sessão não realizada representa 100% de perda de receita para um serviço de alto custo variável zero. Sistemas com confirmação automática de consulta por WhatsApp 24-48 horas antes, link de cancelamento que coloca automaticamente o próximo da lista de espera no horário disponível, e cobrança de taxa de no-show via cartão pré-cadastrado, reduzem o no-show de 15-25% para menos de 5%. Este argumento tem ROI imediato e quantificável."),
        ("Telepsicologia: Atendimento Online com Conformidade CFP",
         "A Resolução CFP 11/2018 regulamentou definitivamente a telepsicologia no Brasil — atendimento por videoconferência com requisitos específicos de privacidade e segurança. Plataformas de telepsicologia devem ter: criptografia de ponta a ponta, servidor no Brasil ou com adequação à LGPD, e registro do consentimento informado do paciente para o atendimento remoto. Sistemas de gestão que incluam plataforma de videoconferência integrada — sem que o paciente precise baixar app ou o psicólogo mude de sistema — têm muito mais adoção do que soluções que dependem de Zoom ou Google Meet externos."),
        ("Abordagem e Proposta de Valor: ROI do No-Show",
         "A demonstração mais eficaz para psicólogos começa pelo cálculo do no-show: quantas sessões foram perdidas no último mês? A um valor médio de R$ 150-250/sessão, 4 no-shows por mês representam R$ 600-1.000 de receita perdida. Um SaaS que custe R$ 80-150/mês e elimine o no-show se paga em 1-2 semanas. Mostre o confirmador automático de consulta em ação, o prontuário com controle de acesso CFP-compliant, e a cobrança simplificada por PIX com recibo automático. Para clínicas, adicione o dashboard de ocupação e o relatório de faturamento por profissional."),
    ],
    [
        ("Quais sistemas sao mais usados por psicologos?", "Os sistemas mais populares entre psicologos brasileiros incluem: iClinic, Ninsaude Apolo, Psicomanager, Vitafor e Clinicorp. A maioria desses sistemas atende multiplas especialidades, com modulo de psicologia. Sistemas especificamente desenhados para psicologia (com terminologia correta do CFP, controle de sigilo por resolucao vigente, e prontuario sem campos medicos desnecessarios) tem vantagem de adocao com o publico de saude mental. O diferencial de telepsicologia integrada e cada vez mais valorizado."),
        ("Como abordar psicologos para vender SaaS?", "Psicologos sao muito presentes nas redes sociais profissionais — Instagram e LinkedIn sao os canais de marketing de conteudo mais eficazes. Conteudo sobre gestao de consultorio, precificacao de servicos e reducao de no-show gera engajamento muito alto nesse publico. Parcerias com CFP regional (Conselhos de Psicologia estaduais) e cursos de pos-graduacao em psicologia clinica sao canais de distribuicao relevantes. Um trial gratuito de 30 dias com onboarding guiado tem taxa de conversao muito maior do que demonstracoes ao vivo nesse publico."),
        ("Qual e o ticket medio para SaaS de psicologia?", "Para psicologos autonomos: R$ 70-150/mes (sensivel ao preco, mas altamente retido se o sistema entrega no reducao de no-show). Para clinicas de saude mental com 5-15 profissionais: R$ 400-1.200/mes. Para redes e grupos de saude mental com multiplas unidades: R$ 1.500-5.000/mes. A saude mental e um dos mercados de SaaS de saude com maior potencial de crescimento nos proximos 5 anos — o numero de psicologos ativos cresceu 40% nos ultimos 5 anos e a demanda por atendimento continua crescendo."),
    ]
)

art(
    "consultoria-de-gestao-de-pessoas-e-cultura-em-startups-e-scale-ups",
    "Consultoria de Gestão de Pessoas e Cultura em Startups e Scale-Ups | ProdutoVivo",
    "Como estruturar e vender consultoria de gestão de pessoas para startups e scale-ups — cultura organizacional, People Ops, estrutura de times, compensação e retenção de talentos.",
    "Consultoria de Gestão de Pessoas e Cultura em Startups e Scale-Ups",
    "Startups que crescem rapidamente frequentemente negligenciam a área de pessoas — até que enfrentam alta rotatividade, conflitos de liderança ou dificuldade para contratar. Consultores de People especializados em empresas de alto crescimento têm demanda crescente.",
    [
        ("Os Problemas de Pessoas em Scale-Ups: Da Tribo à Organização",
         "Startups em fase inicial funcionam como tribos — todos se conhecem, a cultura é implícita, decisões são rápidas e informais. Quando a empresa chega a 50-100 pessoas, essa estrutura quebra: novos funcionários não sabem o que é esperado, decisões ficam centralizadas no fundador que é o único com contexto, culturas diferentes emergem entre times que mal se comunicam, e o turnover começa a subir. O consultor de pessoas diagnostica esse momento de ruptura e ajuda a empresa a construir estruturas que preservam o que é bom da cultura original enquanto criam ordem necessária para escalar."),
        ("People Ops: Da Administração de RH à Estratégia de Pessoas",
         "People Ops (ou HR moderno em startups) vai além da administração de folha e benefícios — é uma função estratégica que garante que a empresa tem as pessoas certas, no lugar certo, desenvolvidas e engajadas. Inclui: talent acquisition (recruiting como função de produto, com funil, métricas e melhoria contínua), onboarding estruturado (que acelera a produtividade de novos colaboradores), people analytics (usar dados para entender rotatividade, engajamento e produtividade), e gestão de desempenho (calibrações, promoções, PIPs). O consultor estrutura essa função do zero ou profissionaliza o que existe."),
        ("Cultura Organizacional: Da Declaração à Operacionalização",
         "Valores declarados numa parede não criam cultura — comportamentos reais criam cultura. O trabalho do consultor é identificar os comportamentos que a empresa quer reforçar, e criar mecanismos que os tornem reais: processo de admissão que avalia fit cultural além das competências técnicas, rituais de reforço (como reuniões onde histórias de cultura são compartilhadas), sistema de reconhecimento de comportamentos culturais, e avaliação de desempenho que inclui 'como' ao lado do 'o quê'. Culturas fortes não acontecem por acidente — são projetadas e gerenciadas ativamente."),
        ("Compensação e Equity: Atraindo Talentos Sem Ser a Empresa com Maior Salário",
         "Startups raramente podem competir com salários de grandes corporações ou multinationals para top performers. A estratégia de compensação de startups usa três alavancas: salário base competitivo (80-90% do mercado, não o topo), equity significativo (stock options ou phantom shares com vesting de 4 anos e cliff de 1 ano), e benefícios de estilo de vida (trabalho remoto/híbrido, horário flexível, autonomia, oportunidade de crescimento acelerado). O consultor estrutura a política de compensação com bandas salariais, política de equity e critérios de promoção — essencial para times acima de 30 pessoas."),
        ("Retenção de Talentos: Por Que as Pessoas Saem e o Que Fazer",
         "A pesquisa consistentemente mostra que as principais causas de turnover em startups são: relacionamento com o gestor direto (não com a empresa), falta de clareza sobre crescimento de carreira, desalinhamento de valores, e — em escala menor — compensação. Consultores de pessoas implementam: entrevistas de desligamento estruturadas para identificar padrões, pesquisas de pulso mensais (3-5 perguntas) para monitorar engajamento em tempo real, programas de desenvolvimento de liderança para melhorar a qualidade dos gestores, e trilhas de carreira transparentes que mostram o que é preciso para avançar."),
    ],
    [
        ("Quando uma startup deve contratar consultoria de gestao de pessoas?", "Os momentos criticos sao: (1) 30-50 funcionarios — quando o fundador perde o contato direto com todos e a cultura começa a diluir; (2) primeiro Head of People — quando a empresa contrata o primeiro profissional de RH, um consultor pode ajudá-lo a estruturar a area rapidamente; (3) alta de turnover — quando o churn de talentos passa de 15-20% ao ano, e e preciso diagnosticar e intervir; (4) pre-series B ou C — quando investidores exigem maturidade de gestao de pessoas como parte do due diligence."),
        ("Quanto custa consultoria de People para startups?", "Projetos de diagnostico de cultura e proposta de estrutura de People Ops: R$ 20k-60k. Implementacao completa (definicao de valores, estrutura de carreira, politica de compensacao, onboarding): R$ 50k-180k. Retainer de People Advisor (consultor de pessoas parcial, 2-4 dias/semana): R$ 8k-20k/mes. Treinamentos de lideranca e gestores: R$ 3k-8k por turma. Para startups pre-series A, um People Advisor parcial é frequentemente mais custo-efetivo do que um Head of People full-time."),
        ("Como criar um programa de equity que retém talentos?", "Um programa de equity eficaz tem: (1) percentual relevante — para atrair talentos senior, o grant inicial deve ser significativo (0.1-1% para C-level, 0.01-0.1% para IC senior); (2) vesting com cliff — 4 anos com cliff de 1 ano e vesting mensal depois é o padrao; (3) comunicacao clara — a maioria dos colaboradores nao entende o valor potencial do equity; o consultor ajuda a criar documentacao e sessoes educativas; (4) refresh grants — para reter top performers apos o cliff inicial, grants adicionais são necessarios; (5) liquidez — colaboradores precisam entender quando e como podem vender suas acoes."),
    ]
)

art(
    "gestao-de-negocios-de-empresa-de-b2b-saas-de-energytech-e-gestao-de-energia",
    "Gestão de Negócios de Empresa de B2B SaaS de Energytech e Gestão de Energia | ProdutoVivo",
    "Guia completo para gestão de empresas de SaaS de energytech — gestão de energia, eficiência energética, mercado livre de energia e descarbonização para indústria e comércio.",
    "Gestão de Negócios de Empresa de B2B SaaS de Energytech e Gestão de Energia",
    "Energytech está em alta com a pressão por eficiência energética, metas ESG de descarbonização e abertura do mercado livre de energia para consumidores menores. SaaS que ajudam empresas a gerenciar e reduzir custo de energia têm mercado crescente.",
    [
        ("O Mercado de Energytech: Eficiência, Mercado Livre e Renováveis",
         "Energytech abrange três mercados complementares: eficiência energética (monitoramento de consumo, identificação de desperdícios e projetos de retrofit — motores, iluminação LED, HVAC), mercado livre de energia (migração do mercado cativo para o Ambiente de Contratação Livre, onde empresas compram energia diretamente de geradores com preço negociado), e renováveis distribuídas (geração solar fotovoltaica, compensação de energia, e GD — Geração Distribuída). Empresas com conta de energia acima de R$ 30.000/mês têm interesse crescente em todas as três frentes."),
        ("Gestão de Energia: Medição, Monitoramento e Relatórios",
         "A base de qualquer estratégia de eficiência energética é medir o consumo em tempo real. Sistemas de gestão de energia coletam dados de medidores inteligentes ou do quadro de distribuição, apresentam dashboards de consumo por unidade, equipamento e período, identificam picos de demanda (que geram tarifas extras na conta de energia), comparam o consumo real com benchmarks do setor, e geram relatórios para ISO 50001 e para metas de ESG. A integração com dados de produção (kWh/tonelada produzida) permite calcular a intensidade energética — métrica essencial para empresas industriais."),
        ("Mercado Livre de Energia: Migração, Gestão e Compliance",
         "O mercado livre de energia permite que consumidores com demanda acima de 500 kW (e progressivamente menor a partir de 2024) comprem energia diretamente de geradores com preço e prazo negociados. A gestão no mercado livre envolve: análise da viabilidade de migração (comparando custo atual no mercado cativo com projeções do mercado livre), estruturação do contrato de compra de energia, gestão do relacionamento com o comercializador (ajuste de contrato, risco de preço de curto prazo), e compliance com a ANEEL (declaração de operação, medição e faturamento). SaaS que automatizam essas tarefas reduzem o custo de gestão de energia para o cliente."),
        ("Go-to-Market: Gerentes de Energia, ESG e Facilities",
         "Compradores de SaaS de energytech são gerentes de energia e utilities em indústrias, gerentes de facilities em shoppings e prédios corporativos, e diretores de ESG em empresas que precisam reportar emissões de carbono. Canais eficazes incluem: consultorias de energia que já fazem projetos de eficiência e precisam de software, distribuidores de equipamentos de monitoramento (que podem incluir o SaaS como serviço), e eventos do setor (Intersolar, SNPTEE, eventos da ABRACE). O argumento de venda mais forte é o cálculo do custo evitado — quanto a empresa vai economizar na conta de energia com a gestão eficiente."),
        ("Modelo de Negócio: Economia Compartilhada e SaaS Recorrente",
         "Energytech tem modelos de negócio criativos além do SaaS recorrente puro: economia compartilhada (o cliente paga um percentual da economia gerada — alinha incentivos mas é mais difícil de monetizar em escala), performance contracting (o SaaS garante determinado nível de economia e é pago pelo resultado), e SaaS por ponto de medição (escalável com o crescimento da empresa cliente). Para mercado livre de energia, o modelo de gestão como serviço (taxa mensal pelo gerenciamento do contrato e das posições) é muito comum — o cliente não quer se preocupar com a complexidade regulatória do ACL."),
    ],
    [
        ("Qual e o potencial de economia de energia com SaaS de gestao energetica?", "Empresas que implementam gestao de energia estruturada economizam em media 10-20% na conta de energia — apenas por identificar e corrigir ineficiencias (equipamentos ligados fora do horario, ajuste de demanda contratada, otimizacao de fator de potencia). Para uma empresa com conta de energia de R$ 100.000/mes, isso representa R$ 10.000-20.000/mes de economia. Um SaaS de gestao de energia que custe R$ 2.000-5.000/mes tem ROI de 2-10x — um dos ROIs mais faceis de demonstrar em qualquer SaaS B2B."),
        ("Mercado livre de energia vale a pena para PMEs?", "A Resolucao ANEEL 1000/2021 abriu o mercado livre para consumidores com demanda a partir de 500 kW em 2024, e o roadmap prevê abertura progressiva ate consumidores residenciais ate 2026. Para empresas acima de 500 kW, a migracao para o mercado livre pode gerar economia de 15-30% no custo de energia. O risco e o preco de curto prazo (quando o contrato nao cobre toda a demanda, a diferenca e liquidada a preco spot — que pode ser alto em anos secos). SaaS que gerenciam esse risco e otimizam a posicao contratual entregam valor real alem da migracao."),
        ("Como SaaS de energytech se posiciona no contexto de ESG?", "Reducao de consumo de energia e descarbonizacao sao objetivos centrais da agenda ESG corporativa. SaaS que calculam automaticamente a pegada de carbono associada ao consumo de energia (em tCO2e), monitoram a progressao em relacao as metas Net Zero, e geram relatorios no padrao GRI ou TCFD para disclosure sustentabilidade, sao percebidos como infraestrutura de ESG — com um ciclo de venda no C-level muito mais curto do que SaaS de eficiencia operacional. Integrar os dados de energia com os relatorios de sustentabilidade e um dos maiores diferencias no mercado atual."),
    ]
)

art(
    "gestao-de-clinicas-de-pneumologia-pediatrica-e-fibrose-cistica",
    "Gestão de Clínicas de Pneumologia Pediátrica e Fibrose Cística | ProdutoVivo",
    "Guia completo para gestão de clínicas de pneumologia pediátrica — asma infantil, bronquiolite, fibrose cística e programas de função pulmonar pediátrica.",
    "Gestão de Clínicas de Pneumologia Pediátrica e Fibrose Cística",
    "Pneumologia pediátrica trata doenças respiratórias na criança — desde asma e bronquiolite até fibrose cística e bronquiectasias. A gestão de pacientes crônicos com fibrose cística exige sistemas especializados de acompanhamento longitudinal.",
    [
        ("Asma Infantil: Protocolos GINA Pediátricos e Escalas de Controle",
         "Asma é a doença crônica mais comum na infância — afeta 10-20% das crianças brasileiras. O manejo segue as diretrizes GINA adaptadas para pediatria, com atenção às faixas etárias (< 5 anos, 6-11 anos, ≥ 12 anos) que têm abordagens diagnósticas e terapêuticas diferentes. A espirometria só é confiável em crianças acima de 5-6 anos — abaixo dessa idade, o diagnóstico é clínico. Sistemas que registrem o escore de controle da asma por faixa etária (CTA para < 12 anos, ACT para ≥ 12 anos), o nível de controle e o degrau de tratamento GINA atual, facilitam a tomada de decisão terapêutica."),
        ("Fibrose Cística: Seguimento Multidisciplinar e Função Pulmonar",
         "Fibrose cística (FC) é a doença genética grave mais comum em caucasianos — causa disfunção de múltiplos órgãos, mas principalmente pulmão e pâncreas. O acompanhamento multidisciplinar envolve: pneumologista pediátrico (função pulmonar com VEF1 trimestral, microbiologia de escarro semestral, culturas específicas para PA e MRSA), nutricionista (estado nutricional e suplementação de enzimas pancreáticas), fisioterapeuta (fisioterapia respiratória diária e técnicas de clearance), e geneticista (identificação de mutações para elegibilidade aos moduladores — ivacaftor, lumacaftor, elexacaftor). Sistemas que integrem todas as especialidades no mesmo prontuário e monitorem o percentual predito de VEF1 ao longo do tempo são essenciais."),
        ("Bronquiolite e Sibilância Recorrente: Diagnóstico Diferencial e Seguimento",
         "Bronquiolite aguda (geralmente por VSR no lactente) e sibilância recorrente (pré-asma em crianças < 3 anos) são as condições respiratórias mais frequentes em lactentes. O diagnóstico diferencial é importante — sibilância recorrente em crianças < 3 anos pode ser asma precoce, mas também aspiração de corpo estranho, malformações pulmonares ou refluxo gastroesofágico. Sistemas que registrem o índice API (Asthma Predictive Index) e facilitem o seguimento de crianças com sibilância recorrente para identificar os que vão evoluir para asma ajudam a personalizar o tratamento."),
        ("Função Pulmonar Pediátrica: Z-Scores e Referências Globais LMS",
         "Espirometria pediátrica tem interpretação diferente do adulto — em crianças, é mais adequado usar Z-scores (desvios da mediana para idade, sexo e etnia) do que percentuais do predito. O Global Lung Initiative (GLI 2012) fornece as equações de referência mais aceitas internacionalmente. Sistemas que calculem automaticamente os Z-scores de VEF1, CVF e VEF1/CVF com base nas equações GLI 2012 — alertando para valores abaixo de -1,64 Z (percentil 5) como anormais — têm muito mais valor clínico do que sistemas que usam percentuais de predito baseados em equações desatualizadas."),
        ("Faturamento: Espirometria Pediátrica e Consultas de Doença Crônica",
         "Clínicas de pneumologia pediátrica realizam: espirometria com e sem broncodilatador (com código específico para pediatria), teste de suor (para diagnóstico de fibrose cística), oscilometria de impulso (alternativa à espirometria em crianças < 5 anos), e consultas de doença crônica com tempo estendido. Convênios frequentemente limitam o número de espirometrias cobertas por paciente por ano — sistemas que documentem claramente a indicação médica de cada exame facilitam a justificativa para o convênio e reduzem glosas."),
    ],
    [
        ("Quais sistemas sao mais usados em pneumologia pediatrica?", "Pneumologia pediatrica frequentemente usa sistemas gerais de pediatria com modulos de espirometria customizados. A principal lacuna e um sistema com z-scores automaticos pelo GLI 2012 integrado ao laudo de espirometria, e gestao especifica para fibrose cistica com registro de VEF1 em serie e microbiologia respiratoria. Centro de referencia em fibrose cistica normalmente tem registro no Registro Brasileiro de Fibrose Cistica (REBRAFC) — sistemas que facilitem a exportacao de dados para o registro nacional tem valor adicional."),
        ("Como estruturar um centro de referencia em fibrose cistica?", "Um centro de referencia em FC deve ter: (1) equipe multidisciplinar completa (pneumologista, nutricionista, fisioterapeuta, assistente social, psicólogo — todos com treinamento especifico em FC); (2) laboratorio de microbiologia respiratoria com tecnicas especificas para PA mucoide e MRSA; (3) registro de todos os pacientes no REBRAFC; (4) protocolo claro de progressao de tratamento incluindo criterios de inicio dos moduladores; (5) programa de fisioterapia respiratoria com tecnicas de clearance (Flutter, SHAKER, vest). O seguimento trimestral com espirometria e culturas de escarro e o padrao de cuidado."),
        ("Qual e o ticket medio para SaaS de pneumologia pediatrica?", "O ticket para SaaS com modulo especifico de espirometria pediatrica com z-scores e gestao de fibrose cistica fica entre R$ 800 e R$ 2.500/mes. Centros de referencia em FC com alto volume de pacientes cronicos e multiprofissionais podem justificar tickets de R$ 2.000-4.000/mes. O mercado de pneumologia pediatrica e menor que o de pneumologia adulto — mas o perfil de paciente cronico com FC tem LTV muito alto e torna qualquer solucao que melhore a gestao do programa extremamente valiosa."),
    ]
)

art(
    "vendas-para-o-setor-de-saas-de-gestao-de-clinicas-de-odontologia-estetica-e-reabilitacao-oral",
    "Vendas para o Setor de SaaS de Gestão de Clínicas de Odontologia Estética e Reabilitação Oral | ProdutoVivo",
    "Estratégias B2B para vender SaaS de gestão a clínicas de odontologia estética — como abordar dentistas, apresentar valor e fechar contratos neste mercado de alto ticket.",
    "Vendas para o Setor de SaaS de Gestão de Clínicas de Odontologia Estética e Reabilitação Oral",
    "Odontologia estética e reabilitação oral são nichos de alto ticket — facetas, implantes e lentes de contato dental geram receita significativa por paciente. SaaS que otimiza agendamento, plano de tratamento e cobrança tem ROI imediato.",
    [
        ("Perfil do Decisor: Dentista Especialista e Gestor de Clínica Odontológica",
         "Dentistas de odontologia estética e reabilitação oral atendem pacientes de alta renda com tratamentos de longa duração — reabilitação total com implantes pode durar 12-18 meses e custar R$ 30.000-150.000. Valorizam sistemas que suportem plano de tratamento detalhado (com odontograma digital, lista de procedimentos e cronograma), orçamento com parcelamento e controle de pagamentos, e documentação fotográfica (fotos de antes/depois para portfolio e para o paciente). A gestão financeira do plano de tratamento — garantindo que o paciente está pagando conforme realiza os procedimentos — é crítica."),
        ("Plano de Tratamento Digital: Odontograma e Cronograma de Procedimentos",
         "Um plano de tratamento odontológico de reabilitação pode envolver dezenas de procedimentos ao longo de meses — extrações, enxertos ósseos, instalação de implantes, período de osseointegração, moldagem, prototipagem, instalação de próteses e ajustes. Sistemas com odontograma digital interativo (onde o dentista seleciona dente por dente os procedimentos planejados), cronograma de consultas vinculado ao plano, e controle de o que já foi realizado versus o que está pendente, facilitam muito a comunicação com o paciente e o controle financeiro."),
        ("Fotodocumentação Clínica: Portfolio e Antes/Depois",
         "Documentação fotográfica de alta qualidade é o principal ativo de marketing do dentista estético — fotos de antes/depois são o argumento mais poderoso para atrair novos pacientes. Sistemas com fototeca organizada por paciente e procedimento, composta de sequências fotográficas padronizadas (extraoral frontal, sorriso, detalhes), comparação lado a lado de antes/depois, e exportação fácil para uso em redes sociais (com anonimização do paciente), são diferenciais muito valorizados. O sistema que organiza o portfolio fotográfico de um dentista estético agrega valor além do prontuário."),
        ("Gestão Financeira: Orçamento, Parcelamento e Inadimplência",
         "Tratamentos de alto valor geram desafios de gestão financeira: orçamentos complexos com múltiplas opções de pagamento (à vista com desconto, parcelado no cartão, parcelado no próprio consultório, financiamento externo), controle de recebíveis com alertas de parcelas em atraso, e fluxo de caixa que considera o momento do recebimento versus o momento do procedimento realizado. Sistemas que automatizem o envio de boleto/link de pagamento, alertem para inadimplência, e mostrem o caixa projetado baseado no cronograma de procedimentos e pagamentos planejados, eliminam horas de controle manual por mês."),
        ("Demonstração de Valor: ROI em Agendamento e Retenção de Pacientes",
         "Para dentistas estéticos, o argumento mais forte não é a redução de no-show (que já é menor nesse nicho por causa do alto compromisso financeiro do paciente) — é a gestão eficiente do plano de tratamento e a fotodocumentação. Mostre: um plano de tratamento de reabilitação total com cronograma de consultas e controle de pagamentos, a fototeca com sequência de antes/durante/depois, e o orçamento com simulação de parcelamento. Adicione o argumento de marketing: quantos pacientes novos por mês vêm indicados por pacientes que viram o portfolio? Um sistema que facilita criar e organizar esse portfolio tem ROI indireto muito relevante."),
    ],
    [
        ("Quais sistemas sao mais usados em odontologia estetica?", "Os sistemas mais usados incluem Dental Office, iDental, Cloud Dental, Clinicorp Odonto e o Clinux. A maioria tem odontograma, prontuario e agendamento, mas diferem na qualidade da fototeca e da gestao financeira de planos de tratamento complexos. Sistemas com integracao com bancos de financiamento odontologico (como a linha Odonto da Caixa ou financeiras especializadas em saude) sao diferenciais importantes para fechamento de tratamentos de alto valor."),
        ("Como calcular o potencial de perda por gestao inadequada de plano de tratamento?", "Uma clinica de reabilitacao oral com 20 pacientes em plano de tratamento ativo, media de R$ 50.000 por plano e inadimplencia de 10% tem R$ 100.000 em risco. Um sistema que alerte para parcelas em atraso e automatize a cobranca pode recuperar 60-80% dessa inadimplencia. Alem disso, dentistas sem sistema de acompanhamento de plano de tratamento frequentemente 'esquecem' de agendar o proximo procedimento — cada procedimento nao realizado no prazo pode atrasar o tratamento em semanas e reduzir a satisfacao do paciente."),
        ("Qual e o ticket medio para SaaS de odontologia estetica?", "Para consultórios independentes de dentista estetico: R$ 200-500/mes. Para clinicas com 2-5 dentistas e alto volume de tratamentos de reabilitacao: R$ 500-1.500/mes. O mercado de odontologia estetica e premium — os pacientes pagam alto, o dentista tem receita alta, e o custo de um bom sistema de gestao é facilmente justificável. Funcionalidades como integracao com WhatsApp para confirmacao de consultas e fototeca organizada sao os maiores diferenciais de conversao nesse nicho."),
    ]
)

art(
    "consultoria-de-crescimento-e-expansao-para-empresas-de-servicos",
    "Consultoria de Crescimento e Expansão para Empresas de Serviços | ProdutoVivo",
    "Como estruturar e vender consultoria de crescimento para empresas de serviços — escalabilidade, novos mercados, modelo de franquias, digitalização e go-to-market para crescer sem perder qualidade.",
    "Consultoria de Crescimento e Expansão para Empresas de Serviços",
    "Empresas de serviços crescem de forma diferente de empresas de produto — o maior desafio é escalar sem perder qualidade. Consultores que entendem os modelos de crescimento específicos do setor de serviços têm demanda crescente.",
    [
        ("Os Gargalos de Crescimento em Empresas de Serviços",
         "Empresas de serviços têm gargalos de crescimento distintos das empresas de produto: a capacidade de entrega é limitada pelo número de pessoas qualificadas (não pela fábrica), a qualidade depende de pessoas e processos (não de máquinas calibradas), e o modelo linear ('venda mais horas') não escala. Os principais gargalos são: dependência do fundador para entrega de qualidade, dificuldade de contratar e treinar pessoas no ritmo do crescimento, e incapacidade de atender geografias distantes sem abrir filial. O consultor diagnostica qual é o gargalo principal e propõe o modelo de crescimento correto para cada caso."),
        ("Modelos de Crescimento para Serviços: Franquias, Licenciamento e Plataforma",
         "Existem três modelos principais para escalar empresas de serviços: franquias (o franqueado compra o direito de operar o modelo de negócio — adequado para serviços com alto grau de padronização como academias, escolas e clinicas), licenciamento de metodologia (a empresa vende o 'como fazer' para outros prestadores de serviço — adequado para consultorias e serviços técnicos), e plataforma (a empresa conecta ofertantes e demandantes do serviço — adequado para serviços altamente fragmentados onde nenhum prestador tem escala). O consultor avalia qual modelo é mais viável considerando a natureza do serviço e o perfil da empresa."),
        ("Padronização de Processos: A Base da Escalabilidade",
         "Antes de franquear, licenciar ou crescer por filiais, a empresa precisa ter seus processos documentados e padronizados — de forma que qualquer profissional treinado possa entregar o mesmo nível de qualidade. O trabalho de padronização inclui: mapeamento dos processos críticos de entrega (os que mais impactam a experiência do cliente), documentação em playbooks operacionais, criação de checklists e sistemas de controle de qualidade, e treinamento e certificação de equipe. Empresas que não padronizam antes de crescer descobrem que a escala amplifica problemas de qualidade ao invés de diluí-los."),
        ("Expansão Geográfica: Quando Abrir Filial vs. Parcerias",
         "Expandir geograficamente por filiais próprias requer capital, gestão remota e risco de diluição da cultura. Alternativas menos intensivas em capital incluem: parcerias com empresas locais (operação conjunta ou co-branded), representantes e agentes que vendem o serviço sem ser funcionários, e entrega remota facilitada por tecnologia (para serviços que podem ser digitalizados). A decisão de abrir filial versus partnership depende do grau de customização do serviço (quanto mais padronizado, mais fácil a filial ou franquia), da necessidade de presença física, e do capital disponível."),
        ("Crescimento por Novos Segmentos: Vertical e Adjacente",
         "Empresas de serviços crescem por duas rotas principais além da expansão geográfica: vertical (servir mais profundamente o mesmo cliente — uma consultoria de marketing que adiciona execução, ou uma clínica que adiciona especialidades complementares) e adjacente (servir um novo segmento de cliente com o mesmo serviço — uma consultoria de manufatura que começa a atender o setor de saúde). A expansão vertical tem menor risco (já tem o cliente) mas requer novos recursos. A expansão adjacente tem maior risco de go-to-market mas aumenta o mercado endereçável. O consultor avalia qual rota tem melhor risk/return para a empresa."),
    ],
    [
        ("Quanto custa uma consultoria de crescimento para empresa de servicos?", "Projetos de diagnostico de gargalos de crescimento e plano de expansao: R$ 25k-70k. Projeto de padronizacao de processos e documentacao de playbooks: R$ 40k-120k. Estruturacao de modelo de franquias (incluindo COF — Circular de Oferta de Franquia): R$ 60k-200k. Retainer de acompanhamento de crescimento (mentorias mensais e suporte de execucao): R$ 5k-15k/mes."),
        ("Franquia e sempre a melhor forma de crescer em servicos?", "Nao — franquias exigem alta padronizacao (qualidade deve ser replicavel por um terceiro), capital para estruturar a franqueadora (royalties, COF, suporte), e disposicao para um modelo de negocio muito diferente do servico em si (o franqueador vende sistema, nao servico). Empresas com servico altamente customizado (consultoria complexa, servicos de saude de alta especialidade) nao sao bons candidatos a franquia. Para esses casos, licenciamento de metodologia, modelos de partnership ou digitalização do servico para escala sao alternativas mais adequadas."),
        ("Como manter qualidade ao escalar empresa de servicos?", "Tres pilares sustentam qualidade em escala: (1) Processos padronizados — documentados em playbooks que qualquer profissional treinado pode executar; (2) Pessoas e cultura — selecao rigorosa de quem entra, treinamento intenso, e cultura de qualidade que nao aceita atalhos; (3) Mecanismos de controle — NPS do cliente em cada entrega, auditorias regulares de qualidade, e ciclo de feedback rapido para corrigir desvios. Empresas que escalam sem esses tres pilares descobrem que clientes novos recebem qualidade diferente dos clientes originais — e o boca-a-boca para de funcionar."),
    ]
)

print("Done.")
