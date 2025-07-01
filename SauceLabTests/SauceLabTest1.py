import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException
)
from selenium.webdriver.chrome.options import Options

# ========== Configuration ========== #

SAUCE_USERNAME = os.getenv("SAUCE_USERNAME", "oauth-manalimalkani-e6934")
SAUCE_ACCESS_KEY = os.getenv("SAUCE_ACCESS_KEY", "bc45d8d8-7901-4147-8c41-c0cf4e2cc842")
SAUCE_REGION = "eu-central-1"
SAUCE_URL = f"https://{SAUCE_USERNAME}:{SAUCE_ACCESS_KEY}@ondemand.{SAUCE_REGION}.saucelabs.com:443/wd/hub"

TARGET_URL = "http://www.dummypoint.com/seleniumtemplate.html"

# ========== Sauce Options ========== #

def create_driver():
    options = Options()
    options.browser_version = "latest"
    options.platform_name = "macOS 10.15"

    sauce_options = {
        "name": "Dummy Point Test in Mac",
        "build": "Dummypoint Regression Test",
        "screenResolution": "1024x768",
        "username": SAUCE_USERNAME,
        "accessKey": SAUCE_ACCESS_KEY,
        "tags": ["instant-sauce", "pytest", "module4"],
    }

    options.set_capability("sauce:options", sauce_options)

    print("Connecting to Sauce Labs...")
    driver = webdriver.Remote(
        command_executor=SAUCE_URL,
        options=options
    )

    return driver

# ========== Test Logic ========== #

def run_test():
    driver = create_driver()

    try:
        print(f"Navigating to {TARGET_URL}")
        driver.get(TARGET_URL)

        wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[
            ElementNotInteractableException, NoSuchElementException
        ])

        print("Waiting for input field...")
        input_box = wait.until(EC.presence_of_element_located((By.ID, "user_input")))
        input_box.send_keys("Code2Lead")
        print("✅ Text entered successfully.")

        time.sleep(3)

    except Exception as e:
        print(f"❌ Test failed: {e}")
        driver.save_screenshot("failure_screenshot.png")
    finally:
        print("Closing browser session.")
        driver.quit()

# ========== Execute ========== #

if __name__ == "__main__":
    run_test()