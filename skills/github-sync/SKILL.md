---
name: github-sync
description: "Use when the user wants to back up a design-studio-team-setup client project's docs to a shared GitHub repo, pull an existing GitHub project folder into a new claude.ai Project, or set up a recurring reminder for either. Triggers: 'sync to GitHub', 'back up this project', 'push docs to GitHub', 'check for new projects on GitHub', 'pull in the GitHub project folder', 'set up a sync reminder'."
---

# GitHub Sync — for design-studio-team-setup projects

Companion to `design-studio-team-setup`. Lets a client project's docs (Project Brain, role logs, Research Repository, Digest Index — everything that skill writes) travel to and from a shared GitHub repo, so the pattern is backed up, reusable as a template by colleagues, and portable between projects.

**Be upfront about the hard limits before doing anything.** These are platform boundaries, not missing features — don't build around them, and don't let the user assume otherwise:

- No tool available in a Claude session can create a new claude.ai Project. That click is always the user's, by hand, in the app. This skill can prepare everything else, but "make me a new Project" is a request to hand back to the user, not to attempt.
- No tool can reach into a *different* person's Claude account and push, sync, or install anything for them. Every colleague who wants this has to run this skill themselves, in their own account, with their own repo access and their own credentials. One person's setup never does work on another's behalf.
- Nothing here is a live, automatic, two-way sync. Every push, every pull, and every "check for new folders" is either a one-off action the user asks for, or a scheduled *reminder* that still stops and asks before doing anything with repo access.

## Repo and folder convention

Ask which repo to use if it isn't already known (check the current project's Brain and any `<ClientName>_GitHub_Sync_Log.md` doc first — don't re-ask what's already recorded). Each client project gets its own subfolder named after the client, matching the Project Brain's own naming convention, e.g.:

```
docs/<ClientName>/          — one .md file per project doc, same names as in the Project
README.md                   — what this repo is, and how a colleague turns a folder into their own Project (see "Pull", below)
```

**If the repo the user names is also a plugin marketplace repo** (it has a `.claude-plugin/marketplace.json` at its root — this plugin's own repo is exactly this shape) — stop and flag it before writing anything. Mixing plugin source code with confidential client docs in the same repo is very likely not what they want. Suggest a dedicated repo or a clearly separate top-level path, and get an explicit yes before proceeding into a marketplace repo.

## Action A — Push this project's docs to GitHub

1. Read every doc listed for the current Project with `project_read` (Project Brain, every role log, Research Repository, Digest Index, and this project's own `<ClientName>_GitHub_Sync_Log.md` if one exists).
2. Write each as a `.md` file under `docs/<ClientName>/` in a local working copy of the repo, same filenames. Write or refresh the top-level `README.md` explaining what the repo holds and how to reuse a folder (point at Action B).
3. Ask for a fine-grained GitHub personal access token, scoped to only this one repo, Contents: Read and write. Never store it — it's used for this push only and dropped afterward. Never write it into a project doc, a memory file, or anywhere durable.
4. Commit with a date-stamped message and push.
5. Create or update `<ClientName>_GitHub_Sync_Log.md` in the Project (via `project_write`, following `references/sync-log-template.md`) recording the repo URL, the subfolder, and the push date. This is what lets a future session — this user's or a colleague's — pick up the repo details without re-asking.

## Action B — Pull a GitHub folder into this Project

Use this once the user has already created the empty destination Project by hand and a session is attached to it.

1. Ask for the repo URL and the subfolder name (e.g. `docs/<ClientName>/`), and — only if the repo is private — a token. A read-only, repo-scoped token is enough for a pull; never ask for more access than the action needs.
2. Fetch each `.md` file's current content from that folder.
3. Write each one into the current Project with `project_write`, keeping the original filenames.
4. Create `<ClientName>_GitHub_Sync_Log.md` in the new Project the same way as Action A, step 5, so this Project also knows where it came from.

## Action C — Recurring reminders

Always use the scheduled-task tools (`create_trigger` and friends) for anything recurring. Never the local cron tools — those die with the session and the reminder silently never fires again.

Ask the user which of these they want, and for each, how often:

**Push reminder** — fires in a fresh session on the user's chosen schedule. Write its prompt to be self-contained: open the Project, read `<ClientName>_GitHub_Sync_Log.md` for the repo URL and subfolder so it doesn't have to ask again, then ask the user if they want to push now. If yes, run Action A (still asking for a fresh token each time — a scheduled push reminder is not licence to store one).

**New-folder check** — fires on the user's chosen schedule to look for project folders in the shared repo they haven't turned into a Project yet. Ask the user, with `AskUserQuestion`, which mode they want before setting this up (default to the first if they have no preference — it's the safer one):

- *No stored credential (default):* the reminder just nudges — "go take a look at the shared repo and tell me if there's anything new" — and does nothing on its own. Safest, but it's a nudge, not a check.
- *Read-only token stored with the schedule:* the reminder actually lists the repo's top-level folders itself, compares against ones already known (keep this list in the user's own account-level memory or a tracking doc — never inside a specific client Project, since this check spans all of them), and only pings when it finds something new. Faster, but say plainly that a credential — even read-only and scoped to one repo — then lives in the schedule's stored configuration. Get an explicit yes before setting this up this way.

Either way, finding a new folder never creates anything by itself. It always ends with asking the user whether they want it — and if they do, the answer is "go create the empty Project by hand, then come back and say pull it in," followed by Action B.

## References

- `references/sync-log-template.md` — the `<ClientName>_GitHub_Sync_Log.md` template used by Actions A and B.
