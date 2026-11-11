---
name: cover-letter
description: Write a one-page tailored cover letter (job ad, speculative, follow-up or referral) and the short email that goes with an emailed application. Use for every application unless the employer says not to send one.
---

# Cover letter

A cover letter is a short argument for hiring the user, not a longer version of the resume. It answers can you do the job, will you do the job, and will you fit in. It is the main place to show motivation - why this company, why this role - which is often what decides who gets an interview.

Specific evidence beats claims. One real project with a real engineering decision says more than "passionate problem-solver".

Inputs: `criteria.md`, `research.md`, `resume.md`, `master/master-resume.md`, `master/stories.md`.
Outputs: `cover-letter.md` (format below, ready for `docx-export`) and `email.md`.

## 1. Pick the letter type

Use the `Letter type` in `criteria.md`.

| Type        | When                                                 | Subject line                                              |
| ----------- | ---------------------------------------------------- | --------------------------------------------------------- |
| job-ad      | Responding to an advertised role                     | `Re: <Position> – <Company>` plus `(Ref: <ref>)` if given |
| speculative | No ad and no prior contact                           | None                                                      |
| follow-up   | They asked you to send a resume after a conversation | `Re: <Company> <opportunity>`                             |
| referral    | Someone referred you                                 | Optional                                                  |

## 2. Pick the opening

- **job-ad:** open with the match. Name the role and connect something the user has built or done to what the employer needs. Use a _motivational opening_ when `research.md` has a strong hook that connects to the user; otherwise lead with the strongest relevant evidence.
- Never open with "I am writing to apply for…", "I am the perfect candidate" or a childhood origin story. Name the role inside a sentence that already says something about you or them.
- **follow-up:** thank them for the conversation and name what impressed you.
- **referral:** name the referrer and their relationship to you in the first sentence.
- **speculative:** give a specific reason you are drawn to them, and acknowledge there may be no advertised role.

## 3. Structure

Three or four short paragraphs. Follow the employer's instructions first if they set a length or format. Use files in `templates/` and `references/` folder as guides only. Each paragraph should have a clear purpose:

1. **Opening - the match.** The role, plus one line connecting the user's strongest relevant work to the employer's need.
2. **Engineering evidence - why you.** Pick one relevant project from `master/stories.md` and tell it as: **problem → the user's contribution → decision or difficulty → result**. Show behaviours a junior engineer needs: debugging, testing, reading documentation, using Git, breaking down a problem. Name the ad's technologies only where this example used them. Include one useful project link (repo or demo). Choose the example that covers the most vital criteria from `criteria.md`; do not try to cover every criterion.
3. **Working with people.** One concrete example: responding to code review, clarifying requirements, documenting a setup, helping a teammate. Coursework, volunteering, tutoring and non-tech jobs count (see the mapping in section 6). Merge into paragraph 2 if the same project shows it.
4. **Why this company, and close.** One specific, verifiable reason from `research.md`: its product, users or advertised engineering work, linked to the user's own work. Then thank them and say you look forward to discussing the role at an interview. Close with readiness, not pleading.

## 4. Greeting and sign-off

| Greeting                                                                                | Sign-off            |
| --------------------------------------------------------------------------------------- | ------------------- |
| Named contact: `Dear Ms Roberts,` (title and surname, spelled exactly)                  | `Yours sincerely,`  |
| No name found in the ad or research: `Dear Hiring Manager,` or `Dear Recruitment Team,` | `Yours faithfully,` |

Look for a name first: the ad, `research.md`, then ask the user. Never write "To whom it may concern".

## 5. Tone: confident and enthusiastic, never cliché

- **Confident:** state what you did and what you will do. Use active, factual verbs ("I built", "I tested", "I fixed", "I collaborated on"). No "I feel", "I believe I could" or "I hope to".
- **Enthusiastic:** show eagerness through specifics, not adjectives. Name the product, project, value or problem that draws you and say what you want to do with it. One concrete reason beats any amount of "excited".
- **Never cliché:** no "passionate", "thrilled", "dream job", "hard-working", "fast learner", "self-starter", "team player", "detail-oriented", "excellent communicator", "hit the ground running", "fast-paced environment", "innovative company", "industry leader" or "perfect fit". If a sentence could appear in anyone's letter, rewrite it with a fact only this user has.
- Keep energy in the verbs and rhythm: short punchy sentences mixed with longer ones. No exclamation marks.

| Instead of                            | Write something like                                                                                           |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| "I'm a fast learner."                 | "I learned pytest to reproduce a bug and added a regression test."                                             |
| "I'm passionate about clean code."    | "I split validation from request handling so both could be tested independently."                              |
| "I'm a team player."                  | "I changed our error-response format after a teammate flagged it in code review, and documented the decision." |
| "I believe I would be a great fit."   | "My experience with [specific work] matches the role's focus on [specific requirement]."                       |
| "Your company is an industry leader." | One honest reason its product or work interests the user                                                       |
| A list of eight technologies          | One example showing how the relevant ones were used                                                            |

## 6. Limited experience: reframe, never apologise

Do not call the user inexperienced, and never write "Although I lack experience…", "I'm eager to learn" or "I'm willing to learn". These make the reader remember the gap. Lead with the closest relevant evidence instead: "My strongest relevant experience is…".

Mine non-SWE experience for evidence:

| Past experience                  | Junior SWE relevance                                                                       |
| -------------------------------- | ------------------------------------------------------------------------------------------ |
| Retail, hospitality, call centre | Handling unclear requests, staying calm under pressure, explaining to non-technical people |
| Group assignment or hackathon    | Collaboration, version control, dividing work, resolving disagreements                     |
| Tutoring or teaching             | Explaining technical ideas, receiving feedback                                             |
| Personal project                 | Self-direction, debugging, shipping an end-to-end feature                                  |
| Volunteer or club role           | Ownership, coordination, documentation, working within constraints                         |

If the ad asks for a tool the user lacks, use at most one honest bridge sentence, and only if every part is true: "I haven't used [tool] professionally, but I've used it in [project] to [task]." If the user has never touched it, name the closest transferable skill instead. Never fake familiarity.

## 7. Rules

- About 200-300 words, one page. No paragraph longer than 6 lines.
- Write like a sales pitch, not an essay. Do not restate the resume in paragraphs (degree, every technology, every job title). Add context the resume cannot: what the user built, why, what broke, what they changed.
- No fillers such as "Most recently", "In addition to those skills mentioned previously" or "However".
- Never invent or inflate metrics. "Added integration tests for expired sessions and failed payments" beats "improved reliability by 40%" with no defensible measurement.
- Never overclaim. Do not say "led" for a contribution, or imply production scale for a personal project.
- Every claim must pass: could the user point to a project, commit, test, document or conversation that proves it? If not, find the evidence or cut the claim.
- Use the ad's language only where it is true. No keyword stuffing.
- Do not say the resume is attached.
- No salary unless the ad asks. Then say it is negotiable and you are happy to discuss it at interview.
- Never criticise a previous employer, lecturer or teammate.
- No irrelevant personal detail: age, marital status, nationality, religion, political views or unrelated hobbies.
- Do not quote the company website. Show you understand what a fact means for them.
- Spell out uncommon acronyms. No SMS abbreviations.
- Never reuse a letter by swapping the company name. Similar roles can share structure, but motivation and evidence must be specific to each. Final test: could another applicant send this unchanged? If yes, add more of the user's actual work, not more adjectives.
- Proofread against the actual ad: company name, role title, reference number and recipient name.

## 8. Quality check

Before sending, make sure the applicant/user can answer these questions confidently:

- What exact problem did you solve?
- Why was your first approach insufficient?
- What did you change, and what evidence shows it worked?
- What did you learn from feedback or testing?
- Why this company, specifically?
- Can you walk an interviewer through the project in two minutes?

If you can answer all six, the letter will hold up.

## 9. Finish: always in this order

1. Run `humanize-prose` on `cover-letter.md` and `email.md`.
2. Then run `verify-claims` on the humanized text. It is always the final step, so no wording change can slip in an unchecked claim.

Never skip or reorder these steps. Never run `humanize-prose` on `resume.md`.
