# Digital Cleanup Playbook: Problem Statement

Nov 9, 2026 · Public edition

*This is the brief the playbook was built from, trimmed for publication. Three things are left out: the description of the household the example case was drawn from, the instructions for the build itself, and the author's name. One example that pointed at that household's line of work is shortened. Nothing else is changed.*

## Problem statement

Many small business owners and families can't hand work to an AI agent yet because their digital life has no single home. Accounts, calendars, passwords and commitments are scattered across Gmail, Yahoo, Outlook, iCloud, paper and memory, so nothing stays in sync and no tool can get clean, reliable access.

The fix usually needs a patient expert in the room, and these users won't tolerate being moved off apps they already know.

**The opportunity:** a guided cleanup playbook any assistant (Claude, ChatGPT, Grok) can run from one starter prompt. It maps their setup, ranks fixes by the pain they actually feel, and walks them through each one. Nothing is removed without a backup and the user's OK, so every step can be undone.

## Personas

**The field operator.** Lives on their phone, out of the office most of the day. Makes commitments in passing and loses them. Wants to be where they said they'd be without someone calling them. Low tolerance for setup; will try things if they're quick.

**The overloaded organizer.** Runs the household, a partner's schedule and the business finances, mostly from a PC. Carries the whole system in their head and feels overwhelmed. Struggles to even name all the tools they use. Wants clarity and fewer things to keep track of.

**The helper.** The tech-savvy friend or consultant who gets pulled in. Wants to hand them something that works without being in the room for every step.

## User stories

Grouped by the pain they fix, roughly in the order a cleanup should tackle them.

**Access and passwords**

- As the organizer, I want to know exactly which login is my Apple ID, so I can connect my calendar without guessing.
- As a couple, we want our passwords in one shared, safe place, so we stop getting locked out and stop relying on sticky notes.
- As a couple, we want our reused shared password replaced, so one leak doesn't expose everything.

**Calendars and commitments**

- As the field operator, I want the kids' activity schedules on my phone automatically, so I don't depend on my partner to tell me.
- As the field operator, I want anything I agree to by text, call or out loud to land on my calendar with an alert, so I show up on time without a rescue call.
- As the organizer, I want the dead calendars cleaned out, so I can actually see what's real.
- As a couple, we want one shared calendar for family and one for business, so we both see the same picture.

**Email**

- As the field operator, I want all my business inboxes in the app I already open, so I'm not checking five places.
- As the organizer, I want to keep using the mail app I know, so nothing about my day feels different.

**Notifications and devices**

- As a user, I want only the alerts that matter to reach me, so a buzz means something again.
- As the organizer, I want messages I delete on my phone to disappear on my iPad too, so my devices match.

**Clarity**

- As the organizer, I want one page showing every account, app and calendar we use, so I can stop carrying it all in my head.

**The playbook itself**

- As a helper, I want to hand someone one prompt and a repo link, so their assistant walks them through the cleanup and they only need me when they get stuck.
- As a user, I want to be asked one question at a time in plain language, and "I don't know" should be a fine answer.
- As a user, I want every change explained and reversible before I make it, so I'm never afraid of breaking something.
- As a user, I want fixes ordered by what bugs me most, so I get a win early.
- As an AI agent, I need clean, consistent access to calendars, email and tasks, so I can actually help once the cleanup is done.

## Design principles

1. **Change the plumbing, not the apps.** People keep Apple Mail, Apple Calendar, their PC. We change what those apps point at.
2. **Add before you remove.** New things go in before old ones come out. Nothing is removed without a backup and the user's explicit OK, so every step can be undone.
3. **Pain first.** Each fix is sold by the problem it solves ("never miss a game"), not the tech ("migrate your calendar").
4. **One step at a time.** The assistant checks in before every change and confirms it worked after.
5. **Phone-friendly.** Every step has to work for someone doing it all on an iPhone.
6. **Assistant-agnostic.** The playbook runs the same in Claude, ChatGPT or Grok.
7. **Passwords are the one real habit change.** Worth pushing, because everything else depends on it.

## Open questions

- [ ] Do both partners use the brokerage Outlook account, or just one?
- [ ] How does the playbook tell live calendar subscriptions from dead ones?
- [ ] Where do client meetings and appointments go today, if anywhere?
- [ ] Decided: Apple vs Google is presented as a tradeoff in the tools agreement, with a recommendation; users choose.
- [ ] Which password manager to recommend, and does setup need a human?
- [ ] How should industry tools plug in?
- [ ] Decided: a helper hands it out for now, staying on call during the pilot.

## Panel review

The biggest gap: the plan never says what happens between sessions or when a step goes wrong halfway through. Five simulated reviewers stress-tested it; their findings are below.

**Security expert**

- Never have users paste passwords into an AI chat. The playbook should say so up front and use sign-in screens and OAuth connectors instead.
- Order matters when replacing a reused password: email accounts first, since they reset everything else.
- Turn on two-factor sign-in for every email account and the Apple ID, and set an Apple recovery contact.
- The password manager needs a recovery plan (an emergency kit stored offline) and a shared vault plus a personal vault for each partner.
- Old, long-lived accounts like a shared Yahoo address are high risk. Check whether they've shown up in known breaches.

**Apple and Google admin**

- Adding a Google account to Apple Calendar syncs both ways. A subscribed calendar link is read-only and can refresh slowly. The playbook must pick the right one for each case.
- Shared iCloud calendars work for Apple devices, but a PC user needs iCloud for Windows or a web login to see them.
- Messages sync only works when both devices use the same Apple ID with Messages in iCloud turned on. Check that first.
- Email forwarding changes which address replies come from. Adding accounts to the mail app is often safer than forwarding.
- A brokerage or employer Outlook account may be locked down by its IT team, blocking forwarding or connectors.

**Non-technical test user**

- "Subscribe", "OAuth" and "system of record" mean nothing to me. Use plain words and say why each step matters to me.
- I'll stop halfway. I need to pick up where I left off, with a checklist showing what's done.
- Tell me how long each step takes before I start.
- If something looks different on my screen, what do I do? Every step needs a "this doesn't match" escape hatch.
- Two people doing this together need to know who does which step on which device.

**Small business operations consultant**

- Separate business from personal: who owns each account, and what happens if an employee leaves or the business is sold?
- Shared business inboxes on free Gmail accounts work, but a paid business account adds ownership and admin control. It's worth flagging as an option, not a requirement.
- Brokerages often have record-keeping and client-data rules. Check them before connecting an agent to work email.
- The real behaviour change is capturing commitments. Tools only help if capture is nearly effortless, ideally by voice.
- Someone has to maintain this. Add a short monthly checkup to the playbook.

**Agent builder**

- Check which connectors each assistant actually offers. Gmail and Google Calendar are widely supported; Yahoo and iCloud mail mostly aren't.
- Many connectors handle one Google account at a time, so several business Gmail inboxes may need consolidating or forwarding into one for an agent to see them.
- Agents need one calendar and one task list they can write to. That pushes the system-of-record choice toward Google, even if users keep viewing in Apple apps.
- Save the intake map as a file in the repo, so later agents start from it instead of re-asking.

**What this changes in the plan**

- [ ] Add a no-passwords-in-chat rule to the starter prompt
- [ ] Add saved progress and a resume flow
- [ ] Give every fix module a time estimate, plain-language "why", and a "screen doesn't match" path
- [ ] Present Apple vs Google as a tradeoff in the tools agreement, with a clear recommendation and why; users make the final call
- [ ] Add a compliance check for work email accounts
- [ ] Add a monthly checkup module

## Brief for Claude Code

**Mantra: garbage in, garbage out.** The best agent in the world gives garbage answers on top of messy accounts, calendars and passwords. This playbook cleans the inputs first.

**What to build:** a generic, assistant-agnostic cleanup playbook. A first pilot runs with one couple who run a business together, in their shared ChatGPT Business project.

**How it reaches people:** a helper sends one starter prompt that links to a repo with the playbook details. Intake and the tools agreement are one joint session with both partners, since they set the shared foundation. After that, either partner can run fix modules on their own.

**Pilot setup in ChatGPT (no choices left to the users):** open their shared Project, stay in **Chat** (not Work), select **GPT-6** with the thinking level on **Medium** (GPT-6 Sol runs underneath). Switch to High only if the tools agreement step feels thin. Don't use Instant, Pro, or the Work tab. The starter prompt should say all of this in its first lines.

**Flow**

1. **Intake.** A plain-language interview, one question at a time, where "I don't know" is fine. It produces a saved map of accounts, devices, calendars and pain points.
2. **Tools agreement.** Lay out options side by side in plain words: cost, how much it changes their day, and how well their assistant connects to it. Make a clear recommendation and explain why, then let them choose. Both partners explicitly agree on one shared stack, including anything new to buy (e.g. a password manager) and how it's shared. Nothing changes silently.
3. **Fix modules,** ordered by pain. First slice: password manager, shared calendar, commitment capture. Commitment capture depends on the calendar choice, so it comes after the shared calendar.

**Rules for every module:** add before removing, and remove only with a backup and explicit OK; reversible; time estimate up front; a plain-language "why"; a "my screen doesn't match" path; works on an iPhone; never ask for passwords in chat.

**Progress:** a checklist and the map saved where both partners can see them (for the pilot, their shared ChatGPT project), so either can pick up where the other left off.

**Pilot success**

- Both partners finish the first slice, with the helper on call like a forward-deployed PM; every time they reach out is logged as feedback to improve the playbook, not a failure
- They say things feel clearer, judged in a short debrief conversation with the helper, not a score
- ChatGPT can access the information they expect it to have

**For Claude Code to work out**

- [ ] Can the starter prompt stand alone, or does it need the repo? Test whether ChatGPT reliably reads a linked repo
- [ ] How shared files, memory and chats behave in ChatGPT Business projects
- [ ] What goes in the saved map: useful, but nothing sensitive
- [ ] The repo structure and the format of a fix module
- [ ] Which connectors each assistant supports for Gmail, iCloud, Yahoo and Outlook
- [ ] Turn the panel review checklist into requirements
