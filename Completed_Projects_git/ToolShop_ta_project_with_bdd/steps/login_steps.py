from behave import *

from pages.base_page import BasePage
from pages.login_page import LoginPage

base_page = BasePage()
login_page = LoginPage()
@Then('login: The URL page is "{url}"')
def step_impl(context, url):
    base_page.verify_page_url(url)

@Then('login: An error message is displayed')
def step_impl(context):
    login_page.verify_error_message_is_displayed()

@Then('login: I should see "{text}"')
def step_impl(context, text):
    login_page.verify_error_message_text(text)

@When('login: I click on Register your account link')
def step_impl(context):
    login_page.click_register_link()

@When('login: I enter "{text}" as Email Address')
def step_impl(context, text):
    login_page.type_email(text)

@When('login: I enter "{text}" as Password')
def step_impl(context, text):
    login_page.type_password_login(text)

@When('login: I click on the login button')
def step_impl(context):
    login_page.click_login_button()
