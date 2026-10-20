from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_standard_user_can_login(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(inventory_page.inventory_container).to_be_visible()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_locked_out_user_sees_error(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    expect(login_page.error_message).to_contain_text(
        "Sorry, this user has been locked out."
    )


def test_standard_user_can_add_two_products_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()

    expect(inventory_page.cart_badge).to_have_text("2")


def test_standard_user_can_complete_checkout(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    expect(cart_page.cart_items).to_have_count(1)

    cart_page.proceed_to_checkout()

    checkout_page.enter_customer_information("Test", "User", "00100")

    checkout_page.finish_checkout()

    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")
