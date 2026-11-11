# Decisions

The choices that shaped the first slice, and why. Newest at the bottom. When one is reversed, add a new entry rather than editing the old one.

## 1. The playbook travels as uploaded files, not as a link

The helper puts nine Markdown files into the couple's project, and the starter prompt points at them by name.

Why: no official source describes how ChatGPT reads a linked repository, older community reports are mixed, and the repo is not public. Uploading files to a project is documented and works the same on every plan. The cost is one extra setup task for the helper. A link can be added as a fallback once the repo is public and the behaviour has been tested.

## 2. The same prompt starts and resumes

The starter prompt checks for a saved Map and either begins the interview or picks up where they stopped.

Why: non-technical users should have one thing to keep. A separate "resume" prompt is one more thing to lose, and in a shared ChatGPT project each sitting has to be a new chat anyway, because one partner cannot type into the other's.

## 3. One document, the Map, holds both the map and the checklist

Why: saving in ChatGPT is a manual step a person performs. One document means one save and one load, and resuming needs both halves anyway. The checklist sits near the top so "where are we" is the first thing anyone reads.

## 4. A person saves the Map; the assistant never claims it is saved

The assistant posts the full Map as its own message and walks the person through "Add to project sources", then asks them to confirm it is listed.

Why: no documented way exists for ChatGPT to write into a project's files, and recall across chats in a project is not guaranteed. A save the person can see is a save that exists. This is the least proven step in the design, so it has two fallbacks and is the first thing the helper's smoke test checks.

## 5. The Map uses lists, not tables, and plain words for unknowns

Why: it is read on a phone, and it is meant to be picked up later by other agents. One fact per line is readable at phone width and easy for a program to parse. `not sure yet` is recorded rather than omitted because the gap tells the next module what to look up.

## 6. Email addresses are allowed in the Map; secrets are not

Why: the Map's job is to tell accounts apart, and that is impossible without addresses. Addresses are identifiers, not secrets. Everything that could open an account or embarrass someone is excluded by an explicit list in `04-map-and-checklist.md`, including the location of the emergency sheets, clients' names, and links to private calendar feeds.

## 7. Everything specific to one assistant lives in one file

`01-assistant-notes-chatgpt.md` holds the setup check, how sharing behaves, where the Map is stored, and which connections exist.

Why: the brief asks for a playbook that runs in any assistant, but saving, sharing and connections differ sharply between them. Isolating those differences keeps the other eight files neutral, and adding an assistant means writing one notes file.

## 8. The assistant guides; the people make every change

The assistant does not change anything in their accounts, except a calendar event when asked for that exact event.

Why: the brief requires that nothing changes silently and that every step can be undone. People who make a change with their own hands know it happened and where. It also means the playbook works the same whether or not the assistant has any connections.

## 9. Recommend 1Password Families when a Windows PC is in daily use

Why: the pilot household is two iPhones and Windows PCs. Of the three options compared, it is the only one that is equally good on both, it comes with a shared box and a private box each, and each partner can restore the other's access. Apple's built-in app is free and the least change, but on Windows it needs an iPhone nearby and cannot manage sharing. Bitwarden's free tier covers the basics but has no way back in for a forgotten password. The agreement states when each alternative is the better call. Cost at the time of writing: about $72 a year.

## 10. Recommend Google as the calendar home, viewed in Apple Calendar

Why: it is the only calendar that ChatGPT, Claude and Grok all connect to through an ordinary sign-in screen, it opens in any browser on a PC, and the couple keep the Apple Calendar app. ChatGPT gained an iCloud connection in late October 2026, so iCloud is offered as a real alternative for a ChatGPT-only household, with the tradeoff stated: it ties them to one assistant.

## 11. Followed schedules are added on each phone, not routed through Google

Each partner follows the kids' team schedule on their own iPhone, stored in iCloud.

Why: the pain is "it's only on one phone". Following the link directly is a two-minute step that can be done entirely on the phone. Routing it through Google needs a computer, an extra sync setting, and refreshes more slowly. The price is that neither the assistant nor the PC's browser view can see followed schedules. The calendar module says so plainly, tells the assistant to name what it cannot see whenever it answers a "what's on" question, and offers an optional computer step (4.4) that adds the schedule to each person's Google account for those who want the assistant to see it.

## 12. Hiding is the default end state for old calendars

Calendars are hidden for two weeks before removal is even offered, and a calendar with events in it is left hidden unless the helper is involved.

Why: deleting an iCloud calendar deletes its events everywhere, and backing one up without a Mac is fiddly. Hiding delivers the benefit, a clean view, with no risk. The brief's rule is add before remove, and here "don't remove" is usually the right amount of removal.

## 13. Promises go on the calendar; to-dos get a time

Why: the partner who loses commitments needs one place and one alert. A separate to-do list is a second thing to forget, and Apple Reminders cannot use a Google account, so the assistant would not see it. Giving an untimed promise a time is the habit that makes it real.

## 14. One default calendar per phone, chosen by the person

Why: Siri puts events on the default calendar and cannot reliably be told a calendar by name. Both shared calendars are visible to both partners, so an event on the "wrong" one is still seen, and moving it takes two taps. That is a better trade than asking someone in a truck to choose a calendar every time.

## 15. A monthly checkup is included in the first slice

It is not one of the three required fix modules.

Why: the panel's plan checklist asks for it, it is short, and each of the three fixes leaves something that drifts: new accounts with weak passwords, seasonal schedules, the capture habit. It runs once the fixes are done or far enough along to have something to check, and its calendar reminder is created at the end of Fix 3.

## 16. Structural checks stand in for tests

`tools/check.py` verifies the things that can be checked mechanically: file set, starter prompt contents, module format, removal steps, jargon, checklist-to-module agreement, and personal details.

Why: the playbook is prose run by a language model, so correctness can only be judged in the pilot. The checks stop the mechanical regressions that would otherwise creep in as modules are edited.

## 17. The author's name was removed from the saved brief

`docs/brief.md` is the brief as written, except that the byline's name is replaced with a placeholder.

Why: the instruction to keep the repo free of real names outranks an exact copy of one byline. Nothing else in the brief was changed.

## 18. The order of the three fixes is fixed; the pain ranking steers everything else

The brief says fixes are ordered by pain, and also names the first slice's order: password app, shared calendar, commitment capture.

Why the order is fixed: each depends on the one before. The calendar step signs in to Google accounts on several devices, which should happen once, with passwords that are already unique and stored. Capturing promises needs the shared calendars to land on. So the ranking from the interview is used where it can be honoured: one early win is offered straight after the agreement (getting a kids' schedule onto the second phone needs nothing else), the most painful accounts and schedules go first inside each fix, and the ranking picks which parked problem becomes the next module.

## 19. The joint session has one optional break, and some later parts need both partners

The brief describes intake and agreement as one joint session, after which either partner can run fixes alone.

Why the break: an hour is long for someone with little patience for setup, and a tired couple makes poor decisions. The interview ends with a saved Map, so pausing there loses nothing; the agreement still requires both. Why some fix parts need both: creating the family account, storing the emergency sheets, anything touching an account both use, the house rule, and the final removal each affect both people, and the rule that nothing changes silently outranks convenience. Everything else is per person.

## 20. The Map is saved in the couple's project, not in this repo

The panel suggested saving the intake map as a file in the repo so later agents can start from it.

Why not: the repo must contain no real names or account details and may become public. The Map is saved in the couple's own shared project, in a fixed format, which gives later agents the same starting point without putting a household's details under version control. The repo carries the blank format and an invented example.

## 21. "Finished" is defined for the debrief

The modules include deliberate waits: two weeks before the sticky notes are retired, a one-week check on the capture habit, a two-week experiment.

Why define it: without a definition, "both partners finish the first slice" cannot be true at a two-week debrief. `helper/debrief.md` sets the bar at the joint session, Fix 1 through Part 6 for the important accounts, Fix 2 through Part 5 and Fix 3 through the one-week check, and expects three to five weeks.

## 22. Changes made after independent review

Two reviewers on a different model read the finished slice, one hunting for ways the steps could lock someone out or lose data, one checking it against the brief. Changes that came from them:

- A shared account's password is never changed until everyone who uses it has the password app working, and never by one partner alone.
- Each email account's own recovery phone and backup address are checked before its password changes.
- Where the sign-in code goes on a shared account is settled before the second sign-in step is switched on, and mail delivery is re-tested afterwards on every device.
- The password app's trial is settled before the bulk of password changes begins.
- A calendar the couple created is never treated as empty; it stays hidden.
- The person who owns a Google account is the one who signs in to it.
- Two partners saving the same Map version number is detected and merged.
- Resuming always means pasting the starter message again.
- The playbook states what the assistant cannot see, instead of implying it sees everything.
- An event one partner captures is checked for an alert on the other's phone.

## 23. The Map is found by its contents, not by a file name or by being first in the file

A live run (research section 8) showed two things the design had assumed wrongly. ChatGPT gives a saved reply its own invented title, and it cannot post the Map as a reply on its own, because it answers the "we need to stop" message and posts the Map in the same turn.

So loading looks for any source containing the Map heading and a version line, and saving asks for the Map plus an `End of Map` marker, with as little around it as possible. The version line inside the Map is the only thing that identifies the newest copy.

## 24. The published brief is a trimmed edition, and the history starts at publication

The repo was made public on 2026-11-10 so that an assistant can read the playbook from a link (see decision 25 once the test is recorded).

Before that, three things were taken out of `docs/brief.md`: the table describing the real household the example case was drawn from, the build instructions with their private link and local folder name, and the byline. The table was the reason: it described one real household's setup in detail, and a public repo is no place for that. The full original is kept outside version control.

The commit history before publication held the untrimmed brief and links to private working sessions, so the public history begins with a single commit. This replaces decision 17.
