import os


def kill_app(app):
    os.system(f"pkill {app}")
    return
