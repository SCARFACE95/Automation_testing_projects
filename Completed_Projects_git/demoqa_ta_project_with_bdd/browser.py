from selenium import webdriver



class Browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10) #It will wait up to 10 seconds for elements to appear
    driver.set_page_load_timeout(10) #it will wait up to 10 seconds for page to load
    driver.maximize_window()

    def close(self):
        self.driver.quit()
