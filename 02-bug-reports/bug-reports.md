# Bug Reports

## Bug 1: All products display the same incorrect image for problem_user

### Environment
- Browser: Google Chrome 150.0.7871.186 
- Operating System: Linux
- Screen Size: [1920x1200]

### Preconditions
- User is on the Sauce Demo login page.
- User has valid `problem_user` credentials.

### Steps to Reproduce
1. Open Sauce Demo.
2. Log in as `problem_user`.
3. Open the Products page.
4. Observe the images displayed beside each product.
5. Log out.
6. Log in as `standard_user`.
7. Compare the product images.

### Expected Result
Each product should display the image that matches the product, as seen when logged in as `standard_user`.

### Actual Result
All products display the same dog image when logged in as `problem_user`.

### Severity
Medium — users can still view and purchase products, but the incorrect images make it difficult to identify products visually.

### Priority
Medium — the issue should be fixed because product images are an important part of the shopping experience.

### Evidence
See screenshot: `evidence/bug-01-problem-user-images.png`

## Bug 2: Sauce Labs Bolt T-Shirt cannot be added to the cart by problem_user

### Environment
- Browser: Google Chrome 150.0.7871.186
- Operating System: Linux
- Screen Size: 1920x1200

### Preconditions
- User is on the Sauce Demo login page.
- User has valid `problem_user` credentials.

### Steps to Reproduce
1. Open Sauce Demo.
2. Log in as `problem_user`.
3. Go to the Products page.
4. Find `Sauce Labs Bolt T-Shirt`.
5. Click `Add to cart`.

### Expected Result
The Sauce Labs Bolt T-Shirt should be added to the cart.

The button should change from `Add to cart` to `Remove`, and the cart badge should increase by 1.

### Actual Result
The Sauce Labs Bolt T-Shirt is not added to the cart.

The button remains `Add to cart`, and the cart badge does not increase for that product.

### Severity
Medium — the user cannot purchase this product, although other products can still be added to the cart.

### Priority
Medium — the issue affects a core shopping action for a specific product and should be fixed before release.

### Evidence
See screenshot: `evidence/bug-02-add-to-cart.png`

## Bug 3: Last Name field does not accept input during checkout for problem_user

### Environment
- Browser: Google Chrome 150.0.7871.186
- Operating System: Linux
- Screen Size: 1920x1200

### Preconditions
- User is logged in as `problem_user`.
- At least one product has been added to the cart.
- User is on the Checkout: Your Information page.

### Steps to Reproduce
1. Open Sauce Demo.
2. Log in as `problem_user`.
3. Add a product to the cart.
4. Open the cart.
5. Click `Checkout`.
6. Enter a value in the First Name field.
7. Enter a value in the Last Name field.
8. Enter a valid Postal Code.
9. Click `Continue`.

### Test Data
- First Name: Test
- Last Name: User
- Postal Code: 00100

### Expected Result
The Last Name field should accept the entered value and allow the user to continue to the next checkout step.

### Actual Result
The Last Name field does not retain the entered value.

When `Continue` is clicked, the page shows the error:

`Error: Last Name is required`

The user cannot continue with checkout.

### Severity
High — the user is blocked from completing the checkout process.

### Priority
High — checkout is a core shopping flow, so this should be fixed before release.

### Evidence
See screenshot: `evidence/bug-03-last-name-field.png`

## Bug 4: Product sorting does not work for problem_user

### Environment
- Browser: Google Chrome 150.0.7871.186
- Operating System: Linux
- Screen Size: 1920x1200

### Preconditions
- User is logged in as `problem_user`.
- User is on the Products page.

### Steps to Reproduce
1. Open Sauce Demo.
2. Log in as `problem_user`.
3. Go to the Products page.
4. Open the sorting dropdown.
5. Select `Name (Z to A)`.
6. Observe the product order.
7. Repeat using `Price (low to high)` and `Price (high to low)`.

### Expected Result
The product list should change according to the selected sorting option.

For example, when `Price (low to high)` is selected, the products should be ordered from the lowest price to the highest price.

### Actual Result
The product order does not change after selecting a different sorting option.

The dropdown also continues to display `Name (A to Z)`.

### Severity
Medium — users can still view and purchase products, but they cannot sort the product list as expected.

### Priority
Medium — the issue affects product browsing and should be fixed before release.

### Evidence
See screenshot: `evidence/bug-04-sorting-not-working.png`

## Bug 5: Clicking Sauce Labs Backpack opens the wrong product details page for problem_user

### Environment
- Browser: Google Chrome 150.0.7871.186
- Operating System: Linux
- Screen Size: 1920x1200

### Preconditions
- User is logged in as `problem_user`.
- User is on the Products page.

### Steps to Reproduce
1. Open Sauce Demo.
2. Log in as `problem_user`.
3. Go to the Products page.
4. Click `Sauce Labs Backpack`.

### Expected Result
The Sauce Labs Backpack details page should open and display the backpack name, image, description and price.

### Actual Result
The user is redirected to the Sauce Labs Fleece Jacket details page instead.

The page shows the Fleece Jacket name, image, description and price rather than the Backpack details.

### Severity
High — the user is taken to the wrong product, which can cause confusion and incorrect purchases.

### Priority
High — product navigation is a core shopping function and should be fixed before release.

### Evidence
See screenshots:
- `evidence/bug-05-backpack-click.png`
- `evidence/bug-05-wrong-product-details.png`
