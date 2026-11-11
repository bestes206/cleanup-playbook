# Requirements

Derived from `docs/brief.md`: the "Brief for Claude Code" section, its "For Claude Code to work out" list, and the panel review. Each requirement says where it came from and where it is met. *(checked)* means `tools/check.py` enforces it.

Sources: **B** = Brief for Claude Code. **W** = the "work out" list. **P-Sec**, **P-Admin**, **P-User**, **P-Ops**, **P-Agent** = panel reviewers. **P-Plan** = the panel's "what this changes in the plan" checklist. **DP** = design principles.

## Starter prompt

| ID | Requirement | Source | Met in |
| --- | --- | --- | --- |
| S1 | Its first lines set up ChatGPT: shared Project, Chat not Work, GPT-6, Medium thinking; High only if the tools agreement feels thin; no Instant, Pro or Work | B | `starter-prompt.md` *(checked)* |
| S2 | It states the no-passwords-in-chat rule | P-Plan, P-Sec | `starter-prompt.md` *(checked)* |
| S3 | One prompt is all the helper sends, and it works for the first session and every later one | B | `starter-prompt.md` (resumes from the Map if one exists) |
| S4 | It does not depend on the assistant opening a web link | W1 | Files are uploaded to the project; safety rules are inline. See `docs/research.md` section 3 |
| S5 | The assistant confirms the setup with the users, since it cannot see its own mode or model | derived from S1 | `starter-prompt.md`; `01-assistant-notes-chatgpt.md` |

## Every session

| ID | Requirement | Source | Met in |
| --- | --- | --- | --- |
| G1 | One question at a time, in plain language; "I don't know" is an acceptable answer | B, P-User | `00-start-here.md` rules 2 and 3; `02-intake.md` |
| G2 | No jargon without an explanation; "subscribe", "OAuth", "system of record" never appear bare | P-User | Glossary in `00-start-here.md`. A list of hard-banned words is *(checked)*; "subscribe" and "sync" appear only as on-screen labels or with an explanation, which is reviewed by eye, not checked |
| G3 | The assistant checks in before every change and confirms after | DP4 | `00-start-here.md` rule 4; every step has a Check line *(checked)* |
| G4 | Add before removing; remove only with a backup and an explicit OK; every step reversible | B, DP2 | `00-start-here.md` rule 5; an Undo line on every step *(checked)*; removal steps marked, each with a backup and a yes *(checked)*. One step is irreversible by nature (shredding the notes, Fix 1 step 7.2) and says so |
| G5 | Never ask for passwords in chat; say so up front; use the provider's own sign-in screens | B, P-Sec | `00-start-here.md` rule 1; starter prompt; each module |
| G6 | Every step works on an iPhone; where a computer is unavoidable, the part says so before it starts | B, DP5 | Partly met. Computer-only: Fix 2 Part 2 (creating a Google calendar). May need a computer: Fix 2 steps 3.2 and 4.4 (the second is optional), setting calendar alerts in Fix 3 step 3.4, and the password app sign-up in Fix 1 step 1.1 (phone route unconfirmed). Each says so in its header or Who line |
| G7 | Saved progress and a resume flow; either partner can pick up where the other stopped | B, P-Plan, P-User | `04-map-and-checklist.md`; "Start of every chat" in `00-start-here.md`; loading, a failed save, and two partners saving the same version number are handled in `01-assistant-notes-chatgpt.md` |
| G8 | What happens when a step goes wrong halfway is defined | panel's "biggest gap" | Safe stopping points after every part; "The screen wins" and "When to bring in the helper" in `00-start-here.md` |
| G9 | Each reach-out to the helper is logged as feedback, not failure | B | `helper/feedback-log.md`; *Questions for the helper* in the Map |
| G10 | The playbook runs the same in any assistant | DP6 | Core files name no assistant; specifics isolated in `01-assistant-notes-chatgpt.md` |
| G11 | Nothing changes silently | B | `00-start-here.md` rules 7 and 8 |

## Intake

| ID | Requirement | Source | Met in |
| --- | --- | --- | --- |
| I1 | Run as one joint session with both partners, together with the tools agreement | B | `02-intake.md` (won't start with one partner) |
| I2 | Produces a saved map of accounts, devices, calendars and pain points | B | `02-intake.md` parts 1 to 8; `04-map-and-checklist.md` |
| I3 | Establishes which login is each person's Apple Account | user story | `02-intake.md` question 7 |
| I4 | Records who owns each account and whether it is business or personal | P-Ops | `02-intake.md` part 3 |
| I5 | Flags accounts run by an employer or brokerage | P-Ops, P-Admin, P-Plan | `02-intake.md` part 3 (`managed by someone else`) |
| I6 | Captures where client meetings go and who uses the brokerage account (the brief's open questions) | brief, open questions | `02-intake.md` questions 5 and 15 |
| I7 | Ranks pains so fixes can be ordered by what bugs them most | B, DP3 | Partly met, by design. `02-intake.md` part 1 and closing rank the pains. The order of the three fixes is fixed by dependency (decision 18), so the ranking is used for: the one early win offered at the end of `03-tools-agreement.md`, which accounts and schedules go first inside each fix, and which parked problem becomes the next module |
| I8 | Captures what they expect the assistant to be able to answer, as the pilot's test | B (pilot success) | `02-intake.md` question 26; `helper/debrief.md` question 11 |

## Tools agreement

| ID | Requirement | Source | Met in |
| --- | --- | --- | --- |
| T1 | Options side by side in plain words: cost, change to their day, how well the assistant connects | B | `03-tools-agreement.md` decisions 1 to 3 |
| T2 | A clear recommendation with reasons; the users choose | B, P-Plan | Each decision |
| T3 | Apple versus Google presented as a tradeoff | P-Plan, P-Agent | Decision 2 |
| T4 | Both partners explicitly agree, including anything to buy and how it is shared | B | "How to run each decision" step 5; closing |
| T5 | A compliance check before any work email account is connected | P-Plan, P-Ops | Decision 5; rule 9 in `00-start-here.md` |
| T6 | A paid business email account is flagged as an option, not a requirement | P-Ops | Decision 5, last paragraph |
| T7 | Which password manager to recommend, and whether setup needs a person | brief, open questions | Decision 1 |

## Every fix module

| ID | Requirement | Source | Met in |
| --- | --- | --- | --- |
| M1 | A time estimate up front | B, P-Plan, P-User | Header *(checked)* |
| M2 | A plain-language "why" | B, P-Plan | "Why this matters" and each step's Why *(checked)* |
| M3 | A "my screen doesn't match" path | B, P-Plan, P-User | Section in every module *(checked)*; general routine in `00-start-here.md` |
| M4 | Who does which step on which device | P-User | "Who / where" on every step *(checked)* |
| M5 | Safe places to stop | P-User | End of every part *(checked)* |
| M6 | Follows one documented format | W4 | `docs/module-format.md` *(checked)* |

## Fix 1: password manager

| ID | Requirement | Source | Met in |
| --- | --- | --- | --- |
| P1 | Email accounts first when replacing the reused password | P-Sec | Part 4, before Part 6 |
| P2 | Second sign-in step on every email account and the Apple Account; an Apple recovery contact | P-Sec | Steps 4.6, 5.1, 5.2 |
| P3 | A recovery plan with an emergency kit stored offline | P-Sec | Part 2; each email account's own recovery phone and address checked in step 4.2 |
| P4 | A shared vault plus a personal vault each | P-Sec | Part 1; agreement decision 1 |
| P5 | Old accounts checked against known breaches | P-Sec | Step 4.1 |
| P6 | The old passwords and notes are kept until the new system is proven | DP2 | Step 4.3; Part 7 |
| P7 | Shared accounts are changed without locking the other person out | derived | Part 4 introduction (app installed for everyone first; never one partner alone); step 4.6; Part 6 |

## Fix 2: shared calendar

| ID | Requirement | Source | Met in |
| --- | --- | --- | --- |
| C1 | Uses a two-way account where they need to change events and a read-only link where they only follow | P-Admin | Part 3 (account) and Part 4 (followed schedules) |
| C2 | A PC user can see the shared calendars | P-Admin | Step 3.4; iCloud variant. Followed schedules reach the PC only through optional step 4.4 |
| C3 | One shared calendar for family and one for business | user story | Part 2 |
| C4 | Kids' schedules reach both phones | user story | Part 4 |
| C5 | Tells live subscriptions from dead ones | brief, open questions | Step 6.1 |
| C6 | Dead calendars are hidden first, removed later, with a backup and an OK | DP2 | Part 6 *(checked)* |
| C7 | The assistant ends up with a calendar it can read and, if agreed, write to | P-Agent | Part 7. Limit: it reads Family and Business; followed schedules only after optional step 4.4. The assistant is told to name what it cannot see every time it answers |

## Fix 3: commitment capture

| ID | Requirement | Source | Met in |
| --- | --- | --- | --- |
| K1 | Comes after the shared calendar, and depends on it | B | "Before you start" |
| K2 | Capture is nearly effortless, ideally by voice | P-Ops | Part 2 |
| K3 | Captured things land on the calendar with an alert | user story | Part 1 |
| K4 | The organizer stops being the human reminder | persona | Step 3.2 |
| K5 | An event one partner captures alerts the other | derived | Step 3.4 |

## The Map and checklist

| ID | Requirement | Source | Met in |
| --- | --- | --- | --- |
| D1 | Useful, with nothing sensitive in it | W3 | "What never goes in the Map" in `04-map-and-checklist.md`; `tools/check.py` rejects secret-shaped fields in the template and example *(checked)* |
| D2 | Saved where both partners can see it | B | Project sources, per `01-assistant-notes-chatgpt.md` |
| D3 | A checklist that shows what is done | P-User | Checklist section and marks |
| D4 | A format later agents can start from | P-Agent | Fixed section order *(checked)*, one fact per line; `examples/example-map.md`. The panel asked for the Map to be saved in the repo; it is saved in the couple's project instead, because the repo must hold no real details (decision 20) |
| D5 | One page showing every account, app and calendar | user story | The Map itself |

## Upkeep and the repo

| ID | Requirement | Source | Met in |
| --- | --- | --- | --- |
| U1 | A short monthly checkup | P-Plan, P-Ops | `20-monthly-checkup.md`; its calendar reminder is created in Fix 3 step 5.3 |
| U2 | No real person's name or account details in the repo | kickoff prompt | `tools/check.py` privacy scan *(checked)*; brief byline redacted |
| U3 | Research states what could not be verified | kickoff prompt | `docs/research.md` |

## Not in this slice

From the brief's user stories, parked until a later module and captured in the Map's parking lot during intake: bringing business inboxes into one mail app, notification cleanup, Messages matching between devices, and where industry software fits. The brief's open question on industry tools is not answered here.
