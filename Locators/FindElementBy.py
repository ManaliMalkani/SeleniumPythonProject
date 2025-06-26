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

time.sleep(2)

driver.find_element(By.ID,"user_input").send_keys("Code2Lead")
#driver.find_element(By.CLASS_NAME,"entertext").send_keys("Code2Lead_ClassName")
#driver.find_element(By.NAME,"textbox").send_keys("Code2Lead_Name")
#driver.find_element(By.TAG_NAME,"input").send_keys("Code2Lead_TagName")
#driver.find_element(By.LINK_TEXT,"FORM").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"FOR").click()

time.sleep(5)
driver.quit()