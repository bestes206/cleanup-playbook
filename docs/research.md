# Research notes

Researched on 2026-11-10 by four web-research passes, each told to open pages rather than trust search snippets. This file records what was found, where, and how sure we are. The playbook's facts trace back to here.

**How to read the tags**

- **Verified:** an official page from the vendor was opened and says this.
- **Secondary:** a non-official page was opened and says this.
- **Not verified:** could not be confirmed. The playbook either avoids depending on it or marks the step *(unconfirmed)*.

Sections 1 to 6 are desk research: no account was signed in to and no product was bought. Section 8 records one hands-on run of the playbook in ChatGPT on the web, done later the same day with the owner's approval. Section 7 lists what the pilot still needs to settle.

## 1. ChatGPT: modes, models, thinking levels

| Finding | Status | Source |
| --- | --- | --- |
| Chat and Work are separate modes. Chat is conversational; Work is an agent for longer multi-step tasks. Desktop app has a Chat/Work toggle; mobile has a dropdown at the top of the screen | Verified | help.openai.com/en/articles/20001275-chatgpt-work-and-codex |
| The exact label for switching modes on the web | Not verified | |
| The picker label is "GPT-6". "GPT-6 Sol powers GPT-6 at Instant through Extra High… it is shown as GPT-6, not Sol" | Verified | help.openai.com/en/articles/12003714-chatgpt-business-models-and-limits |
| Thinking levels on Business: Instant, Medium, High, Extra High, Pro. Web uses a thinking slider | Verified | same page; help.openai.com/en/articles/20001354-gpt-6-and-other-models-in-chatgpt |
| Pro uses a different underlying model and Business Standard gets 15 Pro messages a month | Verified | Business models page |
| GPT-6 replaced "Latest" in the menu on 2026-10-07; a workspace may not have it yet | Verified | help.openai.com/en/articles/6825453-chatgpt-release-notes; Business models page |
| Model picker is at the top of the conversation on iOS, in the composer on web | Verified, but the note predates GPT-6 | release notes, 2026-06-10 |
| On Business, a "Higher intelligence" setting lets Instant add reasoning on its own | Verified | Business models page |
| A separate "GPT-6 Sol" entry exists only in Work and Codex | Verified | Work and Codex page |
| Work is not available in projects that use project-only memory, which includes every shared project | Verified | help.openai.com/en/articles/10169521-projects-in-chatgpt |

**What this means for the playbook.** The brief's setup (shared Project, Chat, GPT-6, Medium; no Instant, Pro or Work) matches the current product. The starter prompt tells people to look for "GPT-6", never "Sol". Because Work isn't offered in shared projects, "stay in Chat" will usually be the only choice they see.

## 2. ChatGPT: shared Projects on Business

All from help.openai.com/en/articles/10169521-projects-in-chatgpt unless noted.

| Finding | Status |
| --- | --- |
| Roles: Chat access (use chats, files, instructions; cannot invite), Edit access (change instructions, add or remove files, invite), Owner | Verified |
| Limits on Business: 40 files per project, 10 files per upload, up to 100 collaborators | Verified |
| Every member sees the project's chats, files, instructions and member list | Verified |
| A member cannot post into another member's chat. "Chats in shared projects can be branched, not collaborated on synchronously" | Verified |
| Deleting a file removes it for everyone | Verified |
| Shared projects are forced to project-only memory: no outside memories, custom instructions or other chats | Verified |
| ChatGPT "may use context from other conversations in the same project"; there is no list of project memories | Verified. Completeness of recall is not promised |
| A message can be saved to the project with "Add to project sources" from the message menu; files can be uploaded | Verified |
| Where "Add to project sources" sits in the iPhone app | Not verified |
| ChatGPT can itself create or edit a file in the project's files | Not verified; no official page describes any way |
| Canvas is now "writing blocks", saved with the conversation, not the project | Verified (help.openai.com/en/articles/20001246) |
| A Page in Space can be created and edited by ChatGPT and co-edited by collaborators; web and desktop only, read-only on mobile | Verified (help.openai.com/en/articles/20001549) |
| A Page in Space can be opened from inside a Project chat | Not verified |
| Markdown files are a supported upload type | Verified (help.openai.com/en/articles/8555545-file-uploads-faq) |
| Scheduled tasks exist on Business (up to 10), but a task created in a project cannot read that project's files | Verified (help.openai.com/en/articles/10291617) |
| Voice works in Projects and can use connections; approvals are taps on screen, not spoken | Verified (Business release notes 2026-08-07; help.openai.com/en/articles/20001274) |

**What this means for the playbook.**

- **Each sitting is a new chat**, and continuity comes from a saved Map, because one partner cannot continue the other's chat and cross-chat recall is not guaranteed.
- **A person saves the Map**, using "Add to project sources", because no documented route lets ChatGPT write to project files. This is the least proven step in the whole design and is the first thing the smoke test checks.
- **Both partners need Edit access**, since saving means adding a file.
- **The playbook is nine files**, to fit one ten-file upload and leave most of the 40-file allowance for Map versions.
- A Page in Space and a Google Doc via the Drive connection were considered as a living Map and rejected for the pilot: Pages can't be edited on a phone, and both add a second product for non-technical users to set up. Worth revisiting if the manual save proves too fiddly.

## 3. ChatGPT: reading a linked repo

| Finding | Status | Source |
| --- | --- | --- |
| No official page describes how ChatGPT handles a pasted GitHub or raw link: whether it follows links between files, truncates, or reads only the README | Not verified | |
| ChatGPT's user-triggered fetcher may not apply robots.txt rules | Verified | developers.openai.com/api/docs/bots |
| GitHub's robots.txt names ChatGPT-User and disallows `/raw/`, `/tree/`, `/archive/`, `/commits/` paths; repo root and `/blob/` pages are not disallowed; raw.githubusercontent.com has no robots.txt | Verified | github.com/robots.txt, fetched 2026-11-10 |
| Community reports of refusals and partial reads | Secondary, dated 2023 to 2024 | community.openai.com thread 636506 |
| A GitHub connection exists, is read-only, targets repos you authorise, and "may support GitHub in deep research or agent mode but not in standard chat" | Verified | help.openai.com/en/articles/11145903 |

**What this means for the playbook.** The brief asked whether the starter prompt can stand alone or needs the repo, and to test whether ChatGPT reliably reads a linked repo. That test was not run: it needs a signed-in ChatGPT account and a published repo, and both require approval. On the evidence, a link is the less dependable route, so the pilot does not use one. The playbook files are uploaded to the project, the starter prompt points at them by name, and the safety rules are repeated inside the prompt so they hold even if a file fails to load. The starter prompt therefore needs the files but not a link.

## 4. Connections, by assistant

Yes means a first-party connection exists.

| Service | ChatGPT | Claude | Grok |
| --- | --- | --- | --- |
| Gmail | Yes. Can draft and send with confirmation; sending on web only | Yes. Official pages disagree on whether it can send (see below) | Yes. Read by default; writing needs extra permissions |
| Google Calendar | Yes. Can create and update events | Yes. Same disagreement on writing | Yes. Read by default; writing needs extra permissions |
| Google Drive | Yes | Yes | Yes |
| Outlook / Microsoft 365 | Yes, mail and calendar | Yes, including personal Outlook.com on individual plans | Yes; sign-in documented for work or school accounts only |
| iCloud mail and calendar | Yes, since 2026-10-27, using an Apple app-specific password | No connection. The iPhone app can read and create events in the phone's calendar | None |
| Yahoo Mail | None found | None | None |
| Several Google accounts at once | Yes, since 2026-08-28 (Settings > Plugins > Connect another account) | Officially silent; one secondary source says one at a time | Officially silent; one secondary source says one at a time |

Sources and status:

- **ChatGPT.** Verified: help.openai.com/en/articles/11487775 (Settings > Plugins), 10408842 (Google scopes), 11391654 (calendar actions, March 2026), 12512241 (Outlook), 20001494 (iCloud), 11509118 (admin controls), and the release notes for dates. The March 2026 note said write actions were off by default until a workspace admin enabled them; the current default is **not verified**. Calendar writes from the iPhone app are **not verified**. Adding a calendar event by voice is **not verified**. Whether the iCloud connection sees shared calendars is **not verified**.
- **Claude.** Verified: support.claude.com/en/articles/10166901 says Gmail can draft and send and Calendar can create, update and delete; claude.com/docs/connectors/google/gmail and /calendar say read-only. The two official sources conflict; treat write access as **not verified**. Microsoft 365: claude.com/docs/connectors/microsoft/365 and support.claude.com/en/articles/15183774 ("one Microsoft account at a time"). iOS app calendar access: support.claude.com/en/articles/11869619. Single Google account: secondary (dragapp.com, July 2026).
- **Grok.** Verified: docs.x.ai/grok/connectors and x.ai/news/grok-connectors (launched 2026-05-06). Write scopes "enabled progressively by your organization's administrators" (docs.x.ai/grok/connectors/gmail-google-calendar); whether an individual can enable them is **not verified**. Single Google account: secondary (usecarly.com, September 2026), a competitor's page with no evidence shown.

**What this means for the playbook.**

- The brief's claim that Yahoo and iCloud mail are poorly reachable is half out of date: ChatGPT now reaches iCloud; nothing reaches Yahoo.
- Google Calendar is still the only calendar all three assistants connect to through an ordinary sign-in screen, which is why the tools agreement recommends it as the home. With iCloud newly reachable from ChatGPT, the agreement presents iCloud as a workable choice for a ChatGPT-only household and says what it costs in portability.
- The brief's concern that several business Gmail inboxes would need consolidating no longer applies to ChatGPT, which connects several Google accounts at once. It may still apply to Claude and Grok.

## 5. Shared workspaces in the other assistants

For the playbook's "runs in any assistant" goal. Neither was piloted.

- **Claude.** Sharing a project needs a Team or Enterprise plan (verified: support.claude.com/en/articles/9519189, claude.com/pricing). Chats inside a shared project are private unless shared by hand (verified, same article), which is the opposite of ChatGPT. People upload project knowledge; nothing documents Claude writing to it (verified: support.claude.com/en/articles/9517075). Claude can read a public GitHub repo through its GitHub integration on all plans, though not in shared projects (verified: claude.com/docs/connectors/github). How memory behaves across members of a shared project is **not verified**.
- **Grok.** Projects or Workspaces group chats, files and instructions (secondary). Business plans let admins set project sharing (verified: docs.x.ai/grok/management). Who can edit, whether members see each other's chats, and whether Grok can write project files are **not verified**; no official consumer Projects page was found.

**What this means for the playbook.** The core files assume only that the assistant can read uploaded files and that a person can store a document where both partners see it. Everything else that is specific to one assistant lives in a single notes file (`playbook/01-assistant-notes-chatgpt.md`), so supporting another assistant means writing one more notes file and five setup lines.

## 6. Passwords, calendars and the iPhone

Current iOS: 27.2.1, released 2026-11-09 (verified: support.apple.com/en-us/100100).

**Password apps**

| Finding | Status | Source |
| --- | --- | --- |
| 1Password Families: $5.99 a month billed yearly, up to 5 people, 14-day trial without a card. A first-year promotional price also shows | Verified | 1password.com/pricing/password-manager |
| Each person gets a Private and a Shared vault, their own account, Secret Key and Emergency Kit | Verified | support.1password.com/explore/families, /get-started-families |
| An organizer can recover another member's account but not their own; nobody can reset a forgotten account password | Verified | support.1password.com/recovery, /forgot-account-password |
| Paths for inviting people, saving the Emergency Kit, and adding a Windows device | Verified | support.1password.com/add-remove-family-members, /emergency-kit, /add-account |
| The button label for making someone a family organizer | Not verified | |
| Whether the whole Families sign-up works in Safari on an iPhone | Not verified | |
| Import from Apple's Passwords app on iOS 26 and later | Verified that it exists; exact wording not verified | support.1password.com/import |
| Bitwarden: free two-person organization with two collections; Families $47.88 a year for six | Verified | bitwarden.com/pricing, bitwarden.com/help/about-organizations |
| Bitwarden has no master-password reset; emergency access needs a paid plan | Verified | bitwarden.com/help/forgot-master-password, /emergency-access |
| A malicious copy of Bitwarden's command-line package was published on 2026-04-22; Bitwarden reported no evidence vault data was affected | Verified | community.bitwarden.com statement, 2026-04-23 |
| Apple Passwords: shared groups are created on an Apple device; on Windows it needs iCloud for Windows, a browser add-on, and either Advanced Data Protection or an Apple device nearby | Verified | support.apple.com/guide/iphone/iphe6b2b7043, support.apple.com/guide/icloud-windows/icw2babf5e03 |
| Whether one Windows PC can serve two Apple Accounts' passwords | Not verified | |
| iPhone autofill: Settings > General > AutoFill & Passwords; up to three password apps | Verified | support.apple.com/guide/iphone/iphf9219d8c9 |
| No confirmed breach of 1Password or Apple Passwords in 2025 to 2026 was found | Secondary | news coverage |

**Account protection**

| Finding | Status | Source |
| --- | --- | --- |
| Google: Google Account > Security & sign-in > Turn on 2-Step Verification | Verified | support.google.com/accounts/answer/185839 |
| Yahoo: Account Security > 2-step verification | Verified | help.yahoo.com/kb/SLN5013.html |
| Microsoft: account.microsoft.com/security > Manage how I sign in > Additional security | Verified | support.microsoft.com (two-step verification article) |
| Apple: Settings > name > Sign-In & Security, for Two-Factor Authentication, Recovery Contacts, and the list of addresses on the account | Verified | support.apple.com/en-us/102641, /102529, iPhone guide |
| An Apple Recovery Key, if set and lost, locks the account permanently | Verified | support.apple.com/en-us/109345 |
| Have I Been Pwned's email search is free; the site also has a password-search box and carries adverts | Verified | haveibeenpwned.com |
| Email first, then other important accounts, when replacing a reused password | Verified | ncsc.gov.uk guidance |
| Putting the mobile carrier and Apple Account next in line | Our judgment, not from a source | |
| The exact password-change menu labels for Google, Yahoo and Microsoft | Not verified | |
| Where iOS 27 shows a mail account that needs signing in again | Not verified | |

**Calendars**

| Finding | Status | Source |
| --- | --- | --- |
| Add a Google account for calendars: Settings > Apps > Calendar > Calendar Accounts > Add Account > Google | Verified | Apple iPhone guide, iphc37be2016 |
| A new Google calendar can only be created in a web browser | Verified | support.google.com/calendar/answer/37095 |
| Sharing, the permission labels, and accepting by email link | Verified | support.google.com/calendar/answer/37082, /15716974 |
| Only "My calendars" sync to Apple Calendar automatically; others are ticked at calendar.google.com/calendar/syncselect | Verified | support.google.com/calendar/answer/99358 |
| That a calendar shared by a partner needs that tick | Inferred from Google's rule; the module treats it as a fix-up to try only if the calendars don't appear | |
| A subscription added to iCloud on the phone is not visible at calendar.google.com or to an assistant's Google Calendar connection | Follows from where it is stored; not tested | |
| Google "From URL" calendars are added on the web only and can take up to about a day to refresh | Verified (web only); secondary (refresh time) | support.google.com/calendar/answer/37100 |
| Each Google account keeps its own notification settings for a shared calendar, so one partner's event may not alert the other | Raised in review; not verified | |
| Older mail programs may need an "app password" once the second sign-in step is on | Raised in review; not verified for current Yahoo and Microsoft | |
| Whether the sync page works in an iPhone browser | Not verified | |
| Subscribed calendars are read-only; adding one to iCloud shows it on all that person's devices | Verified | support.apple.com/en-us/102301 |
| How often a subscribed calendar refreshes | Not verified; secondary sources say hours | |
| Any indicator that a subscription is dead | None found | |
| Whether the (i) screen shows a subscription's address | Not verified | |
| Hide: untick in Calendars. Unsubscribe and Delete Calendar under (i) | Verified | support.apple.com/en-us/102180, iPhone guide |
| Deleting an iCloud calendar deletes its events on every device; icloud.com can restore an earlier snapshot, which resets sharing | Verified | support.apple.com/guide/icloud (delete a calendar; restore calendars) |
| Exporting an iCloud calendar without a Mac means making it public and editing the link | Verified | support.apple.com/en-us/108306 |
| Moving an event: open it and change its Calendar line. No bulk move on iPhone | Verified / none found | iPhone guide |
| Default Calendar and Default Alert Times under Settings > Apps > Calendar | Verified | iPhone guide, iphc37be2016 |
| Siri adds to the default calendar; naming a calendar is unreliable | Secondary | forum reports |
| Typing a plain-language description into a new event fills in the details | Verified | iPhone guide, iph3d110f84 |
| Touching an underlined date in Messages to create an event | Secondary; Apple does not document it | |
| Apple Reminders cannot use a Google account | Verified | iPhone guide, iph8739025dd |

## 7. What the pilot has to settle

In priority order. The smoke test in `helper/pilot-setup.md` covers the first five before the couple starts.

0. **The linked-repo question from the brief is still open.** The brief asks for the helper to send a prompt that links to a repo, and for a test of whether ChatGPT reliably reads one. That test needs a signed-in ChatGPT account and a public repo, both of which require approval, so it was not run, and the pilot uploads files instead. This is the one place the delivery differs from the brief.
1. **Does ChatGPT read the nine uploaded files in full and follow them**, or does it skim? Passed on the web (section 8); a longer session is still untested.
2. **Does "Add to project sources" exist on the phone**, and does the saved Map show up there? Confirmed on the web only (section 8). (Check 8.)
3. **Does a new chat, started by the other partner in a shared project, find and resume from the saved Map?** Passed from the same account in a single-person project (section 8); the two-person case is untested. (Check 7.)
4. **Does it hold the no-passwords rule and one-question-at-a-time** over a long session? Held over a short one (section 8).
5. **Is GPT-6 in the couple's picker**, with Medium offered? It is on the account used in section 8; theirs is unchecked.
6. **Can the Google Calendar connection add events in their workspace**, from the phone, by voice?
7. **Does a calendar shared between two Google accounts appear in Apple Calendar** without the sync-page step, or only with it? Can that step be done on a phone?
8. **Can the 1Password Families sign-up be completed on an iPhone alone?**
9. **Do alerts reach the partner who didn't create the event?** (Fix 3, step 3.4.)
10. **Can the thinking level be changed partway through a chat**, for the tools agreement?
11. **How visible followed schedules are to the assistant**, with and without the optional step 4.4 in Fix 2.
12. **The unconfirmed button labels**, each marked *(unconfirmed)* in the modules.

## 8. Hands-on run, 2026-11-10

One run of the smoke test in ChatGPT on the web (Chrome), in the repo owner's own account, with invented answers. Two single-person scratch projects were used, both created with project-only memory to mimic a shared project. Not covered: the iPhone app, a second account, a shared project, or a Business workspace's admin settings.

**What the screens actually look like**

- The home screen has a **Chat / Work** toggle at the top. Inside a project created with project-only memory there is no such toggle. The project-creation dialog says of that mode: "Work in the cloud isn't available for this type of project."
- The message box shows only the thinking level, as a word at its right-hand end. Clicking it opens a five-stop **Thinking effort** slider (Instant, Medium, then three more). Clicking the level's name above the slider opens the model list, which offered **GPT-6** (ticked) and **GPT-5.6 Sol**.
- A brand-new project's first chat was set to **Instant**. After Medium was chosen once, later chats and a second new project started on Medium.
- **Add to project sources** is a button in the icon row under every assistant reply (a folder icon), not inside a menu. Pressing it shows a green "Added to project sources" notice.
- The saved reply appears at the top of the project's **Sources** tab with the date and a title ChatGPT invents ("Setup Map and Security Notes", "Setup Map Saved"). The title never matched the Map's own heading.
- A new project can be given project-only memory from a dropdown in the creation dialog.

**How ChatGPT (GPT-6, Medium) behaved**

| Check | Result |
| --- | --- |
| Reads the files and follows them | Pass. Its first reply named `00-start-here.md`, `01-assistant-notes-chatgpt.md` and `04-map-and-checklist.md`, reported that no Map was saved, and asked for the three setup confirmations |
| Quotes the first intake question word for word | Pass. Exact match with `02-intake.md` |
| One question at a time | Pass over five turns. It alternated between the two partners by name |
| A fake password typed into the chat | Pass. It did not repeat it, said to treat it as exposed, promised to keep it out of the Map, and carried on. The Map it later produced recorded that a password had been disclosed, without the password |
| Stops and saves | Partly. It produced a complete Map in the right format, version line included, and gave resume instructions. But it wrapped the Map in a reply with several sentences above and below it, and in the first run it did not wait for confirmation that the save had worked |
| Resume in a new chat (first run) | Partly. It found "a record of an earlier session" and summarised the right place, but did not recognise the source as the saved Map, because the instructions told it to look for a file *starting* with the Map's heading. It asked the user whether the Map had been saved |
| Refuses to continue the interview with one partner | Pass |

**What was changed as a result, and the re-test**

- Loading now looks for a source that *contains* the Map heading and a version line, and ignores the source's title.
- Saving now accepts that the Map arrives in one reply with a sentence or two around it (the assistant answers the "we need to stop" message and posts the Map in the same turn, so a Map-only reply is not realistic), asks for an `End of Map` line, and requires confirmation in the same sitting.
- The notes file and the starter prompt's setup lines were corrected to match the screens above.

Re-test in a second scratch project with the updated files: the save reply ended with "End of Map" and "I won't consider the Map saved until you confirm"; a new chat then opened with "found your saved Our Setup Map, Version 1, dated November 10, 2026" and resumed at the correct question. It still put four short sentences above the Map, more than the two asked for; harmless now that loading is tolerant.

The two scratch projects used for the run were deleted afterwards at the owner's request, along with their chats and uploaded files.


**iPhone app, first look (one screenshot from the owner's phone, 2026-11-10)**

- The home screen has a two-part **Chat / Work** switch at the top, the same as the web. The earlier note that it is a dropdown on the phone was wrong.
- The thinking picker is the same five-stop slider, with the level's name above it. It was sitting on **High**, the third stop, not Medium, so the setup check matters on the phone as well.
- Not yet seen on the phone: what a chat inside a project looks like, where to tap to open the slider, where the model list is, and where **Add to project sources** is.
- A second screenshot showed the **Work** tab's settings on the phone: a sheet titled **Configure** with three rows, Model (showing "6.1 Sol"), Effort (showing "Max") and Speed (showing "Standard"), plus "Reset to default". This is a different control from Chat's slider, with different level names, which gives the assistant a way to tell that a user has ended up on Work.
- The iPhone app's side menu has **no Projects list**. It shows Meet dot, Scheduled, Space, Customize, Codex and Explore, then recent chats and "See all...". A project created on the web minutes earlier was found by tapping the magnifier and typing its name; it appears in the results labelled "Project". Whether Space or "See all..." also lead to projects was not checked.
- The project's own page on the phone shows a back arrow, the project's name, a "..." menu, **Chats** and **Sources** tabs, and a message box. There is no Chat / Work switch there, and no thinking level on show. Tapping the message box reveals a small gauge-shaped icon; tapping that opens the slider (reported by the owner, who set it to Medium this way).
- Starter prompt and stop-and-save on the phone: the assistant confirmed the setup, and on "We need to stop now" produced a Map with the right heading and version line. Two flaws. It shortened the checklist's part titles ("Part 1. Set up together" for "Set up the password app together"), so the format rules now say to copy them word for word. And the app draws `[ ]` as an empty circle, inconsistently mixed with bullets, which is cosmetic.
- Saving on the phone: under the reply is a row of four small icons (copy, rate, share, three dots). The three dots open a menu with "Branch in new chat", "Read Aloud" and **Add to project sources**. After saving, the same menu reads **Remove from project sources**, which is the clearest confirmation on the phone. The assistant's own instruction ("press and hold this reply") came from the notes file and sent the user to the wrong place; the notes are corrected. Whether press-and-hold shows the same menu was not checked.
- Resume on the phone: a new chat in the project, with the starter prompt pasted again, opened with "found your saved Map in the project sources", named Version 1 and its date, said the interview was next, and re-asked the setup check. Pass. With this, every single-person check has passed on both the web and the iPhone app. What remains untested is a second account in a shared project.
- The starter prompt's setup lines now say how to find the project and the thinking level on a phone.
- A privacy trap on the phone: in the row of icons under a reply, the one beside the three dots is **Share**. It opens a sheet headed "Share a better-formatted response. Anyone with the link can view this message", with Copy link, WhatsApp, Messages, X and More. The owner opened it by accident more than once while reaching for the three dots. A Map holds email addresses, so the notes now warn against it. Not checked: whether a link exists before Copy link is tapped, and whether a Business workspace can switch public links off.
- The scratch project used for the phone run was deleted afterwards at the owner's request, with its two chats and uploaded files.
