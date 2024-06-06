import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from browser import Browser


class BasePage(Browser):

    #time for 5 seconds is searching for the presence of an element with type XPATH, if is found you can go further
    def wait_for_elem(self, xpath_selector):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, xpath_selector)))

    #This method is used when you want to go back to previous page
    def browser_back(self):
        self.driver.back()

