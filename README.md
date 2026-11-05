# design-studio-team-setup

A Claude plugin for Colin Preston. Sets up a "company brain + desks" pattern for a new design consultancy client engagement: one shared Project Brain, a roster of role "desks" each with a one-page brief and a memory log structured in three zones (Active Notes / Digest / Archive) so it stays usable as the engagement grows, a shared project-level research repository built the same way, a standing Digest Index that rolls up every desk's current Digest into one page for a step-back read, a retrieval mode (RAG-style: search, then answer only from what's found and cite the source) for specific questions rather than routine work, a Delivery Manager that both reacts (status checks, stalled-handoff spotting) and proactively routes new multi-desk work (sequencing who's needed and in what order from the roster's dependency graph, before anyone starts), a visual desk-status dashboard, and a Colin send/edit/skip review gate.

Default roster (eleven desks): Lead UX Designer, Lead UX Researcher, Expert Workshop Facilitator, Product Consultant, Engineering Principal, QA & Definition Lead, Content/UX Writer, Visual/Brand Designer, Data & Insight Analyst, Meeting Notes Lead, and Delivery Manager — plus whatever additional specialists a given engagement needs.

Bundles eight more skills:

- `cx-journey-map` — builds Code's "customer journey full detail" CX map, the Pure Pet format, from client assets and interviews, with evidence, data-gap and research-needed rows, a flow row of exits and loops, and P1/P2 interview tagging.
- `code-design-playbook` — Code Computerlove's internal design team curriculum, standing context for every design-facing desk.
- `code-brand-style` — Code's visual identity and deck system, for anything that should look on-brand; every Code deck takes its look from here. Includes the phone frame every mobile screen in a deck sits in.
- `code-ux-review` — Code-format UX review of a site or journey: the journey funnel judged against Code's Persuasion Model, with a Core Web Vitals / PageSpeed check and a design, content and screen-reader accessibility check, delivered as a Code-branded research playback deck in five sections, including **Understanding the user**.
- `code-ux-userprofile` — chooses and builds user profiles with Code's User Profile Model (demographic personas, data segments, mindset profiles, jobs to be done). Starts with **proto-personas** from desk research and assumption (v0.1), validated and updated as research lands (v0.2 with data segments, v1.0 after interviews). Each profile is a designed board in the client's brand: push, pull, anxiety and habit (what makes a customer choose and commit), humanised with a neutral scene, a moment and an assumed quote, every line source-tagged, with **research to validate** and **data to validate at scale** at the bottom.
- `code-market-review` — market and competitor review across direct, indirect, category and wildcard competitors, comparing proposition, price, service, USPs, product features and UX through the Persuasion Model, delivered as a Code-branded immersion deck.
- `elevate-sow-writer` — drafts Hunter Douglas Elevate website-build Statements of Work (single brands, locales or batches) for the delivery team. Asks the intake questions itself (or pre-fills from the costing spreadsheet), writes scope from Code's house SoW wording, derives Out of Scope from a master feature list, and builds a Code-branded .docx with a QA pass for arithmetic, locale counts, leftover brand names and broken cross-references.
- `code-effort-estimate` — effort estimate and costing for research, CX, UX, strategy, design and prototyping work. Asks the day rate, currency and every research quantity before costing; builds interviews, groups, user testing, workshops, field visits and complex journeys from house multipliers (setup once, then prep, running and analysis per unit); asks about recruitment, incentives and external costs (equipment, tools, travel); charges management (Delivery Management 20%, Product Consultancy 5%) and AI tokens (2%) once on the whole project. Delivers a Code-styled Excel sheet with live formulas and a TOTALS table at the top, plus checks for notes that don't match their days, expenses costed as days and missing quantities.

## Installing this

This repo is a Claude plugin marketplace (`.claude-plugin/marketplace.json` at the repo root). Add the marketplace from this repo's URL, then install the `design-studio-team-setup` plugin from it — all nine of its skills come with it.

## Building proto-persona boards

```bash
python3 skills/code-ux-userprofile/scripts/profile_board.py \
  skills/code-ux-userprofile/assets/example-breitling.json --out profiles --png
```

One JSON spec holds the client's brand and every profile (see `skills/code-ux-userprofile/references/board-spec.md`). The script writes, per profile, a review page, a Design canvas artboard (`.dc.html`) and, with `--png` (needs Playwright), a 2x image to place full-slide in a deck. Edit the JSON and re-run for each new version.

## Building an Elevate SoW

```bash
node skills/elevate-sow-writer/scripts/build_sow.js \
  skills/elevate-sow-writer/examples/luxaflex-project.json "Luxaflex Project SoW DRAFT.docx"
```

One JSON spec per SoW (shape in `skills/elevate-sow-writer/SKILL.md`, wording in `references/modules.md`). Needs the `docx` npm package. The script prints a QA report and the open `[TBC]` items.

## Building an effort estimate

```bash
python3 skills/code-effort-estimate/scripts/build_estimate.py \
  skills/code-effort-estimate/examples/discovery-example.json "Discovery estimate.xlsx"
```

One JSON spec per estimate (shape in `skills/code-effort-estimate/references/spec-format.md`). Needs `openpyxl`. The script prints its checks and the totals; open the sheet in Excel (or recalculate with LibreOffice) to see the formula results.

## Structure

```
.claude-plugin/
  marketplace.json                          — marketplace manifest, plugin sourced from "./"
  plugin.json                               — plugin manifest (repo root doubles as plugin root)
README.md
skills/
  design-studio-team-setup/
    SKILL.md                                — the team-setup skill
    references/
      project-brain-template.md             — shared engagement-level context doc
      role-brief-template.md                — per-role brief template
  code-design-playbook/
    SKILL.md                                — Code's internal design curriculum
  code-brand-style/
    SKILL.md                                — Code's visual identity
    references/
      deck-system.md                        — deck tokens, type scale, motifs and layouts
      tokens.css                            — brand colour/type tokens
    scripts/
      slides_house.py                       — builds the house slide layouts, including the phone frame
  code-ux-review/
    SKILL.md                                — Persuasion Model UX review + Core Web Vitals + accessibility + user profiles, as a deck
  code-ux-userprofile/
    SKILL.md                                — User Profile Model, proto-personas and push/pull boards
    references/
      board-spec.md                         — the JSON spec for profile boards
    assets/
      example-breitling.json                — worked example: three Breitling US proto-personas
    scripts/
      profile_board.py                      — JSON spec → HTML, Design canvas artboard and PNG per profile
  code-market-review/
    SKILL.md                                — market and competitor review across four rings of competition, as a deck
  cx-journey-map/
    SKILL.md                                — build a Code-format CX journey map and add interviews to it
    references/
      map-spec.md                           — rows, card conventions and the JSON spec format
      example-map.json                      — complete fictional example spec
    scripts/
      build_map.py                          — JSON spec → Design canvas artboard (or --standalone HTML)
  elevate-sow-writer/
    SKILL.md                                — intake questions, spec format, build and QA steps for Elevate SoWs
    references/
      modules.md                            — Code's house SoW wording per scope module + out-of-scope feature keys
    examples/
      luxaflex-project.json                 — worked spec rebuilding the signed Luxaflex Project SoW
    assets/
      cover.jpg, code-logo-navy.png, code-logo-white.png
    scripts/
      build_sow.js                          — JSON spec → Code-branded .docx + QA report
  code-effort-estimate/
    SKILL.md                                — intake questions, house rules, checks and build steps for effort estimates
    references/
      research-multipliers.md               — setup / per-unit / analysis standards for research and design methods
      activity-library.md                   — typical activities and days by phase
      spec-format.md                        — the JSON spec the script reads
    examples/
      discovery-example.json                — fictional single-block discovery estimate
      phased-client-example.json            — fictional two-phase estimate in the client layout
    scripts/
      build_estimate.py                     — JSON spec → Code-styled .xlsx with live formulas, TOTALS table and checks
```

Every skill Claude's plugin loader can discover lives at `skills/<skill-name>/SKILL.md` under the plugin root — that's the convention this structure follows for all nine skills.
