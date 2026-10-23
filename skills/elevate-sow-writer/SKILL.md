---
name: elevate-sow-writer
description: Turn a client brief plus the master Elevate costing sheet (brand tab + package rules) into a detailed Hunter Douglas Statement of Work (Code-branded Word doc) and a list of scope clarifications for the client. Reconciles brief against costing, chases every cost driver, and only asks what's missing.
---

# Elevate SoW Writer

**The problem:** Code writes lots of SoWs for new Hunter Douglas website builds on the Elevate platform. The sites share infrastructure and a lot of features, but the differences drive cost: dealer locator, number of locales, languages, multi-language sites, imports, back-end integrations, how much the design tokens change. HD tend to make the work sound simple, and the missing detail turns up once the build has started. So the costing sheet (a shopping list of features and jobs) has to become a SoW that says **exactly** what Code will do, and nothing more.

**What this skill does:** the Delivery Manager uploads the **brief(s)** and the **master costing sheet** (*Elevate_Package_of_Work_Costings.xlsx*: package tabs that act as a price book with rules, plus one completed tab per brand). The skill reads both and builds a scope ledger. It reconciles the two, checks every cost driver, asks the Delivery Manager only what's genuinely missing, then produces:
1. **The SoW**: a Code-branded .docx in the house style (photo cover, navy #000050, navy table headers, aqua #93DFE3 totals, Code logo footer)
2. **Scope clarifications**: a Code-branded .docx of questions for HD, each with why it matters and the assumption the SoW makes if it isn't answered

The generator script writes the 70% of the SoW that's fixed boilerplate identically every time: warranty, governance, ceremonies, core dependencies, acceptance and appendix. Your job is the scope.

## Rules
- **Defensive scoping.** Every cost driver ends up confirmed (stated precisely, with numbers), assumed (a written assumption, plus a clarification for HD), or out of scope. Nothing stays vague. "In line with the current site" or "same as Hillarys" is never a scope statement on its own; name the reference implementation **and** list what it includes.
- **Quantify everything:** locales, languages, forms, endpoints, integrations, components, imports, redirects, PIM counts.
- **Never silently include unpriced work.** If the brief asks for it but the costing sheet doesn't price it, it's a scope risk. Raise it, and either get it priced or put it in Out of Scope.
- **The price is never `[TBC]`.** It comes from the costing sheet or the user. Don't build without it.
- Never invent prices, PO numbers, endpoints, URLs, dates or people. Ask.
- **Store no cost sheet data.** The skill holds no day rates, prices, days, package rules or brand costings. Always ask for the master costing sheet and read it fresh in every run. Never write its figures or rules back into the skill, its examples, memory or any file other than the SoW being produced.
- **Personal details always come from the person creating the SoW.** Ask for them in every run, and never copy names, phone numbers or emails from the examples, a previous SoW or the costing sheet. The examples deliberately use placeholders.
- **Ask about every `[TBC]`.** Before building, collect every detail you'd otherwise mark `[TBC]` and ask the user for it. A `[TBC]` may stay in the SoW only if the user says it isn't known yet; record it in `unknown_tbcs`, and it's listed back at the end.
- The Delivery Manager owns the document. You draft; a human checks and signs off.
- British English, plain contractual tone, Code house wording.

## Files
- `references/cost-drivers.md`: **read first.** The 18 cost drivers, red-flag brief phrases, default assumptions, and the scope-ledger method
- `references/costing-map.md`: how to read the master costing sheet (package tabs vs brand tabs, columns, zero/HD-owned rows, bottom notes) and map its rows to scope modules and feature keys
- `references/package-rules-method.md`: how to pull the rules, assumptions and "additional cost" scenarios out of the uploaded sheet's package tabs, and turn them into SoW assumptions and change-request triggers. It also covers Delivery & QA methods and sheet quirks. (It contains no figures or rules itself.)
- `references/modules.md`: house wording for every scope module, plus the out-of-scope feature keys
- `scripts/build_sow.js`: spec JSON → SoW .docx + clarifications .docx + QA report (needs the `docx` npm package)
- `examples/brightvale-test.json`: a **fictional** brand, showing the spec shape: costing refs, people × days, milestones and clarifications. Its rate, days and people are dummy values, not real costs. Never reuse its numbers.
  (It sets `"example": true`, which skips the personal-details and TBC checks. Never set it on a real SoW.)
- `assets/`: cover image and Code logos

---

## Step 1: Get the inputs

**First question, every time:**
> *"Please upload the latest master costing sheet (Elevate_Package_of_Work_Costings.xlsx). I don't keep a copy, so I need it each time to use the current prices and package rules. Is it the most up-to-date version?"*

- **Don't go further without the sheet.** If the user can't upload it, explain that the skill can't price or apply the package rules without it. Offer to wait, or to draft the scope only, with every price and rule marked for the Delivery Manager to fill in. A scope-only draft never goes to the client.
- Once it's uploaded, list its tabs back briefly (package tabs, brand tabs, any scenario/guidance tabs, and tabs marked old or removed) and confirm the user has the latest version.

Then ask for: *"Upload the brief (or briefs), and tell me which brand tab this is for. A previous SoW for the same brand family helps too, if there is one."*

- **Brief + costing sheet** (the normal route): go to Step 2.
- **Costing sheet only:** go to Step 2, but expect more clarifications.
- **Brief + master sheet but no brand tab yet:** propose a draft costing from the package tabs (see `costing-map.md` → *Building a costing from the price book*) and get the Delivery Manager to approve it before anything else.
- **Brief only (no sheet):** ask for the sheet (see above). Don't price from memory or from earlier runs.
- **Nothing to upload:** use the fallback intake questions (Appendix A) instead.
- **Several briefs/brands at once (batch):** run Steps 2–4 per brand, but ask shared questions once. Present the ledgers as one table (brand | locales | languages | key drivers | price | open questions).

### Personal details (ask in every run)
Ask the person creating the SoW for these, in one free-text message. Offer to reuse what they gave earlier in the same conversation, but never anything from the examples or old SoWs:
- **Author:** name (cover, document control)
- **Contact for the Summary line:** name, role, phone, email
- **Delivery Manager** and **Digital Consultant:** names
- **Code core team:** name, role and email for each (Technical Lead, Delivery Lead, Test Lead, Design…), on one email domain
- **HD core team:** name and project role for each
- **Distribution list:** name and company
- **Signatories** for acceptance, if known (the signature blocks are left blank for signing)

Set `people_confirmed: true` in the spec only once the user has supplied or confirmed these.

## Step 2: Read and build the scope ledger

1. **Costing sheet:** follow `references/costing-map.md`. On the brand tab, list every selected row (cost > 0) with a `ref` (`<tab>!<row>`), people × days and cost. Map each to a module and feature key, and keep its notes. Note the zero rows that HD owns, the Delivery & QA method, the **Total Project Costs**, and any bottom notes ("To confirm", "Scenario to cost for"). For each package used, pull its rules, assumptions and additional-cost scenarios from that **package tab in the uploaded sheet** (method in `references/package-rules-method.md`).
2. **Brief:** extract every fact against each of the 18 drivers in `references/cost-drivers.md`. Note every red-flag phrase ("simple", "same as…", "just", "etc.", "TBC", "phase 2"…).
3. **Ledger:** one row per driver or feature: *Driver | Brief says | Costing says | Status | Action*, where status is Match · Costed, not in brief · In brief, not costed · Vague · Conflict · Missing.

Show the ledger to the user as a compact table, with the problems first: conflicts, unpriced scope, vague items, missing drivers. This is the most valuable thing the skill does, because it's where the hidden detail comes out.

## Step 3: Resolve the gaps with the Delivery Manager

Ask only what the ledger couldn't answer. Use the AskUserQuestion tool for choices (max 4 questions per call, 2–4 options each) and one free-text message for details. Sort each open item into:

- **The Delivery Manager knows:** e.g. day rate, billing, team, whether a costed extra is intentional, the design-token change level. Ask now.
- **Package rules that the brief breaks:** e.g. dealer data not in Luxaflex format, a journey that differs from Luxaflex, new form fields, products outside the 3-tier taxonomy, a new locale that looks different from the base brand. These are **additional cost**. Treat them as unpriced scope: price it or exclude it.
- **Open scenarios on the brand tab** (column H alternatives, "Scenario to cost for", e.g. Code import vs HD import with Code support): ask which applies.
- **Only HD knows:** e.g. endpoints, dealer data format, redirect map, translations, import volumes, integration specs. Don't block on it. Write the default assumption from `cost-drivers.md` into the SoW and add a clarification for HD (area, question, why it matters, assumption).
- **Unpriced scope** (in brief, not costed): ask "Price it (update the costing sheet) or exclude it?" If excluded, it goes in Out of Scope `extras`. If priced, get the days or cost.
- **Conflicts:** always ask; never pick a side.

Always confirm: the price (fixed total or days per line), billing (PO number, or milestone months and amounts that add up to the total), the timing window, the personal details above, and the version and date.

**Then sweep for `[TBC]`s.** List every detail still unknown, e.g. fonts, email endpoints, URLs, brief links, invoice months, timing, PIM counts, people. Ask the user for all of them in one message (AskUserQuestion where the answer is a choice). Fill in what they give you. Put anything they say isn't known yet into `unknown_tbcs`, using the exact `[TBC: …]` text, and ask whether it should also go to HD as a clarification.

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
  budget:    {type:"budget", day_rate, fixed?, intro, sheet_total (brand tab Total Project Costs),
             lines:[{activity, bullets, people?, days, cost?, costing_refs} | {activity, percent}],
             total?, billing:{po} | {milestones:[{label,value}]}}
             (cost = people × days × rate; "Days effort" shows person-days; percent lines are calculated on the sub total)
contact:     {name, role, phone, email}   ← from the user; fills "{{contact}}" in the Summary
people_confirmed: true                    ← only after the user has given/confirmed the personal details
unknown_tbcs: ["[TBC: …]", …]            ← TBCs the user has said aren't known yet
governance:  delivery_manager, digital_consultant, client_team[[name,role]], code_team[[name,role,email]]
dependencies:   extra rows (HD-provided items + every assumption that carries cost risk)
clarifications: [{area, question, why, assumption}]   ← questions for HD
warranty:    false to drop it
```

Blocks: `"paragraph"` · `{bullets:[...]}` (nested arrays/`{text, sub}` for sub-bullets, `{text, detail}` for bold label + detail) · `{label}` · `{table:{columns,rows,total}}` · `{note}`. Inline: `**bold**`, `*italic*`, `[text](url)`, `{{ref:id}}`. Use `{{ref:id}}` for every cross-reference; never type section numbers.

Writing the scope:
- Use the house wording in `references/modules.md`. Add the **Locales & Languages** module whenever there's more than one locale or any multi-language locale.
- Each module says **what Code will do, with quantities**, ends with its **assumptions**, and carries the `costing_refs` of the rows that price it.
- **Carry each package's rules into its module as assumptions**, and its "additional cost" scenarios as change-request statements (wording in `package-rules-method.md`). Use the sheet's own wording each time. For example, a rule that dealer data must match a reference brand's format becomes "Dealer data will be supplied in the same format as [reference brand] dealers", and its additional-cost scenario becomes "… would be a change request".
- Zero rows the brand tab marks as HD's (SEO via CMS, product import into Salsify, image migration if HD does it) go in the module or Overview as **HD responsibilities**.
- Tag each module's `features`. **Out of Scope is derived** from the master list (everything not tagged), plus `extras` for brief items that were excluded or not priced. Always include anything the brief mentioned but isn't being delivered, so HD can see it was considered.
- Every assumption with cost risk also goes into `dependencies`, worded as "Assumption: …" or "Dependency: HD to provide …".
- Summary: the house opener; locales and URLs; one context sentence; the price sentence; and the contact line, written as "If you have any questions on this document, please contact {{contact}}." (filled from `contact`).

## Step 5: Build and QA

```bash
node <skill-dir>/scripts/build_sow.js spec.json "Code_Hunter Douglas <Brand> SoW V<x.y> DRAFT.docx"
```

(If `require('docx')` fails, run `npm install docx`.) This writes the SoW and, if there are clarifications, `… - Scope clarifications.docx` next to it. It prints `qa_issues`, `open_tbcs` and `open_clarifications`.

**Fix every QA issue.** The checks:
- **costing ↔ scope**: a priced line not described in any module; a module pointing at a line that isn't in the costing sheet (unpriced scope); a line marked out but referenced
- **personal details not confirmed** (`people_confirmed` missing), or **any `[TBC]` not asked** (not listed in `unknown_tbcs`). Go back to the user, then rebuild
- a missing price, or missing milestone amounts; a budget total that differs from the costing sheet's Total Project Costs
- arithmetic: people × days × rate, line sum, percentage lines, billing sum vs total, Summary total vs Budget total
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
  - the `[TBC]` items the user said aren't known yet (from `unknown_tbcs`), and who needs to supply each
- Suggest the Delivery Manager sends the clarifications to HD **before** the SoW, or with it, so assumptions are agreed before sign-off.
- Word fills in the table of contents when the document opens (accept "update fields"). The house font is WPP; machines without it substitute a sans-serif.

---

## Appendix A: Fallback intake (sheet uploaded, but no brief)

Use this when the costing sheet is in but there's no brief. It still needs the sheet: never run it without one. Ask in rounds with AskUserQuestion:
1. **Shape:** How many SoWs (one · batch · one SoW for several locales) · Build type (new brand repo · new locale in existing repo · small brand/POC · brand + new components) · Design route (reuse tokens · light change · new token set · mock-ups provided) · Pricing (from the brand tab · fixed price · draft from the package tabs). **If fixed: ask the amount straight away.**
2. **Features:** Lead forms (Contact Us · Appointment · Consultation · Dealer locator) · Other forms (Email sign-up · Brochure/E-brochure · Samples · Embedded form) · Integrations (PIM · Bloomreach · Turnstile · Trustpilot) · More (Taps & Sources · GUID · Loqate · OneTrust via GTM)
3. **Changes and commercials:** Components (new · variant · linked · none) · Import/migration (none · content · products · images) · Traffic split (no · yes) · Billing (PO → number · milestones → months and amounts) · Warranty (include · exclude)
4. **Details (free text):** locales with URLs and languages; fonts; form endpoints per locale; dealer data; PIM counts; component briefs; integration systems; timing; version/date. Personal details come from the *Personal details* step.

Then build the ledger from the answers and the sheet, and continue from Step 3.
