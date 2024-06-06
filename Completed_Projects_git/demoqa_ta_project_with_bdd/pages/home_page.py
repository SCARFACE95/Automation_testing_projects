from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    # selectors:
    BOOK_STORE_APPLICATION_CARD = '//h5[text()="Book Store Application"]'

    # actions
    def navigate_to_home_page(self):
        self.driver.delete_all_cookies() #Delete all coockies before open the site
        self.driver.get('https://demoqa.com')

    def click_book_store_application_card(self):
        self.wait_for_elem(self.BOOK_STORE_APPLICATION_CARD)
        element = self.driver.find_element(By.XPATH, self.BOOK_STORE_APPLICATION_CARD)
        self.driver.execute_script("arguments[0].click();", element)
        #self.driver.find_element(By.XPATH, self.BOOK_STORE_APPLICATION_CARD).click() #dau click pe el






