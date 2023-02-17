from Pages.Login import Login
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.MainPage import MainPage
from time import sleep
import unittest


class LoginTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
        
    def  test_valid_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_on_login_button()
        main_page.check_main_page()
        sleep(2)
    
    def  test_invalid_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)
        login.enter_username("Admin")
        login.enter_password("admin1234")
        login.click_on_login_button()
        main_page.check_main_page()
        sleep(2)
    
    @classmethod    
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
