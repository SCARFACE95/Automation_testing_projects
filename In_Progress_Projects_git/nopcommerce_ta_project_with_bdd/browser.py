#Aici cream driver-ul cu toata logica lui
from selenium import webdriver


class Browser:

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3) # mereu o sa astepte 3 secunde ca sa nu cada testul


    def close(self):
        self.driver.close()