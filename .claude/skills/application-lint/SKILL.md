---
name: application-lint
description: Check a resume, cover letter or selection criteria response against the UNSW checklists, and report errors and warnings. Use as the final step before exporting or sending any application document.
---

# Application lint

## Step 1: run the script

```
python3 scripts/lint.py --type resume|cover|criteria <file.md> [--spelling us] [--words 250-350] [--keywords criteria.md]
```

`scripts/` is relative to this skill's base directory, not the user's workspace.

- Always pass `--keywords applications/<company>-<role>/criteria.md` for the resume. It reports which of the ad's keywords are missing. Add only the ones that are true for the user.
- Pass `--spelling us` only when `criteria.md` says `Spelling: US`.
- For criteria responses, pass the employer's word limit as `--words`, e.g. `--words 200-300`.

Fix every `ERROR`. Review each `WARN` with judgement: the script approximates page length and line length from character counts.

What it checks:

| Type | Checks |
|---|---|
| all | US spelling (-ize, -or, -er words); with `--keywords`, missing keywords from `criteria.md` (exact wording, whole words) |
| resume | "Resume" as heading, personal details, referees, date format, weak openers, first person, long bullets |
| cover | "To whom it may concern", apologetic phrasing, fillers, "resume attached", salary, referees, greeting and sign-off match, paragraphs over 6 lines, over 450 words, missing "Re:" line |
| criteria | missing `##` criteria, words per criterion, no numbers, passive phrasing, "always/often/every" |

## Step 2: manual checklist

The script cannot check these. Report each as pass or fail.

### Resume

- [ ] Every vital criterion in `criteria.md` has evidence, mostly on page 1
- [ ] Keywords appear in the ad's wording, not synonyms ("stakeholder management", not "managing stakeholders")
- [ ] Name is the heading; phone, professional email, hyperlinked LinkedIn; no date of birth, gender, photo or marital status
- [ ] Most relevant sections first; most recent first within each section
- [ ] Profile uses summary statements; experience uses achievement statements
- [ ] Past tense for past roles; current roles consistent within the role
- [ ] No referees section
- [ ] Single column; no tables, text boxes, images or icons; contact details as plain text
- [ ] Sent in the format the ad asks for (.docx or PDF); PDF text is selectable

### Cover letter

- [ ] One page, generous margins, no long paragraphs
- [ ] Contact details, date, recipient's correct title and name, position and address
- [ ] Opening sparks interest and shows research beyond the company website
- [ ] Explains motivation for the role, organisation or industry
- [ ] Middle covers the 3-5 vital criteria only, one theme per paragraph, with specific examples
- [ ] Closing summarises strengths, thanks the reader and asks for an interview
- [ ] Genuine enthusiasm; direct, succinct style suited to the industry
- [ ] Not a generic letter with the company name swapped
- [ ] Same font and size as the resume

### Selection criteria

- [ ] Starts with name and position title
- [ ] Every criterion copied exactly as a heading, and every one answered
- [ ] Each response has overview, STAR evidence and a link to the role
- [ ] Evidence matches the wording's level (see `../job-ad-decoder/references/criteria-glossary.md`)
- [ ] No main story used for two criteria
- [ ] Same font and size as the resume

### All documents

- [ ] Spelling, punctuation and grammar checked; read it aloud. A single error can cost the interview.
- [ ] Positive, motivated tone
- [ ] Submit before the closing date, not on it

## Output

List failures first, each with the line and the fix. Then list passes in one line.
