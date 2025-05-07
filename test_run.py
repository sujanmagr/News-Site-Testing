from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from pom.page.login_page import loginpage
from pom.page.signup_page import signup
from pom.page.article_page import article
from pom.page.live_page import live
from pom.page.search_page import search

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
def close_ad(driver):
    try:
        ad_close = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//i[@onclick="hide(\'roadblock-ad\')"]'))
        )
        ad_close.click()
        print("Ad closed successfully")
    except Exception as e:
        print("No ad popup or ad close button not found:", e)
#parameter values for username and password
@pytest.mark.parametrize("email, password", [
    ("magarsujan1433@gmail.com", "Sujan12345"),
    ("zzz@gmail.com", "password"),#wrong user
])
#for login test
def test_login(driver, email, password):
    login_page=loginpage(driver)
    login_page.open_page("https://ekantipur.com/")
    close_ad(driver)
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
    #to check login successful or not
    try:
        if "तपाईंको  प्रोफाइल " in driver.page_source:
            print("Login successful!")
            assert True 
        else:
            raise AssertionError("Login failed - 'profile' not found in page source.")
    
    except Exception as e:
        print(f"Error! {str(e)}")
        assert False 

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
    article_page.click_normal("This is article based on automation testing. Automation is a type of testing using tools and scripts to automate any product.")
    time.sleep(1)
#to insert link
    article_page.insert_link()
    time.sleep(3)
    
    # insert image
    article_page.insert_image()
    time.sleep(2)

    #save the article
    driver.execute_script("window.scrollTo(0,0);")
    article_page.save_article()
    time.sleep(4)
        #to check article save successful or not
    try:
        if "तपाईँको लेख सञ्चय गरिएको छ।" in driver.page_source:
            print("article saved successfully!")
            assert True 
        else:
            raise AssertionError("article save failed - 'article' not found in page source.")
    
    except Exception as e:
        print(f"Error! {str(e)}")
        assert False 


#to check live page
def test_live(driver):
    login(driver)
    live_page=live(driver)

    #close profile
    live_page.close_profile()
    time.sleep(1)
    # open live page
    live_page.check_live()

    # Step 2: Switch to the new tab
    driver.switch_to.window(driver.window_handles[1])
    page_height=driver.execute_script("return document.body.scrollHeight")
    scroll_speed=500
    scroll_iteration=int(page_height/scroll_speed)
    #loop to perform scroll
    for _ in range(scroll_iteration):
        driver.execute_script(f"window.scrollBy(0,{scroll_speed});") 
        time.sleep(4)

def test_search(driver):
    search_page=search(driver)
    login(driver)
    live_page=live(driver)

    #close profile
    live_page.close_profile()
    time.sleep(2)
    # click menu
    search_page.click_menu()
    time.sleep(1)

    #search content on the search bar 
    search_page.search_content()
    time.sleep(2)
    #scroll the page
    page_height=driver.execute_script("return document.body.scrollHeight")
    scroll_speed=500
    scroll_iteration=int(page_height/scroll_speed)
    #loop to perform scroll
    for _ in range(scroll_iteration):
        driver.execute_script(f"window.scrollBy(0,{scroll_speed});") 
        time.sleep(4)
















