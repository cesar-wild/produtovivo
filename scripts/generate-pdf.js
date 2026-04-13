#!/usr/bin/env node
/**
 * generate-pdf.js
 * Gera o guia ProdutoVivo em PDF a partir do markdown.
 * Uso: node scripts/generate-pdf.js
 * Saída: product/guia-produtovivo-v1.pdf
 */

'use strict';

const fs = require('fs');
const path = require('path');
const PDFDocument = require('pdfkit');

const INPUT  = path.join(__dirname, '..', 'product', 'guia-produtovivo.md');
const OUTPUT = path.join(__dirname, '..', 'product', 'guia-produtovivo-v1.pdf');

// ─── Colours ────────────────────────────────────────────────────────────────
const BRAND   = '#FF6B35';   // ProdutoVivo orange
const DARK    = '#1A1A2E';   // near-black
const MID     = '#4A4A6A';   // body text
const LIGHT   = '#F5F5F5';   // background blocks
const CODE_BG = '#F0F0F0';

// ─── Layout ─────────────────────────────────────────────────────────────────
const MARGIN  = 60;
const W       = 595.28;           // A4 width  (pt)
const H       = 841.89;           // A4 height (pt)
const CONTENT = W - MARGIN * 2;  // usable width

function newDoc () {
  const doc = new PDFDocument({
    size: 'A4',
    margins: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN },
    info: {
      Title:    'ProdutoVivo — Guia Completo',
      Author:   'ProdutoVivo',
      Subject:  'Transforme seus PDFs em Apps Interativos com IA',
      Keywords: 'infoproduto, IA, PDF, app, chatbot, quiz',
      Creator:  'ProdutoVivo v1.0',
    },
    bufferPages: true,
  });
  return doc;
}

// ─── Helpers ────────────────────────────────────────────────────────────────
function safeY (doc, needed = 20) {
  if (doc.y + needed > H - MARGIN) doc.addPage();
}

function hrule (doc, color = '#DDDDDD') {
  safeY(doc, 10);
  doc.moveTo(MARGIN, doc.y)
     .lineTo(W - MARGIN, doc.y)
     .strokeColor(color)
     .lineWidth(0.5)
     .stroke()
     .moveDown(0.5);
}

// Draw page numbers in bufferPages mode
function addPageNumbers (doc) {
  const range = doc.bufferedPageRange();
  for (let i = range.start; i < range.start + range.count; i++) {
    doc.switchToPage(i);
    doc.fontSize(8).fillColor('#999999')
       .text(
         `produtovivo.com  ·  ${i + 1} / ${range.count}`,
         MARGIN,
         H - MARGIN / 2,
         { width: CONTENT, align: 'center' }
       );
  }
}

// ─── Cover page ─────────────────────────────────────────────────────────────
function renderCover (doc) {
  // Background stripe
  doc.rect(0, 0, W, H).fill('#FAFAFA');
  doc.rect(0, 0, W, 300).fill(DARK);

  // Logo / wordmark
  doc.fontSize(11).fillColor('#FFFFFF').opacity(0.5)
     .text('PRODUTOVIVO', MARGIN, 60, { letterSpacing: 4 });

  // Headline
  doc.opacity(1).fontSize(32).fillColor('#FFFFFF').font('Helvetica-Bold')
     .text('Transforme seus PDFs em', MARGIN, 100, { width: CONTENT });
  doc.fillColor(BRAND).text('Apps Interativos com IA', { width: CONTENT });

  // Subtitle
  doc.fontSize(13).fillColor('#CCCCCC').font('Helvetica')
     .text(
       'Guia completo com 50 prompts prontos para criadores brasileiros',
       MARGIN, 200, { width: CONTENT }
     );

  // Version badge
  doc.roundedRect(MARGIN, 250, 130, 28, 4).fill(BRAND);
  doc.fontSize(10).fillColor('#FFFFFF').font('Helvetica-Bold')
     .text('Versão 1.0 · Abril 2026', MARGIN + 10, 258, { width: 120, align: 'center' });

  // Body section
  const bodyY = 330;
  doc.fontSize(12).fillColor(MID).font('Helvetica')
     .text('O que você vai dominar:', MARGIN, bodyY);

  const bullets = [
    'Converter qualquer PDF em chatbot especializado sem código',
    'Gerar quizzes com feedback personalizado por nível',
    'Criar glossários, resumos e mapas de aprendizado com IA',
    'Publicar e vender em Hotmart ou Kiwify como profissional',
    '50 prompts testados — copie, personalize, use agora',
  ];
  let by = bodyY + 24;
  bullets.forEach(b => {
    doc.circle(MARGIN + 6, by + 5, 3).fill(BRAND);
    doc.fillColor(DARK).font('Helvetica').fontSize(11)
       .text(b, MARGIN + 18, by, { width: CONTENT - 20 });
    by += 22;
  });

  // Guarantee box
  doc.roundedRect(MARGIN, by + 20, CONTENT, 54, 6)
     .fillAndStroke('#FFF8F5', BRAND);
  doc.fontSize(11).fillColor(DARK).font('Helvetica-Bold')
     .text('Garantia de 7 dias', MARGIN + 16, by + 28);
  doc.font('Helvetica').fillColor(MID).fontSize(10)
     .text(
       'Leu o guia e não agregou valor? Pedimos reembolso sem perguntas.',
       MARGIN + 16, by + 42, { width: CONTENT - 32 }
     );

  // Footer
  doc.fontSize(9).fillColor('#999999')
     .text('suporte@produtovivo.com  ·  produtovivo.com', MARGIN, H - 60,
           { width: CONTENT, align: 'center' });

  doc.addPage();
}

// ─── Table of contents ───────────────────────────────────────────────────────
function renderTOC (doc, chapters) {
  doc.fontSize(22).fillColor(DARK).font('Helvetica-Bold')
     .text('Sumário', MARGIN, doc.y);
  doc.moveDown(0.4);
  hrule(doc, BRAND);
  doc.moveDown(0.8);

  chapters.forEach((ch, i) => {
    safeY(doc, 22);
    doc.fontSize(11).fillColor(MID).font('Helvetica')
       .text(`${i + 1}.`, MARGIN, doc.y, { continued: true, width: 20 })
       .fillColor(DARK).font('Helvetica-Bold')
       .text(` ${ch.title}`, { width: CONTENT - 20 });
    doc.moveDown(0.25);
  });

  doc.addPage();
}

// ─── Parse markdown ──────────────────────────────────────────────────────────
function parseMarkdown (md) {
  const lines = md.split('\n');
  const tokens = [];

  let inCode = false;
  let codeLines = [];

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // Code block toggle
    if (line.startsWith('```')) {
      if (inCode) {
        tokens.push({ type: 'code', text: codeLines.join('\n') });
        codeLines = [];
        inCode = false;
      } else {
        inCode = true;
      }
      continue;
    }
    if (inCode) { codeLines.push(line); continue; }

    // Horizontal rule
    if (/^-{3,}$/.test(line.trim())) { tokens.push({ type: 'hr' }); continue; }

    // H1
    if (line.startsWith('# ')) {
      tokens.push({ type: 'h1', text: line.slice(2).trim() });
      continue;
    }
    // H2 (chapters)
    if (line.startsWith('## ')) {
      const raw = line.slice(3).trim();
      // strip inline anchors like {#cap1}
      const text = raw.replace(/\s*\{#[^}]+\}/, '').trim();
      tokens.push({ type: 'h2', text });
      continue;
    }
    // H3
    if (line.startsWith('### ')) {
      tokens.push({ type: 'h3', text: line.slice(4).trim() });
      continue;
    }
    // H4 (bold prompt title)
    if (line.startsWith('#### ') || /^\*\*[A-Z]-\d+/.test(line)) {
      const text = line.replace(/^\*\*/, '').replace(/\*\*$/, '')
                       .replace(/^#+\s*/, '').trim();
      tokens.push({ type: 'h4', text });
      continue;
    }

    // Table row
    if (line.startsWith('|')) {
      tokens.push({ type: 'tableRow', text: line });
      continue;
    }

    // Blockquote
    if (line.startsWith('> ')) {
      tokens.push({ type: 'quote', text: line.slice(2).trim() });
      continue;
    }

    // Bullet / numbered list
    if (/^(\s*)[-*+]\s/.test(line)) {
      const depth = (line.match(/^(\s*)/)[1].length / 2) | 0;
      tokens.push({ type: 'bullet', depth, text: line.replace(/^\s*[-*+]\s/, '').trim() });
      continue;
    }
    if (/^\d+\.\s/.test(line)) {
      tokens.push({ type: 'numbered', text: line.replace(/^\d+\.\s/, '').trim() });
      continue;
    }

    // Empty line
    if (line.trim() === '') { tokens.push({ type: 'empty' }); continue; }

    // Paragraph
    tokens.push({ type: 'para', text: line.trim() });
  }

  return tokens;
}

// Strip inline markdown (bold, italic, backticks, links)
function stripInline (t) {
  return t
    .replace(/\*\*(.+?)\*\*/g, '$1')
    .replace(/\*(.+?)\*/g, '$1')
    .replace(/`(.+?)`/g, '$1')
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
    .replace(/\[([^\]]+)\]/g, '$1');
}

// ─── Render tokens → PDF ─────────────────────────────────────────────────────
function renderTokens (doc, tokens) {
  let emptyCount = 0;
  let tableRows  = [];
  let inTable    = false;

  const flushTable = () => {
    if (!tableRows.length) return;
    // Simple table: just render rows as indented text pairs
    safeY(doc, tableRows.length * 18 + 20);
    doc.rect(MARGIN, doc.y, CONTENT, tableRows.length * 18 + 12)
       .fill(LIGHT);
    let ty = doc.y + 6;
    tableRows.forEach((row, ri) => {
      const cells = row.split('|').filter(c => c.trim() !== '');
      const cleanCells = cells.map(c => stripInline(c.trim()));
      const isHeader = ri === 0;
      doc.fontSize(9)
         .font(isHeader ? 'Helvetica-Bold' : 'Helvetica')
         .fillColor(isHeader ? DARK : MID)
         .text(cleanCells.join('   ·   '), MARGIN + 8, ty, { width: CONTENT - 16 });
      ty += 18;
    });
    doc.y = ty + 6;
    tableRows = [];
    inTable   = false;
  };

  tokens.forEach((tok, idx) => {
    // Handle table accumulation
    if (tok.type === 'tableRow') {
      if (!tok.text.includes('--')) { // skip separator rows
        tableRows.push(tok.text);
        inTable = true;
      }
      return;
    }
    if (inTable) flushTable();

    switch (tok.type) {
      case 'h1': {
        safeY(doc, 60);
        doc.moveDown(0.5);
        doc.fontSize(26).fillColor(DARK).font('Helvetica-Bold')
           .text(stripInline(tok.text), MARGIN, doc.y, { width: CONTENT });
        doc.moveDown(0.6);
        hrule(doc, BRAND);
        emptyCount = 0;
        break;
      }
      case 'h2': {
        doc.addPage();
        // Chapter header bar
        doc.rect(0, MARGIN - 20, W, 80).fill(DARK);
        doc.fontSize(18).fillColor('#FFFFFF').font('Helvetica-Bold')
           .text(stripInline(tok.text), MARGIN, MARGIN, { width: CONTENT });
        doc.y = MARGIN + 70;
        emptyCount = 0;
        break;
      }
      case 'h3': {
        safeY(doc, 40);
        doc.moveDown(0.4);
        doc.fontSize(14).fillColor(BRAND).font('Helvetica-Bold')
           .text(stripInline(tok.text), MARGIN, doc.y, { width: CONTENT });
        doc.moveDown(0.3);
        emptyCount = 0;
        break;
      }
      case 'h4': {
        safeY(doc, 30);
        doc.moveDown(0.3);
        doc.fontSize(11).fillColor(DARK).font('Helvetica-Bold')
           .text(stripInline(tok.text), MARGIN, doc.y, { width: CONTENT });
        doc.moveDown(0.2);
        emptyCount = 0;
        break;
      }
      case 'para': {
        safeY(doc, 20);
        doc.fontSize(10.5).fillColor(MID).font('Helvetica')
           .text(stripInline(tok.text), MARGIN, doc.y, {
             width: CONTENT,
             lineGap: 2,
             align: 'justify',
           });
        emptyCount = 0;
        break;
      }
      case 'bullet': {
        safeY(doc, 16);
        const indent = MARGIN + (tok.depth * 14) + 14;
        doc.circle(indent - 8, doc.y + 5, 2.5).fill(BRAND);
        doc.fontSize(10.5).fillColor(MID).font('Helvetica')
           .text(stripInline(tok.text), indent, doc.y, {
             width: CONTENT - (indent - MARGIN),
             lineGap: 1,
           });
        emptyCount = 0;
        break;
      }
      case 'numbered': {
        safeY(doc, 16);
        // count numbered items in sequence
        const numTokens = tokens.slice(0, idx).filter(t => t.type === 'numbered');
        const num = numTokens.length + 1;
        doc.fontSize(10.5).fillColor(MID).font('Helvetica')
           .text(`${num}.  ${stripInline(tok.text)}`, MARGIN + 14, doc.y, {
             width: CONTENT - 14,
             lineGap: 1,
           });
        emptyCount = 0;
        break;
      }
      case 'code': {
        const codeText = tok.text;
        const lineCount = codeText.split('\n').length;
        const boxH = lineCount * 13 + 20;
        safeY(doc, Math.min(boxH + 10, H - MARGIN * 2 - 40));
        doc.moveDown(0.4);
        doc.rect(MARGIN, doc.y, CONTENT, boxH).fill(CODE_BG);
        doc.rect(MARGIN, doc.y, 3, boxH).fill(BRAND);
        doc.fontSize(8).fillColor(DARK).font('Courier')
           .text(codeText, MARGIN + 12, doc.y + 10, {
             width: CONTENT - 20,
             lineGap: 2,
           });
        doc.moveDown(0.6);
        emptyCount = 0;
        break;
      }
      case 'quote': {
        safeY(doc, 40);
        doc.moveDown(0.3);
        doc.rect(MARGIN, doc.y, CONTENT, 0).stroke();
        doc.rect(MARGIN, doc.y, 3, 40).fill(BRAND);
        doc.fontSize(10.5).fillColor(MID).font('Helvetica-Oblique')
           .text(stripInline(tok.text), MARGIN + 14, doc.y + 6, {
             width: CONTENT - 20,
             lineGap: 2,
           });
        doc.moveDown(0.8);
        emptyCount = 0;
        break;
      }
      case 'hr': {
        safeY(doc, 16);
        doc.moveDown(0.4);
        hrule(doc);
        doc.moveDown(0.4);
        emptyCount = 0;
        break;
      }
      case 'empty': {
        emptyCount++;
        if (emptyCount <= 1) doc.moveDown(0.4);
        break;
      }
    }
  });

  if (inTable) flushTable();
}

// ─── Main ────────────────────────────────────────────────────────────────────
async function main () {
  console.log('→ Lendo markdown…');
  const md = fs.readFileSync(INPUT, 'utf8');

  console.log('→ Parseando tokens…');
  const tokens = parseMarkdown(md);

  // Extract chapter list for TOC
  const chapters = tokens
    .filter(t => t.type === 'h2' && /^Capítulo|^Cap\./.test(t.text))
    .map(t => ({ title: t.text }));

  console.log(`→ ${chapters.length} capítulos detectados`);

  console.log('→ Gerando PDF…');
  const doc = newDoc();
  const out = fs.createWriteStream(OUTPUT);

  doc.pipe(out);

  renderCover(doc);
  renderTOC(doc, chapters);
  renderTokens(doc, tokens);

  addPageNumbers(doc);
  doc.end();

  await new Promise((resolve, reject) => {
    out.on('finish', resolve);
    out.on('error',  reject);
  });

  const stats = fs.statSync(OUTPUT);
  console.log(`✓ PDF gerado: ${OUTPUT}`);
  console.log(`  Tamanho: ${(stats.size / 1024).toFixed(1)} KB`);
}

main().catch(err => {
  console.error('Erro ao gerar PDF:', err.message);
  process.exit(1);
});
