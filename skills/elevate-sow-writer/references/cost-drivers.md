# Cost drivers: what every Elevate SoW must pin down

Hunter Douglas briefs often make the work sound simpler than it is. Detail gets missed and turns up mid-build as "small" extras. Each driver below changes the cost. **Every driver must end up in one of three states before the SoW goes out:**

1. **Confirmed:** the brief or the costing sheet states it, so the SoW states it precisely (with numbers).
2. **Assumed:** nobody knows yet, so the SoW states a written assumption and the question goes on the clarifications list for HD.
3. **Out of scope:** not wanted or not priced, so it goes in Out of Scope.

Nothing is allowed to stay vague. Each package price in the master costing sheet also depends on **rules** (see `package-rules-method.md`). Check the brief against them, because a brief that breaks a rule means additional cost. "In line with the current site" is not a scope statement.

## Red-flag phrases in briefs
When you see these, treat the item as **not yet defined**: write a precise scope line plus an assumption, and raise a clarification.

"simple" · "just" · "basic" · "quick" · "same as [brand]" · "like the current site" · "standard" · "a few" · "some" · "etc." · "and so on" · "TBC" · "phase 2" · "nice to have" · "if possible" · "should be easy" · "we'll send over later" · "the usual" · "all the forms" · "all the pages" · "migrate everything" · "integrate with our system"

---

| # | Driver | What the SoW must state | Ask if missing | Default assumption if HD can't answer yet |
|---|---|---|---|---|
| 1 | **Locales** | Number of locales; existing URL → new URL/path for each; domain vs subfolder | How many locales, and what are the URLs? | Only the locales listed are in scope; each extra locale is a change request |
| 2 | **Languages** | Languages per locale; which locales are **multi-language** (e.g. CH DE/FR, BE NL/FR); language switcher; hreflang | Which languages does each locale need? | One language per locale unless listed; translated content supplied by HD |
| 3 | **Content & translation** | Who writes, translates and loads content; Code builds no content unless stated | Who's supplying and loading content in each language? | HD content editors create and load all content and translations in Prismic |
| 4 | **Repo** | New Prismic repo, or new locale in an existing repo | Is this a new brand repo or a locale of an existing brand? | (must be confirmed, as it changes infra effort) |
| 5 | **Design tokens** | Change level: **none** (reuse existing) · **light** (colour/font swap within existing tokens) · **new token set** · **component variants**; fonts and licence status | How different is the look from [parent brand]? Are fonts bought? | New token set within existing governance; no new components or variants; fonts purchased by HD before token work |
| 6 | **Page designs** | None · mock-ups already provided · Code to design (number of templates) | Do you need page designs, or will the team build from existing components? | No page designs or wireframes; HD selects components |
| 7 | **Forms** | Each form by name; locales it applies to; field changes vs the standard Elevate form; endpoint per locale; delivery method; postcode lookup; Turnstile | Which forms, on which locales, and where does each submission go? | Standard Elevate form fields and behaviour; one email endpoint per locale; password-protected CSV per submission |
| 8 | **Dealer / showroom locator** | Map view; dealer data source and format; who maintains it and how often; dealer types; appointment-from-locator; filters | Is there a dealer locator? Where does the dealer data come from and in what format? | Standard Elevate locator journey (as on Luxaflex); HD supplies the dealer database in the existing format; no new filters or dealer types |
| 9 | **Back-end integrations** | Each system by name (Salsify PIM, Bloomreach, sales/CRM app, Maxlead samples, Live Diary, Infinity, dynamic Trustpilot); direction of data; who provides spec, endpoints and keys per environment | Which back-end systems must the site send data to or read from? | Only the integrations listed; HD provides briefs, endpoints and keys for each environment before ticket scoping |
| 10 | **PIM** | Brand record, locales; counts of new categories, filters and specs; PDP/PFG templates; data in the expected structure | How many new categories, filters and specs? Is the product data in Salsify already? | Products exist in Salsify in the structure Elevate expects; only the stated counts are configured |
| 11 | **Import / migration** | What's imported (pages, images, products, dealers, blog), roughly how much, the method (automated / scripted / manual) and who does it | Does anything need importing from the current site? Roughly how much? | No content, image or product migration by Code; HD content editors rebuild pages in Prismic |
| 12 | **Redirects & SEO** | 301 redirect map, who supplies it, how many; any SEO activity | Who's producing the redirect map from old URLs to new? | HD supplies the redirect map; Code implements it via existing Cloudflare config; no SEO activity |
| 13 | **New / changed components** | Each one by name; brief link; becomes available to all brands | Is there a brief for this component? | Built to the brief provided; available to all brands; no other component changes |
| 14 | **Linked, not rebuilt** | Features kept on existing systems and linked from the new site (calculator, dealer login, brochure via dealer portal) | Are any features staying on their current systems? | Linked via CMS by HD content editors; not rebuilt |
| 15 | **Analytics & consent** | GTM, OneTrust per domain (staging + prod), GUID site ID, taps & sources, form tracking | Who's providing the OneTrust scripts and the GTM container? | Analytics in line with the existing Elevate implementation; HD provides OneTrust scripts per domain |
| 16 | **Launch approach** | 100% or traffic split (Cloudflare LB); all locales together or staggered | Will all locales launch together, at 100%? | All locales launch together at 100%; no load balancer |
| 17 | **Testing & automation** | Automation level (e.g. P1/P2 smoke tests), browsers and devices, UAT owner | — | Standard Elevate automation and test coverage; HD performs UAT in line with the delivery plan |
| 18 | **Commercials** | Fixed price or days × rate; billing (PO or milestones); timing window | (always ask; never `[TBC]`) | none: a price is mandatory |

## Reconciling the brief with the costing sheet
Build a **scope ledger**, with one row per driver or feature:

| Driver / feature | Brief says | Costing sheet says | Status | Action |
|---|---|---|---|---|

Statuses:
- **Match:** the brief and the costing sheet agree. Write it into scope.
- **Costed, not in brief:** confirm with the Delivery Manager that it's wanted (it may be a sensible inclusion the brief forgot), then write it in.
- **In brief, not costed:** a **scope risk**. Either it gets priced (back to the costing sheet) or it goes explicitly into Out of Scope. Never silently include it.
- **Vague:** a red-flag phrase or a missing quantity. Write a precise line plus an assumption, and raise a clarification.
- **Conflict:** the brief and the costing sheet disagree (e.g. brief says 3 locales, sheet prices 2). Stop and ask the Delivery Manager.
