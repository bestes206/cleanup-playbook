# Pilot setup: the helper's guide

You are the helper: the person the couple calls when they get stuck. This page covers what to do before you send them the starter prompt, and how to be on call afterwards. Allow 30 minutes for the setup, most of it the smoke test.

Facts about ChatGPT here were checked against OpenAI's help pages on 2026-11-10. `docs/research.md` lists what could not be verified; the smoke test below is designed to settle the most important of those before the couple hits them.

## 1. Check their ChatGPT workspace

Do this with them on a short call, or have whichever partner is the workspace admin read the screens to you.

- [ ] **Both partners are members of the same shared project, each with Edit access or higher.** Chat-only access cannot add files, and saving the Map means adding a file. In the project, open the member list to check.
- [ ] **GPT-6 appears in the model picker** for both. If it doesn't, it hasn't reached their workspace; use the newest model offered at a medium thinking level and note it in the feedback log.
- [ ] **They know where the Chat / Work switch is** and that the pilot stays in Chat. Work isn't offered inside shared projects anyway, so if they see only Chat, that is fine.
- [ ] **One partner knows they are the workspace admin.** Later, the calendar connection may need "write actions" switched on in **Admin Console > Plugins**. Don't change it now; the shared calendar module asks for it when it is needed.

## 2. Put the playbook files in the project

The nine files in `playbook/` are the assistant's instructions. They go into the project's files (ChatGPT calls them **sources**).

- A project accepts ten files per upload, so all nine go in one go.
- Whoever uploads needs Edit access. If you are not a member of their workspace, send the files to the organizer and stay on the line while they upload from a computer: open the project, add files, select all nine.
- To send them as one attachment: `zip -j cleanup-playbook-files.zip playbook/*.md`
- Don't rename the files. The assistant finds them by name.
- When the playbook is updated, upload the new version of a file and remove the old one. Removing a source removes it for everyone in the project.

Optional, and recommended: in the project's **instructions**, paste this, so that a plain "let's pick up the cleanup" works in any new chat without the starter prompt:

```text
When anyone in this project mentions the cleanup, the playbook, or picking up where we left off: first read 00-start-here.md and 01-assistant-notes-chatgpt.md from this project's sources in full, then follow them. Never ask for or accept passwords, PINs, sign-in codes or card numbers in a chat.
```

## 3. Smoke test (10 to 15 minutes)

Run this before the couple's first session, ideally in a scratch shared project of your own with a second account, otherwise in theirs with the two of them. Use made-up answers. Each check settles something the research could not confirm.

**Already run once, on 2026-11-10:** checks 1 to 6, and check 7 from the *same* account, passed on the web in a single-person project (results in `docs/research.md` section 8). Check 8 passed the same day on the iPhone app, again in a single-person project, after three corrections to the notes: a project is found on the phone by searching its name (the side menu doesn't list projects), the thinking slider is behind a small gauge icon that appears when you tap the message box, and **Add to project sources** is under the three dots beneath the reply. Still to do: check 7 from a second account in a shared project.

Run check 7 as a round trip, on the devices each partner really uses. The partner at a computer starts, stops and saves. The partner on a phone opens a new chat, is shown where they left off, answers one question, stops and saves from the phone. The first partner then opens a new chat and should be told the Map is on version 2. The workspace admin does not need to be the one who uploads the files or starts; anyone with Edit access can.

If you test in a project of your own that isn't shared, pick **Project-only memory** when you create it, so it behaves like the couple's shared project. And look at the thinking level in the message box before the first message: a new project chat can start on Instant.

| # | Do this | You want to see | If not |
| --- | --- | --- | --- |
| 1 | Paste the starter prompt into a new chat in the project | It asks you to confirm project, Chat, GPT-6, Medium, and it says it has read the two files | If it can't find the files, check they are in the project's sources, not attached to another chat |
| 2 | Ask: "What is the first question in Part 1 of the intake file, word for word?" | A quote that matches `02-intake.md` | If it paraphrases or invents, the files are being skimmed rather than read. Log it; try asking it to open the file again |
| 3 | Answer a few interview questions | One question per message, plain words | Log as `assistant` |
| 4 | Type a fake password ("it's Sunshine123") | It does not repeat it, tells you to change it, moves on | Log as `assistant`; this is the rule that matters most |
| 5 | Say "we need to stop now" | It posts the Map in one reply (a sentence or two above it is normal), ends with "End of Map", points you to the **Add to project sources** button under the reply, and asks you to confirm the save | On the web that button is the folder icon in the row under the reply. On the iPhone app it is under the three dots at the end of that row |
| 6 | Press the button, then open the project's **Sources** tab | A green "Added to project sources" notice on the web (on the phone, the three-dots menu changes to "Remove from project sources"), and a new entry at the top with today's date. Its title is invented by ChatGPT ("Setup Map Saved", for example), not "Our Setup Map" | Use the copy-and-upload fallback in the notes file |
| 7 | Start a new chat as the **other** account and type "let's pick up the cleanup" (or paste the starter prompt) | It finds the Map, names the version, and says where you left off | This is the single most important check. If it fails, continuity between partners is broken; fall back to pasting the Map in by hand and tell the couple that is the routine |
| 8 | On an iPhone, repeat checks 1, 5 and 7 | Same behaviour | The field operator will only ever use the phone |

Delete the test Map and test chats afterwards so the couple starts clean.

## 4. Send the starter prompt

Send the block from `starter-prompt.md` by text or email to both partners, with one line of your own: when they should do the first session (both together, about an hour, somewhere they can talk) and that they can stop partway.

## 5. On call

You are there for when they get stuck, not to do it for them. Think of yourself as a product person watching a first release.

- **Every reach-out goes in `feedback-log.md`.** It is feedback on the playbook, not a failure by them or by you.
- **Ask for the Map's "where we left off" line** before anything else. It tells you the file and step.
- **Prefer unblocking to taking over.** If you fix it for them, you lose the information about why the playbook failed there, and they lose the confidence.
- **The same rules bind you.** Never ask them to send you a password or a code either. If they need you to see a screen, a screenshot with nothing secret in it is enough.
- **Situations to treat as urgent:** someone locked out of email or their Apple Account; a security alert they didn't cause; a charge they didn't expect. Everything else can wait for a convenient time.
- **The Share icon.** On the phone, the icon beside the three dots under a reply offers a link anyone can open. Tell the couple once, in your own words, never to share the Map that way. If one of them thinks they copied or sent a link, log it and help them remove the link. ChatGPT has kept a list of shared links under Settings > Data controls; where that is today was not checked.
- **Calls to expect.** Three steps are flagged in the playbook as good moments to ring you: setting up the second sign-in step on an account both partners use; anything involving an "app password" for an older mail program; and signing up for the password app if it stalls on a phone (that sign-up is unconfirmed on iPhone; a computer is the safe route).
- **Don't expand the scope mid-pilot.** If they ask about inboxes, notifications or business software, make sure it is in the Map's parking lot and tell them it is next.

## 6. Wrap up

Run `debrief.md` when both have finished the first slice as that file defines it, or five weeks after their first session, whichever comes first. The fixes include deliberate waits (two weeks before the sticky notes are retired, a one-week check on the new habit), so three to five weeks of short sittings is normal.
