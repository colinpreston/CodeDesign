# Code deck system

Every Code deck takes its look from this file: UX reviews, market reviews, research playbacks, journey map slides, pitch slides. The skills that build decks (`code-ux-review`, `code-market-review`, `cx-journey-map`) say **what** goes in the deck and in what order. This file says **how it looks**. Don't restyle a deck inside another skill; change it here.

The layouts come from Code's own research playbacks, chiefly the Pure Pet Food "Research findings and response" deck (WPP Media template, 2026). They're written for a **Slides** artifact (1920×1080, inline styles only) and tested there. In PowerPoint, use the WPP Media template's matching layouts (named in brackets) with the same rules.

`scripts/slides_house.py` builds every layout below as a Python function that returns one slide. Use it, or copy its markup, rather than drawing layouts by hand.

## 1. Tokens

| Token | Hex | Use |
|---|---|---|
| Navy | `#000050` | Headlines, body on light, dark panels |
| Body | `#2A2F6E` | Long body copy on white |
| Muted | `#5A5F8A` | Footer source line, captions (6.1:1 on white) |
| White | `#FFFFFF` | Page |
| Panel | `#ECF1F4` | Quiet grey-blue panel (brief, exec summary columns) |
| Lime | `#B0F467` | One accent per slide: section pill outline, eyebrow on navy, theme wash end |
| Aqua | `#93DFE3` | Gradient stop, theme wash start |
| Cyan | `#00DBEE` | Gradient stop on dividers |
| Cornflower | `#5465FF` | Gradient stop. Not for text on white (4.5:1, borderline) |
| Periwinkle | `#788BFF` | Gradient stop, quadrant outlines. Never for text |
| **Cornflower text** | `#3F4FE0` | Highlighted words in headlines, eyebrows, stat panels (6.2:1 on white) |
| Deep blue | `#2D3BC7` | Left end of the blue wash, so white text sits on 8:1 |
| Pale | `#C9CDEF` | Text on navy that isn't the main line |
| Dot | `#B9C2E6` | Dot texture |

**Semantic colours** (data, not decoration). These always carry a written word too: never colour alone.

| Meaning | Hex |
|---|---|
| Persuasion stage: Usability | `#2F6B00` |
| Persuasion stage: Trust | `#000050` |
| Persuasion stage: Emotion | `#3F4FE0` |
| Persuasion stage: Trigger | `#00707D` |
| Good / Yes | `#188038` on `#E6F4EA` |
| Needs work / Partly | `#B85C00` on `#FFF1E0` |
| Poor / No | `#B3261E` on `#FCE8E6` |
| Not seen | `#2A2F6E` |
| Competitor ring: client | lime `#B0F467` fill, navy text |
| Competitor ring: direct / indirect / category / wildcard | `#000050` / `#3F4FE0` / `#00707D` / `#6B2C91` |

## 2. Type

Font: **Poppins** as the stand-in for WPP (Google Fonts, weights 300–700). Load `family=Poppins:wght@300;400;500;600;700`.

The playbacks set headlines **light, not bold**, and pick out the key words in bold cornflower. That contrast is the house voice: "This document will outline the **findings of our research** and recommendations for how **we think you should respond**."

| Style | Size / weight | Notes |
|---|---|---|
| Section title (divider) | 150px / 500, letter-spacing −5px | Navy |
| Section number (divider) | 360px / 500 | Navy, top right |
| Slide headline | 56–64px / 400, line-height 1.12, letter-spacing −1px | Navy; key phrase in `#3F4FE0` bold |
| Contents headline | 84px / 300 | White on the wash |
| Theme number | 220px / 400 | Navy on the theme wash |
| Big stat | 150px / 400 | White on a cornflower-text panel |
| Insight number | 48–64px / 300 | Navy, "01" style, two digits |
| Card or insight heading | 28px / 700 | Navy |
| Body | 24–26px / 400, line-height 1.4–1.45 | `#2A2F6E` on white, navy on washes |
| Eyebrow | 24px / 500 sentence case ("Our brief", "Key insights · site review") | Above a headline. On navy panels: 24px / 600 uppercase lime, letter-spaced 3px |
| Footer | 24px / 400 | Muted |

Never below 24px. Sentence case everywhere. Highlight one phrase per headline, not several.

## 3. Motifs in Slides markup

**Soft glow** (the gradient orb). One radial gradient per div, blurred, pinned, listed before any flow content:
```html
<div style="position:absolute;left:1150px;top:0px;width:770px;height:640px;background:radial-gradient(circle at 100% 0%, #B0F467 0%, #93DFE3 30%, #788BFF 52%, rgba(255,255,255,0) 74%);filter:blur(20px)"></div>
```
Keep glows in corners. On content slides use a small one (about 360×260 at the top right) so it never sits under text.

**Blue wash** (cover, contents, thank you). White text goes on the left, deep end:
```html
<section style="background:linear-gradient(115deg, #2D3BC7 0%, #3F4FE0 45%, #5465FF 75%, #788BFF 100%);…">
```

**Theme wash** (theme openers). Navy text throughout:
```html
<section style="background:linear-gradient(110deg, #93DFE3 0%, #BDEFD0 50%, #B0F467 100%);…">
```

**Dot texture** (white content slides), first child of the section:
```html
<svg aria-label="Dot texture" width="1920" height="1080" viewBox="0 0 1920 1080" style="position:absolute;left:0px;top:0px;width:1920px;height:1080px;opacity:0.5"><defs><pattern id="dots" width="36" height="36" patternUnits="userSpaceOnUse"><circle cx="18" cy="18" r="1.6" fill="#B9C2E6"/></pattern></defs><rect width="1920" height="1080" fill="url(#dots)"/></svg>
```

**Footer**, on every slide but the cover: page number and source bottom left, the "Code" wordmark bottom right.
```html
<p style="position:absolute;left:128px;bottom:56px;width:1300px;font-size:24px;color:#5A5F8A">07 · Source, date</p>
<p style="position:absolute;right:128px;bottom:48px;width:300px;text-align:right;font-size:40px;font-weight:700;letter-spacing:-1px;color:#000050">Code</p>
```
White wordmark and `#C9CDEF` source on the washes. Put the version on the cover, not in every footer.

**Margins:** 128px sides, 112–128px top, 160px bottom (for the footer band). Nothing but the footer below y 920.

## 4. Layouts

Function names are in `scripts/slides_house.py`. The template layout name is in brackets.

| Layout | Function | Use it for |
|---|---|---|
| **Cover** (Section Divider-4) | `cover` | Blue wash; white rounded card on the left with the client eyebrow (uppercase, letter-spaced) and the title, one phrase in cornflower; "Code / A WPP Media Brand" in white on the right |
| **Contents** (1_Section Divider-4) | `contents` | Blue wash; "What we'll cover in this document" light and large on the left; numbered sections on the right, each with a one-line description, divided by white hairlines |
| **Role statement** (Title Only) | `statement` | White with dots; small eyebrow, then one centred sentence with two highlighted phrases |
| **Section divider** (Section Divider-2) | `section_divider` | White; cyan glow bottom left, lime-to-periwinkle glow top right; giant number top right; a white pill with a lime outline reading "→ SECTION 01"; huge title bottom left |
| **Sub-divider** | `sub_divider` | Inside a section (one page of a site walk, one competitor): lime pill ("Page 1 of 5 · Discover"), large title, one light line, the URL |
| **Title only** (Title Only) | `title_only` | The workhorse. Left column: eyebrow, light headline with a highlight, body paragraphs. Right: the evidence (a panel, a quote card, a screenshot, a collage). Use it for "Our brief", method intros ("Desk research / Understanding the marketplace at a deeper level") and "Delivering value" |
| **Research scope** (Agenda-1) | `numbered_list` | Two columns of numbered items under navy hairlines: each research task with one line on what it was |
| **Key insights** (Agenda-1) | `key_insights` | Eyebrow plus headline, then 4–6 numbered insights in 2 or 3 columns: light "01", bold heading, 1–2 lines of body |
| **Big stat** (Content Framed-3) | `stat_panel` | A cornflower-text panel on the left with one giant number and its label; eyebrow, headline and body on the right |
| **Making research actionable** | `flow` | Findings → recommendations and themes → solutions, with "We are here" over the step this deck delivers |
| **Theme opener** (Fullbleed Title-Light) | `theme` | Theme wash; giant theme number; the theme as a sentence; a short paragraph of evidence; on the right, the business measures it moves, each starting "**Improved** …" |
| **Recommendations panel** | `recs_panel` | A navy panel listing the theme's recommendations, numbered, two columns, client name as a lime tag |
| **Recommendation detail** | `rec_detail` | Navy panel on the left ("RECOMMENDATION" eyebrow in lime, the recommendation as a light headline); on the right the case in 2–3 short paragraphs (evidence, the psychology meaning first, the change), then Value, Effort, Confidence and Owner under a navy rule |
| **Value against effort** | `matrix` | 2×2 with labelled axes ("← High value", "Low value →", "High effort", "Low effort"); quadrants "Do first · quick wins" (bottom left, cornflower outline), "Plan in · bigger bets", "Fit in · when there's room", "Park · for now" |
| **Executive summary** | `exec_summary` | Three columns on grey panels: Research (methods), Assets (what we made), Opportunities (the themes as numbered navy pills) |
| **Thank you** | `thanks` | Blue wash, large light "Thank you", one warm line, a contact |

**Client colour.** The playbacks give recommendation panels and illustrations the client's own brand colour and logo, as a nod to them. Use the client's primary colour on the recommendations panel and recommendation detail panel when it's known and passes 4.5:1 with white text; otherwise use navy. Never guess a client's colour.

**Layouts that belong to one kind of deck** live with that skill but use these tokens: the annotated screenshot, score rings, scores slide and accessibility slide (`code-ux-review`); the landscape rings, scorecard heatmap, comparison matrix and positioning map (`code-market-review`); "Reading a map" (`cx-journey-map`).

## 5. Rules

- **One idea per slide.** A headline states the point as a sentence, not a label.
- **Light headline, one highlight.** Bold is for the highlighted phrase, card headings and labels, not whole headlines.
- **Lime once per slide.**
- **Glows in corners, never under text.** One gradient wash per slide at most.
- **Contrast:** body text 4.5:1, large text 3:1. White text only on navy, `#3F4FE0` or the deep end of the blue wash. Never white on aqua, lime, periwinkle or the light end of a wash.
- **Every colour that carries meaning also carries a word.**
- **Footer on every slide but the cover; speaker notes on every slide** with sources, dates and what wasn't covered.
- **Numbers:** two-digit ("01"), light weight, for sections, insights and recommendations alike.
