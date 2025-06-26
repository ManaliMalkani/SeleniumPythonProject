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

wait = WebDriverWait(driver,25,poll_frequency=1,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])
ele = wait.until(ec.presence_of_element_located((By.ID,"dropdown")))
ele.click()
# import the Select class

# Create the object for Select class
dd_options = Select(ele)

# List the values in Drop Down
dd_v = dd_options.options
for dd_values in dd_v:
    print(dd_values.text)

# Click by Index
dd_options.select_by_index(2)
time.sleep(2)

# Click by Value
dd_options.select_by_value("OptionThree")
time.sleep(2)

# Click by Text
dd_options.select_by_visible_text("Option5")

time.sleep(5)
driver.quit()