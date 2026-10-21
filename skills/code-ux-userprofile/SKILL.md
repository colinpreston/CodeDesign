---
name: code-ux-userprofile
description: Choose, research and build Code-format user profiles (proto-personas, mindset profiles, data segments, demographic personas, jobs to be done) using Code's User Profile Model and push/pull forces. Use when Colin asks for personas, user profiles, segments, mindsets, JTBD or 'who are the users'.
---

# Code UX User Profile

This is how Code Computerlove defines users. It follows Code's **User Profile Model** (Jessica Sherratt, UX Magazine, "Understand and define users with the User Profile Model", 2023), module 6 of `code-design-playbook`, and the push/pull profile boards Code made for Pure Pet Food. Use it in preference to a generic persona template whenever the work is Code's.

**The house view in one line:** pick the *right profile type for the question*, start with proto-personas from desk research and assumption, then validate and update them as research lands. A profile is an artefact for sharing what research found, never the research itself, and always made for a specific purpose.

Read `code-design-playbook` (modules 3 Research, 5 Mapping, 6 User profiles, 11 Inclusive design) before starting. Deck styling comes from `code-brand-style`; the profile boards themselves take the **client's** brand.

## Start with the psychology, then the method

Colin wants the meaning first. Before any template, say in plain words what the profile type, and each force or bias, means and what it can't tell the team. Then the method.

## The process

### 1. Write the research statement
> **We are researching** (what) … **for** (who) … **so that** (outcome).

If the brief is unclear, run the playbook's Day 1 dissection first: what we know, what we know we don't know, what we want to know.

### 2. Break it into research questions
5–12 concrete questions, each answerable, each tagged as about *who* people are, *what* they do, *how* they think, or *what* they're trying to get done.

### 3. Plot the questions on the User Profile Model
- **Finding users ↔ Enabling users** (attract new customers, or help people already using it?)
- **Empathy-based ↔ Task-based** (feelings and situations, or behaviour and outcomes?)

| | Empathy-based | Task-based |
|---|---|---|
| **Finding users** | Demographic personas | Data segments |
| **Enabling users** | Mindset profiles | Jobs to be done |

Show the questions as numbered chips in the quadrants. Clusters show which types the work needs; empty or evidence-free quadrants are blind spots to raise with the client.

### 4. Choose the profiles and methods, blending where needed
- **Acquisition / marketing:** demographic personas + data segments.
- **Usability / product:** mindset profiles + jobs to be done.
- **Conversion problem that needs sizing:** mindset profiles to design with + data segments to measure with; borrow the media agency's audiences rather than build new demographic personas.
- **Problem space:** demographic + mindset. **Solution space:** data segments + JTBD.

### 5. Build proto-personas first (v0.1)
Before any customer research, build proto-personas from desk research, the site or service walk, market checks and stated assumptions. Then:
- **v0.1** desk research and assumption
- **v0.2** updated with data segments
- **v1.0** rebuilt from interviews and survey; real quotes replace assumed ones

Each round confirms, changes or removes lines, and the confidence bar moves up. Never present a proto-persona as validated.

## The four profile types

### Demographic personas
- **Use for:** finding customers for targeted, branded experiences; media briefs.
- **Tells you:** motivations, frustrations, needs, situation; builds empathy.
- **Doesn't tell you:** how people behave with the product. Risk of stereotypes.
- **Methods:** audience and segmentation data (e.g. Mosaic, media planning data), interviews recruited from target groups, surveys.
- **Rule:** demographics are a way in, not an explanation of behaviour.

### Data segments
- **Use for:** finding and sizing groups at scale; personalisation; channel impact.
- **Tells you:** real behaviour by cohort: device, channel, new vs returning, value, drop-off.
- **Doesn't tell you:** why.
- **Methods:** analytics cohorts (GA4, Contentsquare), CRM and order data, funnels by device.

### Mindset profiles
- **Use for:** one core journey used by many kinds of people (a checkout, a product page, a claims form).
- **Tells you:** how people think and what they expect; inclusive by design; functional and content requirements.
- **Doesn't tell you:** who to target or where new audiences are.
- **Methods:** interviews, contextual observation, empathy mapping; regroup participants by shared expectations, not demographics. Name them for the mindset ("The reassurance seeker"), with the occasion as a subtitle ("often marking a milestone").

### Jobs to be done
- **Use for:** complex services with many users and complex needs; the job statement inside every board.
- **Tells you:** the progress people want to make, outcomes, frustrations.
- **Doesn't tell you:** targeting; little empathy on its own.
- **Methods:** switch interviews, forces of progress, job statements: *When (situation), I want to (motivation), so I can (outcome).*

## The forces of progress (the heart of each board)

Explain the meanings first:
- **Push:** the frustration or moment that makes someone act now.
- **Pull:** what attracts them to this particular choice.
- **Anxiety:** worry about what could go wrong with the new choice.
- **Habit:** the comfort of how they do it today.

People choose and commit when push + pull outweigh anxiety + habit. Design can strengthen pull or, often more powerfully, reduce anxiety.

## The profile board: layout

One landscape board per profile (about 1600×1000), designed in the **client's brand** (colours, type, shapes), on a Design canvas so it stays editable, then rendered and placed full-slide in the Code deck.

1. **Strip:** client · proto-persona NN of NN · version and date · source legend.
2. **Header, humanised:**
   - a small **scene illustration** of their moment, with a thought bubble naming their core worry ("Is it safe?");
   - a one-line **moment** ("Lunch break, three tabs open…");
   - mindset name, occasion subtitle and a one-line description;
   - a line **in their words**, labelled *assumed; to be replaced with real interview quotes* until research supplies one;
   - the **job statement** in a brand-colour panel;
   - a **confidence bar** (4 steps) with a one-line note on what it rests on.
3. **Forces:** "Moving them to buy" row (Push → Pull → Choose and commit) and "Holding them back" row (Anxiety ← Habit), 2–3 lines each.
4. **Side panels:** "What would tip them" (design levers) and "Where the site loses them today" (linked to the findings).
5. **Bottom, split in two:**
   - **Research to validate** (the why, ~10 people): 3 hypotheses, each with method and a status (To do / In progress / Done).
   - **Data to validate at scale** (how many, sizes the persona): 3–4 measures, each tagged with its source tool (GA4, Contentsquare, Medallia, order data, media agency data).

**Source tag on every line:** Desk research · Site walk · Assumption (later: Interview · Survey · Analytics). Nothing untagged.

**Build it with the script.** Write a JSON spec (client brand + profiles; see `references/board-spec.md`, copy `assets/example-breitling.json`), then run `python3 scripts/profile_board.py spec.json --out profiles --png`. It writes a `.dc.html` per profile for a Design canvas (rename the first to `Main.dc.html`) and a 2x PNG to upload to the deck and place full-slide. Update the JSON and re-run for each new version.

## Guardrails

- **No stereotypes.** Following Indi Young: age, gender and ethnicity don't cause behaviour.
- **Humanise without demographics:** draw people as simple neutral figures in a scene, with objects that tell their situation. No stock photos on mindset or JTBD profiles; on demographic personas only if the client needs them, and show diversity.
- **No invented quotes or stats presented as real.** Assumed quotes are labelled as such.
- **Purpose first.** If no one can say what decision a profile informs, don't make it.
- **Keep it digestible.** One board per profile; large type in the deck explainer slide, detail on the board.
- **No dark patterns** in the "what would tip them" levers.

## Deck section (Code research playback)

A section "Understanding the user", styled with `code-brand-style`:
1. Section divider
2. The User Profile Model: four types, best for, won't tell you
3. Research statement and questions (numbered chips coloured by type)
4. Questions plotted on the model; blind spots called out
5. The blend chosen and why
6. How to read the proto-personas: forces meanings + v0.1 → v0.2 → v1.0
7. One full-slide board per profile
8. Profiles against the findings (High / Medium / Low, labelled as judgement)
9. Data segments to build (segment, definition, what it tells us, source)
10. Validation plan with days per stage
11. Interview guides per role (full scripts in speaker notes)

## When Colin asks for a research programme

Always include: the research brief (statement, questions, quadrant plot, profile choice); methods per stage with participant numbers and recruitment criteria (recruit from segments, include people with access needs, both extremes); effort and days per stage (set-up, segments, recruitment, fieldwork, survey, synthesis, playback); interview scripts for each stakeholder or participant role (warm-up, context, core questions per research question, close). Code's balance: ~10 people to find the why, ~100 to confirm it at scale.

## Worked examples

- **Pure Pet Food:** push/pull profiles on what makes a customer choose and commit, built from real research, in the client's brand.
- **Breitling US (Oct 2026):** three proto-personas (reassurance seeker, value checker, deadline giver) from desk research and a site walk, with research and scale data to validate.
- **From the model:** blinds company (demographic), property developer (data segments), ombudsman (mindset; an 82-year-old and a 24-year-old shared one mindset), gift card company (JTBD "gesture" profiles).

## Expert tips

- Profiles aren't one-size-fits-all; pick the type for the question.
- The data in a profile should reflect the research goal that produced it.
- Start proto, version every update, and show what changed.
- Link profiles into the journey map (`cx-journey-map`), the Persuasion Model (`code-ux-review`) and test hypotheses: *Because we have observed… we believe that… will result in… confirmed when…*
