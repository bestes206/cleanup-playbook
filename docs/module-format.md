# Fix module format

Every fix module follows this format. The reader of a module is the assistant, which relays it to the couple one step at a time. Write to the assistant in plain instructions, and put the words the couple needs to see (menu names, button labels) in **bold** exactly as they appear on screen.

`tools/check.py` enforces the parts marked *(checked)*.

## File name

`playbook/NN-module-<name>.md`. Modules are numbered in the order they should run. The name is flat and self-describing on purpose: when the files are uploaded to an assistant's project the folders disappear, and the file name is all the assistant has to go on.

## Header block *(checked)*

Start with a level-1 title, then this list:

```markdown
- **Fixes:** the pain, in words the couple would use ("never get locked out again")
- **Time:** total, and the per-part split, so they can do one part in a spare ten minutes
- **Who:** which partner, or both; and which parts either can do alone
- **Devices:** what they need in hand
- **Before you start:** what must already be true (decisions in the Map, earlier modules)
- **What changes:** one or two lines
- **What stays the same:** the apps and habits that do not change
- **Undo:** how the whole module is reversed
- **Last checked:** date and software versions the steps were checked against
```

The time estimate and the plain-language reason are requirements, not courtesy. Non-technical users decide whether to start based on "how long, and why should I care".

## Sections *(checked)*

1. `## Why this matters`. Two or three sentences the assistant can say nearly verbatim. Sell the fix by the problem it removes, not by the technology.
2. `## Before you start`. Checks the assistant makes against the Map before step 1, including what to do if a prerequisite is missing.
3. `## Parts and steps`. The work, split into parts that each end at a safe stopping point.
4. `## If your screen doesn't match`. Module-specific mismatches and what to do about each. The general routine lives in `00-start-here.md`; this section lists the known ones for this module.
5. `## Undo`. How to reverse each part.
6. `## Done when`. Observable checks. The module is not done until each one has been confirmed by the couple, not assumed.
7. `## Update the Map`. Exactly which Map lines and checklist items change.

## Step format

Each step inside a part:

```markdown
### Step 3. Share the calendar with your partner
- **Who / where:** the organizer, on the PC (phone alternative below)
- **Why:** one line
- **Do:** numbered taps, with on-screen labels in bold
- **Check:** what they should now see, and a question that confirms it
- **Undo:** how to reverse this one step, or "nothing changed" if it only looked
```

All five lines are required on every step *(checked)*. Steps are level-4 headings inside a level-3 `### Part N. Title (who, time)`, and every part ends with a **Safe stopping point** *(checked)*.

Rules for steps:

- **One change per step.** If a step changes two things, split it.
- **Add before remove.** A step that removes, deletes, replaces or turns something off comes only after the new thing is confirmed working, needs a backup first, and needs an explicit yes from the user in that moment. Mark such steps `**Removal step**` so the assistant treats them with care. *(checked: any step with a Removal marker must mention a backup and an OK)*
- **iPhone first.** Give the iPhone path first. If a step truly needs a computer, say so in the part header so nobody starts it on the bus.
- **No secrets in chat.** Never write a step that has the user type, paste, photograph or read out a password, PIN, code, recovery key or card number to the assistant. Steps that involve a password say where to type it (the app's or website's own screen) and say "don't tell me what it is".
- **Checks are questions.** "What do you see now?" beats "did it work?", because people say yes to the second one.
- **Purchases and sign-ups** are done by the user on the provider's own page, after both partners agreed in the tools agreement. The assistant never does them and never needs payment details.

## Plain words

Two lists. The glossary in `00-start-here.md` gives the plain version of each word.

- **Never used in a playbook file outside the glossary** *(checked)*: OAuth, system of record, source of truth, 2FA, two-factor (except in Apple's on-screen label "Two-Factor Authentication"), connector, vault, credentials, authenticate, migrate, ICS, IMAP.
- **Used only as an on-screen label or with an explanation in the same sentence** (not checked; review by eye): sync, subscribe and unsubscribe, default, backup codes.

## Keeping modules honest

- Menu paths go stale. Every module carries a **Last checked** line, and anything not confirmed against an official source is listed in `docs/research.md` under "not verified".
- The assistant is told (in `00-start-here.md`) that when a step doesn't match the screen, the screen wins. Modules should therefore explain the goal of each step well enough that the assistant can find another route to it.
