# Assistant notes: ChatGPT (Business, shared Project)

**For the assistant.** The rest of the playbook is written for any assistant. This file holds everything specific to running it in ChatGPT inside a shared Project on a Business workspace. Where another file says "see the assistant notes", it means this file.

Last checked against OpenAI's help pages, and by a hands-on run on the web in a single-person project: 2026-11-10. Lines marked *(unconfirmed)* could not be verified; the iPhone app was checked the same day in a single-person project; a two-person shared project has not been tested. If what the user sees differs, the screen wins.

## The right setup, checked at the start of every chat

You cannot see which mode or model you are running in, so ask. At the start of each chat, before anything else, have the person confirm three things:

1. They are inside the **shared project**, not a loose chat. The project's name shows above the chat. On the iPhone app the side menu does not list projects: they tap the magnifier at the top of the menu, type the project's name, and tap the result labelled **Project**.
2. If there is a switch at the top that says **Chat** and **Work**, it is on **Chat**. Inside a project there is often no such switch at all, because Work isn't offered there; no switch is fine. (On the web the switch is a Chat / Work toggle at the top of the home screen. On the iPhone app it is the same two-part Chat / Work switch at the top of the home screen. Inside a project on the phone there is no switch.) A sign they are on Work by mistake: the settings sheet is titled **Configure** and lists Model, Effort and Speed. Chat has only the slider. If they describe that sheet, ask them to tap **Chat** at the top and start again from step 1.
3. The thinking level is **Medium** and the model is **GPT-6**. On the web, the message box shows only the thinking level, as a word at its right-hand end. A new project chat may start on **Instant**, so this is worth a real look. To change it they click that word and drag the slider to the second of its five stops, **Medium**. To see the model, they click the level's name above the slider; a short list opens, and **GPT-6** should have the tick. On the iPhone app the slider is the same: five stops, with the level's name shown above it. It can be sitting on a level left over from an earlier chat, such as High, so they check it on the phone too. On the phone the level is not shown until they tap the message box; a small icon like a gauge then appears in it, and tapping that opens the slider. *(Where the model list is on the phone: unconfirmed.)*

If the first is off, they need to open the project, start a new chat there, and paste the starter message again; a chat started outside the project cannot see the playbook files. If the second or third is off, ask them to change it with the same switch or picker and carry on.

The thinking levels they will see are Instant, Medium, High, Extra High and Pro. Medium is the one to use. **High** is allowed for one case only: the tools agreement, if the side-by-side comparison feels thin. Either of you can call it: they may ask for more depth, or you may say that a decision deserves a closer look and suggest it. To switch, they open the same picker where they chose Medium, pick High, and after the agreement is recorded they set it back to Medium. *(Changing the level partway through a chat is unconfirmed. If the picker won't allow it, they start a new chat on High, paste the starter message, and you resume the agreement from the saved Map.)* Not Instant (it skips the careful reasoning the step-by-step work needs), not Pro (a small monthly allowance, and slow), and not Work (it is built for long solo tasks rather than a back-and-forth conversation, and it is not offered inside shared projects).

If **GPT-6 is not in their model list**, it may not have reached their workspace yet. Tell them to pick the newest model offered at a medium thinking level, carry on, and mention it to their helper.

## How a shared project behaves

- Both partners see the project's files, its instructions, and every chat in it, including each other's. Say this once in the first session, so neither is surprised and both understand why nothing secret goes in a chat.
- One partner cannot type into the other's chat. They can open it and read it, or branch it into a copy of their own. So **each sitting is a new chat**, and continuity comes from the saved Map, not from the old chat.
- A shared project uses project-only memory. You do not carry memories in from their other chats, and what you may recall from other chats in this project is not guaranteed to be complete. Treat the saved Map as the only record you trust. If something you seem to remember conflicts with the Map, ask.
- The project holds up to 40 files. The playbook uses nine. Saved Maps use the rest, so old versions need clearing out now and then (see below).

## Where the Map lives

In the project's files (the project calls them **sources**), as a saved copy of a message you wrote.

### To load it

1. Look in the project's sources for a saved Map: any source whose text contains the heading `Our Setup Map` followed by a `Version:` line. Do not go by the source's name. A Map saved from a chat is listed under a title ChatGPT invents (for example "Setup Map and Security Notes") with the date it was saved, and it may have a sentence or two before or after the Map itself. Ignore anything outside the Map and read the Map.
2. If there are several, use the one with the highest `Version` number. If two share the highest number, the partners each did a sitting from the same starting point. Read both, combine them using their Change logs and Checklists (keep every `[x]` and every Change log line from either), tell the person you have merged two versions, and save the result under the next number up.
3. Tell the person which one you are using ("I'm working from version 6, saved on the 18th by Riley") and ask whether that sounds like the latest. If one of them did a sitting and it was never saved, the Map will be behind, and they will know.
4. If you find no Map in the sources, ask whether they have done the first session. If they have, the save didn't stick: ask them to open the most recent cleanup chat in the project, copy the last Map from it, and paste it here.

### To save it

You cannot write into the project's files yourself *(unconfirmed, but no official page describes a way)*. The person saves it, in three taps:

1. Post one reply that contains the whole Map, with the `# Our Setup Map` heading and the new version number on the line under it. Whatever else is in that reply gets saved along with the Map, so keep it to the minimum: at most two short sentences above the Map (for instance, that this is a good place to stop and nothing was changed), then the Map, then a line reading `End of Map`, then the save instructions from step 2. Put nothing sensitive in those extra sentences either.
2. Ask them to press the **Add to project sources** button under that reply. On a computer it is one of the small icons in the row beneath the reply (a folder), and a green notice saying "Added to project sources" appears at the top. On the iPhone app, scroll to the very end of the reply, tap the three dots (**...**) at the right-hand end of the row of small icons under it, and tap **Add to project sources** in the menu. Don't tell them to press and hold the reply; that is not where it is. Warn them about the icon next to the three dots, an arrow coming out of a box: that one is **Share**, and it offers a link that anyone can open. The Map must never be shared that way. If a sheet titled "Share" opens, they swipe it down to close it without tapping **Copy link** or any app.
3. Ask them whether they saw the green notice, or to open the project's **Sources** tab and tell you whether a new entry with today's date is at the top. On the phone the surest check is to tap the three dots again: once the reply is saved, the menu reads **Remove from project sources**. They close the menu without tapping that line, because tapping it takes the Map back out. Wait for their answer in this sitting; don't leave it for next time.

If they can't find **Add to project sources**:

- **Second choice:** have them copy the message, paste it into a note or document, save it with the name `our-setup-map-vN`, and upload it to the project with the project's add-files button.
- **Last resort:** leave it. The Map is still in this chat, and both partners can open this chat from the project. Tell them the name of this chat, add "Map not saved to sources" to *Questions for the helper*, and carry on. Next time, they paste it from here.

Never tell them the Map is saved until they have confirmed they can see it listed.

### Old versions

Each save adds a file. When more than five Map versions are in the sources, suggest removing the oldest ones and keeping the latest two. This is a removal, so the usual rule applies: confirm the latest version opens and reads correctly first, and get a yes. Removing a source removes it for both partners.

## Connections (ChatGPT calls them plugins or apps)

Found under **Settings > Plugins** (older versions of the app say **Apps**). Each partner connects their own accounts; one partner's connections are not shared with the other.

What exists today, for the tools agreement and the modules:

| Service | Connection | Can it make changes? | Notes |
| --- | --- | --- | --- |
| Gmail | Yes | Can draft and send, with a confirmation each time; sending is on the web only | Several Google accounts can be connected at once: Settings > Plugins > Gmail > **Connect another account** |
| Google Calendar | Yes | Can create and change events | Several accounts at once. On Business, the workspace admin may have to switch on "write actions" first (Admin Console > Plugins). Whether adding events works from the iPhone app is *unconfirmed* |
| Google Drive | Yes | Can create and edit Docs and Sheets | On by default on Business. Not used by this playbook |
| Outlook mail and calendar | Yes | Mail: draft and send. Calendar: changes documented for shared calendars | A company-run Microsoft account may need its IT admin's approval, and rule 9 in `00-start-here.md` applies |
| iCloud mail and calendar | Yes, since late October 2026 | Can update calendar events | Signs in with a special one-off password created on Apple's website, typed into ChatGPT's settings screen. Never into a chat |
| Yahoo Mail | None found | | Mail in Yahoo stays out of reach unless it is brought into another account |

How to guide a connection: the person opens Settings > Plugins themselves, picks the service, and signs in on the provider's own screen. You never see the password. Afterwards, test it with a harmless read ("what's on my calendar tomorrow?") and compare with their phone.

When you use a connection inside the project, ChatGPT may ask the person for permission to look outside the project. That is expected; tell them so.

## Voice

Voice works inside projects and can use connections, but anything that changes something (like adding a calendar event) needs a tap on the screen to approve; saying "yes" out loud is not enough. Adding a Google Calendar event by voice is plausible but *unconfirmed*; `12-module-commitment-capture.md` treats it as something to try, not something to rely on.

## Things this assistant cannot do here

- Set reminders or scheduled check-ins that read the project's files. Scheduled tasks exist, but a task cannot open project files, so it cannot load the Map. For the monthly checkup, a repeating event on their own shared calendar is the reliable prompt.
- See its own model or mode. Always ask.
- Open the other partner's connections.
