# Reading the costing sheet

The delivery team's costing sheet is a shopping list: one row per feature or job, with a selection marker, quantity, days and/or cost. Layouts vary, so read it like this:

1. Open every sheet/tab (pandas or openpyxl; keep formulas' computed values). Find the header row: look for columns like *Item / Feature / Activity / Description*, *Qty / Include / Y/N / Selected*, *Days / Effort*, *Rate*, *Cost / Total*, *Notes / Assumptions*.
2. A row is **selected** if it has any of: Include = Y / Yes / ✓ / TRUE / 1, a quantity > 0, days > 0, or cost > 0. Rows with blank or zero values are **not selected**: they're candidates for Out of Scope.
3. Give each selected row a `ref` (sheet row number, or its own ID column if there is one) and record it in the spec's `costing` list: `{ ref, item, qty, days, cost, notes }`. Unselected rows that match a master out-of-scope feature can be listed with `status: "out"`.
4. Keep the **Notes** column. It often carries the detail (endpoints, locales, "same as Hillarys") that belongs in the scope text or the clarifications.
5. Map each row to a scope module and feature key using the table below. Put the row's `ref` in that module's `costing_refs`, so the QA can check that **every priced line is described in scope, and every scope module is priced**.
6. Totals: if the sheet has a total, it's the SoW price, so confirm it with the user. If it's days-based, check days × rate per line and say if anything doesn't add up.

If the sheet has a row that doesn't fit any module, write a module for it from the row and notes, and raise it with the user.

## Keyword → module / feature key

| Sheet wording (examples) | Scope module | Feature key(s) |
|---|---|---|
| repo, Prismic set-up, pipelines, environments, CI/CD, infra, Cloudflare | Prismic Setup & Infrastructure | — |
| new locale, locale set-up, additional locale | Prismic Setup & Infrastructure (+ locale list) | — |
| language, translation, multi-language, language switcher, hreflang | Locales & Languages | — |
| design tokens, theming, brand application, fonts | Design activities | design_tokens |
| page designs, wireframes, templates, UX | Design activities | page_designs |
| new component, component build, variant, header, nav, banner | New / updated Elevate component | — |
| contact form, contact us | Forms | contact_us |
| appointment, book appointment, consultation | Forms | request_appointment / request_consultation |
| brochure, e-brochure | Forms | request_brochure / request_ebrochure |
| email sign up, newsletter | Forms | email_signup |
| samples, swatches, Maxlead | Forms | samples |
| generic form, simple form, embedded form | Forms | — |
| dealer locator, store finder, showroom, map | Dealer / Showroom Locator | dealer_locator |
| PIM, Salsify, products, PDP, PFG, filters, specs, categories | PIM integration | salsify_pim, pdp, pfg |
| Bloomreach, CDP, marketing automation | Bloomreach | bloomreach |
| CRM, sales app, lead management, API integration | Back-end integration | — |
| Live Diary, booking engine | Back-end integration | live_diary |
| Infinity, call tracking | Analytics & Compliance | infinity |
| Trustpilot, reviews | Trustpilot | trustpilot |
| Turnstile, captcha | Forms | turnstile |
| analytics, GTM, tracking, OneTrust, cookies, GUID | Analytics & Compliance | guid |
| taps and sources | Taps and Sources | taps_sources |
| import, migration, content migration, image migration, product import | Import & Migration | content_migration / image_migration |
| redirects, 301s, SEO | Redirects & SEO | seo |
| load balancer, traffic split | Prismic Setup & Infrastructure | — |
| QA, testing, automation, smoke tests | Budget line: Delivery & QA | — |
| delivery, project management, ceremonies | Budget line: Delivery & QA | — |

> Update this table once the real costing sheet has been read, so the row names match exactly.
