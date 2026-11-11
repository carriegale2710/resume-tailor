# MASTER RESUME (source of truth: never submit this directly)

> **Use:** `bash scripts/new-application.sh company-role`, filter bullets by tag, cut to one page (two pages maximum), tick `tailoring-rules/every-resume.md`, export as **.docx**.
> **Rules:** Edit facts here only. Every number needs a row in `master/metrics-log.csv`. Fill every `TODO` before reusing a claim. Swap unproven numbers for the safe wording.

**Tag key:** `fullstack` `backend` `frontend` `qa` `ux` `a11y` `ai-eval` `devops` `product` `leadership` `security` `research` `ecommerce` `startup` `retail` `customer-service`
**Variant key:** **S** = short one-liner, **M** = standard, **Q** = quantified

> TEMPLATE: replace every `TODO`. Copy a block to add another role, project or certification. Delete blocks you do not need. Delete this note when done. See `README.md` in this folder.

---

# Maintenance (private; never on a resume)

## Maintenance checklist

- [ ] Within 1 week of finishing anything: add bullets, tags, and metrics evidence
- [ ] Monthly (10 min): add new work, check links, update demo URLs
- [ ] Quarterly: move stale material to an Archive section
- [ ] Commit after every change (or save a dated copy)
- [ ] Before exporting any tailored CV: follow `tailoring-rules/every-resume.md`

---

## 0. Header and admin facts

Leave the `${...}` placeholders exactly as written. `scripts/build.sh` fills them from `.env` at docx build time.

- Name: ${RESUME_NAME}
- Location: ${RESUME_LOCATION}
- Phone / Email: ${RESUME_PHONE} / ${RESUME_EMAIL}
- LinkedIn / GitHub / Portfolio: ${LINKEDIN_URL} / ${GITHUB_URL} / ${PORTFOLIO_URL}
- Work rights / visa status: ${RESUME_WORKRIGHTS}
- Languages: TODO

### Headline options

One per role family. Format: `Role | Stack`.

- **TODO (family):** TODO Role | TODO stack

### Summary variants

One per role family. 2-3 sentences. Facts from sections 2-5 only. Variant tags are in `tags.md`.

- **TODO (`tag`):** TODO

**Optional add-on lines (one per CV at most):**

- **Interests (`addon-interests`):** TODO

---

## 1. Skills inventory (reference only; not a CV section)

**Main tech stack** (strongest first, not exhaustive): TODO. For full skills inventory list, see `skills-inventory.csv`.

---

## 2. Education & Training

### TODO Institution, TODO Qualification

- TODO City, State | TODO Mon YYYY – Mon YYYY | Major: TODO | Grade: TODO
- `tag` TODO what was studied or built.

### Certifications

#### TODO Issuer, TODO Certification

- TODO Mon YYYY – Mon YYYY | `tag`

---

## 3. Work experience

### TODO Employer, TODO Job title

TODO City, State | TODO Mon YYYY – Mon YYYY | Team size: TODO | Stack/Tools: TODO
Links: TODO

**One-liners:**

- **S:** TODO

**Bullets:** what you did + how + why it mattered. Past tense. Numbers only if in `metrics-log.csv`.

- `tag` TODO
- `tag` TODO

### Earlier roles (`optional: drop unless the application needs them`)

#### TODO Employer, TODO Job title

TODO City, State | TODO Mon YYYY – Mon YYYY

- `tag` TODO

---

## 4. Projects

> **Rule:** no dates or years on projects. Add one only for a work in progress, and only if given here.

### TODO Project name | TODO type

Role: TODO | Team: TODO
Stack: TODO
Live: TODO | Repo: ${GITHUB_URL}/TODO

**One-liners:**

- **S:** TODO

**Bullets:**

- `tag` TODO

> Unfinished? Add a note here, e.g. "Do not describe the project as complete or deployed."

---

## 5. Leadership, programs and activities

> **Graduate roles:** put section 2 plus any programs below together under "Education & Training" directly below the summary.

### TODO Organisation, TODO Role

TODO City, State | TODO Mon YYYY – Mon YYYY

- `leadership` TODO

### Awards

- TODO

---

## 6. Private constraints and evidence (NEVER on a resume)

- **Metrics evidence:** `master/metrics-log.csv`. Every number on a CV needs a row; Estimate, Projection and Self-reported rows use the Safe wording column.
- **Narrative material:** `master/narrative-notes.md` (personal story, differentiators, likely objections, target industries).
- **Retired content and the maintenance checklist:** `master/archive.md`.
- **Applications:** `applications/tracker.csv`.

- **NDA or confidentiality limits:** TODO (what you may and may not name per employer or client)
- **Eligibility-only facts (e.g. WAM):** TODO. Quote only when an application form asks.
- **Date overlaps:** TODO
- **Interview stories (STAR):** TODO. Later stories go in `master/stories.md`.
- **Anything discussable but not publishable:** TODO
- **Third-party evidence (reference letters):** TODO. Use for cover letters and interviews, never as resume adjectives.
- **Do not claim:** TODO (things an older CV says that you cannot back up)

### Conflicts between this master and older CVs (resolve once, then delete this list)

- TODO
