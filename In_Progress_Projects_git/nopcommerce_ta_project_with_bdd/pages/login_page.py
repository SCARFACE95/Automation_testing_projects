from selenium.webdriver.common.by import By

from browser import Browser
from pages.base_page import BasePage


# definesc pagina de login CU DESIGN PATTERN PAGE OBJECT MODEL
# aici se pune doar cod care are de a face doar cu pagina html
# prin urmare driver-ul nu se creeaza aici  si se creaza intr-un fisier separat!!!

class LoginPage(BasePage):  # Mosteneste clasa BasPage care mosteneste clasa Broswer unde e definit driver-ul

    INPUT_EMAIL = (By.ID, "Email")
    INPUT_PASSWORD = (By.ID, "Password")
    BUTTON_LOGIN = (By.CLASS_NAME, "login-button")
    ERROR_MESSAGE = (
    By.CSS_SELECTOR, "div.message-error li")  # Din div accesez clasa message-error si ma duc in elementul li

    # creez metodele care interactioneaza cu fiecare element

    # Metoda asta va deschide pagina de login
    def open(self):
        self.driver.get("https://demo.nopcommerce.com/login")

    def set_email(self, text):  # Unde e textul se scrie EMAIL-ul
        self.type(self.INPUT_EMAIL, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def click_login_button(self):
        self.click(self.BUTTON_LOGIN)

    def verify_error_message_is_displayed(self):
        assert self.find(self.ERROR_MESSAGE).is_displayed(), "Error message is not displayed"

    def verify_error_message_text(self, expected):
        actual = self.find(self.ERROR_MESSAGE).text
        assert expected == actual


