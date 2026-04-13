# Templates de Cold Email — ProdutoVivo

> **Instrução de uso:** Enviar via Resend (ou Gmail manual) assim que DNS estiver configurado.  
> Substituir `{{NOME}}` pelo primeiro nome do prospect, `{{NICHO}}` pelo nicho deles.  
> Intervalo recomendado: Email 1 → aguardar 3 dias → Email 2 → aguardar 4 dias → Email 3.

---

## Email 1 — Abertura (Curiosidade + Problema)

**Assunto:** {{NOME}}, seu PDF está perdendo vendas

**Corpo:**

Oi {{NOME}},

Você provavelmente tem um PDF, um ebook ou um guia que já criou — e ele está parado numa pasta do Drive ou numa página de vendas com conversão fraca.

O problema não é o conteúdo. É a apresentação.

Um PDF estático não rastreia quem lê, não coleta e-mails, não engaja e não se vende sozinho.

Um app interativo faz tudo isso — e você pode criar um em 48h usando IA, sem programar, sem contratar ninguém.

Escrevi um guia com o passo a passo exato: como transformar qualquer PDF em um produto digital interativo que vende no Hotmart ou Kiwify.

Está saindo por R$37 nessa semana de lançamento.

Curioso(a)? Responde esse email com "sim" e mando o link direto.

—  
César / ProdutoVivo

---

## Email 2 — Prova social + especificidade (3 dias depois)

**Assunto:** O quiz que converte 3x mais do que landing page

**Corpo:**

Oi {{NOME}},

Você sabia que quizzes têm taxa de conversão média de 40–50% (vs. 2–5% de uma landing page típica)?

No guia ProdutoVivo eu mostro como criar um quiz de diagnóstico gratuito com IA — em menos de 2 horas — que captura e-mail antes de mostrar o resultado.

Esse é o funil que eu uso aqui: /quiz → resultado personalizado → oferta do guia.

Para infoprodutores de {{NICHO}}, isso funciona especialmente bem porque as pessoas querem saber "onde estou nessa jornada?" antes de comprar qualquer coisa.

O guia completo está em: https://produtovivo.com/#comprar

R$37 · Garantia de 7 dias · Acesso vitalício.

—  
César / ProdutoVivo

P.S. Se quiser ver o quiz antes de comprar: https://produtovivo.com/quiz

---

## Email 3 — Urgência + Objeção Final (4 dias depois)

**Assunto:** Último aviso — preço sobe em breve

**Corpo:**

Oi {{NOME}},

Essa é minha última mensagem sobre isso.

O ProdutoVivo está em R$37 só durante o lançamento. Quando o período de lançamento acabar, o preço vai para R$97.

Se você cria — ou quer criar — qualquer tipo de infoproduto digital (ebook, guia, mini-curso, quiz, chatbot), o guia te mostra como:

✓ Transformar seu PDF em app interativo  
✓ Criar quiz de diagnóstico que captura leads  
✓ Montar chatbot de suporte sem código  
✓ Publicar no Hotmart ou Kiwify do zero  
✓ Usar 50 prompts prontos de IA para criar tudo mais rápido  

Garantia incondicional de 7 dias — se não gostar, devolvo 100%.

Link: https://produtovivo.com/#comprar

Se não for o momento certo para você, sem problema — fico à disposição quando fizer sentido.

—  
César / ProdutoVivo

---

## Sequência para Leads do Quiz (automática via Resend)

> **Trigger:** Lead completa o quiz e fornece e-mail  
> **Envio:** Imediato (welcome), +24h (conteúdo), +48h (oferta)

### Welcome (imediato — já configurado em `/routes/leads.js`)

```
Assunto: Seu resultado do quiz ProdutoVivo 🎯

Oi {{NOME}}!

Seu perfil: {{PERFIL}} (Iniciante / Intermediário / Avançado)

[conteúdo personalizado por perfil — ver leads.js]

Um abraço,
César / ProdutoVivo
```

### +24h — Conteúdo de valor

```
Assunto: 3 prompts que uso todo dia para criar infoprodutos

Oi {{NOME}},

Como prometido, aqui estão 3 prompts do guia ProdutoVivo que você pode usar hoje mesmo:

**Prompt 1 — Estruturar um ebook:**
"Você é um especialista em [NICHO]. Crie o índice completo de um ebook de 7 capítulos sobre [TEMA]. Cada capítulo deve ter: título, 3 subtópicos, e um exercício prático no final."

**Prompt 2 — Criar quiz de diagnóstico:**
"Crie 5 perguntas de diagnóstico para descobrir o nível de [PÚBLICO-ALVO] em [ÁREA]. Cada pergunta deve ter 3 opções (iniciante, intermediário, avançado). No final, gere 3 perfis de resultado com recomendações específicas."

**Prompt 3 — Escrever copy de vendas:**
"Escreva uma copy de vendas para [PRODUTO] direcionada a [PÚBLICO]. Use a estrutura: problema → agitação → solução → prova → oferta → garantia → CTA. Tom: direto e empático."

O guia completo tem 50 prompts assim — organizados por etapa de criação.

Está em R$37 nessa semana: https://produtovivo.com/#comprar

—  
César
```

### +48h — Oferta direta

```
Assunto: {{NOME}}, você ainda está pensando?

Oi {{NOME}},

Percebi que você fez o quiz mas ainda não pegou o guia.

Talvez seja dúvida sobre se vai funcionar para o seu nicho ({{NICHO}} ou similar). Entendo.

Por isso a garantia é incondicional: 7 dias para testar, e se não gostar devolvo tudo, sem formulário, sem perguntas.

R$37 agora ou R$97 depois: https://produtovivo.com/#comprar

—  
César
```

---

## Notas de Personalização

| Segmento | Ajuste no Email 1 | Ajuste no Email 2 |
|----------|-------------------|-------------------|
| Educação/Cursos | "seu curso em PDF" | "alunos que buscam feedback" |
| Fitness/Saúde | "seu plano de treino/dieta" | "quiz de diagnóstico físico" |
| Finanças | "seu guia de investimento" | "quiz de perfil de investidor" |
| Marketing | "seu playbook/framework" | "quiz de maturidade digital" |
| Coaching | "seu workbook/diário" | "quiz de autoconhecimento" |
