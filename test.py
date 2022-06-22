from selenium import webdriver
import pyautogui as py
from selenium.webdriver.common.by import By

browser = webdriver.Safari()

browser.get('https://www.google.com')
images = browser.find_element(By.LINK_TEXT, "https://www.google.com/imghp?hl=en&ogbl")
py.moveTo(images)
py.click()
