# Master template: fill-in guide

Rename this folder to `master/` (root README, Setup step 1), then fill each file below. Delete this README when done.

## Rules

- Facts only. Never invent a skill, tool, date, title, metric or outcome.
- Unknown = `TODO`. Never guess.
- Leave every `${...}` placeholder as written. `.env` fills them at docx build time.
- Write raw facts in your own words. Tailoring polishes them later.
- Tag each bullet with 1-3 tags from `tags.md`.

## Fill order

| # | File | What to do |
|---|---|---|
| 1 | `master-resume.md` | Sections 0-6: replace each `TODO`. Delete blocks you do not need, copy blocks to add more. |
| 2 | `metrics-log.csv` | One row per number used in a bullet. Type: `Evidenced`, `Self-reported`, `Estimate` or `Projection`. Unproven types need a "Safe wording". |
| 3 | `skills-inventory.csv` | Fill each category. Strong / Proficient only if a master bullet evidences it; otherwise Weak / exposure only. |
| 4 | `projects-inventory.csv` | One row per project (header row lists the columns). Source for portfolio and case studies. |
| 5 | `narrative-notes.md` | Private story, differentiators, objections, target roles. Never goes on a resume. |
| 6 | `tags.md` | Keep or edit tag names. Must match tags used in `master-resume.md`. |
| 7 | `case-studies/` | Copy `_template.md` per project. Optional. |
| 8 | `archive.md` | Leave. Move retired bullets here instead of deleting. |

## Shortcut

Run the `resume-import` skill to fill these files from your existing resumes. It confirms each edit before writing.
