from time import sleep

from selenium.webdriver.common.by import By

from browser import Browser
from pages.base_page import BasePage


# definesc pagina de login CU DESIGN PATTERN PAGE OBJECT MODEL
# aici se pune doar cod care are de a face doar cu pagina html
# prin urmare driver-ul nu se creeaza aici  si se creaza intr-un fisier separat!!!

class LoginPage(BasePage):  # Mosteneste clasa BasPage care mosteneste clasa Broswer unde e definit driver-ul
    #Selectors
    INPUT_EMAIL = (By.ID, "Email")
    INPUT_PASSWORD = (By.ID, "Password")
    BUTTON_LOGIN = (By.CLASS_NAME, "login-button")
    ERROR_MESSAGE = (
    By.CSS_SELECTOR, "div.message-error li")  # Din div accesez clasa message-error si ma duc in elementul li
    TITLE_PAGE_LOGIN = (By.ID, '//title[text()="nopCommerce demo store. Login"]')

    # Here we are creating the methods for actions and validations

    # Actions
    def open(self):
        self.driver.get("https://demo.nopcommerce.com/login")

    def set_email(self, text):  # Unde e textul se scrie EMAIL-ul
        self.type(self.INPUT_EMAIL, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def click_login_button(self):
        self.click(self.BUTTON_LOGIN)


    #Validations
    def verify_error_message_is_displayed(self):
        assert self.find(self.ERROR_MESSAGE).is_displayed(), "Error message is not displayed"

    def verify_error_message_text(self, expected):
        actual = self.find(self.ERROR_MESSAGE).text
        assert expected == actual


    def verify_if_land_on_home_page_after_login(self):
        expected_url = 'https://demo.nopcommerce.com/'
        print(self.driver.current_url)
        assert expected_url == self.driver.current_url, "Error, URL is not correct"