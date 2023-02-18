import pyautogui as py

"""
List of available pyautogui functions:
"""

py.alert(text="Hello, World!", title="", button="OK")  # Display alert box
confirmInput = py.confirm(text='', title='', buttons=['OK', 'Cancel'])  # Displays alert and returns which button
print(confirmInput)  # returned button
returnedText = py.prompt(text='', title='', default='')
print(returnedText)  # returns text when 'OK' is selected, None when 'Cancel' is selected.
password = py.password(text='Enter password:', title='Password', default='', mask='*')
print(password)  # return password
