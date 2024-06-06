from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LeftPage(BasePage):
    # selectors:
    LOGIN_BUTTON = '//button[@id="login"]'
    PROFILE_BUTTON = '//span[text()="Profile"]'

    # actions
    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)  # astept sa se incarce elementul
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

    def click_profile_button(self):
        self.wait_for_elem(self.PROFILE_BUTTON)  # astept sa se incarce elementul
        self.driver.find_element(By.XPATH, self.PROFILE_BUTTON).click()  # dau click pe el