import os


def open_app(app):
    os.system(f"open -a {app}")
    return


def open_url(url):
    os.system(f'open {url}')
    return
