import unittest
import pytest
import time
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.ContctFormPage import ContactForm
import SeleniumFramework.utilities.CustomLogger as cl

#pytest tests/test_ContactFormtest.py
#py.test --alluredir="/Users/mamalkani/PycharmProjects/SeleniumPythonProject/SeleniumFramework/reports/allureReports" tests/test_ContactFormtest.py
#allure serve /Users/mamalkani/PycharmProjects/SeleniumPythonProject/SeleniumFramework/reports/allureReports

@pytest.mark.usefixtures("beforeClass","beforeMethod")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)
        self.bp = BaseClass(self.driver)


    @pytest.mark.order(2)
    def test_enterDataInForm(self):
        time.sleep(5)
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterMessage()
        self.cf.enterCaptha()
        self.cf.clickOnPostButton()

    @pytest.mark.order(1)
    def test_formPage(self):
        self.cf.clickContactForm()
        self.cf.verifyFormPage()
