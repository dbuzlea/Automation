import sys
import pyautogui as py

"""
Spotlight example that accepts 1 argument "String" and runs it through Spotlight
to search. When running in Terminal, provide the argument after the file.
Ex: "python3 spotlight.py Settings"
"""


def spotlight(text):
    py.keyDown('command')
    py.press('space')
    py.keyUp('command')
    py.write(text)
    py.press('return')
    return


spotlight(text=sys.argv[1])
