---
name: master-resume
description: Build or update the user's master resume, selling points and STAR story bank - the source of truth for every application. Use before tailoring any document, or when the user mentions new experience.
---

# Master resume and stories

Two files hold everything about the user. Every application is cut from them. Keep them current so the user can apply quickly when an opportunity appears.

- `master/master-resume.md` - start from `templates/master-resume-template.md`
- `master/stories.md` - start from `templates/stories-template.md`

## Building the master resume

Interview the user one section at a time: contact, education, experience, projects, skills, extras, then selling points.

For each role or project, capture:

- Descriptive title ("Front-end Developer (Contract)", not "Contractor")
- Organisation, location, start and end month/year
- Every task, in their own words
- For each task: the outcome or purpose, and any number (users, %, $, time saved, team size, count)
- Tools and technologies, with proficiency (beginner, proficient, advanced) and where used
- Which kinds of roles it supports

Ask "what happened as a result?" and "how many or how much?" for each task, then "how was it measured, and where is the proof?" Record the source (PR, CI run, analytics, email, transcript, or "recollection"). Record "no metric" when there is none. Never guess.

Ask about any gap of 3 months or more between dates, and record what the user did in `## Date gaps`.

## Selling points, motivations and values

Ask the user to self-assess what differentiates them: grades, work experience, degree, extracurricular, clubs, volunteering, personal development, certifications, skills, international experience, awards, motivations. Record:

- **Selling points:** their top 5-8 strengths, each with where it is proven
- **Motivations:** what kinds of work, products and teams they want, and why
- **Values:** what they look for in an organisation

These feed the cover letter's "why them" and "why you" paragraphs.

## Building the story bank

For each significant achievement, write one STAR story in `stories.md`:

- **Situation** - where you were, and the context
- **Task** - the problem or challenge
- **Action** - what you did (first person, active verbs)
- **Result** - how effective it was, quantified where possible
- **Shows** - the skills and criteria it proves (for example teamwork, problem solving, leadership)

Aim for 6-10 stories covering different skills. Draw from work, projects, study and volunteering.

## Gap interview

When a job ad needs evidence that is not recorded here, follow `references/gap-interview.md`. It finds experience the user has but has not written down, and adds it here before any application uses it.

## Reviewing the master

When asked to review or improve the master, list its gaps, most blocking first:

- Blank fields; tasks marked "no metric" that matter for the target roles
- Estimates with no method recorded
- Skills with no proficiency, or no task that proves them
- Selling points with no proof
- Fewer than 6 stories, or a key skill with no story
- Dates or titles that differ from `master/linkedin.md`
- Work from the last 6 months not yet recorded

Show the top 5. Let the user pick. Run `references/gap-interview.md` on each.

## Rules

- Show each proposed edit as section, old, new. Write only edits the user confirms.
- Mark confidential or NDA work `NDA`. Applications describe it generically, with no client names or figures.
- Record raw facts, not polished bullets. Polishing happens per application.
- Keep old and minor items here even if they rarely get used.
- Never record date of birth, gender, photo, marital status, or political or religious affiliation.
- Do not record referees. They never go in an application document.
- When the user mentions a new achievement in any conversation, offer to add it here.
