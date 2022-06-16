import pyautogui as py
import time
import os

"""
This program opens the Notes app, creates a new note, and then writes into it a pre-set string.
After waiting 3 seconds, the Notes app closes and the program ends. 
"""


#  ===================================================================================================
def take_notes(text):
    os.system("open -a 'Notes'")  # open Notes
    time.sleep(3)
    py.click(852, 50)  # Create a note
    py.write(text)
    time.sleep(13)
    os.system("pkill 'Notes'")  # close Notes
    return


#  ===================================================================================================
#  Tests:
take_notes("Hello, world!")
