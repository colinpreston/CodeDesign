# Package rules: how to pull them from the uploaded cost sheet

**This skill stores no cost sheet data.** No day rates, prices, days, rules or brand costings live in the skill, and none should ever be written into it, its examples or memory. Every figure and rule comes from the master costing sheet the user uploads **in this run**. If there's no sheet, ask for it.

## Why the rules matter
Each package tab in the master sheet prices a piece of work **on the condition that its rules hold**. Those rules protect Code when a brief turns out to be less simple than it sounded. So for every package a SoW uses:
- the package's **rules and assumptions** go into the SoW module as **assumptions**
- its **"additional cost" scenarios** go in as **change-request triggers** ("…would be a change request")
- a brief that **breaks** a rule is **unpriced scope**, so raise it: price it or exclude it

## Where to find them on a package tab
Read every package tab (the non-brand tabs that list standard items, e.g. new brand, new locale, forms, design tokens, PIM, dealer locator). Look for:
- a row or cell labelled **"Rules"**, and the lines under it, which may continue down column B
- a row labelled **"Assumptions"**, often naming who must do due diligence before the price is honoured
- a heading like **"Scenarios where the assumptions above are not adhered to will be additional costs"**, and the lines under it
- lines like **"Out of scope of …"** and **"Assumes …"**
- the **notes column** ("Enablers / notes / assumptions") on each item, e.g. who provides what, what must be signed off before build, "per endpoint", "case by case", "may not always be needed"
- **case-by-case items** with no fixed price (e.g. "tbc", "case by case"). These always need days from the Delivery Manager.
- **scenario / guidance tabs** (e.g. repo or multi-brand scenarios). These are rules about how a build must be structured and costed. Apply them, and flag any risks they mention.

Quote the rule's meaning in plain SoW language. Keep the package's conditions intact; don't soften them.

**Example of the conversion (illustrative only; take the real wording from the sheet):**
- Sheet rule: *"Dealer details are in the same format as [reference brand] dealers"*
- SoW assumption: "Dealer data will be supplied by HD in the same format as [reference brand] dealers."
- Sheet scenario: *"Any variance in how data is stored or displayed on the FE"*
- SoW change trigger: "Any variance in how dealer data is stored or displayed on the front end would be a change request."

## Delivery & QA
Brand tabs price delivery and QA in different ways. Read the method from the brand tab and mirror it. Don't assume one.
- as **days** (a "Delivery and QA" line)
- as **percentages** of the sub total (e.g. separate Delivery and QA lines "calculated at x%") → `{activity, percent}`
- as a **Delivery Lead at n days per week** × weeks, plus QA
- any combination of these

## Sheet quirks to watch for
- **Cost = people effort × day rate × days.** Read the day rate from the sheet; never assume it. In the SoW, "Days effort" = person-days (people × days).
- **"Total days effort" rows can be wrong.** Recompute days from the line items. Check "Sub Total" and "Total Project Costs" against the lines, and tell the user about any mismatch.
- **Percentage lines can produce pence.** Keep them.
- **An extra column** (often H) may hold an alternative-scenario value, and some tabs show two scenarios side by side. These are **open decisions**, so ask which applies.
- **Bottom-of-tab notes** like "To confirm", "Scenario to cost for" or "X not included" are open decisions or exclusions. Ask, or put them in Out of Scope.
- **Zero rows** with notes like "CMS", "HD to complete" or "Assume HD can do" are **HD responsibilities**. List them in the SoW as such.
- **Tabs marked old or removed** (in the tab name or title cell): ignore them unless the user says otherwise.

## Comparing sheets
If the user mentions a previous SoW or earlier sheet, compare only what they've uploaded **in this run**. Don't keep a copy of either.
