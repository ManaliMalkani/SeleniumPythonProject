from traceback import print_stack
import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import SeleniumFramework.utilities.CustomLogger as cl


class BaseClass:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def launchWebPage(self, url, title):
        try:
            self.driver.get(url)
            assert title in self.driver.title
            self.log.info(f"Web Page Launched with URL: {url}")
        except Exception as e:
            self.log.error(f"Web Page not Launched with URL: {url}. Error: {str(e)}")
            print_stack()

    def getLocatorType(self, locatorType):
        locatorType = locatorType.lower()
        mapping = {
            "id": By.ID,
            "name": By.NAME,
            "class": By.CLASS_NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "tag": By.TAG_NAME,
            "link": By.LINK_TEXT,
            "plink": By.PARTIAL_LINK_TEXT,
        }
        result = mapping.get(locatorType)
        if not result:
            self.log.error(f"Locator Type '{locatorType}' is invalid")
        return result

    def getWebElement(self, locatorValue, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            webElement = self.driver.find_element(locatorByType, locatorValue)
            self.log.info(f"WebElement found: '{locatorValue}' using '{locatorType}'")
            return webElement
        except Exception as e:
            self.log.error(f"WebElement not found: '{locatorValue}' using '{locatorType}'. Error: {str(e)}")
            print_stack()
            return None

    def waitForElement(self, locatorValue, locatorType="id", timeout=25):
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            wait = WebDriverWait(self.driver, timeout, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            webElement = wait.until(ec.presence_of_element_located((locatorByType, locatorValue)))
            self.log.info(f"Wait successful: '{locatorValue}' using '{locatorType}'")
            return webElement
        except Exception as e:
            self.log.error(f"Element not found during wait: '{locatorValue}' using '{locatorType}'. Error: {str(e)}")
            print_stack()
            self.takeScreenshot(locatorType)
            assert False
        return webElement

    def clickOnElement(self, locatorValue, locatorType="id"):
        try:
            webElement = self.waitForElement(locatorValue, locatorType)
            if webElement:
                webElement.click()
                self.log.info(f"Clicked element: '{locatorValue}' using '{locatorType}'")
            else:
                raise Exception("Element not found to click")
        except Exception as e:
            self.log.error(f"Click failed: '{locatorValue}' using '{locatorType}'. Error: {str(e)}")
            print_stack()
            self.takeScreenshot(locatorType)
            assert False

    def sendText(self, text, locatorValue, locatorType="id"):
        try:
            webElement = self.waitForElement(locatorValue, locatorType)
            if webElement:
                webElement.send_keys(text)
                self.log.info(f"Sent text: '{text}' to '{locatorValue}' using '{locatorType}'")
            else:
                raise Exception("Element not found to send text")
        except Exception as e:
            self.log.error(f"Text send failed: '{text}' to '{locatorValue}' using '{locatorType}'. Error: {str(e)}")
            print_stack()
            self.takeScreenshot(locatorType)
            assert False

    def getText(self, locatorValue, locatorType="id"):
        try:
            webElement = self.waitForElement(locatorValue, locatorType)
            if webElement:
                elementText = webElement.text
                self.log.info(f"Got text: '{elementText}' from '{locatorValue}' using '{locatorType}'")
                return elementText
            else:
                raise Exception("Element not found to get text")
        except Exception as e:
            self.log.error(f"Text retrieval failed: '{locatorValue}' using '{locatorType}'. Error: {str(e)}")
            print_stack()
            self.takeScreenshot(locatorType)
            assert False
            return ""

    def isElementDisplayed(self, locatorValue, locatorType="id"):
        try:
            webElement = self.waitForElement(locatorValue, locatorType)
            if webElement:
                displayed = webElement.is_displayed()
                self.log.info(f"Element is displayed: '{locatorValue}' using '{locatorType}'")
                return displayed
            else:
                raise Exception("Element not found to check display status")
        except Exception as e:
            self.log.error(f"Display check failed for: '{locatorValue}' using '{locatorType}'. Error: {str(e)}")
            print_stack()
            return False

    def scrollTo(self, locatorValue, locatorType="id"):
        try:
            webElement = self.waitForElement(locatorValue, locatorType)
            if webElement:
                actions = ActionChains(self.driver)
                actions.move_to_element(webElement).perform()
                self.log.info(f"Scrolled to: '{locatorValue}' using '{locatorType}'")
            else:
                raise Exception("Element not found to scroll to")
        except Exception as e:
            self.log.error(f"Scroll failed: '{locatorValue}' using '{locatorType}'. Error: {str(e)}")
            print_stack()

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)