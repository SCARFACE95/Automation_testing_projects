from behave import *

from pages.home_page import HomePage
from pages.product_page import ProductPage

home_page = HomePage()
product_page = ProductPage()

@when('product: I click to Add to cart button')
def step_impl(context):
    product_page.click_on_add_to_cart_button()


@when('product: I click on cart checkout button')
def step_impl(context):
    product_page.click_on_cart_checkout_button()






@then('product: I should see "{text}" as product name')
def step_impl(context, text):
    product_page.verify_product_name(text)
@then('product: I should see "{text}" as message')
def step_impl(context, text):
    product_page.verify_message_alert_is_displayed()
    product_page.verify_message_alert_text(text)

@then('product: I check the cart with 1 item')
def step_impl(context):
    product_page.verify_checkout_cart_is_displayed()
    product_page.verify_quantity_from_checkout_cart()


@then('product: The URL page contains "{text}"')
def step_impl(context, text):
    home_page.verify_page_url_contains(text)
