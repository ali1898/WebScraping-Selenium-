"""
Session 13 - Tricks for
    * Alert
    * Dialog (Popup)
    * snack-bar (Toast)
    * Tooltip
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(2)
alert = Alert(driver)

# Alert
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

# Get text alert
print(alert.text)
sleep(2)

# Accept alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
alert.accept()
text = driver.find_element(By.XPATH, "//*[text()='You clicked: Ok']")
assert text == 'You clicked: Ok'
# Up assertion or below assertion
dom = driver.page_source  # dom of a page is an instruction of a page
assert 'You clicked: Ok' in dom  # This text in in dom

# Dismiss
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
alert.dismiss()
dom = driver.page_source  # dom of a page is an instruction of a page
assert 'You clicked: Cancel' in dom  # This text in in dom
