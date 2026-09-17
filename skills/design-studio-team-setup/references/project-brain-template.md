# <Client Name> — Project Brain

*Built <date>, using the design-studio-team-setup pattern (the "company brain + desks" anatomy Colin runs design consultancy engagements with). This doc is the shared context every desk reads before it acts — keep it current as the brief evolves rather than letting a desk work from a stale copy.*

## 1. Client

- **Client:** <name>
- **Industry / sector:** <...>
- **Key stakeholders:** <names, roles, who's the primary day-to-day contact>
- **How this engagement came about:** <optional context — referral, pitch, existing relationship, etc.>

## 2. The Brief

- **Problem / opportunity:** <what we're actually here to solve>
- **Objectives:** <what a good outcome looks like>
- **In scope:** <...>
- **Out of scope:** <...>
- **Constraints:** <budget, timeline, technical, brand, legal/compliance>
- **Success criteria:** <how we'll know it worked>
- **Key dates / milestones:** <kickoff, workshops, delivery checkpoints, go-live>

## 3. The Roster

| Role | One-liner | Brief |
|---|---|---|
| Lead UX Designer | Owns the design direction | `<ClientName>_Lead_UX_Designer_Brief.md` |
| Lead UX Researcher | Plans and runs research, surfaces insight | `<ClientName>_Lead_UX_Researcher_Brief.md` |
| Expert Workshop Facilitator | Designs and runs collaborative sessions | `<ClientName>_Workshop_Facilitator_Brief.md` |
| Product Consultant | Ties the work to product strategy and value | `<ClientName>_Product_Consultant_Brief.md` |
| Engineering Principal | Sense-checks feasibility and delivery reality | `<ClientName>_Engineering_Principal_Brief.md` |
| QA & Definition Lead | Turns approved design into user stories/acceptance criteria; checks build against them | `<ClientName>_QA_Definition_Lead_Brief.md` |
| Content/UX Writer | Owns copy, microcopy, and tone of voice | `<ClientName>_Content_UX_Writer_Brief.md` |
| Visual/Brand Designer | Owns visual identity, UI styling, and brand application | `<ClientName>_Visual_Brand_Designer_Brief.md` |
| Data & Insight Analyst | Analytics and usage data that inform decisions | `<ClientName>_Data_Insight_Analyst_Brief.md` |
| Meeting Notes Lead | Captures meeting transcripts/discussions, tracks open actions & requests, answers queries against past meetings | `<ClientName>_Meeting_Notes_Brief.md` |
| Delivery Manager | Coordinates the desks, tracks and actions gaps, sequences new multi-desk work before it starts | `<ClientName>_Delivery_Manager_Brief.md` |
| <Additional specialist role, if added> | <...> | `<ClientName>_<RoleName>_Brief.md` |

**The Boss:** Colin Preston, Product & Service Design Director. Plans the program of work, sets priorities and phasing, gives final send/edit/skip — see the fences below.

## 4. Research Repository — shared across every desk

`<ClientName>_Research_Repository.md` holds every research or data finding collected on this engagement, synthesized to a headline entry with a pointer back to the producing role's own log for full detail. Structured in the same three zones as every desk's own log — see Section 5. Every desk checks its Active Notes and Digest as standing context before starting new work, not just the Lead UX Researcher or Data & Insight Analyst.

## 5. Memory architecture — three zones, a standing index, plus targeted retrieval for specific questions

Every memory doc in this engagement — each desk's own log (Section 3) and the Research Repository (Section 4) — is written in three zones inside the same file, not as one endlessly-growing append-only stream:

- **Active Notes** — what's open right now: unresolved items, the last session or two's work. Appended to as normal, most recent first; read by default before picking up new work.
- **Digest** — standing facts and decisions that are still true but no longer "in flight." When something in Active Notes resolves, it collapses to one dense line here and the original moves to the Archive. Read alongside Active Notes as normal working context.
- **Archive** — the complete, unedited original entries, kept forever for traceability. Not read by default — pulled only to trace exactly when and why something happened, or to settle a dispute about what was said.

One desk is a deliberate exception to "not read by default": the Meeting Notes Lead's Archive is read routinely, because that desk's whole job is answering "what did we say/agree in that meeting" — its own log doubles as the meeting record. That's a specific case of retrieval mode (below), not a one-off.

**Query routing (picking up new work):** a desk picking up work reads this Brain, the Research Repository's Active Notes and Digest (not its Archive), and its own (plus any dependency desk's) Active Notes and Digest — never a full Archive to start a normal session.

**Retrieval (answering a specific question):** a direct question ("what did we decide about X," "what came out of that meeting") is a different mode, patterned on retrieval-augmented generation (RAG) — search first, answer only from what's found, and say where it came from. Search every memory doc that could plausibly hold the answer, including Archives, since a targeted question is exactly the case an Archive exists for. There's no vector database needed — the "retriever" is Claude reading the plain-text logs for matching entries; the "generator" is Claude answering only from what it found, naming the doc, zone, and date each answer came from so it can be checked against the source. If nothing matches, say so rather than guessing.

**Naming what this is:** the three zones are this pattern's version of a second brain — a curated knowledge base kept current by the desk that writes it, read whole rather than searched. Retrieval mode above is this pattern's RAG — a targeted search used only when a specific question calls for it, not how work normally gets picked up. Both run side by side on purpose; picking the right one for the situation is part of using this correctly.

**Digest Index — a standing rollup:** `<ClientName>_Digest_Index.md`, at the same project level as this Brain, holds nothing but every desk's current Digest, pulled together in roster order (Section 3, each section pointing back to that desk's own log), with the Research Repository's Digest at the top. It's one linked page showing what's actually true and settled across the whole engagement right now, without opening every desk's log to find out. The Delivery Manager keeps it current as part of its regular status check — no separate maintenance needed. Read it directly for a step-back view; a desk picking up new work still starts from this Brain and its own logs, not the index.

The Delivery Manager prunes: every status check (Section 7), it checks whether any desk's Active Notes has grown past a page or holds uncollapsed resolved items, and if so compresses it itself and updates that desk's section in the Digest Index, saying so in its action list. See `SKILL.md` Step 6 for the full rationale.

## 6. Fences — always Colin's "send"

- Anything sent to the client (a deliverable going out, an email, a workshop invite)
- Anything committing budget, scope, or timeline beyond what's already agreed above
- Any change to the brief itself (section 2)
- Anything that speaks for the client publicly or externally

Everything else — drafting, research, synthesis, workshop planning, prototyping, internal analysis — can run ahead and comes back as send / edit / skip.

## 7. How to actually use this

Start a session in this project and either name a role directly ("as the Lead UX Researcher, draft the discussion guide") or just describe the job ("we need to plan the kickoff workshop") — Claude reads this doc plus the named role's brief to pick it up, checking the Research Repository's Active Notes and Digest for anything already known first. For a new job that plainly needs more than one desk, hand it to the Delivery Manager first rather than guessing which role to name — it reads the roster's "Collaborates with" arrows and produces a short sequenced plan (who's needed, in what order, what each hands off) before any desk actually starts, and that plan comes back as send/edit/skip like anything else. For a specific question instead of a job to pick up — "what did we decide about X," "what came out of that meeting" — a desk switches into retrieval mode instead (Section 5): it searches every relevant log, including Archives, and answers only from what it finds, naming the doc, zone, and date each answer came from. Ask the Delivery Manager for a status check any time with something like "what's outstanding" or "give me the team update" — this also prunes any desk's log that's grown past a page of Active Notes and refreshes the Digest Index (Section 5). For a quick read on what's currently true across the whole engagement without opening every desk's log, check the Digest Index directly. Hand a meeting transcript or notes to the Meeting Notes Lead any time to get it logged, and ask it directly what was said or agreed in a past meeting. If a new specialist turns out to be needed partway through, add a row above, write that role's brief the same way as the others, and add its section to the Digest Index.

## 8. Skill sources — installed vs. recommended vs. pending Colin's install

Every role's brief lists skills to check automatically. Note here which are already installed, which are recommended but not yet installed, which repo they'd come from, and what Colin said when asked.

**Always-on studio skill:** `code-design-playbook` (Code's internal design team curriculum) ships bundled with this plugin and is standing context for every design-facing desk on this roster — not a per-role recommendation to track here.

## 9. Log of changes to this brief

*Append here whenever the brief itself changes (scope, timeline, objectives) — this is the changelog Colin and every desk can check to see what's shifted since they last looked.*

- <date> — <what changed and why>
