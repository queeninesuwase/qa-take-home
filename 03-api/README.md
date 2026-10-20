# Restful Booker API Tests

This folder contains automated API tests for the Restful Booker practice API using Python, pytest and requests.

## Tools Used

- Python
- pytest
- requests

## Setup

From the main project folder, create a virtual environment:

```bash
python3 -m venv env
```

Activate it:

```bash
source env/bin/activate
```

Install the required packages:

```bash
pip install -r 03-api/requirements.txt
```

## Run the Tests

Run all API tests with:

```bash
python -m pytest 03-api/test_booker_api.py -v
```

## What Is Tested

The test suite contains 12 API tests covering:

1. Successful authentication
2. Authentication with invalid credentials
3. Creating a booking
4. Reading a created booking
5. Updating a booking using PUT
6. Partially updating a booking using PATCH
7. Deleting a booking
8. Creating a booking with missing fields
9. Creating a booking with incorrect data types
10. Requesting a booking that does not exist
11. Updating a booking without an authentication token
12. Updating a booking with an invalid token

## Test Checks

For each request, the tests check:

- HTTP status code
- Important fields in the response body where applicable
- Response time is under 2 seconds

The booking ID created during the tests is reused automatically by later tests instead of being copied manually.

The authentication token is also created automatically and reused for requests that require authentication.

## Known Findings

Some behaviour did not match the expected API behaviour.

Examples include:

- Some API responses occasionally took longer than 2 seconds.
- A booking with missing required fields returned HTTP 500 instead of a client validation error.
- A booking with incorrect data types was accepted with HTTP 200.

More details are available in:

`findings.md`

## Notes

Some response-time tests may pass or fail between runs because Restful Booker is a shared public practice API and response times can vary.

Known validation problems are marked with `xfail` so they remain visible without being confused with unexpected test failures.