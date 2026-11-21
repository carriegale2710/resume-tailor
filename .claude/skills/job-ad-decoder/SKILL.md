---
name: job-ad-decoder
description: Turn a job ad or position description into application facts, the vital 3-5 selection criteria, can/will/fit tags, evidence levels and keywords. Use before writing any application document.
---

# Job ad decoder

Input: the job ad or position description (pasted, a file, or a URL to fetch), plus `research.md` if it exists.
Output: `applications/<company>-<role>/criteria.md` in the format below.

## Steps

1. **Facts.** Record role, company, contact name and title, reference number, closing date, how to apply, and whether a separate selection criteria response is required (and any word limit). Record the interview stages if the ad lists them. Set spelling to AU unless the employer is US-based; confirm with the user if unsure. If the ad is vague and lists a contact, suggest 1-2 specific questions the user could ask them before writing.
2. **What they say they want.** Extract every explicit requirement. Split must-have ("required", "essential", "you will have") from nice-to-have ("desirable", "ideally", "bonus"). A requirement repeated 3 or more times is must-have even if it is not labelled.
3. **What else they seek.** Infer criteria from the duties list and the company's values. Check the transferable skills graduate employers rate highly: communication, teamwork, interpersonal skills, initiative and enterprise, resilience, emotional intelligence, planning and organising, understanding of the organisation, self-management, leadership.
4. **The vital 3-5.** Pick the criteria most likely to decide shortlisting. These drive the resume's first page and the cover letter's middle paragraphs.
5. **Tag** each criterion: `can` (skills, knowledge), `will` (motivation, attitude) or `fit` (values, attributes).
6. **Evidence level.** Read the wording against `references/criteria-glossary.md`. "Proven record" needs documented outcomes; "awareness of" needs only familiarity.
7. **Keywords.** Collect tools, methods, domain terms, certifications, licences and soft skills in the ad's exact wording, most frequent first.
8. **Map** each criterion to evidence in `master/master-resume.md` and `master/stories.md`. Mark it `strong`, `weak` or `gap`.
9. **Gap interview.** For each vital criterion marked `weak` or `gap`, run the gap interview in `master-resume` (`references/gap-interview.md`). Update the evidence level afterwards.
10. **Gap options.** For each criterion still marked `gap`, give the user these options and record their choice:
    - **Cover letter:** say how they are closing the gap (a course, a project, how fast they learned something similar)
    - **Leave it out:** drop the resume slot, and give the space to a stronger criterion
    - **Weak match:** use the best `weak` evidence, worded honestly (see `achievement-statements`, `references/reframing.md`)
    - **Accept:** apply anyway, and prepare an honest interview answer
11. **Risks.** List anything a reader might hold against the user for this role: overqualified, a career change, a date gap, missing work rights, a required clearance or citizenship, a required degree, years of experience well below the ask, location. For each, note how the application answers it. Use the terminology map in `research.md`, if it exists, for the organisation language.

## Output format

```markdown
# <Role> — <Company>

## Facts

- Contact: <title and name, position> | none found
- Reference:
- Closing date: <D Month YYYY>
- Apply via: <portal | email to ...>
- Selection criteria response: required (<word limit>) | not required
- Spelling: AU | US
- Letter type: job-ad | speculative | follow-up | referral (<referrer>)
- Process: <interview stages, if listed>

## Vital criteria

| #   | Criterion | Tag | Evidence level | Best evidence | Fit |
| --- | --------- | --- | -------------- | ------------- | --- |

## All criteria

### Must have

| Criterion | Tag | Keywords | Evidence | Fit |
| --------- | --- | -------- | -------- | --- |

### Nice to have

| Criterion | Tag | Keywords | Evidence | Fit |
| --------- | --- | -------- | -------- | --- |

## Keywords (exact wording, most frequent first)

- <keyword> (<times mentioned>)

## Organisation language

## Gaps

| Criterion | Interviewed | Option chosen |
| --------- | ----------- | ------------- |

## Risks

| Risk | How the application answers it |
| ---- | ------------------------------ |
```

## Rules

- Use the ad's wording for keywords. Do not substitute synonyms.
- Do not mark a `gap` final until the gap interview has run. The user chooses the gap option, not you.
- If the closing date is 3 days away or less, say so first.
- Do not advise whether to apply. Report fit only.
