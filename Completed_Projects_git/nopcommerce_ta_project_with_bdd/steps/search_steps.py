from behave import *

#Given Section

#When Section


#Then Section
@then('Search: I am redirected to the search results page')
def step_impl(context):
    context.search_results_page.verify_page_url_contains_text("https://demo.nopcommerce.com/search")

@then('Search: There are some results displayed')
def step_impl(context):
    context.search_results_page.verify_search_results_are_displayed()
