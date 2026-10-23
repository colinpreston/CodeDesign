# Reading the master costing sheet

The delivery team's master sheet (**Elevate_Package_of_Work_Costings.xlsx**) has two kinds of tab:

1. **Package tabs (the price book):** standard work packages, e.g. new brand, new locale, form submissions, design tokens, Salsify PIM, dealer locator. These hold standard items with people, days and cost, **plus the rules and "additional cost" scenarios** that the prices depend on. See `package-rules-method.md` for how to pull them out.
2. **Brand tabs (completed costings):** one per brand, usually named after it. Each is the package items selected for that brand. **This is the SoW's costing.**

Other tabs: scenario or guidance tabs (e.g. repo / multi-brand scenarios) are rules to apply. Tabs marked old or removed should be ignored unless the user says otherwise.

**Store nothing.** Read the sheet fresh in every run. Never copy its figures, rules or brand costings into the skill, its examples or memory.

## How to read it
1. Open with openpyxl `data_only=True` to get computed values. Open again with `data_only=False` if you need to see formulas.
2. Ask which **brand tab** this SoW is for, or match it from the brief or the tab's title cell (A1 usually holds the brand and URL). If there's no brand tab yet, see *Building a costing from the price book* below.
3. Columns: **B** item · **C** people effort · **D** day rate · **E** days · **F** cost (= C × D × E) · **G** enablers / notes / assumptions · **H** (sometimes) alternative-scenario days. Some tabs are shifted (e.g. Dealer Locate has two scenarios side by side in C–F and G–J). Read the header row (*People Effort / Day Rate / Days effort / Costs / Enablers…*) to locate the columns.
4. Rows:
   - a **section heading** has text in B and no numbers (e.g. "Prismic pipelines & infrasture", "DL and forms submissions", "Analytics", "SEO activity", "PIM", "Locale")
   - a **line item** has an item and numbers. **Selected = cost > 0** (or days > 0).
   - a **zero line** is either not in scope, or owned by HD. A note like "CMS", "HD to complete" or "Assume HD can do" means **HD's responsibility**, so say so in the SoW. A note like "Potential to remove" means it's been removed from scope.
   - **Total / Sub Total / Total Project Costs** rows: recompute and check them (see *Sheet quirks* in `package-rules-method.md`)
   - **bottom notes:** "To confirm", "Scenario to cost for", "X not included" are **open decisions or exclusions**. Ask the Delivery Manager, or write them into Out of Scope.
5. Give each selected line a `ref` of **`<tab>!<row>`** (e.g. `BrandTab!21`) and record it in the spec's `costing` list: `{ref, item, people, days, cost, notes}`. Record HD-owned and excluded zero lines with `status: "out"` when they matter (SEO items, image migration, Bloomreach, Turnstile…).
6. Delivery & QA: copy the brand tab's method (days, percentages or Delivery Lead weeks) into the budget. Percentage lines → `{activity, percent}`.
7. Set `budget.sheet_total` to the tab's **Total Project Costs**. QA flags any difference.

## Building a costing from the price book (no brand tab yet)
If there's a brief but no brand tab yet, the skill can **propose** a costing from the package tabs:
- **New brand:** *Elevate new brand* infra + analytics + automation; Design Tokens (new brand); plus Forms, PIM and Dealer Locate items as the brief needs
- **Each extra locale:** the new-locale package total, as long as the tab's rule holds (the locale is the same as the base brand)
- **Delivery & QA:** use the method most recent brand tabs in the uploaded sheet use, and ask the Delivery Manager to confirm it

Present it as a **draft costing for the Delivery Manager to approve**: a table of package, item, people × days, cost and rule assumptions. Never present it as the price until they've confirmed it. Anything in the brief that the price book doesn't cover (new components, CRM integrations, new form fields, content migration beyond images) is **case by case**: ask for days.

## Row name → SoW module / feature key

| Sheet row (as written) | SoW module | Feature key |
|---|---|---|
| Prismic repo instance · Pipeline configuration · Infra configuration · Cloudflare configuration | Prismic Setup & Infrastructure | — |
| Prismic locale configuration | Prismic Setup & Infrastructure + Locales & Languages | — |
| Second / Third / Fourth locale – XX ("costs taken from locale tab") | Locales & Languages | — |
| Automation testing (P1 and 2 – smoke tests, gtm, cookies and site iD) | Prismic Setup & Infrastructure (Automation) | — |
| Designs of new pages / Design of new pages – as is | Design activities (HP, 1 PLP + component recommendations) | page_designs |
| Design token application of global component library / of components needed | Design activities | design_tokens |
| Duplication of design token system / Copy of existing design token code base | Design activities | design_tokens |
| Image migration IF Code do / Image migration | Import & Migration (images) | image_migration |
| Image migration support IF HD do the work | Import & Migration (support only; HD migrates) | — (add "Image migration (Code support only)" text) |
| FE Dealer Locate APF · DL Design token application · DL Create and configure Prismic Finder page and slice | Dealer / Showroom Locator | dealer_locator |
| Dealer locate – dealer import (Code doing full import) / SUPPORT only | Dealer / Showroom Locator (import responsibility) | dealer_locator |
| Front end form – to email integration contact us / Contact Us | Forms: Contact Us | contact_us |
| OAR – to one endpoint | Forms: Request an Appointment (OAR) | request_appointment |
| Live Diary – to one endpoint | Forms: Live Diary appointment booking | live_diary |
| Request a Brochure / Request an e-brochure | Forms | request_brochure / request_ebrochure |
| Request a Consultation | Forms | request_consultation |
| Email Sign up | Forms | email_signup |
| Samples | Forms: Samples | samples |
| Showroom locator – adding form | Forms + Dealer locator | request_appointment |
| Turnstile | Forms | turnstile |
| Customer Data Portal – backend hook up (/ SUPPORT only) · CDP to email integration | Forms: Customer Data Portal | — |
| PII – create new storage container | Forms: PII storage | — |
| Bloomreach / Forms > Bloomreach | Bloomreach | bloomreach |
| Implement existing T&S | Taps and Sources | taps_sources |
| Data layer CMS version · Cookie consent – one trust · Guid site ID | Analytics & Compliance | guid |
| Build site map · schema · noindex · 400/500 error pages · offline page · breadcrumbs · hreflang · robots.txt | **HD responsibility** (SEO via CMS) | seo (out) |
| Create a brand record / Assign locales / Create product pages / Create filter records · Systems health check · PIM changes | PIM integration | salsify_pim, pdp, pfg |
| Import products into Salsify – HD | PIM: HD responsibility | — |
| Vis app to locales | Vis app | vis_app |
| Sitespect implementation | Sitespect | sitespect |
| Delivery / QA / Delivery Lead / Delivery and QA | Budget: Delivery & QA | — |
| anything else (e.g. new component, API translation layer, BE admin tool) | its own module from the row and notes | — |
