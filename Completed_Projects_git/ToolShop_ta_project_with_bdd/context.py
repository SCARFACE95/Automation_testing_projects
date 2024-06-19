from browser import Browser
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage

def before_all(context):
    context.browser = Browser()
    context.base_page = BasePage()
    context.home_page = HomePage()
    context.login_page = LoginPage()
    #context.register_page = RegisterPage()


def after_all(context):
    context.browser.close()

