---
name: code-brand-style
description: Code Computerlove's visual identity and deck system — colour palette, typography, gradients, dot-matrix motif, iconography, photography, layout conventions and tested slide layouts for research and strategy decks, taken from the official WPP Media brand template and Code's research playbacks. Use whenever creating a deck, doc, artifact, dashboard, one-pager, or any visual output that should look "on-brand," "in our style," or "like our template," and whenever another skill builds a deck (UX review, market review, journey map slides, research playback): every deck takes its look from here.
---

# Code Brand Style

> **All deck styling lives here.** Any Code deck (a UX review, a market review, a research playback, journey map slides, a pitch) takes its fonts, colours, motifs and slide layouts from this skill. Before building any deck, read `references/deck-system.md` and build the slides with `scripts/slides_house.py`. Other skills decide what a deck says and in what order; they don't restyle it.

This is Code Computerlove's visual identity, read directly off the official **WPP Media brand template** (`CodeDesignTemplate.pptx` — a 104-slide master deck of layouts, colour specs, typography specs, graphic elements and icon libraries). Code sits inside WPP Media, so the template is Code's own visual system: the cover slide shows the rounded "Code" wordmark under the line "A WPP Media Brand," and every content slide carries the "WPP Media" mark bottom-right unless it's been swapped for Code's own.

Use this whenever building something that should look like it came from Code — an HTML artifact, a dashboard, a deck, a one-pager, a status page, a PDF. It's a visual language, not a set of fixed slide templates — apply the palette, type rules and motifs below to whatever you're actually building rather than trying to force it into a specific slide layout.

## Colour

**Primary palette** — the core identity. Deliberately "light and bright," with lime as the signature pop of colour against a near-black navy.

| Name | Hex | Use |
|---|---|---|
| WPP Navy | `#000050` | Primary text colour, dark backgrounds, headline colour |
| White | `#FFFFFF` | Base background, text on dark/colour |
| Lime Green | `#B0F467` | Signature accent — the one colour that should feel unmistakably "us." Numbered badges, small highlight blocks, a pop of colour on an otherwise navy/white layout |
| WPP Pantone 629 (Aqua) | `#93DFE3` | Secondary light background, nod back to the WPP masterbrand |

**Secondary palette** — deeper into the brand, for variation once the primary palette is established. "Light and bright, feminine and refreshing," and built to complement the primary set rather than replace it.

| Name | Hex | Use |
|---|---|---|
| Cornflower Blue | `#5465FF` | Gradient anchor, eyebrow/label text, mid-tone blocks |
| Periwinkle | `#788BFF` | Gradient midpoint, softer blue fills |
| Teal / Cyan | `#00DBEE` | Gradient anchor, link colour, high-energy accent |
| Yellow | `#FCFE67` | Gradient accent, sparingly — the loudest colour in the system |

**Text-safe blues.** Cornflower `#5465FF` only just passes 4.5:1 on white, so text in that colour uses the deeper `#3F4FE0` (6.2:1). White text on a blue gradient sits on its deep end, `#2D3BC7` or `#3F4FE0`, never on periwinkle, aqua or lime. Supporting colours (body `#2A2F6E`, muted `#5A5F8A`, panel `#ECF1F4`) and the semantic colours for Persuasion stages, Good / Needs work / Poor and competitor rings are in `references/deck-system.md` and `references/tokens.css`.

**Rules of thumb:** navy and white carry almost all body content — colour is for accents, gradients and moments of emphasis, not for filling large text areas. Lime is the one colour reserved for "this is ours" moments (numbered list badges, a single highlighted stat, a small tag). Never put body text in a saturated colour; body copy is navy on white/light, or white on navy/dark.

## Typography

The template uses a proprietary in-house font family, **WPP** (weights: Thin, Light, Regular, Medium, Bold). The official spec, straight off the template's own typography slide:

- **Headlines** — WPP Bold, 28pt, sentence case, WPP Navy
- **Subheadings / section labels** — WPP Bold, 18pt, UPPER CASE, Cornflower Blue
- **Body copy** — WPP Regular, 14pt, WPP Navy

**In decks, headlines run light, not bold.** Code's research playbacks (for example the Pure Pet Food "Research findings and response" deck) set slide headlines in a light or regular weight and pick out the one key phrase in bold cornflower: "This document will outline the **findings of our research** and recommendations for how **we think you should respond**." Section titles and the giant section numbers are medium. Bold is for the highlighted phrase, card headings and labels. The full deck type scale is in `references/deck-system.md`.

Beyond those three named styles, the deck also uses a fourth, unnamed one consistently: a small **eyebrow / kicker label** — uppercase, letter-spaced, ~11pt, WPP Navy on light backgrounds or white on dark (e.g. "SECTION 01," "PREPARED BY: CODE," "CASE STUDY," "GSO CASE STUDY | UK | HEALTH & BEAUTY"). Use it above a headline to tag what a block is, sparingly.

Big display numbers (stats, section numbers) run much larger — 40–90pt+, Bold, in navy on light backgrounds or white on dark/colour backgrounds. These are treated as graphic elements as much as text: a giant "01," "50%," "20K," or "92%" is a legitimate hero element on its own, not just a data point.

**Font substitution:** the WPP font isn't public, so anything built outside PowerPoint (an HTML artifact, a web page, a doc) needs a fallback. Match the shape, not just the vibe — WPP Bold reads as a rounded, geometric grotesque with soft terminals (visible in the "Code" wordmark's rounded strokes). Closest safe web fallbacks, in order of preference: **Poppins**, **Plus Jakarta Sans**, **General Sans**. Use the fallback's Bold/SemiBold weight for headlines and eyebrow labels, Regular for body. Say plainly, when it matters, that the real WPP font would need the actual font files from Colin/WPP's brand kit.

## Graphic motifs

Two recurring textures do most of the "this looks like us" work, and they combine freely with each other and with photography.

**Gradients** — soft, blurred colour blobs (radial, not linear-crisp), almost always spanning from the primary palette (navy/lime/aqua) into the secondary palette (cornflower/periwinkle/cyan/yellow). Two common shapes: a large soft-edged circular "orb" bleeding off one side of the canvas, and a diagonal wash that fades from a solid colour corner into white. Used to (a) fill a whole slide/panel as a background, (b) sit behind a white content card for depth, or (c) sit subtly in a single corner of an otherwise white layout. Never sharp-edged or flat — always a soft blur/feather.

**Dot matrix** — a scattered grid of small dots, mostly uniform size with a few enlarged for rhythm, rendered in a single colour (navy, white, or lime) at low opacity. Used as a textured overlay: scattered across a plain background, laid over photography, or filling a colour block. The brand's own copy for this motif: "the dots are the building blocks for big ideas ... born from our people with unique, creative and colourful minds from different cultures, backgrounds and experiences." It's the system's texture, not decoration for its own sake — use it to add depth without adding noise, never dense enough to compete with text.

The "WPP" wordmark itself is sometimes rendered in this dot-matrix style (each letterform built from dots) paired with "Media" set solid — worth doing for a Code lockup too if the letterforms allow it (e.g. a dotted "Code" mark for a title treatment).

## Iconography

Two distinct icon styles appear, used for different purposes:

- **Feature/UI icons:** simple, single-line white icons inside a solid circular badge, badge filled with a navy→cornflower or cornflower→cyan gradient. Use for feature lists, capability grids, or any "here's what this does" moment.
- **Social/platform icons:** flat, single-colour circular badges (brand-blue) for recognisable third-party logos (Google, Meta, LinkedIn, etc.) — kept visually consistent with the feature-icon style so a mixed row doesn't look bolted-together.

Keep icon strokes thin and rounded, never filled/solid glyphs — the system is line-based throughout.

## Photography

Candid, natural-light business/lifestyle photography — people mid-conversation in meetings, genuine (not posed-stock) smiles, visibly diverse in age, ethnicity and background. Never stiff corporate stock-photo posing. Portraits (e.g. a team grid) are cropped tight and consistent, one person per frame, name/title overlaid directly on the image in a semi-transparent strip. Photography can carry a dot-matrix overlay or a colour-gradient tint/duotone treatment (see slide with the VR headset shot half-tinted lime-green) when it needs to feel more "brand" than "stock."

## Layout patterns

Recurring structures worth reusing directly:

- **Cover / section divider:** full-bleed gradient-blob background, with a white rounded-corner card (generous radius — treat corners as ~20–24px at web scale) floating on the left third, holding an eyebrow label + big sentence-case headline. A huge outline/solid number (e.g. "01") sits oversized in the gradient area for section dividers.
- **Title-only content slide:** plain white background, headline top-left in navy, supporting body copy below it, generous whitespace — the gradient/dot motifs stay confined to a corner or a strip rather than covering the page.
- **Split image/text:** photography fills one half (edge-to-edge, no padding), copy and headline fill the other half on white.
- **Full-bleed statement/data:** a gradient (often navy→cornflower→cyan) fills the entire background, with a large headline and either a bulleted list or a row of stat callouts in white text laid directly over it. A thin dot-matrix texture sits behind everything at low opacity.
- **Stat callout:** giant bold number (40pt+) directly above a one- or two-line label in regular weight — no card, no border, just scale contrast doing the work.
- **Numbered list:** small circular lime badge holding a two-digit number, sitting to the left of a headline/body pair, rows separated by a thin hairline rule.
- **Case study / proof point:** a two- or three-column split — headline + labelled sections (eyebrow-style labels: "CHALLENGE," "APPROACH") on white/light, a photo in the middle, and a colour-block sidebar (cornflower or navy) carrying stat callouts in white.
- **Footer convention:** page number bottom-left, small and unobtrusive; "WPP Media" (or "Code") wordmark bottom-right, bold, in the colour that contrasts the background (navy on light, white on dark).

**Research and strategy playbacks** add a fixed set of layouts, all specified and built in `references/deck-system.md` and `scripts/slides_house.py`:
- **Contents:** blue wash, "What we'll cover in this document" light and large, numbered sections with one-line descriptions.
- **Role statement:** one centred sentence on why the document exists, two phrases highlighted.
- **Section divider:** white with corner glows, giant section number top right, a lime-outlined "→ SECTION 01" pill and a huge title.
- **Title only with evidence:** eyebrow, light headline, body on the left; the evidence (panel, quote, screenshot, collage) on the right. Used for the brief, each research method and "Delivering value".
- **Key insights:** numbered "01–06" insights, bold heading and a line or two each.
- **Big stat:** one number on a cornflower panel, the story beside it.
- **Theme opener:** aqua-to-lime wash, giant theme number, the theme as a sentence, and the measures it moves ("**Improved** visit bookings").
- **Recommendations panel and recommendation detail:** a dark panel (the client's colour when known, else navy) with the recommendation; the case and the decision lines beside it.
- **Value against effort 2×2, executive summary (Research | Assets | Opportunities), thank you.**
- **Mobile screens:** every mobile screen sits in Code's phone frame (`phone()`), alone beside the copy, annotated with callouts, or two to four in a row (`screens`). Never a bare mobile screenshot or a stock mock-up. Spec in `references/deck-system.md` §5.

## Applying this outside PowerPoint

When building an HTML artifact, dashboard, or web-facing output:

- Set up the palette as CSS custom properties (see `references/tokens.css` in this skill for a ready-made set) rather than hand-picking hex values per element.
- Build the "orb" gradient with a large, heavily-blurred radial-gradient div (or an SVG `<feGaussianBlur>`), not a CSS linear-gradient with hard stops — the softness is the point.
- Build the dot matrix as a repeating background (a small SVG or CSS `radial-gradient` dot repeated on a grid, e.g. `background-image: radial-gradient(currentColor 1.5px, transparent 1.5px); background-size: 24px 24px;`) at low opacity (10–20%), never as individually placed elements.
- Reserve lime (`#B0F467`) for one deliberate accent per screen — a badge, a highlighted stat, a single CTA — not for large fills.
- For a slide deck built with a Slides-type artifact, use `references/deck-system.md` and `scripts/slides_house.py`: the layouts are tested in that format, so reuse them rather than drawing new ones.
- For a written doc (not a visual deck), the visual system matters less than the type rules: navy headings, sentence-case headlines, uppercase blue eyebrow labels above section headers if the doc format supports it.

## Quick reference

- Navy `#000050` + White `#FFFFFF` carry everything; Lime `#B0F467` is the one accent that says "this is ours."
- Headlines: sentence case, navy. In decks, light weight with one phrase in bold `#3F4FE0`. Subheadings/labels: Bold, UPPERCASE, cornflower blue. Body: Regular, navy.
- Decks: read `references/deck-system.md` first; build with `scripts/slides_house.py`.
- Two motifs, used everywhere: soft blurred gradient blobs, and a low-opacity scattered dot grid.
- Icons are line-based, white-on-gradient-circle.
- Photography is candid and diverse, never stiff stock-photo posing.
- Footer: page number bottom-left, wordmark bottom-right.
- Mobile screens: always in the phone frame, `phone()` in `scripts/slides_house.py`.
- No exact WPP font outside PowerPoint → fall back to Poppins/Plus Jakarta Sans/General Sans and say so.
