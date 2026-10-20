# Test Summary

## What Was Tested

The assessment covered manual UI testing, API testing, SQL data validation and UI automation.

### Sauce Demo Manual Testing

I tested the `problem_user` account against the `standard_user` account across login, product listing, product details, cart and checkout.

Five issues were documented:

- Product images are incorrect for `problem_user`.
- Sauce Labs Bolt T-Shirt cannot be added to the cart.
- The Last Name field does not retain input during checkout.
- Product sorting does not work.
- Clicking Sauce Labs Backpack opens the wrong product details page.

### Restful Booker API

Twelve API tests were created covering authentication, booking creation, retrieval, PUT and PATCH updates, deletion and negative scenarios.

Latest full suite result:

- 8 passed
- 2 failed because the response time exceeded 2 seconds
- 2 expected failures due to confirmed API validation issues

The API also showed inconsistent response times during repeated test runs.

### SQL Data Validation

Five SQL queries were used to inspect the claims dataset.

The queries identified:

- a claim submitted after the member's policy had already ended
- possible duplicate claims with the same member, provider, amount and submission date

### UI Automation

Four Sauce Demo tests were automated using Python, pytest and Playwright.

Automation result:

- 4 passed
- 0 failed

The automated tests covered successful login, locked-out user validation, adding two products to the cart and completing checkout.

## Top Risks

1. Checkout may be blocked because the Last Name field does not correctly accept input for `problem_user`.
2. Users may interact with or purchase the wrong product because product links can open incorrect product details.
3. Weak API validation may allow invalid booking data or return server errors for invalid requests.

## Release Recommendation

I would not recommend releasing the affected functionality in its current state.

The checkout blocker and incorrect product navigation are high-impact user-facing issues. The API validation problems could also affect data quality and reliability.

These issues should be fixed and retested before release.

## What I Would Test Next

I would next test:

- more cart and checkout combinations
- removal and quantity behaviour in the cart
- additional product detail navigation
- API date validation and boundary values
- repeated and concurrent booking requests
- cross-browser behaviour for the Sauce Demo application
