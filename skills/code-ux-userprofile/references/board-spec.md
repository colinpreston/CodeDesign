# Proto-persona board spec (`scripts/profile_board.py`)

One JSON file describes the client's brand and every profile. `assets/example-breitling.json` is a full worked example.

```bash
python3 scripts/profile_board.py spec.json --out profiles --png
```

Writes `NN-<slug>.html` (review), `NN-<slug>.dc.html` (Design canvas artboard; rename the first to `Main.dc.html`) and, with `--png`, a 2x `NN-<slug>.png` to upload to the deck and place full-slide (1600×1000 board → 1382×864 at left 269, top 40 on a 1920×1080 slide). `--png` needs Playwright; Google Fonts load only where the network allows, else pass local `@font-face` files.

## Top level

| Key | Meaning |
|---|---|
| `client`, `version`, `date` | Strip text, e.g. "Breitling US", "v0.1", "21 Oct 2026" |
| `size` | `[1600, 1000]` default |
| `lang` | Copy language, default `en` |
| `brand` | The **client's** brand (see below) |
| `legend` | Source keys shown in the strip, e.g. `["D","S","A"]` |
| `sources` | Optional extra or renamed source tags: `{"I": {"label": "Interview", "style": "primary"}}`; style is `outline`, `primary` or `accent` |
| `labels` | Optional overrides, e.g. `goal` ("Moving them to buy on breitling.com"), `loses`, `job`, `research`, `data` |
| `profiles` | List of profiles (below) |

Default source keys: `A` Assumption, `D` Desk research, `S` Site walk, `I` Interview, `Q` Survey, `N` Analytics.

## `brand`

`primary` (strip, headings, Commit block), `accent` (job panel, tags, quote mark), `accent_ink` (text on accent), `ink`, `grey`, `line`, `bg`, `band` (bottom band), `warn` (anxiety and habit), `head_font`, `body_font`, `head_upper` (true for condensed display faces), `fonts_href` (Google Fonts css2 link).

## Each profile

| Key | Meaning |
|---|---|
| `name`, `type`, `often` | "The value checker", "Mindset", "often an enthusiast" |
| `who` | One-line description |
| `moment` | One line under the scene: when and where they are |
| `quote` | In their words. Assumed until interviews; `quote_note` overrides the label |
| `scene_svg` | Inline SVG, 270×187, neutral figures only. Omit for a labelled placeholder |
| `job` | When…, I want to…, so I can… |
| `confidence`, `confidence_note` | 0–4 filled steps; what it rests on |
| `push`, `pull`, `anxiety`, `habit` | `[["text", "sourceKey"], …]`, 2–3 each |
| `tips`, `loses` | 3–4 short lines each |
| `research` | `[["hypothesis", "method", "To do"], …]`, 3 |
| `data` | `[["measure", "source tool"], …]`, 3–4 |

## Scene guidance

Draw the person as simple shapes (circle head, rounded body, one neutral fill) with objects that show the situation and a thought bubble naming the core worry in 2–4 words. No age, gender, ethnicity or stock photos. Keep shapes in the client's primary and accent colours.
