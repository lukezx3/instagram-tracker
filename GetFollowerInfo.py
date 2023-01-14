from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from FollowTracker import password

username = 'fl.eeb'


def login(driver):
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("name", "password").send_keys(u'\ue007')

def click_button_with_css(driver, css_selector):
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    element.click()


def navigate_to_followers(driver):
    dropdown_css = '[alt*="' + username + '"]'
    profile_css = "[href*=\"" + username + "\"]"
    click_button_with_css(driver, dropdown_css)
    click_button_with_css(driver, profile_css)

def __main__():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(1)
    login(driver)
    navigate_to_followers(driver)
    time.sleep(10000)


    return
    
__main__()
