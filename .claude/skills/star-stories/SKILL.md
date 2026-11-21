---
name: star-stories
description: Writes and updates STAR stories in master/stories.md, drawn only from facts in the master files and the user's answers, either to fill gaps in the story bank or to answer a given list of behavioural questions. Use when the user asks to write, add, fill or review STAR stories or the story bank, gives behavioural interview questions to prepare stories for, or when interview-prep or selection-criteria finds no story that fits.
---

# STAR stories

## Goal

Turn recorded achievements into STAR stories in `master/stories.md`. Every fact in a story traces to `master/master-resume.md`, `master/case-studies/` or a confirmed user answer. `master/narrative-notes.md` adds context and motivation only, rewritten, never copied.

Two modes:

- **Coverage mode** (default): fill the bank's missing themes, 1-3 stories per run.
- **Question mode**: the user gives behavioural questions, pasted in chat or as a file path (for example `applications/<folder>/questions.md`). Each question gets one story.

## Stages

Run in this order. Write to `master/` only after the user confirms each edit.

### 1. Intake

- **Input:** `master/stories.md` (may not exist), `master/master-resume.md`, `master/case-studies/*.md`, `master/narrative-notes.md`, `master/skills-inventory.csv`, `master/tags.md`.
- **Action, both modes:** Re-check each existing story's `Source`. Flag any story whose source heading or bullet is gone or changed, and offer to update it.
- **Action, coverage mode:** Build the theme list:
  - Generic: problem solving, teamwork, conflict or disagreement, leadership or initiative, failure or mistake, learning something fast, tight deadline, acting on feedback, explaining tech to non-tech people, customer or user focus.
  - Role-specific: 1-2 themes per target summary variant in `master/tags.md` (for example "shipped a feature end to end" for `dev`). Add any theme the user or the current `criteria.md` names.
  - Show a table: theme, covering story (or none), best candidate achievement from the master (heading + bullet), tech or non-tech.
- **Action, question mode:** Show a table: question, best existing story, fit (strong, weak, none), best candidate achievement for weak or none. Strong fits reuse the existing story by default. One achievement backs at most 2 questions per list; after that, use the next-best achievement.
- **Draw from all experience:** work, projects, study, volunteering, and the retail and hospitality roles.
- **Gate:** The user confirms the table. In coverage mode they pick 1-3 stories. In question mode they accept or override each match. Skip coverage mode's table if the user already named the achievement.

### 2. Draft all stories

- **Input:** For each new story: the chosen achievement, every master bullet, one-liner and case study about it, and related `narrative-notes.md` entries.
- **Action:** Fill `.claude/skills/master-resume/templates/stories-template.md` for each story before any interview. Write each field from master facts only, lightly edited: first person, past tense, plain, no added claims. Use narrative notes for Situation context or motivation, in new words. A narrative note that states an achievement fact (task, outcome, number) needs write-back to `master-resume.md` first (Stage 4). Mark each unknown part `TODO`. Set `Status: draft` while any `TODO` remains.
- **Output:** All drafts in chat, with `TODO`s visible.
- **Gate:** No sentence states a fact that is not in the sources. On fail, cut the sentence or mark it `TODO`.

### 3. Fill gaps by interview

- **Condition:** Run only if a draft has a `TODO`, or Action says "we" without the user's own part.
- **Action:** Work across all drafts at once, most important gap first. Ask at most 3 questions at a time; prefer one. One answer can fill gaps in several stories. Use the soft-skill branch in `.claude/skills/master-resume/references/gap-interview.md`. Good questions:
  - Situation: "Who was involved, and what was at stake?"
  - Task: "What exactly was your responsibility?"
  - Action: "What did you do yourself, step by step? What did you decide, and why?"
  - Result: "What changed afterwards? How do you know? Any number, and where is the proof?"
  - Failure or feedback stories: "What would you do differently, and have you done that since?"
- **Output:** User answers, in their words.
- **Gate:** Stop after 2-3 tries that find nothing on one gap. Leave it `TODO` and the story `draft`. Never suggest an answer the user then just agrees to.

### 4. Write back

- **Action:** Follow master write-back in `AGENTS.md`. Order matters:
  1. New facts go into `master/master-resume.md` first, in the user's own words, in the right section, with tags.
  2. New numbers get a `master/metrics-log.csv` row. Unproven numbers are Self-reported or Estimate, with a Safe wording.
  3. Then the stories go into `master/stories.md`. Create it from the template header on first use. Set `Status: ready` only when no `TODO` remains. In question mode, add each matched question to the story's `Answers` field, including reused stories.
  4. Question mode with a file input only: write the question-to-story table to `story-map.md` in that file's folder.
- **Output:** All edits shown together, each as file, section, old, new.
- **Gate:** Write only edits the user confirms. Declined edits stay out.

### 5. Check each story

Tick each item for every new or changed story:

- [ ] Action is the longest field, first person, active verbs, and names what the user did (not the team).
- [ ] Result states an outcome. Numbers appear only if in `metrics-log.csv`, using Safe wording where the row needs it.
- [ ] `Shows` lists 2-4 skills, matching wording in `skills-inventory.csv` where one exists.
- [ ] `Tags` uses bullet tags from `master/tags.md` only.
- [ ] Failure and feedback stories have `Learned` filled in.
- [ ] `Status` is `ready` only if no `TODO` remains.
- [ ] NDA work uses generic wording for client, tools and project type.
- [ ] Nothing from master section 6 or `archive.md` is used. Nothing from `narrative-notes.md` is copied word for word.
- [ ] No placeholder values (`${RESUME_NAME}` etc.) are filled in.
- [ ] Situation, Task and Result are 1-2 sentences each. Action is 2-4 sentences.
- [ ] Situation to Result totals 80-150 words. Interview-prep expands it to a spoken answer.
- [ ] Australian English spelling.

On fail, fix and re-check. Report any item you could not fix.

## Rules

- A story can reuse a master achievement. It never adds detail the master lacks without write-back.
- Keep stories neutral: plain STAR facts, not worded for one question. Interview-prep and selection-criteria adapt them per application.
- One achievement per story. A second skill is a `Shows` entry, not a second story.

## Done when

The confirmed stories are in `master/stories.md`, all new facts and numbers are in the master first, and every Stage 5 item is ticked. Report: stories added, reused or changed, stories still `draft` and their `TODO`s, themes or questions still uncovered, stale stories flagged, and every write-back edit (file, section).
