# Sauce Demo UI Automation

This folder contains automated UI tests for the Sauce Demo website using Python, pytest and Playwright.

## Tools Used

- Python
- pytest
- Playwright
- pytest-playwright

## Setup

From the project root, create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

Install the required packages:

```bash
pip install -r 05-automation/requirements.txt
```

Install the Chromium browser used by Playwright:

```bash
playwright install chromium
```

## Run the Tests

From the `05-automation` folder, run:

```bash
python -m pytest tests/test_saucedemo.py -v
```

## Automated Tests

The suite contains four automated tests:

1. Standard user can log in successfully and see the products page.
2. Locked-out user receives the correct error message.
3. Standard user can add two products to the cart and the cart badge shows 2.
4. Standard user can complete checkout and see the order confirmation message.

## Test Design

The automation uses the Page Object Model to separate page interactions from test logic.

Page objects are stored in the `pages` folder.

Stable `data-test` attributes are used as locators.

The tests do not use fixed sleep statements.

Each test starts from the login page and is independent from the other tests.

Assertions are made against visible UI behaviour such as the products page, error message, cart badge and checkout confirmation.
