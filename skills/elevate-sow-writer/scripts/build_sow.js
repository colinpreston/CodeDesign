#!/usr/bin/env node
/*
 * Elevate SoW builder — turns a SoW spec (JSON) into a Code-branded .docx.
 *
 *   node build_sow.js <spec.json> [output.docx]
 *
 * Fixed boilerplate (warranty, governance, ceremonies, dependencies core,
 * acceptance, appendix) is generated here so it is identical every time.
 * Variable content (summary, overview, scope modules, budget, timing) comes
 * from the spec. Out of scope is derived from a master list. A QA report is
 * printed to stdout as JSON after the build.
 */
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell,
  Footer, AlignmentType, LevelFormat, HeadingLevel, BorderStyle, WidthType,
  ShadingType, PageNumber, PositionalTab, PositionalTabAlignment,
  PositionalTabRelativeTo, PositionalTabLeader, ExternalHyperlink,
  TableOfContents, HorizontalPositionRelativeFrom, VerticalPositionRelativeFrom,
  VerticalAlign, PageBreak, TableLayoutType, Tab, TabStopType,
} = require("docx");

// ---------- brand ----------
const NAVY = "000050";
const AQUA = "93DFE3";
const WHITE = "FFFFFF";
const LINK = "1F4FD8";
const FONT = process.env.SOW_FONT || "WPP"; // Code house font; Word substitutes if not installed
const BODY = 21; // half-points (10.5pt)
const ASSETS = path.join(__dirname, "..", "assets");
const PAGE_W = 11906, PAGE_H = 16838; // A4
const MARGIN = 1300;
const CONTENT_W = PAGE_W - MARGIN * 2; // 9306
const COVER_W = PAGE_W - 1400; // cover margins 700 each side

// ---------- master out-of-scope list ----------
const MASTER_FEATURES = {
  bloomreach: "Bloomreach",
  taps_sources: "Taps and Sources",
  guid: "GUID Site ID",
  salsify_pim: "Salsify PIM",
  pdp: "Product Detail Pages (PDP)",
  pfg: "Product Filter Grid (PFG)",
  infinity: "Infinity call tracking",
  trustpilot: "Trustpilot",
  turnstile: "Turnstile",
  sitespect: "Sitespect",
  vis_app: "Vis app",
  design_tokens: "Design token application",
  page_designs: "Journey, page designs / wireframes",
  contact_us: "Contact Us form",
  request_appointment: "Request an Appointment form",
  request_consultation: "Request a Consultation form",
  request_brochure: "Request a Brochure form",
  request_ebrochure: "Request an E-brochure form",
  email_signup: "Email sign up",
  samples: "Samples",
  dealer_locator: "Dealer / Showroom Locator",
  pii_exports: "PII Blob storage exports",
  blob_storage: "Blob storage",
  live_diary: "Live Diary",
  discount_codes: "Discount codes",
  seo: "Any SEO activity (HD can set up / manage this within Prismic CMS)",
  image_migration: "Image migration",
  content_migration: "Automated / scripted / manual content migrations",
};
const ALWAYS_LAST_OOS = "Any variations to Elevate components or architecture that are not specified within this SoW";

// ---------- QA collection ----------
const allText = [];
const tbcs = [];
const collect = (t, where) => { if (t) allText.push({ t: String(t), where }); };

// ---------- inline text parsing: **bold**, *italic*, [text](url), {{ref:id}} ----------
let REFS = {};
function resolveRefs(s) {
  return String(s).replace(/\{\{ref:([\w-]+)\}\}/g, (m, id) => REFS[id] || `[BROKEN REF: ${id}]`);
}
function runs(text, opts = {}) {
  const s = resolveRefs(text);
  const color = opts.color || NAVY;
  const size = opts.size || BODY;
  const out = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*|\[[^\]]+\]\([^)]+\))/g;
  let last = 0, m;
  const plain = (t, extra = {}) => new TextRun({ text: t, font: FONT, size, color, bold: opts.bold, italics: opts.italics, ...extra });
  while ((m = re.exec(s))) {
    if (m.index > last) out.push(plain(s.slice(last, m.index)));
    const tok = m[0];
    if (tok.startsWith("**")) out.push(plain(tok.slice(2, -2), { bold: true }));
    else if (tok.startsWith("[")) {
      const mm = tok.match(/\[([^\]]+)\]\(([^)]+)\)/);
      out.push(new ExternalHyperlink({ link: mm[2], children: [new TextRun({ text: mm[1], font: FONT, size, color: LINK, underline: {} })] }));
    } else out.push(plain(tok.slice(1, -1), { italics: true }));
    last = m.index + tok.length;
  }
  if (last < s.length) out.push(plain(s.slice(last)));
  (s.match(/\[TBC[^\]]*\]/g) || []).forEach((x) => tbcs.push(x));
  return out;
}
const P = (text, opts = {}) => {
  collect(resolveRefs(text), opts.where);
  return new Paragraph({
    spacing: { after: opts.after ?? 140, before: opts.before ?? 0, line: 300 },
    alignment: opts.align,
    keepNext: opts.keepNext,
    children: runs(text, opts),
  });
};
function bullets(items, level = 0, where) {
  const out = [];
  for (const it of items) {
    if (Array.isArray(it)) { out.push(...bullets(it, level + 1, where)); continue; }
    if (typeof it === "object" && it.text) {
      out.push(bulletPara(it.text, level, where, it.detail));
      if (it.sub) out.push(...bullets(it.sub, level + 1, where));
      continue;
    }
    out.push(bulletPara(it, level, where));
  }
  return out;
}
function bulletPara(text, level, where, detail) {
  collect(resolveRefs(text), where);
  const ch = runs(text);
  if (detail) { collect(detail, where); ch.push(new TextRun({ break: 1 }), ...runs(detail)); }
  return new Paragraph({ numbering: { reference: "bullets", level: Math.min(level, 2) }, spacing: { after: 80, line: 290 }, children: ch });
}

// ---------- headings ----------
const H1 = (num, title) => new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: true, children: [new TextRun({ text: `${num}   ${title}`, font: FONT })] });
const H2 = (num, title, pb) => new Paragraph({ heading: HeadingLevel.HEADING_2, pageBreakBefore: !!pb, children: [new TextRun({ text: num ? `${num}   ${title}` : title, font: FONT })] });
const H3 = (title) => new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun({ text: title, font: FONT })] });
const MOD = (num, title) => [
  new Paragraph({ spacing: { before: 280, after: 40 }, keepNext: true, children: [new TextRun({ text: num, font: FONT, size: BODY, bold: true, color: NAVY })] }),
  new Paragraph({ spacing: { after: 140 }, keepNext: true, children: [new TextRun({ text: title, font: FONT, size: BODY, bold: true, color: NAVY })] }),
];
const LABEL = (t) => new Paragraph({ spacing: { before: 160, after: 80 }, keepNext: true, children: [new TextRun({ text: t, font: FONT, size: BODY, bold: true, color: NAVY })] });

// ---------- tables ----------
const border = { style: BorderStyle.SINGLE, size: 4, color: NAVY };
const borders = { top: border, bottom: border, left: border, right: border, insideHorizontal: border, insideVertical: border };
function cellContent(c, opts) {
  if (c == null) return [new Paragraph({ children: [] })];
  if (typeof c === "string" || typeof c === "number") return [cellPara(String(c), opts)];
  const out = [];
  if (c.text) out.push(cellPara(c.text, opts));
  if (c.bullets) out.push(...bullets(c.bullets, 0, "table"));
  return out.length ? out : [new Paragraph({ children: [] })];
}
function cellPara(t, opts = {}) {
  collect(resolveRefs(t), "table");
  return new Paragraph({ alignment: opts.align, spacing: { after: 40, line: 280 }, children: runs(t, { color: opts.color, bold: opts.bold, size: opts.size || 20 }) });
}
function makeCell(c, width, o = {}) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    columnSpan: o.span,
    verticalAlign: o.valign || VerticalAlign.TOP,
    shading: o.fill ? { fill: o.fill, type: ShadingType.CLEAR, color: "auto" } : undefined,
    margins: { top: 70, bottom: 70, left: 110, right: 110 },
    children: cellContent(c, { color: o.color, bold: o.bold, align: o.align }),
  });
}
/** table({ columns:[{h, w(ratio), align}], rows:[[...]], total:[...]} ) */
function table(spec, width = CONTENT_W) {
  const ratios = spec.columns.map((c) => c.w || 1);
  const sum = ratios.reduce((a, b) => a + b, 0);
  let widths = ratios.map((r) => Math.floor((r / sum) * width));
  widths[widths.length - 1] += width - widths.reduce((a, b) => a + b, 0);
  const rows = [];
  rows.push(new TableRow({ tableHeader: true, children: spec.columns.map((c, i) => makeCell(c.h, widths[i], { fill: NAVY, color: WHITE, align: c.align })) }));
  for (const r of spec.rows) rows.push(new TableRow({ cantSplit: true, children: r.map((c, i) => makeCell(c, widths[i], { align: spec.columns[i].align })) }));
  if (spec.total) rows.push(new TableRow({ children: spec.total.map((c, i) => makeCell(c, widths[i], { fill: AQUA, bold: true, align: spec.columns[i].align })) }));
  return [new Table({ width: { size: width, type: WidthType.DXA }, columnWidths: widths, borders, layout: TableLayoutType.FIXED, rows }), new Paragraph({ spacing: { after: 160 }, children: [] })];
}

// ---------- blocks ----------
function renderBlocks(blocks = [], where) {
  const out = [];
  for (const b of blocks) {
    if (typeof b === "string") out.push(P(b, { where }));
    else if (b.p) out.push(P(b.p, { where, italics: b.italic, bold: b.bold }));
    else if (b.bullets) out.push(...bullets(b.bullets, 0, where), new Paragraph({ spacing: { after: 80 }, children: [] }));
    else if (b.label) out.push(LABEL(b.label));
    else if (b.table) out.push(...table(b.table));
    else if (b.note) out.push(P(`Note: ${b.note}`, { italics: true, where }));
    else if (b.pagebreak) out.push(new Paragraph({ children: [new PageBreak()] }));
  }
  return out;
}

// ---------- money ----------
const gbp = (n) => "£" + Number(n).toLocaleString("en-GB", { minimumFractionDigits: n % 1 ? 2 : 0, maximumFractionDigits: 2 });

// =====================================================================
function build(spec) {
  const warnings = [];
  const m = spec.meta;
  const brandLabel = m.stakeholder_label || m.brand; // e.g. "Luxaflex Project"
  const buildLabel = m.build_label || "this website build"; // e.g. "the Luxaflex Project locale build"
  const client = m.client || "Hunter Douglas";
  const children = [];

  // ---- pre-pass: section numbers + refs ----
  REFS = {};
  let n = 0;
  const plan = [];
  for (const s of spec.sections) {
    n++;
    const entry = { s, num: String(n) };
    plan.push(entry);
    if (s.id) REFS[s.id] = String(n);
    let sub = 0, mod = 0;
    for (const it of s.items || []) {
      if (it.module) { mod++; it._num = `${n}.1.${mod}`; }
      else if (it.sub) { sub++; it._num = `${n}.${sub}`; }
      if (it.id) REFS[it.id] = it._num;
    }
    if (s.type === "budget") { REFS.billing = `${n}.1`; }
  }
  // standard sections appended after spec sections
  const std = [];
  if (spec.warranty !== false) std.push("warranty");
  std.push("governance", "notes", "acceptance");
  const stdNums = {};
  for (const k of std) { n++; stdNums[k] = String(n); }
  n++; stdNums.appendix = String(n);

  // ---- section renderers ----
  const inScopeKeys = new Set();
  for (const { s, num } of plan) {
    children.push(H1(num, s.title));
    if (s.type === "budget") { children.push(...renderBudget(s, num, warnings)); continue; }
    children.push(...renderBlocks(s.blocks, s.title));
    for (const it of s.items || []) {
      if (it.module) { children.push(...MOD(it._num, it.module)); children.push(...renderBlocks(it.blocks, it.module)); (it.features || []).forEach((k) => inScopeKeys.add(k)); }
      else if (it.sub) { children.push(H2(it._num, it.sub)); children.push(...renderBlocks(it.blocks, it.sub)); }
      else if (it.out_of_scope) children.push(...renderOOS(it.out_of_scope, inScopeKeys, warnings));
      else children.push(...renderBlocks([it], s.title));
    }
  }

  // ---- warranty ----
  if (stdNums.warranty) {
    const w = stdNums.warranty;
    children.push(H1(w, "Warranty Period"));
    children.push(P("Upon the successful delivery and acceptance of the completed development work Code will provide a **30-day warranty period**. During this warranty period, the following terms will apply:"));
    children.push(H3(`${w}.1 Scope of Warranty:`));
    children.push(...bullets([
      "Code warrants that the delivered solution will perform according to the agreed-upon specifications & functionality outlined in this SoW and signed off requirements at each individual ticket level",
      "Code will correct any defects, bugs, or performance issues identified during the warranty period that are directly attributable to the development work performed.",
      "Any discrepancies between the actual functionality and the documented specifications will be considered a defect and will be corrected at no additional cost to Hunter Douglas.",
      "Given the likelihood that features will be delivered iteratively it’s essential that all client acceptance testing is completed in a timely manner as features and functionality become available to ensure they are working as expected throughout the development build phase.",
    ]));
    children.push(H3(`${w}.2 Warranty Support:`));
    children.push(...bullets([
      "Code will respond to and address any issues raised by Hunter Douglas within a reasonable timeframe, not exceeding **72 hours** from the time of notification.",
      "All necessary fixes, updates, and modifications related to defects or performance issues will be completed promptly to minimise disruption to the client operations.",
    ]));
    children.push(H3(`${w}.3 Exclusions:`));
    children.push(...bullets([
      "The warranty does not cover issues caused by:",
      ["Misuse or alteration of the system by Hunter Douglas or third parties.", "Third-party services, tools, or systems outside Code’s responsibility.", "Issues arising from changes to the environment or infrastructure that were not present during the original development and deployment."],
    ]));
    children.push(H3(`${w}.4 Expiration of Warranty:`));
    children.push(...bullets([
      `The warranty period will expire **30 days** after the launch of ${m.warranty_trigger || "the first brand site"}, at which point Code’s obligation to provide free maintenance and support under this clause will conclude.`,
      "After the expiration of the warranty period, any further modifications, bug fixes, or support requests will be subject to a separate maintenance agreement or billed at Code’s standard rates.",
    ]));
    children.push(P("This warranty ensures that the delivered development meets the required standards and is free of critical defects during the initial operation phase.", { before: 160 }));
  }

  // ---- governance ----
  const g = spec.governance || {};
  const gn = stdNums.governance;
  children.push(H1(gn, "Governance"));
  children.push(H2(`${gn}.1`, "People"));
  children.push(P("Code’s processes are underpinned by assigned Product Consultants & Delivery Managers who manage the overarching relationship and delivery on a day-to-day basis and act as your key contacts at Code for this workstream."));
  children.push(P("Good lines of communication and clear roles and responsibilities are key to getting this work done well and on time."));
  children.push(H3("Delivery Manager"));
  children.push(P(`${g.delivery_manager || "[TBC: Delivery Manager]"} will be your main daily point of contact in our relationship to date and will continue to be your Delivery Manager for the duration of delivery. Responsibilities will include:`));
  children.push(...bullets(["Co-ordinating internal Code resources and teams", "Leading ceremonies related to delivery", "Planning and performance reporting", "Prioritisation of work", "Budget management", "Being the single point of contact for all delivery related queries and communication"]));
  children.push(H3("Digital Consultant"));
  children.push(P(`${g.digital_consultant || "[TBC: Digital Consultant]"} will continue to be the Digital Consultant, ensuring that the product meets the demands of your business and aligns to a longer-term business strategy that we have agreed in the ‘definition’ stage. Responsibilities will include:`));
  children.push(...bullets(["Working to deliver against the business case aspirations set in ‘definition’", "Leading the client on new opportunity recognition, digital performance measurement and business reporting", "Supporting the team in aligning decisions to wider business strategy", "Leading quarterly and business reviews", "A first point of escalation"]));

  children.push(H2(`${gn}.2`, "Ceremonies & Ways of Working", true));
  children.push(P("Code believes in a collaborative approach to working with our clients, and closely integrate key stakeholders as much as possible with delivery routines."));
  children.push(P("The delivery of this Statement of Work will follow a Scrum Methodology, meaning that the work will be broken into 1 or 2 week ‘Sprints’ of work to be delivered with a sprint starting on a Wednesday and finishing on a Thursday."));
  children.push(P("At the end of each sprint, the work completed will be delivered to Hunter Douglas in the form of a weekly build demo where the team will walk you through what has been delivered."));
  children.push(P("It is expected that Hunter Douglas stakeholders will actively engage in these demo sessions and sign off work as meeting the desired scope at the end of client acceptance testing."));
  children.push(P("In addition to the demo sessions, we will also conduct weekly project status calls, where we will communicate progress updates on the project and any active blockers we may need support to remove."));
  children.push(P(`The following ceremonies have been anticipated as part of the delivery of ${buildLabel}:`));
  const cer = g.ceremonies || [["Stand-up", "Tues / Thurs 9.30am", "All relevant HD stakeholders"], ["Weekly build demo", "Weekly", "TBC"]];
  children.push(...table({ columns: [{ h: "Ceremony", w: 4 }, { h: "Frequency", w: 3 }, { h: "Hunter Douglas Attendees", w: 3 }], rows: cer }, 7400));

  children.push(H2(`${gn}.3`, "Roles & Responsibilities", true));
  children.push(H3(`Core ${client} Team`));
  children.push(...table({ columns: [{ h: "Name", w: 3 }, { h: "Project Role", w: 7 }], rows: (g.client_team || [["[TBC]", "[TBC]"]]) }, 7400));
  children.push(H3("Core Code Team"));
  const ct = g.code_team || [];
  const domains = new Set(ct.map((r) => (r[2] || "").split("@")[1]).filter(Boolean).map((d) => d.toLowerCase()));
  if (domains.size > 1) warnings.push(`Code team emails use more than one domain: ${[...domains].join(", ")}`);
  children.push(...table({ columns: [{ h: "Name", w: 2.4 }, { h: "Project Role", w: 2.6 }, { h: "Email Address", w: 5 }], rows: ct.map((r) => [r[0], r[1], r[2] ? `[${r[2]}](mailto:${r[2]})` : ""]) }, 7800));

  // ---- items of note ----
  const nn = stdNums.notes;
  children.push(H1(nn, "Items of note"));
  children.push(H3("Dependencies and assumptions"));
  const deps = [
    `Dependency: All relevant ${brandLabel} stakeholders are engaged on all planned routines and meetings and agree to sign off work / scope / client acceptance needs in line with the delivery plan`,
    ...(spec.dependencies || []),
    "Dependency: All ticket requirements are scoped and signed off by HD stakeholders relevant to the work before Engineering activities can commence",
    "Assumption: No other changes in scope will be requested once the project has formally kicked off in line with the in / out of scope detailed in this SoW",
  ];
  children.push(...table({ columns: [{ h: "Ref.", w: 1.1 }, { h: "Dependency or assumption", w: 8.9 }], rows: deps.map((d, i) => [String(i + 1).padStart(3, "0"), d]) }, 7800));

  // ---- acceptance ----
  const an = stdNums.acceptance;
  children.push(H1(an, "Acceptance"));
  children.push(P("I understand that the above detail comprises the scope of the agreed work, and this document supersedes any previous e-mails, phone calls, proposals or documentation provided or exchanged which detailed the scope. I also accept that additional services can be included but this would be subject to an additional cost."));
  const sig = (label) => {
    const W = [1700, 2600, 1100, 2000];
    const lab = (t) => makeCell(t, W[0], { fill: AQUA, valign: VerticalAlign.CENTER });
    const blank = (w, span) => makeCell("", w, { span });
    return [new Table({
      width: { size: 7400, type: WidthType.DXA }, columnWidths: W, borders, layout: TableLayoutType.FIXED,
      rows: [
        new TableRow({ children: [makeCell(`Acceptance – ${label}`, 7400, { span: 4, fill: NAVY, color: WHITE })] }),
        new TableRow({ height: { value: 500, rule: "atLeast" }, children: [lab("Date"), blank(5700, 3)] }),
        new TableRow({ height: { value: 600, rule: "atLeast" }, children: [lab("Name"), blank(W[1]), makeCell("Job Title", W[2], { fill: AQUA, valign: VerticalAlign.CENTER }), blank(W[3])] }),
        new TableRow({ height: { value: 1000, rule: "atLeast" }, children: [lab("Signature"), blank(5700, 3)] }),
      ],
    }), new Paragraph({ spacing: { after: 0 }, children: [] })];
  };
  children.push(...sig(m.acceptance_client || client));
  children.push(...sig("WPP Media UK Ltd t/a Code"));
  children.push(P("**Thank you.**", { before: 400, after: 40 }));
  children.push(P("We hope that this document and the supporting discussions have provided reassurance and also excitement about the possibility of Discovering, Innovating, Making or Growing something together. For 25 years the best work has come from doing work in the best way, together."));

  // ---- appendix ----
  const ap = stdNums.appendix;
  children.push(H1(ap, "Appendix"));
  children.push(H2(`${ap}.1`, "Choose Code"));
  children.push(P("Code is a design & technology agency, working alongside our clients to create and evolve world-class customer experiences for their customers."));
  children.push(P("We use research methods to identify opportunities for customer experience improvement, and then find the most efficient way to design, build, test and improve experiences, addressing the needs of real people."));
  children.push(P("Established in 1999, and part of WPP since 2016, Code’s clients include the BBC, GoAhead Group, The Crown Estate, Hillarys Blinds, Solmar Villas and Bayer Crop Science."));
  children.push(P("**Code**", { before: 240, after: 0 }));
  children.push(P("Creative.Technology.People"));

  return { children, warnings, inScopeKeys };
}

function renderOOS(o, inScopeKeys, warnings) {
  const out = [H2(null, "Out of scope")];
  out.push(P("The following deliverables are out of scope for this statement of work:"));
  const inScope = new Set([...(o.in_scope || []), ...inScopeKeys]);
  for (const k of inScope) if (!MASTER_FEATURES[k]) warnings.push(`Unknown in_scope feature key: ${k}`);
  const items = [];
  for (const [k, label] of Object.entries(MASTER_FEATURES)) {
    if (inScope.has(k)) continue;
    const linked = (o.linked || []).find((l) => l.key === k);
    items.push(linked ? `${label} (see section {{ref:${linked.ref}}})` : label);
  }
  for (const l of o.linked || []) if (!MASTER_FEATURES[l.key]) items.push(`${l.label} (see section {{ref:${l.ref}}})`);
  for (const e of o.extras || []) items.push(e);
  // duplicate check
  const seen = new Set();
  for (const i of items) { const k = (typeof i === "string" ? i : i.text).toLowerCase(); if (seen.has(k)) warnings.push(`Duplicate out-of-scope item: ${k}`); seen.add(k); }
  items.push(ALWAYS_LAST_OOS);
  out.push(...bullets(items, 0, "Out of scope"));
  return out;
}

function renderBudget(s, num, warnings) {
  const out = [];
  const rate = s.day_rate;
  const isNum = (v) => typeof v === "number" && isFinite(v);
  const money = (v, fallback = "[TBC: cost]") => (isNum(v) ? gbp(v) : (v || fallback));
  out.push(...renderBlocks(s.intro || [], "Budget"));
  if (s.lines && s.lines.length) {
    const showDays = s.lines.some((l) => l.days != null);
    let sumDays = 0, sumCost = 0, allCosted = true;
    const rows = s.lines.map((l) => {
      const cost = l.cost != null ? l.cost : (isNum(l.days) && rate ? l.days * rate : null);
      if (isNum(l.days) && rate && isNum(l.cost) && Math.abs(l.days * rate - l.cost) > 0.5) warnings.push(`Budget line "${l.activity}": ${l.days} days × ${gbp(rate)} = ${gbp(l.days * rate)} but cost given as ${gbp(l.cost)}`);
      if (isNum(l.days)) sumDays += l.days;
      if (isNum(cost)) sumCost += cost; else allCosted = false;
      const act = l.bullets ? { text: l.activity, bullets: l.bullets } : l.activity;
      const costCell = cost == null && s.fixed ? "" : money(cost);
      return showDays ? [act, l.days ?? "", costCell] : [act, costCell];
    });
    let total = s.total != null ? s.total : (allCosted ? sumCost : null);
    if (isNum(s.total) && allCosted && Math.abs(sumCost - s.total) > 0.5 && !s.fixed) warnings.push(`Budget lines sum to ${gbp(sumCost)} but total given as ${gbp(s.total)}`);
    s._total = isNum(total) ? total : null;
    if (s._total == null) warnings.push(s.fixed
      ? "PRICE MISSING: fixed-cost SoW has no fixed amount. Ask the user for it (\u00a3, ex VAT) and set budget.total to a number."
      : "PRICE MISSING: one or more budget lines have no days/cost. Ask the user for the days per line.");
    const cols = showDays ? [{ h: "Activity", w: 6.6 }, { h: "Days effort", w: 1.4 }, { h: "Costs", w: 2 }] : [{ h: "Activity", w: 7.5 }, { h: s.fixed ? "Fixed Cost" : "Cost", w: 2.5 }];
    const totalCell = money(total, "[TBC: total cost]");
    s._totalCell = totalCell;
    const totalRow = showDays ? [s.total_label || "TOTAL PROJECT COSTS", sumDays ? String(sumDays) : "", totalCell] : [s.total_label || "TOTAL", totalCell];
    out.push(...table({ columns: cols, rows, total: totalRow }));
  }
  out.push(P("Note: All costs provided are exclusive of VAT which will be charged at the prevailing rate", { italics: true }));
  if (s.flex_note !== false) out.push(P("Note: Team role contribution identified above should be used as a guide only and will remain flexible throughout to best optimise / prioritise the work required.", { italics: true }));
  out.push(H2(`${num}.1`, "Billing plan"));
  const b = s.billing || {};
  if (b.po) out.push(P(`No billing plan is required as PO ${b.po} has already been provided and invoiced against.`));
  else if (b.milestones) {
    out.push(P("The billing plan associated with this work has been included below, subject to a timely contract agreement. All costs are exclusive of VAT."));
    const allNum = b.milestones.every((x) => isNum(x.value));
    if (!allNum) warnings.push("BILLING MISSING: one or more milestone amounts aren't numbers. Ask the user for each month and amount.");
    const sum = allNum ? b.milestones.reduce((a, x) => a + x.value, 0) : null;
    if (allNum && s._total != null && Math.abs(sum - s._total) > 0.5) warnings.push(`Billing plan sums to ${gbp(sum)} but budget total is ${gbp(s._total)}`);
    out.push(...table({ columns: [{ h: "Milestone", w: 7 }, { h: "Invoice Value", w: 3, align: AlignmentType.RIGHT }], rows: b.milestones.map((x) => [x.label, money(x.value, "[TBC: value]")]), total: ["TOTAL", allNum ? gbp(sum) : (s._totalCell || "[TBC: total cost]")] }, 8400));
  } else out.push(P("[TBC: billing plan — PO number or milestone invoices]"));
  return out;
}

// ---------- cover ----------
function cover(m) {
  const img = fs.readFileSync(path.join(ASSETS, m.cover_image ? m.cover_image : "cover.jpg"));
  const logo = fs.readFileSync(path.join(ASSETS, "code-logo-white.png"));
  const w = (t, size, extra = {}) => new TextRun({ text: t, font: FONT, size, color: WHITE, ...extra });
  ["version", "date", "author", "brand", "title", "client"].forEach((k) => collect(m[k], "cover"));
  return [
    new Paragraph({ children: [new ImageRun({ type: "jpg", data: img, transformation: { width: 794, height: 1123 }, floating: { horizontalPosition: { relative: HorizontalPositionRelativeFrom.PAGE, offset: 0 }, verticalPosition: { relative: VerticalPositionRelativeFrom.PAGE, offset: 0 }, behindDocument: true, allowOverlap: true } }),
      w(`VERSION ${m.version}`, 22), new TextRun({ children: [new Tab()] }), w(m.date, 22), new TextRun({ children: [new Tab()] }), w(m.author, 22)],
      tabStops: [{ type: TabStopType.CENTER, position: COVER_W / 2 }, { type: TabStopType.RIGHT, position: COVER_W }] }),
    new Paragraph({ spacing: { before: 6400, after: 200 }, alignment: AlignmentType.CENTER, children: [w(m.eyebrow || "STATEMENT OF WORK", 32)] }),
    new Paragraph({ spacing: { after: 160 }, alignment: AlignmentType.CENTER, children: [w(m.brand || "", 32)] }),
    new Paragraph({ spacing: { after: 1200 }, alignment: AlignmentType.CENTER, children: [w(m.title || "Website Build", m.title && m.title.length > 22 ? 52 : 80)] }),
    new Paragraph({ spacing: { after: 0 }, alignment: AlignmentType.CENTER, children: [w(m.client || "Hunter Douglas", 32)] }),
    new Paragraph({ spacing: { before: 3500 }, tabStops: [{ type: TabStopType.RIGHT, position: COVER_W }], children: [w("Creative.Technology.People", 24), new TextRun({ children: [new Tab()] }), new ImageRun({ type: "png", data: logo, transformation: { width: 86, height: 42 } })] }),
  ];
}

function docControl(spec) {
  const dc = spec.doc_control || {};
  return [
    new Paragraph({ children: [new TextRun({ text: "Document control", font: FONT, size: 30, bold: true, color: NAVY })], spacing: { after: 240 } }),
    H3("Version Control"),
    ...table({ columns: [{ h: "Version", w: 1.2 }, { h: "Revision date", w: 1.7 }, { h: "Author", w: 2 }, { h: "Summary of changes", w: 5 }], rows: (dc.versions || []).map((v) => [v.version, v.date, v.author, v.summary]) }),
    H3("Distribution"),
    ...table({ columns: [{ h: "Version", w: 1.2 }, { h: "Date", w: 1.7 }, { h: "Name", w: 3.5 }, { h: "Company", w: 3.5 }], rows: (dc.distribution || []).map((v) => [v.version, v.date, v.name, v.company]) }),
  ];
}

// ---------- QA ----------
function qa(spec, warnings) {
  const issues = [...warnings];
  const text = allText.map((x) => x.t).join("\n");
  const checks = [
    [/as agreed in the\.\s/i, "Truncated sentence “…as agreed in the.”"],
    [/formerly kicked off/i, "“formerly kicked off” should be “formally”"],
    [/Error! Bookmark/i, "Broken bookmark text"],
    [/BROKEN REF/i, "Unresolved {{ref:…}} cross-reference"],
    [/\bDeutte\b/i, "Spelling: Deutte → Duette"],
    [/\bCalander\b/i, "Spelling: Calander → Calendar"],
    [/incapsulated/i, "Spelling: incapsulated → encapsulated"],
    [/customer date\b/i, "Typo: customer date → customer data"],
    [/\?\s*$/m, "A line ends with a question mark — possible open question left in scope text"],
  ];
  for (const [re, msg] of checks) if (re.test(text)) issues.push(msg);
  const bud = (spec.sections || []).find((x) => x.type === "budget");
  if (bud && bud._total != null) {
    const want = gbp(bud._total);
    const summary = (spec.sections[0].blocks || []).map((b) => (typeof b === "string" ? b : b.p || "")).join(" ");
    if (!summary.includes(want)) issues.push(`Summary doesn’t quote the budget total ${want}. Make the two match.`);
  }
  // locale count words vs declared locales
  const nLoc = (spec.meta.locales || []).length;
  const words = { one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8 };
  const re = /\b(one|two|three|four|five|six|seven|eight)\s+(locales?|websites?|website builds|brands?|sites?)\b/gi;
  let mm;
  while ((mm = re.exec(text))) {
    const v = words[mm[1].toLowerCase()];
    if (nLoc && v !== nLoc && /locale/i.test(mm[2])) issues.push(`Text says “${mm[0]}” but ${nLoc} locale(s) declared in meta.locales`);
  }
  // other HD brand names leaking in
  const brands = ["Hillarys", "Luxaflex", "Duette", "Aluvert", "Kjells", "Markisemannen", "Fasadeprodukter", "Wallners", "Sunway", "Velux"];
  const allowed = new Set((spec.meta.allowed_brand_mentions || []).concat(spec.meta.brand || "", spec.meta.stakeholder_label || "").map((s) => s.toLowerCase()));
  for (const b of brands) {
    if ([...allowed].some((a) => a.includes(b.toLowerCase()))) continue;
    const c = (text.match(new RegExp(`\\b${b}\\b`, "g")) || []).length;
    if (c) issues.push(`Mentions “${b}” ${c}× — check it isn’t left over from a previous SoW (add to meta.allowed_brand_mentions if intended)`);
  }
  return { issues, tbcs: [...new Set(tbcs)] };
}

// =====================================================================
async function main() {
  const [specPath, outArg] = process.argv.slice(2);
  if (!specPath) { console.error("usage: node build_sow.js spec.json [out.docx]"); process.exit(1); }
  const spec = JSON.parse(fs.readFileSync(specPath, "utf8"));
  const out = outArg || spec.output || "SoW.docx";
  const { children, warnings } = build(spec);
  const logo = fs.readFileSync(path.join(ASSETS, "code-logo-navy.png"));
  const footer = new Footer({ children: [new Paragraph({ children: [
    new ImageRun({ type: "png", data: logo, transformation: { width: 74, height: 36 } }),
    new TextRun({ children: [new Tab(), PageNumber.CURRENT], font: FONT, size: 20, color: NAVY }),
  ], tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }] })] });
  const page = { size: { width: PAGE_W, height: PAGE_H }, margin: { top: 1440, bottom: 1300, left: MARGIN, right: MARGIN, footer: 500 } };

  const doc = new Document({
    creator: spec.meta.author || "Code",
    title: `Statement of Work – ${spec.meta.brand || ""} ${spec.meta.title || ""}`.trim(),
    features: { updateFields: true },
    styles: {
      default: { document: { run: { font: FONT, size: BODY, color: NAVY } } },
      paragraphStyles: [
        { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: 30, bold: true, color: NAVY }, paragraph: { spacing: { before: 200, after: 240 }, outlineLevel: 0, keepNext: true } },
        { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: 25, bold: true, color: NAVY }, paragraph: { spacing: { before: 320, after: 160 }, outlineLevel: 1, keepNext: true } },
        { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: BODY + 1, bold: true, color: NAVY }, paragraph: { spacing: { before: 240, after: 120 }, keepNext: true } },
        { id: "TOC1", name: "toc 1", basedOn: "Normal", run: { font: FONT, size: 19, color: NAVY }, paragraph: { spacing: { after: 60 } } },
        { id: "TOC2", name: "toc 2", basedOn: "Normal", run: { font: FONT, size: 19, color: NAVY }, paragraph: { spacing: { after: 60 }, indent: { left: 240 } } },
      ],
    },
    numbering: { config: [{ reference: "bullets", levels: [
      { level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } },
      { level: 1, format: LevelFormat.BULLET, text: "o", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1440, hanging: 360 } } } },
      { level: 2, format: LevelFormat.BULLET, text: "▪", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 2160, hanging: 360 } } } },
    ] }] },
    sections: [
      { properties: { page: { ...page, margin: { top: 500, bottom: 500, left: 700, right: 700 } } }, children: cover(spec.meta) },
      { properties: { page }, footers: { default: footer }, children: [
        new Paragraph({ children: [new TextRun({ text: "Table of Contents", font: FONT, size: 26, bold: true, color: NAVY })], spacing: { after: 240 } }),
        new TableOfContents("Table of Contents", { hyperlink: true, headingStyleRange: "1-2" }),
        new Paragraph({ children: [new PageBreak()] }),
        ...docControl(spec),
        ...children,
      ] },
    ],
  });
  fs.writeFileSync(out, await Packer.toBuffer(doc));
  const report = qa(spec, warnings);
  console.log(JSON.stringify({ output: path.resolve(out), qa_issues: report.issues, open_tbcs: report.tbcs }, null, 2));
}
main().catch((e) => { console.error(e); process.exit(1); });
