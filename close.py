import os

"""
OS function that accepts one arguement (In the form of a sting) and pkills the process.
Preferably an application. Ex: Notes, Safari, Music, etc.
"""


def kill_app(app):
    os.system(f"pkill {app}")
    return

# Launch Safari on your computer first:
kill_app("Safari")