from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://wikipedia.com")

# 1 ---> ID
el1 = driver.find_element('id', 'searchInput')
sleep(2)

# 2 ---> Xpath
el2 = driver.find_element('xpath', '//*[(@id = "searchInput")]')
sleep(2)
assert el1 == el2

el3 = driver.find_element('xpath', "//*[text()='Italiano']")
el3.click()
sleep(2)
driver.back()

# 3 ---> tag
el4 = driver.find_element('tag name', 'select')
el4.click()
sleep(2)

# 4 ---> link text
driver.find_element('link text', 'Creative Commons Attribution-ShareAlike License').click()
sleep(2)
driver.back()

# 5 ---> partial link text
driver.find_element('partial link text', 'Download').click()
sleep(2)

# 6 ---> class name
driver.find_element('class name', 'svg-search-icon').click()
sleep(2)

driver.back()
driver.find_element('css selector', '#searchInput').clear()

# 7 ---> css selector
driver.find_element('css selector', '#searchInput').send_keys('searchInput') # for css selector use {(#)[searchInput]} at the first value for id
sleep(2)
driver.find_element('css selector', '.svg-search-icon').click() # for css selector use {(.)[svg-search-icon]} at the first value for class
sleep(2)