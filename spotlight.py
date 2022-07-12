import sys

import pyautogui as py


def spotlight(text):
    py.keyDown('command')
    py.press('space')
    py.keyUp('command')
    py.write(text)
    py.press('return')
    return


spotlight(text=sys.argv[1])
