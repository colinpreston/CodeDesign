# Lineage and Corrections: stopping one wrong fact from multiplying

In a loose chat, a wrong fact entered early gets reused by every later step, and the error compounds. This skill stops that in three ways:
1. Every output records what it was **built on**.
2. Only checked work can be built on.
3. A correction **flags everything downstream** and gets it redone, in order, and re-checked.

## 1. Lineage (every output records what it was built on)

Every card-knowledge entry Claude writes carries `uses`: the IDs of the entries it was made from. For example:
- the GROW summary's `uses` lists the transcript entries;
- the insight register's `uses` lists the summaries;
- a story's evidence trace lists the insights and test findings it rests on.

Facts from chat count too. If someone says "drop-off is 38%" and an output relies on it, the chat entry is in that output's `uses`. Ledger items follow the same pattern through their `sources`. `uses` is never left empty on a summary, synthesis or output. If something genuinely came from nowhere, it's an Assumption and is labelled as one.

## 2. Only build on checked work

Claude builds from `H` and `AI✓` entries only. If the only input available is an unchecked `AI` entry:
- say so;
- ask for it to be checked first;
- or, if told to go ahead, label the new output "built on unchecked work". The board then shows it as needing a human.

This is what keeps a single unchecked error from flowing forward.

## 3. Correcting something

Anyone can press **Something's wrong here** on a card-knowledge entry, or tell Claude in chat ("the 68% is wrong, it's 38%"). Before saving, the board shows **which later items will be affected**. The correction then:
1. **Writes a correction entry** (`prov: H`, `supersedes:` the old entry's ID, carrying the old entry's `uses`) with what's wrong and what's right.
2. **Marks the old entry** as `status: "corrected"`. It stays visible, struck through, for the audit trail. Nothing is deleted.
3. **Flags everything downstream** (anything whose `uses` chain reaches the corrected entry) as **out of date**. Each affected card moves to Needs a human, and the header counts the out-of-date items.
4. **Blocks gates:** a stage can't be signed off while it has out-of-date items. A stage already signed off shows "this sign-off rested on something that's changed. Re-check before relying on it". Reopening a gate is a human call. Claude doesn't unsign anything.

## 4. Reworking (Claude)

When there are out-of-date items, Claude:
1. **Lists the impact first:** each out-of-date item, its card, and what it was built on. Ask before redoing more than a handful, or anything a client has already seen.
2. **Redoes the items in order, upstream first.** For example: summary, then insight register, then profiles, then epics, then stories. Each new version is logged as a new entry with:
   - `supersedes` set to the out-of-date entry;
   - `uses` pointing at the corrected inputs;
   - `prov: "AI"`, so it waits to be checked again.
3. **Marks** each replaced entry `status: "corrected"`, with a correction note saying "rebuilt after <correction title>".
4. **Re-saves files:** writes new versions into the card's `outputs/` folder with a version suffix (`-v2`). Old versions are kept.
5. **Updates the ledger:** affected EV and IN items are corrected, and any story whose evidence trace touches a corrected item is flagged for refinement. Its acceptance criteria and confidence are re-checked.
6. **Reports in one line:** "Rebuilt 4 items on 3 cards after the drop-off correction. All need checking."

Something a client has already received (a playback deck, a SoW) is never quietly changed. Claude drafts the corrected version and flags that the client copy is now out of date, and Colin decides what to send.
