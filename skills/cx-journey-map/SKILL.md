---
name: cx-journey-map
description: Build a Code-format current-state CX journey map ("customer journey full detail", the Pure Pet Food format) from client assets, desk research and interviews. It shows evidence, data gaps and the research still needed, plus a flow row of exits and loops, and adds interview insights tagged P1, P2 and so on. Use when Colin asks for a CX map, journey map, experience map or service-style map for a client, or to add interview findings to one.
---

# CX Journey Map

This builds Code's "Customer journey full detail" map: the format Code used for Pure Pet Food, with stage chevrons, numbered customer steps and a row per lens. It adds three things a desk-research map needs to be honest:

- an **Evidence** row, showing what each stage is built on;
- a **Research needed** row, giving each gap a question, method and priority;
- **"data needed" cards** wherever a number is missing.

A **Flow** row shows how the steps connect: exits, loops, re-entry and time gaps. Interview findings go on as tagged cards (P1, P2 …) so first-hand evidence stands apart from desk research.

It follows the mapping module of `code-design-playbook`:
- mapping is collaborative;
- it's a shared view, not a personal record;
- keep it low-fidelity while still gathering input;
- call out the critical points;
- back pain points with data, not just assertion.

Read `references/map-spec.md` before building. It defines every row, card and convention, and the JSON format the builder takes.

## Step 1 — Gather and read the inputs

- **Client assets:** journey maps, persona or ICP docs, research decks, audience setups, analytics. Read all of them, including image-only slides; render those to images and look at them, because text extraction misses most of them.
- **Format example:** if Colin points at a previous map (e.g. Pure Pet), look at it to match its rows and style. Otherwise use the spec as written.
- **Interviews and notes:** each participant gets a tag (P1, P2 …) in the order they're added.
- If the session has a company brain (Project Brain, Research Repository), check the Repository first for anything already known.

Write down, for each finding:
- its **source**;
- whether it's **about this client's journey or a proxy**, e.g. another client's portfolio or a different market;
- any **caveat**, e.g. results run across different markets, a method that isn't known, or an internal participant.

## Step 2 — Shape the journey

- **Stages:** pick 5–8, using the client's own words where they have a framework.
- **Steps:** aim for 15–20 customer actions in total. A step is something the customer does, not what the business does.
- **Funnel band:** add the client's lifecycle bands if they use them (e.g. Lead → Registered → Active).
- **Scope band:** mark the part of the journey the engagement is actually working on. Steps inside it get a tinted column.

## Step 3 — Fill the rows

Use `map-spec.md` for what goes where.

- **Data:** every number carries its source. Each important number you don't have becomes a "data needed" card. Never estimate one.
- **Pains, positives and internal challenges:** short, plain and specific. Internal challenges are stakeholder quotes with the speaker.
- **Comms:** CRM and outbound messages only, happening or missing: emails, texts, calls, letters, ads, confirmations and reminders. Add a dashed "Missing: …" card, labelled with its channel ("Email / SMS"), where an obvious message doesn't exist. Website content isn't comms: a gap in what a page says or shows is a customer pain or an HMW.
- **Mindset:** real quotes only, each tagged to a profile. If the profiles come from desk research, label them provisional.
- **Evidence and Research needed:** per stage, be honest about confidence. Every stage with no user evidence says so in red.
- **HMW:** one per real opportunity, not one per step for the sake of it.

## Step 4 — Draw the flow

In the spec's `flow` block, add:
- **exits:** where people drop out, and the step they leave from;
- **loops:** back-and-forth, retries and re-entry;
- **gaps:** time where nothing happens, e.g. "dormant for months".

Interview-sourced loops and gaps get the participant tag. The builder lays loops out in lanes so overlapping ones stay readable.

## Step 5 — Build it

1. Write the spec as JSON (see `references/example-map.json`).
2. Run the builder:
   `python3 scripts/build_map.py map.json Main.dc.html`
   It refuses to build if stage, funnel or flow step counts don't add up, and reports how many "data needed" cards there are.
3. Publish the artboard to a **Design** canvas when that Artifact type is available. Use a wide artboard (the width the builder sets) and a second artboard, **"Research we need to run"**, which carries:
   - who to talk to, by cohort, with numbers and recruitment route;
   - methods with effort in days and priority;
   - the desk claims to test;
   - the data to ask the client for.
4. No Design canvas? Use `--standalone` to get a plain HTML page and publish that instead.
5. Keep the JSON spec with the client's project docs. It's the source the map is regenerated from.

**Every card is literal text** (no template placeholders), so people can click into the canvas and edit any card directly. Don't switch the map to data-bound cards; editors would see placeholder tokens instead of the words.

## Putting the map in a deck

Research playbacks, UX reviews and market reviews show the map in their "Research outcomes" section. Two slides, styled by `code-brand-style` (`references/deck-system.md`):
1. **Your end-to-end customer journey map:** the "title only" layout, with a light headline ("Your end-to-end **customer journey map**"), one line on what it covers and its version, and the whole map as an image on the right. Render the map with `--standalone`, screenshot it full page, and upload the image as an asset.
2. **Reading a map** (optional, for a client seeing the format for the first time): the map image with labelled callouts for each row: stage, steps, data, positives and pains, internal insights, comms, opportunities.

Re-render the image whenever the map changes, so the deck and the map agree.

## Step 6 — Adding an interview

Run the interview one question at a time and follow the participant's story. Then:
- add their findings to the spec with the `Pn|` prefix: pains, positives, comms, HMWs, flow loops and gaps;
- add their quotes as mindset cards using a participant profile;
- update the stage `user_evidence` chips, and any Evidence note the interview changes (especially where it contradicts desk research);
- rebuild and republish;
- write it up as an interview note, and as a Research Repository entry if a company brain exists, with caveats stated plainly. Caveats include: an internal or project-team participant, a research-led rather than natural trigger, or outside help most customers wouldn't have.

## Revising a published map

People edit the canvas by hand. Before changing it, read the current artboard and compare it with what you last published. If they've edited it, carry their edits into the spec first, so a rebuild doesn't wipe their work. If the canvas re-fits an artboard's height, keep its layout and only make room for what you add.

## Fences

- The map is an internal draft until Colin approves it. Say so in the footnote.
- It usually carries client data (portfolio metrics, ICP numbers, stakeholder quotes). Before it's shared, check the artifact's sharing setting and flag it if it's open to anyone with the link.
- Don't put client logos or brand marks on the map. Use a plain text badge.
- Client data never goes in this skill's repo. Only fictional examples live in `references/`.
