---
name: elevate-sow-writer
description: Draft Hunter Douglas Elevate website-build Statements of Work (new brands, locales or batches) as Code-branded Word documents. Asks the intake questions itself, then builds the .docx with standard modules, derived out-of-scope and a QA check.
---

# Elevate SoW Writer

Drafts Statements of Work for Hunter Douglas brand and locale builds on the Elevate platform (Prismic CMS, global component library, design-token governance). The output is a **Code-branded .docx** in the same style as the signed SoWs: photo cover, navy (#000050) text, navy table headers, aqua (#93DFE3) totals and acceptance rows, and the Code logo with a page number in the footer.

About 70% of every SoW is fixed boilerplate. The generator script writes that part identically every time: warranty, governance, ceremonies, core dependencies, acceptance and appendix. Your job is the variable part: intake, scope modules, budget and timing.

**Rules**
- The Delivery Manager owns the document. You draft; a human checks the commercials and signs off.
- Never invent prices, PO numbers, email endpoints, URLs, dates or named people. Ask for them. Only if the user genuinely doesn't have a detail yet, write `[TBC: what's needed]` and it will be listed back.
- **The price is never `[TBC]`.** For a fixed-cost SoW, ask for the amount and don't build until you have it. For days × rate, ask for the days per activity line. A SoW without a price can't go to the client.
- British English, plain contractual tone, Code house wording (see `references/modules.md`).

Files in this skill:
- `scripts/build_sow.js`: spec JSON → branded .docx + QA report (needs the `docx` npm package)
- `references/modules.md`: house wording for every scope module, plus the out-of-scope feature keys
- `assets/`: cover image and Code logos
- `examples/luxaflex-project.json`: a complete worked spec (rebuilds the signed Luxaflex Project SoW). Copy its shape.
- `examples/brightvale-test.json`: fictional multi-locale new brand on a fixed cost with milestone billing, a new component and derived out-of-scope

---

## Step 1: Intake (always ask; never skip)

Start with: *"Have you got the costing spreadsheet or a previous SoW for this one? Attach it and I'll pre-fill what I can."* If one is attached, read it, map every line to the questions below, and only ask what's still missing. Show the user what you pre-filled so they can correct it.

Then ask in these rounds. Use the AskUserQuestion tool where it's available (max 4 questions per call, 2–4 options each; users can always type "Other"). If it isn't available, ask the same questions as a numbered list in one message.

### Round 1: Shape of the job
1. **How many SoWs?** One brand/locale · A batch (several, one SoW each) · One SoW covering several locales
2. **Build type?** New brand (new Prismic repo) · New locale in an existing repo · Small brand / POC · Brand(s) with new components
3. **Design route?** Reuse existing tokens (no design work) · New tokens within agreed governance · HD owns look and feel, existing components only · Mock-ups already provided, token application only
4. **Pricing model?** Days × day rate breakdown · Fixed cost from pitch · Fixed cost POC, time tracked

**If either fixed-cost option is chosen, ask straight away, before Round 2:** *"What's the fixed cost (£, ex VAT)?"* This is a required answer, so keep asking until you have a number. Check it against the day rate (amount ÷ £670) and mention the equivalent days so the user can sanity-check it. If the pitch price doesn't divide evenly, that's fine; just say so.

### Round 2: Features (multi-select)
5. **Lead forms in scope?** Contact Us · Request an Appointment · Request a Consultation · Showroom / Dealer Locator
6. **Other forms in scope?** Email sign-up · Brochure / E-brochure · Samples · Embedded third-party form (Prismic slice)
7. **Integrations (1)?** Salsify PIM (+ PDP/PFG) · Bloomreach · Turnstile · Trustpilot
8. **Integrations (2)?** Taps & Sources · GUID site ID · Loqate postcode lookup · OneTrust via GTM (instead of Prismic)

### Round 3: Changes and commercials
9. **Component changes?** (multi) New Elevate component · Variant/update to an existing component · Linked, not rebuilt (e.g. calculator, dealer login) · None
10. **Traffic split at launch?** No, 100% at launch · Yes, Cloudflare load balancer
11. **Billing?** PO already raised · Milestone invoices
    - PO → ask for the PO number(s).
    - Milestones → ask for each month and amount. Offer a default split of the total (e.g. 50/50 across the build months) for them to confirm. The milestones must add up to the total.
12. **Warranty?** Include the standard 30-day warranty · Exclude (no dev work)

### Round 4: The details (one free-text message; list only what applies)
Ask for these together, tailored to the answers above:
- **Identity:** client entity (e.g. Hunter Douglas EU, Solskjerming AS) and who pays or recharges; brand(s); existing URLs; new URLs/paths; languages per locale
- **Design:** fonts per brand (purchased yet?); links to mock-ups or governance
- **Forms:** email endpoint per locale for each form; any new or removed fields; where submissions go (CSV per submission is the default)
- **PIM:** number of new categories, filters and specs
- **Components:** name, what it does, brief/requirements doc link
- **Commercials:** for days × rate, activity lines with days; day rate (default £670 = 23% rate-card discount, confirm it); timing window. The fixed amount, PO number and milestones should already be captured in Rounds 1 and 3; don't move on without them.
- **People:** HD core team (name + role); Code team (Tech Lead, Delivery Lead, Test Lead, Design) with emails on **one** domain; Delivery Manager; Digital Consultant; author, phone and email for the Summary
- **Doc control:** version, date, distribution list
- **Anything else** explicitly out of scope, or HD dependencies (scripts, keys, dealer DB, briefs)

For a batch, collect the shared answers once, then the per-brand differences as a table (brand | locales | URLs | fonts | endpoints | cost), and confirm the list before building.

---

## Step 2: Write the spec

Build one JSON spec per SoW, following `examples/luxaflex-project.json`. Key parts:

```
meta:        version, date, author, brand (cover small line), title (cover big line),
             client, stakeholder_label, build_label ("the Duette EU locale builds"),
             locales[] (one entry per locale — QA checks counts against this),
             allowed_brand_mentions[] (other HD brands legitimately referenced),
             acceptance_client, warranty_trigger, output (file name)
doc_control: versions[], distribution[]
sections[]:  in order: Summary, Project Overview, Scope of work, Budget, Timing plan
             (the script appends Warranty, Governance, Items of note, Acceptance, Appendix)
  blocks:    "paragraph" | {bullets:[...]} | {label:"..."} | {table:{columns,rows,total}} | {note:"..."}
  items:     {module:"Title", id, features:[keys], blocks:[...]}  → numbered x.1.n
             {sub:"Title", blocks}                                → numbered x.n
             {out_of_scope:{in_scope:[keys], linked:[{key,ref}], extras:[...]}}
  budget:    {type:"budget", day_rate, intro, lines:[{activity, bullets, days, cost}],
             total, fixed, billing:{po} | {milestones:[{label,value}]}}
governance:  delivery_manager, digital_consultant, client_team[[name,role]],
             code_team[[name,role,email]], ceremonies (optional override)
dependencies: extra rows only (the 3 standard rows are added automatically)
warranty:    false to drop the warranty section
```

Inline text supports `**bold**`, `*italic*`, `[text](url)` and `{{ref:id}}`. Use `{{ref:id}}` for every cross-reference so section numbers always resolve; never type a section number by hand.

**Out of scope is derived, not written.** Tag each scope module with its `features` keys (list in `references/modules.md`). Every master feature not tagged in scope appears in Out of Scope automatically, followed by the standard "Any variations…" line. For features that are linked rather than rebuilt, use `linked: [{key, ref}]` so the item reads "(see section 3.1.6)". Add brand-specific exclusions in `extras`.

Write the Summary, Overview and each scope module with the house wording in `references/modules.md`, adapted to this brand. Every in-scope form gets: which locales it applies to; standard Elevate look, fields, validation and tracking; Prismic CMS fields in line with the existing set-up; endpoints per locale; delivery method; and the PII sentence. Every new or changed component ends: "Once built and implemented this feature will be available to all HD brands", plus the brief link.

Add HD-side dependencies to `dependencies`, e.g. fonts purchased before token work; OneTrust script per domain (staging + prod); Turnstile keys; dealer database; Bloomreach FE/BE briefs; PIM hierarchy; embedded third-party JS/CSS clash risk.

---

## Step 3: Build

```bash
node <skill-dir>/scripts/build_sow.js spec.json "Code_Hunter Douglas <Brand> SoW V<x.y> DRAFT.docx"
```

(If `require('docx')` fails, run `npm install docx` first.) The script prints JSON with `qa_issues` and `open_tbcs`.

**Fix every QA issue before delivering.** A missing price is a QA failure, not a TBC. It checks for:
- a missing price (fixed total or line costs not given as numbers) or missing milestone amounts
- arithmetic (days × rate, line sum, billing sum vs total)
- locale-count words that don't match `meta.locales`
- other HD brand names left over from a previous SoW
- the truncated "as agreed in the." sentence
- "formerly kicked off"
- open questions left in scope text
- unresolved references
- duplicate out-of-scope items
- mixed Code email domains
- known misspellings

Then do a quick read-through yourself for anything the script can't catch, such as a locale missing from a bullet list.

Render the .docx to PDF and look at a few pages (cover, scope, budget) to check the layout before you hand it over.

---

## Step 4: Deliver

- Save the .docx into the user's working folder, in a `SoW drafts/` subfolder. If no folder is connected, send it as a file.
- Batch: one .docx per SoW plus a short summary table in the reply (brand | locales | total | billing | open TBCs).
- Finish with: QA result (clean, or what you fixed), the list of `[TBC]` items still open, and any assumptions you made.
- The table of contents is a Word field. Word fills it in when the document opens (accept "update fields"). If it shows blank, right-click it and choose Update Field.
- The house font is WPP. On a machine without it installed, Word substitutes a sans-serif until it's opened on a WPP machine.
