from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class HomePage(BasePage):

    #Selectors:
    SIGN_IN_BUTTON = (By.XPATH, '//*[@routerlink="/auth/login"]')
    SEARCH_BOX = (By.XPATH, '//input[@id="search-query"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@data-test="search-submit"]')
    CLASS_PRODUCT_CARD = (By.XPATH, '//*[@class="card"]')
    SORT_BOX = (By.XPATH, '//select[@data-test="sort"]')
    SLIDER_BOX = (By.XPATH, '//div[@class="input-group mb-3"]')
    SLIDER_VALUE = (By.XPATH, '//span[@class="ngx-slider-span ngx-slider-bubble ngx-slider-model-high"]')
    DELETE_FILTER_BUTTON = (By.XPATH, '//button[@data-test="search-reset"]')

    #Actions:
    def open(self):
        self.driver.get("https://practicesoftwaretesting.com/#")


    def click_sign_in_button(self):
        self.click(self.SIGN_IN_BUTTON)


    def type_in_search_box(self, text):
        self.type(self.SEARCH_BOX, text)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)


    def sort_dropdown(self):
        dropdown_sort = Select(self.find(self.SORT_BOX))
        dropdown_sort.select_by_visible_text('Name (A - Z)')


    def change_slider_value(self):
        #From Chat GPT
        list_elem = self.find_all(self.SLIDER_BOX)
        elem = list_elem[1]

        # Create ActionChains object
        actions = ActionChains(self.driver)
        sleep(1)
        # Move the slider (adjust xoffset as needed)
        actions.click_and_hold(elem).move_by_offset(-20, 0).release().perform()
        sleep(1)


    def click_filter_by_name(self, name): #'//label[text()=" Hammer "]'
      self.driver.find_element(By.XPATH, '//label[text()="' + name + '"]').click()
      name.replace(' ', '')


    def click_delete_filter(self):
        self.click(self.DELETE_FILTER_BUTTON)
        sleep(3)


    def click_on_first_product_from_the_list(self):
        self.wait_for_elem(self.CLASS_PRODUCT_CARD, 10)
        self.click(self.CLASS_PRODUCT_CARD)


    #Validations
    def verify_search_results_are_displayed(self):
        #self.wait_for_elem(self.CLASS_PRODUCT_CARD_1, 10)
        sleep(3)
        results_list = self.find_all(self.CLASS_PRODUCT_CARD)
        assert len(results_list) > 0, "Unexpected error"

    def verify_slider_value(self, expected):
        value = self.find(self.SLIDER_VALUE).text
        assert value == expected, 'Unexpected error'


    def verify_first_name_after_filtering_by(self, expected_name):
        sleep(3)
        list_of_elements = self.find_all(self.CLASS_PRODUCT_CARD)
        first_element = list_of_elements[0]
        actual_name = first_element.text
        assert expected_name in actual_name, "Unexpected error"


