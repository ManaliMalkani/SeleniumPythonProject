"""
Below are some of the ways to find WebElement using CssSelector

1. To write id name in css selector you need to add "#" before id value

2. To write class name in css selector you need to add "." before class name

3. Using " Tag name("input") and name " Attribute value as css_selector

4. Using " Tag name("input"),className and name " Attribute value as css_selector

5. “^” - Find elements using starts with a string value

6. “$” - Find elements using Ends with a string value

7. “*” - Find elements using contains a substring.

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

time.sleep(2)

# 1. Using ID name in CSS Selector (To write id name in css selector you need to add "#" before id value)
#driver.find_element(By.CSS_SELECTOR,"#user_input").send_keys("Code2Lead_Id")

# 2. Using Class Name in CSS Selector (To write class name in css selector you need to add "." before class name)
#driver.find_element(By.CSS_SELECTOR,".entertext").send_keys("Code2Lead_ClassName")

# 3. Using " Tag name("input") and name " Attribute value as css_selector
#driver.find_element(By.CSS_SELECTOR,"input[name=textbox]").send_keys("Code2Lead_TN")

# 4. Using " Tag name("input"),className and name " Attribute value as css_selector
#driver.find_element(By.CSS_SELECTOR,"input.entertext[name=textbox]").send_keys("Code2Lead_TCN")

# 5. “^” - Find elements using starts with a string value
#driver.find_element(By.CSS_SELECTOR,"input[class^='en']").send_keys("Code2Lead_SLUC")

# 6. “$” - Find elements using Ends with a string value
#driver.find_element(By.CSS_SELECTOR,"input[class$='xt']").send_keys("Code2Lead_ELUC")

# 7. “*” - Find elements using contains a substring.
driver.find_element(By.CSS_SELECTOR,"input[class*='ter']").send_keys("Code2Lead_SULUC")

time.sleep(2)
driver.quit()