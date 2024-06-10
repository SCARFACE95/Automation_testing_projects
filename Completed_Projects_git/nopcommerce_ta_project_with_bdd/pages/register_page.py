import random
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class RegisterPage(BasePage):
    #Selectors
    #Mandatory field selectors
    ERROR_FIRST_NAME = (By.XPATH, '//span[@id="FirstName-error"]')
    ERROR_LAST_NAME = (By.ID, "LastName-error")
    EMAIL_ERROR = (By.ID, "Email-error")
    PASSWORD_CONFIRM_ERROR = (By.ID, "ConfirmPassword-error")
    BUTTON_REGISTER = (By.ID, "register-button")

    #Rest of selectors
    INPUT_FIRST_NAME = (By.ID, "FirstName")
    INPUT_LAST_NAME = (By.ID, "LastName")
    INPUT_R_EMAIL = (By.ID, "Email")
    INPUT_COMPANY_NAME = (By.ID, "Company")
    INPUT_R_CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    LABEL_REGISTRATION_SUCCESS = (By.XPATH, "//div[text()='Your registration completed']")

    #Input day, month,year selectors
    INPUT_DAY = (By.XPATH, "//select[@name='DateOfBirthDay']")
    INPUT_MONTH = (By.XPATH, "//select[@name='DateOfBirthMonth']")
    INPUT_YEAR = (By.XPATH, "//select[@name='DateOfBirthYear']")



    #Actions
    def open(self):
        self.driver.get("https://demo.nopcommerce.com/register")

    def click_register_button(self):
        self.click(self.BUTTON_REGISTER)

    def set_first_name(self, text):
        self.type(self.INPUT_FIRST_NAME, text)

    def set_last_name(self, text):
        self.type(self.INPUT_LAST_NAME, text)

    def set_company_name(self, text):
        self.type(self.INPUT_COMPANY_NAME, text)

    def set_new_email(self, text):
        self.type(self.INPUT_R_EMAIL, text)

    def set_confirm_password(self, text):
        self.type(self.INPUT_R_CONFIRM_PASSWORD, text)

    def click_on_day_of_birth_box(self):
        self.click(self.INPUT_DAY)

    def set_day_of_birth(self, text):
        self.select_dropdown_text(self.INPUT_DAY, text)

    def click_on_month_of_birth_box(self):
        self.click(self.INPUT_MONTH)

    def set_month_of_birth(self, text):
        self.select_dropdown_text(self.INPUT_MONTH, text)

    def click_on_year_of_birth_box(self):
        self.click(self.INPUT_YEAR)

    def set_year_of_birth(self, text):
        self.select_dropdown_text(self.INPUT_YEAR, text)



    #Validations
    def verify_first_name_error_displayed(self):
        self.wait_for_elem(self.ERROR_FIRST_NAME)
        assert self.find(self.ERROR_FIRST_NAME).is_displayed(), "First name error is not displayed"
        assert self.find(self.ERROR_FIRST_NAME).text == "First name is required."

    def verify_last_name_error_displayed(self):
        assert self.find(self.ERROR_LAST_NAME).is_displayed(), "Last name error is not displayed"
        assert self.find(self.ERROR_LAST_NAME).text == "Last name is required."

    def verify_email_mandatory_error_displayed(self):
        assert self.find(self.EMAIL_ERROR).is_displayed(), "Email error is not displayed"
        assert self.find(self.EMAIL_ERROR).text == "Email is required."

    def verify_password_confirm_mandatory_error_displayed(self):
        assert self.find(self.PASSWORD_CONFIRM_ERROR).is_displayed(), "Password confirm error is not displayed"
        assert self.find(self.PASSWORD_CONFIRM_ERROR).text == "Password is required."

    def verify_registration_success_message_is_displayed(self, expected):

        assert self.find(self.LABEL_REGISTRATION_SUCCESS).is_displayed()
        actual = self.find(self.LABEL_REGISTRATION_SUCCESS).text
        assert expected == actual


