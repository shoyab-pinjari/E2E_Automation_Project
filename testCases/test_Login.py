from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUseremail()
    passowrd = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_HomePageTitle(self,setup):
        self.logger.info("****** Test_Login_001 ******")
        self.logger.info("****** Verifying Home Page Title ******")
        self.driver =setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "SCORM Cloud - Log in securely to your account":
            assert True
            self.driver.close()
            self.logger.info("****** Home Page Title Test is Passed ******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("****** Home Page Title Test is Failed ******")
            assert False

"

