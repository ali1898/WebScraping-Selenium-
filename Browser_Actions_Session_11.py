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
# driver.maximize_window()
driver.implicitly_wait(2)

# 'By' class
# driver.find_element(By.XPATH)
# driver.find_element(By.ID)

# # Get Text
# driver.get("https://material.angular.io/components/categories")
# text = driver.find_element(By.CLASS_NAME, 'mdc-button__label').text
# print(text)


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


# # Check "Radio button" status
# driver.get("https://material.angular.io/components/checkbox/examples")
# Before = driver.find_element(By.ID, 'mat-radio-3')
# attrB = Before.get_attribute('class')
# print(attrB)
# assert 'checked' not in Before.get_attribute('class')
# Before.click()
# attrB = Before.get_attribute('class')
# print(attrB)
# assert 'checked' in Before.get_attribute('class')
# sleep(2)
#
# After = driver.find_element(By.ID, 'mat-radio-2')
# attrA = After.get_attribute('class')
# print(attrA)
# assert 'checked' not in After.get_attribute('class')
# After.click()
# attr2 = After.get_attribute('class')
# print(attr2)
# assert 'checked' in After.get_attribute('class')
# sleep(2)


# # Check "Switch button" status
# driver.get("https://material.angular.io/components/slide-toggle/overview")
# toggle = driver.find_element(By.ID, 'mat-mdc-slide-toggle-1-button')
# assert 'checked' not in toggle.get_attribute('class')
# toggle.click()
# assert 'checked' in toggle.get_attribute('class')
# sleep(3)


# # Check "Checkbox" status
# driver.get("https://material.angular.io/components/checkbox/overview")
# checkbox = driver.find_element(By.ID, 'mat-mdc-checkbox-1-input')
# assert 'selected' not in checkbox.get_attribute('class')
# sleep(3)
# checkbox.click()
# assert 'selected' in checkbox.get_attribute('class')
# sleep(3)


# # Check Enable/Disable
# driver.get("https://material.angular.io/components/checkbox/examples")
# E_D = driver.find_element(By.ID, 'mat-mdc-checkbox-3')
# assert 'checked' not in E_D.get_attribute('class')
# attr1 = E_D.get_attribute('class')
# print(f'"{attr1}" Before Checked the check box!')
# E_D.click()
# sleep(5)
# assert 'checked' in E_D.get_attribute('class')
# attr2 = E_D.get_attribute('class')
# print(f'"{attr2}" After Checked the check box!')

# # Get value of input
# driver.get("https://material.angular.io/components/input/overview")
# el = driver.find_element(By.ID, 'mat-input-2')
# el.send_keys('This is session 11')
# sleep(2)
# input_value = el.get_attribute('value')
# print(input_value)
# assert input_value == "This is session 11"
# sleep(2)


# Check invalid input (field errors)
driver.get("https://material.angular.io/components/input/overview")
parent_el = driver.find_element(By.XPATH, "//*[@id='mat-input-2']")
assert 'dirty' not in parent_el.get_attribute('class')
input_el = driver.find_element(By.ID, 'mat-input-2')
input_el.send_keys("daljfjsdjf")
assert 'dirty' in parent_el.get_attribute('class')
sleep(2)
