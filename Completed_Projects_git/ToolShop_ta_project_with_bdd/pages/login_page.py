from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    #Selectors
    REGISTER_LINK = (By.XPATH, '//*[text()="Register your account"]')
    LOGIN_LABEL = '//h3[text()="Login"]'
    EMAIL = (By.XPATH, '//input[@id="email"]')
    PASSWORD_LOGIN = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@data-test="login-submit"]')
    LOGIN_ERROR_LABEL = (By.XPATH, '//div[text()="Invalid email or password"]')


    #Actions
    def click_register_link(self):
        self.click(self.REGISTER_LINK)

    def type_email(self, text):
        self.type(self.EMAIL, text)

    def type_password_login(self, text):
        self.type(self.PASSWORD_LOGIN, text)


    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    #Validations

    def verify_login_label_after_register(self):
        self.wait_for_elem(self.LOGIN_LABEL, 10)
        assert self.driver.find_element(By.XPATH, self.LOGIN_LABEL).is_displayed(), 'Error, is not displayed'


    def verify_URL_after_register(self):
        expected = "https://practicesoftwaretesting.com/#/auth/login"
        actual = self.driver.current_url
        assert expected == actual, 'Error, the URL is wrong'


    def verify_error_message_is_displayed(self):
        assert self.find(self.LOGIN_ERROR_LABEL).is_displayed() , 'Error, Message is not displayed'


    def verify_error_message_text(self, expected):
        actual = self.find(self.LOGIN_ERROR_LABEL).text
        assert expected == actual, 'Error, message is different than expected'
