"""
This Script can download application for windows
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# ------------ This 4 line codes are for run the program in background without show chrom browser -------------
# chrome_options = Options()  # make an instance from Options() class
# chrome_options.add_argument("--incognito")  # open chrome driver in incognito session
# chrome_options.add_argument("--headless")   # Run the program in background without show Chrome browser
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)


# ------------- This 4 line codes are for run the program with IDM extension to download apps -------------
option = webdriver.ChromeOptions()
option.add_extension(r"G:\webscraping\windows application download\ExtentionsForWebDriverSelenium\IDMGCExt.crx")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=option)


all_handles = driver.window_handles
driver.switch_to.window(all_handles[0])
# driver.maximize_window()
driver.implicitly_wait(1)


lst_apps = ['https://soft98.ir/software/compress/21-winrar-full.html',
            'https://soft98.ir/internet/web-browser/244-google-chrome-desktop.html',
            'https://soft98.ir/internet/download-manager/4-internet-download-manager-4.html',
            'https://soft98.ir/internet/remote-control/15737-anydesk-download.html',
            ]

xpath_list = ['//*[@id="dtill"]/dd[1]/a']


def download_app():
    for item in lst_apps:
        driver.get(item)
        driver.execute_script("window.scrollTo(0, 2000)")
        print("Getting the driver")
        for xpath in xpath_list:
            the_app = driver.find_element('xpath', xpath)
            the_app.click()
            driver.get(item)
            print("The app is downloading....")
    print("Download is Complete")
    driver.quit()


download_app()
