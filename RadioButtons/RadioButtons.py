from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

# Specify the path to chromedriver explicitly
service = Service("/Users/mamalkani/PycharmProjects/SeleniumPythonProject/drivers/chromedriver-mac-arm64/chromedriver")

# Optional: Add options if needed
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run headless if you want

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("http://www.dummypoint.com/seleniumtemplate.html")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
time.sleep(2)

# 1. find the list of radio buttons using locator
ele_r = driver.find_elements(By.NAME,"radio")
time.sleep(2)

# 2. Using for loop iterate the list object and click on required option
for rbutton in ele_r:
    rbutton_t = rbutton.get_attribute("value")
    print(rbutton_t)
    if rbutton_t == "Button2":
        rbutton.click()
        print("Is Selected : ",rbutton.is_selected())
        break



time.sleep(2)
driver.quit()