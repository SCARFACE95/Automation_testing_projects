from behave import *

from pages.home_page import HomePage

home_page = HomePage()

@given('home: I am on the home page')
def step_impl(context):
    home_page.open()


#Actions
@when('home: I click on Sign In button')
def step_impl(context):
    home_page.click_sign_in_button()

@when('home: I enter "{text}" in the search field')
def step_impl(context, text):
    home_page.type_in_search_box(text)

@when('home: I click the search button')
def step_impl(context):
    home_page.click_search_button()

@when('home: I sort from A-Z')
def step_impl(context):
    home_page.sort_dropdown()

@when('home: I change the value from 100 to a lower value')
def step_impl(context):
    home_page.change_slider_value()

@when('home: I click on "{text}" box')
def step_impl(context, text):
    home_page.click_filter_by_name(text)

@when('home: I delete all filters')
def step_impl(context):
    home_page.click_delete_filter()

@when('home: I click on first product from the search list')
def step_impl(context):
    home_page.click_on_first_product_from_the_list()




#Validations

@then('home: There are some results displayed')
def step_impl(context):
    home_page.verify_search_results_are_displayed()


@then('home: I should see "{text}" < 100')
def step_impl(context, text):
    home_page.verify_slider_value(text)

@then('home: I check first element displayed if in the name contains "{text}"')
def step_impl(context, text):
    home_page.verify_first_name_after_filtering_by(expected_name=text)

