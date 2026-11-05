# Research multipliers

Research effort scales with how many sessions Code runs. For these methods, **always ask the quantity first** ("How many customer groups of 5?", "How many user-testing groups / audience types?", "How many 1:1 interviews?", "How many workshops?"). Then build the lines from the standard below. Don't type a lump number for these.

Each method has a one-off **setup** (done once, whatever the quantity) and **per-unit** steps (multiplied by the quantity). Analysis lands in Synthesis and analysis so the phases read the way Code presents them.

The days below are house defaults. They are starting points to confirm with the person, and can be overridden per estimate in the spec (`standards`).

| Method (`method` key) | Unit | Setup (once) | Per unit | Analysis per unit |
|---|---|---|---|---|
| Customer groups (`customer_groups`) | group of ~5 | Discussion guide and screener: 2 | Session prep and logistics 0.5 · Running and notes 3.5 | 1 |
| 1:1 customer interviews (`customer_interviews`) | interview | Discussion guide and screener: 1.5 | Prep 0.1 · Running and notes 0.4 | 0.25 |
| Stakeholder interviews (`stakeholder_interviews`) | interview | Interview guide: 1 | Prep 0.1 · Running 0.4 (paired: 2 people run 5 a day) | 0.2 |
| User testing (`user_testing`) | test group (one audience type, ~5–6 participants) | Test plan and script: 2 | Prep and set-up 0.5 · Running sessions 2.5 | 2 |
| Internal mapping workshops (`workshops`) | 2-hour session | Workshop design: 1 | Prep 0.25 · Running 0.25 | Write-up 0.25 |
| Field visits (`field_visits`): ride-alongs, store or retailer visits, contextual inquiry | visit (about a day on site) | Field guide and visit planning: 1.5 | Prep 0.25 · Visit and notes 1 | 0.5 |
| Complex journey design (`complex_journeys`) | complex journey | — | Design sprint 6 · Content design 4 · Hi-fidelity design 4 · Usability testing 4 · Amends 2 (= 20 per journey) | — |

**Recruitment whenever Code speaks to people.** Customer groups, 1:1 customer interviews and user testing always get the recruitment questions: who recruits (recruitment partner, panel, the client's own customers), the cost per group or per participant, and incentives. These are expense lines, never days. The script warns if a participant method has no recruitment cost, unless it's set to `recruitment: "none"` (the client supplies participants, which goes in the assumptions). Stakeholder interviews and internal workshops are the client's own people, so no recruitment. For field visits, ask about recruitment (usually the client arranges) and incentives, plus travel as an external cost.

**Ranges seen in past estimates.** Customer groups have been costed at 4 to 5 days per group for prep and running, with analysis separate. Use the standard, and if the person's house number differs, override it in `standards`. For complex journeys, use `split_steps: true` to list sprint, content, hi-fi, testing and amends as separate lines, which is how Code shows design phases to clients.

**Quantities must agree.** The quantity recruited, run and analysed comes from one number in the spec, so it can't drift between lines.

Stakeholder interviews are run as a pair, 5 in a day, so 5 interviews = 1 day × 2 people = 2 days running. Default quantity is 5 unless the person says otherwise.

Worked example: 5 customer groups → setup 2 + 5 × (0.5 + 3.5) = 22 days in Insight gathering, plus 5 × 1 = 5 days analysis in Synthesis and analysis. 1 user-testing group → 2 + 1 × 3 = 5 days running, 2 days analysis.
