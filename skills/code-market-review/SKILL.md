---
name: code-market-review
description: Run a Code-format market and competitor review that shows how a client's site and service stack up against direct, indirect, category and wildcard competitors at every stage of the customer's journey funnel (trigger moment, discover, consider, convert), comparing proposition, price, service, USPs, product features and UX judged with Code's Persuasion Model, always offers to build the CX journey map first, and always builds the result as a Code-branded slide deck to immerse a team in a new engagement. Use when Colin asks for a competitor review, competitive audit, market review, landscape review, benchmark or "how do they stack up".
---

# Code Market Review

> **Always do this first: offer the CX journey map.** Whenever someone asks for a competitor review, market review or competitive audit, the first thing you do, before any searching, browsing or scoping, is check for a CX journey map for this client and ask about it:
> - **No map yet:** ask whether to run the `cx-journey-map` skill first, and recommend it. It tells the review who the customers are, what starts their journey, and how and when they use the website. Use AskUserQuestion with the options "Build the journey map first (recommended)", "Go ahead without it" and "There's a map already; here's where".
> - **A map exists:** say which one you found, its version and date, and confirm you'll use it.
>
> Don't start the review until this is answered. If the person isn't there to answer, build the journey map first. If they choose to go ahead without it, say in the deck that the customer view is assumed.

At the start of an engagement the team needs to understand the market the client lives in, not just the client's site. Customers don't judge a site on its own. They judge it against:
- the other brands selling the same thing;
- the other ways they could meet the same need;
- the sites and apps they use every week.

This review lays that landscape out and follows the customer's journey funnel, from the moment the need appears to the moment they act. It shows, with evidence, where the client **leads, matches or lags** at each stage on:
- **proposition and price;**
- **service** (delivery, flexibility, guarantees, support);
- **USPs and product features;**
- **UX**, judged with Code's Persuasion Model.

It's the sister skill to `code-ux-review`, which goes deep on the client's own site. Run this one first at the start of an engagement, then the UX review. Both use the same journey scenario, so their scores line up.

**The deliverable is always a deck,** a Code research playback like the UX review: four numbered sections (Revisiting the brief, Research findings, Research outcomes, Themes & recommendations). Its look comes entirely from `code-brand-style` (`references/deck-system.md`, built with `scripts/slides_house.py`); this skill decides what it says and in what order. Its job is immersion: someone new to the account should read it and understand the market, the customer's alternatives and where the client wins and loses.

## The four rings of competition

Sort every competitor into one of four rings. A Pure Pet Food example shows how:

| Ring | What it is | Pure Pet Food example | The question it answers |
|---|---|---|---|
| **1. Direct** | Same product, same model, same customer | Other dog food subscription brands | Who would a customer pick instead of us? |
| **2. Indirect** | Same need, a different way of meeting it | Dog food from the supermarket, pet shops, vets | What do customers do if they don't subscribe at all? |
| **3. Category** | Where the customer shops for neighbouring things | Grocery shopping apps and sites | What does "normal" buying feel like for this customer? |
| **4. Wildcard** | A different industry with the same experience pattern | HelloFresh and other subscription services | Whose experience sets the bar for ours? |

**Explain the psychology first.** Two effects make rings 3 and 4 matter:
- **Liquid expectations** means people judge every experience against the best one they've had anywhere, not just against rivals in the same market. If pausing a meal-kit box takes two taps, pausing a dog food box should too.
- **Jakob's law** means people spend most of their time on other sites, so they expect yours to work the way those do. Breaking a familiar pattern costs effort and trust.

Rings 1 and 2 are scored and compared feature by feature. Rings 3 and 4 are **benchmarks for experience patterns**: pick the specific moments they do brilliantly (pausing, reordering, delivery tracking) and compare those moments, not the whole business.

## The journey funnel: compare every stage, not just the website

Competitors win and lose customers long before the enquiry form. Compare them at each stage of the funnel:

| Funnel stage | The customer is thinking | What to compare across competitors |
|---|---|---|
| **1. Trigger moment** | "I need to sort this." | Which moments each brand speaks to (a fall, a diagnosis, planning ahead, a worried relative, a referral), and whether its messaging and landing pages name them |
| **2. Discover** | "Is this the answer for us?" | Top-level research: how each brand helps people decide whether they need the service at all (guides, advice, explainers), and who shows up for the searches customers actually make, in paid ads, organic results, maps and AI answers; their ad promises; review scores visible in search; presence on review and comparison sites |
| **3. Consider** | "Is this right for me, and can I trust them?" | Proposition, price, product information, comparison help, proof, guarantees and finance |
| **4. Convert** | "I'll go ahead." | The route to act (form, booking, phone, chat), how much it asks, whether you can choose a time, and what they say happens next |

**Two different "triggers".** The funnel's first stage is the *trigger moment*: the life event that starts the journey. The Persuasion Model's fourth stage is *Trigger*: the nudge that gets someone to act on the page. Always write "trigger moment" for the funnel and "Trigger" for the Persuasion Model.

The rings and the funnel work together. Direct and indirect competitors are compared at all four stages. Category and wildcard benchmarks are compared at the stages where they set the bar, usually Discover or Convert, for example a service that lets you book online.

### Start from the CX journey map

The journey funnel needs evidence about real customers, not just the website. So before anything else:

- **Ask Colin whether a CX journey map exists for this client.** Look for one in the Project (for example `<Client>_Journey_Map.json`) or among his artifacts.
- **If there isn't one, ask him whether to run the `cx-journey-map` skill first** (this is the "Always do this first" question at the top). Recommend it, because it gives the review its customer types, trigger moments, pains and data gaps. If he says no or there's no time, carry on, and say in the deck that the customer view is assumed.
- **Use the map throughout:**
  - its **customer types or mindsets** become the trigger moments you search for and write about (for example "the planner", "the family helper", "the urgent need");
  - its **stages and steps** decide which pages and moments you walk, and each finding links back to a step;
  - its **pains and positives** are evidence you can cite next to your own findings;
  - its **data gaps and research questions** go into the next steps slide;
  - its **funnel** (for example prospect, lead, quoted, customer) shows where the business loses people, when data exists.
- **Feed back into the map.** When the review confirms, adds or disproves something on the map, update it (or tell Colin what to update) so the map and the deck agree. Never leave a finding in the map that the review has shown to be wrong.

In the deck, add one slide near the start: "Who the customer is and what starts their journey", built from the map's customer types and trigger moments, with a link to the map and its confidence level.

## The lens: Code's Persuasion Model

UX comparisons use the same four stages as `code-ux-review`. Each stage gates the next.

| Stage | The user thinks | Compare |
|---|---|---|
| **1. Usability** | "I can do X" | How easily can a customer find, understand and start the journey? |
| **2. Trust** | "It's OK to do X" | Reviews, guarantees, clear pricing, credible brand and proof. |
| **3. Emotion** | "I want to do X" | Imagery, story, tone, how personal it feels. |
| **4. Trigger** | "I will do X" | Offers, clear calls to action, the first step made easy. |

If `code-ux-review` isn't loaded, its "foundation" section and `code-design-playbook` module 8 give the full model and techniques.

## Step 1: Scope it

Ask only what you can't infer, one question at a time:
- **Client and offer.** Which site, and which product or service is being compared? A business with several lines (subscription and one-off, for example) usually needs one chosen.
- **Customer and job.** Who's the customer and what are they trying to get done? Write the comparison journey as a Code scenario: *"As a [customer] who wants to [goal], I want to [task], so that [outcome]."* Every competitor is walked through this same scenario.
- **Trigger moments and searches.** List the 2–4 moments that usually start the journey, and 3–5 searches each leads to, in the customer's words. Ask the client for their top search terms if they have them; otherwise draft them and mark them as assumptions.
- **Market.** Country or region, and whether it's online only or online plus stores.
- **Site access.** Claude in Chrome only opens sites the person has approved. Once the competitor set is agreed, open each site with its own standalone navigate (never inside a batch, where the approval prompt can't appear) and ask Colin to approve them all before the walks start. Don't fall back to page text without telling him.
- **The competitor set.** Propose a list per ring from desk research and the client's own view, then confirm it with Colin before walking any sites. A typical set:
  - **Direct:** 3–5.
  - **Indirect:** 2–3.
  - **Category:** 2–3.
  - **Wildcard:** 2–3.

  That's 8–12 in all. Fewer, done properly, beats more done thinly.
- **Where it's going.** An internal immersion deck, a pitch, or a client deliverable. A pitch gets the landscape, the scorecard and the gaps. Full immersion gets everything.
- **What already exists.** If a company brain exists for the client (`design-studio-team-setup`), read the Project Brain and the Research Repository first. If a `code-ux-review` of the client exists, reuse its findings and scores for the client column rather than redoing them.

## Step 2: Profile each competitor (desk research)

For each competitor, gather the facts below **from the source, with the date checked**. A fact without a source doesn't go in the deck.

| Area | Capture |
|---|---|
| **Proposition** | Headline promise, who it's for, positioning in their own words |
| **Price** | Entry price and what it buys, in a comparable unit (per day, per month, per kg); intro offers and how long they last |
| **Service** | Delivery speed and cost, subscription flexibility (pause, skip, change, cancel, and how), guarantees, returns, support channels and hours |
| **USPs** | What they claim makes them different, word for word where short |
| **Product** | Range, personalisation, ingredients or specs, the key features customers compare on |
| **Trust** | Review platform rating **and** review count, with the date; awards, press, accreditations; what reviews praise and complain about, summarised |
| **Channels** | App (and its store rating), stores, marketplaces, social presence where it matters |

**Sources:**
- the competitor's own site;
- Trustpilot, Feefo or Google reviews;
- App Store and Google Play;
- the press and their own about pages.

Use WebSearch for discovery and WebFetch or the browser to read pages. When a price varies (by dog size, by box size, by postcode), compare **one defined case** and state it, such as "a 10kg adult dog, standard plan".

**Never invent a number.** If a price, rating or count isn't visible, write "not shown". Don't estimate market share, revenue or traffic unless Colin provides a source.

## Step 3: Walk the comparison journey

Use the browser (Claude in Chrome or the built-in browser), desktop first.

**Trigger moment and Discover: start with search.** Run each Step 1 search in the browser and record a row per search:
- who appears in the paid ads, the organic results, the map results and any AI answer, and in what position;
- each ad's headline and offer;
- whose review scores show in the results.

This becomes the search visibility table: searches as rows, competitors as columns, each cell saying where that brand appeared (for example "Ad 2", "Organic 4", "Not shown"). Results vary by location, device and history, so date them, note the location and call them indicative. **Never click a paid ad**, because it costs the advertiser money: open the advertised page by typing its address. Then check whether each landing page matches the promise of its ad, and note which trigger moments each brand's headlines name.

**Discover: compare the advice content.** Search shows who people meet. The advice shows who helps them decide. For the client and every direct and indirect competitor, find the guides, blog, buyer's guide and FAQs (menu, homepage and footer), and record:
- **Where it sits:** in the main menu, on the homepage, or tucked under a catch-all such as "More" or "Everything else"?
- **"Is it right for me?":** does a guide help people decide whether they need the service at all, and compare it with the alternatives?
- **Cost:** does a cost guide give real figures (ranges, "from" prices or typical job prices), or ask the cost question and then not answer it?
- **Help with paying:** grants, VAT relief, finance and assessments, where they apply.
- **Tools:** checkers, calculators or quizzes that answer a question for the person.
- **Freshness and ownership:** a named author and a recent "last updated" date.
- **Next step:** what each guide asks people to do next, and whether that fits someone who is still deciding.

Count, don't guess: note the figures quoted, word for word, and the date read. Read the main guides, not every article, and say so.

This becomes the **advice comparison table**: brands as rows; where the advice sits, "is it right for me?", cost guide with real prices, and help with paying as columns. Colour each cell green (does it well), amber (partly) or red (missing). Then add **two or three annotated screenshots**: the best competitor guide, and the client's equivalent. **Score Discover on both**: search visibility and advice content. Say in the notes how each one moved the score.

**Direct and indirect competitors.** Walk the scenario from Step 1 on each site, stopping at the point of commitment. At each **key moment** (landing page, choosing or configuring, product detail, offer and price, the start of sign-up or basket):
1. **Screenshot it**, viewport-height and saved to disk, recording the scroll position and window size.
2. **Note 2–4 findings**, each tagged **(+)** or **(−)** and to one Persuasion stage, in the house style: *"(+) Trust / Price per day is shown before the quiz, so there are no surprises at the end."*
3. **Record the element's centre** for any callout, using the same method and connector maths as `code-ux-review` Step 2 and Step 6.
4. **Count, don't estimate:** steps to reach a price, quiz questions, form fields, calls to action.

**Category and wildcard competitors.** Don't walk the whole journey. Go straight to the **two or three moments** they set the bar on and capture those, such as:
- how a subscription is paused or changed (only from public pages, help centre articles and screenshots they publish; never log in);
- how the first order is configured;
- how delivery is promised and tracked;
- how the offer is explained.

**Score the UX.** For each direct and indirect competitor, plus the client, give two sets of 1–5 scores: one per **funnel stage** (how well they handle trigger moment, discover, consider and convert), and one per **Persuasion stage** on the comparison journey:

| Score | Meaning |
|---|---|
| **1** | Blocks the customer |
| **2** | Weak: works, but with real friction or doubt |
| **3** | Parity: does the job, nothing more |
| **4** | Good: clearly better than most |
| **5** | Best in class: the one to learn from |

Every score needs one line of evidence. These are expert judgements, so present them as that and never average them into a single "UX score".

**Never sign up, log in, buy or enter personal data.** Stop at the commitment point and note what lies beyond it, unseen.

## Step 4: Speed and accessibility at a glance (light touch)

Run PageSpeed Insights **mobile** on each direct competitor's homepage and the client's, using the method in `code-ux-review` Step 3. Record:
- Core Web Vitals pass or fail (field data);
- LCP, INP and CLS;
- the Lighthouse Performance score, with the date.

This shows whether speed is a differentiator or a weakness in this market. Optionally, run the `code-ux-review` quick accessibility scan on the same pages, but keep it to headline findings, such as contrast failures and reading ease. The deep accessibility check belongs in the UX review.

## Step 5: Synthesise

Work through these in order:

1. **Comparison matrices, in funnel order.** Build these tables with competitors as columns and the client first:
   - **Trigger moment and Discover:** search visibility, and which trigger moments each brand speaks to;
   - **Consider:** proposition and price, then product information and proof;
   - **Convert:** the route to act, what it asks, choosing a time, and what happens next, plus guarantees and finance if they're presented at this point.

   Mark each cell with a word, not only a symbol or colour: **Yes**, **Partly**, **No**, or **Not seen**.
2. **Table stakes, differentiators, gaps and white space.**
   - **Table stakes:** everyone in ring 1 does it, so not having it is a gap, but having it wins nothing.
   - **Differentiators:** what the client does that few others do. Check the client actually tells customers about them.
   - **Gaps:** what competitors do that the client doesn't, ranked by how much customers care (use review themes as evidence).
   - **White space:** what nobody in rings 1–2 does well but rings 3–4 have taught customers to expect.
3. **Positioning map.** Choose two axes that genuinely split this market, from the evidence (for example price per day against how personalised the product is). Place each competitor from the facts in Steps 2–3, and say in the notes that placement is a judgement.
4. **The headline.** One sentence on where the client sits, then 3–5 short paragraphs for the executive summary, biggest point first. Say at which funnel stage the client loses most ground to competitors.
5. **Opportunities, Now / Next / Future,** tied to evidence:
   - **Now:** say what you already do better, closing cheap gaps.
   - **Next:** design or build to close real gaps.
   - **Future:** move into white space.

   Explain the psychology behind each one before the action. For the top three, write Code's test hypothesis: *"Because we have observed (finding), we believe that (change) will result in (effect), confirmed when (measure)."*
6. **Name the gaps in the evidence:** no logged-in experience, no analytics, no customer interviews, prices from one defined case only. These become the research and next steps slide.

**No dark patterns.** Copying a competitor's fake urgency, hidden cancellation or pre-ticked extras is never a recommendation, however well it converts.

## Make the recommendations strategic

Findings tell the client what's wrong. Recommendations have to tell them what to do, why it matters to the business and how to start. Before writing any recommendation:

1. **Anchor on the business goal.** Name the outcome the client cares about, such as more qualified enquiries, better return on media spend, a higher visit-to-sale rate or lower cost per lead. If the brief doesn't say, ask. Every recommendation must link to it.
2. **Group findings into 3–4 strategic themes.** A theme is a single problem or opportunity that several findings point to, written as a plain sentence, for example "Make the home visit the easiest thing to book". Themes are what a client director remembers; individual findings support them.
3. **Write every recommendation as a decision card:**
   - **What:** the change, in one sentence a designer or developer could start on.
   - **Why:** the evidence (the finding, competitor or benchmark), with its source.
   - **Funnel stage:** trigger moment, discover, consider or convert.
   - **Value:** which business metric it should move, in which direction, and how we'd measure it. Never invent a size: if there's no data, say what data would size it.
   - **Effort:** low, medium or high, with one line on what makes it so (content change, design, build, new system, third party).
   - **Confidence:** high, medium or low, based on how strong the evidence is.
   - **Owner:** who would do it (client marketing, web team, Code, media agency).
4. **Prioritise on value against effort.** Plot the recommendations on a 2×2: quick wins (high value, low effort) first, big bets (high value, high effort) planned, fill-ins (low value, low effort) when there's capacity, and drop the rest. Explain the placement in the speaker notes.
5. **Turn it into a roadmap.** Now (the next 4–6 weeks: quick wins and tests), Next (the next quarter: design and build), Future (bigger change, new capability or research). Show dependencies, for example "price guide needs MBG quote data".
6. **Say what to measure.** For the top recommendations, give the test hypothesis in Code's format: "Because we have observed (finding), we believe that (change) will result in (effect), confirmed when (measure)." List the analytics the client needs in place to judge success.

**No fluff.** Every recommendation needs evidence, an owner and a way to measure it. If it has none, it's an observation, not a recommendation.

**Strategy slides, in the deck** (layouts from `code-brand-style`):
- **Theme opener:** one per theme, with the measures it should move ("Improved visit bookings").
- **Recommendations panel:** the theme's 2–4 recommendations, numbered.
- **Recommendation detail:** one per top recommendation: the competitor evidence, the psychology (meaning first), the change, then Value, Effort, Confidence and Owner.
- **Value against effort:** the 2×2, quadrants "Do first", "Plan in", "Fit in", "Park".
- **Roadmap** (optional): Now, Next and Future, each item tagged by funnel stage and owner.

## Step 6: Build the deck (always)

**Every run ends in a deck.** If time is short, cut competitors, not the deck.
- **Default:** a **Slides** artifact. Run Artifact `quickstart` with intent `slides`, or create from the Slides type when its link is known, and follow the type's own instructions.
- **PowerPoint:** only when Colin asks for a .pptx. Then use the pptx skill and the same structure.
- **Never invent content to fill the deck.** Missing facts become bracketed placeholders, listed in your reply.

**Look.** Read `code-brand-style` first: `references/deck-system.md` for tokens, type, motifs and layouts (including the competitor ring colours), and `scripts/slides_house.py` to build the house layouts. Reuse the annotated screenshot, connector maths and score ring from `code-ux-review`. Upload every screenshot as an asset first and use the `/_blob/…` URL. Stage colours mean Persuasion stages and nothing else; ring colours appear only on the landscape and positioning slides.

**Deck order: a research playback in four sections.**

*Opening*
1. Cover
2. Contents
3. Role statement

*01 Revisiting the brief*
4. Section divider
5. Our brief and the customer scenario ("We are reviewing / For / So that")
6. Delivering value: the business measures
7. Research scope: what was compared, the defined price case, and what wasn't covered
8. The landscape: the rings, with every competitor named
9. The journey funnel and how the Persuasion Model applies at each stage

*02 Research findings*
10. Section divider
11. Key insights: the market in 4–6 numbered points
12. Funnel scorecard, then Persuasion scorecard
13. Positioning map
14. Trigger moment and Discover: the moments each brand speaks to, search visibility, the advice comparison, and the best competitor guide beside the client's
15. Consider: proposition and price, then product information and proof
16. Convert: the route to act, side by side
17. For each direct competitor: a sub-divider or profile slide, then 1–2 annotated moments
18. Indirect, category and wildcard: what customers have come to expect
19. Speed at a glance
20. Where the client stands: what everyone offers, where the client is ahead, where competitors are ahead, what no one offers yet

*03 Research outcomes*
21. Section divider
22. Who the customer is and what starts their journey, from the CX journey map

*04 Themes & recommendations*
23. Section divider
24. Making research actionable
25. For each theme: theme opener, recommendations panel, recommendation detail slides
26. Value against effort
27. Roadmap (optional)
28. Executive summary: Research, Assets, Opportunities
29. Next steps, measurement and research gaps
30. Thank you

In a pitch, keep the landscape, the scorecards, where the client stands and the themes; cut competitor detail first.

**Write for the client.** Plain, natural English and no padding. Slide titles state the point in a full sentence ("Age UK Mobility lets customers choose a date and time of day"), not a label or slogan. Avoid jargon such as "table stakes", "white space", "front door" or "edges"; say what you mean.

**Market-review recipes.** These layouts belong to this review only. They use the brand's tokens and follow the same Slides rules: pinned children use `position:absolute` with pixel values, and text always sits in `<p>`, `<h2>` or `<h3>`. Everything else comes from `code-brand-style`.

**Landscape slide.** Draw four concentric rings on the left, with the client in the centre. On the right, list each ring with its competitors as pills.
```html
<div style="position:absolute;left:180px;top:160px;width:800px;height:800px;border-radius:50%;background:#F3EAF8"></div>
<div style="position:absolute;left:260px;top:240px;width:640px;height:640px;border-radius:50%;background:#E0F1F2"></div>
<div style="position:absolute;left:340px;top:320px;width:480px;height:480px;border-radius:50%;background:#E8EBFF"></div>
<div style="position:absolute;left:420px;top:400px;width:320px;height:320px;border-radius:50%;background:#D5D9F5"></div>
<div style="position:absolute;left:500px;top:480px;width:160px;height:160px;border-radius:50%;background:#B0F467;display:flex;align-items:center;justify-content:center"><p style="font-size:24px;font-weight:700;color:#000050;text-align:center">[Client]</p></div>
<p style="position:absolute;left:460px;top:182px;width:240px;text-align:center;font-size:24px;font-weight:700;color:#6B2C91">Wildcard</p>
<p style="position:absolute;left:460px;top:262px;width:240px;text-align:center;font-size:24px;font-weight:700;color:#00707D">Category</p>
<p style="position:absolute;left:460px;top:342px;width:240px;text-align:center;font-size:24px;font-weight:700;color:#3F4FE0">Indirect</p>
<p style="position:absolute;left:460px;top:422px;width:240px;text-align:center;font-size:24px;font-weight:700;color:#000050">Direct</p>
```
The rings share a centre at (580, 560): each ring is 160px wider than the one inside it, and each label sits in its own 80px band at the top.
Down the right side (from `left:1060px`), for each ring, add a heading `<p>` in the ring colour, then a row of pills (`border:2px solid <ring colour>;border-radius:999px;padding:6px 18px`), each holding a `<p>` with the competitor's name. Write each competitor's name as text; logos are optional extras, never the only label.

**Scorecard heatmap.** Use a grid: one row per competitor, with the client first and in bold, and one column per stage. Each cell is a `<p>` holding the number, tinted by band, with a one-word band under the number. Never colour alone.
```html
<div style="display:flex;flex-direction:row;align-items:center;gap:8px">
<p style="width:360px;font-size:26px;font-weight:700;color:#000050">[Client]</p>
<div style="width:260px;background:#FCE8E6;border-radius:12px;padding:14px 0px"><p style="font-size:36px;font-weight:700;text-align:center;color:#B3261E">2</p><p style="font-size:22px;text-align:center;color:#B3261E">Weak</p></div>
<div style="width:260px;background:#FFF1E0;border-radius:12px;padding:14px 0px"><p style="font-size:36px;font-weight:700;text-align:center;color:#B85C00">3</p><p style="font-size:22px;text-align:center;color:#B85C00">Parity</p></div>
<div style="width:260px;background:#E6F4EA;border-radius:12px;padding:14px 0px"><p style="font-size:36px;font-weight:700;text-align:center;color:#188038">4</p><p style="font-size:22px;text-align:center;color:#188038">Good</p></div>
<div style="width:260px;background:#E6F4EA;border-radius:12px;padding:14px 0px"><p style="font-size:36px;font-weight:700;text-align:center;color:#188038">5</p><p style="font-size:22px;text-align:center;color:#188038">Best</p></div>
</div>
```
Bands: 1–2 use Poor colours, 3 uses Needs work colours, and 4–5 use Good colours. Add a header row with the stage names in their stage colours. Keep to 8 rows; split across two slides beyond that.

**Funnel scorecard.** Use the scorecard heatmap recipe with the four funnel stages as columns: 1. Trigger moment, 2. Discover, 3. Consider, 4. Convert. Put the column headings in navy, not the Persuasion stage colours, so the two scorecards never get confused.

**Search visibility table.** Use the comparison matrix recipe with searches as rows and brands as columns. Each cell is a word and a position, such as "Ad 1", "Organic 3", "Map" or "Not shown". Colour "Ad" and "Organic" cells green and "Not shown" cells red, but always write the word. Put the date, the location and "results vary by person and place" in the footer.

**Comparison matrix** (proposition, service and features). Rows are the things compared; columns are the client then competitors, up to 6 columns per slide. Every cell is a word:
- **Yes:** `#188038`
- **Partly:** `#B85C00`
- **No:** `#B3261E`
- **Not seen:** `#2A2F6E`

Alternate the row backgrounds `#E8EBFF` / `#FFFFFF`. Put prices as plain values in the same unit, with the defined case in the slide's footer source line.

**Positioning map.** Use a plotting area of `left:360px;top:200px;width:1200px;height:640px` with a 2px navy cross through its centre and the axis labels at each end. Place each competitor as a 32px dot in its ring colour plus a name `<p>` beside it:
- `left = 360 + x × 1200 − 16`
- `top = 200 + (1 − y) × 640 − 16`

Here `x` and `y` run from 0 to 1, from the evidence. The client's dot is lime with a navy border. Speaker notes say how each placement was judged.

**Competitor profile slide.** Use two columns.
- **Left:** one screenshot of the homepage hero, at `left:128px;top:220px;width:860px;height:452px;object-fit:contain`.
- **Right:** cards for:
  - the proposition, in one line;
  - the price, for the defined case;
  - 3 USPs;
  - the review rating, count and date;
  - "What they do better" and "Where we're ahead", 2 lines each.

**Annotated moments slides** reuse the UX review's annotated screenshot recipe and stage-coloured callouts unchanged. Title each one as the lesson, for example "HelloFresh: pausing a box takes two taps".

**Speed at a glance** reuses the "scores at a glance" table pattern from the UX review: one row per site, with Core Web Vitals, CLS, Performance and lab LCP.

**Stage colours, (+)/(−) labels and band words must always be written, not only coloured.**

**Speaker notes on every slide** give sources, dates, the defined price case and anything not covered.

**After publishing, give Colin:**
- the deck;
- one line on where the client sits in the market;
- the biggest gap and the biggest untold strength;
- the placeholders to fill;
- what wasn't covered.

Don't render or screenshot the deck to check it unless he asks.

## Step 7: Log it and hand it over

- If a company brain exists:
  - add a summary entry to the Research Repository;
  - put the full matrices and sources in the relevant desk's log (Product Consultant, Lead UX Researcher or CRO);
  - add any competitor review themes to the research backlog for interviews.
- Save the raw facts table (competitor, field, value, source URL, date checked) as a file, so a re-run can show what changed.
- Hand straight into `code-ux-review` if the client's own site needs the deep dive, and into `cx-journey-map` if the team is mapping the current journey.

## Fences

- **Everything is an internal draft until Colin sends it.** Competitor screenshots are for analysis; check usage before they go in anything public.
- **Public pages only.** Never sign up, log in, buy, start a trial, contact a competitor or enter personal data. Don't use anyone else's account.
- **Never click paid search or social ads.** Open the advertised page directly.
- **Cookie banners:** choose necessary cookies only.
- **Never invent a number.** Prices, ratings, counts and speeds are as seen on the date checked, with the source. No guessed market share, revenue or traffic.
- **Summarise reviews; don't paste them.** Quote at most a short phrase, attributed to the platform.
- **Fair comparison.** Use the same scenario, the same defined case and the same date range for every competitor, and say where that wasn't possible.
- **Date-stamp everything.** Prices, offers and ratings change weekly.
- **No dark patterns** in recommendations, even when a competitor uses them.
