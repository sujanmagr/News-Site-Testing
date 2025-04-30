#to test sign up page
from selenium.webdriver.common.by import By
import time
class signup:
    def __init__(self, driver):
        self.driver=driver
        self.profile=(By.XPATH,"//span[@class='menu-login-hide']")
        self.sign_page=(By.LINK_TEXT,"साइन अप")
        self.fullname_textbox=(By.XPATH,"//input[@id='txtFullNameee']")
        self.email_textbox=(By.XPATH,"//input[@id='txtEmaill1']")
        self.password_textbox=(By.XPATH,"//input[@id='txtPassworddd']")
        self.signup_button=(By.XPATH,"//div[@class='default-btn signupText']")
    def open_page(self, url):
        self.driver.get(url)
    
    def open_profile(self):
        self.driver.find_element(*self.profile).click()
    
    def scroll_page1(self):
        self.driver.execute_script("window.scrollBy(0,110);")

    def open_signup(self):
        self.driver.find_element(*self.sign_page).click()

    def enter_fullname(self, fullname):
        self.driver.find_element(*self.fullname_textbox).send_keys(fullname)
    
    def enter_Semail(self, Semail):
        self.driver.find_element(*self.email_textbox).send_keys(Semail)

    def enter_Spassword(self, Spassword):
        self.driver.find_element(*self.password_textbox).send_keys(Spassword)
    
    def click_signup(self):
        self.driver.find_element(*self.signup_button).click()

    