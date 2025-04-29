#to test login page
from selenium.webdriver.common.by import By
import time
class loginpage:
    def __init__(self, driver):
        self.driver=driver
        self.profile=(By.XPATH,"//span[@class='menu-login-hide']")
        self.email_textbox=(By.XPATH,"//input[@id='txtEmail1']")
        self.password_textbox=(By.XPATH,"//input[@id='txtPassword1']")
        self.login_button=(By.XPATH,"//div[@class='col-md-6 col-xs-12 col-sm-12']//div[@id='login-btn']")
    def open_page(self, url):
        self.driver.get(url)
    
    def open_profile(self):
        self.driver.find_element(*self.profile).click()
    
    def scroll_page(self):
        self.driver.execute_script("window.scrollBy(0,90);")

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

