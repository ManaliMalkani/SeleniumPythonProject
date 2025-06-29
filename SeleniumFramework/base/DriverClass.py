from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import SeleniumFramework.utilities.CustomLogger as cl

class WebDriverClass:
    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName.lower() == "chrome":
            service = ChromeService(executable_path="/Users/mamalkani/PycharmProjects/SeleniumPythonProject/drivers/chromedriver-mac-arm64/chromedriver")
            driver = webdriver.Chrome(service=service)
            self.log.info("Chrome Driver is initializing")

        elif browserName.lower() == "safari":
            driver = webdriver.Safari()
            self.log.info("Safari Driver is initializing")

        elif browserName.lower() == "firefox":
            service = FirefoxService(executable_path="/Users/mamalkani/PycharmProjects/SeleniumPythonProject/drivers/geckodriver/geckodriver")
            driver = webdriver.Firefox(service=service)
            self.log.info("Firefox Driver is initializing")

        else:
            self.log.error(f"Unsupported browser: {browserName}")

        return driver
