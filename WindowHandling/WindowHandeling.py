from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/sujithreddy/Documents/Others/Drivers/chromedriver")  # Using Chrome Driver

driver.get("http://www.dummypoint.com/Windows.html")
assert "Selenium Template" in driver.title

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

# To get the current window name
window_name = driver.current_window_handle
print("Before switching ",window_name)

time.sleep(2)
# click on popup button to open new window
ele = driver.find_elements(By.TAG_NAME,"input")

for popup_bs in ele:
    popup_b = popup_bs.get_attribute("value")
    if popup_b == "Open a Popup Window2":
        popup_bs.click()

time.sleep(2)
# Print the list of windows are present on the screen in present session

windows = driver.window_handles
for window in windows:
    print(window)

# switch to required window
driver.switch_to.window(windows[1])

time.sleep(2)
window_name = driver.current_window_handle
print("After switching ",window_name)

driver.maximize_window()

""" 
Here switching to new window and performing action on frame
"""

time.sleep(2)
ele = driver.find_element(By.ID,"f2")
driver.switch_to.frame(ele)

data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",data.text)

time.sleep(2)
driver.close()


time.sleep(5)
driver.quit()
