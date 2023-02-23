"""
Session 11 - Get attributes of elements
    * 'By' class
    * Get Text
    * Get Class/Link, etc....
    * Check element is selected
    * Check "Radio button" status
    * Check "Switch button" status
    * Check "Checkbox" status
    * Check Enable/Disable
    * Get value of input
    * Check invalid input (field errors)
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# actions = ActionChains(driver=driver)
driver.maximize_window()
driver.implicitly_wait(2)

# 'By' class
# driver.find_element(By.XPATH)
# driver.find_element(By.ID)

# # Get Text
# driver.get("https://material.angular.io/components/categories")
# el = driver.find_element(By.CLASS_NAME, 'mdc-button__label').text
# print(el)


# # Get Class/Link, etc....
# driver.get("https://material.angular.io/components/categories")
# el1 = driver.find_element(By.XPATH, "//*[@class='mdc-button__label' and text()='Components']/..")
# attr = el1.get_attribute('class')
# assert 'selected' in attr, 'Element is not selected'
# print(attr)
# el2 = driver.find_element(By.XPATH, "//*[@class='mdc-button__label' and text()='CDK']/..").click()
# sleep(1)
# attr2 = el1.get_attribute('class')
# print(attr2)
# assert 'selected' not in attr2, 'Element is selected'


# Check "Radio button" status
driver.get("https://material.angular.io/components/radio/overview")
el_Option_2 = driver.find_element(By.XPATH, "//*[@id='mat-radio-3-input']")
assert 'checked' in el_Option_2.get_attribute('id')
el_Option_1 = driver.find_element(By.XPATH, "//*[@id='mat-radio-2-input']")
attr1 = el_Option_1.get_attribute('id')
print(attr1)
assert 'checked' not in attr1
sleep(1)

el_Option_1.click()
attr2 = el_Option_1.get_attribute('id')
print(attr2)
assert 'checked' in attr2
assert 'checked' not in el_Option_2.get_attribute('id')
sleep(3)
