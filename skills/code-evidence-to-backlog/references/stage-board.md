# Stage Board: the project's Kanban dashboard

Every project gets a **Project stage board**, a dashboard artifact that shows:
- where the engagement sits on Code's process map;
- which methods were chosen for it;
- what each method has produced, with links to the artefacts.

It's a shared, live page. The team can drag cards, tick off questions and sign off gates, and Claude writes to the same store when a skill registers an output. The template's source is in `assets/stage-board.html` (published reference: "Project stage board").

## What it shows

- **Header:**
  - the project name;
  - the current stage;
  - questions answered towards the next gate;
  - the **Needs a human** count (highlighted when it's above zero);
  - methods done out of methods in scope.
- **Stepper:** Brief & scope → Immersion → Discovery → Vision → Definition, each with its headline question. A new project starts in **Brief & scope**. Scoping happens on the board, and signing off the plan moves the project to Immersion.
- **Inbox:** new inputs (a brief, an email, a research pack), each with a suggested next step. People add items, and Claude adds items with an `action`.
- **Board view:**
  - **Columns:** one per stage. The current stage is outlined.
  - **Lanes:** each column has four lanes: To do · Doing · Needs a human · Done.
  - **Cards:** only **in-scope** methods appear. Each card shows its ID, name, artefacts, a spine tag, provenance (H / AI / AI✓), owner, a linked indicator and an "early" tag.
  - **Questions to be answered:** sit at the foot of each column, ticked off as they're answered.
  - **Gate card:** sign-off unlocks only when every question is ticked and nothing is waiting in Needs a human. Signing off moves the stage on and records who signed and when.
- **Scope view:** the full method library as tick lists by stage and group. This is the reductive step: untick to cut, with a reason (required in practice for spine methods). The count of cut spine methods shows at the top.

## The store (what Claude reads and writes)

Use `db_list` / `db_get` to read and `db_write` to write, on the project's board artifact. **Read before you write.** Every op on an existing document needs its `ifVersion`.

| Path | Body | Written by |
|---|---|---|
| `board/meta` | `{name, stage, folderRoot, folderRootUrl?, gates: {<stageId>: {by, at}}, edit}`. Stage ids: `brief`, `immersion`, `discovery`, `vision`, `definition` | Setup (Claude); people (name, gate sign-off) |
| `cards/<methodId>` | `{in, lane, owner, link, prov, note, reason, early, folder?, folderUrl?, folderFiles?, edit}`. `folder` overrides the default path, `<NN Stage>/<ID> <name>` (see `project-folder.md`). `folderUrl` is the folder's link when the root is Drive or SharePoint. `folderFiles` is the file count. `lane` is one of `todo`, `doing`, `human`, `done`. `prov` is one of `H`, `AI`, `AIV` (AIV means AI✓) | Scope and Register (Claude); people |
| `questions/<qid>` | `{answer, uses, prov, by, at, answered, approvedBy?, approvedAt?, previous?, edit}`. `answer` is the text. `uses` is the card-knowledge entry IDs it rests on. `prov` is `AI` for a Claude draft and `H` once a person writes or edits it (`AIV` once a person approves an AI draft). `answered` means **a person has approved it**. `previous` keeps the last answer when someone edits | Claude drafts (`answer`, `uses`, `prov: "AI"`, `answered: false`); people edit and approve |
| `inbox/<id>` | `{id, text, action, at, done}` | People and Claude |
| `entries/<id>` | **Card knowledge.** `{id, card, type, title, body, source, link, prov, by, at, validatedBy?, validatedAt?, method?}`:
- `card` is a method ID;
- `type` is one of `transcript`, `summary`, `synthesis`, `output`, `chat`, `note`, `source`;
- `prov` is `H`, `AI` or `AIV`;
- `by` is `"claude"` or a user id;
- `uses` is a list of entry IDs this one was built from. `supersedes` is the ID of the entry this replaces. `status` is `"corrected"` once something has replaced it, with `correction`, `correctedBy` and `correctedAt`. An entry is **out of date** when anything in its `uses` chain is corrected (see `corrections.md`). `body` is at most ~20,000 characters. Anything longer goes in a project file, linked from `link` or `source`, with a summary in `body`. | Claude (automatically); people (notes, and "Mark checked") |

Defaults when a card has no document: spine methods are in, everything else is out, and the lane is `todo`. Method IDs and question IDs are the ones in `method-library.md` and in the page's `LIB` and `QS` lists. Keep the two in step when either changes.

## Card knowledge (automatic)

Every card carries a running log of everything known or done for that method. Claude adds to it **without being asked** whenever it works on the project:

| What happened | Entry |
|---|---|
| Transcripts or files were added to the project folder for a method | `type: "source"` or `"transcript"`, `prov: "H"`, `source` = the file path (one entry per file, or one per batch) |
| Claude transcribed, cleaned or summarised them | `type: "summary"`, `prov: "AI"`, `body` = the summary |
| Claude synthesised across sources (insights, GROW, themes, profiles) | `type: "synthesis"`, `prov: "AI"`, `body` = the synthesis, plus EV/IN IDs if the ledger is in use |
| A skill produced an artefact (deck, map, report, estimate) | `type: "output"`, `prov: "AI"` (or `"H"` if a person made it), `link` = the artefact |
| Someone told Claude something relevant in the project chat (a decision, a fact from a meeting, a correction) | `type: "chat"`, `prov: "H"`, `body` = their point in their own words, kept short |

**Matching to a card.**
- Match by the method being done: stakeholder interviews go to DI-B1, a competitor review to DI-M1, and so on.
- If two cards fit, or none does, ask once ("Log this against DI-B1 or DI-B3?").
- If the method is out of scope, log it anyway against its card, mark the card `in: true, early` as needed, and say so.

**Lane effects.** An `AI` entry moves its card to `human`, unless it's already there. The card can't go to Done while unchecked AI entries remain.

**Checking.**
- A person presses **Mark checked** on an entry and says how they checked it. That sets `prov: "AIV"`, the validator and the method.
- When the last AI entry on a card is checked, the board moves the card to Done.
- Claude never marks its own entries checked.

**Telling Colin.** One line per batch, e.g. "Logged 5 transcripts and a GROW summary on DI-B1 (needs checking)."

**The ledger.** When the Evidence Ledger is in use, the same work also gets EV/IN items there. The card entry carries their IDs in its title or body so the two can be traced.

## Questions to be answered

Each stage's questions (from the map) sit at the foot of its column. Each one shows:
- **its answer**;
- **who wrote it** (AI draft, human, or AI approved);
- **what it's built on**, with links to the cards and entries.

Each question is a **ticket**: a card at the foot of its column showing its status (no answer yet, awaiting approval, approved, or ⚠ re-check), a two-line preview of the answer, its provenance and how many sources it has. Clicking it opens the full ticket overlay, the same as a method card. That shows the full answer to edit, the **Built on** list (each source links through to its card, and corrected or out-of-date sources are flagged), who approved it and when, and the previous answer. The buttons are **Save answer**, **Save and approve** and **Withdraw approval**. An edit is saved as a human answer and needs approving again. The tick means **"I approve this answer"**. It stays disabled until there's an answer to approve. A question counts towards the gate only if its answer is approved and nothing it rests on has since been corrected.

Claude **drafts** answers: when a stage's cards have enough checked knowledge, or when asked ("draft the Discovery answers"). It writes the answer as a short plain statement, then:
- fills `uses` with the checked entries it drew on;
- never uses unchecked AI entries;
- if the evidence doesn't answer the question, says so in the answer ("Not yet known: no customer research done") rather than guessing.

Claude never ticks approval.

## How Claude uses it

- **Setup:**
  1. Publish a fresh board for the client from `assets/stage-board.html`, titled `<Client> stage board`.
  2. Declare `{db: {}, user: {scopes: ["profile"]}}`.
  3. Write `board/meta` with the stage set to `brief`.
  4. Write a `cards/<id>` document for every method Scope selected or cut, with the reason for each cut.
  5. Record the URL in the ledger and the Project Brain.
- **Register an output:** set the card's `link`, `owner` and `prov`, and its `lane`:
  - `human` if it holds `[AI]` items;
  - `done` if it's `[H]` or `[AI✓]`.

  If the card belongs to a later stage, add `early: true`. Clear any inbox item the output answers. Tell Colin in one line, e.g. "DI-M1 competitor review is on the board (Discovery, early)".
- **A new input lands:** add an inbox item with a suggested `action`, e.g. "Draft proposal (BR-4) with code-effort-estimate".
- **Never on its own:**
  - approve (tick) a question. Drafting the answer is fine;
  - sign off a gate;
  - set `prov: "AIV"`.

  These are human acts. Claude can set them only when Colin explicitly says so, and must note who validated it.

## Build notes

- Single-file HTML, styled with Code's palette (navy, lime and aqua; Poppins as the stand-in for the WPP font).
- Every value is rendered with `textContent`. Links open only if they're `http(s)`.
- Read-only viewers see the board without its controls.
- The page prints as a stand-up snapshot.
