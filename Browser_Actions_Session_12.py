"""
Session 12 - Conditional Waits
    * Sleep
    * Implicitly
    * Wait until element has an attribute
    * Wait until element has not an attribute
    * Wait until elements is disable/enable
    * Wait until element is visible
    * Wait until element is disappear
    * WebDriverWait until/until not Expected Conditions
    * Wait until page is loaded
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver)
driver.maximize_window()
driver.implicitly_wait(1)


# # Sleep
# print(datetime.now())
# sleep(1)
# print(datetime.now())


# # Implicitly
# driver.get("https://play1.automationcamp.ir/index.html")
# driver.implicitly_wait(3)
# print(datetime.now())
# try:
#     driver.find_element(By.XPATH, "//*[text()='saldf']")
# except:
#     print(datetime.now())


# # Wait until element has an attribute
# def wait_until_element_has_an_attribute(element_selector,
#                                         element_locator,
#                                         attribute,
#                                         attribute_value,
#                                         timeout=5,
#                                         exact=True
#                                         ):
#     for i in range(timeout * 5):
#         try:
#             element = driver.find_element(element_selector, element_locator)
#             if exact:
#                 assert element.get_attribute(attribute) == attribute_value
#             else:
#                 assert attribute_value in element.get_attribute(attribute)
#             print(" Element attribute met: " + str(attribute_value))
#             return
#         except:
#             sleep(0.2)
#     raise Exception("Element attribute is not: " + str(attribute_value)
#
# # Wait until element has not an attribute
# def wait_until_element_has_not_an_attribute(element_selector,
#                                         element_locator,
#                                         attribute,
#                                         attribute_value,
#                                         timeout=5,
#                                         exact=True
#                                         ):
#     for i in range(timeout * 5):
#         try:
#             element = driver.find_element(element_selector, element_locator)
#             if exact:
#                 assert element.get_attribute(attribute) != attribute_value
#             else:
#                 assert attribute_value not in element.get_attribute(attribute)
#             print(" Element attribute not in or not equals: " + str(attribute_value))
#             return
#         except:
#             sleep(0.2)
#     raise Exception("Element attribute in or equals: " + str(attribute_value))
#
#
# driver.get("https://play1.automationcamp.ir/expected_conditions.html")
# trigger = driver.find_element(By.ID, "enabled_trigger")
# trigger.location_once_scrolled_into_view
# wait_until_element_has_an_attribute(By.ID, "enabled_target", 'class', 'danger', exact=False)
# wait_until_element_has_not_an_attribute(By.ID, "enabled_target", 'class', 'success', exact=False)
# trigger.click()
# wait_until_element_has_an_attribute(By.ID, "enabled_target", 'class', 'success', exact=False)
# wait_until_element_has_not_an_attribute(By.ID, "enabled_target", 'class', 'danger', exact=False)
# print("Test case PASSED")


# # Wait until elements is disable/enable
# def wait_until_elements_is_enable(element_selector,
#                                  element_locator,
#                                  timeout
#                                   ):
#     for i in range(timeout * 2):
#         try:
#             element = driver.find_element(element_selector, element_locator)
#             assert element.is_enabled()
#             return
#         except:
#             sleep(0.5)
#
# # Wait until elements is disable
# def wait_until_elements_is_disable(element_selector,
#                                    element_locator,
#                                    timeout
#                                    ):
#     for i in range(timeout * 2):
#         try:
#             element = driver.find_element(element_selector, element_locator)
#             assert not element.is_enabled()
#             return
#         except:
#             sleep(0.5)
#
# driver.get("https://play1.automationcamp.ir/expected_conditions.html")
# trigger = driver.find_element(By.ID, "enabled_trigger")
# trigger.location_once_scrolled_into_view
# wait_until_elements_is_disable(By.ID, "enabled_target", 5)
# print("Element is Desable now!")
# trigger.click()
# wait_until_elements_is_enable(By.ID, "enabled_target", 5)
# print("Element is enabled now!")


# # Wait until element is visible
# def wait_until_elements_is_visible(element_selector,
#                                    element_locator,
#                                    timeout=5
#                                    ):
#     for i in range(timeout * 2):
#         try:
#             element = driver.find_element(element_selector, element_locator)
#             assert element.is_displayed()
#             print("Test is PASSED")
#             return
#         except:
#             sleep(0.5)
#
# # Wait until element is invisible
# def wait_until_elements_is_invisible(element_selector,
#                                      element_locator,
#                                      timeout=2
#                                      ):
#     for i in range(timeout * 2):
#         try:
#             element = driver.find_element(element_selector, element_locator)
#             assert not element.is_displayed()
#             print("Test is PASSED")
#             return
#         except:
#             sleep(0.5)
#
# driver.get("https://play1.automationcamp.ir/expected_conditions.html")
# trigger = driver.find_element(By.ID, "visibility_trigger")
# trigger.location_once_scrolled_into_view
# print(driver.find_element(By.ID, "visibility_target").is_displayed())
# wait_until_elements_is_invisible(By.ID, "visibility_target", 5)
# print("Element is invisible before click!")
# trigger.click()
# wait_until_elements_is_visible(By.ID, "visibility_target", 6)
# print(driver.find_element(By.ID, "visibility_target").is_displayed())
# print("Element is visible after click!")


# WebDriverWait until/until not Expected Conditions
# driver.get("https://play1.automationcamp.ir/expected_conditions.html")
# trigger = driver.find_element(By.ID, "enabled_trigger")
# trigger.location_once_scrolled_into_view
# trigger.click()
# wait = WebDriverWait(driver, 3)
# element = wait.until(EC.element_to_be_clickable((By.ID, "enabled_trigger")))
# print(element)


# Wait until page is loaded
def wait_until_page_is_loaded(timeout = 10):
    for i in range(timeout * 2):
        try:
            state = driver.execute_script("return document.readyState")
            assert state == 'complete'
            print("State is: ", str(state))
            return
        except:
            sleep(0.5)

driver.get("https://archive.org/details/biodiversity")
wait_until_page_is_loaded()
