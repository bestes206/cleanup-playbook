# Fix 1: The password app

- **Fixes:** getting locked out, hunting for sticky notes, and one reused password that would open everything if it leaked
- **Time:** about 2 hours in total, never in one go. Part 1: 25 min. Part 2: 20 min. Part 3: 10 min per device. Part 4: 15 min per email account. Part 5: 10 min each. Part 6: 10-minute sittings, as many as it takes. Part 7: 5 min, weeks later
- **Who:** both together for Parts 1, 2 and 7, and for any account you both use, whichever part it comes up in. Part 3 each partner does alone. Part 5 each does on their own phone, with the other on hand for one tap. Part 6 each can do alone for accounts that are theirs alone
- **Devices:** each person's iPhone. A computer helps for Part 1 and a printer for Part 2. A printer is not required; whether Part 1's sign-up can be finished on a phone alone is unconfirmed
- **Before you start:** the tools agreement in the Map names the password app and who pays
- **What changes:** passwords move into one locked app that fills them in for you. The reused password gets replaced, account by account, with a different one for each
- **What stays the same:** every app and website you use, and how you unlock your phone
- **Undo:** each changed password keeps its old version in the app's history. The sticky notes stay until the very end. The app itself can be cancelled and its contents exported
- **Last checked:** 2026-11-10, iOS 27.2, against 1Password, Bitwarden, Apple, Google, Yahoo and Microsoft help pages

The steps are written for **1Password**, the usual recommendation. If the Map says Bitwarden or Apple Passwords, the goals of each step are the same; the differences are listed at the end of this file.

## Why this matters

Say something close to this:

"Right now one password opens most of your accounts, and it's written on paper. If any one website leaks it, everything is exposed, and when a note goes missing you're locked out. A password app remembers a different, strong password for every account and types it in for you. You remember one password, the one for the app, and your face unlocks it day to day. This is the one real habit change in the whole cleanup, and every later step leans on it."

## Before you start

Check the Map:

- **Which app** did they agree on, and who is paying? If there is no agreement yet, run `03-tools-agreement.md` first.
- **Are both here?** Parts 1 and 2 need both. If only one is present, offer Part 3 on their own devices if Part 1 is done, or pick a time for both.
- **Which email address gets their password-reset emails?** Part 4 starts with that one.

Remind them of the rule before the first step: "You'll be creating and typing passwords in the next few minutes. Type them only into the app or the website. Don't tell me what any of them are, and I won't ask."

## Parts and steps

### Part 1. Set up the password app together (both, 25 minutes)

Goal: one family account, both partners in it, each with a private box and one shared box between them.

#### Step 1.1 Start the family account
- **Who / where:** the partner who agreed to pay, on a computer if one is handy. The phone's web browser should also work *(unconfirmed for the whole sign-up; if it stalls on the phone, move to a computer rather than fight it)*
- **Why:** the account is created on the provider's website, and that person becomes its first organizer.
- **Do:**
  1. Go to **1password.com** and choose the **Families** plan. There is a 14-day free trial that doesn't ask for a card.
  2. Enter an email address they will keep for years. Their own, not a shared one.
  3. Choose the account password. Give this advice: "This is the one password you'll still need to remember. Make it three or four unrelated words, something you have never used anywhere. Write it on paper for now; that paper becomes part of your emergency sheet in Part 2. Don't tell me what it is."
- **Check:** "What do you see now?" They should be inside the app's website with two boxes listed: **Private** and **Shared**.
- **Undo:** an unused trial account can simply be left to lapse or deleted from its settings.

#### Step 1.2 Keep the Emergency Kit
- **Who / where:** same partner, same screen
- **Why:** the sign-up creates a one-page Emergency Kit containing a long **Secret Key**. Without it, nobody, including the company, can get them back in.
- **Do:** when the site offers **Save Emergency Kit**, save the file. If the offer has passed: **1password.com > their name > Manage Account > Save Emergency Kit**. It gets printed in Part 2. Tell them: don't email it, don't photograph it, don't paste it into a chat.
- **Check:** they can find the saved file.
- **Undo:** nothing to undo.

#### Step 1.3 Invite your partner
- **Who / where:** first partner sends; second partner accepts on their own phone
- **Why:** each person gets their own account, their own password and their own Emergency Kit, so neither depends on the other's phone.
- **Do:**
  1. First partner: tap the account icon, then **Manage Accounts > People > Invite People**, enter the partner's own email address, **Invite**.
  2. Second partner: open the invitation email, follow it, choose their own account password (same advice as step 1.1), and save their own Emergency Kit.
  3. First partner: back in **People**, tap **Confirm** next to the partner's name.
- **Check:** ask the second partner what boxes they see. They should have their own **Private** and the same **Shared**.
- **Undo:** a person can be removed again from **People**.

#### Step 1.4 Make both of you organizers
- **Who / where:** first partner, on 1password.com
- **Why:** an organizer can restore the other person's access if they forget their password, but cannot restore their own. With both as organizers, each of you is the other's way back in.
- **Do:** in **People**, open the partner's name and make them a **family organizer**. *(The exact button label is unconfirmed; look for "organizer" on that screen.)*
- **Check:** the partner's name shows as an organizer.
- **Undo:** the same screen removes the role.

#### Step 1.5 Prove the sharing works
- **Who / where:** both, on phones or the website
- **Why:** seeing it work once is what makes the shared box trustworthy.
- **Do:** first partner creates a new item in **Shared** called "Test, delete later" with any made-up text. Second partner looks in their **Shared**.
- **Check:** "Can you both see the test item?" Leave it there; it is used again in Part 3.
- **Undo:** delete the test item.

**Safe stopping point.** Update the Checklist, save the Map. Tell them Part 2 needs a printer or a pen and takes about 20 minutes, and that it should happen within a day or two, before the app holds anything they'd miss.

### Part 2. The way back in (both, 20 minutes)

Goal: if a phone is lost or a password forgotten, each of them can still get in.

#### Step 2.1 Print both Emergency Kits
- **Who / where:** each partner, wherever there is a printer
- **Why:** a kit that exists only on the phone is lost with the phone.
- **Do:** print the kit. Write the account password on it by hand, in the space provided. No printer: copy the sign-in address, the email address and the Secret Key onto paper by hand, then check it character by character against the screen.
- **Check:** each partner is holding a sheet of paper with four things on it: sign-in address, email, Secret Key, account password. Don't ask them to read any of it out.
- **Undo:** nothing to undo.

#### Step 2.2 Put the sheets somewhere safe
- **Who / where:** both
- **Why:** the sheet opens everything, so it lives where passports and important papers live.
- **Do:** agree on a place at home that a burglar wouldn't think of and that both partners can reach. Not in a wallet, not on the fridge, not in the car. Then delete the downloaded kit file from the phone or computer's Downloads if they like; the printed sheet is now the copy.
- **Check:** ask only: "Are both sheets stored, and do you both know where?" Do not ask where. Record yes or no in the Map.
- **Undo:** the sheets can be moved at any time; tell the other partner if they are.

#### Step 2.3 Settle the subscription before the trial runs out
- **Who / where:** the partner who agreed to pay, on the provider's website
- **Why:** the account started as a 14-day free trial. If the trial lapses while you are halfway through changing passwords, the app may stop saving new ones, and a password it failed to save is a lockout.
- **Do:** ask on what date the account was created, and work out the date twelve days after it. Then either:
  - they subscribe now, on the provider's own billing page, with the card they agreed on in the tools agreement. They type the card details there; you never need them. Or
  - they choose to wait. In that case write the deadline into the Map's *Where we left off* note, suggest they put it on their calendar, and do not start Part 4 until it is settled.
- **Check:** "Does the billing page show a paid plan, or a trial with an end date?" Record which in the Map, with the date.
- **Undo:** a subscription can be cancelled from the same billing page. Before cancelling, see the module's Undo section.

**Safe stopping point.** Update the Checklist, save the Map.

### Part 3. On each phone, tablet and computer (each person, 10 minutes per device)

Goal: the app is on every device they use, and it offers to fill in passwords.

#### Step 3.1 Install and sign in
- **Who / where:** each partner, on each of their own devices
- **Why:** a password app that is on one device gets abandoned the first time they need a password on another.
- **Do:**
  - **iPhone or iPad:** install **1Password** from the App Store. Sign in by scanning the square code on the Emergency Kit or from another signed-in device, then type the account password. Turn on Face ID when offered.
  - **Windows PC:** download the app from **1password.com/downloads**. In a browser signed in to 1password.com, choose **their name > Set up another device** and follow it. Add the browser add-on when the app offers it.
- **Check:** "Open the app. Can you see the 'Test, delete later' item?"
- **Undo:** deleting the app from a device removes nothing from the account.

#### Step 3.2 Prove you know your own account password
- **Who / where:** each partner, on their own iPhone, once
- **Why:** Face ID does the unlocking from now on, which is exactly how people forget the one password they still need.
- **Do:** close the app completely, open it again, and unlock it by typing the account password instead of using Face ID.
- **Check:** "Did you get in by typing?" If not: don't keep guessing. The other partner, as an organizer, can start a recovery for them from **People** on 1password.com. Do that while both are available, and note it for the helper if it doesn't go through.
- **Undo:** nothing to undo.

#### Step 3.3 Let it fill in passwords on the iPhone
- **Who / where:** each partner, on iPhone and iPad
- **Why:** this is what makes it effortless. Without it, they'd be copying and pasting.
- **Do:** **Settings > General > AutoFill & Passwords**. Turn on **AutoFill Passwords and Passkeys**. In the list under it, turn on **1Password**. Leave **Passwords** (Apple's own) switched on as well for now, so anything the phone already remembers keeps working.
- **Check:** open a website they have an account on, in Safari. Tap the sign-in box. "Do you see 1Password offering to help above the keyboard?"
- **Undo:** the same switches.

#### Step 3.4 Bring across what the phone already remembers (optional)
- **Who / where:** each partner, on iPhone
- **Why:** it saves typing in accounts the phone already knows.
- **Do:** in the 1Password app, look for **Import** and choose to import from the Passwords app. *(Available on recent iOS; exact wording unconfirmed. If it isn't there, skip this step. Passwords will be saved one at a time as they sign in to things, which works just as well.)*
- **Check:** new items have appeared in their **Private** box.
- **Undo:** imported items can be deleted. Nothing is removed from Apple's Passwords by importing.

**Safe stopping point.** One Checklist line per person. Save the Map.

### Part 4. Lock down the email accounts first (15 minutes per account)

Goal: every email account has its own strong password, saved in the app, and a second sign-in step.

Explain the order: "Email comes first because every other account sends its 'forgot password' link to your email. Whoever controls the email can reset everything else."

Work through the email accounts in the Map in this order: the one that receives password-reset emails first, then the other personal ones, then the business ones. One account per sitting is fine.

**Before changing any account's password, check Part 3.** The new password will be one nobody has seen, so it exists only in the app. Every person who uses the account must already have the app working (Part 3 ticked in the Checklist) on a device they will have with them, and anyone who reads that mailbox on a PC needs the app on that PC too. If that isn't true yet, do Part 3 first. Skipping this is the surest way to lock someone out.

**For an account both partners use:** do every step of this part together, or at a time you have both agreed, with both phones on the table. Never one partner alone. Changing its password signs the other person's devices out of that mailbox until they sign in again with the new one, and the second sign-in step has to be set up so that both can get the code (step 4.6 explains how). Its item belongs in the **Shared** box.

**For an iCloud address** (one ending icloud.com, me.com or mac.com): its password is the Apple Account password. Skip it in this part and do it in Part 5, which has the right safeguards. If an iCloud address is where the password-reset emails go, do Part 5 before the rest of this part.

**For an account marked `managed by someone else`:** changing the password is fine. Leave everything else about it alone, and if the second sign-in step isn't offered, the organisation controls it.

#### Step 4.1 See whether this address has been in a leak
- **Who / where:** whoever uses the account, in a web browser
- **Why:** old accounts have often been caught in a company break-in. Knowing tells you how urgent this one is.
- **Do:** go to **haveibeenpwned.com** and type the **email address** into the search box. Say clearly: "Only the email address. That site also has a box for checking passwords. Don't use it. Ignore the adverts too."
- **Check:** ask whether it said the address was found in any leaks. Either way the next steps are the same; a "yes" just means do this one today. Record the result in the Map.
- **Undo:** nothing changed.

#### Step 4.2 Check this account's own way back in
- **Who / where:** whoever uses the account, signed in to it in a web browser
- **Why:** every email account has a recovery phone number and a backup email address that its "forgot password" link relies on. On an old account these are often a number or address nobody has any more. They must be right before the password changes, because they are the safety net for the next steps.
- **Do:** in the account's security settings, find the recovery phone and the recovery or backup email. Have them tell you only whether each one is a number or address they can still receive messages on today. If one is out of date, add a current one first, confirm it works, and only then remove the old one.
- **Check:** "Could you receive a code right now at the phone number and the backup address listed there?" Record the answer in the Map.
- **Undo:** the same settings page.

#### Step 4.3 Save the password it has now
- **Who / where:** same person
- **Why:** add before remove. If the change goes wrong halfway, the current password is safely stored rather than half-remembered.
- **Do:** sign in to the email account in a web browser, typing the current password as usual. When 1Password offers to save it, accept, choosing **Shared** for a shared account and **Private** for a personal one. If it doesn't offer, create the item by hand in the app.
- **Check:** the account now appears in the app, in the right box.
- **Undo:** delete the item.

#### Step 4.4 Change it to a new one
- **Who / where:** same person, in the browser, signed in to the email account
- **Why:** this is the moment the reused password stops opening this account.
- **Do:**
  1. Find the account's password setting. Gmail: **Google Account > Security & sign-in > Password**. Yahoo: **Account Security > Change password**. Outlook.com: **account.microsoft.com/security**. These labels move; go by what is on screen.
  2. In the new-password box, let 1Password suggest a password and accept it. They never need to see or type it.
  3. When 1Password asks to **update** the saved item, accept.
- **Check:** open the item in the app. "Does it show that the password was changed just now?" The old one is kept in the item's history.
- **Undo:** the old password is in the item's history, and the provider's own "forgot password" link sends a reset to their phone or recovery address.

#### Step 4.5 Sign back in everywhere this mailbox is used
- **Who / where:** everyone who uses the account, on every device from the Map's *Read in* line
- **Why:** each device was signed in with the old password and will stop receiving mail until it has the new one.
- **Do:** open the Mail app. Within a few minutes it shows an account error or asks for the password. Tap it and sign in on the screen that appears, letting 1Password fill in the new password. For a shared account, the other partner does the same on their devices now. A mail program on a PC will ask in the same way; they copy the new password from the password app on that PC and paste it in.
- **Check:** send a test email to that address from another account. "Has it arrived on every device in this account's *Read in* line, the PC included?"
- **Undo:** not applicable; this step restores things.

#### Step 4.6 Turn on the second sign-in step
- **Who / where:** same person; both for a shared account
- **Why:** with this on, a stolen password alone isn't enough. Someone would also need the phone.
- **Do:**
  1. **First, if both partners use this account, settle where the code will go, before touching any setting.** If it goes to one person's phone, the other is stuck whenever they need to sign in. Two ways round it, in order of preference:
     - add **both** phone numbers as ways to receive the code, if the provider allows more than one;
     - have the password app produce the codes, stored on the shared item, so both phones have them. This takes a few extra taps and is a good moment to call the helper.

     Both partners must be present for the rest of this step.
  2. Turn it on:
     - **Google:** **Google Account > Security & sign-in >** under "How you sign in to Google", **Turn on 2-Step Verification**.
     - **Yahoo:** **Account Security >** under "Ways of signing in", **2-step verification**, then pick a method.
     - **Outlook.com:** **account.microsoft.com/security > Manage how I sign in > Additional security > Two-step verification > Turn on**.
  3. If the provider offers **backup codes**, save them inside the account's item in 1Password. Not in a chat, not in a note.
- **Check:** three things, in order.
  1. Sign out of the account in the browser and sign back in. "Did it ask for a code, and did you get in?"
  2. For a shared account, the other partner signs in too, on their own device, and gets their own code.
  3. Send another test email to the address. "Has it arrived on every device in the *Read in* line?" Some older mail programs, mostly on PCs, stop working when the second step goes on and ask for a special "app password". If mail has stopped on any device, or anything asks for an app password, turn the second step off again for now (same settings page), mark this step `stuck`, and bring in the helper.
- **Undo:** the same settings page turns it off.

**Safe stopping point after each account.** Update that account's lines in the Map (way back in checked, second sign-in step, in the password app, has its own password, checked for leaks). Save.

### Part 5. Lock down the Apple Accounts (each person, 10 minutes, partner on hand)

Goal: each Apple Account has a second sign-in step, a current phone number, a recovery contact, and a password of its own.

#### Step 5.1 Check the second sign-in step
- **Who / where:** each partner, on their iPhone
- **Why:** the Apple Account holds the phone's backups, photos and messages.
- **Do:** **Settings > their name > Sign-In & Security > Two-Factor Authentication**.
- **Check:** "Does it say On, and is the phone number listed there the one you use now?" Most accounts already have it on. If the number is out of date, add the current one on that screen before removing the old one.
- **Undo:** not applicable.

#### Step 5.2 Add a recovery contact
- **Who / where:** each partner, on their iPhone, with the other partner reachable to accept
- **Why:** if they forget the Apple Account password, the recovery contact's phone can produce a code to let them back in. Without one, Apple's own recovery can take days.
- **Do:** **Settings > their name > Sign-In & Security > Recovery Contacts > Add Recovery Contact**, and choose the partner. The partner accepts on their phone.
- **Check:** each partner's phone lists the other as a recovery contact.
- **Undo:** the same screen removes a contact.

Do **not** set up a "Recovery Key" if the phone offers one. Losing that key means losing the account for good. A recovery contact is the safer choice.

#### Step 5.3 Give the Apple Account its own password
- **Who / where:** each partner, on their iPhone
- **Why:** if the Apple Account uses the old shared password, it is the most valuable thing that password still opens.
- **Do:** ask only: "Is your Apple Account password the old shared one, or one used anywhere else? Yes or no." If no, save it into their **Private** box by hand and move on. If yes: **Settings > their name > Sign-In & Security > Change Password**. The phone asks for its passcode first. For the new password, use the app's generator set to produce words rather than random characters, because this is one they may occasionally have to type on another screen. Save it in **Private**.
- **Check:** the Apple Account item is in their Private box with today's date.
- **Undo:** the password can be changed again from the same screen.

If the Map says the two of them **share one Apple Account** on any device, don't try to separate it here. Note it under *Questions for the helper*; untangling a shared Apple Account can affect photos and messages and needs care.

**Safe stopping point.** Update the Apple Account lines in the Map. Save.

### Part 6. Replace the old shared password everywhere else (10-minute sittings)

Goal: nothing important still opens with the old password.

This part is a routine repeated, not a single sitting. Each account takes about three minutes once they have the hang of it: save the current password (as in step 4.3), change it with the app's suggestion (4.4), and turn on the second sign-in step where it's offered (4.6).

**An account both of you use is never changed by one of you alone.** A joint bank login, a shared shopping account, a business tool you both sign in to: stop, and do it together or at an agreed time, exactly as in Part 4, including settling where the sign-in code goes before the second step is turned on. Each partner working alone sticks to accounts that are theirs alone.

Work in this order, and explain why: "Start with what would hurt most."

1. **The mobile phone account** with their carrier. Sign-in codes go to the phone number, so whoever controls the phone account can intercept them.
2. **Money:** banks, cards, payment apps, payroll, accounting, anything that can move money.
3. **Accounts that hold a card or can spend:** shopping sites, app stores, subscriptions.
4. **Tax, government, health and insurance.**
5. **Business tools both rely on.**
6. **Everything else,** as they come across it.

Two habits make the long tail take care of itself:

- **As you go:** whenever either of them signs in to anything, they let the app save it. If it was the old password and the account is theirs alone, they change it then and there. If the other partner uses it too, they save it now and change it together later.
- **Use the app's own check:** in 1Password this is **Watchtower**, which lists reused and weak passwords. Ask them for the *count* of reused passwords at the end of each sitting and record it in the Map. Watching the number fall is the progress bar.

**Safe stopping point after any account.** Mark Part 6 done when the first four groups are finished and the reused count is at or near zero. The rest continues through the monthly checkup.

### Part 7. Retire the sticky notes (both, 5 minutes, at least two weeks after Part 6 began)

**Removal step.** The notes are the old system and the backup for the new one, so they go last and in two stages.

#### Step 7.1 Envelope first
- **Who / where:** both, with the notes in front of them
- **Why:** hiding comes before destroying.
- **Do:** only when all of these are true:
  - both have used the app for two weeks without reaching for a note;
  - both emergency sheets are stored (Part 2);
  - they have gone through the notes one at a time and, for each, confirmed the account is in the app. They check silently; they do not read passwords out to you.

  Then put every note in an envelope, write the date on it, and store it with the emergency sheets. The backup is the app plus the two emergency sheets. Ask each partner for a clear yes before the notes go in.
- **Check:** "Are there any passwords left on paper anywhere outside that envelope? Desk, wallet, monitor, car?"
- **Undo:** open the envelope.

#### Step 7.2 Shred, later
- **Who / where:** both
- **Why:** paper passwords are a risk as long as they exist, and by now every one of them has been changed anyway.
- **Do:** if the envelope has stayed sealed for two more weeks, shred it. Both say yes on the day.
- **Check:** done, and noted in the Change log with the date.
- **Undo:** none, which is why it waits for two quiet weeks.

## If your screen doesn't match

- **The sign-up page shows a different price or plan names.** Prices change. Have them read you the plan names and prices; the plan they want is the one for a family or household. If the price differs a lot from the agreement in the Map, pause and let both partners confirm before continuing.
- **"Security & sign-in" isn't in the Google Account.** Older layouts call it "Security". Look for "2-Step Verification" by name.
- **AutoFill & Passwords isn't under General.** Try the search box at the top of Settings and type "AutoFill".
- **1Password doesn't offer to save or fill.** Check step 3.3, then close and reopen the browser. As a fallback, they can copy the password from the app and paste it.
- **The Mail app never asks for the new password.** Have them send themselves a test email. If it doesn't arrive, look in **Settings > Apps > Mail > Mail Accounts** for the account and an option to sign in again. *(Path unconfirmed on the current iOS; use the Settings search for "Mail Accounts".)*
- **A provider won't accept the long generated password.** Some sites have length limits. Shorten the generated password in the app's generator and try again.
- **They are locked out of something.** Stop. Don't guess passwords. Use the provider's official "forgot password" link, check the item's history in the app for the previous password, and bring in the helper.

Anything else: follow the general routine in `00-start-here.md`.

## Undo

- **A changed password:** the old one is in the item's history in the app. If the account is inaccessible, use the provider's "forgot password" link.
- **The second sign-in step:** can be turned off on the same settings page. Keep it on unless it is actually locking someone out.
- **Autofill on the phone:** the switches in step 3.3.
- **The whole app:** everything in it can be exported, and the account cancelled, from the provider's website. Export first, cancel second, and do this only with the helper: a cancelled or lapsed account may stop saving or showing passwords.
- **The sticky notes:** recoverable until step 7.2.

## Done when

- Both partners can open the app on every device they use, and each has typed their account password from memory at least once.
- Both emergency sheets are printed and stored, and both know where.
- Each partner is an organizer and is the other's Apple recovery contact.
- Every email account in the Map shows: way back in checked, its own password, in the app, second sign-in step on, and mail still arriving on every device.
- The password app is on a paid plan, or its trial end date is in the Map with a decision made.
- The carrier, money, spending and government groups no longer use the old password.
- The app's reused-password count is recorded, and at or near zero.
- No password is written on paper outside the sealed envelope.

## Update the Map

- *Passwords* section: app name and setup date, emergency sheets, both know where, reused count with date, sticky-note status.
- Each email account block: the four protection lines.
- *Apple and Google accounts*: second sign-in step and recovery contact for each person.
- Checklist: Fix 1 parts, with dates and names.
- Change log: one line per sitting.

## If they chose a different app

The goals of every step stay the same. Only these details differ.

**Bitwarden**

- Sign up at bitwarden.com; verify the email. Sharing is set up on the website: **New organization**, then **Admin Console > Members > Invite member**; the partner accepts, and the first partner confirms.
- Shared items are ones whose **Owner** is the organization. Everything else is private.
- Bitwarden's free tier has no trial to settle; step 2.3 applies only if they chose a paid plan.
- There is no reset for a forgotten main password. The emergency sheet (Bitwarden calls its version a Security Readiness Kit) is the only way back in on the free tier, so Part 2 matters even more. On a paid plan, set each other up under **Emergency access**.
- On the iPhone, step 3.3 is the same with **Bitwarden** in the list.
- The reused and weak reports need a paid plan; the leak report is free.

**Apple Passwords**

- Nothing to install on the iPhones. In the **Passwords** app, tap **+** to create a shared group, name it, and **Add People**; the partner accepts under **Group Invitations**. The partner must be in Contacts.
- There is no separate account password, no trial and no emergency sheet. The way back in is the Apple Account itself. So Part 2 is replaced by Part 5: do Part 5 straight after Part 1, and skip steps 2.1 to 2.3 and 3.2. Wherever this module, the Map or the monthly checkup says "emergency sheets stored", read instead "each of you is the other's recovery contact, and the phone numbers on both Apple Accounts are current". That is the condition for retiring the sticky notes in Part 7.
- On a Windows PC: install **iCloud for Windows**, turn on **Passwords & Keychain**, approve on the iPhone, and install the browser add-on it offers. The iPhone needs to be nearby. Shared groups can be used on the PC but only created and managed on the iPhone.
- When a shared password is changed in a PC browser, the "update password" prompt may not appear; update the item by hand in the iCloud Passwords app.
- The security check is **Passwords > Security**.
