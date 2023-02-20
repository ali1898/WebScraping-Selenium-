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

# Get Text
driver.get("https://material.angular.io/components/categories")
el = driver.find_element(By.CLASS_NAME, 'mdc-button__label')
attr = el.text
print(attr)

