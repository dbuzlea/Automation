import pyautogui as py
# from close import kill_app
from open import open_app
import time
import logging

"""
This program automates logging into Netflix with pre-set credentials and resume playing the first video in
the continue watching list.
"""


#  ===================================================================================================
#  Global:
USERNAME = "ddbuzlea31@gmail.com"
PASS = "Italia237"
py.FAILSAFE = True
logging.basicConfig(filename='netflix.log', level=logging.INFO)


#  ===================================================================================================
def open_netflix():
    print('Opening Safari...')
    open_app("Safari")
    time.sleep(3)
    print('Launching Netflix...')
    py.click(468, 49)
    py.write("https://www.netflix.com")
    py.press('return')
    time.sleep(5)
    return


def watch_recent_in_continue_watching():
    print('Logging in...')
    log_in()
    print('Selecting first option in continue watching...')
    py.click(166, 799)  # First option in 'Continue Watching for Daniel'
    time.sleep(5)
    print('Resume playing...')
    py.click(378, 499)  # Resume
    time.sleep(13)
    print('Enabling full screen mode...')
    py.click(1391, 791)  # Full screen
    time.sleep(10)
    # kill_app("Safari")
    return


def log_in():
    print('Opening Netflix...')
    open_netflix()
    print('Signing in...')
    py.click(1336, 122)
    time.sleep(3)
    print('Logging in with credentials...')
    py.click(590, 322)  # Email or phone number
    py.write(USERNAME)
    py.press('tab')  # Switch to password entry
    py.write(PASS)
    time.sleep(5)
    print('Credentials entered, signing in...')
    py.click(714, 474)  # Sign in
    time.sleep(10)
    return


def log_out():
    print('Opening Netflix...')
    open_netflix()
    print('Selecting Profiles...')
    py.click(1351, 110)  # Profiles
    time.sleep(2)
    print('Signing out of Netflix...')
    py.click(1284, 493)  # Sign out of Netflix
    time.sleep(3)
    print('Selecting Go Now...')
    py.click(720, 472)  # Go Now

    time.sleep(5)
    watch_recent_in_continue_watching()  # Uncomment to use this module by itself.
    return


#  ===================================================================================================
#  Tests:
log_out()
# open_safari()
# open_netflix()
# log_in()
# watch_recent_in_continue_watching()
