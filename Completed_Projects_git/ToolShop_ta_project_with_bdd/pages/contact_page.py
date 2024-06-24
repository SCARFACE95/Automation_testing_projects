from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from time import sleep


class ContactPage(BasePage):
    #SELECTORS

    INPUT_FIRST_NAME = (By.XPATH, '//input[@id="first_name"]')
    INPUT_LAST_NAME = (By.XPATH, '//input[@id="last_name"]')
    INPUT_EMAIL = (By.XPATH, '//input[@id="email"]')
    INPUT_SUBJECT = (By.XPATH, '//select[@id="subject"]')
    INPUT_MESSAGE = (By.XPATH, '//textarea[@id="message"]')
    INPUT_SUBMIT = (By.XPATH, '//input[@class="btnSubmit"]')
    SUCCESS_MSG = (By.XPATH, '//div[text()=" Thanks for your message! We will contact you shortly. "]')
    SUBJECT_OPTION = (By.XPATH, '//option[@value="status-of-order"]')

        #ERRORS
    ERROR_FIRST_NAME_MSG = (By.XPATH, '//div[@data-test="first-name-error"]')
    ERROR_LAST_NAME_MSG = (By.XPATH, '//div[@data-test="last-name-error"]')
    ERROR_EMAIL_MSG = (By.XPATH, '//div[@data-test="email-error"]')
    #ERROR_SUBJECT = (By.XPATH, '//div[@data-test="subject-error"]')
    ERROR_INPUT_MESSAGE = (By.XPATH, '//div[@data-test="message-error"]')


    #Actions
    def click_send_button(self):
        self.click(self.INPUT_SUBMIT)


    def type_first_name(self, text):
        self.type(self.INPUT_FIRST_NAME, text)

    def type_last_name(self, text):
        self.type(self.INPUT_LAST_NAME, text)

    def type_email(self, text):
        self.type(self.INPUT_EMAIL, text)


    def choose_subject(self):

       # dropdown_element = self.find(self.INPUT_SUBJECT)
        #select_text = Select(dropdown_element)
        #select_text.select_by_visible_text('customer-service')
        self.click(self.INPUT_SUBJECT)
        self.click(self.SUBJECT_OPTION)

    def type_message(self, text):
        self.type(self.INPUT_MESSAGE, text)



    #Validations
    def verify_error_first_name_is_displayed(self):
        sleep(3)
        assert self.find(self.ERROR_FIRST_NAME_MSG).is_displayed(), 'Error, is not displayed'
        assert self.find(self.ERROR_FIRST_NAME_MSG).text == 'First name is required', 'Error, text not match'

    def verify_error_last_name_is_displayed(self):
        assert self.find(self.ERROR_LAST_NAME_MSG).is_displayed(), 'Error, is not displayed'
        assert self.find(self.ERROR_LAST_NAME_MSG).text == 'Last name is required', 'Error, text not match'

    def verify_error_last_name_is_displayed(self):
        assert self.find(self.ERROR_LAST_NAME_MSG).is_displayed(), 'Error, is not displayed'
        assert self.find(self.ERROR_LAST_NAME_MSG).text == 'Last name is required', 'Error, text not match'

    def verify_error_email_is_displayed(self):
        assert self.find(self.ERROR_EMAIL_MSG).is_displayed(), 'Error, is not displayed'
        assert self.find(self.ERROR_EMAIL_MSG).text == 'Email is required', 'Error, text not match'


    def verify_error_message_is_displayed(self):
        assert self.find(self.ERROR_INPUT_MESSAGE).is_displayed(), 'Error, is not displayed'
        assert self.find(self.ERROR_INPUT_MESSAGE).text == 'Message is required', 'Error, text not match'


    def verify_success_message_displayed_msg(self,expected_text):
        assert self.find(self.SUCCESS_MSG).is_displayed(), 'Error, is not displayed'
        actual_text = self.find(self.SUCCESS_MSG).text
        print(actual_text)
        assert actual_text == expected_text, 'Error, text not match'