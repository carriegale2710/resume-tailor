---
name: cover-letter
description: Write a one-page tailored cover letter (job ad, speculative, follow-up or referral) and the short email that goes with an emailed application. Use for every application unless the employer says not to send one.
---

# Cover letter

A cover letter complements the resume. It answers can you do the job, will you do the job, and will you fit in. It is the main place to show motivation - why this company, why this role - which is often what decides who gets an interview.

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

- **job-ad:** use a _motivational opening_ when `research.md` has a strong hook that connects to the user. Otherwise use a _key selling points opening_: qualification, strongest experience, and why you can succeed in the role.
- Never open with "I am writing to apply for…" or "I am the perfect candidate". Name the role inside a sentence that already says something about you or them.
- **follow-up:** thank them for the conversation and name what impressed you.
- **referral:** name the referrer and their relationship to you in the first sentence.
- **speculative:** give a specific reason you are drawn to them, and acknowledge there may be no advertised role.

## 3. Structure

1. **Opening - why them.** Who you are in one line (qualification plus strongest experience). Why this role and company, using researched specifics. What value you bring to their needs, not what you want.
2. **Middle, 1-3 paragraphs - why you.** Cover the vital 3-5 criteria from `criteria.md`, not every criterion. One theme per paragraph: either one experience that shows several skills, or one skill shown across several experiences. Back each claim with an achievement. For tech roles, name the ad's technologies you have used, and link one relevant repo or project.
3. **Summary.** Why you are the best fit. Try the 3 best things about you and how they will get results in this role.
4. **Closing.** Thank them, and say you look forward to discussing the role at an interview.

## 4. Greeting and sign-off

| Greeting                                                               | Sign-off            |
| ---------------------------------------------------------------------- | ------------------- |
| Named contact: `Dear Ms Roberts,` (title and surname, spelled exactly) | `Yours sincerely,`  |
| No name found in the ad or research: `Dear Hiring Manager,`            | `Yours faithfully,` |

Look for a name first: the ad, `research.md`, then ask the user. Never write "To whom it may concern".

## 5. Rules

- One page: about 300-400 words. No paragraph longer than 6 lines.
- Write like a sales pitch, not an essay. State benefits; skip long explanations.
- No fillers such as "Most recently", "In addition to those skills mentioned previously" or "However".
- Never apologise or hedge. No "while I don't have…" or "although I have limited experience…". Describe what you do have, with enthusiasm.
- Do not say the resume is attached.
- No salary unless the ad asks. Then say it is negotiable and you are happy to discuss it at interview.
- Do not quote the company website. Show you understand what a fact means for them.
- Spell out uncommon acronyms. No SMS abbreviations.
- Never reuse a letter by swapping the company name. Similar roles can share structure, but motivation and evidence must be specific to each.

## Last step: humanize-prose

Always run the `humanize-prose` skill on `cover-letter.md` (and `email.md` if written) as the final step of this skill, after the rules above pass. Then hand off to `verify-claims`, which stays the mandatory final audit before anything is called ready. Never skip this step. Never run `humanize-prose` on `resume.md`.

## cover-letter.md format

```markdown
# Name Surname

0400 000 000 | name.surname@email.com | linkedin.com/in/namesurname

2 November 2026

Ms Jane Jenkins
HR Manager
Company Name
Street, Suburb STATE Postcode

**Re: Graduate Software Engineer – Company Name (Ref: 1234)**

Dear Ms Jenkins,

<opening paragraph>

<middle paragraphs>

<summary paragraph>

<closing paragraph>

Yours sincerely,

Name Surname
```

Use the date format `D Month YYYY`. Include whatever recipient details are known; leave out unknown lines rather than guessing.

## email.md

Write this when the application goes by email, or when the user asks. Do not paste the cover letter into the email body unless the employer asks.

```markdown
Subject: <Position> application – <Name Surname>

Dear <same greeting as the letter>

Please find attached my resume and cover letter for the <Position> role.

- <selling point 1>
- <selling point 2>
- <selling point 3>

If you have any questions about my experience, please get in touch.

Thank you for your time and consideration.

<Same sign-off as the letter>
<Name Surname>
<Qualification>
M: <phone> | E: <email>
```

Use 3-5 selling points, taken from the letter's strongest evidence.
