#!/usr/bin/env node
// Turn an application Markdown file into a formatted .docx.
// Usage: node export_docx.js <in.md> <out.docx>
//        node export_docx.js --test
// Layout: documents with "## " headings get resume layout (section rules, footer with page numbers);
// documents without get letter layout (wider margins, no footer).
const fs = require("fs");
// Find docx next to this script, globally, or in the user's workspace (where they ran `npm install docx`).
const d = (() => {
  try { return require("docx"); } catch {}
  try { return require(require.resolve("docx", { paths: [process.cwd()] })); } catch {}
  console.error("Missing dependency: run `npm install docx` in your workspace, then try again.");
  process.exit(1);
})();

const FONT = "Calibri";
const A4 = { width: 11906, height: 16838 };
const LINK_TLD = /\.(com|dev|io|au|net|org|app|me|co|ai|design)(\/|$)/i;

// Split text into runs: **bold** segments, emails and URLs become plain-styled hyperlinks.
function runs(text, base = {}) {
  const out = [];
  for (const seg of text.split(/(\*\*[^*]+\*\*)/)) {
    if (!seg) continue;
    const bold = seg.startsWith("**") && seg.endsWith("**");
    const opts = { ...base, bold: bold || base.bold };
    let buf = "";
    for (const tok of (bold ? seg.slice(2, -2) : seg).split(/(\s+)/)) {
      const link = /^[\w.+-]+@[\w-]+\.[\w.]+$/.test(tok) ? `mailto:${tok}`
        : /^https?:\/\/\S+$/.test(tok) ? tok
        : /^[\w.-]+\.[a-z]{2,}(\/\S*)?$/i.test(tok) && LINK_TLD.test(tok) ? `https://${tok}`
        : null;
      if (!link) { buf += tok; continue; }
      if (buf) out.push(new d.TextRun({ ...opts, text: buf }));
      buf = "";
      out.push(new d.ExternalHyperlink({ link, children: [new d.TextRun({ ...opts, text: tok })] }));
    }
    if (buf) out.push(new d.TextRun({ ...opts, text: buf }));
  }
  return out;
}

function parse(md) {
  const lines = md.replace(/\r/g, "").split("\n");
  const blocks = [];
  let name = "";
  let inContact = false;
  lines.forEach((raw, i) => {
    const line = raw.trimEnd();
    const gap = !(lines[i + 1] || "").trim();
    let m;
    if (!line.trim()) { inContact = false; return; }
    if ((m = line.match(/^# (.+)/))) { name = m[1].trim(); blocks.push({ kind: "name", text: name }); inContact = true; return; }
    if (inContact) { blocks.push({ kind: "contact", text: line.trim(), gap }); return; }
    if ((m = line.match(/^## (.+)/))) { blocks.push({ kind: "h2", text: m[1].trim() }); return; }
    if ((m = line.match(/^### (.+)/))) {
      const t = m[1].trim(), j = t.lastIndexOf(" | ");
      blocks.push({ kind: "h3", title: j < 0 ? t : t.slice(0, j), dates: j < 0 ? "" : t.slice(j + 3) });
      return;
    }
    if ((m = line.match(/^\s*[-*] (.+)/))) { blocks.push({ kind: "bullet", text: m[1], gap }); return; }
    const prev = blocks[blocks.length - 1];
    blocks.push({ kind: prev && prev.kind === "h3" ? "sub" : "para", text: line.trim(), gap });
  });
  return { name, blocks, resume: blocks.some((b) => b.kind === "h2") };
}

function build(md) {
  const { name, blocks, resume } = parse(md);
  const margin = resume ? 1020 : 1440;
  const width = A4.width - 2 * margin;
  const render = {
    name: (b) => new d.Paragraph({ children: runs(b.text, { bold: true, size: 40 }) }),
    contact: (b) => new d.Paragraph({ spacing: { after: b.gap ? 160 : 0 }, children: runs(b.text) }),
    h2: (b) => new d.Paragraph({ style: "SectionHeading", children: runs(b.text) }),
    h3: (b) => new d.Paragraph({
      spacing: { before: 60 }, keepNext: true,
      tabStops: [{ type: d.TabStopType.RIGHT, position: width }],
      children: [...runs(b.title, { bold: true }), ...(b.dates ? [new d.TextRun({ children: [new d.Tab(), b.dates] })] : [])],
    }),
    sub: (b) => new d.Paragraph({ keepNext: true, spacing: { after: b.gap ? 120 : 0 }, children: runs(b.text) }),
    bullet: (b) => new d.Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { after: b.gap ? 120 : 0 }, children: runs(b.text) }),
    para: (b) => new d.Paragraph({ spacing: { after: b.gap ? 160 : 0 }, children: runs(b.text) }),
  };
  const footers = resume ? { default: new d.Footer({ children: [new d.Paragraph({
    alignment: d.AlignmentType.RIGHT,
    // "Name – Position, Org" headings (criteria responses) keep only the name in the footer
    children: [new d.TextRun({ children: [`${name.split(/ [–-] /)[0]}, page `, d.PageNumber.CURRENT], size: 18 })],
  })] }) } : undefined;

  return new d.Document({
    creator: name,
    title: name,
    styles: {
      default: { document: { run: { font: FONT, size: 22 } } }, // 11pt
      paragraphStyles: [{
        id: "SectionHeading", name: "Section Heading", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { bold: true, allCaps: true, size: 24, font: FONT },
        paragraph: {
          spacing: { before: 240, after: 80 }, keepNext: true,
          border: { bottom: { style: d.BorderStyle.SINGLE, size: 6, color: "000000", space: 1 } },
        },
      }],
    },
    numbering: { config: [{
      reference: "bullets",
      levels: [{ level: 0, format: d.LevelFormat.BULLET, text: "•", alignment: d.AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 360, hanging: 240 } } } }],
    }] },
    sections: [{
      properties: { page: { size: A4, margin: { top: margin, bottom: margin, left: margin, right: margin } } },
      footers,
      children: blocks.map((b) => render[b.kind](b)),
    }],
  });
}

function test() {
  const assert = require("assert");
  const r = parse("# Jo Bloggs\n0400 | jo@x.com\n\n## Projects\n### App | Mar 2025 – Current\nReact | github.com/jo/app\n- Built it\n");
  assert.strictEqual(r.name, "Jo Bloggs");
  assert.ok(r.resume);
  assert.deepStrictEqual(r.blocks.map((b) => b.kind), ["name", "contact", "h2", "h3", "sub", "bullet"]);
  assert.strictEqual(r.blocks[3].dates, "Mar 2025 – Current");
  assert.ok(!parse("# Jo\n\nDear Ms X,\n\nHi.\n").resume);
  const linked = runs("a **b** jo@x.com github.com/jo Next.js").filter((x) => x instanceof d.ExternalHyperlink);
  assert.strictEqual(linked.length, 2);
  console.log("ok");
}

if (require.main === module) {
  const [inPath, outPath] = process.argv.slice(2);
  if (inPath === "--test") test();
  else if (!inPath || !outPath) { console.error("Usage: node export_docx.js <in.md> <out.docx>"); process.exit(2); }
  else d.Packer.toBuffer(build(fs.readFileSync(inPath, "utf8"))).then((buf) => fs.writeFileSync(outPath, buf));
}
