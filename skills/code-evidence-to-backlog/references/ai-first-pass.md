# Run AI: what each card's button does

The **▶ Run AI** button on the stage board sends Claude one of the jobs below for that card. This file is the reference; the page holds the same list as `RUN` in `assets/stage-board.html`. Change both together.

**Modes**
- **First pass:** a draft of the method's main artefact from what's known.
- **Prep:** what the team needs before doing the method with people: guide, plan, screener, agenda.
- **Synthesis & analysis:** turns what's in the card's `inputs/` (transcripts, notes, data) into the method's output, with EV/IN/TF items logged.
- **Report or deck:** a finished-looking report or presentation, on brand.

**Needs inputs** means the job works on material in the card's `inputs/` folder. With nothing there, the panel warns and Claude asks for it rather than inventing it.

**Not offered:** IM-4 Chemistry test and IM-6 Team-building sessions (they're about people in a room).

How Claude handles a request: SKILL.md Step 3b.


## Brief & scope

| Method | Mode | Job | What Claude does | Skills | Needs inputs |
|---|---|---|---|---|---|
| BR-1 Read the brief | First pass | Brief summary | Read the brief and everything in this card's inputs. Write the brief summary: problem, project type, budget, timeline, known constraints and what the client already has. Log BR, CN and AS items in the ledger and list the gaps to ask the client about. | `code-design-playbook` |  |
| BR-2 Select methods (reductive) | First pass | Method selection | Run Scope mode: cut the method library to what the brief, time and budget allow. In and out with a reason or risk for each; log any spine cut as a DC. | `code-evidence-to-backlog` |  |
| BR-3 Programme plan | First pass | Programme plan | Turn the selected methods into the programme plan: research brief, methods, effort and days per stage, and draft interview scripts per stakeholder role. | `code-effort-estimate`, `design-research:interview-script` |  |
| BR-4 Proposal / SoW | Report or deck | Proposal or SoW | Draft the proposal or SoW from the agreed programme plan and estimate, on brand. | `code-effort-estimate`, `code-brand-style` |  |

## Immersion

| Method | Mode | Job | What Claude does | Skills | Needs inputs |
|---|---|---|---|---|---|
| IM-1 Understand the problem | First pass | Problem statement | Frame the problem: type of project, problem statement, what success looks like, and the assumptions to test. | `ux-strategy:frame-problem` |  |
| IM-2 Day 0 (kick-off) | Prep (guide or plan) | Day 0 plan | Plan Day 0: agenda, pre-read, attendees and exercises (product canvas, lo-fi map, OKRs), using what we already know. | `stakeholder-comms:alignment-workshop` |  |
| IM-2 Day 0 (kick-off) | Synthesis & analysis | Day 0 write-up | Write up Day 0 from the notes, photos and boards in inputs: what we heard, the lo-fi map, draft OKRs, and the assumptions to test. | `stakeholder-comms:alignment-workshop`, `design-research:synthesize` | yes |
| IM-3 Tech due diligence (not TDD) | First pass | Tech due diligence doc | Draft the tech doc from what we know: current estate, integrations, migration needs, constraints, risks, and the questions for the client's tech team. | `delivery-execution:risk-register`, `program-planning:dependency-map` |  |
| IM-5 Ways of working | First pass | Working agreement | Draft the working agreement: roles, cadence, decision rights, tools and communication. | `cross-functional-alignment:working-agreement` |  |
| IM-7 Research immersion | First pass | Research plan | Write the research plan: questions, each traced to an AS or BR item, methods, participants, recruitment and timing. | `design-research:discover`, `design-research:interview-script` |  |
| IM-8 Knowledge base | First pass | Tidy the knowledge base | File anything unsorted, backfill EV IDs in the ledger from what's in the folder, and refresh the folder index. | `design-research:research-repository` |  |

## Discovery

| Method | Mode | Job | What Claude does | Skills | Needs inputs |
|---|---|---|---|---|---|
| DI-P1 Research sprint | Prep (guide or plan) | Research sprint plan | Plan the research sprint: goals, schedule, methods, participants and outputs. | `design-ops:design-sprint-plan` |  |
| DI-P2 Analytics health check | Synthesis & analysis | Analytics health check | Analyse the analytics exports in inputs: tracking health, key funnels, drop-offs and anomalies, with what each means for the questions we're answering. | `design-research:behavioural-analytics`, `data:analyze` | yes |
| DI-P3 Content and UX audit | Report or deck | Content and UX audit | Audit the current site's content and UX against the brief; prioritised findings with evidence and screenshots. | `code-ux-review` |  |
| DI-P4 Expert review | Report or deck | Expert review | Run a heuristic expert review of the current experience; severity-rated findings with recommended fixes. | `code-ux-review`, `prototyping-testing:heuristic-evaluation` |  |
| DI-P5 Tech review | Prep (guide or plan) | Tech review plan | Plan the tech review: what to inspect, access needed, questions for the client's developers, and the report outline. | `program-planning:dependency-map` |  |
| DI-P5 Tech review | Synthesis & analysis | Tech review write-up | Write up the tech review from the audit notes in inputs: north star, current product understood, keep/fix/replace, constraints. | `delivery-execution:risk-register` | yes |
| DI-P6 Product spike | First pass | Spike plan | Define the product spike: question, approach, timebox and what would count as feasible. | — |  |
| DI-P7 Experiments | First pass | Experiment design | Design the experiments: hypotheses, variants, metrics and sample size. | `prototyping-testing:experiment` |  |
| DI-P8 Accessibility audit | Report or deck | Accessibility audit | Audit accessibility against WCAG 2.2 AA; findings by severity and the NFRs they imply. | `design-systems:accessibility-audit` |  |
| DI-B1 Stakeholder interviews | Prep (guide or plan) | Stakeholder interview guide | Draft the stakeholder interview guide per role, with each question traced to an AS or BR item. | `design-research:interview-script` |  |
| DI-B1 Stakeholder interviews | Synthesis & analysis | GROW write-up | Summarise each stakeholder interview in inputs, then synthesise into the GROW write-up; log EV and BR items with sources. | `design-research:summarize-interview`, `design-research:synthesize` | yes |
| DI-B2 Contextual observation / shadowing | Prep (guide or plan) | Observation guide | Draft the shadowing guide and the stakeholder map: who to observe, what to watch for, how to capture. | `stakeholder-comms:stakeholder-map` |  |
| DI-B2 Contextual observation / shadowing | Synthesis & analysis | Observation write-up | Turn the shadowing notes in inputs into timelines, pain points and a stakeholder map; log EV items. | `design-research:synthesize` | yes |
| DI-B3 Staff interviews | Prep (guide or plan) | Staff interview guide | Draft the staff interview guide per team. | `design-research:interview-script` |  |
| DI-B3 Staff interviews | Synthesis & analysis | Staff interview write-up | Summarise the staff interviews in inputs and synthesise themes; log EV items. | `design-research:summarize-interview`, `design-research:synthesize` | yes |
| DI-B4 Content governance workshop | Prep (guide or plan) | Governance workshop plan | Plan the content governance workshop: aims, agenda, exercises, attendees. | `stakeholder-comms:alignment-workshop` |  |
| DI-B4 Content governance workshop | Synthesis & analysis | Governance write-up | Write up the workshop from the notes in inputs: owners, workflow, rules; log BR items. | — | yes |
| DI-M1 Competitor review | Report or deck | Competitor review | Review the competitors and comparable experiences; patterns, gaps and opportunities with screenshots. | `code-market-review` |  |
| DI-M2 Existing customer segment review | Report or deck | Customer segment review | Review the existing customer segments from the data in inputs; segment profiles and what they mean for the work. | `code-ux-userprofile` | yes |
| DI-M3 Brand review | Report or deck | Brand review | Review how the brand shows up across channels today against its guidelines. | `visual-critique:critique-brand-consistency` |  |
| DI-M4 Brand proposition workshop | Prep (guide or plan) | Brand proposition workshop plan | Plan the brand proposition workshop. | `stakeholder-comms:alignment-workshop` |  |
| DI-M4 Brand proposition workshop | Synthesis & analysis | Brand proposition write-up | Write up the workshop from the notes in inputs. | — | yes |
| DI-C1 Customer opportunity review | Report or deck | Customer opportunity review | Review the client's existing customer research in inputs: what it covers, what it says, and the gaps our research needs to fill. | `design-research:synthesize` | yes |
| DI-C2 Market opportunity analysis | Report or deck | Market opportunity analysis | Analyse the market opportunity: size, segments, competitors and openings. | `ux-strategy:competitive-analysis` |  |
| DI-C3 Customer interviews | Prep (guide or plan) | Discussion guide and screener | Draft the customer discussion guide and recruitment screener, each question traced to an AS item. | `design-research:interview-script` |  |
| DI-C3 Customer interviews | Synthesis & analysis | Customer interview write-up | Summarise each customer interview in inputs, then synthesise themes; log EV items with quotes checked against the transcripts. | `design-research:summarize-interview`, `design-research:synthesize` | yes |
| DI-C4 Remote research | Prep (guide or plan) | Remote research plan | Plan the remote research: method, tasks, participants and tooling. | `design-research:test-plan` |  |
| DI-C4 Remote research | Synthesis & analysis | Remote research write-up | Write up the remote sessions in inputs; log EV items. | `design-research:summarize-interview` | yes |
| DI-C5 Diary study | Prep (guide or plan) | Diary study plan | Plan the diary study: prompts, cadence, participants, incentives. | `design-research:diary-study-plan` |  |
| DI-C5 Diary study | Synthesis & analysis | Diary study write-up | Synthesise the diary entries in inputs into behaviour over time; log EV items. | `design-research:synthesize` | yes |
| DI-C6 Usability testing | Prep (guide or plan) | Usability test plan | Write the usability test plan: tasks, metrics, participants, script. | `design-research:test-plan` |  |
| DI-C6 Usability testing | Synthesis & analysis | Usability findings | Write up the sessions in inputs as findings with severity; log TF items. | `design-research:summarize-interview` | yes |
| DI-C7 Contextual observation | Prep (guide or plan) | Field guide | Draft the contextual observation field guide: what to observe, questions, capture template. | `design-research:interview-script` |  |
| DI-C7 Contextual observation | Synthesis & analysis | Field visit write-up | Turn the field notes in inputs into timelines and pain points; log EV items. | `design-research:synthesize` | yes |

## Vision

| Method | Mode | Job | What Claude does | Skills | Needs inputs |
|---|---|---|---|---|---|
| VI-1 Research analysis and synthesis | Synthesis & analysis | Insight register and profiles | Synthesise the checked Discovery evidence into the insight register (IN items with sources) and profiles. | `design-research:synthesize`, `code-ux-userprofile` | yes |
| VI-2 Experience analysis and synthesis | Synthesis & analysis | Journey map | Map the experience from the checked evidence: stages, actions, feelings, pain points and opportunities. | `cx-journey-map` | yes |
| VI-3 Opportunity analysis and synthesis | Synthesis & analysis | JTBD, opportunities and epics | Turn validated insights into jobs to be done, opportunities (OP) and the first draft of epics. | `design-research:jobs-to-be-done`, `ux-strategy:opportunity-framework` | yes |
| VI-4 Brand / AD vision | First pass | Design principles | Draft early design principles and the visual direction. | `ux-strategy:design-principles` |  |
| VI-5 Content strategy | First pass | Content strategy | Draft the content strategy and editorial principles. | `ux-strategy:content-strategy` |  |
| VI-6 Tech architecture | First pass | Tech map | Draft the target tech map: platforms, integrations, data flows, constraints and NFRs. | `program-planning:dependency-map` |  |
| VI-7 Future possibilities (design sprint) | Prep (guide or plan) | Future possibilities sprint | Plan the design sprint and frame the options to explore. | `design-ops:plan-sprint`, `prototyping-testing:explore-options` |  |
| VI-8 Service and product propositions | First pass | Service and product principles | Draft the service and product propositions and principles. | `ux-strategy:north-star-vision` |  |
| VI-9 Service / product strategy | Report or deck | Strategy deck | Build the service or product strategy presentation from the Vision work. | `ux-strategy:strategize`, `code-brand-style` |  |
| VI-10 Measures | First pass | OKRs and hypotheses | Draft the OKRs and hypotheses in Code's format (Because we observed… → we believe… → measured by…). | `ux-strategy:metrics-definition` |  |
| VI-11 Definition of design challenges | First pass | Design challenge roadmap | Frame the design challenges and lay them out as the roadmap themes. | `ux-strategy:frame-problem` |  |

## Definition

| Method | Mode | Job | What Claude does | Skills | Needs inputs |
|---|---|---|---|---|---|
| DF-1 Prioritisation session | Prep (guide or plan) | Prioritisation session | Plan the prioritisation session and draft the road map to bring to it. | `program-planning:prioritisation-framework` |  |
| DF-2 Measurement framework | First pass | Measurement framework | Draft the measurement framework and dashboard spec. | `measurement-ops:define-metrics` |  |
| DF-3 Tracking for framework | First pass | Tracking plan | Draft the analytics tracking plan for the framework. | `marketing-skills:analytics` |  |
| DF-4 Design sprints | Prep (guide or plan) | Design sprint plan and flows | Plan the design sprint and draft the flows to prototype, including error, empty and edge states. | `design-ops:plan-sprint`, `prototyping-testing:user-flow-diagram` |  |
| DF-5 Content design | First pass | Content design | Write real copy for the prototype screens. | `designer-toolkit:ux-writing` |  |
| DF-6 Information architecture | First pass | Information architecture | Draft the site map and navigation. | `ux-strategy:information-architecture` |  |
| DF-7 Tree testing | Prep (guide or plan) | Tree test plan | Plan the tree test: tree, tasks, participants. | `prototyping-testing:test-plan` |  |
| DF-7 Tree testing | Synthesis & analysis | Tree test results | Analyse the tree test results in inputs; log TF items. | — | yes |
| DF-8 Art direction / design system | First pass | Component inventory | Draft the component inventory (new, changed, existing) and accessibility annotations. | `design-systems:audit-system`, `accessibility-decisions:handoff` |  |
| DF-V Prototype validation (proposed) | Prep (guide or plan) | Prototype test plan | Write the prototype validation plan: hypotheses, tasks, participants. | `prototyping-testing:test-plan` |  |
| DF-V Prototype validation (proposed) | Synthesis & analysis | Test findings and scorecard | Write up the sessions in inputs: TF items with severity, iteration log and hypothesis scorecard. | `design-research:summarize-interview` | yes |
| DF-9 Full product epic / story map | First pass | Story map | Run Build backlog: backbone, epics, steps and stories, every story traced to evidence. | `code-evidence-to-backlog` |  |
| DF-10 MVP story map | First pass | MVP slice | Draw the MVP line and release slices, each with its outcome, hypotheses, dependencies and why this cut. | `code-evidence-to-backlog` |  |
| DF-11 Experiment programme definition | First pass | Experiment programme | Define the post-launch experiments, traced to HY items. | `prototyping-testing:experiment` |  |
