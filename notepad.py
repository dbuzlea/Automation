import pyautogui as py
import time
import os
import sys

"""
This program opens the Notes app, creates a new note, and then writes into it a pre-set string.
After waiting 3 seconds, the Notes app closes and the program ends. 
"""


#  ===================================================================================================
def take_notes(text):
    os.system("open -a 'Notes'")  # open Notes
    time.sleep(5)
    # Create a note
    py.click(123,13)
    time.sleep(1)
    py.click(147,41)
    time.sleep(1)
    py.write(text)
    time.sleep(13)
    os.system("pkill 'Notes'")  # close Notes
    return


#  ===================================================================================================
#  Tests:
take_notes(sys.argv[1])
