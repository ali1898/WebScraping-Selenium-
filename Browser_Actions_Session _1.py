from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# driver = webdriver.Chrome(executable_path=)
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# Browser Action 1 > open web
driver.get("https://google.com")

# # Browser Action 2 > Title
# window_title = driver.title
# print(window_title)
#
# # Browser Action 2 > open wikipedia
# driver.get("https://wikipedia.com")
# sleep(1)
#
# # Browser Action 2 > back
# driver.back()
# sleep(1)
#
# # Browser Action 2 > forward
# driver.forward()
# sleep(1)
#
# # Browser Action 2 > Refresh
# driver.refresh()
# sleep(1)
#
# # Browser Action 2 > open new window and switch to it (tab)
# driver.switch_to.new_window('tab')
# sleep(1)
#
# # Browser Action 2 > open new window and switch to it (window)
# driver.switch_to.new_window('window')
# driver.get('https://yahoo.com')
# sleep(3)
#
# # Browser Action 2 > Current window
# yahoo_window = driver.current_window_handle
# print('yahoo_handle' + str(yahoo_window))
#
# # Browser Action 2 > All handles
# all_handles = driver.window_handles
# print('all_handles' + str(all_handles))
#
# # Browser Action 2 > switch
# driver.switch_to.window(all_handles[1])
# sleep(2)
#
# # Browser Action 2 > Close tab
# driver.close()
# sleep(2)

# Browser Action 2 > Window Size
windows_size = driver.get_window_size()
print(f'window_size is ---> {windows_size}')
width = windows_size['width']
print(f'width ---> {width}')
height = windows_size['height']
print(f'height ---> {height}')
sleep(2)

# Browser Action 2 > Set Window Size
driver.set_window_size(800, 600)
sleep(1)
size = driver.get_window_size()
print(f'size ---> {size}')
sleep(1)
assert size['width'] == 802  # checked if the size is 1050 or not
sleep(1)

# Browser Action 2 > Change window position
current_position = driver.get_window_position()
print(f'current_position ---> {current_position}')

# Browser Action 2 > Set window position
new_position = driver.set_window_position(200, 20)
print(f'new_position ---> {new_position}')
sleep(1)
assert driver.get_window_position()['y'] == 20

# Browser Action 2 > Maximize window
driver.maximize_window()
sleep(2)

# Browser Action 2 > Full screen window
driver.fullscreen_window()
sleep(2)

# Browser Action 2 > Minimize window
driver.minimize_window()
sleep(2)

# Browser Action 2 > Close chrome
driver.quit()
