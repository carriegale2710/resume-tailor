---
name: interview-prep
description: Prepare for an interview from an application's criteria, research and the story bank - likely questions with matched STAR stories, honest answers for gaps, company facts to know, and questions to ask. Use when the user gets an interview, or asks to practise for one.
---

# Interview prep

Input: `criteria.md`, `research.md`, the documents sent (`resume.md`, `cover-letter.md`, `selection-criteria.md`), `master/stories.md`, and any interview details from the user.
Output: `applications/<company>-<role>/interview-prep.md`.

Ask once: "What do you know about the interview? Format, length, who is on the panel, any technical test?"

## Steps

1. **Likely questions.** For each vital criterion, write 1-2 behavioural questions ("Tell me about a time you...") and, for `can` criteria, 1 technical question. Add the usual openers: "Tell me about yourself", "Why this role?", "Why us?", "What do you know about us?", "Where do you see yourself in 5 years?"
2. **Match a story.** For each question, pick the best story from `stories.md`. Prefer `Status: ready` stories; flag any `draft` story used. Use each story at most twice. If no story fits, run the gap interview (`master-resume`, `references/gap-interview.md`) and add the new story to `stories.md` first.
3. **Answer outlines.** Give each story as 4 short STAR lines, not a script. The user says it in their own words. Action is the longest part, and is what the user did, not the team. Aim for 90 seconds to 2 minutes per answer.
4. **Gaps.** For each `gap` in `criteria.md`, outline an honest answer: what they have that is closest, and how they would learn the rest. Never suggest claiming the skill.
5. **Know what you sent.** List every claim in the sent documents that the panel may probe, with the story behind it.
6. **Company facts.** Pick 5-6 facts from `research.md` to know cold, with their sources.
7. **Questions to ask.** Write 3-5 questions based on the research hooks. Match them to the panel: for the hiring manager, what success looks like at 90 days and how performance is measured; for a team member, what a typical week looks like. Open-ended questions only, no yes/no. Do not ask anything the website answers, and do not ask about salary first.
8. **Technical topics.** For tech roles, list the tools and concepts in `criteria.md` keywords to revise, ordered by how often the ad mentions them. Prepare to discuss how you approach code reviews, and how you balance technical debt against new features.
9. **Hard questions.** Outline an answer for each of these, from the user's real experience:
   - **"What is your greatest weakness?"** A real weakness that is not a vital criterion, what the user does about it, and evidence it is improving. No disguised strengths ("I work too hard").
   - **"Tell me about a time you failed."** A real failure from `stories.md`, the user's own part in it, what they learned, and when they applied it since. End on the later success.
   - **"Why are you leaving?" or "Why now?"** Forward-looking: what this role offers that the current one does not. No complaints about past employers.
   - **"Explain this gap."** For any gap of 3 months or more in the resume dates: what the user did, briefly, and why they are ready now.
   - **Salary.** Say it is negotiable and ask for the budgeted range. If pressed, give a range the user has researched. Never supply a figure yourself.

## Format

```markdown
# Interview prep — <Role>, <Company>

## Interview details
- Date and time:
- Format: <phone | video | in person | panel | technical>
- Panel:
- Logistics: <route and travel time | video link and tech check>

## Tell me about yourself
<4-5 lines, about 2 minutes spoken: who you are, what you bring that matches the vital criteria, why this role>

## Likely questions
### <Criterion>
**Q:** <question>
**Story:** <story title from stories.md>
- S:
- T:
- A:
- R:

## Gaps and honest answers
| Criterion | What you have | How you would close it |
|---|---|---|

## Claims they may probe
| Claim (document) | Story behind it |
|---|---|

## Hard questions
### <Question>
- <outline>

## Company facts to know
1. <fact> — <source>

## Questions to ask them
1.

## Technical topics to revise
```

## Rules

- Every story and claim must already exist in `master/master-resume.md` or `master/stories.md`.
- Answers are outlines. Do not write word-for-word scripts.
- Offer a practice round: ask one question at a time, then give feedback on structure (did it follow STAR, end with a result, and link back to the role).
- Remind the user to send a short thank-you email within a day of the interview.

The hard questions are adapted from `interview-prep-generator` in [ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills), MIT License, Copyright (c) 2026 Resume Skills.
