from behave import *

#Given Section
@given('Search: I am on the home page')
def step_impl(context):
    context.home_page.open()

#When Section
@when('Search: I enter "{text}" in the search field')
def step_impl(context, text):
    context.home_page.enter_search_term(text)

@when('I click the search button')
def step_impl(context):
    context.home_page.click_search_button()


#Then Section
@then('Search: I am redirected to the search results page')
def step_impl(context):
    context.search_results_page.verify_page_url_contains_text("https://demo.nopcommerce.com/search")

@then('Search: There are some results displayed')
def step_impl(context):
    context.search_results_page.verify_search_results_are_displayed()
