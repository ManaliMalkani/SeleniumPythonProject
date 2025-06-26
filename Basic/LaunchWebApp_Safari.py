from selenium import webdriver
import time

# Safari does not require a driver path on macOS
driver = webdriver.Safari()

driver.get("http://www.dummypoint.com/seleniumtemplate.html")

time.sleep(5)

driver.quit()