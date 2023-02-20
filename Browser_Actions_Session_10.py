"""
Session 10 - Scroll
    * Scroll using JavaScript Commands
        * Scroll down by pixel
        * Scroll to specific position
        * Scroll to element if it could find by driver
        * Scroll to element if currently cannot be found or not sure if it is in the page
        * Scroll to down of the page
        * Scroll to top of the page
        * Scroll horizontally
    * Is displayed
    * Scroll using ActionChains library
    * Scroll using Keyboard (KEYS)
    * Scroll to find element
    * Scroll using WebDriver itself
    * Scroll horizontally
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver=driver)
driver.maximize_window()
driver.implicitly_wait(2)

# # Scroll down by pixel
# driver.get("https://trytestingthis.netlify.app/")
# driver.execute_script("window.scrollBy(0, 200)")  # For run JavaScript commands
# sleep(1)
#
#
# # Scroll to specific position
# driver.get("https://trytestingthis.netlify.app/")
# driver.execute_script("window.scrollTo(0, 1000)")
# sleep(1)
#
#
# #  Scroll to element if it could find by driver
# driver.get("https://www.imdb.com/chart/top")
# element = driver.find_element('link text', 'The Help')
# print(element)
# driver.execute_script("arguments[0].scrollIntoView();", element)
# sleep(2)


# #  Scroll to element if currently cannot be found or not sure if it is in the page (True-False)
# def scroll_to_find_element(locator, pixel):
#     for i in range(10):
#         try:
#             driver.find_element(locator[0], locator[1])
#             return True
#         except:
#             driver.execute_script(f"window.scrollBy(0, {str(pixel)})")
#             sleep(0.5)
#     return False
#
#
# driver.get("https://www.imdb.com/chart/top")
# result = scroll_to_find_element(['link text', 'Dersu Uzala'], 1800)
# print(result)


# #  Scroll to element if currently cannot be found or not sure if it is in the page (Assertion)
# def scroll_to_find_element(locator, pixel):
#     for i in range(10):
#         try:
#             driver.find_element(locator[0], locator[1])
#             print(f"The element '{locator}' has been found")
#         except:
#             driver.execute_script(f"window.scrollBy(0, {str(pixel)})")
#             sleep(0.5)
#     raise Exception(f"The element '{locator}' cannot be found")
#
#
# driver.get("https://www.imdb.com/chart/top")
# scroll_to_find_element(['link text', 'Dersu Uzala'], 1800)


# # Scroll to down of the page
# driver.get("https://www.imdb.com/chart/top")
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# # or
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# sleep(2)
#
# # Scroll to top of the page
# driver.execute_script("window.scrollTo(0, 0)")
# sleep(2)


# # Scroll horizontally
# driver.get("https://datatables.net/examples/styling/display.html")
# driver.set_window_size(480, 640)
# #  document.getElementById('quantity').scrollIntoView() , document.querySelector('#quantity').scrollIntoView() ,
# driver.execute_script("document.querySelector('table td:last-child').scrollIntoView()")
# sleep(4)


# # Is displayed
# driver.get("https://www.imdb.com/chart/top")
# element = driver.find_element('link text', 'Hotel bozorg-e budapest').is_displayed()
# print(element)
# result = element.is_displayed()
# print(result)


# # Scroll using ActionChains library
# driver.get("https://trytestingthis.netlify.app/")
# el1 = driver.find_element('xpath', "//*[@name='message']")
# el2 = driver.find_element('id', 'fname')
# actions.move_to_element(el2).click_and_hold().move_to_element(el1).release().perform()
# sleep(5)


# # Scroll using Keyboard (KEYS)
# driver.get("https://trytestingthis.netlify.app/")
# page_el = driver.find_element('tag name', 'html')
# actions.send_keys_to_element(page_el, Keys.END).perform()  # Page Down
# sleep(2)
# actions.send_keys_to_element(page_el, Keys.HOME).perform()  # Page Up
# sleep(2)


# #  Scroll to find element
# def scroll_to_find_element(locator):
#     page_el = driver.find_element('tag name', 'html')
#     for i in range(10):
#         try:
#             driver.find_element(locator[0], locator[1])
#             return True
#         except:
#             actions.send_keys_to_element(page_el, Keys.PAGE_DOWN).perform()
#             sleep(0.5)
#     return False
# driver.get("https://www.imdb.com/chart/top")
# result = scroll_to_find_element(['link text', 'dslfajdf'])


# # Scroll using WebDriver itself
# driver.get("https://www.imdb.com/chart/top")
# element = driver.find_element('link text', 'The Handmaiden')
# element.location_once_scrolled_into_view
# sleep(3)


# Scroll horizontally
driver.get("https://datatables.net/examples/styling/display.html")
driver.set_window_size(480, 640)
element = driver.find_element('xpath', '//tbody//td[last()]')
sleep(2)
element.location_once_scrolled_into_view
sleep(3)
