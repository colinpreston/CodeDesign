# Code Method Library: Immersion → Discovery → Vision → Definition

This is Code's process map, transcribed from the team's board (`assets/process-map-*.png`). It lists **everything we could do**. An engagement never does all of it. Scope mode cuts it down to the methods the brief, time and budget allow. That selection is the programme plan, and only selected methods become cards on the stage board.

**How to read it:**
- **Stage:** the column on the map, with its headline question.
- **Group:** the activity group within the stage.
- **ID:** each method's ID (e.g. `DI-C3`), which is also its card ID on the stage board.
- **Artefacts:** what the method produces.
- **Skill:** the skill that helps make it. CodeDesign skills are named bare; other plugins' skills carry their prefix and are used if installed.
- **Logs:** the ID prefixes its findings get in the Evidence Ledger.
- **●** marks the **evidence spine**: the minimum that has to happen, in some form, for the stories at the end to be evidence-backed (see the bottom of this file).
- Items marked *(proposed)* are not on the team's map; they're suggested additions for Colin to accept or strike.

---

## Stage 0: Brief & scope *(before the map starts)*

| ID | Method | Artefacts | Skill | Logs |
|---|---|---|---|---|
| BR-1 ● | Read the brief | Brief summary: problem, project type, budget, timeline, known constraints | — | AS, CN |
| BR-2 ● | Select methods (reductive) | Method selection with what's in, what's cut, and the risk of each cut | this skill, Scope mode | DC |
| BR-3 ● | Programme plan | Research brief, methods, effort and days per stage, draft interview scripts per stakeholder role | `code-effort-estimate`, `design-research:interview-script` | — |
| BR-4 | Proposal / SoW | Proposal or SoW | `elevate-sow-writer` (Elevate work) | — |

## Stage 1: Immersion — *Where are we now?*

**Questions to be answered (these form the G1 gate):** What is the problem? · How will we work together? · Why are we doing this work? · What do we already know?

**Group: Setting the right foundations**

| ID | Method | Artefacts | Skill | Logs |
|---|---|---|---|---|
| IM-1 ● | Understand the problem | Type of project; problem statement | `ux-strategy:frame-problem` | AS |
| IM-2 ● | Day 0 (kick-off, name TBC) | Product canvas / lo-fi map / OKRs. Inputs: commercial/business audit, experience today, tech today, product-thinking presentation | `stakeholder-comms:alignment-workshop` | BR, AS |
| IM-3 | Tech due diligence (not TDD) | Tech doc, including any site migration | — | CN, NFR |
| IM-4 | Chemistry test | Agreed foundations | — | — |
| IM-5 | Ways of working | Working agreement | `cross-functional-alignment:working-agreement` | — |
| IM-6 | Team-building sessions | — | — | — |
| IM-7 ● | Research immersion | Research plan or brief, with each question traced to an AS or BR | `design-research:discover` | EV |
| IM-8 ● | Knowledge base | Digital log; data. This **is** the evidence log: every source becomes an EV entry | `design-research:research-repository` | EV |

## Stage 2: Discovery — *What is happening and why?*

This stage ends in **INSIGHT**.

**Group P: Understand the product or service**
**Questions:** What is the product? · What is not working? · What is working?

| ID | Method | Artefacts | Skill | Logs |
|---|---|---|---|---|
| DI-P1 | Research sprint | Sprint outputs | `design-ops:design-sprint-plan` | EV |
| DI-P2 | Analytics health check | Report | `design-research:behavioural-analytics` | EV |
| DI-P3 | Content and UX audit | Report | `code-ux-review` | EV |
| DI-P4 | Expert review | Report | `code-ux-review`, `prototyping-testing:heuristic-evaluation` | EV |
| DI-P5 | Tech review (tech due diligence, not TDD) | North star; understanding of the current product | — | CN |
| DI-P6 | Product spike | Prototype or feasibility report | — | CN, EV |
| DI-P7 | Experiments | Prototypes | `prototyping-testing:experiment` | EV |
| DI-P8 | Accessibility audit | Report | `design-systems:accessibility-audit` | EV, NFR |
| — | *(output across the group)* | Constraints | — | CN |

**Group B: Understand the business**
**Questions:** What does success look like? · Why are we doing things?

| ID | Method | Artefacts | Skill | Logs |
|---|---|---|---|---|
| DI-B1 ● | Stakeholder interviews | GROW write-up | `design-research:interview-script`, `design-research:summarize-interview` | EV, BR |
| DI-B2 | Contextual observation / shadowing | Timelines and notes; stakeholder map | `stakeholder-comms:stakeholder-map` | EV |
| DI-B3 | Staff interviews | Timelines and notes, or write-up | `design-research:summarize-interview` | EV |
| DI-B4 | Content governance workshop | Write-up | — | BR |
| — | *(outputs across the group)* | Commercial performance; commercial opportunities; constraints; what have we tried before (if not covered by hopes and fears); list of what to avoid; service map / commercial impact report | `ux-strategy:service-blueprint` | BR, CN |

**Group M: Understand the market and brand**
**Questions:** Who do we want the brand to be? · What do you want? · How do you want to be known?

| ID | Method | Artefacts | Skill | Logs |
|---|---|---|---|---|
| DI-M1 | Competitor review | Report | `code-market-review` | EV |
| DI-M2 | Existing customer segment review | Report | `code-ux-userprofile` (data segments) | EV |
| DI-M3 | Brand review | Report | `visual-critique:critique-brand-consistency` | EV |
| DI-M4 | Brand proposition workshop | Write-up | — | BR |
| — | *(outputs across the group)* | Advertising and media audit (could be done by the media agency); real-world insights team; effectiveness report; market and trends report | — | EV |

**Group C: Understand the customer**
**Questions:** Who uses it? · What do they need?

| ID | Method | Artefacts | Skill | Logs |
|---|---|---|---|---|
| DI-C1 | Customer opportunity review | Report | — | EV |
| DI-C2 | Market opportunity analysis | Report | `ux-strategy:competitive-analysis` | EV |
| DI-C3 | Customer interviews | Timelines and notes, or write-up | `design-research:interview-script`, `design-research:summarize-interview` | EV |
| DI-C4 | Remote research | Timelines and notes, or write-up | — | EV |
| DI-C5 | Diary study | Timelines and notes, or write-up | `design-research:diary-study-plan` | EV |
| DI-C6 | Usability testing (plus experiments) | Timelines and notes, or write-up | `design-research:test-plan` | EV, TF |
| DI-C7 | Contextual observation | Timelines and notes, or write-up | — | EV |

**Spine rule for Group C:** at least one primary customer method (DI-C3 to DI-C7) is required. If the brief rules all of them out, every insight downstream is capped at Moderate confidence, and the board says so.

## Stage 3: Vision — *Where do we want to be?*

**Group: Consolidate insights**

| ID | Method | Artefacts | Skill | Logs |
|---|---|---|---|---|
| VI-1 ● | Research analysis and synthesis | Profiles; **insight register** | `design-research:synthesize`, `code-ux-userprofile` | IN |
| VI-2 | Experience analysis and synthesis | A map | `cx-journey-map` | IN |
| VI-3 ● | Opportunity analysis and synthesis | **JTBD / epics**: the first draft of the story map's epics | `design-research:jobs-to-be-done`, `ux-strategy:opportunity-framework` | OP, EP |

**Group: Ingredients**

| ID | Method | Artefacts | Skill | Logs |
|---|---|---|---|---|
| VI-4 | Brand / AD vision | Early design principles and visual language | `ux-strategy:design-principles` | DC |
| VI-5 | Content strategy | Editorial principles | `ux-strategy:content-strategy` | DC |
| VI-6 | Tech architecture | A tech map | — | CN, NFR |
| VI-7 | Future possibilities (design sprint) | Prototypes or visuals | `design-ops:plan-sprint`, `prototyping-testing:explore-options` | DC |
| VI-8 | Service and product propositions | Product and service principles | `ux-strategy:north-star-vision` | DC |

**Group: The plan**

| ID | Method | Artefacts | Skill | Logs |
|---|---|---|---|---|
| VI-9 | Service / product strategy | Presentation | `ux-strategy:strategize`, `code-brand-style` | — |
| VI-10 ● | Measures | OKRs, plus hypotheses in Code's format: *Because we observed… → causing… → we believe… → will have… → measured by…* | `ux-strategy:metrics-definition` | HY |
| VI-11 ● | Definition of design challenges | Design challenge roadmap: the **themes** for the story map's backbone | `ux-strategy:frame-problem` | TH |

## Stage 4: Definition — *What are we making?*

**Group: Focus**

| ID | Method | Artefacts | Skill | Logs |
|---|---|---|---|---|
| DF-1 ● | Prioritisation session | Road map | `program-planning:prioritisation-framework` | DC |
| DF-2 | Measurement framework | Dashboard | `measurement-ops:define-metrics` | — |
| DF-3 | Tracking for the framework | Analytics events / tracking plan *(proposed: the map has no artefact here)* | — | — |

**Group: Make tangible experiences**

| ID | Method | Artefacts | Skill | Logs |
|---|---|---|---|---|
| DF-4 ● | Design sprints | Prototypes, with flows covering error, empty and edge states | `design-ops:plan-sprint`, `prototyping-testing:user-flow-diagram` | DC, FL |
| DF-5 | Content design | Prototypes, with real copy | `designer-toolkit:ux-writing` | — |
| DF-6 | Information architecture | Site map | `ux-strategy:information-architecture` | — |
| DF-7 | Tree testing | Navigation structure | `prototyping-testing:test-plan` | TF |
| DF-8 | Art direction / design system | Design system / guide; component inventory (new / changed / existing); accessibility annotations | `design-systems:audit-system`, `accessibility-decisions:handoff` | NFR |
| DF-V ● | Prototype validation *(proposed)* | Test findings, iteration log, hypothesis scorecard, frozen prototype version | `prototyping-testing:test-plan`, `design-research:summarize-interview` | TF |

DF-V is the one real gap on the map. Design sprints include testing, but nothing on the board names the **tested prototype** that stories link to. That can be its own card, or folded into DF-4's definition of done. Either way G4 needs it.

**Group: Define the first release** *(the endpoint)*

| ID | Method | Artefacts | Skill | Logs |
|---|---|---|---|---|
| DF-9 ● | Full product epic / story map | User stories (see `story-schema.md`) | this skill, Build backlog; `code-design-playbook` §7 | EP, ST |
| DF-10 ● | MVP story map | Backlog, with release slices | this skill, Build backlog | RL |
| DF-11 | Experiment programme definition | Test plan for post-launch experiments, traced to HY | `prototyping-testing:experiment` | HY |

---

## Gates

Each gate passes when the stage's questions are answered with validated evidence and its checks pass. Every gate needs a named human sign-off in the ledger.

**G1 Immersion done:**
- All four questions are answered and signed off by the client sponsor.
- Every research question traces to an AS or a BR.
- A named dev contact owns the tech constraints.

**G2 Insight:**
- Each selected Discovery group's questions are answered.
- Every insight that will be cited later has EV links, a provenance tag and a named validator.
- AI-only insights are quarantined.
- Each AS is marked confirmed, refuted or still open.

**G3 Vision agreed:**
- Profiles, map and epics trace to IN.
- Measures and hypotheses are set.
- The design challenge roadmap is signed off by the sponsor and the dev lead.

**G4 Design validated** (mid-Definition, before "Define the first release"):
- No critical test findings remain open.
- Every open major finding is either a story or a logged risk.
- The prototype version is frozen.

**G5 Ready for estimation:**
- Every story passes the Definition of Ready.
- There are no untraced stories outside the parking lot.
- The dev lead and the product owner have signed off.

## The evidence spine (●)

These are the methods that can't be cut if the stories at the end are going to be evidence-backed. Each can be shrunk to fit the budget, but not removed. If Scope mode cuts a spine item anyway, the ledger records it as a DC with the reason, and every story downstream carries the lower confidence.

- **Brief & scope:** BR-1, BR-2, BR-3.
- **Immersion:** IM-1, IM-2, IM-7, IM-8.
- **Discovery:** DI-B1, plus at least one Group C primary method.
- **Vision:** VI-1, VI-3, VI-10, VI-11.
- **Definition:** DF-1, DF-4, DF-V, DF-9, DF-10.

## Provenance and confidence (every logged item)

**Provenance**
- `[H]`: made by a human.
- `[AI]`: AI draft, **not yet validated**. It can't be cited at a gate or used to ground a story.
- `[AI✓]`: made by AI, then validated by a human. The ledger records the validator, the date and the method.

**Confidence**
- **Strong:** at least 2 independent sources, at least 1 of them primary.
- **Moderate:** 1 primary source, or several consistent secondary ones.
- **Assumption:** no evidence yet. It stays labelled and becomes a DF-V test, a DF-11 experiment or a spike story.

**Other legitimate sources.** These are traced, but labelled by source, so the team can see what's user-evidenced and what's a business call:
- BR: business requirement
- CN: tech or regulatory constraint
- NFR: non-functional requirement
