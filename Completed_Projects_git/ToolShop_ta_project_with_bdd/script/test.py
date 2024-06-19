from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10) #It will wait up to 10 seconds for elements to appear
driver.set_page_load_timeout(10) #it will wait up to 10 seconds for page to load
driver.maximize_window()

driver.get("https://practicesoftwaretesting.com/#")

# driver.find_element(By.XPATH, '//*[@routerlink="/auth/login"]').click()
# sleep(3)


 #Locate the slider element
list_elem = driver.find_elements(By.XPATH, '//div[@class="input-group mb-3"]')

elem = list_elem[1]
#print(elem.text)


# Create ActionChains object
actions = ActionChains(driver)

sleep(3)
# Move the slider (adjust xoffset as needed)
actions.click_and_hold(elem).move_by_offset(-20, 0).release().perform()
sleep(5)


#print(elem.text)

SLIDER_VALUE = '//span[contains(@class, "ngx-slider-span") and @aria-valuetext="85"]'



#############


