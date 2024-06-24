from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):

    #SELECTORS
    PRODUCT_NAME = (By.XPATH, '//h1[@data-test="product-name"]')
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[@data-test="add-to-cart"]')
    ALERT_MESSAGE = (By.XPATH, '//div[@role="alert"]')
    CART_CHECKOUT = (By.XPATH, '//span[@id="lblCartCount"]')
    #ACTIONS
    def click_on_add_to_cart_button(self):
        self.wait_for_elem(self.ADD_TO_CART_BUTTON,10)
        self.click(self.ADD_TO_CART_BUTTON)

    def click_on_cart_checkout_button(self):
        self.click(self.CART_CHECKOUT)


    #VALIDATIONS
    def verify_product_name(self, expected):
        #sleep(3)
        self.wait_for_element_presence(self.PRODUCT_NAME, 10)
        actual = self.find(self.PRODUCT_NAME).text
        print(actual)
        assert actual == expected, 'Unexpected Error'

    def verify_message_alert_is_displayed(self):
        self.wait_for_elem(self.ALERT_MESSAGE, 10)
        assert self.find(self.ALERT_MESSAGE).is_displayed(), 'Unexpected Error'

    def verify_message_alert_text(self, expected):
        actual = self.find(self.ALERT_MESSAGE).text
        assert actual == expected, 'Unexpected Error'

    def verify_checkout_cart_is_displayed(self):
        self.find(self.CART_CHECKOUT).is_displayed()

    def verify_quantity_from_checkout_cart(self):
        quantity = int(self.find(self.CART_CHECKOUT).text)
        assert quantity > 0, 'Unexpected error'




