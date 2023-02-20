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


# # Click
# driver.get("https://trytestingthis.netlify.app/")
# driver.find_element("id", "male").click()
#
# # Double Click
# driver.get("https://trytestingthis.netlify.app/")
# el = driver.find_element('xpath', "//button[text()='Double-click me']")
# actions.double_click(el)
# actions.perform()
#
# text = driver.find_element("xpath", "//*[text()='Your Sample Double Click worked!']")
#
# # Right Click
# driver.get("https://trytestingthis.netlify.app/")
# el1 = driver.find_element('id', 'fname')
# actions.context_click(el1).perform()
#
# # Move the Mouse Cursor
# driver.get("https://trytestingthis.netlify.app/")
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
# driver.get("https://demos.telerik.com/kendo-ui/circular-gauge/index")   # Open website
# # driver.find_element('id', 'onetrust-accept-btn-handler').click()    # Accept cookie
# driver.execute_script("scroll(0, 400)")     # Scroll down the page
#
# el3 = driver.find_element('xpath', "//*[contains(@class, 'k-button-increase')]")  # Find element to click and hold
# el4 = driver.find_element('xpath', "//*[contains(@class, 'k-button-decrease')]")
# actions.click_and_hold(el3).pause(2).release().click_and_hold(el4).pause(2).perform()
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

# # Offset of element (Coordinates)
# driver.get("https://trytestingthis.netlify.app/")
# # Get Coordinates
# offset = driver.find_element("xpath", "//*[text()='Lets you select only one option']").location
#
# driver.execute_script("scroll(0, 500)")
# sleep(2)
# # move by offset
# driver.find_element("id", "option").click()
#
# actions.move_by_offset(offset['x'], offset['y']).pause(1).click().perform()
# sleep(2)

# Drag and  Drop by Offset
driver.get("https://selenium08.blogspot.com/2020/01/drag-drop.html")
el5 = driver.find_element('id', 'draggable')
offset = driver.find_element('id', 'droppable').location
print(offset)
actions.drag_and_drop_by_offset(el5, xoffset=200, yoffset=100).pause(1).perform()
sleep(2)
# or
driver.get("https://selenium08.blogspot.com/2020/01/drag-drop.html")
driver.maximize_window()
el1 = driver.find_element('id', 'draggable')
coord_el1 = driver.find_element('id', 'droppable').location
coord_el2 = driver.find_element('id', 'droppable').location
print("Coord5: " + str(coord_el1))
print("Coord6: " + str(coord_el2))
offset_x = coord_el2['x'] - coord_el1['x']
offset_y = coord_el2['y'] - coord_el1['y']
actions.drag_and_drop_by_offset(el5, offset, yoffset=100).pause(1).perform()
sleep(2)

# Element Rect
driver.get("https://selenium08.blogspot.com/2020/01/drag-drop.html")
driver.maximize_window()
el1 = driver.find_element('id', 'draggable')
el2 = driver.find_element('id', 'droppable')
coord_el1 = driver.find_element('id', 'droppable').location
coord_el2 = driver.find_element('id', 'droppable').location
print("Coord5: " + str(coord_el1))
print("Coord6: " + str(coord_el2))
offset_x = (coord_el2['x'] - coord_el1['x']) + (el2.rect['width'] - el1.rect['width'])/2
offset_y = (coord_el2['y'] - coord_el1['y']) + (el2.rect['height'] - el1.rect['height'])/2
actions.drag_and_drop_by_offset(el5, offset, yoffset=100).pause(1).perform()
sleep(2)
