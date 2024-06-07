from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://demo.nopcommerce.com/login")

actual=driver.find_element(By.XPATH, '//title[text()="nopCommerce demo store. Login"]').text

expected = 'nopCommerce demo store. Login'
assert actual==expected, 'Error'

