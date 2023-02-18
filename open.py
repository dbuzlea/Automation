import os

"""
OS example, similar to the close.py file, that accepts 1 argument in the form
of a "String" and runs the shell script "open -a" which open an application found
inside the /Applications folder. 
Ex: open -a Safari
"""

def open_app(app):
    os.system(f"open -a {app}")
    return


def open_url(url):
    os.system(f'open {url}')
    return

open_app("Safari")

# Open can also be used for opening URLs provided from the command line:

# open_url("https://www.apple.com")