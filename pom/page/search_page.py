#to test sign up page
from selenium.webdriver.common.by import By
import time
class search:
    def __init__(self, driver):
        self.driver=driver
        self.menu=(By.XPATH,"//button[@id='nav-menu-btn']")
        self.search_textbox=(By.XPATH,"//input[@id='txtSearchBox']")
        self.search_button=(By.XPATH,"//button[normalize-space()='Search']")



    def click_menu(self):
        self.driver.find_element(*self.menu).click()
    
    def search_content(self):
        self.driver.find_element(*self.search_textbox).send_keys("education")
        self.driver.find_element(*self.search_button).click()
