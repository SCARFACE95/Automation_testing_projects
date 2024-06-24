import random
from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage



class RegisterPage(BasePage):
    #Selectors
    FIRST_NAME = (By.XPATH, '//input[@id="first_name"]')
    LAST_NAME = (By.XPATH, '//input[@id="last_name"]')
    ADDRESS = (By.XPATH, '//input[@id="address"]')
    POST_CODE = (By.XPATH, '//input[@id="postcode"]')
    CITY = (By.XPATH, '//input[@id="city"]')
    STATE = (By.XPATH, '//input[@id="state"]')
    PHONE = (By.XPATH, '//input[@id="phone"]')
    USERNAME = (By.XPATH, '//input[@id="email"]')
    PASSWORD = (By.XPATH, '//input[@id="password"]')
    REGISTER_BUTTON = (By.XPATH, '//button[@data-test="register-submit"]')
    COUNTRY_LABEL = (By.XPATH, '//*[@id="country"]')
    COUNTRY = (By.XPATH, '//*[@value="RO"]')
    BIRTH_DAY = (By.XPATH, '//*[@id="dob"]')

    #Mandatory fields selectors
    ERROR_FIRST_NAME = (By.XPATH, '//div[text()=" First name is required "]')
    ERROR_LAST_NAME = (By.XPATH, '//div[text()=" fields.last-name.required "]')
    ERROR_BIRTH = (By.XPATH, '//div[text()=" Date of Birth is required "]')
    ERROR_ADDRESS = (By.XPATH, '//div[text()=" Address is required "]')
    ERROR_POST_CODE = (By.XPATH, '//div[text()=" Postcode is required "]')
    ERROR_CITY = (By.XPATH, '//div[text()=" City is required "]')
    ERROR_STATE = (By.XPATH, '//div[text()=" State is required "]')
    ERROR_COUNTRY = (By.XPATH, '//div[text()=" Country is required "]')
    ERROR_PHONE = (By.XPATH, '//div[text()=" Phone is required. "]')
    ERROR_USERNAME = (By.XPATH, '//div[text()=" Email is required "]')
    ERROR_PASSWORD = (By.XPATH, '//div[text()=" Password is required "]')





    #Actions
    def type_first_name(self, text):
        self.type(self.FIRST_NAME, text)
    def type_last_name(self, text):
        self.type(self.LAST_NAME, text)
    def type_address(self, text):
        self.type(self.ADDRESS, text)
    def type_post_code(self, text):
        self.type(self.POST_CODE, text)

    def type_city(self, text):
        self.type(self.CITY, text)
    def type_state(self, text):
        self.type(self.STATE, text)
    def type_phone(self, text):
        self.type(self.PHONE, text)
    def type_username(self):
        random_number = str(random.randint(1,10000000000000))
        username = f"robertbst{random_number}@yahoo.com"
        self.type(self.USERNAME, username)
    def type_password(self, text):
        self.type(self.PASSWORD, text)
    def select_country(self):
        self.click(self.COUNTRY_LABEL)
        self.click(self.COUNTRY)
    def click_register_button(self):
        self.click(self.REGISTER_BUTTON)
    def type_date_of_bday(self,text):
        self.type(self.BIRTH_DAY, text)


    #Validations
    def verify_first_name_error_displayed(self):
        assert self.find(self.ERROR_FIRST_NAME).is_displayed(), 'Error, is not displayed'
        assert self.find(self.ERROR_FIRST_NAME).text == 'First name is required', 'Error, text not match'

    def verify_last_name_error_displayed(self):
        assert self.find(self.ERROR_LAST_NAME).is_displayed(), 'Error, is not displayed'
        print(self.find(self.ERROR_LAST_NAME).text)
        assert self.find(self.ERROR_LAST_NAME).text == 'fields.last-name.required', 'Error, text not match'

    def verify_birth_error_displayed(self):
        assert self.find(self.ERROR_BIRTH).is_displayed(), 'Error, is not displayed'
        print(self.find(self.ERROR_BIRTH).text)
        assert self.find(self.ERROR_BIRTH).text == 'Date of Birth is required', 'Error, text not match'

    def verify_address_error_displayed(self):
        assert self.find(self.ERROR_ADDRESS).is_displayed(), 'Error, is not displayed'
        print(self.find(self.ERROR_ADDRESS).text)
        assert self.find(self.ERROR_ADDRESS).text == 'Address is required', 'Error, text not match'

    def verify_post_code_error_displayed(self):
        assert self.find(self.ERROR_POST_CODE).is_displayed(), 'Error, is not displayed'
        print(self.find(self.ERROR_POST_CODE).text)
        assert self.find(self.ERROR_POST_CODE).text == 'Postcode is required', 'Error, text not match'

    def verify_city_error_displayed(self):
        assert self.find(self.ERROR_CITY).is_displayed(), 'Error, is not displayed'
        print(self.find(self.ERROR_CITY).text)
        assert self.find(self.ERROR_CITY).text == 'City is required', 'Error, text not match'

    def verify_state_error_displayed(self):
        assert self.find(self.ERROR_STATE).is_displayed(), 'Error, is not displayed'
        print(self.find(self.ERROR_STATE).text)
        assert self.find(self.ERROR_STATE).text == 'State is required', 'Error, text not match'

    def verify_country_error_displayed(self):
        assert self.find(self.ERROR_COUNTRY).is_displayed(), 'Error, is not displayed'
        print(self.find(self.ERROR_COUNTRY).text)
        assert self.find(self.ERROR_COUNTRY).text == 'Country is required', 'Error, text not match'

    def verify_phone_error_displayed(self):
        assert self.find(self.ERROR_PHONE).is_displayed(), 'Error, is not displayed'
        print(self.find(self.ERROR_PHONE).text)
        assert self.find(self.ERROR_PHONE).text == 'Phone is required.', 'Error, text not match'

    def verify_username_error_displayed(self):
        assert self.find(self.ERROR_USERNAME).is_displayed(), 'Error, is not displayed'
        print(self.find(self.ERROR_USERNAME).text)
        assert self.find(self.ERROR_USERNAME).text == 'Email is required', 'Error, text not match'

    def verify_password_error_displayed(self):
        assert self.find(self.ERROR_PASSWORD).is_displayed(), 'Error, is not displayed'
        print(self.find(self.ERROR_PASSWORD).text)
        assert self.find(self.ERROR_PASSWORD).text == 'Password is required', 'Error, text not match'
