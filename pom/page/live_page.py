#to test cricket live page
from selenium.webdriver.common.by import By
import time
class live:
    def __init__(self, driver):
        self.driver=driver
        self.close_button=(By.XPATH,"//a[@class='closeBtn']//*[name()='svg']")
        self.live_score=(By.XPATH,"//h2[normalize-space()='Live Score Update']")
        
    def close_profile(self):
        self.driver.find_element(*self.close_button).click()
    
    def check_live(self):
        self.driver.find_element(*self.live_score).click()

    
