#to test sign up page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class home:
    def __init__(self, driver):
        self.driver=driver



    def open_page(self, url):
        self.driver.get(url)

    def click_news(self):
        try:
        # Wait for the first news item to be present and clickable
            first_news = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,"/html[1]/body[1]/div[7]/div[3]/div[2]/div[1]/main[1]/section[1]/div[1]/article[1]/h2[1]/a[1]"))
                # EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class, 'block--news') or contains(@class, 'teaser') or contains(@class, 'featured')]//a)[1]"))
        )
            first_news.click()
            print("First news clicked successfully.")
        except Exception as e:
            print(f"Failed to click the first news: {e}")



