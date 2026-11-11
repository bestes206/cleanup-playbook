# Digital Cleanup Playbook

A guided cleanup that an AI assistant walks a household through, in plain language, so that their accounts, calendars and passwords are tidy enough for an assistant to be useful afterwards.

**Garbage in, garbage out.** The best agent in the world gives bad answers on top of scattered accounts, unshared calendars and one reused password. This playbook cleans the inputs first.

It is written for people who are not technical: typically a couple running a household and a small business together, one mostly on a phone, the other carrying the whole system in their head. A **helper** (a tech-savvy friend or consultant) hands it to them and stays on call.

## Status

First slice, ready to pilot with one couple in a shared ChatGPT Business project. Not yet run with real users. `docs/research.md` lists what was verified from official sources and what the pilot still has to prove.

## How it works

1. The helper uploads the nine files in `playbook/` to the couple's shared project and sends them one message: the block in `starter-prompt.md`.
2. **Joint session (about an hour, both partners).** The assistant interviews them one question at a time and builds their **Map**: every account, device and calendar, and what bugs them most. Then they agree together on what to use.
3. **Three fixes,** in short sittings, by either partner:
   1. A password app, shared safely, with the reused password replaced.
   2. Shared Family and Business calendars, in the calendar app they already use.
   3. A habit for capturing promises the moment they are made.
4. Progress is saved in the Map after every sitting, so either partner can pick up where the other stopped.
5. A ten-minute monthly checkup keeps it from drifting.

## The rules it runs by

- Never ask for a password, code or card number in a chat.
- One question or instruction at a time, in plain words. "I don't know" is fine.
- The assistant guides; the people make every change themselves.
- Add before removing. Nothing is removed without a backup and a clear yes.
- Every step says why, how long, who, on which device, and how to undo it.
- When the screen doesn't match, the screen wins.

## What's in the repo

```
starter-prompt.md        The one message the helper sends
playbook/                The assistant's instructions (upload these nine files)
  00-start-here.md         Session routine and ground rules
  01-assistant-notes-chatgpt.md   Everything specific to ChatGPT
  02-intake.md             The interview
  03-tools-agreement.md    Deciding together what to use
  04-map-and-checklist.md  The Map format, saving and loading
  10-module-password-manager.md
  11-module-shared-calendar.md
  12-module-commitment-capture.md
  20-monthly-checkup.md
helper/                  For the person handing it out
  pilot-setup.md           Setup, smoke test, being on call
  feedback-log.md          Where every reach-out is recorded
  debrief.md               The end-of-pilot conversation
examples/example-map.md  A filled-in Map for an invented household
docs/
  brief.md                 The problem statement this was built from (public edition)
  requirements.md          Requirements, traced to the brief and to files
  research.md              Findings, sources, and what is unverified
  decisions.md             Design decisions and why
  module-format.md         How to write a fix module
tools/check.py           Structural checks; run before every commit
```

## If you are the helper

Start with `helper/pilot-setup.md`. It takes about 30 minutes, most of it a smoke test that settles the things research could not confirm.

## If you are changing the playbook

- Read `docs/module-format.md` before writing or editing a module.
- Run `python3 tools/check.py`. It must report zero errors.
- Menu paths go stale. When you re-check a module against current screens, update its **Last checked** line.
- Keep the repo free of real names, addresses and account details. Examples use invented people and `example.com`. To have the check scan for specific names, list them one per line in a git-ignored `.private-terms` file.
- Feedback from the pilot goes in `helper/feedback-log.md`; if it contains anything identifying, keep that copy outside the repo.

## Other assistants

Eight of the nine playbook files are written for any assistant. To run it in Claude or Grok, write a notes file to replace `01-assistant-notes-chatgpt.md` and change the setup lines at the top of the starter prompt. `docs/research.md` sections 4 and 5 have what is known about each. Only the ChatGPT path has been prepared for a pilot.

## What is kept out of this repo

This repo is public. It holds no real person's name, address or account detail, and it should stay that way.

- The original brief described a real household's setup, so only a trimmed edition is here (`docs/brief.md`).
- A household's Map lives in that household's own project, never here.
- Before every commit, run `python3 tools/check.py` with a `.private-terms` file listing every real name involved in a pilot.
