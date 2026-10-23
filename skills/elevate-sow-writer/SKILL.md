---
name: elevate-sow-writer
description: Turn a client brief plus the completed Elevate costing sheet into a detailed Hunter Douglas Statement of Work (Code-branded Word doc) and a list of scope clarifications for the client. Reconciles brief against costing, chases every cost driver, and only asks what's missing.
---

# Elevate SoW Writer

**The problem:** Code writes lots of SoWs for new Hunter Douglas website builds on the Elevate platform. The sites share infrastructure and a lot of features, but the differences drive cost: dealer locator, number of locales, languages, multi-language sites, imports, back-end integrations, how much the design tokens change. HD tend to make the work sound simple, and the missing detail turns up once the build has started. So the costing sheet (a shopping list of features and jobs) has to become a SoW that says **exactly** what Code will do, and nothing more.

**What this skill does:** the Delivery Manager uploads the **brief(s)** and the **completed costing sheet**. The skill reads both and builds a scope ledger. It reconciles the two, checks every cost driver, asks the Delivery Manager only what's genuinely missing, then produces:
1. **The SoW**: a Code-branded .docx in the house style (photo cover, navy #000050, navy table headers, aqua #93DFE3 totals, Code logo footer)
2. **Scope clarifications**: a Code-branded .docx of questions for HD, each with why it matters and the assumption the SoW makes if it isn't answered

The generator script writes the 70% of the SoW that's fixed boilerplate identically every time: warranty, governance, ceremonies, core dependencies, acceptance and appendix. Your job is the scope.

## Rules
- **Defensive scoping.** Every cost driver ends up confirmed (stated precisely, with numbers), assumed (a written assumption, plus a clarification for HD), or out of scope. Nothing stays vague. "In line with the current site" or "same as Hillarys" is never a scope statement on its own; name the reference implementation **and** list what it includes.
- **Quantify everything:** locales, languages, forms, endpoints, integrations, components, imports, redirects, PIM counts.
- **Never silently include unpriced work.** If the brief asks for it but the costing sheet doesn't price it, it's a scope risk. Raise it, and either get it priced or put it in Out of Scope.
- **The price is never `[TBC]`.** It comes from the costing sheet or the user. Don't build without it.
- Never invent prices, PO numbers, endpoints, URLs, dates or people. Ask. Use `[TBC: …]` only for details the user genuinely doesn't have yet. They're listed back at the end.
- The Delivery Manager owns the document. You draft; a human checks and signs off.
- British English, plain contractual tone, Code house wording.

## Files
- `references/cost-drivers.md`: **read first.** The 18 cost drivers, red-flag brief phrases, default assumptions, and the scope-ledger method
- `references/costing-map.md`: how to read the costing sheet and map its rows to scope modules and feature keys
- `references/modules.md`: house wording for every scope module, plus the out-of-scope feature keys
- `scripts/build_sow.js`: spec JSON → SoW .docx + clarifications .docx + QA report (needs the `docx` npm package)
- `examples/luxaflex-project.json`: rebuild of a signed SoW (days × rate)
- `examples/brightvale-test.json`: fictional multi-locale new brand from a brief + costing sheet, with costing refs and clarifications
- `assets/`: cover image and Code logos

---

## Step 1: Get the inputs

Ask for: *"Upload the brief (or briefs) and the completed costing sheet. A previous SoW for the same brand family helps too, if there is one."*

- **Brief + costing sheet** (the normal route): go to Step 2.
- **Costing sheet only:** go to Step 2, but expect more clarifications.
- **Brief only:** go to Step 2. The price must come from the user, and the scope must be priced before it's final, so say so.
- **Nothing to upload:** use the fallback intake questions (Appendix A) instead.
- **Several briefs/brands at once (batch):** run Steps 2–4 per brand, but ask shared questions once. Present the ledgers as one table (brand | locales | languages | key drivers | price | open questions).

## Step 2: Read and build the scope ledger

1. **Costing sheet:** follow `references/costing-map.md`. List every selected row with a `ref`, map it to a module and feature key, keep its notes, and note the total.
2. **Brief:** extract every fact against each of the 18 drivers in `references/cost-drivers.md`. Note every red-flag phrase ("simple", "same as…", "just", "etc.", "TBC", "phase 2"…).
3. **Ledger:** one row per driver or feature: *Driver | Brief says | Costing says | Status | Action*, where status is Match · Costed, not in brief · In brief, not costed · Vague · Conflict · Missing.

Show the ledger to the user as a compact table, with the problems first: conflicts, unpriced scope, vague items, missing drivers. This is the most valuable thing the skill does, because it's where the hidden detail comes out.

## Step 3: Resolve the gaps with the Delivery Manager

Ask only what the ledger couldn't answer. Use the AskUserQuestion tool for choices (max 4 questions per call, 2–4 options each) and one free-text message for details. Sort each open item into:

- **The Delivery Manager knows:** e.g. day rate, billing, team, whether a costed extra is intentional, the design-token change level. Ask now.
- **Only HD knows:** e.g. endpoints, dealer data format, redirect map, translations, import volumes, integration specs. Don't block on it. Write the default assumption from `cost-drivers.md` into the SoW and add a clarification for HD (area, question, why it matters, assumption).
- **Unpriced scope** (in brief, not costed): ask "Price it (update the costing sheet) or exclude it?" If excluded, it goes in Out of Scope `extras`. If priced, get the days or cost.
- **Conflicts:** always ask; never pick a side.

Always confirm: the price (fixed total or days per line), billing (PO number, or milestone months and amounts that add up to the total), the timing window, the people, and the version/date/author.

## Step 4: Write the spec

One JSON spec per SoW. Copy the shape of `examples/brightvale-test.json`:

```
meta:        version, date, author, brand, title, client, stakeholder_label, build_label,
             locales[] (one per locale; QA checks counts), allowed_brand_mentions[],
             acceptance_client, warranty_trigger
doc_control: versions[], distribution[]
costing:     [{ref, item, qty, days, cost, notes, status?:"out"}]   ← every selected costing row
sections[]:  Summary, Project Overview, Scope of work, Budget, Timing plan
  items:     {module, id, features:[keys], costing_refs:[refs], blocks:[...]}
             {out_of_scope:{in_scope:[keys], linked:[{key,ref}], extras:[...]}}
  budget:    {type:"budget", day_rate, fixed?, intro, lines:[{activity, bullets, days, cost, costing_refs}],
             total, billing:{po} | {milestones:[{label,value}]}}
governance:  delivery_manager, digital_consultant, client_team[[name,role]], code_team[[name,role,email]]
dependencies:   extra rows (HD-provided items + every assumption that carries cost risk)
clarifications: [{area, question, why, assumption}]   ← questions for HD
warranty:    false to drop it
```

Blocks: `"paragraph"` · `{bullets:[...]}` (nested arrays/`{text, sub}` for sub-bullets, `{text, detail}` for bold label + detail) · `{label}` · `{table:{columns,rows,total}}` · `{note}`. Inline: `**bold**`, `*italic*`, `[text](url)`, `{{ref:id}}`. Use `{{ref:id}}` for every cross-reference; never type section numbers.

Writing the scope:
- Use the house wording in `references/modules.md`. Add the **Locales & Languages** module whenever there's more than one locale or any multi-language locale.
- Each module says **what Code will do, with quantities**, ends with its **assumptions**, and carries the `costing_refs` of the rows that price it.
- Tag each module's `features`. **Out of Scope is derived** from the master list (everything not tagged), plus `extras` for brief items that were excluded or not priced. Always include anything the brief mentioned but isn't being delivered, so HD can see it was considered.
- Every assumption with cost risk also goes into `dependencies`, worded as "Assumption: …" or "Dependency: HD to provide …".
- Summary: the house opener; locales and URLs; one context sentence; the price sentence; the contact line.

## Step 5: Build and QA

```bash
node <skill-dir>/scripts/build_sow.js spec.json "Code_Hunter Douglas <Brand> SoW V<x.y> DRAFT.docx"
```

(If `require('docx')` fails, run `npm install docx`.) This writes the SoW and, if there are clarifications, `… - Scope clarifications.docx` next to it. It prints `qa_issues`, `open_tbcs` and `open_clarifications`.

**Fix every QA issue.** The checks:
- **costing ↔ scope**: a priced line not described in any module; a module pointing at a line that isn't in the costing sheet (unpriced scope); a line marked out but referenced
- a missing price, or missing milestone amounts
- arithmetic: days × rate, line sum, billing sum vs total, Summary total vs Budget total
- locale-count words that don't match `meta.locales`
- other HD brand names left over from a previous SoW
- the truncated "as agreed in the." sentence, "formerly kicked off", open questions left in scope text, unresolved references, duplicate out-of-scope items, mixed Code email domains, known misspellings

Then re-read the scope against the ledger yourself. Every driver should be confirmed, assumed or out. Render the .docx to PDF and look at the cover, scope and budget pages.

## Step 6: Deliver

- Save both .docx files into the user's working folder, in a `SoW drafts/` subfolder. If no folder is connected, send them as files.
- Reply with:
  - a one-line summary (brand, locales, price)
  - the scope risks you found (unpriced scope, conflicts, vague items) and what was decided
  - the number of clarifications for HD
  - the `[TBC]` items still open
- Suggest the Delivery Manager sends the clarifications to HD **before** the SoW, or with it, so assumptions are agreed before sign-off.
- Word fills in the table of contents when the document opens (accept "update fields"). The house font is WPP; machines without it substitute a sans-serif.

---

## Appendix A: Fallback intake (no brief or costing sheet)

Ask in rounds with AskUserQuestion:
1. **Shape:** How many SoWs (one · batch · one SoW for several locales) · Build type (new brand repo · new locale in existing repo · small brand/POC · brand + new components) · Design route (reuse tokens · light change · new token set · mock-ups provided) · Pricing (days × rate · fixed from pitch · fixed POC). **If fixed: ask the amount straight away.**
2. **Features:** Lead forms (Contact Us · Appointment · Consultation · Dealer locator) · Other forms (Email sign-up · Brochure/E-brochure · Samples · Embedded form) · Integrations (PIM · Bloomreach · Turnstile · Trustpilot) · More (Taps & Sources · GUID · Loqate · OneTrust via GTM)
3. **Changes and commercials:** Components (new · variant · linked · none) · Import/migration (none · content · products · images) · Traffic split (no · yes) · Billing (PO → number · milestones → months and amounts) · Warranty (include · exclude)
4. **Details (free text):** locales with URLs and languages; fonts; form endpoints per locale; dealer data; PIM counts; component briefs; integration systems; day rate and days per line; timing; people; version/date/author.

Then build the ledger from the answers and continue from Step 3.
