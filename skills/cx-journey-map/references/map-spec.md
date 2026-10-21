# CX map spec — rows, cards and the JSON format

This is the house format for Code's "Customer journey full detail" map, modelled on the Pure Pet Food digital customer CX map. `scripts/build_map.py` turns a JSON spec in this shape into the map. `references/example-map.json` is a complete, fictional example.

## The rows, top to bottom

| Row | Spans | What goes in it | Card style |
|---|---|---|---|
| **CX objective** | Stage | The stages of the journey (e.g. Considering, Sign-up, First use) | Orange chevrons |
| **Funnel / customer stage** *(optional)* | Any run of steps | The client's own lifecycle bands, in their terms | Purple bands |
| **Scope band** *(optional)* | From step → to step | What this engagement is actually working on | Dashed purple outline |
| **Customer steps** | Step | One action per step, numbered, with who's doing it | White card, purple edge, segment footer |
| **Flow** *(optional, recommended)* | Whole journey | Main path, exits, loops, re-entry and time gaps | Dashed lines over the step columns |
| **Data** | Step | Known numbers with their source, and the numbers still missing | Orange figure; red "?" for data needed |
| **Positives** | Step | What works for the customer | Green with up-triangle |
| **Customer pains** | Step | What gets in their way | Red with down-triangle |
| **Internal challenges** *(shown if any)* | Step | What stakeholders and client teams say, as quotes with the speaker | White, magnifier icon |
| **Comms** | Step | CRM and outbound messages, happening or missing: emails, texts, calls, letters, ads, confirmations, reminders. Website content gaps are pains or HMWs, not comms | Grey-green; dashed red when missing, labelled with the channel |
| **Mindset thinking** | Step | Real customer quotes, tagged to a mindset profile | Quote card, profile-coloured footer |
| **Evidence** | Stage | What each stage is built on, plus whether there's any user evidence | Teal chips; red or tag-coloured user chip |
| **Research needed** | Stage | Each gap: priority, question and method | Teal cards |
| **HMW** | Step | How might we… opportunities | Yellow stickies |

## Conventions

- **Every number carries its source**: who measured it, and when. If a figure comes from a proxy (another client's portfolio, a different market), say so in the source line.
- **Never fill a gap with a guess.** Use `{"label": "...", "needed": true}`, which renders as a red "?" "Data needed" card. These cards are how the map shows where the research gaps are.
- **Participant tags.** Prefix any text with `P1|`, `P2|` and so on to mark it as first-hand from that interview. It renders with a red tag. List each participant in `participants` so the key explains the tag. A participant's quotes use a profile entry with `"participant": true`, so it's kept out of the mindset-profile legend.
- **Profiles are provisional until interviews validate them.** Say so in `profiles_note`.
- **Quotes stay short and attributed.** Paraphrase anything long.
- **Evidence row honesty.** `user_evidence` should say plainly "No user evidence" until there is some. When it mentions an interview, the chip turns from red to the participant colour.

## JSON format

```json
{
  "client": "Name shown in the header badge if badge.top is absent",
  "page_title": "Browser / artboard title",
  "badge": {"top": "SHORT NAME", "sub": "Sub-label"},
  "title": "Customer journey full detail",
  "subtitle": "Version, sources, interview count, date",
  "profiles_title": "Provisional mindset profiles",
  "profiles_note": "Drawn from desk research. To be validated in interviews.",
  "profiles": {"key": {"name": "Profile name", "color": "#hex", "desc": "one line"}},
  "participants": {"P1": "What P1 was"},
  "stages": [{"name": "Stage", "steps": 2, "evidence": ["Source"], "user_evidence": "No user evidence",
              "confidence": "low", "note": "One line", "research": [{"priority": "High", "question": "…", "method": "…"}]}],
  "funnel_title": "Customer stage",
  "funnel": [{"name": "Band", "desc": "One line", "steps": 3}],
  "scope": {"from": 2, "to": 5, "label": "Our scope: …"},
  "internal_subtitle": "What stakeholders say",
  "steps": [{
    "title": "Step text", "who": "Segment",
    "data": [{"label": "Metric", "value": "12%", "source": "Where, when"}, {"label": "Metric we lack", "needed": true}],
    "positives": ["…"], "pains": ["…", "P1|…"],
    "internal": [{"quote": "…", "source": "Who said it"}],
    "comms": [{"text": "…", "channel": "Email"}, {"text": "Missing: …", "channel": "Gap", "missing": true}],
    "mindset": [{"quote": "…", "profile": "key", "source": "Where it came from"}],
    "hmw": ["…? (the card adds 'How might we')"]
  }],
  "flow": {
    "exits": [{"step": 3, "label": "Exit: …", "above": false}],
    "loops": [{"from": 1, "to": 3, "kind": "reentry|tag|positive|neutral", "label": "…", "both_ends": false}],
    "gaps": [{"from": 4, "to": 5, "label": "P1|Waited 3 days for …"}],
    "end_label": "Where the journey leads next"
  },
  "footnote": "Sources and caveats line",
  "height": 3200
}
```

Rules the builder checks before it writes anything:
- the stages' `steps` add up to the number of steps;
- the funnel bands' `steps` add up to the number of steps;
- every flow `step`, `from` and `to` is within range.

### Flow loop kinds

| `kind` | Colour | Use for |
|---|---|---|
| `reentry` | Teal | People coming back after an exit (retargeting, emails) |
| `tag` | Participant red | A loop seen first-hand in an interview |
| `positive` | Green | A healthy loop (monitor → tweak → spend more) |
| `neutral` | Purple | Any other repeat or back-and-forth |

A loop with `from` equal to `to` draws a small loop around a single step, such as "wrong goal → stop → rebuild". Loops that overlap get stacked into separate lanes automatically.
