from selenium.webdriver.common.by import By
#pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
class LoginPage:
    # Login Page
    loginSignUp_Xpath='//a[contains(text(),"Signup")]'
    textbox_email_name="email"
    textbox_password_name="password"
    button_login_xpath="//button[@type='submit' and contains(text(),'Login')]"
    text_checkLoggedIn_Xpath='//a[contains(text(),"Logged in as")]'

    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(20)
        

    def clickLoginSignupButton(self):
        self.driver.find_element(By.XPATH,self.loginSignUp_Xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.textbox_email_name).clear()
        self.driver.find_element(By.NAME, self.textbox_email_name).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.NAME,self.textbox_password_name).clear()
        self.driver.find_element(By.NAME,self.textbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def loggedInConfirmation(self):
        count=self.driver.find_elements(By.XPATH,self.text_checkLoggedIn_Xpath)
        if len(count)>0:
            return True
        else:
            return False
    def revertBackTologinPage(self,loginPageUrl):
        self.driver.get(loginPageUrl)