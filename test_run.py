from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from pom.page.login_page import loginpage
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

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
