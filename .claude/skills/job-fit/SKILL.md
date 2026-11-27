---
name: job-fit
description: Quick triage before tailoring - mark each must-have in applications/<folder>/job-description.md as met, partly or not met against the master, and give an apply, stretch or skip verdict. Use right after tracker-intake, before resume-orchestrator, to drop poor-fit roles early.
---

# Job fit

Inputs: `applications/<folder>/job-description.md`, `master/master-resume.md`, `master/skills-inventory.csv`. Never read `.env`.
Output: `applications/<folder>/fit.md` in the format below, and the verdict in chat.

Keep it fast: no gap interview, no research, no drafting. `job-ad-decoder` does the full analysis later.

## Steps

1. List every must-have the posting marks "required", "essential" or "you will have". Repetition alone does not make a must-have; skip anything marked preferred, desirable, optional or nice to have. Merge only true near-duplicates. Count every must-have for the verdict; show at most 10 in the table, most important first.
2. For each, find the strongest master bullet that proves it:
   - **Met:** a master bullet shows it directly.
   - **Partly:** related or weaker evidence in a master bullet (adjacent tool, smaller scope).
   - **Not met:** no master evidence. A skill only in the inventory with no bullet counts as not met.
3. Flag hard blockers separately: required degree, licence, clearance, citizenship or work rights, years of experience well above the master, location. Read work rights as unknown; never ask for or write the real value.
4. Verdict (check in this order; the first that holds wins):
   - **Apply:** all blockers clear and at least 70% of must-haves met.
   - **Stretch:** no blockers clear-fail, and met + partly cover at least half.
   - **Skip:** a blocker clearly fails, or fewer than half are met or partly met.
   The user decides. The verdict is a recommendation only.
5. Report the verdict first, then the top 1-2 reasons.

## Output format

```markdown
# Fit: <Role> — <Company>

**Verdict:** apply | stretch | skip — <one-line reason>

| Must-have | Fit | Proof (master bullet, short) |
| --------- | --- | ---------------------------- |

## Blockers

- <blocker>: clear | fails | unknown

## Next

- apply/stretch: run `resume-orchestrator`
- skip: note the reason in the tracker `notes` column (user's choice)
```

## Rules

- Evidence comes only from `master/`. Never invent or stretch a match; when unsure, mark `partly`.
- Never copy master section 6, `metrics-log.csv`, `narrative-notes.md` or `archive.md` content into `fit.md`.
- No percentage score in the output. Use counts only (e.g. 5/7 met).
- Do not change tracker status.
