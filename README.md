# Junior QA Take-Home Assessment

This repository contains my completed Junior QA take-home assessment.

The work includes manual test case design, bug reporting, API testing, SQL data validation, UI automation and a final test summary.

## Tasks

### Task 1 - Test Cases

Appointment booking test cases covering positive, negative and boundary scenarios.

[View Test Cases](01-test-cases/test-cases.md)

### Task 2 - Bug Reports

Manual testing of Sauce Demo using `problem_user` and comparison with `standard_user`.

Five bugs were documented with screenshots.

[View Bug Reports](02-bug-reports/bug-reports.md)

[View Evidence](02-bug-reports/evidence)

### Task 3 - API Testing

Automated tests for the Restful Booker API using Python, pytest and requests.

The suite contains 12 tests covering authentication, CRUD operations and negative scenarios.

[View API Tests](03-api/test_booker_api.py)

[View API Findings](03-api/findings.md)

[View API Setup Instructions](03-api/README.md)

### Task 4 - SQL

Five SQL queries were written to investigate the provided claims dataset.

The queries cover claim details, approved totals, members without claims, claims submitted after policy expiry and possible duplicate claims.

[View SQL Queries](04-sql/queries.sql)

[View SQL Bug Report](04-sql/bug-report.md)

### Task 5 - UI Automation

Four Sauce Demo scenarios were automated using Python, pytest and Playwright.

The automated tests cover:

- successful login
- locked-out user error handling
- adding two products to the cart
- completing checkout

[View Automation Tests](05-automation/tests/test_saucedemo.py)

[View Automation Setup Instructions](05-automation/README.md)

### Task 6 - Test Summary

A final summary of the testing performed, results, key risks and release recommendation.

[View Test Summary](06-test-summary.md)

## Test Results

### API

Latest full API suite result:

- 8 passed
- 2 expected failures
- 2 failures caused by responses exceeding the required 2-second response time

Additional API findings are documented in `03-api/findings.md`.

### UI Automation

Latest automation result:

- 4 passed
- 0 failed

## Tools Used

- Python
- pytest
- requests
- Playwright
- SQLite
- Google Chrome
- Git and GitHub
- VS Code

## Challenges

Some Restful Booker requests had inconsistent response times and occasionally exceeded the required 2-second limit.

I also encountered a package download timeout while installing Playwright. I resolved it by increasing the pip download timeout and then completed the browser installation successfully.
