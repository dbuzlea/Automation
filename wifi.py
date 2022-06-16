import pyautogui as py
from spotlight import spotlight
import time


def open_wifi():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(568, 528)
    time.sleep(3)
    return


open_wifi()
