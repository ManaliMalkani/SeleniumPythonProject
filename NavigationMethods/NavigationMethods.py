from selenium import webdriver
from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# Specify the path to chromedriver explicitly
service = Service("/Users/mamalkani/PycharmProjects/SeleniumPythonProject/drivers/chromedriver-mac-arm64/chromedriver")

# Optional: Add options if needed
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run headless if you want

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
time.sleep(2)

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
ele = wait.until(ec.presence_of_element_located((By.ID, "multiselect")))


# import the Select class

# Create the object for Select class
ms_options = Select(ele)

print("Check whether it is a multi select or not : ", ms_options.is_multiple)

# List the values in Multi Select
ms_v = ms_options.options
for ms_value in ms_v:
    print(ms_value.text)

# Click by Index
ms_options.select_by_index(1)
# Click by Value
ms_options.select_by_value("mOptionTWo")
# Click by Text
ms_options.select_by_visible_text("mOption3")

time.sleep(2)


# deselect_by_index
ms_options.deselect_by_index(1)
time.sleep(2)

# deselect_by_value
ms_options.deselect_by_value("mOptionTWo")
time.sleep(2)

# deselect_by_visible_text
ms_options.deselect_by_visible_text("mOption3")
time.sleep(2)


# Click by Index
ms_options.select_by_index(1)
# Click by Value
ms_options.select_by_value("mOptionTWo")
# Click by Text
ms_options.select_by_visible_text("mOption3")

time.sleep(2)

# deselect_all
ms_options.deselect_all()


time.sleep(5)
driver.quit()
