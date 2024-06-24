from behave import *

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

base_page = BasePage()
register_page = RegisterPage()
login_page = LoginPage()

#Given

#When
@When('register: I enter "{text}" as First Name')
def step_impl(context, text):
    register_page.type_first_name(text)

@When('register: I enter "{text}" as Last Name')
def step_impl(context, text):
    register_page.type_last_name(text)

@When('register: I enter "{text}" as Address')
def step_impl(context, text):
    register_page.type_address(text)

@When('register: I enter "{034231}" as Post Code')
def step_impl(context, text):
    register_page.type_post_code(text)

@When('register: I enter "{text}" as City')
def step_impl(context, text):
    register_page.type_city(text)

@When('register: I enter "{text}" as State')
def step_impl(context, text):
    register_page.type_state(text)


@When('register: I enter "{text}" as Phone')
def step_impl(context, text):
    register_page.type_phone(text)

@When('register: I enter a random Email Address')
def step_impl(context):
    register_page.type_username()


@When('register: I enter "{text}" as Password')
def step_impl(context, text):
    register_page.type_password(text)

@When('register: I select RO country')
def step_impl(context):
    register_page.select_country()

@When('register: I enter "{text}" as birth day')
def step_impl(context, text):
    register_page.type_date_of_bday(text)


@When('register: I click to register button')
def step_impl(context):
    register_page.click_register_button()




#Then
@Then('register: I land on the customer registration page')
def step_impl(context):
    base_page.verify_page_url('https://practicesoftwaretesting.com/#/auth/register')
    base_page.verify_page_title('Register - Practice Software Testing - Toolshop - v5.0')

@Then('login: I should land on login page')
def step_impl(context):
    login_page.verify_URL_after_register()
    login_page.verify_login_label_after_register()





@Then('register: First name mandatory error is displayed')
def step_impl(context):
    register_page.verify_first_name_error_displayed()

@Then('register: Last name mandatory error is displayed')
def step_impl(context):
    register_page.verify_last_name_error_displayed()


@Then('register: Birth mandatory error is displayed')
def step_impl(context):
    register_page.verify_birth_error_displayed()

@Then('register: Address mandatory error is displayed')
def step_impl(context):
    register_page.verify_address_error_displayed()

@Then('register: Post code mandatory error is displayed')
def step_impl(context):
    register_page.verify_post_code_error_displayed()

@Then('register: City mandatory error is displayed')
def step_impl(context):
    register_page.verify_city_error_displayed()

@Then('register: State mandatory error is displayed')
def step_impl(context):
    register_page.verify_state_error_displayed()

@Then('register: Country mandatory error is displayed')
def step_impl(context):
    register_page.verify_country_error_displayed()

@Then('register: Phone mandatory error is displayed')
def step_impl(context):
    register_page.verify_phone_error_displayed()

@Then('register: Email mandatory error is displayed')
def step_impl(context):
    register_page.verify_username_error_displayed()

@Then('register: Password mandatory error is displayed')
def step_impl(context):
    register_page.verify_password_error_displayed()