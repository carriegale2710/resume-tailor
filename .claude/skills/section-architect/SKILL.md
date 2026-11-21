---
name: section-architect
description: Decide which resume sections to include, what to call them, what order they go in, what to cut and how to format them, for a specific job. Use after decoding the job ad and before writing bullets.
---

# Section architect

Input: `master/master-resume.md` and `applications/<company>-<role>/criteria.md`.
Output: a section outline with headings, entries under each, and a cut list with reasons.

## Default order: graduate tech roles

Use this unless the role is not technical.

1. Contact details (name is the heading; phone, email, suburb; then LinkedIn, GitHub, portfolio)
2. Profile
3. Technical skills (grouped: languages, frameworks and libraries, databases and cloud, tools and practices; within each group, the ad's keywords first, in its wording)
4. Education
5. Projects
6. Relevant experience
7. Additional experience
8. Programs & activities (outside uni: bootcamps, hackathons, certifications, open source, meetups)
9. Extracurricular involvement (uni clubs and societies)
10. Interests (optional)

## General order: non-technical roles

Contact, profile, education, relevant experience, relevant projects, additional experience, extracurricular, programs & activities, technical skills, professional memberships, interests.

## Moving sections

The most relevant content goes first, and page 1 matters most. Move a section up when it is the strongest evidence for the vital criteria. Put Projects above experience when paid experience in the field is thin.

Never add a referees section or "references available upon request".

## Headings

Split experience by relevance, not by type of work:

- "Relevant experience" for roles that match the criteria
- "Projects" for bootcamp, course, client, hackathon and personal projects that use the role's skills
- "Additional experience" for unrelated roles that still show work skills

Within each section, list the most recent first.

- **Several titles at one employer** (promotion or role change): one `###` per title with its own dates, the same organisation line, most recent first.
- **Freelance or contract work:** one `### <Title> (Freelance) | Mon YYYY – Current` entry, organisation line "Self-employed – clients include A, B", one bullet per client result.

## Cutting

- Review items older than about 5 years. Keep them only if they support a criterion.
- Cut anything that supports no criterion and shows no general work skill.
- List technical skills only if the ad asks for them or they are relevant, and say how proficient you are or where you used them. Leave out soft skills (show them in bullets), assumed basics (Microsoft Office, operating systems) unless the ad names them, outdated tech, skill bars or ratings, and anything the user could not discuss in a technical interview.
- Cut tutorial follow-alongs and trivial demo apps unless the user extended them well beyond the tutorial. Prefer projects with real users, collaborators, merged open-source PRs or hackathon results.
- List spoken languages only if relevant to the role or beyond conversational, with a level: Native, Professional or Conversational.
- Keep a short role if it is relevant. Do not explain short tenure on the resume.
- Include interests only if they show commitment, achievement or fit with the role.
- Leave out political or religious affiliations unless relevant.

## Length

- Graduate resumes average 2 pages. Use 1 page if the ad asks for it.
- 3 pages only for extensive experience or research output.

## Formatting

The `docx-export` script applies these. Check them if the user formats by hand.

- One plain font (Calibri) at 11pt throughout
- Bold for headings, job titles and degree names; no italics or underline
- Title first, organisation on the next line, dates right-aligned as `Mon YYYY – Mon YYYY`
- Descriptive titles ("Front-end Developer Intern", not "Intern")
- Bullets, left-aligned text, white space between sections
- Footer with name and page number
- Single column; no tables, text boxes, icons or images; contact details in the body, not the page header
