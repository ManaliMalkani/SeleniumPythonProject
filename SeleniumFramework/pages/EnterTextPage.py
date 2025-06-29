from SeleniumFramework.base.BasePage import BaseClass
import SeleniumFramework.utilities.CustomLogger as cl


class EnterText(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact form
    _seleniumTemplate = "//*[@id='sidebar-wrapper']/ul/li[5]/a/span"  # xpath
    _locatorsPage="Locators" # link
    _enterTextEditBox = "user_input"  # id
    _submitButton = "submitbutton"  # id

    def clickOnLocatorsPage(self):
        self.clickOnElement(self._seleniumTemplate, "xpath")
        self.clickOnElement(self._locatorsPage,"link")

    def enterText(self):
        self.sendText("Code2Lead",self._enterTextEditBox,"id")
        cl.allureLogs("Entered Text in Edit Box")

    def clickOnSubmitButton(self):
        self.clickOnElement(self._submitButton,"id")