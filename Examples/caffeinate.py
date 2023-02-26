
"""
Pyautogui example: Open spotlight via keyboard shortcut, open Terminal, and enter
and run the shell command 'caffeinate -d'.
"""

import pyautogui as py

def pyautogui_example():
	py.keyDown('command')
	py.press('space')
	py.keyUp('command')

	py.write('Terminal')
	py.press('Return')

	py.write('caffeinate -d')
	py.press('Return')
	return


"""
Easier way of executing this code with less lines is by usuing OS framework.
Where the 'system' module in os can run shell scripts by the argument that is
passed in. 
"""

import os

def os_example():
	os.system("caffeinate -d")
	return


# Uncomment to run:
pyautogui_example()
# os_example()	

