from Locators import dashbord_label_xpath


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        
    def check_main_page(self):
        self.driver.find_element('xpath', dashbord_label_xpath)
        