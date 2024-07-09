import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWaitForElemVisibilityPractice(unittest.TestCase):

    #SELECTORS:

    BUTTON_START = (By.XPATH, "//button[text()='Start']")
    DIV_FINISH = (By.ID, "finish")


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    def tearDown(self) -> None:
        self.driver.quit()

    def find(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    def wait_for_element_visibility(self, locator, seconds):
        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.visibility_of_element_located(locator))
    def test_verify_element_is_not_displayed(self):
        self.find(self.BUTTON_START).click()
        assert self.find(self.DIV_FINISH).is_displayed() == False


    def test_verify_element_is_displayed(self):
        #Click on the button
        self.find(self.BUTTON_START).click()

        #Introducing wait to wait until visibility of DIV_FINISH
        self.wait_for_element_visibility(self.DIV_FINISH,15)

        #Check if the element is displayed
        assert self.find(self.DIV_FINISH).is_displayed()


