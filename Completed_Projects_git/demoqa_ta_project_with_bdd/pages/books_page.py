from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage



class BooksPage(BasePage):
    # XPATH selectors:
    LOGIN_BUTTON = '//button[@id="login"]'
    NUMBER_OF_BOOKS = '//div[@class="action-buttons"]'
    SEARCH_INPUT = '//*[@id="searchBox"]'
    BOOK_TITLE = '//div[@class="action-buttons"]//a'

    # actions
    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)  # Wait for 5 seconds until the button appears
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()


    def fill_search_input(self,query):
        self.wait_for_elem(self.SEARCH_INPUT)
        search = self.driver.find_element(By.XPATH, self.SEARCH_INPUT)
        search.clear() #First I clear the search box to make sure is empty
        search.send_keys(query) #I enter on search box "query"


    def clear_search_input(self):
        self.wait_for_elem(self.SEARCH_INPUT)
        search = self.driver.find_element(By.XPATH, self.SEARCH_INPUT)
        #we can use also data from keyboard to clear the search box
        search.send_keys(Keys.COMMAND, 'a') #CTRL + A
        search.send_keys(Keys.BACKSPACE) # BACK



    #validations
    def validate_correct_url(self):
        sleep(2)
        expected = "https://demoqa.com/books"
        actual = self.driver.current_url
        self.assertEqual(expected, actual, "URL is incorrect")


    def validate_books_count(self, expected_number):
        sleep(1)
        actual_number = len(self.driver.find_elements(By.XPATH, self.NUMBER_OF_BOOKS))
        self.assertEqual(expected_number, actual_number, "Number of books incorrect")


    def validate_books_title(self, expected_title):
        self.wait_for_elem(self.BOOK_TITLE)
        actual_title = self.driver.find_element(By.XPATH, self.BOOK_TITLE).text
        self.assertEqual(expected_title, actual_title, "Book title is incorrect")





