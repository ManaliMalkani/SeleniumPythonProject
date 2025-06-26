"""
1. Absolute XPath:
It uses from complete html root path to the required WebElement.
EX : "/html/body/div/div[2]/div[2]/div/div/div/div[2]/form/input[1]" (or)  "//form//input[1]"


'/'  - finding the element inside the parent element
'//' - finding the child or nested-child element inside the parent element

2. Relative Xpath :
It uses the direct path of a WebElement using (id,className,attribute values , sub-string,etc) to perform action on it.

i) EX : //tag[@attribute='value']
   "//*[@id='user_input']" or "//input[@id='user_input']"

ii) Using Contains ( Need to give partial value) :
    Syntax : "//tag[contains(@attribute,'partial value of attribute')]"
    Ex :     "//input[contains(@id,'user')]"  , "//a[contains(text(),'Form')]"

iii) Starts-With ( Need to give partial value) :
    Syntax: "//tag[starts-with(@attribute,'partial value of attribute')]"
    Ex :    "//input[starts-with(@id,'user')]"



"""

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("/Users/mamalkani/PycharmProjects/SeleniumPythonProject/drivers/chromedriver-mac-arm64/chromedriver")

# Optional: Add options if needed
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run headless if you want

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("http://www.dummypoint.com/seleniumtemplate.html")

driver.find_element(By.XPATH,"//a[contains(text(),'Form')]").click()


time.sleep(2)
driver.quit()
