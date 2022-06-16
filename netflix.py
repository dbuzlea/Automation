import pyautogui as py
# from close import kill_app
from open import open_app
import time

"""
This program automates logging into Netflix with pre-set credentials and resume playing the first video in
the continue watching list.
"""


#  ===================================================================================================
#  Global:
USERNAME = "ddbuzlea31@gmail.com"
PASS = "Italia237"


#  ===================================================================================================
def open_netflix():
    open_app("Safari")
    time.sleep(3)
    py.click(468, 49)
    py.write("https://www.netflix.com")
    py.press('return')
    time.sleep(5)
    return


def watch_recent_in_continue_watching():
    log_in()
    py.click(166, 799)  # First option in 'Continue Watching for Daniel'
    time.sleep(5)
    py.click(378, 499)  # Resume
    time.sleep(13)
    py.click(1391, 791)  # Full screen
    time.sleep(10)
    # kill_app("Safari")
    return


def log_in():
    open_netflix()
    py.click(1336, 122)
    time.sleep(3)
    py.click(590, 322)  # Email or phone number
    py.write(USERNAME)
    py.press('tab')  # Switch to password entry
    py.write(PASS)
    time.sleep(5)
    py.click(714, 474)  # Sign in
    time.sleep(10)
    return


def log_out():
    open_netflix()
    py.click(1351, 110)  # Profiles
    time.sleep(2)
    py.click(1284, 493)  # Sign out of Netflix
    time.sleep(3)
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
