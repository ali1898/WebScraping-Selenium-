"""
* Page Object Model
    * Non pom structure
    * pom based structure

https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
"""

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_name = "username"
        self.password_textbox_name = "password"
        self.login_button_type = "submit"
    def enter_username(self, username):
        self.driver.find_element('name', self.username_textbox_name).send_keys(username)
        
    def enter_password(self, password):
        self.driver.find_element('name', self.password_textbox_name).send_keys(password)
        
    def click_on_login_button(self):
        self.driver.find_element('type', self.login_button_type).click()