from behave import *

#din home page dau click pe Shopping cart

@given('Home: I am on the home page')
def step_impl(context):
    context.home_page.open()


@when('Home: I enter "{text}" in the search field')
def step_impl(context, text):
    context.home_page.enter_search_term(text)

@when('Home: I click the search button')
def step_impl(context):
    context.home_page.click_search_button()