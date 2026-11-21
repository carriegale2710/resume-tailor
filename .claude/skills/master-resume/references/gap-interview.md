# Gap interview

Use when `criteria.md` marks a criterion `weak` or `gap`. The aim is to surface evidence the user has but has not recorded. It is a conversation, not a questionnaire: each answer decides the next question.

Adapted from `branching-questions.md` in [resume-tailoring-skill](https://github.com/varunr89/resume-tailoring-skill), MIT License, Copyright (c) 2025 Varun Ramesh.

## Technical skill gap

Open: "The role asks for <skill>. Have you used <skill> or anything like it?"

Branch on the answer:

| Answer                            | Follow up with                                                                                            | Capture as                               |
| --------------------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **Yes, directly**                 | What did you use it for? What scale? Production or a test setup? What problem did you solve? Any numbers? | A full achievement bullet                |
| **Indirectly** (worked beside it) | What was your part? Did you configure, test, review or document it? What did you learn?                   | A supporting-role bullet, if substantial |
| **Adjacent** (a similar tool)     | Tell me about <similar tool>. Did you do <the same kind of task>?                                         | Related experience, named honestly       |
| **Study or personal project**     | Which course or project? What did you build? How recent?                                                  | A project or coursework entry            |
| **No**                            | Any other <broader category> work?                                                                        | Move on if still no                      |

## Soft skill or experience gap

Open: "The role emphasises <skill>. Tell me about a time you <did that skill>."

| Answer                        | Follow up with                                                                                 | Capture as                                |
| ----------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **A clear example**           | Who was involved? What was the challenge? What did you do? What was the result?                | A STAR story in `stories.md`              |
| **Vague or unsure**           | Rephrase: "Have you ever <concrete version of the skill>?" How many people? What made it hard? | Help them put it into words               |
| **One project**               | What was your part versus others'? Who did you coordinate with?                                | Leadership or teamwork, if there is depth |
| **Volunteering or side work** | Scope and timeline? Which skills match this job? Any outcome?                                  | Include if it proves the capability       |

## Recent work

Ask once per application: "What have you done in the last 6 months that isn't in your master resume yet?"

If they say "nothing new", prompt: small improvements, process changes, new tools learned, mentoring or teaching, anything that seemed too small to mention.

## How to run it

- Start broad, then narrow. Do not ask about details they have already given.
- Short answers: offer choices ("Was it more like X or Y?"). Long answers: ask for the key point.
- Link answers: "Earlier you mentioned <X>. Does that apply here too?"
- Stop after 2-3 tries that find nothing. Mark the criterion `gap` and offer the gap options in `job-ad-decoder`. Do not pressure the user into evidence that does not exist.
- Ask at most three questions at a time. Prefer one.

## After the interview

1. Add every new fact to `master/master-resume.md`, and every new story to `master/stories.md`, in the user's own words.
2. Update the criterion's evidence level in `criteria.md`.
