import random

from behave import *

#Given Section
@given("Register: I am on the register page")
def step_impl(context):
    context.register_page.open()


#When Section
@when("Register: I click Register button")
def step_impl(context):
    context.register_page.click_register_button()

@when('Register: I enter "{text}" as First Name')
def step_impl(context, text):
    context.register_page.set_first_name(text)

@when('Register: I enter "{text}" Last Name')
def step_impl(context, text):
    context.register_page.set_last_name(text)

@when('Register: I click on day of birth box')
def step_impl(context):
    context.register_page.click_on_day_of_birth_box()

@when('Register: I enter "{text}" as day o birth')
def step_impl(context, text):
    context.register_page.set_day_of_birth(text)

@when('Register: I click on month of birth box')
def step_impl(context):
    context.register_page.click_on_month_of_birth_box()

@when('Register: I enter "{text}" as month o birth')
def step_impl(context, text):
    context.register_page.set_month_of_birth(text)

@when('Register: I click on year of birth box')
def step_impl(context):
    context.register_page.click_on_year_of_birth_box()

@when('Register: I enter "{text}" as year of birth')
def step_impl(context, text):
    context.register_page.set_year_of_birth(text)

@when('Register: I enter "{text}" as new Email')
def step_impl(context, text):
    context.register_page.set_new_email(text)

@when('Register: I enter "{text}" as Company Name')
def step_impl(context, text):
    context.register_page.set_company_name(text)

@when('Register: I enter "{text}" as confirm password')
def step_impl(context, text):
    context.register_page.set_confirm_password(text)


#Then Section
@then("Register: First name mandatory error is displayed")
def step_impl(context):
    context.register_page.verify_first_name_error_displayed()


@then("Register: Last name mandatory error is displayed")
def step_impl(context):
    context.register_page.verify_last_name_error_displayed()


@then("Register: Email mandatory error is displayed")
def step_impl(context):
    context.register_page.verify_email_mandatory_error_displayed()


@then("Register: Password mandatory confirm error is displayed")
def step_impl(context):
    context.register_page.verify_password_confirm_mandatory_error_displayed()



#TEMA REGISTRATION SUCCESS


@then('Register: Success message displayed "{text}"')
def step_impl(context, text):
    context.register_page.verify_registration_success_message_is_displayed(text)








