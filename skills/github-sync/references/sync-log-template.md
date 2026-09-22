# <ClientName> — GitHub Backup / Sync Log

Tracks this Project's backup to (and, if relevant, its origin from) a shared GitHub repo, following the `github-sync` skill.

## Status
- **Repo URL:** (e.g. https://github.com/<owner>/<repo>)
- **Subfolder:** docs/<ClientName>/
- **Last successful push:** (date, or "never")
- **Pulled from GitHub on setup:** (date, or "no — this Project originated here")
- **Sync mode:** Manual push/pull by default. A push reminder and/or a new-folder check may also be scheduled — note below if so, and which mode the new-folder check uses (no stored credential / read-only token stored with the schedule).

## What a push does
1. Export every doc in this Project's list to `.md` files, same names, under the subfolder above.
2. Write or refresh the repo's top-level `README.md`.
3. Commit with a date-stamped message and push, using a token supplied fresh for that push only.
4. Update this log's Status section.

## History
- <date>: <what happened — log created / pushed / pulled / reminder scheduled, etc.>
