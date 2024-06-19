from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    #SELECTORS
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, '//button[@data-test="proceed-1"]')
    PROCEED_TO_CHECKOUT_BUTTON2 = (By.XPATH, '//button[@data-test="proceed-2"]')
    PROCEED_TO_CHECKOUT_BUTTON3 = (By.XPATH, '//button[@data-test="proceed-3"]')
    STEP1 = (By.XPATH, '//li[@class="ng-star-inserted done navigable"]//div[text()="Cart"]')
    STEP2 = (By.XPATH, '//li[@class="ng-star-inserted done navigable"]//div[text()="Sign in"]')
    STEP3 = (By.XPATH, '//li[@class="ng-star-inserted done navigable"]//div[text()="Billing Address"]')
    PAYMENT = (By.XPATH, '//select[@data-test="payment-method"]')
    PAYMENT_DELIVERY = (By.XPATH, '//option[@value="cash-on-delivery"]')
    PAYMENT_SUCCESS_MESSAGE = (By.XPATH, "//div[@class='help-block']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()=' Confirm ']")


    #Actions

    def click_proceed_to_checkout_button(self):
        self.wait_for_elem(self.PROCEED_TO_CHECKOUT_BUTTON, 10)
        self.click(self.PROCEED_TO_CHECKOUT_BUTTON)

    def click_proceed_to_checkout_button2(self):
        self.wait_for_elem(self.PROCEED_TO_CHECKOUT_BUTTON2, 10)
        self.click(self.PROCEED_TO_CHECKOUT_BUTTON2)

    def click_proceed_to_checkout_button3(self):
        self.wait_for_element_presence(self.PROCEED_TO_CHECKOUT_BUTTON3, 5)
        self.click(self.PROCEED_TO_CHECKOUT_BUTTON3)

    def choose_payment_option(self):
        #dropdown = Select(self.find(self.PAYMENT))
        self.click(self.PAYMENT)
        self.click(self.PAYMENT_DELIVERY)

    def click_on_confirm_button(self):
        self.click(self.CONFIRM_BUTTON)




    #Verifications
    def verify_success_payment_message(self, expected):
        actual = self.find(self.PAYMENT_SUCCESS_MESSAGE).text
        assert actual == expected, "Unexpected error"