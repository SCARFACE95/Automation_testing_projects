from pages import home_page
from pages.home_page import HomePage
from behave import *

home_page = HomePage()



@given('home: I am an user on home page')
def step_impl(context):
    home_page.navigate_to_home_page()

@when('home: I click bookstore application')
def step_impl(context):
    home_page.click_book_store_application_card()

