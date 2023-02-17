from Login import Login
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(3)

login = Login(driver=driver)

login.enter_username("Admin")
login.enter_password("admin123")
login.click_on_login_button()