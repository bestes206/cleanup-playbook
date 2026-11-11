#!/usr/bin/env python3
"""Structural checks for the cleanup playbook.

Run from anywhere:  python3 tools/check.py
Exit code 0 means every check passed. Warnings do not fail the run.

The playbook is prose, so these checks cannot tell whether it is good. They
catch the mechanical ways it can break: a missing file, a module without a
time estimate or an undo, a removal step without a backup, jargon leaking
into user-facing text, a checklist that no longer matches the modules, and
personal details that must not be committed.

Optional: put one term per line in a file named .private-terms at the repo
root (it is git-ignored) and the check fails if any of them appears in the
repo. Use it for real names and addresses that must never be committed.
"""
import os
import re
import sys
from typing import Dict, List, Optional, Tuple

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAYBOOK = os.path.join(ROOT, "playbook")

PLAYBOOK_FILES = [
    "00-start-here.md",
    "01-assistant-notes-chatgpt.md",
    "02-intake.md",
    "03-tools-agreement.md",
    "04-map-and-checklist.md",
    "10-module-password-manager.md",
    "11-module-shared-calendar.md",
    "12-module-commitment-capture.md",
    "20-monthly-checkup.md",
]
MODULE_FILES = [f for f in PLAYBOOK_FILES if "-module-" in f or f.startswith("20-")]

# ChatGPT accepts ten files per upload to a project; the playbook must fit in one.
MAX_PLAYBOOK_FILES = 10

HEADER_FIELDS = [
    "Fixes", "Time", "Who", "Devices", "Before you start",
    "What changes", "What stays the same", "Undo", "Last checked",
]
MODULE_SECTIONS = [
    "## Why this matters",
    "## Before you start",
    "## Parts and steps",
    "## If your screen doesn't match",
    "## Undo",
    "## Done when",
    "## Update the Map",
]

# Words the couple should never meet without an explanation. Matched as whole
# words, case-insensitively, in playbook files. Table rows are exempt so the
# glossary can list them.
JARGON = [
    "OAuth", "system of record", "source of truth", "2FA", "two-factor", "IMAP",
    "ICS", "authenticate", "authentication", "credentials", "migrate", "migration",
    "vault", "connector",
]
# On-screen labels that legitimately contain a jargon word.
JARGON_ALLOWED_PHRASES = ["Two-Factor Authentication"]

MAP_SECTIONS = [
    "# Our Setup Map",
    "## Where we left off",
    "## Checklist",
    "## What bugs us most",
    "## People and devices",
    "## Email accounts",
    "## Apple and Google accounts",
    "## Calendars",
    "## Promises and to-dos",
    "## Passwords",
    "## Our agreement",
    "## The assistant",
    "## Not sure yet",
    "## Parking lot (no fix yet)",
    "## Questions for the helper",
    "## Change log",
]

CHECKLIST_HEADINGS = {
    "10-module-password-manager.md": "### Fix 1: Password app",
    "11-module-shared-calendar.md": "### Fix 2: Shared calendars",
    "12-module-commitment-capture.md": "### Fix 3: Capturing promises",
}

SAFE_EMAIL_DOMAINS = ("example.com", "example.org", "example.net", "anthropic.com")
TEXT_EXTENSIONS = (".md", ".py", ".txt", ".json", ".yml", ".yaml", "")

errors: List[str] = []
warnings: List[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def strip_code_blocks(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def first_code_block(text: str, lang: str) -> Optional[str]:
    m = re.search(r"```" + re.escape(lang) + r"\n(.*?)```", text, flags=re.S)
    return m.group(1) if m else None


def check_file_set() -> None:
    present = sorted(f for f in os.listdir(PLAYBOOK) if f.endswith(".md"))
    for f in PLAYBOOK_FILES:
        if f not in present:
            err("playbook/%s is missing" % f)
    for f in present:
        if f not in PLAYBOOK_FILES:
            err("playbook/%s is not in the expected file list (update tools/check.py "
                "and the table in 00-start-here.md)" % f)
    if len(present) > MAX_PLAYBOOK_FILES:
        err("playbook/ has %d files; more than %d will not fit in one upload"
            % (len(present), MAX_PLAYBOOK_FILES))
    start = os.path.join(PLAYBOOK, "00-start-here.md")
    if os.path.exists(start):
        body = read(start)
        for f in PLAYBOOK_FILES:
            if f == "01-assistant-notes-chatgpt.md":
                continue  # referred to generically as "the assistant notes file"
            if "`%s`" % f not in body:
                err("00-start-here.md does not list %s" % f)


def check_starter_prompt() -> None:
    path = os.path.join(ROOT, "starter-prompt.md")
    if not os.path.exists(path):
        err("starter-prompt.md is missing")
        return
    block = first_code_block(read(path), "text")
    if block is None:
        err("starter-prompt.md has no ```text block")
        return
    lines = [ln for ln in block.splitlines() if ln.strip()]
    head = "\n".join(lines[:6])
    required_in_head = {
        "shared project": r"shared project",
        "Chat": r"\bCHAT\b",
        "not Work": r"\bWork\b",
        "GPT-6": r"GPT-6",
        "Medium": r"\bMEDIUM\b",
        "High (only for the agreement)": r"\bHigh\b",
        "not Instant": r"\bInstant\b",
        "not Pro": r"\bPro\b",
    }
    for label, pattern in required_in_head.items():
        if not re.search(pattern, head, flags=re.I):
            err("starter prompt: the first lines do not mention %s" % label)
    required_anywhere = {
        "the no-passwords rule": r"password",
        "one question at a time": r"one question at a time",
        "the start-here file": r"00-start-here\.md",
        "the assistant notes file": r"01-assistant-notes-chatgpt\.md",
        "the saved Map": r"Our Setup Map",
        "backup before removal": r"backup",
    }
    for label, pattern in required_anywhere.items():
        if not re.search(pattern, block, flags=re.I):
            err("starter prompt: does not mention %s" % label)
    words = len(block.split())
    if words > 450:
        warn("starter prompt is %d words; it is meant to be short enough to text" % words)


def split_steps(text: str) -> List[Tuple[str, str]]:
    """Return (heading, body) for every level-3 and level-4 heading."""
    parts = re.split(r"^(#{3,4} .+)$", text, flags=re.M)
    out = []
    for i in range(1, len(parts), 2):
        out.append((parts[i].strip(), parts[i + 1] if i + 1 < len(parts) else ""))
    return out


def check_modules() -> None:
    for name in MODULE_FILES:
        path = os.path.join(PLAYBOOK, name)
        if not os.path.exists(path):
            continue
        text = read(path)
        head = text.split("\n## ", 1)[0]
        for field in HEADER_FIELDS:
            if "- **%s:**" % field not in head:
                err("%s: header is missing '%s'" % (name, field))
        if not re.search(r"\*\*Time:\*\*.*\d", head):
            err("%s: the Time line has no number in it" % name)
        pos = -1
        for section in MODULE_SECTIONS:
            m = re.search(r"^" + re.escape(section) + r"\s*$", text, flags=re.M)
            if not m:
                err("%s: missing section '%s'" % (name, section))
                continue
            if m.start() < pos:
                err("%s: section '%s' is out of order" % (name, section))
            pos = m.start()
        # Every removal step needs a backup and an explicit yes.
        parts_region = text.split("## Parts and steps", 1)[-1].split(
            "## If your screen doesn't match", 1)[0]
        level3 = re.split(r"^(### .+)$", parts_region, flags=re.M)
        for i in range(1, len(level3), 2):
            heading, body = level3[i], level3[i + 1]
            if "**Removal step" in body:
                if not re.search(r"back(ed)?[ -]?up|backup", body, flags=re.I):
                    err("%s: '%s' is a removal step with no backup" % (name, heading))
                if not re.search(r"\byes\b", body, flags=re.I):
                    err("%s: '%s' is a removal step with no explicit yes" % (name, heading))
        # Every step says who, why, do, check and undo.
        steps = 0
        for heading, body in split_steps(parts_region):
            if re.match(r"### Step", heading):
                err("%s: '%s' should be a level-4 heading inside a Part" % (name, heading))
            if not re.match(r"#### Step", heading):
                continue
            steps += 1
            for field in ("Who / where", "Why", "Do", "Check", "Undo"):
                if "**%s:**" % field not in body:
                    err("%s: '%s' has no %s line" % (name, heading, field))
        if steps == 0:
            err("%s: no '#### Step' headings found" % name)
        # Every part ends at a safe stopping point.
        for i in range(1, len(level3), 2):
            if level3[i].startswith("### Part") and "Safe stopping point" not in level3[i + 1]:
                # A removal part may end on its final, irreversible step instead.
                if "**Removal step" not in level3[i + 1]:
                    err("%s: '%s' has no safe stopping point" % (name, level3[i]))
        # Words that signal removal should sit inside a marked removal step.
        for i in range(1, len(level3), 2):
            heading, body = level3[i], level3[i + 1]
            if "**Removal step" in body:
                continue
            for heading4, body4 in split_steps(body):
                do = re.search(r"\*\*Do:\*\*(.*?)(?=\n- \*\*(Check|Undo)|\Z)", body4, flags=re.S)
                if do and re.search(r"\b(delete the calendar|shred|unsubscribe)\b",
                                    do.group(1), flags=re.I):
                    warn("%s: '%s' removes something but its part is not marked "
                         "as a removal step" % (name, heading4))


def check_jargon() -> None:
    for name in PLAYBOOK_FILES:
        path = os.path.join(PLAYBOOK, name)
        if not os.path.exists(path):
            continue
        text = strip_code_blocks(read(path))
        for n, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith("|"):
                continue
            scrubbed = line
            for phrase in JARGON_ALLOWED_PHRASES:
                scrubbed = scrubbed.replace(phrase, "")
            for word in JARGON:
                if re.search(r"\b" + re.escape(word) + r"\b", scrubbed, flags=re.I):
                    err("%s:%d uses '%s' outside the glossary" % (name, n, word))


def map_sections_in(text: str, label: str) -> None:
    pos = -1
    for section in MAP_SECTIONS:
        m = re.search(r"^" + re.escape(section) + r"\s*$", text, flags=re.M)
        if not m:
            err("%s: missing Map section '%s'" % (label, section))
            continue
        if m.start() < pos:
            err("%s: Map section '%s' is out of order" % (label, section))
        pos = m.start()
    if not re.search(r"^Version: \d+ · Saved: .+ · Present: .+$", text, flags=re.M):
        err("%s: second line should read 'Version: N · Saved: date · Present: who'" % label)
    for bad in (r"^\s*-?\s*password\s*:", r"\bPIN\s*:", r"secret key\s*:",
                r"security answer", r"recovery key\s*:", r"card number"):
        if re.search(bad, text, flags=re.I | re.M):
            err("%s: has a field that invites a secret (%s)" % (label, bad))


def module_parts(name: str) -> List[int]:
    text = read(os.path.join(PLAYBOOK, name))
    return [int(n) for n in re.findall(r"^### Part (\d+)\.", text, flags=re.M)]


def checklist_parts(template: str, heading: str) -> List[int]:
    m = re.search(re.escape(heading) + r"\n(.*?)(?=\n###? |\Z)", template, flags=re.S)
    if not m:
        return []
    return sorted(set(int(n) for n in re.findall(r"^- \[.\] Part (\d+)\.", m.group(1), flags=re.M)))


def check_map() -> None:
    path = os.path.join(PLAYBOOK, "04-map-and-checklist.md")
    if not os.path.exists(path):
        return
    template = first_code_block(read(path), "markdown")
    if template is None:
        err("04-map-and-checklist.md has no ```markdown template block")
        return
    map_sections_in(template, "blank Map")
    for module, heading in CHECKLIST_HEADINGS.items():
        if not os.path.exists(os.path.join(PLAYBOOK, module)):
            continue
        want = sorted(set(module_parts(module)))
        got = checklist_parts(template, heading)
        if not want:
            err("%s has no '### Part N.' headings" % module)
        elif want != got:
            err("blank Map checklist '%s' lists parts %s but %s has parts %s"
                % (heading, got, module, want))
        # Titles should match too, so the checklist reads like the module.
        text = read(os.path.join(PLAYBOOK, module))
        titles = dict(re.findall(r"^### Part (\d+)\. (.+?)(?: \(|$)", text, flags=re.M))
        m = re.search(re.escape(heading) + r"\n(.*?)(?=\n###? |\Z)", template, flags=re.S)
        block = m.group(1) if m else ""
        for num, title in titles.items():
            if not re.search(r"Part %s\. %s" % (num, re.escape(title)), block):
                err("blank Map checklist: Part %s of %s should read '%s'" % (num, module, title))
    example = os.path.join(ROOT, "examples", "example-map.md")
    if os.path.exists(example):
        body = read(example)
        start = body.find("# Our Setup Map")
        if start < 0:
            err("examples/example-map.md does not contain a Map")
        else:
            map_sections_in(body[start:], "example Map")
    else:
        err("examples/example-map.md is missing")


def repo_text_files() -> List[str]:
    out = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", "dist")]
        for f in files:
            if f == ".private-terms":
                continue
            if os.path.splitext(f)[1].lower() in TEXT_EXTENSIONS:
                out.append(os.path.join(base, f))
    return out


def check_privacy() -> None:
    private_terms: List[str] = []
    terms_path = os.path.join(ROOT, ".private-terms")
    if os.path.exists(terms_path):
        private_terms = [t.strip() for t in read(terms_path).splitlines() if t.strip()]
    email_re = re.compile(r"[A-Za-z0-9._%+-]+@([A-Za-z0-9-]+\.[A-Za-z0-9.-]+)")
    phone_re = re.compile(r"(?<![\d.])(?:\+?1[ .-]?)?\(?\d{3}\)?[ .-]\d{3}[ .-]\d{4}(?!\d)")
    for path in repo_text_files():
        rel = os.path.relpath(path, ROOT)
        try:
            text = read(path)
        except UnicodeDecodeError:
            continue
        for m in email_re.finditer(text):
            domain = m.group(1).lower().rstrip(".")
            if not domain.endswith(SAFE_EMAIL_DOMAINS):
                err("%s contains an email address that is not an example.com one: %s"
                    % (rel, m.group(0)))
        if rel != os.path.join("tools", "check.py") and phone_re.search(text):
            err("%s contains something that looks like a phone number" % rel)
        for term in private_terms:
            if term.lower() in text.lower():
                err("%s contains a term from .private-terms" % rel)
        if re.search(r"claude\.ai/(code/)?(artifact|session)", text) and rel != os.path.join("tools", "check.py"):
            warn("%s links to a private claude.ai page; review before publishing the repo" % rel)
    if not private_terms:
        warn("no .private-terms file: real names are not being scanned for "
             "(see the docstring in tools/check.py)")


def check_links() -> None:
    """Every `file.md` mentioned in a playbook file must exist in playbook/."""
    for name in PLAYBOOK_FILES:
        path = os.path.join(PLAYBOOK, name)
        if not os.path.exists(path):
            continue
        for ref in set(re.findall(r"`(\d\d-[a-z0-9-]+\.md)`", read(path))):
            if ref not in PLAYBOOK_FILES:
                err("%s refers to %s, which does not exist" % (name, ref))


def main() -> int:
    check_file_set()
    check_starter_prompt()
    check_modules()
    check_jargon()
    check_map()
    check_links()
    check_privacy()
    for w in warnings:
        print("warning: " + w)
    for e in errors:
        print("ERROR: " + e)
    print("%d error(s), %d warning(s)" % (len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
