import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class TestJsAlertsPractice(unittest.TestCase):

    BUTTON_JS_ALERT = (By.XPATH, "//button[@onclick='jsAlert()']")
    BUTTON_JS_CONFIRM = (By.XPATH, "//button[@onclick='jsConfirm()']")
    BUTTON_JS_PROMPT = (By.XPATH, "//button[@onclick='jsPrompt()']")
    TEXT_RESULT = (By.ID, "result")


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    def tearDown(self) -> None:
        self.driver.quit()

    def find(self, locator) -> WebElement:
        return self.driver.find_element(*locator)


    def test_accept_simple_alert(self):
        #Click on visible button for JS alert
        self.find(self.BUTTON_JS_ALERT).click()

        #switch to alert is searching if exist any alert, otherwise is send an error
        alert = self.driver.switch_to.alert
        time.sleep(1)

        #accept the alert
        alert.accept()

        #After accept the alert shall print expected_text
        expected_text = "You successfully clicked an alert"
        actual_text = self.find(self.TEXT_RESULT).text

        #Check expected text with actual text
        assert expected_text == actual_text, 'Unexpected text'


    def test_dismiss_alert(self):
        self.find(self.BUTTON_JS_CONFIRM).click()

        # switch to alert is searching if exist any alert, otherwise is send an error
        alert = self.driver.switch_to.alert
        time.sleep(1)

        #Dismiss the alert
        alert.dismiss()

        # After dismiss the alert shall print expected_text
        expected_text = "You clicked: Cancel"
        actual_text = self.find(self.TEXT_RESULT).text

        # Check expected text with actual text
        assert expected_text == actual_text, 'Unexpected text'


    def test_js_alert_with_prompt(self):
        self.find(self.BUTTON_JS_PROMPT).click()
        time.sleep(1)

        # switch to alert is searching if exist any alert, otherwise is send an error
        alert = self.driver.switch_to.alert
        time.sleep(1)

        #Write something on prompt alert
        text_alert = "Andrei@gmail.com"
        alert.send_keys(text_alert)
        time.sleep(2)

        #Accept the alert
        alert.accept()

        # After dismiss the alert shall print expected_text
        expected_text = "You entered: " + text_alert
        actual_text = self.find(self.TEXT_RESULT).text


        # Check expected text with actual text
        self.assertEqual(expected_text, actual_text, msg="Unexpected error")







