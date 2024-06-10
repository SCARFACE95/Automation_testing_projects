from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://demo.nopcommerce.com/register")
driver.find_element(By.ID, "register-button").click()
sleep(5)
driver.find_element(By.ID, "LastName-error")


driver.close()