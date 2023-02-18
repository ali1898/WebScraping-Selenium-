"""
Session 9 - Mouse Actions
    * Click
    * Double Click
    * Right Click
    * Move Cursor
    * Click and Hold
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

# # Click and Hold The Mouse
# driver.get("https://demos.telerik.com/kendo-ui/circular-gauge/index")   # Open website
# driver.find_element('id', 'onetrust-accept-btn-handler').click()    # Accept cookie
# driver.execute_script("scroll(0, 400)")
#
# el3 = driver.find_element('xpath', "//*[contains(@class, 'k-button-increase')]")  # Find element to click and hold
# actions.click_and_hold(el3).perform()   # click and hold
# sleep(3)

# # Pause and Release
#
# driver.get("https://demos.telerik.com/kendo-ui/circular-gauge/index")   # Open website
# # driver.find_element('id', 'onetrust-accept-btn-handler').click()    # Accept cookie
# driver.execute_script("scroll(0, 400)")     # Scrool down the page
#
# el3 = driver.find_element('xpath', "//*[contains(@class, 'k-button-increase')]")  # Find element to click and hold
# el4 = driver.find_element('xpath', "//*[contains(@class, 'k-button-decrease')]")
# actions.click_and_hold(el3).pause(2).release().click_and_hold(el4).pause(2).perform()   # click and hold and pause for 3 second and release
# sleep(5)

# # Drag and Drop (1)
# driver.get("https://selenium08.blogspot.com/2020/01/drag-drop.html")
# el5 = driver.find_element('id', 'draggable')
# el6 = driver.find_element('id', 'droppable')
# actions.move_to_element(el5).click_and_hold().move_to_element(el6).release().perform()
# sleep(2)

# # Drag and Drop (2)
# driver.get("https://selenium08.blogspot.com/2020/01/drag-drop.html")
# el5 = driver.find_element('id', 'draggable')
# el6 = driver.find_element('id', 'droppable')
# actions.drag_and_drop(el5, el6)
# sleep(2)

# Offset of element (Coordinates)
driver.get("https://trytestingthis.netlify.app/")
# Get Coordinates
offset = driver.find_element("xpath", "//*[text()='Lets you select only one option']").location

driver.execute_script("scroll(0, 500)")
sleep(2)
# move by offset
driver.find_element("id", "option").click()

actions.move_by_offset(offset['x'], offset['y']).pause(1).click().perform()
sleep(5)