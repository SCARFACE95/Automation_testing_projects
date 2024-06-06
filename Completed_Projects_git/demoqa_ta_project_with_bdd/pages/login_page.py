from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

#Credentiale scarface95, pass: 123456asdASD@

class LoginPage(BasePage):
    # selectors:
    USER_INPUT = '//input[@id="userName"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    LOGIN_BUTTON = '//button[text()="Login"]'
    INVALID_CREDENTIALS_ERROR = '//p[@id="name"]'

    # actions
    def fill_user_input(self,user):
        self.wait_for_elem(self.USER_INPUT)
        self.driver.find_element(By.XPATH, self.USER_INPUT).send_keys(user)


    def fill_pass_input(self,pswd):
        self.wait_for_elem(self.PASSWORD_INPUT)
        self.driver.find_element(By.XPATH, self.PASSWORD_INPUT).send_keys(pswd)

    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

        # validations
    def validate_invalid_credentials_error(self):
        sleep(2)
        self.wait_for_elem(self.INVALID_CREDENTIALS_ERROR)
        expected = "Invalid username or password!"
        actual = self.driver.find_element(By.XPATH, self.INVALID_CREDENTIALS_ERROR).text
        self.assertEqual(expected, actual, "Error is not showed")

