# ProdutoVivo
## Guia Completo: Transforme seus PDFs em Apps Interativos com IA

**Versão 1.0 — Abril 2026**

---

> *Para todo infoprodutor que passou horas criando materiais que ninguém usa do jeito que merece.*

---

## Sumário

1. [Por que PDFs estáticos estão perdendo para apps](#cap1)
2. [Como a IA lê e entende seu PDF](#cap2)
3. [Criando seu primeiro chatbot de conteúdo](#cap3)
4. [Quiz inteligente gerado automaticamente](#cap4)
5. [Glossário, resumos e mapas de aprendizado](#cap5)
6. [Publicando e entregando para seus alunos](#cap6)
7. [Banco de 50 prompts prontos para usar](#cap7)

---

## Capítulo 1 — Por que PDFs estáticos estão perdendo para apps {#cap1}

### A promessa vs. a realidade

Você criou aquele ebook com carinho. Escolheu a fonte, ajustou o layout, revisou cada palavra. Depois lançou no Hotmart ou Kiwify, fez alguns stories, e as vendas vieram.

Mas o que acontece depois que o aluno baixa?

A maioria abre o PDF uma vez. Rola pelas primeiras páginas. Fecha. E nunca mais volta.

Não porque o conteúdo é ruim. Mas porque **PDFs são passivos**. Eles não respondem perguntas. Não testam o aprendizado. Não lembram onde o aluno parou. Não se adaptam ao ritmo de cada pessoa.

### O que mudou

Em 2023 e 2024, plataformas como Hotmart e Kiwify começaram a ver algo curioso: produtos com **componentes interativos** — quizzes, comunidades, lives — tinham taxas de conclusão muito maiores. Alunos que terminavam o produto compravam mais. Pediam menos reembolso. Indicavam para amigos.

Ao mesmo tempo, a IA de linguagem (ChatGPT, Claude, Gemini) chegou ao ponto em que qualquer pessoa — sem código — consegue criar experiências interativas a partir de texto existente.

Isso criou uma janela de oportunidade enorme para infoprodutores que agem rápido.

### A oportunidade concreta

Veja o que é possível hoje, sem saber programar:

| Material que você já tem | O que você pode criar com IA |
|--------------------------|------------------------------|
| Ebook em PDF | Chatbot que responde perguntas sobre o conteúdo |
| Apostila de curso | Quiz com feedback personalizado por nível |
| Guia passo a passo | App de acompanhamento com checklists inteligentes |
| Script de aula | Resumo interativo capítulo por capítulo |
| Glossário de termos | Dicionário com exemplos gerados sob demanda |

### Por que agora

A janela não vai ficar aberta para sempre. Em 12–18 meses, isso vai ser padrão. Os produtores que chegarem primeiro vão ter vantagem de preço, reputação e base de alunos.

Este guia é o seu acelerador.

---

## Capítulo 2 — Como a IA lê e entende seu PDF {#cap2}

### O que a IA realmente faz

Quando você cola o texto de um PDF numa ferramenta como o ChatGPT ou Claude, você está essencialmente dando a ela um "manual de instruções" sobre o seu conteúdo. A IA lê, processa e passa a conseguir responder perguntas, criar exercícios, resumir seções e muito mais — tudo baseado no que você forneceu.

O processo básico:

1. **Você extrai o texto** do PDF
2. **Você cola esse texto** no chat da IA (com um prompt adequado)
3. **A IA processa** e fica "especialista" no seu conteúdo
4. **Você usa prompts** para gerar o app, quiz, chatbot, etc.

### Preparando seu PDF

Antes de trabalhar com qualquer ferramenta de IA, prepare seu material:

**Passo 1: Extrair o texto**

Se seu PDF for pesquisável (não é uma imagem):
- Abra no navegador → Ctrl+A → Ctrl+C → cole num documento de texto
- Ou use [smallpdf.com](https://smallpdf.com) → "PDF para Word" → copie o texto

Se seu PDF for uma imagem escaneada:
- Use [Adobe Acrobat](https://acrobat.adobe.com) (versão gratuita) ou Google Drive (abra o PDF lá → clique direito → "Abrir com Google Docs")

**Passo 2: Limpar o texto**

Remova:
- Números de página isolados
- Cabeçalhos e rodapés repetitivos
- Texto de imagens que não foi extraído corretamente

Mantenha:
- Títulos e subtítulos (eles ajudam a IA a entender a estrutura)
- Listas e tabelas (IA lida muito bem com elas)
- Exemplos e casos práticos (são a base dos exercícios)

**Passo 3: Dividir por capítulos (para PDFs longos)**

Se seu PDF tem mais de 30 páginas, trabalhe capítulo por capítulo. A maioria das ferramentas gratuitas tem limite de tokens (texto). Uma boa regra: **nunca passe mais de 15 páginas de texto por vez**.

### Ferramentas recomendadas

| Ferramenta | Plano gratuito | Melhor para |
|------------|----------------|-------------|
| ChatGPT (gpt-4o) | 40 msgs/3h | Prompts em lote, formatação |
| Claude (claude-3-5-sonnet) | Sim (limitado) | Textos longos, instruções complexas |
| Google Gemini | Sim | Integração com Google Docs/Drive |

Para este guia, todos os prompts foram testados no **ChatGPT** e no **Claude**. Funcionam nos dois.

### Entendendo contexto e limites

A IA "esquece" a conversa anterior quando você abre um chat novo. Por isso:

- Sempre cole o texto do PDF no início de cada sessão
- Se o chat ficar longo, abra um novo e reintroduza o contexto
- Use o prompt de sistema (instruções iniciais) para fixar o comportamento — os prompts do Capítulo 7 já fazem isso

---

## Capítulo 3 — Criando seu primeiro chatbot de conteúdo {#cap3}

### O que é um chatbot de conteúdo

Um chatbot de conteúdo é uma IA configurada para responder perguntas exclusivamente sobre o seu material. Seu aluno digita uma dúvida, e o chatbot responde com base no que está no seu PDF — sem inventar, sem sair do tema.

Isso resolve um problema real: **alunos travam e abandonam o produto quando têm dúvida e não têm como perguntar**.

### Como funciona na prática

Você não vai "programar" nada. Vai usar um prompt bem construído que transforma o ChatGPT ou Claude num assistente especializado no seu conteúdo.

Existem dois formatos principais:

**Formato 1: Chat direto (mais simples)**
O aluno acessa um link para o ChatGPT ou Claude com seu prompt já carregado. Você compartilha o link.

**Formato 2: Interface customizada (intermediário)**
Você usa ferramentas como Poe, Typebot ou Botpress para empacotar o chatbot numa interface com sua marca.

Para começar, **Formato 1 já funciona e já vende**.

### Passo a passo: chatbot em 60 minutos

**Minuto 0–15: Preparar o conteúdo**

1. Extraia o texto do seu PDF (ver Capítulo 2)
2. Cole num documento de texto
3. Revise rapidamente para remover lixo de formatação

**Minuto 15–30: Construir o prompt base**

Use o Prompt C-01 do Capítulo 7. Substitua os campos indicados pelo nome do seu produto e cole o texto do PDF.

**Minuto 30–45: Testar**

Faça perguntas que seus alunos fariam. Veja se as respostas fazem sentido. Ajuste o prompt se necessário.

Testes obrigatórios:
- Pergunta que está claramente no material → deve responder corretamente
- Pergunta que NÃO está no material → deve dizer que não sabe
- Pergunta ambígua → deve pedir esclarecimento

**Minuto 45–60: Empacotar e publicar**

- Crie um "GPT customizado" no ChatGPT (requer plano Plus) — ou
- Compartilhe o prompt como um link de chat público do Claude — ou
- Instrua o aluno a copiar o prompt e colar no ChatGPT gratuito

### Entregando para o aluno

Inclua no seu produto:
1. Um arquivo `CHATBOT.txt` com o prompt pronto para colar
2. Instruções simples de uso (1 página)
3. Link para o ChatGPT ou Claude gratuito

Isso já diferencia seu produto de 90% dos concorrentes.

---

## Capítulo 4 — Quiz inteligente gerado automaticamente {#cap4}

### Por que quizzes vendem mais

Produtos com quizzes têm duas vantagens comerciais diretas:

1. **Engajamento maior**: alunos que fazem quiz passam mais tempo no produto e chegam mais longe
2. **Prova social automática**: "Fiz o quiz e acertei 8/10" é um argumento de venda que seus alunos compartilham espontaneamente

### Tipos de quiz que a IA gera

**Quiz de verificação (mais comum)**
Testa o que o aluno aprendeu. Vem com gabarito e explicação de cada resposta.

**Quiz diagnóstico**
Coloca antes do conteúdo. Avalia o nível do aluno e sugere por onde começar.

**Quiz de revisão**
Foca nos pontos mais difíceis do material. Ótimo para módulos densos.

### Passo a passo: quiz em 30 minutos

**Passo 1:** Escolha um capítulo ou módulo específico (não o PDF inteiro)
**Passo 2:** Extraia o texto desse capítulo
**Passo 3:** Use o Prompt Q-01 ou Q-02 do Capítulo 7
**Passo 4:** Revise as questões geradas — ajuste qualquer uma que pareça estranha
**Passo 5:** Formate e exporte (Word, PDF, ou use diretamente no chat)

### Ajustando dificuldade

Os prompts do Capítulo 7 permitem ajustar o nível:

- `nivel: iniciante` → questões conceituais simples
- `nivel: intermediário` → questões que exigem aplicação
- `nivel: avançado` → questões de análise e síntese

### Ferramentas para quiz interativo

Se quiser ir além do PDF estático:

| Ferramenta | Gratuita? | O que faz |
|------------|-----------|-----------|
| Google Forms | Sim | Quiz com correção automática |
| Quizlet | Sim (limitado) | Flashcards e quiz gamificado |
| Typeform | Sim (limitado) | Quiz com visual bonito |
| Kahoot | Sim | Quiz ao vivo (ótimo para lives) |

Para a maioria dos infoprodutores, **Google Forms já é suficiente** para começar.

---

## Capítulo 5 — Glossário, resumos e mapas de aprendizado {#cap5}

### Glossário interativo

Um glossário gerado por IA não é só uma lista de definições. É um documento vivo onde cada termo vem com:
- Definição em linguagem simples
- Exemplo prático do seu nicho
- Como o termo se conecta a outros conceitos do material

Use o Prompt G-01 do Capítulo 7.

**Dica de entrega**: entregue o glossário como um segundo PDF bônus. Isso aumenta o valor percebido do produto sem custo extra.

### Resumos por capítulo

Resumos gerados por IA servem dois propósitos:

1. **Para o aluno que está aprendendo**: revisão rápida antes de avançar
2. **Para o aluno que voltou depois de um tempo**: retomada sem precisar reler tudo

O formato ideal é um resumo em bullets com os **3–5 pontos mais importantes** de cada capítulo, mais uma "pergunta de fixação" ao final.

Use o Prompt R-01 ou R-02 do Capítulo 7.

### Mapas de aprendizado

Um mapa de aprendizado é uma trilha visual que mostra:
- Onde o aluno está no material
- O que já foi coberto
- O que vem a seguir
- Pré-requisitos entre tópicos

Com IA, você pode gerar a estrutura do mapa em texto (formato de lista hierárquica) e depois transformar visualmente usando [Miro](https://miro.com), [Whimsical](https://whimsical.com) ou [FigJam](https://www.figma.com/figjam) — todos com planos gratuitos.

Use o Prompt M-01 do Capítulo 7.

---

## Capítulo 6 — Publicando e entregando para seus alunos {#cap6}

### Opções de entrega

Você tem três caminhos principais, dependendo do seu nível técnico e do tipo de produto:

**Opção A: Tudo em PDF (mais simples)**

Entregue o chatbot como um arquivo de texto com o prompt, o quiz como PDF ou Google Form, e o glossário como um segundo PDF. Sem tecnologia extra.

- Prós: Funciona agora, zero custo adicional
- Contras: Experiência menos fluida, aluno precisa seguir instruções

**Opção B: Área de membros (intermediário)**

Use plataformas como **Hotmart Club**, **Kiwify** ou **Teachable** para entregar os materiais com uma interface organizada. Embed o quiz via Google Forms.

- Prós: Experiência profissional, controle de acesso automático
- Contras: Custo mensal da plataforma

**Opção C: Link de chatbot (mais interativo)**

Use o **Poe** ou **Typebot** para criar um chatbot acessível por link, sem precisar que o aluno instale nada.

- Prós: Experiência mais próxima de um "app de verdade"
- Contras: Requer configuração inicial de ~2–3h

### Integrando com Hotmart e Kiwify

**No Hotmart:**
1. Acesse Produtor → Produtos → Área de Membros
2. Crie uma nova aula ou módulo bônus
3. Adicione o link do chatbot como "URL externa" ou faça upload dos PDFs
4. Configure o acesso automático pós-compra

**No Kiwify:**
1. Acesse Produtos → Conteúdo do Produto
2. Adicione módulo "Ferramentas IA" como bônus
3. Insira o link do chatbot ou faça upload dos arquivos

### Comunicando o valor para o aluno

No e-mail de entrega, adicione um parágrafo como:

> *"Você agora tem acesso a algo que poucos produtos do mercado oferecem: um assistente de IA treinado especificamente no conteúdo deste guia. É como ter um tutor disponível 24 horas. Veja como usar: [link com instruções]."*

Isso aumenta a percepção de valor imediatamente.

### Usando como argumento de venda

No copy do produto, na página de vendas, e nos anúncios:

- ✅ "Vem com chatbot de IA incluído"
- ✅ "Quiz com feedback personalizado"
- ✅ "Glossário interativo gerado por IA"

Esses diferenciais justificam preço igual ou superior a produtos mais extensos — sem componentes interativos.

---

## Capítulo 7 — Banco de 50 Prompts Prontos para Usar {#cap7}

> **Como usar:** Copie o prompt, substitua os campos entre `[colchetes]` pelas informações do seu produto, cole o texto do seu PDF onde indicado, e envie ao ChatGPT ou Claude.

---

### SÉRIE C — Chatbot de Conteúdo (Prompts C-01 a C-10)

---

**C-01 — Chatbot especialista no seu conteúdo (base)**

```
Você é um assistente especializado no conteúdo de "[NOME DO SEU PRODUTO]", 
criado por [SEU NOME]. Seu único papel é responder perguntas baseadas 
no material abaixo. Se a resposta não estiver no material, diga exatamente:
"Essa informação não está coberta neste guia. Recomendo buscar [RECURSO ALTERNATIVO]."

Sempre responda em português do Brasil, de forma clara e objetiva.
Quando relevante, cite de qual parte do material a informação vem.

MATERIAL DE REFERÊNCIA:
[COLE O TEXTO DO SEU PDF AQUI]

---
Pronto. Pode fazer sua primeira pergunta.
```

---

**C-02 — Chatbot com persona e tom de voz**

```
Você é [NOME DA PERSONA], assistente de [SEU NOME] e especialista em 
[TEMA DO SEU PRODUTO]. Seu tom é [FORMAL/INFORMAL/MOTIVADOR/DIDÁTICO].

Você responde APENAS com base no conteúdo abaixo. Nunca invente 
informações. Se não souber, diga: "Boa pergunta! Esse tópico específico 
não está coberto no guia, mas você pode explorar [SUGESTÃO]."

Use exemplos práticos sempre que possível. Limite suas respostas a 
3–5 parágrafos, a menos que o aluno peça mais detalhes.

CONTEÚDO DO GUIA:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**C-03 — Chatbot com perguntas de acompanhamento automático**

```
Você é um tutor de [TEMA] baseado em "[NOME DO PRODUTO]". 

Ao responder cada pergunta do aluno:
1. Dê a resposta direta (2–3 parágrafos)
2. Adicione um exemplo prático do nicho [NICHO DO ALUNO]
3. Finalize SEMPRE com uma pergunta de acompanhamento como: 
   "Isso faz sentido? Quer que eu aprofunde algum ponto?"

Conteúdo de referência:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**C-04 — Chatbot com modo de revisão rápida**

```
Você é um assistente de revisão para "[NOME DO PRODUTO]".

Quando o aluno disser "revisão rápida de [CAPÍTULO/TÓPICO]", 
você responde com:
- 3 pontos principais em bullets
- 1 conceito que costuma ser confundido
- 1 pergunta de fixação (com gabarito ao final)

Para perguntas normais, responda baseado apenas no material abaixo.

Material:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**C-05 — Chatbot com níveis de profundidade**

```
Você é um especialista em [TEMA] baseado em "[NOME DO PRODUTO]".

O aluno pode solicitar respostas em 3 níveis:
- "resumido" → 3–5 linhas, conceito central apenas
- "padrão" → 2–3 parágrafos com exemplo
- "detalhado" → explicação completa com contexto, exemplo e aplicação prática

Se o aluno não especificar, use o nível "padrão".

Responda apenas com base no conteúdo abaixo:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**C-06 — Chatbot para onboarding de novos alunos**

```
Você é o assistente de boas-vindas de "[NOME DO PRODUTO]".

Quando o aluno digitar "começar" ou "como usar", apresente:
1. Uma saudação personalizada com o nome do produto
2. Um resumo de 3 linhas do que o aluno vai aprender
3. A sequência recomendada de estudo
4. Como usar este chatbot da melhor forma

Para dúvidas sobre o conteúdo, responda apenas com base no material:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**C-07 — Chatbot com exemplos do nicho do aluno**

```
Você é um consultor de [TEMA] especializado em [NICHO ESPECÍFICO].

Ao responder qualquer pergunta, sempre conecte a resposta ao contexto 
de [NICHO ESPECÍFICO]. Use exemplos práticos e reais desse mercado.

Se o aluno disser qual é o produto ou negócio dele, personalize 
ainda mais as respostas.

Base de conhecimento:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**C-08 — Chatbot com modo de dúvidas frequentes**

```
Você é o suporte de "[NOME DO PRODUTO]".

Primeiro, leia o material abaixo. Depois, quando o aluno perguntar,
verifique se a dúvida é uma das mais comuns:

DÚVIDAS FREQUENTES (responda direto sem buscar no material):
[LISTE 5–10 DÚVIDAS COMUNS COM RESPOSTAS CURTAS]

Para outras dúvidas, busque a resposta no material:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**C-09 — Chatbot de troubleshooting (para cursos técnicos)**

```
Você é um especialista em resolver problemas relacionados a [TEMA TÉCNICO].

Quando o aluno descrever um problema:
1. Faça 1–2 perguntas de diagnóstico
2. Identifique a causa mais provável
3. Dê um passo a passo de solução baseado no material
4. Se o problema não estiver coberto, indique: "Esse caso específico 
   está fora do escopo deste guia. Recomendo [RECURSO]."

Material de referência:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**C-10 — Chatbot multilíngue (para produtos internacionais)**

```
You are an AI assistant specialized in "[NOME DO PRODUTO]".

Detect the language of each message and respond in the same language.
Base all your answers ONLY on the content below.
If you don't know, say so clearly.

If asked in Portuguese: "Sou especialista em [NOME DO PRODUTO]. 
Como posso te ajudar?"
If asked in English: "I'm specialized in [NOME DO PRODUTO]. 
How can I help you?"
If asked in Spanish: "Soy especialista en [NOMBRE DEL PRODUCTO]. 
¿En qué puedo ayudarte?"

Content:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

### SÉRIE Q — Quiz e Avaliação (Prompts Q-01 a Q-10)

---

**Q-01 — Quiz básico de verificação (5 questões)**

```
Com base no texto abaixo, crie um quiz de verificação com 5 questões 
de múltipla escolha (4 alternativas cada) sobre os principais conceitos.

Formato de cada questão:
**Questão [N]:** [enunciado]
a) [opção]
b) [opção]
c) [opção]
d) [opção]
✅ Resposta correta: [letra] — [breve explicação de 1–2 linhas]

Nível de dificuldade: intermediário.

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**Q-02 — Quiz adaptado por nível**

```
Com base no texto abaixo, crie 3 versões de um quiz com 5 questões cada:

VERSÃO INICIANTE: conceitos básicos, vocabulário, definições
VERSÃO INTERMEDIÁRIO: aplicação de conceitos, exemplos práticos
VERSÃO AVANÇADO: análise crítica, casos complexos, síntese

Para cada questão, indique a resposta correta e uma explicação de 
1 linha.

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**Q-03 — Quiz diagnóstico (para ser usado ANTES do conteúdo)**

```
Com base no texto abaixo, crie um quiz diagnóstico de 8 questões 
que avalie o conhecimento PRÉVIO do aluno sobre o tema.

As questões devem cobrir os conceitos fundamentais do material, mas 
sem pressupor que o aluno já leu o conteúdo.

Ao final, adicione uma tabela de interpretação:
- 0–3 acertos: "Você está no ponto certo para este guia. Comece do Capítulo 1."
- 4–6 acertos: "Bom conhecimento base. Você pode pular direto para o Capítulo [X]."
- 7–8 acertos: "Você já domina o básico. Foque nos Capítulos [Y] e [Z]."

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**Q-04 — Quiz de verdadeiro ou falso com justificativa**

```
Com base no texto abaixo, crie 10 afirmações para um quiz de 
Verdadeiro ou Falso.

Misture: 5 afirmações verdadeiras e 5 falsas. Para cada uma, 
forneça a resposta correta e uma justificativa de 1–2 linhas.

Organize em ordem crescente de dificuldade.

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**Q-05 — Quiz de lacunas (fill in the blank)**

```
Com base no texto abaixo, crie 10 frases com uma palavra ou 
expressão-chave removida (substituída por ___).

Para cada frase:
- Indique a resposta correta
- Adicione 2 distratores plausíveis (respostas erradas que parecem certas)

Organize do mais fácil para o mais difícil.

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**Q-06 — Questões abertas para reflexão**

```
Com base no texto abaixo, crie 5 perguntas abertas de reflexão — 
perguntas que não têm uma única resposta certa, mas estimulam o 
aluno a pensar na aplicação prática no contexto dele.

Para cada pergunta, adicione:
- Um "ponto de partida" para a reflexão (1 linha)
- Um exemplo de como alguém poderia responder

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**Q-07 — Quiz de correspondência (matching)**

```
Com base no texto abaixo, crie um exercício de correspondência 
com 8 pares (conceito ↔ definição ou conceito ↔ exemplo).

Apresente:
- Coluna A: os conceitos em ordem aleatória
- Coluna B: as definições em ordem diferente
- Gabarito ao final

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**Q-08 — Quiz de ordenação de etapas**

```
Com base no texto abaixo, identifique 3 processos ou sequências 
descritos no material. Para cada um, crie um exercício onde o 
aluno precisa ordenar as etapas na ordem correta.

Apresente as etapas em ordem embaralhada para o exercício.
Forneça a ordem correta no gabarito.

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**Q-09 — Questões para Google Forms (formato exportável)**

```
Com base no texto abaixo, crie 10 questões de múltipla escolha 
prontas para serem copiadas no Google Forms.

Formato:
Pergunta: [enunciado]
Opção A: [texto]
Opção B: [texto]
Opção C: [texto]
Opção D: [texto]
Resposta correta: [letra]
Feedback (correto): [texto curto]
Feedback (incorreto): [texto curto]

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**Q-10 — Quiz final de certificação**

```
Com base no texto abaixo, crie um quiz de certificação com 
15 questões cobrindo todo o material.

Regras:
- Inclua questões de todos os níveis (iniciante, intermediário, avançado)
- Mínimo para aprovação: 10/15 (66%)
- Adicione uma mensagem de aprovação e reprovação ao final
- Mostre a distribuição: 5 questões básicas, 6 intermediárias, 4 avançadas

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

### SÉRIE G — Glossário (Prompts G-01 a G-05)

---

**G-01 — Glossário completo do material**

```
Com base no texto abaixo, crie um glossário com os 20 termos 
mais importantes do material.

Para cada termo:
**[TERMO]**
- *Definição simples:* [explicação em 1–2 linhas, sem jargão]
- *Exemplo prático:* [como esse termo aparece na vida real do aluno]
- *Relacionado a:* [outros termos do glossário que se conectam]

Organize em ordem alfabética.

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**G-02 — Glossário para iniciantes (linguagem simplificada)**

```
Com base no texto abaixo, crie um glossário de 15 termos-chave 
escrito especificamente para quem está começando no tema.

Regras:
- Use apenas palavras simples nas definições (escreva como se 
  explicasse para um amigo sem conhecimento técnico)
- Inclua uma analogia do dia a dia para cada termo
- Adicione um emoji temático no início de cada entrada

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**G-03 — Glossário bilíngue (PT-BR / EN)**

```
Com base no texto abaixo, identifique os 15 termos técnicos 
mais usados no material e crie um glossário bilíngue.

Para cada termo:
| Português | English | Definição |
|-----------|---------|-----------|
| [termo PT] | [term EN] | [definição simples] |

Após a tabela, adicione uma seção "Como usar em contexto" com 
3 exemplos de frases usando os termos.

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**G-04 — Glossário com mapa de conexões**

```
Com base no texto abaixo, identifique os 10 conceitos centrais 
do material e crie um "mapa de conexões" textual.

Para cada conceito:
**[CONCEITO]**
→ Depende de: [conceitos que precisam ser entendidos antes]
→ Leva a: [conceitos que derivam deste]
→ Confundido com: [conceito similar mas diferente]
→ Em uma linha: [definição ultra-resumida]

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**G-05 — Mini-dicionário com exemplos do nicho**

```
Com base no texto abaixo, crie um mini-dicionário com 12 termos 
adaptado especificamente para o contexto de [NICHO ESPECÍFICO].

Para cada termo, os exemplos devem ser tirados EXCLUSIVAMENTE 
do universo de [NICHO ESPECÍFICO]. Nada genérico.

Formato:
**[TERMO]:** [definição] | Exemplo em [NICHO]: [exemplo específico]

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

### SÉRIE R — Resumos (Prompts R-01 a R-08)

---

**R-01 — Resumo executivo por capítulo**

```
Com base no texto abaixo, crie um resumo executivo para cada 
seção ou capítulo identificado no material.

Para cada seção:
## [Título da Seção]
**Em uma frase:** [a ideia central em 1 linha]
**Pontos-chave:**
- [ponto 1]
- [ponto 2]
- [ponto 3]
**Para que serve:** [aplicação prática do que foi aprendido]

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**R-02 — Resumo em formato de "cheat sheet"**

```
Com base no texto abaixo, crie uma "cheat sheet" (folha de 
consulta rápida) do material completo.

Formato:
- Use bullets curtos e diretos
- Máximo de 3–5 palavras por bullet quando possível
- Organize por tópicos com títulos em negrito
- Adicione emojis para facilitar a leitura rápida
- O objetivo é: alguém pode revisar tudo em 5 minutos

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**R-03 — Resumo narrativo (para quem prefere texto corrido)**

```
Com base no texto abaixo, crie um resumo em prosa com linguagem 
acessível — como se fosse um artigo de blog.

Extensão: 400–600 palavras.
Tom: conversacional, empolgante, direto ao ponto.
Inclua: os conceitos mais importantes + 2–3 exemplos práticos.
Finalize com: as 3 principais conclusões práticas.

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**R-04 — Resumo com perguntas de fixação**

```
Com base no texto abaixo, crie um resumo estruturado onde 
cada seção termina com uma "Pergunta de Fixação".

Formato:
**[Título da Seção]**
[resumo em 3–5 bullets]
🤔 **Pergunta de fixação:** [pergunta que faz o aluno pensar]
💡 *Resposta:* [resposta em 1–2 linhas, no mesmo bloco]

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**R-05 — Resumo de antes e depois**

```
Com base no texto abaixo, crie um resumo no formato "antes e depois" 
que mostre a transformação que o aluno vai passar ao aplicar o conteúdo.

Formato:
**[Tópico]**
❌ Antes: [como o aluno pensa ou faz antes do conteúdo]
✅ Depois: [como passa a pensar ou fazer após aprender]

Crie pelo menos 8 pares de antes/depois baseados no material.

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**R-06 — Resumo em formato de storytelling**

```
Com base no texto abaixo, reescreva o conteúdo como uma narrativa 
com um personagem fictício que passa pelo processo descrito no material.

O personagem deve:
- Ter um perfil do público-alvo do produto ([PERFIL DO ALUNO])
- Enfrentar os problemas abordados no início do material
- Aplicar as soluções descritas passo a passo
- Chegar ao resultado final descrito no material

Extensão: 500–800 palavras. Tom: inspirador e realista.

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**R-07 — Resumo para revisão em 2 minutos**

```
Com base no texto abaixo, crie um resumo de revisão rápida 
que pode ser lido em exatamente 2 minutos (aproximadamente 300 palavras).

Regras:
- Capture apenas os 5 conceitos mais importantes
- Use linguagem extremamente direta
- Sem introdução ou conclusão — vá direto ao ponto
- Adicione: "Aplique hoje: [uma ação concreta que o aluno pode fazer agora]"

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**R-08 — Resumo comparativo (conceitos vs. concepções erradas)**

```
Com base no texto abaixo, crie um resumo que compare os 
conceitos corretos do material com as concepções erradas comuns.

Formato:
| ❌ Mito / Concepção errada | ✅ O que o material diz |
|---------------------------|------------------------|
| [equívoco comum] | [o que é correto segundo o PDF] |

Crie pelo menos 8 linhas na tabela.
Após a tabela, adicione: "Por que essa distinção importa: [1 parágrafo]"

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

### SÉRIE M — Mapa de Aprendizado (Prompts M-01 a M-05)

---

**M-01 — Mapa de tópicos hierárquico**

```
Com base no texto abaixo, crie um mapa de aprendizado hierárquico 
em formato de lista aninhada, mostrando a estrutura completa do conteúdo.

Formato:
📚 [NOME DO PRODUTO]
├── 📖 [Módulo/Capítulo 1]
│   ├── [Subtópico 1.1]
│   ├── [Subtópico 1.2]
│   └── [Subtópico 1.3]
├── 📖 [Módulo/Capítulo 2]
│   └── ...
└── ...

Após o mapa, adicione uma legenda indicando:
⭐ = conceito central (marque os 3–5 mais importantes)
🔗 = depende de outro tópico (indique qual)

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**M-02 — Trilha de aprendizado sequencial**

```
Com base no texto abaixo, crie uma trilha de aprendizado em 
formato de jornada, indicando a sequência ideal de estudo.

Para cada etapa da trilha:
**Etapa [N]: [Nome]**
- O que você vai aprender: [lista de tópicos]
- Pré-requisito: [o que precisa saber antes, se houver]
- Resultado esperado: [o que o aluno consegue fazer ao completar]
- Tempo estimado: [em minutos de leitura/prática]

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**M-03 — Mapa de dependências entre conceitos**

```
Com base no texto abaixo, identifique as dependências entre 
os principais conceitos — o que precisa ser entendido antes de 
avançar para o próximo tópico.

Apresente como um diagrama textual:
[Conceito A] → [Conceito B] → [Conceito C]
                     ↓
              [Conceito D] → [Conceito E]

Adicione uma nota para cada seta explicando por que a dependência existe.

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**M-04 — Roteiro de estudo personalizado por perfil**

```
Com base no texto abaixo, crie 3 roteiros de estudo diferentes 
para 3 perfis de aluno:

PERFIL 1: [DESCREVA O PERFIL — ex: "iniciante com pouco tempo"]
Roteiro: quais seções priorizar, o que pode pular, sequência ideal

PERFIL 2: [DESCREVA O PERFIL — ex: "intermediário que quer acelerar"]
Roteiro: ...

PERFIL 3: [DESCREVA O PERFIL — ex: "avançado buscando lacunas específicas"]
Roteiro: ...

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**M-05 — Checklist de progresso**

```
Com base no texto abaixo, crie um checklist de progresso que 
o aluno pode usar para acompanhar o próprio aprendizado.

Formato:
## Checklist de Progresso — [NOME DO PRODUTO]

### Módulo 1: [Título]
- [ ] Entendo o conceito de [conceito 1]
- [ ] Consigo explicar [conceito 2] com minhas próprias palavras
- [ ] Apliquei [exercício/ação] na prática
- [ ] Passei no quiz do módulo 1

### Módulo 2: [Título]
...

Ao final: "Quando marcar todos os itens, você está pronto para [resultado final do produto]."

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

### SÉRIE E — Exercícios Práticos (Prompts E-01 a E-07)

---

**E-01 — Exercícios de aplicação imediata**

```
Com base no texto abaixo, crie 5 exercícios práticos que o 
aluno pode fazer HOJE para aplicar o que aprendeu.

Para cada exercício:
**Exercício [N]: [Título]**
⏱️ Tempo: [estimativa]
🎯 Objetivo: [o que vai praticar]
📋 O que fazer: [instruções em 3–5 passos]
✅ Como saber se acertou: [critério de sucesso]

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**E-02 — Exercícios baseados em cenários reais**

```
Com base no texto abaixo, crie 4 cenários práticos (mini-casos) 
baseados em situações reais que o aluno de [NICHO] enfrenta.

Para cada cenário:
**Cenário [N]: [Título]**
*Situação:* [descrição do contexto em 3–4 linhas]
*Desafio:* [o que o aluno precisa resolver]
*Aplique o conteúdo:* [qual parte do PDF usar]
*Solução sugerida:* [resposta com base no material]

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**E-03 — Desafio semanal de implementação**

```
Com base no texto abaixo, crie um plano de desafios para 4 semanas 
onde o aluno implementa o conteúdo na prática, uma etapa por vez.

Para cada semana:
**Semana [N]: [Tema]**
- Segunda: [mini-tarefa — 15 min]
- Quarta: [mini-tarefa — 15 min]
- Sexta: [mini-tarefa — 30 min]
- Domingo: [reflexão — 10 min] — "O que funcionou? O que ajustar?"

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**E-04 — Exercício de análise crítica**

```
Com base no texto abaixo, crie 3 exercícios de análise crítica 
onde o aluno precisa avaliar exemplos (bons e ruins) e justificar 
sua avaliação usando os critérios do material.

Para cada exercício:
- Apresente um exemplo concreto (real ou fictício)
- Peça que o aluno avalie: "Esse exemplo segue as diretrizes do guia?"
- Apresente a análise correta ao final
- Explique por que o exemplo é bom ou por que falha

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**E-05 — Projeto prático final**

```
Com base no texto abaixo, crie um "projeto prático final" que 
integra todos os conceitos do material.

O projeto deve:
- Ter um contexto realista do [NICHO DO ALUNO]
- Ser dividido em 4–6 etapas sequenciais
- Incluir critérios de avaliação claros para cada etapa
- Terminar com um entregável concreto que o aluno pode usar imediatamente
- Estimar o tempo total: [X horas]

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**E-06 — Role play para prática de habilidades**

```
Com base no texto abaixo, crie um exercício de role play onde 
o aluno pratica aplicar o conteúdo numa situação simulada.

Formato:
**Contexto do Role Play:**
[Descrição do cenário — quem é o aluno, quem é o "interlocutor"]

**Papel do aluno:** [o que o aluno deve fazer/dizer]
**Papel da IA (você):** [como a IA vai responder/reagir]
**Critérios de sucesso:** [o que constitui uma boa performance]
**Dicas baseadas no material:** [3 pontos-chave para lembrar]

Inicie o role play agora. Eu faço o papel de [PERSONAGEM].

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

**E-07 — Exercício de ensinar para aprender**

```
Com base no texto abaixo, crie um exercício do tipo "ensine para aprender":

Instrua o aluno a explicar os principais conceitos do material 
como se estivesse ensinando para [PERSONA — ex: "um amigo que não 
conhece nada sobre o tema"].

Forneça:
1. 5 conceitos para o aluno explicar (em ordem de dificuldade)
2. Uma rubrica de avaliação para cada explicação
3. Exemplos de como uma boa explicação se parece vs. uma fraca

Texto:
[COLE O TEXTO DO SEU PDF AQUI]
```

---

## Próximos Passos

Você tem agora:
- **7 capítulos** de conteúdo estratégico
- **50 prompts prontos** organizados em 6 séries (C, Q, G, R, M, E)
- Exemplos práticos para cada formato de app interativo

**Comece por aqui:**

1. Escolha o seu PDF mais vendido (ou o que tem mais potencial)
2. Extraia o texto (Capítulo 2 te mostra como)
3. Use o Prompt C-01 para criar o primeiro chatbot
4. Teste com 3–5 perguntas que seus alunos realmente fazem
5. Entregue como bônus no seu produto ainda essa semana

---

*ProdutoVivo — produtovivo.com*  
*Suporte: contato@produtovivo.com*

---

**Versão 1.0 | Abril 2026**  
*Todos os direitos reservados. Este guia é para uso pessoal do comprador.*
