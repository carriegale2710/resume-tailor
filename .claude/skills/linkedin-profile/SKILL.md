---
name: linkedin-profile
description: Write or refresh the user's LinkedIn headline, About section, experience entries, skills and Featured items from the master resume, so recruiters can find them. Use when the user asks about LinkedIn, or after the master resume changes a lot.
---

# LinkedIn profile

Input: `master/master-resume.md`, `master/stories.md`, `master/portfolio-index.md` if it exists, and the kinds of roles the user is targeting.
Output: `master/linkedin.md`, with one section per profile section, ready to paste.

LinkedIn is not tailored per application. Write it for the kind of role the user wants, using the words those ads use most, and in the profiles of people already in that role.

## Sections

**Headline** (220 characters max). Formula: role or target role | key skills | what you deliver.

- Weak: "Student at UNSW" or "Looking for opportunities"
- Strong: "Graduate Software Engineer | React, TypeScript, Node.js | Building accessible web apps"

**About** (2,600 characters max; aim for 1,000-2,000).

1. A first line that works on its own. Only about the first 300 characters show before "see more", so front-load them.
2. Who you are and what you do.
3. 2-3 achievements, each with where it happened.
4. What you want next.
5. A line of key skills, using the target ads' wording.
6. How to contact you.

Write in first person. LinkedIn is the one place where that is normal.

**Experience.** For each role: title, organisation, dates, location, a 1-2 sentence description, then 3-5 achievement statements (`achievement-statements`). Use the master resume's facts, not any one tailored resume.

**Education, Licences & certifications, Volunteer experience.** Fill these from the master resume. For graduates, Education carries as much weight as Experience: add grades if strong, relevant coursework and projects.

**Skills.** Pick the 3 to feature: the skills most common in the target ads that the user can prove. Then list the rest, tools first, ordered by relevance.

**Featured.** 2-4 items: the strongest portfolio case studies, repos or articles. Use the portfolio index.

**Recommendations.** Suggest 2-3 people to ask: a supervisor, a lecturer, a project teammate. For each, give them specific talking points (one project and one skill) so they can write something concrete.

**Custom URL.** Suggest `linkedin.com/in/<firstname-lastname>` if the user has a default URL with numbers. The resume links to it.

## Format

```markdown
# LinkedIn profile — <date>

## Headline

<text> (<n>/220)

## About

<text> (<n>/2,600)

## Experience

### <Title> — <Organisation>

<description>
- <bullet>

## Skills

Featured: <1>, <2>, <3>
Others: <list>

## Featured

1. <title> — <link> — <one-line caption>

## Settings to check

- Custom URL
- "Open to work": visible to recruiters only, if the user is currently employed. Set job titles, locations, start date and job types (graduate, internship, full-time)
- Photo: a professional headshot, face filling most of the frame, good lighting
```

## Rules

- Every fact must exist in the master resume or story bank.
- Keep dates, titles and employers identical to the resume. Recruiters compare them.
- Use Australian English unless the user says otherwise.
- No salary, referees or personal details beyond what the resume shows.
- When revising, show only the changed sections.

Adapted from `linkedin-profile-optimizer` in [ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills), MIT License, Copyright (c) 2026 Resume Skills.
