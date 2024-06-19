from time import sleep

from behave import *

from pages.account_page import AccountPage
from pages.base_page import BasePage

#Then

base_page = BasePage()
account_page = AccountPage()
@Then('account: The URL page is "{url}"')
def step_impl(context, url):
    base_page.verify_page_url(url)

@Then('account: I should see My account in the page')
def step_impl(context):
    account_page.verify_my_account_lable_is_displayed()



#When