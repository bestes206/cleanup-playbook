# The Map and the Checklist

**For the assistant.** The Map is one document that holds everything the cleanup knows about this household: who uses what, what bugs them, what they agreed, what is done, and where they stopped. The Checklist is a section inside it. Keeping both in one document means there is one thing to save and one thing to load.

The Map does three jobs:

1. **Resume.** Either partner can open a new chat and carry on from where the other stopped.
2. **Clarity.** It is the one page showing every account, device and calendar, so nobody has to carry it in their head.
3. **Handover.** A later assistant or agent can start from it instead of asking everything again. Keep it tidy and literal for that reason.

## What never goes in the Map

The Map sits in a shared space and may be read by other tools later. Leave out anything that would hurt them if it leaked:

- Passwords, PINs, device passcodes, hints, or anything like "the usual one"
- Sign-in codes, backup codes, recovery keys, the password app's secret key
- Answers to security questions
- Card, bank, tax or ID numbers, in full or in part
- Where the printed emergency sheet is kept (record only that it exists and both know where)
- Home address, dates of birth, children's surnames or schools
- Names or details of clients, tenants or customers
- Links to calendars or schedules they follow (some are private to the family; if they want one kept, it goes in the password app)
- The content of any email or message

What does belong: email addresses (they are how accounts are told apart), short nicknames for accounts, which provider, who uses it, yes/no facts about how it is protected, and the names of calendars. First names or initials for people, whichever they prefer.

Before every save, read the Map through once against this list. If something slipped in, take it out and tell them you did.

## Format rules

- Plain Markdown, short lines, one fact per line. It has to be readable on a phone, so use lists rather than wide tables.
- Unknowns are written `not sure yet`. Never guess and never leave a line out because the answer is unknown; the gap is information.
- Every account and calendar gets a short nickname the couple would recognise. Use the nickname in conversation.
- Dates as `2026-11-18`.
- The first three lines are always the title, the version line and a blank line, so the newest copy is easy to spot.
- Copy the section headings and the Checklist lines from the template word for word. Don't shorten or reword a part's title; later chats match on them.

## Checklist marks

| Mark | Meaning |
| --- | --- |
| `[ ]` | Not started |
| `[~]` | Started, not finished. Add where it stopped |
| `[x]` | Done. Add the date and who |
| `[!]` | Stuck. Add one line on what happened; also add it under *Questions for the helper* |
| `[-]` | Skipped on purpose. Add why |

On a phone, the app may show `[ ]` as an empty circle and `[x]` as a ticked one; the other marks show as typed. That is only how the screen draws them. If the couple ask, say so.

Only mark `[x]` when the person has confirmed the "Done when" check for that part, not when the steps were read out.

## Saving

Save at the end of every sitting, at every safe stopping point where they pause, and straight after the interview and the agreement.

1. Update *Where we left off*: the file, part and step to do next, who it needs, and how long it takes.
2. Update the Checklist marks and add a line to the Change log.
3. Raise the version number by one, and set the date and who was present.
4. Check the Map against the never-include list above.
5. Post the whole Map as a reply that begins with the Map's title line. You send one reply at a time and the whole reply is what gets saved, so put nothing above the Map and at most the short save instructions below it.
6. Walk them through storing it, using the steps in the assistant notes file.
7. Have them confirm it is stored. Then tell them, in one sentence, how to pick up next time: start a new chat in the project and paste the starter message again.

Always post the whole Map, never just the changed part. A partial Map saved over a full one loses everything else.

## Loading

At the start of each chat, find the newest Map using the steps in the assistant notes file, say which version and date you are working from, and ask if that sounds right. If the person says something has changed since, update the Map first. If two saved Maps carry the same version number, the partners each did a sitting from the same starting point: merge them as the assistant notes file describes, and save the result as the next version.

## The blank Map

Copy this to start a new Map. Lines in angle brackets are placeholders to replace. Repeat the account and calendar blocks as many times as needed.

```markdown
# Our Setup Map
Version: 1 · Saved: <date> · Present: <who>

## Where we left off
- Next: <file, part and step>
- Needs: <one partner by name, or both> · About <minutes> minutes
- Note: <anything the next sitting should know>

## Checklist

### Joint session (both)
- [ ] Interview done and Map saved
- [ ] Tools agreement: every decision agreed by both

### Fix 1: Password app
- [ ] Part 1. Set up the password app together
- [ ] Part 2. The way back in: emergency sheets and recovery
- [ ] Part 3. On each phone, tablet and computer (<name>)
- [ ] Part 3. On each phone, tablet and computer (<name>)
- [ ] Part 4. Lock down the email accounts first
- [ ] Part 5. Lock down the Apple Accounts
- [ ] Part 6. Replace the old shared password everywhere else
- [ ] Part 7. Retire the sticky notes

### Fix 2: Shared calendars
- [ ] Part 1. See what we have
- [ ] Part 2. Create the Family and Business calendars and share them
- [ ] Part 3. Show them on every device (<name>)
- [ ] Part 3. Show them on every device (<name>)
- [ ] Part 4. Bring in the schedules we follow
- [ ] Part 5. Move upcoming events across
- [ ] Part 6. Tidy the old calendars
- [ ] Part 7. Let the assistant see the calendars

### Fix 3: Capturing promises
- [ ] Part 1. Point the phone at the shared calendar (<name>)
- [ ] Part 1. Point the phone at the shared calendar (<name>)
- [ ] Part 2. Pick a capture move and practise it (<name>)
- [ ] Part 2. Pick a capture move and practise it (<name>)
- [ ] Part 3. Agree the house rule
- [ ] Part 4. The look-ahead
- [ ] Part 5. One-week check

### Monthly checkup
- [ ] Repeating reminder is on the shared calendar
- Last checkup: <date or "none yet">

## What bugs us most
1. <pain, in their words> (<who said it>)
2. <pain>
3. <pain>
- Also mentioned: <others>

## People and devices
### <name>
- Uses most: <device>
- Also uses: <devices>
- Shared with anyone: <no / who>

### <name>
- Uses most: <device>
- Also uses: <devices>
- Shared with anyone: <no / who>

## Email accounts
### <nickname>
- Address: <address>
- Provider: <Gmail / Yahoo / Outlook / iCloud / other>
- Used by: <name / both>
- For: <business / personal / mixed>
- Owner: <a person / the business / an employer or brokerage>
- Managed by someone else: <no / yes, by whom>
- Read in: <app and device>
- Mail forwarded into it from: <none / which>
- Recovery phone and backup address are current: <yes / no / not sure yet>
- Second sign-in step: <on / off / not sure yet>
- In the password app: <yes / no>
- Has its own password (not the old shared one): <yes / no / not sure yet>
- Checked for leaks: <date and "nothing found" or "found, password changed" / not yet>

## Apple and Google accounts
- <name>'s Apple Account: <address> · second sign-in step: <on / off / not sure yet> · recovery contact: <set / not set>
- <name>'s Apple Account: <address> · second sign-in step: <on / off / not sure yet> · recovery contact: <set / not set>
- Apple Account shared on any device: <no / which>
- Family Sharing: <on / off / not sure yet>
- <name>'s main Google account: <address or "none">
- <name>'s main Google account: <address or "none">
- Password-reset emails usually go to: <nickname / varies / not sure yet>

## Calendars
### <calendar name>
- Lives in: <iCloud / Google (which account) / a schedule we follow / on this phone only>
- Seen by: <name / both>
- Can be changed by: <name / both / nobody, it is published by someone else>
- For: <family / business / kids' activity / other>
- Status: <keep / hidden since date / removed on date, backup saved / not sure yet>

- Work appointments and client meetings go: <where>
- Others who need to see or add: <none / who>

## Promises and to-dos
- <name> captures promises by: <how, or "nothing yet">
- <name> captures promises by: <how, or "nothing yet">
- One acts as the other's reminder: <no / who for whom>
- To-do lists in use: <apps or paper>
- Agreed house rule: <text, once agreed>
- Paper notes get entered: <when, or "no paper notes">
- Reminder experiment: <not started / runs until date / kept / changed / ended>

## Passwords
- Kept today in: <places only: memory, paper, notes app, phone>
- One password reused widely: <yes / no> · known to both: <yes / no>
- Lockouts: <roughly how often>
- Password app: <which, or "none yet"> · set up: <date>
- Plan: <paid since date / free / trial ends on date>
- Emergency sheet printed and stored offline: <name: yes/no> · <name: yes/no>
- Both know where the sheets are: <yes / no>
- Reused or weak passwords left (count from the app's check): <number, date>
- Sticky notes: <still in use / in an envelope since date / shredded on date>

## Our agreement
Agreed on <date> by <name> and <name>.
- Calendar home: <choice> · why: <one line>
- Family calendar owned by: <account nickname> · Business calendar owned by: <account nickname>
- Password app: <choice and plan> · cost: <amount per year> · paid by: <who>
- Shared box holds: <kinds of accounts> · private boxes hold: <kinds of accounts>
- Promises with a time go: <where> · to-dos with no time go: <where>
- The assistant may be connected to: <list> · not to: <list>
- Accounts on hold until rules are checked: <nickname: who asks whom, by when / none>
- Reopened decisions: <none / what and when>

## The assistant
- Connected so far: <name: what> · <name: what>
- May add calendar events when asked: <name: yes/no> · <name: yes/no>
- Cannot see: <for example: schedules we follow on the phones, old iCloud calendars, mail>
- What we want it to be able to answer:
  - "<example question>" (<who asked>)
  - "<example question>"
  - "<example question>"

## Not sure yet
- <item>: matters when <which module or step>

## Parking lot (no fix yet)
- Too many inboxes: <one line or "fine">
- Notifications: <one line or "fine">
- Messages or photos not matching between devices: <one line or "fine">
- Business software: <one line or "none">
- Other: <one line>

## Questions for the helper
- <date> <question or stuck step, with file and step>

## Change log
- <date> <who>: <what was done or changed, one line>
```

## Notes on a few sections

- **Change log** is the undo trail. Every removal gets a line saying what was removed, when, and where its backup is ("2026-12-02 Riley: removed calendar 'Soccer 2024'; exported copy saved to the family Google Drive").
- **Our agreement** is the plan the modules follow. Change it only in a conversation with both partners, and record the change under *Reopened decisions*.
- **What we want it to be able to answer** is the test for the end of the pilot. Keep their exact wording.
- **Checklist lines with a name** exist because some parts are done once per person. Add or remove lines to match the household.
