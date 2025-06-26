import ec
from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.common.by import By
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
ele = wait.until(ec.presence_of_element_located((By.ID,"user_input")))

#ele = driver.find_element(By.ID,"user_input")

ele_d = ele.is_displayed()
print("Is Displayed : ",ele_d)

ele_e = ele.is_enabled()
print("is enabled : ",ele_e)

ele_s = ele.size
print("Size of ele :" , ele_s)

ele_l = ele.location
print("Ele location : ",ele_l)

ele.click()

ele.send_keys("Code2Lead")
time.sleep(2)

ele.clear()
time.sleep(2)

ele.send_keys("Code2Lead_second time")
time.sleep(2)

ele_t = ele.get_attribute("value")
print("Text from Edit box : ",ele_t)


time.sleep(5)
driver.quit()