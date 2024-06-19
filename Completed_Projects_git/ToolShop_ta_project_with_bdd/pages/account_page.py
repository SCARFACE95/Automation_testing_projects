from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccountPage(BasePage):
    #Selectors
    MY_ACCOUNT_LABEL = (By.XPATH, '//h1[text()="My account"]')

    #Actions
    def verify_my_account_lable_is_displayed(self):
        self.wait_for_elem(self.MY_ACCOUNT_LABEL, 10)
        assert self.find(self.MY_ACCOUNT_LABEL).is_displayed(), "Error, Label is not displayed"


    #Validations
