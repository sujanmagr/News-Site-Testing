#to test article page
from selenium.webdriver.common.by import By
import time

class article:
    def __init__(self, driver) :
        self.driver=driver
        self.write_article=(By.XPATH,"//div[@class='writeArticleTitleText']")
        self.title_textbox=(By.XPATH,"//textarea[@placeholder='शीर्षक']")
        self.summary_textbox=(By.XPATH,"//textarea[@placeholder='सारांश']")
        self.type_normal=(By.XPATH,"//div[@class='fr-element fr-view']")
        self.link=(By.ID, "insertLink-1")
        self.link_url=(By.ID, "fr-link-insert-layer-url-1")
        self.link_text=(By.XPATH, "//*[@id='fr-link-insert-layer-text-1']")
        self.insert_button=(By.XPATH,"//*[@id='fr-link-insert-layer-1']/div[4]/button")
        self.image=(By.ID, "insertImage-1")
        self.file_field=(By.XPATH, "//*[@id='fr-image-upload-layer-1']/div/input")
       

    def open_article(self):
        self.driver.find_element(*self.write_article).click()

    def write_title(self, title):
        self.driver.find_element(*self.title_textbox).send_keys(title)

    def write_summary(self, summary):
        self.driver.find_element(*self.summary_textbox).send_keys(summary)

    def click_normal(self, body):
        self.driver.find_element(*self.type_normal).send_keys(body)

    def insert_link(self):
        self.driver.find_element(*self.link).click()
        time.sleep(1)
        self.driver.find_element(*self.link_url).send_keys("https://ekantipur.com")
        self.driver.find_element(*self.link_text).click()
        self.driver.find_element(*self.link_text).send_keys("Kantipur")
        time.sleep(1)
        self.driver.find_element(*self.insert_button).click()
    
    def insert_image(self):
        self.driver.find_element(*self.image).click()
        time.sleep(1)
        self.driver.find_element(*self.file_field).send_keys("C:/Users/Bhabisara Budhathoki/Desktop/sdmn.jpg")
        time.sleep(1)





