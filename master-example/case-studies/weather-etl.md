# Daily Weather ETL – a scheduled Airflow pipeline into PostgreSQL

_Python, Airflow, PostgreSQL, Docker Compose, dbt | Repo: ${GITHUB_URL}/weather-etl | Live: n/a (local only)_

> EXAMPLE DATA: fictional project for running tests.

> **In 5 seconds**
>
> - **Problem:** I had never built a scheduled pipeline end to end.
> - **What I built:** An Airflow DAG that fetches a public weather API daily, stores raw JSON and loads cleaned rows into PostgreSQL.
> - **Hardest part:** The API rate limit and malformed readings stopped runs.
> - **Outcome:** Daily run works locally with dbt tests. Unfinished: monthly summary models.

| Role | Team | Timeline | Status |
|---|---|---|---|
| Solo: DAG, cleaning, load, dbt tests | Solo | About 3 weeks part-time (self-reported) | Unfinished |

## The story

**Situation.** I wanted hands-on practice with Airflow before applying for data roles. A free public weather API gave steady data.

**Task.** Build a daily pipeline I could rerun safely, run it with Docker Compose, and test the data.

**Action.**

- **Raw first** – stored the untouched JSON, then cleaned into a second table, so a cleaning bug did not lose data.
- **Safe reruns** – loads use upserts keyed on station and date, so rerunning a day adds no duplicates.
- **Retries** – Airflow retries with a delay when the API rate limit returns an error.
- **dbt tests** – checks for nulls and temperatures outside a plausible range.

**Result.**

- Daily DAG loads cleaned rows into PostgreSQL on a local Docker Compose stack.
- dbt tests catch null and out-of-range values.
- Not finished: monthly summary models. Not deployed.

## Feature deep dives

### Idempotent load: **rerun a day, get the same table**

- **Challenge:** A failed run followed by a manual rerun inserted the same day twice.
- **What I did:** Added a unique key on station and date and changed the insert to an upsert.
- **Why it works:** The database refuses the duplicate, so reruns are safe.
- **Outcome:** Rerunning any day leaves row counts unchanged.

## What I'd do next

- Write the monthly dbt models.
- Move it from local Compose to a cloud scheduler.

## Screenshots & links

- Repo: ${GITHUB_URL}/weather-etl
