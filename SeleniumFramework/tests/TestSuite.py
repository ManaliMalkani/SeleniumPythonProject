# 1. Import the files
import unittest
from SeleniumFramework.tests.test_ContactFormtest import ContactFormTest
from SeleniumFramework.tests.test_EnterTextTest import EnterTextTest

#py.test --alluredir="/Users/mamalkani/PycharmProjects/SeleniumPythonProject/SeleniumFramework/reports/allureReports" tests/TestSuite.py
#allure serve /Users/mamalkani/PycharmProjects/SeleniumPythonProject/SeleniumFramework/reports/allureReports
# 2. Create the object of the class using unitTest
cf = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)
et = unittest.TestLoader().loadTestsFromTestCase(EnterTextTest)


# 3. Create TestSuite
regressionTest = unittest.TestSuite([cf,et])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)

# Note : All the methods in test files should define in proper run order
