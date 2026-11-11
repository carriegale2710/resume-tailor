---
name: portfolio-curator
description: Shortlist the 2-4 portfolio case studies that best prove a role's criteria, with links and one-line mentions for the resume and cover letter, and write or strengthen case studies when the portfolio has none that fit. Use for design, front-end and other roles where a portfolio matters.
---

# Portfolio curator

Inputs: `criteria.md`, `research.md`, `master/portfolio-index.md`.
Output: `applications/<company>-<role>/portfolio.md`.

## Build the index once

If `master/portfolio-index.md` does not exist:
1. Get the portfolio URL from `master/master-resume.md`, or ask the user.
2. Fetch the site and list each case study: title, link, one-line summary, skills and tools shown, outcome.
3. If the site cannot be fetched, ask the user to list their case studies.

Reuse the index for every later application. Update it when the user adds work.

## Shortlist for each application

1. Score each case study against the vital criteria in `criteria.md`, and against the company's products, domain and stack from `research.md`.
2. Pick 2-4 high-impact pieces. Fewer strong pieces beat many weak ones.
3. Show range only when the ad asks for breadth.
4. If a vital criterion has no case study to prove it, but the master resume has a project that would, offer to write one (below).

## Write or strengthen a case study

Use when the user has a project with no case study, or a case study that only shows screens and not thinking.

1. Gather the facts from `master/master-resume.md` and `master/stories.md`. Ask the user for anything the template needs that is not there: the problem, the options they considered, the results.
2. Draft it with `references/case-study-template.md`, emphasising what the target role values.
3. Save it as `master/case-studies/<project-slug>.md`. The user publishes it on their site.
4. Add it to `master/portfolio-index.md` once it is live, with its link.

To strengthen an existing case study, check it against the template's checklist and list what is missing, most important first.

## Format

```markdown
# Portfolio shortlist — <Role>, <Company>

| Rank | Case study | Link | Criteria it proves | Why it fits this company |
|---|---|---|---|---|

## Resume mention
<one line for the contact block, profile or Projects subline>

## Cover letter mention
<one sentence for a middle paragraph, naming the top case study>
```

## Rules

- Never describe work that is not in the portfolio index or master resume. In a new case study, every fact and number must come from the master resume or the user.
- Select by criteria and research, not by what the user likes best.
- Before linking a GitHub repo, check its README says what it does, the stack, how to run it, and has a screenshot or demo link. For team work, it states the user's part. Suggest pinning up to 6 repos most relevant to the target roles.
- If the site lets the user reorder or pin work, suggest which piece to put first for this application.
