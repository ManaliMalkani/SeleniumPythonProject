from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Optional: set path to geckodriver if it's not in your system PATH
service = Service("/Users/mamalkani/PycharmProjects/SeleniumPythonProject/drivers/geckodriver/geckodriver")  # Replace with your actual path if different

# Optional: Firefox options
options = Options()
# options.headless = True  # Uncomment to run headless

# Launch Firefox browser
driver = webdriver.Firefox(service=service, options=options)

driver.get("http://www.dummypoint.com/seleniumtemplate.html")

time.sleep(5)

driver.quit()