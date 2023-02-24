"""
Session 12 - Conditional Waits
    * Sleep
    * Implicitly
    * Wait until element has an attribute
    * Wait until element has not an attribute
    * Wait until elements is disable/enable
    * Wait until element is visible
    * Wait until element is disappear
    * WebDriverWait until Expected Conditions
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


# Wait until element has an attribute
driver.get("https://play1.automationcamp.ir/expected_conditions.html")

def wait_until_element_has_an_attribute(element_selector,
                                        element_locator,
                                        attribute,
                                        attribute_value,
                                        timeout=5,
                                        exact=True
                                        ):
    for i in range(timeout * 5):
        try:
            element = driver.find_element(element_selector, element_locator)
            if exact:
                assert element.get_attribute(attribute) == attribute_value
            else:
                assert attribute_value in element.get_attribute(attribute)
            return
        except:
            sleep(0.2)
    raise Exception("Element attribute is not: " + str(attribute))


trigger = driver.find_element(By.ID, "enabled_trigger")
trigger.location_once_scrolled_into_view
trigger.click()
wait_until_element_has_an_attribute(By.ID, "enabled_target", 'class', 'success', exact=False)
