import unittest
import pytest
import time
from SeleniumFramework.pages.EnterTextPage import EnterText

#pytest tests/test_EnterTextTest.py

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class EnterTextTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.et = EnterText(self.driver)

    @pytest.mark.order(4)
    def test_enterDataInEditBox(self):
        self.driver.maximize_window()
        time.sleep(2)
        self.et.enterText()
        self.et.clickOnSubmitButton()

    @pytest.mark.order(3)
    def test_clickOnLocatorsPage(self):
        self.et.clickOnLocatorsPage()