# MASTER RESUME (source of truth: never submit this directly)

> **Use:** `bash scripts/new-application.sh company-role`, filter bullets by tag, cut to one page (two pages maximum), tick `tailoring-rules/every-resume.md`, export as **.docx**.
> **Rules:** Edit facts here only. Every number needs a row in `master/metrics-log.csv`. Fill every `TODO` before reusing a claim. Swap unproven numbers for the safe wording.

**Tag key:** `fullstack` `backend` `frontend` `qa` `ux` `a11y` `ai-eval` `devops` `product` `leadership` `security` `research` `ecommerce` `startup` `retail` `customer-service`
**Variant key:** **S** = short one-liner, **M** = standard, **Q** = quantified

> EXAMPLE DATA: fictional persona (Jordan Reyes, junior backend and data engineer) for running tests. Every name, employer, number and link is made up. Delete this note and replace with your own facts.

---

# Maintenance (private; never on a resume)

## Maintenance checklist

- [ ] Within 1 week of finishing anything: add bullets, tags, and metrics evidence
- [ ] Monthly (10 min): add new work, check links, update demo URLs
- [ ] Quarterly: move stale material to an Archive section
- [ ] Commit after every change (or save a dated copy)
- [ ] Before exporting any tailored CV: follow `tailoring-rules/every-resume.md`

---

## 0. Header and admin facts

Leave the `${...}` placeholders exactly as written. `scripts/build.sh` fills them from `.env` at docx build time.

- Name: ${RESUME_NAME}
- Location: ${RESUME_LOCATION}
- Phone / Email: ${RESUME_PHONE} / ${RESUME_EMAIL}
- LinkedIn / GitHub / Portfolio: ${LINKEDIN_URL} / ${GITHUB_URL} / ${PORTFOLIO_URL}
- Work rights / visa status: ${RESUME_WORKRIGHTS}
- Languages: English (fluent), Tagalog (conversational)

### Headline options

- **Backend:** Junior Backend Developer | Python, FastAPI, PostgreSQL
- **Data:** Junior Data Engineer | Python, SQL, Airflow, dbt
- **DevOps:** Junior Platform Engineer | Docker, GitHub Actions, AWS

### Summary variants

- **Backend (`dev`):** Junior backend developer with a Bachelor of Information Technology and an eight-month internship on a payments API team. Built and tested REST services in Python and FastAPI, and containerised them for CI deployment.
- **Data (`graduate-swe`):** Information Technology graduate who built a daily ETL pipeline and a tested reporting database during an internship and a capstone project. Works in Python, SQL and Airflow, and checks data quality with automated tests.
- **Customer service / retail (`retail-cs`):** Four years of retail and hospitality service work alongside study, now moving into software support and engineering.

**Optional add-on lines (one per CV at most):**

- **Interests (`addon-interests`):** Interests: trail running, board-game design, open-source documentation.

---

## 1. Skills inventory (reference only; not a CV section)

**Main tech stack** (strongest first, not exhaustive): Python, SQL (PostgreSQL), FastAPI, Docker, Git and GitHub, pytest, GitHub Actions. For full skills inventory list, see `skills-inventory.csv`.

---

## 2. Education & Training

### Western Plains University, Bachelor of Information Technology

- Brisbane, QLD | Feb 2021 – Nov 2023 | Major: Software Development, Credit average
- `backend` `qa` Studied data structures, relational databases, networking and software testing. Capstone: built a tested sales-reporting database for a local business.

### Certifications

#### Amazon Web Services, Cloud Practitioner

- Mar 2024 – Mar 2024 | `devops`

#### DataCamp, Associate Data Engineer in SQL

- Jun 2024 – Aug 2024 | `backend`

---

## 3. Work experience

### Harbourline Payments, Software Engineering Intern

Brisbane, QLD | Mar 2024 – Nov 2024 | Team size: 8 | Stack/Tools: Python, FastAPI, PostgreSQL, Docker, GitHub Actions, pytest, Jira
Links: TODO

**One-liners:**

- **S:** Built and tested API endpoints for a payments reconciliation service in a team of eight.

**Bullets:**

- `backend` `qa` Added four REST endpoints to the reconciliation API in FastAPI, with pytest tests for each, so support staff could look up failed transfers without asking an engineer.
- `backend` Rewrote a slow settlement query by adding an index and removing a repeated subquery; query time fell from about 4 seconds to under 1 second _(self-reported; see Metrics Log)_.
- `devops` Wrote a Dockerfile and a GitHub Actions job that ran the test suite on every pull request.
- `qa` Raised test coverage on the reconciliation module from 52% to 71%.
- `security` Replaced hard-coded API keys in two scripts with environment variables after a code review comment.
- `leadership` Presented a five-minute demo of the new endpoints at the sprint review.

### Earlier roles: retail, hospitality and customer service (`optional: use for retail/customer-service applications; otherwise drop`)

#### Kettle & Crumb Cafe, Barista and Shift Supervisor

Brisbane, QLD | Jan 2020 – Feb 2023

- `retail` `customer-service` Served about 150 customers per shift and trained five new staff on the espresso machine and till.
- `leadership` Opened and closed the cafe as shift supervisor, counting the till and reconciling takings.

#### Coastline Outfitters, Sales Assistant

Brisbane, QLD | Dec 2018 – Dec 2019

- `retail` `customer-service` Handled stock counts, returns and online-order pickups in a store of 12 staff.

---

## 4. Projects

> **Rule:** no dates or years on projects. Add one only for a work in progress, and only if given here.

### Sales Reporting Database | Capstone data project

Role: Developer | Team: 3
Stack: Python, PostgreSQL, pandas, pytest
Live: n/a | Repo: ${GITHUB_URL}/sales-reporting

**One-liners:**

- **S:** Loaded a small retailer's CSV exports into PostgreSQL and produced weekly sales reports.

**Bullets:**

- `backend` Designed a normalised PostgreSQL schema for orders, products and customers, and loaded it from CSV exports with a Python script.
- `qa` Wrote pytest checks for duplicate orders and negative quantities, so bad rows were rejected before loading.
- `product` Met the owner twice to agree the weekly report layout, and cut the report to the three tables the owner used.

### Daily Weather ETL | Data pipeline

Role: Solo | Team: Solo
Stack: Python, Airflow, PostgreSQL, Docker Compose, dbt
Live: n/a | Repo: ${GITHUB_URL}/weather-etl

**One-liners:**

- **S:** Airflow pipeline that pulls daily weather data from a public API into PostgreSQL.

**Bullets:**

- `backend` `devops` Built an Airflow DAG that fetches a public weather API each day, stores raw JSON and loads cleaned rows into PostgreSQL, all run with Docker Compose.
- `qa` Added dbt tests for null values and out-of-range temperatures.

> Unfinished: dbt models for monthly summaries are not written. Do not describe the project as complete or deployed.

### URL Shortener API | Backend web service

Role: Solo | Team: Solo
Stack: Python, FastAPI, SQLite, Docker
Live: TODO | Repo: ${GITHUB_URL}/url-shortener

**One-liners:**

- **S:** FastAPI service that shortens URLs and counts redirects.

**Bullets:**

- `backend` Built create, redirect and stats endpoints with input validation and a rate limit per IP address.
- `devops` Containerised the service with Docker and ran its tests in GitHub Actions.

---

## 5. Leadership, programs and activities

> **Graduate roles:** put section 2 plus any programs below together under "Education & Training" directly below the summary.

### Western Plains University Coding Club, Workshop Lead

Brisbane, QLD | Mar 2022 – Nov 2023

- `leadership` Ran six fortnightly Python workshops for first-year students, with groups of about 20.
- `leadership` Wrote the SQL starter exercises that later clubs reused.

### Awards

- Dean's Commendation for Academic Excellence: recognised a high-credit semester in 2022.

---

## 6. Private constraints and evidence (NEVER on a resume)

- **Metrics evidence:** `master/metrics-log.csv`. Every number on a CV needs a row; Estimate, Projection and Self-reported rows use the Safe wording column.
- **Narrative material:** `master/narrative-notes.md` (personal story, differentiators, likely objections, target industries).
- **Retired content and the maintenance checklist:** `master/archive.md`.
- **Applications:** `applications/tracker.csv`.

- **NDA or confidentiality limits:** Harbourline Payments: may name the employer and the stack. Do not name clients, internal service names or transaction volumes. Say "a payments reconciliation service".
- **Eligibility-only facts (e.g. WAM):** WAM 68. Quote only when an application form asks. Never on a resume or cover letter.
- **Date overlaps:** Coding Club (Mar 2022 – Nov 2023) overlaps the degree and the cafe job. Cafe job overlaps the first two years of study.
- **Interview stories (STAR):** TODO one each for the settlement query fix and the capstone data checks. Later stories go in `master/stories.md`.
- **Anything discussable but not publishable:** Intern offer was not converted to a graduate role because of a hiring freeze, not performance.
- **Third-party evidence (reference letters):** Intern supervisor (Priya Nair, Senior Engineer) wrote that Jordan "wrote clear tests and asked good questions". Agreed to be a referee. Use for cover letters and interviews, never as resume adjectives.
- **Do not claim:** Airflow in production (portfolio project only); AWS hands-on work beyond the free-tier labs; 71% coverage for the whole codebase (reconciliation module only); any Kubernetes experience.

### Conflicts between this master and older CVs (resolve once, then delete this list)

- Older CV said "Senior intern" and "built the payments platform". Master says Software Engineering Intern on one service. Use master.
- Older CV listed Java as a skill. No master bullet evidences it; kept as Weak / exposure only (coursework).
