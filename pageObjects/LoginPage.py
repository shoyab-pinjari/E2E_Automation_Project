from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
#https://app.cloud.scorm.com/sc/guest/SignInForm
    email_textbox_xpath ="//div[@id='signin_wrapper' and @class='container']//form/input[@id='email']"
    password_txtbox_xpath ="//div[@id='signin_wrapper' and @class='container']//form/input[@id='password']"
    button_submit_xpath = "//div[@id='signin_wrapper' and @class='container']//form/input[@type='submit']"

    def Email(self,email):
        self.driver.find_element(By.XPATH,self.email_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_textbox_xpath).send_keys("shoyab.pinjari@gmail.com")

    def Password(self,password):
        self.driver.find_element(By.XPATH,self.password_txtbox_xpath).clear()
        self.driver.find_element(By.XPATH,self.password_txtbox_xpath).send_keys("Jethalaal1234")

    def LoginBtnClick(self):
        self.driver.find_element(By.XPATH,self.button_submit_xpath).click()

