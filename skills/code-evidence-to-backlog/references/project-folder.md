# Project Folder

Every artefact a project **makes** or **collects** lives in one project folder, filed by stage and method. Cards on the stage board point at their own folder. "It's in the project folder" is all anyone needs to say: nobody uploads the same file to each ticket.

## Structure

```
<Client> – <Project>/
  _Inbox/                         unsorted drops; Claude files them
  _Ledger/
    <Client>_Evidence_Ledger.md
  00 Brief & scope/
    BR-1 Read the brief/
      inputs/                     what came in (the brief, client emails, RFP)
      outputs/                    what we made (brief summary)
    BR-3 Programme plan/ …
  01 Immersion/
    IM-2 Day 0/ …
  02 Discovery/
    DI-B1 Stakeholder interviews/
      inputs/                     recordings, transcripts, notes
      outputs/                    summaries, GROW write-up
    DI-M1 Competitor review/ …
  03 Vision/ …
  04 Definition/ …
```

- **Naming:** a method folder is named `<method ID> <method name>`. The ID is what matters, since it's how Claude and the board find it.
- **Scope:** only in-scope methods get folders. A method brought into scope later gets its folder when it's switched on.
- **Inputs and outputs:** `inputs/` holds anything collected (from the client, participants, desk research). `outputs/` holds anything made (by a person or by Claude). Provenance follows from this: inputs are sources, and outputs are tagged H, AI or AI✓ on the card.

## Where the root lives, and how it's pulled in

Setup **asks** where the client project folder lives, then **pulls the location in** rather than having anyone type it. It's usually one of two things:

- **A folder on someone's desktop**, reached through the desktop app:
  1. Check the connected folders (`get_device_info`). Use the one matching the client or project, with its absolute path and the machine name.
  2. If none matches, ask for it with `device_request_folder_access`.
  3. Store it on the board as `folderKind: "local"`, `folderRoot` (the absolute path) and `folderMachine`.
- **A shared cloud folder** (Google Drive, SharePoint, OneDrive):
  1. Take the link, or find the folder through the connector by client name and confirm it.
  2. Store `folderKind: "cloud"`, `folderRoot` (a readable name or path) and `folderRootUrl` (the link).
  3. Where the connector allows it, create the method subfolders and store each one's link on its card as `folderUrl`.

The location also goes in the Project Brain and at the top of the ledger.

**What the board shows:**
- **Header:** the location, e.g. "On Colin's MacBook: /Users/colin/Desktop/Acme – Website", or "Shared folder: … Open ↗".
- **Every card:** the full path to its own folder, with **Copy path** and, for cloud folders, **Open folder**.
- **Every knowledge entry:** the full path of its file.

So anyone can double-check that the stuff really lives there.

If the location changes (a folder moved, or a new shared drive), update `board/meta`. Every card follows, because card paths are worked out from the root plus `<NN Stage>/<ID> <name>`, unless a card stores its own `folder`.

**The CodeDesign repo** (`Clients/<Client> – <Project>/`) is a fallback for non-sensitive material only. Never put participant data there.

## Rules for Claude

1. **File everything.** Anything Claude makes for the project is saved to the method's `outputs/` folder, not left only in chat. Anything someone uploads into chat for the project is filed into the right `inputs/` folder first, then used. Say where it went in one line.
2. **"It's in the project folder."** Look in the card's folder (both `inputs/` and `outputs/`) and in `_Inbox/`. List what's new since the card's last entry, then log each new file as a card-knowledge entry: `type: "source"` or `"transcript"`, with `source` set to the path and `link` set to the file link if there is one. Update the card's `folderFiles` count. Then do the work asked.
3. **No method named.** If someone just says "I've put stuff in the folder", check `_Inbox/` and every in-scope method folder for new files. Suggest a card for anything in `_Inbox/` and move it once confirmed.
4. **Links over copies.** Card entries and the ledger point at the file in the folder. Don't paste whole documents into the board. A summary in the entry and a link to the file is enough.
5. **Personal data.** Recordings and transcripts with participant details stay in `inputs/` on the client-approved storage. If the root is the repo, don't put them there: say so and ask where they should live.
6. **Check it's really there.** On a status or gate check, confirm that every card in Done has its outputs in its folder, and that every knowledge entry's file still exists at its path. List anything missing or moved.
