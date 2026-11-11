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
  - the **Manual QA** count (highlighted when it's above zero);
  - methods done out of methods in scope.
- **Stepper:** Brief & scope → Immersion → Discovery → Vision → Definition, each with its headline question. A new project starts in **Brief & scope**. Scoping happens on the board, and signing off the plan moves the project to Immersion.
- **Inbox:** new inputs (a brief, an email, a research pack), each with a suggested next step. It's hidden behind an **Inbox** button in the tab bar, with a red count badge showing how many items are waiting. Clicking it opens or closes the panel, and each viewer's browser remembers whether it was open. Items are cleared with **Done**. People add items, and Claude adds items with an `action`.
- **Board view:**
  - **Columns:** one per stage. The current stage is outlined.
  - **Lanes:** each column has four lanes: To do · Doing · Manual QA · Done.
  - **Cards:** only **in-scope** methods appear. To keep the board easy to scan, a card face shows just its ID (with a small dot for spine methods), its name, and only the badges that apply: provenance (H / AI / AI✓), owner, "early", folder and knowledge counts, "to check" and "out of date". Everything else lives in the ticket.
- **The ticket** (click a card), top to bottom:
  1. **Header:** ID and name, stage, what the method makes, then **📌 Still to do**: a checklist, not an input box. **✦ AI** items are worked out from the card and update themselves (check each unchecked AI output, rework anything out of date, answer Claude's questions, make the first output, move to Done when all is checked), each with **Show** to jump to the entry; plus any `aiTodo` lines Claude writes. **👤 Note** items are what a person adds in the one-line box (Enter or Add) and ticks off when done.
  2. **▶ Run AI** (see Run AI below).
  3. **Outputs:** the work. Each output says who made it (👤 Made by a person / ✦ Made by AI · to check / ✦ Made by AI · checked) with **Open ↗** (the artifact or web link), the file's full local path, the **Claude chat** that made it and **Details**. The card's folder path sits at the top. **+ Add something you made** lets a person log their own output: a name, plus a web link or the file name in the card's `outputs/` folder.
  4. **Knowledge on this card**, grouped: **✦ AI work to check** (AI work waiting for a person, and anything out of date), **📥 Inputs** (sources and transcripts the work is based on), **✓ Checked and other notes**, and **Corrected** (kept for the record).
  5. **Details:** lane, who made the main work, owner, and the card's folder.
  - **Run AI:** a dark grey **▶ Run AI** strip under every card where an AI first pass makes sense (all methods except IM-4 and IM-6; never on Done cards, never for read-only viewers). It opens the card's ticket at the Run AI panel. See Run AI below.
  - **Empty lanes** collapse to a thin dashed label, so full lanes stand out.
  - **Questions to be answered:** sit at the foot of each column, ticked off as they're answered.
  - **Gate card:** shown in full on the current stage only; other stages show a single "not yet" or "passed" line. Sign-off unlocks only when every question is ticked and nothing is waiting in Manual QA. Signing off moves the stage on and records who signed and when.
- **Artefacts view:** every artefact made or collected for the project in one list, by stage and method: each item's type, provenance, an **Open ↗** link to the artifact (if it has one) and its folder file as a link (shown once `folderWeb` is set). Filter: outputs only, or outputs and inputs. Built from card knowledge and card links, so anything logged appears here automatically. `board/meta.links` (`[{title, url, note}]`) adds project-level links (the Project Brain, a shared drive) at the top. Every project artifact's header bar links to `#artefacts`.
- **Scope view:** the full method library as tick lists by stage and group. This is the reductive step: untick to cut, with a reason (required in practice for spine methods). The count of cut spine methods shows at the top.

## The store (what Claude reads and writes)

Use `db_list` / `db_get` to read and `db_write` to write, on the project's board artifact. **Read before you write.** Every op on an existing document needs its `ifVersion`.

| Path | Body | Written by |
|---|---|---|
| `board/meta` | `{name, stage, folderRoot, folderRootUrl?, folderWeb?, gates: {<stageId>: {by, at}}, edit}`. `folderWeb` is the project folder's web address in OneDrive, SharePoint or Drive. Use the address bar from "View online" (it has `?id=`), not a sharing link, so the board can build a direct link to every card's `inputs/` and `outputs/` folder and to each output file. With a sharing link or Drive, links go to the project folder only. Stage ids: `brief`, `immersion`, `discovery`, `vision`, `definition` | Setup (Claude); people (name, gate sign-off) |
| `cards/<methodId>` | `{in, lane, owner, prov, todo, aiTodo?, reason, folder?, folderUrl?, folderFiles?, link?, note?, early?, edit}`. `todo` is the person-added Still to do lines (newline-separated, ticking one removes it); `aiTodo` is an array of short actions Claude adds when it logs work (e.g. "Ask Panache whether rep ordering is in scope"). | Scope and Register (Claude); people |
| `questions/<qid>` | `{answer, uses, prov, by, at, answered, approvedBy?, approvedAt?, previous?, edit}`. `answer` is the text. `uses` is the card-knowledge entry IDs it rests on. `prov` is `AI` for a Claude draft and `H` once a person writes or edits it (`AIV` once a person approves an AI draft). `answered` means **a person has approved it**. `previous` keeps the last answer when someone edits | Claude drafts (`answer`, `uses`, `prov: "AI"`, `answered: false`); people edit and approve |
| `cards/<id>.aiRun` | `{status, action, mode, thread, by, at}` while a Run AI request is open. `status` is `requested` (set by the board when sent), `asking` (Claude has questions in the chat) or `working`; When the output is logged, Claude sets `{status: "done", entry, action, at, chat}`: `entry` is the output's entry id, and the card face shows "AI output ready" until a human checks it. The card face and ticket show the status | Board (on send); Claude |
| `inbox/<id>` | `{id, text, action, at, done}` | People and Claude |
| `entries/<id>` | **Card knowledge.** `{id, card, type, title, body, source, link, chat?, run?, checks?, prov, by, at, validatedBy?, validatedAt?, method?}`. On an output, `link` is the artifact or doc URL, `source` its file in the project folder, and `chat` the link to the Claude chat that made it; `run: true` marks Run AI work. `checks` is 2–5 plain-English things a person should check for this item ("The rep-ordering contradiction reads the same to you"); without it the board shows a standard checklist for the entry's type. Write `body` as short sentences or a numbered list, which the ticket turns into bullets Titles may start with a ledger code (`EV-001 Panache RFQ`); the board shows the plain name first, then the file name, with the code small and grey, because the codes mean nothing outside the ledger:
- `card` is a method ID;
- `type` is one of `transcript`, `summary`, `synthesis`, `output`, `chat`, `note`, `source`;
- `prov` is `H`, `AI` or `AIV`;
- `by` is `"claude"` or a user id;
- `uses` is a list of entry IDs this one was built from. `supersedes` is the ID of the entry this replaces. `status` is `"corrected"` once something has replaced it, with `correction`, `correctedBy` and `correctedAt`. An entry is **out of date** when anything in its `uses` chain is corrected (see `corrections.md`). `body` is at most ~20,000 characters. Anything longer goes in a project file, linked from `link` or `source`, with a summary in `body`. | Claude (automatically); people (notes, and "Mark checked") |

Defaults when a card has no document: spine methods are in, everything else is out, and the lane is `todo`. Method IDs and question IDs are the ones in `method-library.md` and in the page's `LIB` and `QS` lists. Keep the two in step when either changes.

## Card knowledge (automatic)

Every card carries a running log of everything known or done for that method. Claude adds to it **without being asked** whenever it works on the project (see the table below).

**How it shows in the ticket.** Each entry is a single collapsed line: type, who made it (👤 Person / ✦ AI / ✦ AI · checked) and its plain name, with any ledger code small and grey. Clicking it opens labelled sections: **✅ What to check** (AI work only), **📝 What the AI says** (or **What it says**), **📄 Where it is** (open link or path), **📚 Documents used by AI** (each with its file), **🔗 Used in**, who made it and when, then **When you've checked it, say how** with **Mark checked**, and a small **Something's wrong? Correct it** link. There's no free-text note form on the card: people add outputs in the Outputs section and what's left in **Still to do**.

What gets logged:

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

Each question is a **ticket**: a compact row at the foot of its column, showing the question with a status dot (grey: no answer yet, amber: awaiting approval, green: approved, red: re-check). Clicking it opens the full ticket overlay, the same as a method card. That shows the full answer to edit, the **Built on** list (each source links through to its card, and corrected or out-of-date sources are flagged), who approved it and when, and the previous answer. The buttons are **Save answer**, **Save and approve** and **Withdraw approval**. An edit is saved as a human answer and needs approving again. The tick means **"I approve this answer"**. It stays disabled until there's an answer to approve. A question counts towards the gate only if its answer is approved and nothing it rests on has since been corrected.

Claude **drafts** answers: when a stage's cards have enough checked knowledge, or when asked ("draft the Discovery answers"). It writes the answer as a short plain statement, then:
- fills `uses` with the checked entries it drew on;
- never uses unchecked AI entries;
- if the evidence doesn't answer the question, says so in the answer ("Not yet known: no customer research done") rather than guessing.

Claude never ticks approval.

## How Claude uses it

- **Setup:**
  1. Publish a fresh board for the client from `assets/stage-board.html`, titled `<Client> stage board`.
  2. Declare `{db: {}, user: {scopes: ["profile"]}, comments: {}}`. `comments` is what lets the Run AI button send a request to Claude.
  3. Write `board/meta` with the stage set to `brief`.
  4. Write a `cards/<id>` document for every method Scope selected or cut, with the reason for each cut.
  5. Record the URL in the ledger and the Project Brain.
- **Register an output:** log it as an `output` / `summary` / `synthesis` entry with every way to reach it (`link`, `source`, and `chat` when Claude made it), then set the card's `link`, `owner` and `prov`, and its `lane`:
  - `human` if it holds `[AI]` items;
  - `done` if it's `[H]` or `[AI✓]`.

  If the card belongs to a later stage, add `early: true`. Clear any inbox item the output answers. Tell Colin in one line, e.g. "DI-M1 competitor review is on the board (Discovery, early)".
- **A new input lands:** add an inbox item with a suggested `action`, e.g. "Draft proposal (BR-4) with code-effort-estimate".
- **Never on its own:**
  - approve (tick) a question. Drafting the answer is fine;
  - sign off a gate;
  - set `prov: "AIV"`.

  These are human acts. Claude can set them only when Colin explicitly says so, and must note who validated it.

## Run AI

The **▶ Run AI** button gets Claude to do a card's first pass: a draft, a prep pack (guide or plan), a synthesis of what's in the card's inputs, or a report or deck. What each method's button does is in `ai-first-pass.md`, and the same list sits in the page as `RUN`. Keep the two in step.

- **Outputs panel** (in every ticket, under Run AI): the card's folder as a full local path (no file or folder links, see below), then every output, summary and synthesis logged on the card, newest first, each as a tile with its type, provenance, "to check" and date, and the file's full local path, and buttons to **Open ↗** the artifact, open the **Claude chat ↗** that made it, and jump to its **Details** in Card knowledge. The latest Run AI output is marked "New from Run AI". The card face shows a 📄 outputs count. This is how anyone finds what AI made for a method: open the card, it's at the top.
- **The panel** (top of the ticket) shows what Claude will do, the skills it will use and what it reads first. Methods with two jobs (prep before fieldwork, synthesis after) offer both, pre-picking synthesis when the card already has inputs. If a synthesis has nothing in `inputs/`, it warns. There's an optional notes box ("focus on the rep journey").
- **Send to Claude** posts the request as a comment on the card and sends it to Claude (the `comments` capability's `sendToClaude`), which wakes the project chat. The card moves from To do to Doing and gets an `aiRun` status. Claude takes it from there (SKILL.md Step 3b): it reads the context, asks its questions once in the chat, does the work, files it, logs it, and replies in the thread.
- **When it can't send** (no Claude chat watching the board, a viewer who isn't an editor, a view without comments), the panel says why and offers **Copy request**, so it can be pasted into the project chat instead.
- Only editors can send. The output always lands as `AI` in Manual QA.

## Project header bar

Every artifact made for a project with a stage board carries a header bar at the top: **← <Project> stage board** · what this is (method ID and name) · **All artefacts** (the board's `#artefacts` view). It's how people get back to the board and on to everything else from any artifact.

- **Hand-built pages** (HTML artifacts, dashboards, prototypes): paste `assets/project-header.html` straight after `<body>` and fill `{{BOARD_URL}}`, `{{PROJECT}}` and `{{HERE}}`.
- **Docs:** the first line of the doc is the same three links as text: `[← <Project> stage board](<url>) · <ID> <name> · [All artefacts](<url>#artefacts)`.
- **Typed artifacts whose page Claude can't change** (Slides, Design): no bar is possible. Put the board link in the speaker notes or a frame label where the type allows. The board's Artefacts view links to them either way.
- Add the bar when the artifact is created; retro-fit it to existing ones when a project adopts this skill. Don't edit client-facing content to add it without asking.

## Build notes

- Single-file HTML, styled with Code's palette (navy, lime and aqua; Poppins as the stand-in for the WPP font).
- Every value is rendered with `textContent`. Links open only if they're `http(s)`.
- Read-only viewers see the board without its controls.
- The page prints as a stand-up snapshot.

- **Archive / delete a method card** (ticket → Details → bottom): **Archive** hides the card from the board with an optional reason (`archived: true`, `archivedReason`); the board header shows "🗄 n archived · see Scope", and Scope lists archived cards with **Restore**. **Delete** removes the card and its knowledge after a confirm. Use archive for methods cut from scope (keeps the reason on record); delete only for cards made in error.

- **File paths, not file links.** Browsers never let a web page open local files or Finder, and OneDrive / Office "open in app" links proved unreliable (wrong signed-in account, sandboxed frame). So the board shows **the full local path** in a grey box wherever a file or folder is meant: the card's folder at the top of Outputs, each output tile, "Where it is" in card knowledge, the folder box in Details and the Artefacts tab. One click selects the whole path to paste into Finder's Go to Folder (⌘⇧G). Claude artifacts and Claude chats keep their real links. `folderWeb` / `PAGE_FOLDER_WEB` are no longer used.
- **Optional local links page.** `scripts/make_links_page.py` writes `_Open files.html` into the project folder for anyone who wants a clickable list on their own machine (PDFs and notes open locally). Only offer it; don't run it by default.
