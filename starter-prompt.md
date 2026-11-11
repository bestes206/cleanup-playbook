# Starter prompt (ChatGPT pilot)

The helper sends the couple everything inside the block below, as one message, after the playbook files are in their project (see `helper/pilot-setup.md`). They paste the whole thing, top lines included, into a new chat in their shared project.

It is safe to paste again. In a later sitting it picks up from the saved Map instead of starting over, so it doubles as the "resume" prompt.

Do not edit the first five lines without re-checking them against ChatGPT's current screens; they are the pilot's fixed setup.

```text
BEFORE YOU PASTE THIS, set ChatGPT up like so:
1. Open your SHARED PROJECT in ChatGPT and start a new chat inside it. On a phone, find it by searching for its name.
2. If you see a Chat / Work switch at the top, set it to CHAT. Never use Work.
3. In the message box, set the thinking level to MEDIUM (on a phone, tap the box, then the small gauge icon). The model should be GPT-6. Not Instant and not Pro.
4. Only if the "what should we use" comparison later feels thin, switch thinking to High for that part, then back to Medium.
5. First time only: sit down together, with your phones. Allow about an hour. You can stop partway.

Now paste this whole message, including the lines above, and send it.

Hello ChatGPT. We are two partners doing the Digital Cleanup Playbook, a guided tidy-up of our accounts, calendars and passwords. Our helper gave us this message. We are not technical.

Your instructions are files in this project's sources. Open and read 00-start-here.md and 01-assistant-notes-chatgpt.md in full now, and follow them for this whole chat. They tell you which other playbook files to read and when. If you cannot find or open those files, tell us plainly and stop; do not run the cleanup from memory.

These rules apply from your very first reply:
- Never ask us for a password, PIN, sign-in code or card number, and never accept one. If we type one by mistake, don't repeat it; tell us calmly to change it later.
- One question at a time, in plain words. "I don't know" is a fine answer.
- You guide; we make every change ourselves. Before each change, tell us what it does, how long it takes and how to undo it, then wait for our yes.
- Nothing gets removed or deleted without a backup and our clear yes at that moment.
- When we stop, save our progress so either of us can pick up later.

Start by checking our setup with us: are we inside the shared project, in Chat, on GPT-6 with Medium thinking?

Then look in the project's sources for our saved Map: a source containing the heading "Our Setup Map" and a version line, whatever the source is called.
- If there is one, tell us where we left off and what comes next.
- If there isn't, ask whether we have done the first session before. If we have, help us find our Map in the last cleanup chat. If we haven't, check that both of us are here, tell us how long it will take, and begin the interview.
```

## Why it is built this way

- **Setup lines come first and are for the humans.** ChatGPT cannot see or change its own mode, model or thinking level, so the people have to set them before sending. The prompt then has ChatGPT ask them to confirm, which catches the case where the lines were skimmed.
- **It points at files in the project, not at a link.** Whether ChatGPT reliably reads a linked repo could not be verified (see `docs/research.md`), and this repo is not public. Files uploaded to the project are the documented, dependable route. If the repo is published later, a line such as "The same files are at <link>" can be added as a fallback, after testing it.
- **The safety rules are repeated inline** so they hold even if a file fails to load. Everything else lives in the files, which keeps the message short enough to send by text.
- **It is the same prompt every time.** One thing to keep, nothing to choose.

## Other assistants

The body of the prompt is assistant-neutral. To run the playbook in Claude or Grok, replace the five setup lines and the file name `01-assistant-notes-chatgpt.md` with that assistant's equivalents, and write a matching notes file. `docs/research.md` has the connection support for each. Neither has been piloted.
