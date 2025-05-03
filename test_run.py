from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from pom.page.login_page import loginpage
from pom.page.signup_page import signup
from pom.page.article_page import article
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()
def login(driver):
    login_page=loginpage(driver)
    login_page.open_page("https://ekantipur.com/")
    driver.maximize_window()
    time.sleep(2)
    login_page.open_profile()
    time.sleep(1)

    login_page.scroll_page()
    #send username
    login_page.enter_email("magarsujan1433@gmail.com")
    time.sleep(1)
    # send password
    login_page.enter_password("Sujan12345")
    time.sleep(1)

    login_page.click_login()
    time.sleep(4)

#parameter values for username and password
@pytest.mark.parametrize("email, password", [
    ("magarsujan1433@gmail.com", "Sujan12345"),
    ("zzz@gmail.com", "password"),#wrong user
])
#for login test
def test_login(driver, email, password):
    login_page=loginpage(driver)
    login_page.open_page("https://ekantipur.com/")
    driver.maximize_window()
    time.sleep(2)
    login_page.open_profile()
    time.sleep(1)

    login_page.scroll_page()
    #send username
    login_page.enter_email(email)
    time.sleep(1)
    # send password
    login_page.enter_password(password)
    time.sleep(1)

    login_page.click_login()
    time.sleep(4)

#sign up test 
def test_signup(driver):
    signup_page=signup(driver)
    signup_page.open_page("https://ekantipur.com/")
    driver.maximize_window()
    time.sleep(2)
    signup_page.open_profile()
    time.sleep(2)

    signup_page.scroll_page1()

    signup_page.open_signup()
    time.sleep(1)

    signup_page.enter_fullname("Sachin Budhathoki")
    time.sleep(1)

    signup_page.enter_Semail("zzz12@gmail.com")
    time.sleep(1)

    signup_page.enter_Spassword("sac1234")
    time.sleep(1)

    signup_page.click_signup()
    time.sleep(3)

def test_article(driver):
    login(driver)
    article_page=article(driver)

    article_page.open_article()
    time.sleep(4)
#write title
    article_page.write_title("Automation")
    time.sleep(2)
#write a summary
    article_page.write_summary("This is an article of Automation.")
    time.sleep(1)
#write article
    article_page.click_normal("This is article based on automation testing. automation is a type of testing using tools and scripts to automate any product.")
    time.sleep(1)
#to insert link
    article_page.insert_link()
    time.sleep(3)
    
    # insert image
    article_page.insert_image()
    time.sleep(2)







