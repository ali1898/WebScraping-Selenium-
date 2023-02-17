from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
import os                   # join name of file that make with path library
from pathlib import Path    # Make the path of a file

chrome_options = Options()  # make an instance from Options() class
chrome_options.add_argument("--incognito")  # open chrome driver in incognito session
chrome_options.add_argument("--headless")   # Run the program in background without show Chrome browser

# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)   # with chrome options

driver.get('https://yahoo.com')
sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # This command is a javaScript command
current_path = Path(__file__)     # The address of this project("D:\Github\WebScraping-Selenium-\screenshot.png")
FileName = os.path.join(str(current_path) + "screenshot.png")
driver.save_screenshot(FileName)
print(f'The screenshot saved in {FileName}')    # show the path of file


driver.quit()
