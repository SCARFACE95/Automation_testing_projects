import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestKeyLibraryPractice(unittest.TestCase):


    #SELECTORS:
    INPUT_ID = (By.ID, "username")

    def test_keys(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/login")

        input_username = self.driver.find_element(*self.INPUT_ID)

        #Write something on input
        input_username.send_keys("tomsmith")
        time.sleep(1)

        #Using keys library (CTRL+A to all text than Delete)
        input_username.send_keys(Keys.COMMAND + "A")
        time.sleep(1)
        input_username.send_keys(Keys.DELETE)
        time.sleep(1)

        #Write again text
        input_username.send_keys("tomsmith1234567")
        input_username.send_keys(Keys.ARROW_LEFT * 7)
        time.sleep(1)

        #I go back with arrow right
        input_username.send_keys(Keys.ARROW_RIGHT * 7)
        time.sleep(1)


        self.driver.quit()


