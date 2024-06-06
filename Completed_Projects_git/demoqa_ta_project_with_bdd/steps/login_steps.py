
from pages.login_page import LoginPage
from behave import *

login_page = LoginPage()

@when('login: I login with valid user "{user}" and pass "{pswd}"')
def step_impl(context, user, pswd):
   login_page.fill_user_input(user)
   login_page.fill_pass_input(pswd)
   login_page.click_login_button()




@then('login: I validate that error message is displayed')
def step_impl(context):
   login_page.validate_invalid_credentials_error()




