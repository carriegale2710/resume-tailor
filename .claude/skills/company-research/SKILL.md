---
name: company-research
description: Research an organisation before applying - products, recent projects, initiatives, awards, values, culture and tech stack - and find hooks for the cover letter. Use at the start of every application.
---

# Company research

Output: `applications/<company>-<role>/research.md`.

Research shows the employer you understand them, and gives the cover letter a specific "why them". Quoting the company website back to them does not show understanding.

## Sources

1. Web search and fetch: the company site, about and careers pages, engineering or design blog, news and media, annual reports, LinkedIn, GitHub, product pages, award listings.
2. The user's own notes: networking events, information interviews, conversations with staff, things they have used or built with the product. Ask once: "Do you have any notes or contacts at <company>?"

Stop after about 6 searches. Quality beats volume.

## What to collect

- **What they do:** products, services, clients, markets
- **Recent:** projects, launches, initiatives, news and media from the last 12-18 months
- **Awards and achievements**
- **Mission, values, culture**, and corporate social responsibility
- **Tech roles:** tech stack and engineering practices (blog, job ads, GitHub, talks)
- **Graduate program:** structure, rotations, intake dates, if relevant
- **Contact person:** name, title and role from the ad or research
- **Terminology map:** the organisation's own words for common things, for example "squad" for team or "customers" for users, taken from their site, blog and job ads. Bullets and letters use their words.

## Hooks

Finish with 2-4 hooks. A hook is a specific fact that connects to the user's motivations, values or experience in `master/master-resume.md`. For each, write what it is and why it matters to this user.

Illustrative example, for a fictional company:

- Weak hook: "Acme values teamwork."
- Strong hook: "Acme is moving its products onto a shared React design system (engineering blog, March 2026). The user built and documented a component library for a client in 2025."

## Format

```markdown
# <Company> research — <date>

## What they do

## Recent projects and news

## Awards

## Mission, values and culture

## Tech stack and practices

## Graduate program

## Contact person

## Terminology map

| Common term | Their term | Source |
| ----------- | ---------- | ------ |

## Hooks for the cover letter

1. <fact> — why it matters to the user: <link to their motivation or experience>

## Sources

- [Title](URL) — accessed <date>
```

## Rules

- Never invent a fact. Every fact needs a source URL, or "user note".
- Flag anything older than 2 years as possibly stale.
- Put hooks in your own words. Show what a fact means, not just that it exists.
- If the company is too small to research, say so and rely on the user's notes and the ad.
