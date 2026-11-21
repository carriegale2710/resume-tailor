---
name: docx-export
description: Export an application's resume.md, cover-letter.md or selection-criteria.md to a formatted Word document (11pt Calibri, A4, right-aligned dates, no italics). Use after linting, when the user wants files ready to send.
---

# Export to Word

```
node scripts/export_docx.js <in.md> <out.docx>
```

Needs Node.js and the `docx` package. Run the script from the user's workspace. If it reports a missing dependency, run `npm install docx` in the workspace and try again.

`scripts/` and `templates/` are relative to this skill's base directory, not the user's workspace.

Export each document next to its Markdown source:

```
applications/<company>-<role>/resume.docx
applications/<company>-<role>/cover-letter.docx
applications/<company>-<role>/selection-criteria.docx
```

Then render the `.docx` to PDF or images and look at every page: check it fits the page limit (resume 2 pages, cover letter 1 page) and nothing overflows. Flag a last page holding only a few lines: trim or rebalance.

Name the files you send `<Firstname>-<Surname>-Resume` and `<Firstname>-<Surname>-Cover-Letter`, never "final_v2" or "resume (1)". Send the format the portal asks for. By email, send PDF exported from Word, never a scan.

## Layout

The script picks the layout from the Markdown:

- **Resume layout** (any `## ` heading): 1.8cm margins, section headings in bold capitals with a rule, footer with name and page number. Selection criteria responses use this layout too.
- **Letter layout** (no `## ` headings): 2.54cm margins, no footer.

Both use A4, Calibri 11pt, bold for headings and titles, no italics or underline. Emails and URLs become clickable links.

## Markdown contract

| Markdown | Becomes |
|---|---|
| `# Name Surname` | Name heading (also used in the footer) |
| Lines directly under `#`, up to the first blank line | Contact lines |
| `## Heading` | Section heading |
| `### Title \| Mon YYYY – Mon YYYY` | Bold title with dates right-aligned (split on the last ` \| `) |
| Plain line directly under `###` | Organisation or stack line |
| `- text` | Bullet |
| `**Label:** text` | Bold label, regular text |
| Plain line | Paragraph; a blank line after it adds space |

## Templates

Start a new application from these. Each `.docx` is generated from the `.md` beside it, so edit the `.md` and re-export rather than editing the Word file.

- `templates/resume-grad-tech.md` - default for graduate tech roles
- `templates/resume-general.md` - the guide's standard order, for non-technical roles
- `templates/cover-letter.md` - one-page letter
