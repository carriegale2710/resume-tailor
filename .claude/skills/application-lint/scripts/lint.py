#!/usr/bin/env python3
"""Mechanical checks for job application documents in Markdown.

Usage:
  python3 lint.py --type resume|cover|criteria <file.md> [--spelling au|us] [--words 250-350]
                  [--keywords criteria.md]
  python3 lint.py --test

Exit code 1 if any ERROR.
"""
import argparse
import re
import sys

# ---------- shared ----------
BULLET = re.compile(r"^\s*[-*•]\s+(.*)")
URLISH = re.compile(r"\S+\.(com|dev|io|au|net|org|app|me)\S*|\S+@\S+")
US_IZE = re.compile(r"\b[A-Za-z]*(?:iz|yz)(?:e|es|ed|er|ers|ing|ation|ations)\b")
IZE_OK = {"size", "sizes", "sized", "sizing", "resize", "resized", "resizing", "downsize", "downsized",
          "prize", "prizes", "seize", "seized", "seizes", "seizing", "capsize"}
US_WORDS = {"color", "colors", "colored", "behavior", "behaviors", "behavioral", "center", "centers",
            "centered", "favorite", "favorites", "honor", "honors", "labor", "modeling", "modeled",
            "traveled", "traveling", "catalog", "defense", "enrollment", "fulfill"}
REFEREES = re.compile(r"^\s*#*\s*(referees?|references)\b|(available|supplied|provided)\s+(up)?on\s+request", re.I)


def spelling(lines):
    issues = []
    for n, line in enumerate(lines, 1):
        text = URLISH.sub(" ", line)
        for w in US_IZE.findall(text) + [w for w in re.findall(r"[A-Za-z]+", text) if w.lower() in US_WORDS]:
            if w.lower() not in IZE_OK:
                issues.append(("WARN", n, f"US spelling '{w}'. Use Australian English (e.g. -ise, -our, -re)."))
    return issues


def keywords_from(criteria_text):
    """Bullets under the '## Keywords' heading of criteria.md, minus any '(note)' or '— note'."""
    kws, inside = [], False
    for line in criteria_text.splitlines():
        if line.startswith("## "):
            inside = line[3:].lower().startswith("keywords")
        elif inside and (m := BULLET.match(line)):
            kw = re.split(r"\s+[(—–]", m.group(1))[0].strip(" `*")
            if kw:
                kws.append(kw)
    return kws


def keyword_coverage(text, kws):
    missing = [k for k in kws if not re.search(rf"(?<!\w){re.escape(k)}(?!\w)", text, re.I)]
    if not missing:
        return []
    return [("WARN", 0, f"Keywords: {len(kws) - len(missing)}/{len(kws)} from criteria.md found. "
                        f"Missing: {', '.join(missing)}. Add the true ones, in the ad's wording.")]


def blocks(lines):
    """Yield (first_line_no, text) for each blank-line-separated block."""
    start, buf = None, []
    for n, line in enumerate(lines + [""], 1):
        if line.strip():
            start = start or n
            buf.append(line.strip())
        elif buf:
            yield start, " ".join(buf)
            start, buf = None, []


# ---------- resume ----------
WEAK_OPENERS = ("responsible for", "duties included", "worked on", "was involved in",
                "dealt with", "handled", "helped with")
PERSONAL = re.compile(r"\b(date of birth|d\.?o\.?b\.?|marital status|gender\s*:)", re.I)
TITLE_HEADING = re.compile(r"^\s*#*\s*(resume|résumé|curriculum vitae|cv)\s*$", re.I)
NUMERIC_DATE = re.compile(r"\b\d{1,2}/\d{2,4}\b")
LONG_MONTH = re.compile(r"\b(January|February|March|April|June|July|August|September|October"
                        r"|November|December)\s+\d{4}\b")
FIRST_PERSON = re.compile(r"\b(I|my|me)\b")
MAX_BULLET = 110  # ponytail: char count approximates "one line"; real width depends on font


def lint_resume(lines, _):
    issues = []
    for n, line in enumerate(lines, 1):
        if TITLE_HEADING.match(line):
            issues.append(("ERROR", n, "Heading says Resume/CV. Use your name as the heading."))
        if PERSONAL.search(line):
            issues.append(("ERROR", n, "Personal detail (DOB, gender, marital status). Remove it."))
        if REFEREES.search(line):
            issues.append(("ERROR", n, "Referees do not go in a resume. Remove this."))
        if NUMERIC_DATE.search(line) or LONG_MONTH.search(line):
            issues.append(("WARN", n, "Date format. Use 'Mon YYYY', e.g. 'Mar 2019'."))
        m = BULLET.match(line)
        if not m:
            continue
        bullet = m.group(1)
        if bullet.lower().startswith(WEAK_OPENERS):
            issues.append(("ERROR", n, f"Weak or negative opener: '{bullet[:30]}'. Start with an action verb."))
        if FIRST_PERSON.search(bullet):
            issues.append(("WARN", n, "First person (I/my/me). Drop it."))
        if len(bullet) > MAX_BULLET:
            issues.append(("WARN", n, f"Bullet is {len(bullet)} chars. Aim for one line."))
    return issues


# ---------- cover letter ----------
TO_WHOM = re.compile(r"to whom it may concern", re.I)
APOLOGY = re.compile(r"\b((while|although|though) I (don't|do not|lack|have limited|have little)"
                     r"|limited (work |professional )?experience|I (don't|do not) have)\b", re.I)
FILLERS = re.compile(r"^(Most recently|In addition to|However)\b", re.I)
ATTACHED = re.compile(r"\b(attached (is|are) my|please find (attached|enclosed)|my (resume|cv) is (attached|enclosed)"
                      r"|enclosed is my|I have attached)\b", re.I)
SALARY = re.compile(r"\bsalary\b", re.I)
GREETING = re.compile(r"^\s*Dear\s+(.+?),?\s*$", re.I)
SIGNOFF = re.compile(r"^\s*Yours\s+(sincerely|faithfully)\b", re.I)
GENERIC = re.compile(r"\b(sir|madam|hiring|recruitment|team|manager|hr)\b", re.I)
TITLED = re.compile(r"^(Mr|Ms|Mrs|Miss|Mx|Dr|Prof)\.?\s+\S", re.I)
LINE_CHARS = 95       # ponytail: ~chars per line at 11pt Calibri, A4, 2.54cm margins
MAX_WORDS_LETTER = 450  # ponytail: word count approximates "one page"


def lint_cover(lines, _):
    issues = []
    greeting = signoff = None
    for n, line in enumerate(lines, 1):
        if TO_WHOM.search(line):
            issues.append(("ERROR", n, "'To whom it may concern'. Use a name, or 'Dear Hiring Manager'."))
        if APOLOGY.search(line):
            issues.append(("ERROR", n, "Apologetic phrasing. Describe what you have, with confidence."))
        if ATTACHED.search(line):
            issues.append(("WARN", n, "No need to say your resume is attached."))
        if SALARY.search(line) and "negotiable" not in line.lower():
            issues.append(("ERROR", n, "Salary mentioned. Leave it out, or say it is negotiable if the ad asks."))
        if REFEREES.search(line):
            issues.append(("ERROR", n, "Referees do not go in a cover letter. Remove this."))
        if m := GREETING.match(line):
            greeting = (n, m.group(1).strip())
        if m := SIGNOFF.match(line):
            signoff = (n, m.group(1).lower())
    for n, text in blocks(lines):
        if FILLERS.match(text):
            issues.append(("WARN", n, f"Filler opener '{FILLERS.match(text).group(1)}'. Cut it."))
        if len(text) > 6 * LINE_CHARS:
            issues.append(("WARN", n, f"Paragraph is about {len(text) // LINE_CHARS + 1} lines. Keep to 6 or fewer."))
    words = sum(len(l.split()) for l in lines)
    if words > MAX_WORDS_LETTER:
        issues.append(("WARN", 0, f"{words} words. Aim for 300-400 so it fits one page."))
    if not any(re.match(r"^\s*\**\s*Re:", l) for l in lines):
        issues.append(("WARN", 0, "No 'Re: <Position> – <Company>' line. Add one unless this is speculative."))
    if not greeting:
        issues.append(("ERROR", 0, "No 'Dear ...,' greeting."))
    if not signoff:
        issues.append(("ERROR", 0, "No 'Yours sincerely' or 'Yours faithfully' sign-off."))
    if greeting and signoff:
        generic = GENERIC.search(greeting[1]) and not TITLED.match(greeting[1])
        want = "faithfully" if generic else "sincerely"
        if signoff[1] != want:
            issues.append(("ERROR", signoff[0],
                           f"'Dear {greeting[1]}' needs 'Yours {want}', not 'Yours {signoff[1]}'."))
    return issues


# ---------- selection criteria ----------
PASSIVE = re.compile(r"\b(had to|was assigned to|were assigned to|was required to|were required to)\b", re.I)
ABSOLUTE = re.compile(r"\b(always|often|every)\b", re.I)


def lint_criteria(lines, words_range):
    issues = []
    lo, hi = words_range
    sections, current = [], None
    for n, line in enumerate(lines, 1):
        if line.startswith("## "):
            current = [n, line[3:].strip(), []]
            sections.append(current)
        elif current is not None and not line.startswith("#"):
            current[2].append(line)
        if m := PASSIVE.search(line):
            issues.append(("WARN", n, f"Passive phrasing '{m.group(1)}'. Say what you did."))
        if m := ABSOLUTE.search(line):
            issues.append(("WARN", n, f"'{m.group(1)}' reduces credibility. Use a specific example or number."))
    if not sections:
        issues.append(("ERROR", 0, "No criteria found. Use each criterion as a '## ' heading."))
    for n, title, body in sections:
        text = " ".join(body)
        count = len(text.split())
        if not lo <= count <= hi:
            issues.append(("WARN", n, f"'{title[:40]}' has {count} words. Aim for {lo}-{hi}."))
        if not re.search(r"\d", text):
            issues.append(("WARN", n, f"'{title[:40]}' has no numbers. Quantify the result."))
    return issues


CHECKS = {"resume": lint_resume, "cover": lint_cover, "criteria": lint_criteria}


def lint(text, doc_type, spell="au", words_range=(250, 350), keywords=None):
    lines = text.splitlines()
    issues = CHECKS[doc_type](lines, words_range)
    if spell == "au":
        issues += spelling(lines)
    if keywords:
        issues += keyword_coverage(text, keywords)
    return issues


def _test():
    def kinds(issues):
        return {msg.split()[0].strip("'") for _, _, msg in issues}

    bad_resume = ("# Resume\nDate of birth: 1 Jan 2000\n- Responsible for the website\n- I built my app\n"
                  "March 2019\n## Referees\nContact details available upon request\n")
    k = kinds(lint(bad_resume, "resume"))
    assert {"Heading", "Personal", "Weak", "First", "Date", "Referees"} <= k, k
    good_resume = ("# Carrie Gale\nlinkedin.com/in/carrie | github.com/carrie\n"
                   "- Built a Next.js dashboard used by 40 staff\n- Wrote API references for 12 endpoints\n"
                   "- Optimised image loading, cutting page weight by 30%\nMar 2019 – Oct 2019\n")
    assert lint(good_resume, "resume") == [], lint(good_resume, "resume")

    bad_cover = ("To whom it may concern\n\nDear Hiring Manager,\n\n"
                 "Although I have limited experience, I can learn. My salary expectation is high.\n\n"
                 "However, I organized events. Please find attached my resume.\n\nYours sincerely,\n\nCarrie\n")
    k = kinds(lint(bad_cover, "cover"))
    assert {"To", "Apologetic", "Salary", "Filler", "No", "US", "Dear"} <= k, k
    good_cover = ("# Carrie Gale\n\n**Re: Graduate Engineer – Acme**\n\nDear Ms Roberts,\n\n"
                  "I organised 4 meetups for 120 developers.\n\nYours sincerely,\n\nCarrie Gale\n")
    assert lint(good_cover, "cover") == [], lint(good_cover, "cover")
    assert not lint(good_cover.replace("Ms Roberts", "Hiring Manager").replace("sincerely", "faithfully"), "cover")

    bad_sc = "# Carrie – Officer\n\n## Teamwork\n\nI was required to always help.\n"
    k = kinds(lint(bad_sc, "criteria"))
    assert {"Passive", "always", "Teamwork"} <= k, k
    good_sc = "# Carrie – Officer\n\n## Teamwork\n\n" + "I led 4 developers to ship a feature. " * 40
    assert lint(good_sc, "criteria") == [], lint(good_sc, "criteria")

    criteria = ("# Grad – Acme\n\n## Keywords (exact wording, most frequent first)\n"
                "- React (4)\n- CI/CD — mentioned twice\n- C++\n- stakeholder management\n\n"
                "## Gaps\n- not a keyword\n")
    kws = keywords_from(criteria)
    assert kws == ["React", "CI/CD", "C++", "stakeholder management"], kws
    issues = lint(good_resume.replace("Next.js", "React and C++"), "resume", keywords=kws)
    assert len(issues) == 1 and "2/4" in issues[0][2] and "CI/CD, stakeholder management" in issues[0][2], issues
    assert lint("- Reactive UI", "resume", keywords=["React"]), "partial word must not match"
    print("ok")


def main():
    if sys.argv[1:] == ["--test"]:
        _test()
        return 0
    p = argparse.ArgumentParser(description="Lint a job application document.")
    p.add_argument("--type", required=True, choices=CHECKS)
    p.add_argument("--spelling", default="au", choices=["au", "us"])
    p.add_argument("--words", default="250-350", help="criteria word range per criterion, e.g. 250-350")
    p.add_argument("--keywords", metavar="CRITERIA_MD", help="check coverage of the keywords in criteria.md")
    p.add_argument("file")
    a = p.parse_args()
    lo, hi = (int(x) for x in a.words.split("-"))
    kws = None
    if a.keywords:
        with open(a.keywords, encoding="utf-8") as f:
            kws = keywords_from(f.read())
    with open(a.file, encoding="utf-8") as f:
        results = lint(f.read(), a.type, a.spelling, (lo, hi), kws)
    for level, n, msg in results:
        print(f"{level} line {n}: {msg}" if n else f"{level}: {msg}")
    if not results:
        print("No mechanical issues found. Now run the manual checklist.")
    return 1 if any(level == "ERROR" for level, _, _ in results) else 0


if __name__ == "__main__":
    sys.exit(main())
