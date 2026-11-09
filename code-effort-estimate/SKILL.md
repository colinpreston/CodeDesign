---
name: code-effort-estimate
description: "Build a Code effort estimate and costing for research, CX, UX, service design, strategy, design and prototyping work: activities grouped by phase, days per activity, cost at the day rate, management as a percentage, external supplier costs (recruitment, tools, AI tokens), contingency and totals, delivered as a Code-styled Excel sheet with live formulas. Use whenever someone asks to estimate, cost, price, scope the days for, or 'do the numbers on' a project, discovery, research programme, design phase, workshop series or proposal, or pastes an activity/days/cost table to check or rebuild, even if they don't say 'estimate'. Always confirms the day rate and research quantities before costing."
---

# Code effort estimate and costing

Turns a scope of work into a costed estimate in Code's format. **Every cost is days × day rate**, except external costs (passed through at cost) and the occasional fixed-price item.

The sums are done by `scripts/build_estimate.py`, never by hand. It writes live Excel formulas, so the sheet still adds up when someone changes a day later. Your job is the judgement: the right activities, quantities that are asked for rather than assumed, notes that match the numbers, and the checks.

## Principles

- **Ask for the day rate and currency every time.** Don't suggest a figure or assume one: the skill holds no rates, so ask "What day rate and currency should I use for this one?" and use exactly what the person says. Non-round rates are fine (e.g. a converted rate). Get a rate per grade if there's more than one. Never write the rate back into this skill, its examples or memory.
- **Ask the numbers, never assume them.** Research and design effort scales with how many sessions or journeys there are. Build those lines from `references/research-multipliers.md`, not a lump figure.
- **Recruitment whenever we speak to people.** Customer groups, 1:1 customer interviews and user testing always get a recruitment question (who recruits, cost per group or participant) and an incentives question.
- **Always ask about external costs.** Equipment (test devices, recording or research kit), supplier tools (prototyping tool, research or testing platform, survey tool), venues and travel. All are expenses passed through at cost, never converted into days.
- **Management and AI tokens are charged once, on the whole project.** They sit in one block after all the phases, worked out from the project's total effort, not phase by phase. AI token costs are a standing line in that block, default 2% of effort cost; confirm the percentage each run. Use per-phase management only when the person asks for it (some clients are priced phase by phase).
- **Totals up front, in the sheet itself.** Every estimate opens with a TOTALS table at the top of the Estimate sheet: each phase, management and AI tokens, contingency, total ex VAT, VAT and total inc VAT. Whatever goes in a deck or SoW is copied from that table.
- **Stakeholder interviews and team walkthroughs belong in Discovery.** Immersion is getting set up and reading in: kick-off and prep, document and data request, doc review, competitor and market review. Stakeholder interviews and "show me" walkthroughs of how the team uses its systems go in Discovery, with the other research.
- **Notes must agree with the numbers.** The note is what the client reads, so it's where errors bite.
- **No zero lines in a client version.** Size it, or move it to Assumptions & exclusions.
- **Store no client figures.** Never write a client's costings back into this skill, its examples or memory.

## Step 1 — Intake

Read what you've been given (a brief, an outline, a pasted table, an old estimate). Then confirm, asking only what's missing, in one go:

1. **Day rate and currency** (and grades). Ask with no suggested figure.
2. **Phases** — one priced block, or separate phases each with its own subtotal (e.g. Phase 1 Discovery and Strategy, Phase 2 Design and Prototype)? Sections sit inside phases (1a/1b Immersion and Discovery, 1c Strategy).
3. **Activities** — draft them from the brief using `references/activity-library.md` if the person hasn't listed them.
4. **Quantities — always ask.** "How many customer groups of 5?", "How many 1:1 interviews?", "How many user-testing groups (audience types)?", "How many stakeholder workshops or groups?", "How many ride-alongs or site visits?", "How many complex journeys to design?". Any line that says "per group" or "per journey" needs its number.
5. **Recruitment** for every method that talks to customers or users: recruiter, cost per group or participant, incentives. If the client supplies participants, say so in the assumptions.
6. **External costs**: equipment (devices, recording or test kit), supplier tools (prototyping, research platforms, survey), venues, travel. Ask each run. If there are none, the person says so and you record it.
7. **Management** (charged once on the whole project by default): which roles, what percentage, and on what basis.
   - *Days basis* (e.g. Delivery Management 20%, Product Consultancy 5% of effort days, nearest half day), or
   - *Cost basis* (e.g. Project Management 10% of effort and fixed-price costs, per phase, not on expenses).
   - **AI token costs**: always add, default 2% of the project's effort cost (`basis: "cost"`, `applies_to: ["effort"]`). Confirm the %.
8. **Fixed-price items** (work priced as a lump, e.g. a partner's analysis): the cost, and whether it carries management (default yes).
9. **Contingency** % (default 0%, always stated), and whether to show VAT.
10. **Layout**: *full* (Activity | Grade | Days | Hours | Day rate | Cost | Notes, for internal working) or *client* (Activity | Time (days) | Cost, for proposals). Cost rounding to whole units or pence.
11. Client, project, version and who it's prepared by.

If the person pastes an existing estimate to check, run Step 3 on it first and work out how its totals were built (rate per line, management basis) before changing anything.

## Step 2 — Draft the activity list

Show the draft as a short table, phase by phase, with quantities and days, and let the person adjust before building. Use `method` lines for anything quantity-driven, so the number recruited, run and analysed comes from one figure.

## Step 3 — Checks (the script runs these too; report what you find)

- Every line's cost is days × the rate.
- Every note's quantities multiply out to the line's days. "x5 groups" in the activity matches the groups in the note.
- Expenses aren't disguised as days (a note giving a fee per unit is an expense).
- "Per group / per journey" lines state how many.
- Participant methods have a recruitment cost, or "client supplies".
- External costs (equipment, tools, travel) are present, or confirmed as none.
- There's an AI token cost line, and management is charged once on the project unless the person asked for per-phase.
- Stakeholder interviews and walkthroughs sit in Discovery, not Immersion.
- The TOTALS table at the top matches the totals at the bottom.
- Management uses the stated basis and lines. Pass-through expenses are outside it.
- No zero-day lines, and contingency is stated.

**Options or routes.** When a proposal offers alternatives (e.g. Fix and improve vs Start again), cost each one as its own spec and workbook, with its stages as phases so each stage gets its own subtotal. Never add alternatives together. Cost only the fixed-scope stages, and list stages that are sized later in the assumptions. Sense-check the days per stage against the stated duration (days ÷ weeks ÷ 5 = the team size it implies) and say what team that assumes.

## Step 4 — Build

Write the spec as JSON (`references/spec-format.md`), then:

```bash
python scripts/build_estimate.py spec.json output.xlsx
python <xlsx-skill>/scripts/recalc.py output.xlsx
```

The script prints check warnings and the totals per phase. Fix warnings in the spec, not the sheet. It produces four sheets: Estimate (TOTALS table at the top, then the detail), Settings (rates and percentages as blue inputs), Summary (by phase and section, plus effort / fixed / expenses / management split) and Assumptions. Colours come from `code-brand-style` (navy header, lime total row); don't restyle it.

## Step 5 — Hand over

Send the .xlsx. In the reply, give the figures from the TOTALS table: the subtotal per phase, management and AI tokens, the total ex VAT and the total days, and any changes you made against what they gave you (with the money difference). Offer one next step, e.g. feeding the estimate into a SoW (`elevate-sow-writer` for Elevate work) or a proposal deck.

## Files

- `references/research-multipliers.md` — setup / per-unit / analysis standards for interviews, groups, user testing, workshops and complex journeys, plus recruitment. Read whenever research or design is in scope.
- `references/activity-library.md` — typical activities and days across discovery, strategy, and design and prototype work.
- `references/spec-format.md` — the JSON spec the script reads.
- `scripts/build_estimate.py` — builds the sheet with live formulas and runs the checks.
- `examples/discovery-example.json` — single-block, full layout, days-basis management, external costs (fictional).
- `examples/phased-client-example.json` — two phases, client layout, cost-basis PM, fixed-price item (fictional, dummy rate).

## Saving output in a project

If the work is for a client project that has a stage board and project folder (see the Project Brain), do the following before finishing:
1. **Save the output** into the matching method folder's `outputs/`, e.g. `02 Discovery/DI-M1 Competitor review/outputs/`. Decks and docs go in as files. An artifact gets an exported copy plus its link.
2. **Confirm** the file is there by listing the folder.
3. **Log it** on the method's card, as described in `code-evidence-to-backlog`'s `references/stage-board.md` and `references/project-folder.md`.

If the folder can't be reached, say so rather than recording a path.
