"""
Session 9 - Mouse Actions
    * Click
    * Double Click
    * Right Click
    * Move Cursor
    * Click and Hold
    * Release
    * Drag and Drop 1
    * Drag and Drop 2
    * Offset of element (Coordinates)
    * Move by Offset
    * Drag and  Drop by Offset
    * Element Rect
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver)
driver.get("https://trytestingthis.netlify.app/")
sleep(1)

# Click
driver.find_element("id", "male").click()
sleep(1)

# Double Click
el = driver.find_element('xpath', "//button[text()='Double-click me']")
actions.double_click(el)
actions.perform()

text = driver.find_element("xpath", "//*[text()='Your Sample Double Click worked!']")
sleep(2)

# Richt Click
el1 = driver.find_element('id', 'fname')
actions.context_click(el1).perform()
sleep(2)

# Move the Mouse Cursor
el2 = driver.find_element('xpath', "//*[@class = 'tooltip']")
actions.move_to_element(el2).perform()
sleep(2)

# Click and Hold The Mouse
