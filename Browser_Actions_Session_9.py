"""
Session 9 - Mouse Actions
    * Click
    * Double Click
    * Right Click
    * Move Cursor
    * Click and Hold    https://demos.telerik.com/kendo-ui/circular-gauge/index
    * Pause and Release
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
driver.implicitly_wait(3)
actions = ActionChains(driver)
# driver.get("https://trytestingthis.netlify.app/")

# # Click
# driver.find_element("id", "male").click()
#
# # Double Click
# el = driver.find_element('xpath', "//button[text()='Double-click me']")
# actions.double_click(el)
# actions.perform()
#
# text = driver.find_element("xpath", "//*[text()='Your Sample Double Click worked!']")
#
# # Right Click
# el1 = driver.find_element('id', 'fname')
# actions.context_click(el1).perform()
#
# # Move the Mouse Cursor
# el2 = driver.find_element('xpath', "//*[@class = 'tooltip']")
# actions.move_to_element(el2).perform()

# # Click and Hold The Mouse  https://demos.telerik.com/kendo-ui/circular-gauge/index
# driver.get("https://demos.telerik.com/kendo-ui/circular-gauge/index")   # Open website
# driver.find_element('id', 'onetrust-accept-btn-handler').click()    # Accept cookie
# driver.execute_script("scroll(0, 400)")
#
# el3 = driver.find_element('xpath', "//*[contains(@class, 'k-button-increase')]")  # Find element to click and hold
# actions.click_and_hold(el3).perform()   # click and hold
# sleep(3)

# Pause and Release

driver.get("https://demos.telerik.com/kendo-ui/circular-gauge/index")   # Open website
# driver.find_element('id', 'onetrust-accept-btn-handler').click()    # Accept cookie
driver.execute_script("scroll(0, 400)")     # Scrool down the page

el3 = driver.find_element('xpath', "//*[contains(@class, 'k-button-increase')]")  # Find element to click and hold
el4 = driver.find_element('xpath', "//*[contains(@class, 'k-button-decrease')]")
actions.click_and_hold(el3).pause(3).release().click_and_hold(el4).pause(4).perform()   # click and hold and pause for 3 second and release
sleep(5)
