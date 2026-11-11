---
name: code-evidence-to-backlog
description: Run Code's design process (Immersion, Discovery, Vision, Definition) from brief to an estimable backlog. It cuts Code's method library down to a programme plan that fits the brief's time and budget, tracks every method and artefact on a Kanban stage board and in an Evidence Ledger, keeps AI work quarantined until a human validates it, and builds a traced story map, MVP slice and user stories for dev. Use when a brief comes in, when scoping methods, when checking where a project is or whether it's ready to move on, when logging or validating evidence, or when turning validated insight and prototypes into epics and stories.
---

# Evidence to Backlog

This skill gets a design engagement to a point where dev can take a set of user stories, estimate them and plan the build, and trust where they came from. It doesn't do the research or design itself; the other skills do that. This skill does three jobs:

1. **Defines what could exist, and what must.** `references/method-library.md` transcribes Code's process map (`assets/process-map-*.png`): every method and artefact across Immersion (*Where are we now?*), Discovery (*What is happening and why?*), Vision (*Where do we want to be?*) and Definition (*What are we making?*). It also marks the **evidence spine**, the minimum the stories need. Scope mode cuts the library down to what the brief, time and budget allow. That cut is the programme plan.
2. **Keeps the chain honest.** Every insight, decision and finding is logged in an **Evidence Ledger** with a provenance tag (`[H]`, `[AI]`, `[AI✓]`) and a confidence level. AI output can't be used to ground anything until a named human has validated it.
3. **Builds the backlog from the chain.** It produces the story map, release slices and stories, and every story traces back to evidence (see `references/story-schema.md`).

4. **Shows where you are.** A Kanban **stage board** dashboard (`references/stage-board.md`) has:
   - one column per stage, grouped by activity group;
   - a card for each **selected** method, linked to its artefact;
   - each stage's questions-to-be-answered, as the gate checklist;
   - an inbox for new inputs such as briefs.

It follows `code-design-playbook`, especially §7 Story mapping & prioritisation (Vision → Strategy → Roadmap themes → OKRs → story map; themes come from real user jobs; prioritise on user value and business value together with effort; mapping is a team activity). Where the playbook and this skill disagree, the playbook wins.

**The trace runs:**
Story (ST) → Epic (EP) → Theme (TH) → Opportunity (OP) → Insight (IN) / Test finding (TF) → Evidence (EV).
Business requirements (BR), constraints (CN) and NFRs are legitimate sources too, but they keep their own labels, so it stays visible what's user-evidenced and what's a business call.

## Step 0: Find the context

- If the session has a company brain (Project Brain, Research Repository from `design-studio-team-setup`), read the Brain and the Repository's Active Notes and Digest first. In that case the ledger sits alongside them.
- Otherwise ask: which client, what engagement, and is there an existing ledger?
- Read `references/method-library.md` every time. Read `references/project-folder.md` before filing or looking for anything, and `references/corrections.md` before writing any output or acting on a correction. Read `references/story-schema.md` before Steps 4 and 5, and `references/stage-board.md` whenever the board is built or refreshed. Read `references/ai-first-pass.md` when a Run AI request arrives.

## Step 1: Pick the mode

**Always ask which mode. Never infer it.** Two exceptions: **Register** runs automatically when another skill finishes an output inside a project that has a ledger (say so in one line), and **Run AI** runs automatically when a board request arrives, because pressing the button already chose it.

| Mode | Use when | Go to |
|---|---|---|
| **Scope** | A brief has come in. Cut the method library down to a programme plan | Step 1a, then Step 2 |
| **Set up** | New engagement with a plan agreed, no ledger yet | Step 2 |
| **Retro-fit** | A project already in flight that has artifacts but no ledger | Step 2, then the audit in Step 3 |
| **Register** | Any skill or person has just produced something for this project. Runs automatically, along with auto-log | Step 3 |
| **Log & validate** | New research, synthesis, decisions or test results to record, or AI work that needs a human to sign it off | Step 3 |
| **Gate check** | "Are we ready to move on?" / "Where are we?" | Step 4 |
| **Build backlog** | G5 has passed, or Colin wants a draft map early | Step 5 |
| **Run AI** | A comment starting `▶ RUN AI` arrives from the stage board (someone pressed **Run AI** on a card). Runs automatically: the button press is the mode choice | Step 3b |

## Step 1a: Scope (brief → reductive selection → programme plan)

1. **Read the brief (BR-1).** Pull out:
   - the problem, and the project type (the map's "Type of project?");
   - the budget and timeline;
   - the known constraints;
   - what the client already has.

   Ask for anything missing. Never assume the budget or the timeline.
2. **Start from the spine.** Pre-select every ● method, sized to fit.
3. **Add methods by need.** For each Discovery group (Product, Business, Market & brand, Customer), decide whether the brief needs its questions answered. If so, pick the cheapest methods that answer them credibly. Then do the same for Vision ingredients and the Definition methods.
4. **Show the cut.** For each stage, list:
   - **In**: each method with a one-line reason tied to the brief;
   - **Out**: the risk of cutting it, e.g. "no diary study, so behaviour over time is assumed".

   If a spine item has to go, log a DC and lower the confidence of everything downstream.
5. **Cost it.** Hand the selection to `code-effort-estimate`.
6. **Write the programme plan (BR-3).** It always includes:
   - the research brief;
   - the methods;
   - effort and days per stage;
   - draft interview scripts per stakeholder role.

   Colin edits the cut before anything goes to the client. The proposal or SoW (BR-4) follows from the plan.

## Step 2: Set up the ledger and the board

1. **Load the selection.** Use the methods from Scope. With no Scope run, ask Colin which methods are in and which are out.
   - Every method that's out needs a one-line reason, because cutting something must be a deliberate decision.
2. **Create `<Client>_Evidence_Ledger.md`** with these tables:
   - **Artifacts:** method ID, method, artefacts, owner, status (to do, doing, needs a human, done, out + reason), location link, skill used.
   - **Items:** ID (EV/IN/BR/CN/NFR/AS/PR/ND/OP/TH/HY/DC/FL/TF/RK), statement, sources (IDs), confidence, provenance, validator, date, validation method.
   - **Gates:** G1 to G5, plus each stage's questions to be answered (answered yes or no, with evidence IDs), each with its criteria, status, who signed it off and when.
   - **Decisions:** DC entries, plus any changes to the schema or the gates.
3. **Map each artifact to its owner and its skill.** In a company-brain setup, map each one to a desk. Flag any artifact with no skill and no owner as a gap; those are candidates for new plugin skills.
4. **Set the stage to Brief & scope.** The board goes up as soon as a brief lands, so the scoping (Step 1a) and the proposal are tracked on it. Signing off the plan moves the project to Immersion. On Retro-fit, set the stage to the earliest one whose gate hasn't passed.
5. **Find and set up the project folder** per `project-folder.md`. Ask where the client project folder lives (a desktop folder or a shared cloud link), then pull the actual location in: the connected desktop folder's absolute path and machine, or the cloud link. Create the tree for in-scope methods. Record the location on the board, in the Project Brain and at the top of the ledger, so every ticket shows it. If the folder syncs from OneDrive, SharePoint or Drive, also ask for its web address (in Finder: right-click → OneDrive → View online, then copy the address bar) and set it as `folderWeb`, so the board's folder buttons open the card's inputs and outputs in one click.
6. **Publish the stage board dashboard** per `stage-board.md`, with the selection loaded into its store.
   - Record its URL in the ledger and in the Project Brain.
   - Any brief or inputs already in hand go into the inbox, each with a suggested next action.
7. **Put the project header bar on every artifact** made for the project (`assets/project-header.html`, rules in `stage-board.md` → Project header bar), so anyone can get back to the board and its Artefacts list from anything they open.

## Step 3: Log & validate

**Logging**
- Give each new item the next ID and its sources.
- Set confidence using the library's rules:
  - Strong: at least 2 independent sources, at least 1 primary.
  - Moderate: 1 primary source.
  - Assumption: no evidence.
- AI-generated synthesis, insights, profiles or findings go in as `[AI]`. **Never tag your own output `[AI✓]`.**

**Validation.** Colin or a named team member validates. For each `[AI]` item, prepare a short validation pack containing:
- every quote, checked to see it appears verbatim in the cited EV source (flag any that don't);
- each insight's claimed sources, checked to see they actually support it;
- segment coverage: which profiles or segments the evidence comes from, and who's missing;
- contradictions: any EV that cuts against the insight.

The human then accepts, edits or rejects each item. Record the validator, the date and the method, then retag as `[AI✓]` or delete.

**Retro-fit audit.** Go through what exists against the method library, and propose filing any existing files into method folders (`project-folder.md` rule 9):
- mark each artifact present, partial or missing;
- backfill EV and IN IDs from the existing research;
- tag anything with unknown origin as `[AI]` until someone vouches for it.

**Project folder (always on).** Everything made or collected for the project is filed in the project folder under its stage and method (`references/project-folder.md`). When someone says "it's in the project folder", look there, log what's new on the card, and get on with it. Nobody needs to re-upload files per card.

**Lineage and corrections (always on).** Every output records what it was built on (`uses`), and only checked work is built on. When anything is corrected, everything downstream is flagged out of date, reworked upstream-first and re-checked. Gates can't pass while anything is out of date. See `references/corrections.md`. This is what stops one wrong fact entered early from multiplying through everything after it.

**Auto-log (always on).** Inside a project with a stage board, anything Claude does gets logged to the matching card's knowledge as it happens, per `stage-board.md` → Card knowledge. That covers:
- processing transcripts or files;
- writing a summary, synthesis or other output;
- something the team tells it in chat that bears on a method.

Nobody has to ask. AI work is logged as `AI` and pulls the card into **Manual QA**, so the human check is built into the board. Say what was logged in one line.

**Registering an output.** Whenever a skill or person produces something for the project:
1. Match it to a method ID, or add it as an "unplanned" card.
2. Record its link, owner, skill and provenance.
3. Log its items.
4. Clear any inbox card it answers.
5. Republish the board.

## Step 3b: Run AI (a card's first pass, synthesis or report)

Someone pressed **Run AI** on a card and sent Claude a request: a comment on the board starting `▶ RUN AI · <method ID> <name>`, giving the task, its mode (first pass, prep, synthesis or report/deck), the skills, the folder, and any notes. The mapping per method is in `references/ai-first-pass.md`. The bar is work a senior Code practitioner would be happy to put their name to after one edit.

1. **Context first, silently.** Read the Project Brain, the ledger, the Research Repository, the card's knowledge and its folder (`inputs/` and `outputs/`), plus the cards it builds on (e.g. VI-1 reads every checked Discovery card). Use only what's current: honour corrections and out-of-date flags (`corrections.md`).
2. **Check what it rests on.** Build only on `[H]` and `[AI✓]` work. If the task needs inputs that aren't there (no transcripts for a synthesis, no data for an analytics check), or rests on unchecked AI work, that becomes a question rather than a guess.
3. **Ask once, in the chat.** Gather every question that would change the quality of the output (audience, scope, which inputs to use, format, deadline, anything missing) and ask them **together, once**, in the project chat (AskUserQuestion where available). Post one line in the comment thread saying the questions are in the chat. Set the card's `aiRun.status` to `asking`. If nothing needs asking, say what you assumed and go straight on. If nobody answers and the work can be done sensibly, take the most reasonable reading and state it at the top of the output.
4. **Do the work.** Set `aiRun.status` to `working`. Load and follow each mapped skill (and `code-design-playbook`). Bring in other installed skills where they raise the standard, and flag a gap if no skill fits. Reports and decks follow `code-brand-style`; long work is built in stages.
5. **Check it before handing over.** Trace every claim, quote and number to its source and verify the quotes are verbatim. Check the arithmetic by running it. Open any file you made to look at it. Name the weak spots (thin evidence, missing segments, assumptions).
6. **File and log it.** Save to the card's `outputs/` folder and verify it's there (`project-folder.md` rules 7 and 8). Add the project header bar to any artifact. Log it on the card as an `output` (or `summary` / `synthesis`) entry, `AI`, with `uses` filled and **every way to reach it**: `link` (the artifact or doc URL), `source` (its file in `outputs/`), `chat` (this chat's link), `run: true`, and `checks`: 2–5 specific, plain-English things a person should check (the claims most likely to be wrong, the readings that need a human call). Keep `body` to short sentences or a numbered list so the ticket can show it as bullets. That entry is what the ticket's **Outputs** panel shows, so whoever opens the card can get to the work in one click. Log any EV/IN/TF items in the ledger as `[AI]`. The card goes to **Manual QA**. Set `aiRun` to `{status: "done", entry: <the entry id>, action, at, chat}` so the card shows the output is ready. Update the folder index.
7. **Reply in the thread.** Say what was made, where it lives, what to check first, and the open questions. Keep it short; the work is in the folder and on the card. Never mark your own output checked, approve a question or pass a gate.

If the board can't be written to (for example it's shared publicly), do the work anyway, file it, and say in the thread and the chat that the card couldn't be updated and why.

## Step 4: Gate check

Check the folder (`project-folder.md` rule 6). Draft any missing answers to the stage's questions from checked card knowledge, with what each is built on (`stage-board.md`, Questions to be answered), so a person can read, edit and approve them. Then run the gate's criteria from the method library (each stage's questions to be answered, plus its checks) against the ledger, and report three things:
- **Pass / not yet.**
- **What's missing:** specific artifacts or items, each with its owner.
- **What's weak:** things that will hurt later. Examples: insights resting on a single source, profiles with no primary research behind them, `[AI]` items still unvalidated.

A gate only passes with a **named human sign-off** recorded in the ledger. When it passes, advance the stage and republish the board. Gates are proportional: Don't block on methods cut in Scope with a reason.

## Step 5: Build the backlog

Work in this order. Show Colin each stage before moving to the next; the playbook says mapping is a team activity, so these are drafts for the team session, not final answers.

1. **Backbone.** Themes go across the top. They come from the design challenge roadmap (VI-11), refined by the road map (DF-1). If neither exists, draft themes from validated JTBD (VI-3) and flag them as needing sign-off.
2. **Activities / epics.** Start from the JTBD / epics drafted in VI-3, refined by the prototyped flows (DF-4). Give each epic a one-line outcome and the HY IDs it serves.
3. **Steps and stories.** Break each flow into steps, and each step into stories. Add BR, NFR and CN-driven stories and enablers. Draw stories from:
   - DF-V test findings: open majors become stories;
   - DF-8: new or changed components, and accessibility criteria;
   - DF-6 / DF-7: the site map and navigation.
4. **Spikes.** Every open AS item and every unresolved CN becomes a spike story, or a DF-11 experiment if it can only be learned live, with a question and a timebox.
5. **Fill the schema.** Complete every field for every story, per `story-schema.md`.
6. **Prioritise and slice.** Score stories on user value, business value and effort or confidence, never effort alone. Then draw the MVP line (DF-10) as a vertical slice, followed by R1, R2 and so on. Each release (RL) states:
   - its outcome;
   - the hypotheses it tests;
   - its key dependencies;
   - why this cut.
7. **QA pass before anything goes to dev:**
   - **Trace check:** every story resolves to `[H]` or `[AI✓]` items. Anything that doesn't goes to the parking lot.
   - **Coverage check:** every validated IN and OP is covered by at least one story or explicitly out of scope. Every critical or major TF has been dealt with.
   - **DoR check:** run the Definition of Ready per story and list the failures.
   - **Consistency check:** every profile named in a story exists in VI-1, every design link points to the frozen DF-V version, and no story has a duplicate.
8. **Outputs:**
   - the story map (FigJam via `figma:figma-use-figjam` if connected, otherwise a whiteboard or table);
   - the story list as CSV for the dev team's tool (confirm the tool and its field mapping first);
   - the traceability matrix;
   - the refinement questions for the three-amigos session.

   Then run G5 and move the DF-9 and DF-10 cards to Done.

## Fences

- **Never:**
  - tag AI work `[AI✓]`;
  - pass a gate without a named human;
  - let an `[AI]`-only item ground a story;
  - silently drop untraced stories. They go to the parking lot.
- **Never record a folder path you haven't checked.** An output counts as filed only once its file is confirmed in the method's folder (`project-folder.md` rules 7 and 8). Artifacts and project docs get an exported copy; Figma and Miro get a link file.
- **Show, don't hide, the weak spots.** A thin evidence base is fine on a Lean engagement as long as it's visible. Confidence labels travel with each story into the dev tool.
- **Run AI makes drafts, never decisions.** Its output is always `AI`, lands in Manual QA, and is never sent to the client by Claude.
- **Draft, map, check and export freely.** Anything sent to the client or the dev team needs Colin's send.
- **The story schema is a cross-discipline contract.** Changes to it get agreed with dev and delivery and logged as DC entries.

## Connected skills

CodeDesign skills:
- `code-design-playbook`: always-on house method.
- `code-effort-estimate`: Scope costing (BR-3).
- `code-ux-review`: DI-P3, DI-P4.
- `code-market-review`: DI-M1.
- `code-ux-userprofile`: DI-M2, VI-1.
- `cx-journey-map`: VI-2.
- `code-brand-style`: any deck or playback.

Skills from other plugins (used where installed) are named per method in the library.
