from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ShoppingCartPage(BasePage):

    #Selectors:
    ITEM = (By.XPATH, '//div[@class="product-item"]')
    ADD_TO_CART = (By.CSS_SELECTOR, '.add-to-cart-button')
    SUCCESS_CART_MESSAGE = (By.CLASS_NAME, 'bar-notification')
    ADDED_ITEM = (By.XPATH, '//*[@class="cart-qty"]')


    #Actions
    def click_first_item(self):

        list_elements = self.find_all(self.ITEM)
        list_elements[0].click()
    def click_add_to_cart_item(self):
        self.click(self.ADD_TO_CART)


    #Validations
    def verify_add_success_to_cart_message_is_displayed(self,expected):
        sleep(3)
        actual = self.find(self.SUCCESS_CART_MESSAGE)
        actual_text = actual.text
        print(actual_text)
        assert expected == actual.text, 'Error, The message is not the same'


    def verify_if_item_is_added_to_shopping_cart(self):
        expected_not_0 = '(0)'
        actual = self.find(self.ADDED_ITEM)
        assert expected_not_0 != actual.text, "Error, Item is not added"




