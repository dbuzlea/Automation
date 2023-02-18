import pyautogui

"""
This demonstrates pyautogui mouse capabilities:
"""

print(pyautogui.size())

# pyautogui.moveTo(500, 100)
print(pyautogui.position())
# pyautogui.click(100,100)

# Moves to the given coordinates then calls the click() method to simulate a mouse click.
pyautogui.moveTo(24.12)
pyautogui.click()
