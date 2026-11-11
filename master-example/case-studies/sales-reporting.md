# Sales Reporting Database – a retailer's weekly sales report without the re-keying

_Python, PostgreSQL, pandas, pytest | Repo: ${GITHUB_URL}/sales-reporting | Live: n/a_

> EXAMPLE DATA: fictional project for running tests.

> **In 5 seconds**
>
> - **Problem:** A shop owner re-typed weekly CSV exports into spreadsheets to see sales.
> - **What I built:** A PostgreSQL schema, a CSV loader with data checks, and the report queries.
> - **Hardest part:** Exports contained duplicate orders and negative quantities that broke the totals.
> - **Outcome:** Bad rows rejected before loading; weekly report built from three tables.

| Role | Team | Timeline | Status |
|---|---|---|---|
| Developer: schema, loader, data checks | 3 | 12 weeks (university semester) | Complete |

## The story

**Situation.** The owner of a small retailer exported sales to CSV each week and re-typed totals into a spreadsheet. Our capstone team agreed to replace that step.
**Task.** I owned the database design and the loader. The report had to match the owner's existing numbers.

**Action.**

- **Normalised schema** – separate tables for orders, products and customers, so a price change did not rewrite old orders.
- **Checks before load** – pytest tests reject duplicate order IDs and negative quantities, and the loader logs each rejected row.
- **Report scope** – met the owner twice and cut the report to the three tables they actually read.

**Result.**

- Weekly report produced from PostgreSQL, not hand-typed.
- Rejected rows listed in a log file for the owner to fix at source.

## Feature deep dives

### Data checks: **reject bad rows, keep the load running**

- **Challenge:** One duplicate order doubled a day's total in the first test run.
- **What I did:** Wrote pytest checks for duplicate IDs and negative quantities, and made the loader skip and log failing rows instead of stopping.
- **Why it works:** The loader never inserts a row that fails a check, so totals stay correct.
- **Outcome:** Test export totals matched the owner's spreadsheet after the checks were added.

## What I'd do next

- Add a currency check for refunds.
- Schedule the load instead of running it by hand.

## Screenshots & links

- Repo: ${GITHUB_URL}/sales-reporting
