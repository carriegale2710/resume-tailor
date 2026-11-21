---
name: application-form
description: Write answers for the questions in an online application form (graduate program portals, Workday, Greenhouse, government forms), sized to each field's limit and ready to paste. Use when the employer applies through a form with written questions, alongside or instead of a cover letter.
---

# Application form answers

Input: the form's questions with any word or character limits (pasted, a screenshot, or a URL), `criteria.md`, `research.md`, `master/master-resume.md`, `master/stories.md`.
Output: `applications/<company>-<role>/form-answers.md`.

A form answer is not a cover letter squeezed into a box. Answer exactly what the field asks, then stop.

## Question types

| Type | Examples | Structure | Length |
|---|---|---|---|
| **Experience with a tool or domain** | "How many years of experience with React?" "Describe your backend experience." | Skill, honest duration, then one sentence on where you used it. One project per sentence. | 1-4 sentences |
| **Why us, why this role** | "Why do you want to join our graduate program?" | One specific fact from `research.md` hooks, how it links to your work or motivation, then why this field. Do not repeat the ad back. | Under 150 words |
| **Work samples** | "Link to work you are proud of." | One line per project: name, link, what it is, one proof point. Most relevant first. Use `portfolio.md` if it exists. Prefer a live link over a repo. Add real usage numbers once, if recorded. | List, no prose |
| **Technical skills or ratings** | "Rate your Python." "Which frameworks have you used most?" | Main skill, duration, what you built with it. Then the next skill. Rate honestly: interviews test ratings. For a skill not used recently, say when you last used it. | 2-4 sentences |
| **About you** | "Tell us about yourself." | Current study or role, the most relevant experience, one relevant project, then what you want next and why this employer. End on what you want next. Facts, not traits. | 100-200 words |
| **Behavioural** | "Describe a time you solved a hard problem." | STAR without labels: context, what you did, the result. Use a story from `stories.md`. Name the project, the tech and the team size. End on the result. | 150-250 words |
| **Opinion** | "Which technology will matter most in 5 years?" | Pick one or two things, commit to a view, and ground it in something you have done or studied. | 100-150 words |

## Limits

- Use the form's limit when it gives one. Count characters when the limit is in characters; spaces count.
- With no limit, use the lengths above. Shorter is better: recruiters skim.
- Report the count under each answer.

## Fields to leave for the user

Do not draft answers for these. List them in a "You fill in" section:

- Work rights, visa and citizenship
- Referees (only enter people who have agreed)
- Demographic and diversity questions
- Declarations and consent
- Salary expectations, unless the user asks. Then say it is negotiable, or use a range the user has researched. Never supply a figure yourself.

## Format

````markdown
# Form answers — <Role>, <Company>

## <Question, copied exactly>
Limit: <200 words | 1,000 characters | none>

```
<answer>
```
<count> words / <count> characters

## You fill in
- <field>: <why it is the user's call>
````

Each answer goes in a plain code block so it pastes cleanly.

## Rules

- Every fact must exist in `master/master-resume.md` or `master/stories.md`. Run the gap interview (`master-resume`) if a question needs evidence that is not recorded.
- Use a different story for each behavioural question where possible. If the form and a selection criteria response both need stories, do not reuse a main story.
- Use `criteria.md` keywords in the ad's exact wording where they fit naturally.
- Say gaps plainly ("The role asks for 2 years; I have 1 year of production work, plus...") without apologising.
- No trait claims ("I'm a fast learner", "passionate about"). Show it with the work.
- Use Australian English unless `criteria.md` sets `Spelling: US`.

Adapted from `application-form-filler` in [ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills), MIT License, Copyright (c) 2026 Resume Skills.
