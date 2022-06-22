import pyautogui as py

py.keyDown('command')
py.press('space')
py.keyUp('command')

py.write('Terminal')
py.press('Return')

py.write('caffeinate -d')
py.press('Return')
