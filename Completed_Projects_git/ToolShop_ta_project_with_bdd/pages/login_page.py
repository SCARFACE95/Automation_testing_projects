from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    #Selectors
    REGISTER_LINK = (By.XPATH, '//*[text()="Register your account"]')
    LOGIN_LABEL = '//h3[text()="Login"]'
    LOGIN_BUTTON = (By.XPATH, '//input[@data-test="login-submit"]')
    CONTACT_BUTTON = (By.XPATH, '//a[@data-test="nav-contact"]')
    LOGIN_ERROR_LABEL = (By.XPATH, '//div[text()="Invalid email or password"]')
    EMAIL_INPUT = (By.XPATH, '//input[@id="email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@id="password"]')


    EMAIL_ERROR = (By.XPATH, '//div[@id="email-error"]')
    PASSWORD_ERROR = (By.XPATH, '//div[@id="password-error"]')





    #Actions
    def click_register_link(self):
        self.click(self.REGISTER_LINK)


    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def click_contact_button(self):
        self.click(self.CONTACT_BUTTON)


    def type_email(self,text):
        self.type(self.EMAIL_INPUT, text)

    def type_password(self, text):
        self.type(self.PASSWORD_INPUT, text)


    #Validations

    def verify_login_label_after_register(self):
        assert self.driver.find_element(By.XPATH, self.LOGIN_LABEL).is_displayed(), 'Error, is not displayed'


    def verify_URL_after_register(self):

        expected = "https://practicesoftwaretesting.com/#/auth/login"
        self.wait_url(expected)
        actual = self.driver.current_url
        assert expected == actual, 'Error, the URL is wrong'


    def verify_error_message_is_displayed(self):
        assert self.find(self.LOGIN_ERROR_LABEL).is_displayed() , 'Error, Message is not displayed'


    def verify_error_message_text(self, expected):
        actual = self.find(self.LOGIN_ERROR_LABEL).text
        assert expected == actual, 'Error, message is different than expected'



    def verify_email_error_is_displayed(self):
        assert self.find(self.EMAIL_ERROR).is_displayed(), 'Error, is not displayed'
        assert self.find(self.EMAIL_ERROR).text == 'Email is required', 'Error, text not match'

    def verify_password_error_is_displayed(self):
        assert self.find(self.PASSWORD_ERROR).is_displayed(), 'Error, is not displayed'
        assert self.find(self.PASSWORD_ERROR).text == 'Password is required', 'Error, text not match'