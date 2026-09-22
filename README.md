# design-studio-team-setup

A Claude plugin for Colin Preston. Sets up a "company brain + desks" pattern for a new design consultancy client engagement: one shared Project Brain, a roster of role "desks" each with a one-page brief and a memory log structured in three zones (Active Notes / Digest / Archive) so it stays usable as the engagement grows, a shared project-level research repository built the same way, a standing Digest Index that rolls up every desk's current Digest into one page for a step-back read, a retrieval mode (RAG-style: search, then answer only from what's found and cite the source) for specific questions rather than routine work, a Delivery Manager that both reacts (status checks, stalled-handoff spotting) and proactively routes new multi-desk work (sequencing who's needed and in what order from the roster's dependency graph, before anyone starts), a visual desk-status dashboard, and a Colin send/edit/skip review gate.

Default roster (eleven desks): Lead UX Designer, Lead UX Researcher, Expert Workshop Facilitator, Product Consultant, Engineering Principal, QA & Definition Lead, Content/UX Writer, Visual/Brand Designer, Data & Insight Analyst, Meeting Notes Lead, and Delivery Manager — plus whatever additional specialists a given engagement needs.

Bundles three more skills: `code-design-playbook` (Code Computerlove's internal design team curriculum, standing context for every design-facing desk), `code-brand-style` (Code's visual identity, for anything that should look on-brand), and `github-sync` (push a project's docs to a shared GitHub repo, pull an existing repo folder into a new Project, and schedule reminders for either — the mechanism for backing projects up and reusing this pattern across the team).

## Installing this

This repo is a Claude plugin marketplace (`.claude-plugin/marketplace.json` at the repo root). Add the marketplace from this repo's URL, then install the `design-studio-team-setup` plugin from it — all four of its skills come with it.

## Structure

```
.claude-plugin/
  marketplace.json                          — marketplace manifest, plugin sourced from "./"
  plugin.json                               — plugin manifest (repo root doubles as plugin root)
README.md
skills/
  design-studio-team-setup/
    SKILL.md                                — the team-setup skill
    references/
      project-brain-template.md             — shared engagement-level context doc
      role-brief-template.md                — per-role brief template
  code-design-playbook/
    SKILL.md                                — Code's internal design curriculum
  code-brand-style/
    SKILL.md                                — Code's visual identity
    references/
      tokens.css                            — brand colour/type tokens
  github-sync/
    SKILL.md                                — push/pull a project's docs to/from a shared GitHub repo
    references/
      sync-log-template.md                  — the per-project GitHub sync log doc

```

Every skill Claude's plugin loader can discover lives at `skills/<skill-name>/SKILL.md` under the plugin root — that's the convention this structure follows for all four skills.
