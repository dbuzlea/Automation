import pyautogui as py

"""
List of available pyautogui examples:
"""

# Display alert box
py.alert(text="Hello, World!", title="", button="OK") 

# Displays alert and returns which button
confirmInput = py.confirm(text='', title='', buttons=['OK', 'Cancel'])
# returned button
print(confirmInput)
returnedText = py.prompt(text='', title='', default='')
 # returns text when 'OK' is selected, None when 'Cancel' is selected.
print(returnedText)

# Sets password to provided input:
password = py.password(text='Enter password:', title='Password', default='', mask='*')
print(password)  # return password
