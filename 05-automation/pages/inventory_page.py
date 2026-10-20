from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_container = page.locator('[data-test="inventory-container"]')
        self.backpack_add_button = page.locator(
            '[data-test="add-to-cart-sauce-labs-backpack"]'
        )
        self.bike_light_add_button = page.locator(
            '[data-test="add-to-cart-sauce-labs-bike-light"]'
        )
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')

    def add_backpack_to_cart(self):
        self.backpack_add_button.click()

    def add_bike_light_to_cart(self):
        self.bike_light_add_button.click()

    def open_cart(self):
        self.cart_link.click()
