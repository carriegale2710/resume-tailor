---
name: selection-criteria
description: Write a selection criteria response document, answering every criterion with the 3-part structure (overview, STAR evidence, link to the role). Use when criteria.md says the employer requires a response, common in government and academic roles.
---

# Selection criteria response

Input: `criteria.md`, `resume.md`, `master/master-resume.md`, `master/stories.md`.
Output: `applications/<company>-<role>/selection-criteria.md`.

## 1. Set up the document

```markdown
# Name Surname – <Position>, <Organisation>

## <Criterion 1, copied exactly from the ad>

<response>

## <Criterion 2>

### <sub-heading, only if the criterion has distinct parts>

<response>
```

Copy every criterion exactly, as `##` headings. Add `###` sub-headings only where they make a multi-part criterion easier to read.

## 2. Plan before writing

List every criterion. For each, pick the best story from `master/stories.md` and supporting items from the resume. Draw from all parts of the resume: work, projects, study, volunteering. Avoid using the same main story for two criteria. If a criterion has no good evidence, ask the user before writing.

## 3. Write each response in 3 parts

1. **Overview.** One sentence stating where you acquired the criterion.
2. **Evidence.** One STAR story: Situation (where), Task (the problem), Action (what you did), Result (how effective, with numbers). Optionally add 2-4 achievement-statement bullets with further evidence.
3. **Link.** One sentence linking your capability to the position's tasks at this organisation.

Pitch the evidence to the wording, using `../job-ad-decoder/references/criteria-glossary.md`. "Proven record" and "demonstrated" need documented outcomes; "awareness of" needs only familiarity.

## Example

Criterion: _Demonstrated effective problem-solving ability_

> My problem-solving capacity has been applied in consulting competitions and research projects.
>
> In a 2017 consulting case competition, I worked with 4 team members on a Deloitte project to find new ways to market its graduate recruitment drive. I met the HR Business Partner and recruitment team, then ran a needs analysis on survey data and identified gaps. I proposed 3 pathways, setting out the benefits, challenges and cost of each, and presented them to Deloitte. The solutions were well received, and the team placed 4th of 11.
>
> - Designed experiments and analysed data for 3 research reports, earning a distinction average
>
> My ability to identify problems, assess gaps and propose feasible solutions can be applied to <task> at <organisation>.

## Rules

- Address every criterion.
- 250-350 words per criterion, unless the employer sets a limit. Their limit wins.
- Use active voice. Avoid "had to", "was assigned to" and "was required to".
- Avoid words that reduce credibility: "always", "often", "every".
- Quantify with numbers wherever you can.
- First person is fine here.
