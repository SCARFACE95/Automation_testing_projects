# Aici facem maparea de cod la propozitie !!!

from behave import *

#Given Section
@given('login: I am on the login page')
# acum spune ce se va intampla in momentul in care gaseste propozitia asta
def step_impl(context):
    context.login_page.open()


#When sectiom
@when('login: I enter "{text}" as username')
def step_impl(context, text):
    context.login_page.set_email(text)

@when('login: I enter "{text}" as password')
def step_impl(context,text):
    context.login_page.set_password(text)

@when('login: I click the login button')
def step_impl(context):
    context.login_page.click_login_button()


#Then Section
@then('login: An error message is displayed')
def step_impl(context):
    context.login_page.verify_error_message_is_displayed()

@then('login: I should see "{text}"')
def step_impl(context, text):
    context.login_page.verify_error_message_text(text)

@then('login: The URL of the page is "{url}"')
def step_impl(context, url):
    context.login_page.verify_page_url(url)

@then('login: The title of the login page is "{title}"')
def step_impl(context, title):
    context.login_page.verify_page_title(title)

@then('login: I should land on home page')
def step_impl(context):
    context.login_page.verify_if_land_on_home_page_after_login()

