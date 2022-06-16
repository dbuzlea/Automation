from selenium import webdriver
import time
import pyautogui

"""
Demonstration of webdriver and its functions:
"""

# =====================================================================================================================
safari = webdriver.Safari()

# =====================================================================================================================
# Instructions:
safari.get("https://www.netflix.com")
time.sleep(5)
pyautogui.click(715, 122)  # Sign In
time.sleep(3)
pyautogui.click(275, 322)  # Email or phone number
pyautogui.write("ddbuzlea31@gmail.com")
pyautogui.click(305, 411)  # Enter in your password
pyautogui.write("Italia237")
pyautogui.click(401, 532)  # Login
safari.close()
