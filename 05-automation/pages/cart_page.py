from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.cart_items = page.locator('[data-test="inventory-item"]')

    def proceed_to_checkout(self):
        self.checkout_button.click()
