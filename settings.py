import pyautogui as py
from spotlight import spotlight
import time
import sys

"""Automation of the System Preferences. settings(String) accepts one argument as a string from the cli."""

PASSWORD = "Apple"


def appleid():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(294, 236)
    py.click()
    time.sleep(3)
    return


def wifi():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(281, 566)
    py.click()
    time.sleep(3)
    return


def bluetooth():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 281)
    py.click()
    time.sleep(3)
    return


def general():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(276, 434)
    py.click()
    time.sleep(3)
    return


def desktop_screen_saver():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(284, 325)
    py.click()
    time.sleep(3)
    return


def dock_menu_bar():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(281, 369)
    py.click()
    time.sleep(3)
    return


def siri():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(275, 743)
    py.click()
    time.sleep(3)
    return


def language_region():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(280, 501)
    py.click()
    time.sleep(3)
    return


def notifications_focus():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(284, 588)
    py.click()
    time.sleep(3)
    return


def internet_accounts():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(286, 457)
    py.click()
    time.sleep(3)
    return


def passwords():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(283, 610)
    py.click()
    time.sleep(3)
    py.write(PASSWORD)
    py.press("Return")
    return


def wallet_apple_pay():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.press("w")
    time.sleep(1)
    py.moveTo(278, 825)
    py.click()
    time.sleep(3)
    return


def users_groups():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.press("u")
    time.sleep(1)
    py.moveTo(277, 808)
    py.click()
    time.sleep(3)
    return


def accessibility():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 214)
    py.click()
    time.sleep(3)
    return


def screen_time():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 677)
    py.click()
    time.sleep(3)
    return


def extensions():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 392)
    py.click()
    time.sleep(3)
    return


def security_privacy():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 699)
    py.click()
    time.sleep(3)
    return


def software_update():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 765)
    py.click()
    time.sleep(3)
    return


def sound():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 786)
    py.click()
    time.sleep(3)
    return


def touchid():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.press("t")
    py.press("o")
    time.sleep(1)
    py.moveTo(278, 808)
    py.click()
    time.sleep(3)
    return


def keyboard():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 480)
    py.click()
    time.sleep(3)
    return


def trackpad():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.press("t")
    py.press("r")
    time.sleep(1)
    py.moveTo(278, 810)
    py.click()
    time.sleep(3)
    return


def mouse():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 545)
    py.click()
    time.sleep(3)
    return


def displays():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 346)
    py.click()
    time.sleep(3)
    return


def printers_scanners():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 632)
    py.click()
    time.sleep(3)
    return


def battery():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 259)
    py.click()
    time.sleep(3)
    return


def date_time():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 301)
    py.click()
    time.sleep(3)
    return


def sharing():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 721)
    py.click()
    time.sleep(3)
    return


def time_machine():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.press("t")
    py.press("i")
    time.sleep(1)
    py.moveTo(278, 810)
    py.click()
    time.sleep(3)
    return


def startup_disk():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.press("s")
    py.press("t")
    time.sleep(1)
    py.moveTo(278, 808)
    py.click()
    time.sleep(3)
    return


def profiles():
    time.sleep(1)
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 655)
    py.click()
    time.sleep(3)
    return


def settings(setting):
    if setting == "AppleID" or setting == "appleid" or setting == "appleID" or setting == "Appleid":
        print(f"Opening {setting} pane...")
        appleid()
        print(f"{setting} pane successfully launched")
    elif setting == "General" or setting == "general":
        print(f"Opening {setting} pane...")
        general()
        print(f"{setting} pane successfully launched")
    elif setting == "Desktop and Screen Saver" or setting == "desktop and screen saver" or setting == "Desktop & Screen Saver" or setting == "desktop & screen saver":
        print(f"Opening {setting} pane...")
        desktop_screen_saver()
        print(f"{setting} pane successfully launched")
    elif setting == "Dock and Menu Bar" or setting == "dock and menu bar" or setting == "Dock & Menu Bar" or setting == "dock & menu bar":
        print(f"Opening {setting} pane...")
        dock_menu_bar()
        print(f"{setting} pane successfully launched")
    elif setting == "Siri" or setting == "siri":
        print(f"Opening {setting} pane...")
        siri()
        print(f"{setting} pane successfully launched")
    elif setting == "Language and Region" or setting == "language and region" or setting == "Language & Region" or setting == "language & region":
        print(f"Opening {setting} pane...")
        language_region()
        print(f"{setting} pane successfully launched")
    elif setting == "Notifications and focus" or setting == "notifications and focus" or setting == "Notifications & Focus" or setting == "notifications & focus":
        print(f"Opening {setting} pane...")
        notifications_focus()
        print(f"{setting} pane successfully launched")
    elif setting == "Internet Accounts" or setting == "internet accounts":
        print(f"Opening {setting} pane...")
        internet_accounts()
        print(f"{setting} pane successfully launched")
    elif setting == "Passwords" or setting == "passwords":
        print(f"Opening {setting} pane...")
        passwords()
        print(f"{setting} pane successfully launched")
    elif setting == "Wallet and Apple Pay" or setting == "wallet and apple pay" or setting == "Wallet & Apple Pay" or setting == "wallet & apple pay":
        print(f"Opening {setting} pane...")
        wallet_apple_pay()
        print(f"{setting} pane successfully launched")
    elif setting == "Users and Groups" or setting == "users and groups" or setting == "Users & Groups" or setting == "users & groups":
        print(f"Opening {setting} pane...")
        users_groups()
        print(f"{setting} pane successfully launched")
    elif setting == "Accessibility" or setting == "accessibility":
        print(f"Opening {setting} pane...")
        accessibility()
        print(f"{setting} pane successfully launched")
    elif setting == "Screen Time" or setting == "screen time":
        print(f"Opening {setting} pane...")
        screen_time()
        print(f"{setting} pane successfully launched")
    elif setting == "Extensions" or setting == "extensions":
        print(f"Opening {setting} pane...")
        extensions()
        print(f"{setting} pane successfully launched")
    elif setting == "Security and Privacy" or setting == "security and privacy" or setting == "Security & Privacy" or setting == "security & privacy":
        print(f"Opening {setting} pane...")
        security_privacy()
        print(f"{setting} pane successfully launched")
    elif setting == "Software Update" or setting == "software update":
        print(f"Opening {setting} pane...")
        software_update()
        print(f"{setting} pane successfully launched")
    elif setting == "Wifi" or setting == "wifi":
        print(f"Opening {setting} pane...")
        wifi()
        print(f"{setting} pane successfully launched")
    elif setting == "Bluetooth" or setting == "bluetooth":
        print(f"Opening {setting} pane...")
        bluetooth()
        print(f"{setting} pane successfully launched")
    elif setting == "Sound" or setting == "sound":
        print(f"Opening {setting} pane...")
        sound()
        print(f"{setting} pane successfully launched")
    elif setting == "Touch ID" or setting == "touch id":
        print(f"Opening {setting} pane...")
        touchid()
        print(f"{setting} pane successfully launched")
    elif setting == "Keyboard" or setting == "keyboard":
        print(f"Opening {setting} pane...")
        keyboard()
        print(f"{setting} pane successfully launched")
    elif setting == "Trackpad" or setting == "trackpad":
        print(f"Opening {setting} pane...")
        trackpad()
        print(f"{setting} pane successfully launched")
    elif setting == "Mouse" or setting == "mouse":
        print(f"Opening {setting} pane...")
        mouse()
        print(f"{setting} pane successfully launched")
    elif setting == "Displays" or setting == "displays":
        print(f"Opening {setting} pane...")
        displays()
        print(f"{setting} pane successfully launched")
    elif setting == "Printers and Scanners" or setting == "printers and scanners" or setting == "printers & scanners" or setting == "Printers & Scanners":
        print(f"Opening {setting} pane...")
        printers_scanners()
        print(f"{setting} pane successfully launched")
    elif setting == "Battery" or setting == "battery":
        print(f"Opening {setting} pane...")
        battery()
        print(f"{setting} pane successfully launched")
    elif setting == "Date and Time" or setting == "date and time" or setting == " Date & Time" or setting == "date & time":
        print(f"Opening {setting} pane...")
        date_time()
        print(f"{setting} pane successfully launched")
    elif setting == "Sharing" or setting == "sharing":
        print(f"Opening {setting} pane...")
        sharing()
        print(f"{setting} pane successfully launched")
    elif setting == "Time Machine" or setting == "time machine":
        print(f"Opening {setting} pane...")
        time_machine()
        print(f"{setting} pane successfully launched")
    elif setting == "Startup Disk" or setting == "startup disk":
        print(f"Opening {setting} pane...")
        startup_disk()
        print(f"{setting} pane successfully launched")
    elif setting == "Profiles" or setting == "profiles":
        print(f"Opening {setting} pane...")
        profiles()
        print(f"{setting} pane successfully launched")
    else:
        print(f"{setting} is not a valid setting. Please enter in the exact setting exactly how it's spelled.")
    return


settings(sys.argv[1])
