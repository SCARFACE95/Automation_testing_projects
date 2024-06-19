from behave import *

from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage

base_page = BasePage()
checkout_page = CheckoutPage()
@Then('checkout: I land on checkout page')
def step_impl(context):
    base_page.verify_page_url('https://practicesoftwaretesting.com/#/checkout')
    base_page.verify_page_title('Checkout - Practice Software Testing - Toolshop - v5.0')


@Then('checkout: I should see "{text}"')
def step_impl(context,text):
    checkout_page.verify_success_payment_message(text)



@When('checkout: I click to "Proceed to checkout"')
def step_impl(context):
    checkout_page.click_proceed_to_checkout_button()


@When('checkout: I click to "Proceed to checkout 2"')
def step_impl(context):
    checkout_page.click_proceed_to_checkout_button2()

@When('checkout: I click to "Proceed to checkout 3"')
def step_impl(context):
    checkout_page.click_proceed_to_checkout_button3()


@When('checkout: Select payment method as cash on delivery')
def step_impl(context):
    checkout_page.choose_payment_option()

@When('checkout: I click on confirm button')
def step_impl(context):
    checkout_page.click_on_confirm_button()