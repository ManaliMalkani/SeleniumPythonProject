from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException, ElementNotSelectableException
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

driver.get("http://www.dummypoint.com/Frame.html")
time.sleep(2)


wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele = driver.find_elements(By.TAG_NAME, "iframe")

# To display number of Iframes in web page
print("List of iframe : ", len(ele))

""" 
# Switch to iframe by index
time.sleep(2)
driver.switch_to.frame(1)

data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",data.text) """

"""  
# Switch to iframe by name
time.sleep(2)
driver.switch_to.frame("farme3")

data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",data.text)  """


"""   
# Switch to iframe by id
time.sleep(2)
driver.switch_to.frame("f4")

data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",data.text) """


# Switch to iframe by WebElement

time.sleep(2)
ele = driver.find_element(By.ID,"f2")
driver.switch_to.frame(ele)

data = driver.find_element(By.ID,"framename")
print("Frame Name is : ",data.text)


# Switching back to normal content page from frame
time.sleep(2)
driver.switch_to.default_content()

data = driver.find_element(By.ID,"framename")
print("Webpage Name is : ",data.text)

time.sleep(2)
driver.quit()