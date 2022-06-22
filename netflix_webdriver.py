import pyautogui as py
from selenium.webdriver.common.by import By
from selenium import webdriver as driver
import time

USERNAME = 'ddbuzlea31@gmail.com'
PASS = 'Italia237'


print('Opening Browser...')
chrome = driver.Chrome()
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
log_in = chrome.find_element(By.CLASS_NAME, 'btn login-button btn-submit-small')
log_in.click()
