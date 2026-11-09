# Story Schema & Definition of Ready

This is the handoff contract between design and dev. Before first use, agree the fields with the client's dev lead and Code's engineering lead. Log anything they change in the ledger's Decisions table.

## Story map structure

```
Theme (TH, from VI-11 / DF-1)          — the user goal, across the top
  └─ Activity / Epic (EP)     — a JTBD/epic from VI-3, shaped by DF-4 flows
       └─ Step                — what the user does, left to right
            └─ Story (ST)     — features, stacked by priority
                 └─ Release line: MVP | R1 | R2 …
```

Each epic gets a one-line outcome and the hypothesis IDs it serves.

**Slicing rule:** the MVP is a vertical slice. It must deliver one theme's goal end to end, however thinly. Horizontal slices (breadth across the whole map, no depth) are allowed only when the release outcome needs them, and the RL record must give the reason.

## Story fields

| Field | Content | Required |
|---|---|---|
| ID | ST-### | Yes |
| Title | Verb-first, ≤ 8 words | Yes |
| Type | Story / Spike / Enabler | Yes |
| Epic · Step · Release | EP-## · step name · RL-# | Yes |
| Story | As a [profile from VI-1], I want [need], so that [outcome] | Yes (Spike: the question and the timebox instead) |
| Acceptance criteria | Given / When / Then. Include error, empty and edge states from DF-4 flows | Yes, 3+ for stories |
| Accessibility criteria | From DF-8 / DI-P8, with WCAG references | Yes if there's any UI |
| Content | Link to DF-5 copy, or "copy TBC" plus an owner | Yes if there's any UI |
| Design link | The frozen DF-V Figma frame name or URL | Yes if there's any UI |
| Components | New / changed / existing (from DF-8) | Yes if there's any UI |
| Measurement | Analytics events from DF-2 / DF-3 | If the release outcome needs it |
| NFRs | NFR-### refs | If any apply |
| Evidence trace | TF / IN / BR / CN / NFR IDs | **Yes. No trace means parking lot** |
| Confidence | Strong / Moderate / Assumption | Yes |
| Dependencies | ST / external refs | If any |
| Open questions | For three amigos | If any |

## Definition of Ready (checked per story)

1. **INVEST:** the story is independent, negotiable, valuable, estimable, small (fits a sprint) and testable.
2. The evidence trace resolves to ledger items marked `[H]` or `[AI✓]`, never `[AI]` alone.
3. Assumption-confidence stories either have a paired spike or test, or are flagged by the PO as a conscious bet.
4. Every UI story has a design link to the **frozen** DF-V version.
5. The acceptance criteria cover the unhappy paths shown in the DF-4 flows.
6. Accessibility criteria are present.
7. No open question blocks estimation. A question that only blocks build can stay open, as long as it has an owner.

## Parking lot

Stories with no trace aren't deleted. They go to a parking-lot column labelled **"Unevidenced: needs a source"**. The PO either finds a source (BR counts) or drops the story. They never enter a release silently.

## Export

- Default output is a CSV with these columns: Summary, Issue Type, Epic Link, Description (story + AC + a11y + content + design link), Labels (release, confidence), Evidence, Dependencies.
- Confirm the target tool (Jira, Azure DevOps, Linear) and its field mapping with the dev lead before the first export.
- If the tool has custom fields, map Evidence and Confidence to them. Otherwise put both in the Description under a **Trace** heading.

## When evidence changes

A story whose evidence trace touches a corrected item is flagged **out of date** (see `corrections.md`). It goes back to refinement:
- re-check its acceptance criteria and confidence against the corrected evidence;
- if it's already estimated, tell the dev lead what changed rather than editing quietly.
