import pyautogui as py
from selenium.webdriver.common.by import By
from selenium import webdriver as driver
import time

USERNAME = 'emailAddress@email.com'
PASS = 'Password'
chrome = driver.Chrome()


def log_in():
    print('Opening Browser...')
    driver.Chrome()
    time.sleep(3)

    print('Visiting Netflix...')
    chrome.get('https://www.netflix.com')
    time.sleep(3)

    print('Signing in...')
    sign_in = chrome.find_element(By.LINK_TEXT, 'Sign In')
    sign_in.click()
    time.sleep(3)

    #  Log-in Page:
    print('Entering Username...')
    username = chrome.find_element(By.CLASS_NAME, 'placeLabel')
    username.click()
    py.write(USERNAME)
    py.press('tab')
    time.sleep(2)
    print('Entering Password...')
    py.write(PASS)
    time.sleep(2)
    print('Signing in...')
    """Could not find element:"""
    # log_in = chrome.find_element(By.CLASS_NAME, 'btn login-button btn-submit-small')
    # log_in.click()
    py.press("Return")
    return


# log_in()


def begin():
    log_in()
    time.sleep(3)

    print("Logging out...")
    profile_name = chrome.find_element(By.CLASS_NAME, 'profile-name')
    profile_name.click()

    print("Closing alert...")
    py.moveTo(397, 217)
    time.sleep(2)
    py.click()

    print("Maximizing window...")
    py.moveTo(545, 8)
    py.click()
    time.sleep(1)
    py.moveTo(554, 62)
    py.click()
    time.sleep(2)

    print("Signing out of Netflix...")
    py.moveTo(1350, 183)
    py.moveTo(1312, 562)
    py.click()
    py.moveRel(720, 540)
    py.click()
    return


begin()
