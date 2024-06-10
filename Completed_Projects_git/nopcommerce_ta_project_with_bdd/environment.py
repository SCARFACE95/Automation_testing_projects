#vreau sa accesez mai multe obiecte in fisiere cu Context!!
#Aici implementez procedura cu Context

from browser import Browser
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.search_results_page import SearchResultsPage
from pages.shopping_cart_page import ShoppingCartPage


#Metoda asta before all va rula inainte de fiecare feature,
#Practic aici vom pute accesa ce am listat din alte fisiere
def before_all(context):
    context.browser = Browser() #aici instantiem in driver, si va deschide un browser
    context.login_page = LoginPage()
    context.register_page = RegisterPage()
    context.home_page = HomePage()
    context.search_results_page = SearchResultsPage()
    context.shopping_cart_page = ShoppingCartPage()



def after_all(context):
    context.browser.close()