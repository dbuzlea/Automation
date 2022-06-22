import pyautogui as py
from spotlight import spotlight
import time
import sys

"""Automation of the System Preferences. settings(String) accepts one argument as a string from the cli."""

PASSWORD = "Apple"


def appleid():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(294, 236)
    py.click()
    time.sleep(3)
    return


def wifi():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(281, 566)
    py.click()
    time.sleep(3)
    return


def bluetooth():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 281)
    py.click()
    time.sleep(3)
    return


def general():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(276, 434)
    py.click()
    time.sleep(3)
    return


def desktop_screen_saver():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(284, 325)
    py.click()
    time.sleep(3)
    return


def dock_menu_bar():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(281, 369)
    py.click()
    time.sleep(3)
    return


def siri():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(275, 743)
    py.click()
    time.sleep(3)
    return


def language_region():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(280, 501)
    py.click()
    time.sleep(3)
    return


def notifications_focus():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(284, 588)
    py.click()
    time.sleep(3)
    return


def internet_accounts():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(286, 457)
    py.click()
    time.sleep(3)
    return


def passwords():
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
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 214)
    py.click()
    time.sleep(3)
    return


def screen_time():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 677)
    py.click()
    time.sleep(3)
    return


def extensions():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 392)
    py.click()
    time.sleep(3)
    return


def security_privacy():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 699)
    py.click()
    time.sleep(3)
    return


def software_update():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 765)
    py.click()
    time.sleep(3)
    return


def sound():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 786)
    py.click()
    time.sleep(3)
    return


def touchid():
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
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 480)
    py.click()
    time.sleep(3)
    return


def trackpad():
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
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 545)
    py.click()
    time.sleep(3)
    return


def displays():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 346)
    py.click()
    time.sleep(3)
    return


def printers_scanners():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 632)
    py.click()
    time.sleep(3)
    return


def battery():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 259)
    py.click()
    time.sleep(3)
    return


def date_time():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 301)
    py.click()
    time.sleep(3)
    return


def sharing():
    spotlight("System Preferences")
    time.sleep(2)
    py.click(259, 7)
    time.sleep(1)
    py.moveTo(278, 721)
    py.click()
    time.sleep(3)
    return


def time_machine():
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
        appleid()
    elif setting == "General" or setting == "general":
        general()
    elif setting == "Desktop and Screen Saver" or setting == "desktop and screen saver" or setting == "Desktop & Screen Saver" or setting == "desktop & screen saver":
        desktop_screen_saver()
    elif setting == "Dock and Menu Bar" or setting == "dock and menu bar" or setting == "Dock & Menu Bar" or setting == "dock & menu bar":
        dock_menu_bar()
    elif setting == "Siri" or setting == "siri":
        siri()
    elif setting == "Language and Region" or setting == "language and region" or setting == "Language & Region" or setting == "language & region":
        language_region()
    elif setting == "Notifications and focus" or setting == "notifications and focus" or setting == "Notifications & Focus" or setting == "notifications & focus":
        notifications_focus()
    elif setting == "Internet Accounts" or setting == "internet accounts":
        internet_accounts()
    elif setting == "Passwords" or setting == "passwords":
        passwords()
    elif setting == "Wallet and Apple Pay" or setting == "wallet and apple pay" or setting == "Wallet & Apple Pay" or setting == "wallet & apple pay":
        wallet_apple_pay()
    elif setting == "Users and Groups" or setting == "users and groups" or setting == "Users & Groups" or setting == "users & groups":
        users_groups()
    elif setting == "Accessibility" or setting == "accessibility":
        accessibility()
    elif setting == "Screen Time" or setting == "screen time":
        screen_time()
    elif setting == "Extensions" or setting == "extensions":
        extensions()
    elif setting == "Security and Privacy" or setting == "security and privacy" or setting == "Security & Privacy" or setting == "security & privacy":
        security_privacy()
    elif setting == "Software Update" or setting == "software update":
        software_update()
    elif setting == "Wifi" or setting == "wifi":
        wifi()
    elif setting == "Bluetooth" or setting == "bluetooth":
        bluetooth()
    elif setting == "Sound" or setting == "sound":
        sound()
    elif setting == "Touch ID" or setting == "touch id":
        touchid()
    elif setting == "Keyboard" or setting == "keyboard":
        keyboard()
    elif setting == "Trackpad" or setting == "trackpad":
        trackpad()
    elif setting == "Mouse" or setting == "mouse":
        mouse()
    elif setting == "Displays" or setting == "displays":
        displays()
    elif setting == "Printers and Scanners" or setting == "printers and scanners" or setting == "printers & scanners" or setting == "Printers & Scanners":
        printers_scanners()
    elif setting == "Battery" or setting == "battery":
        battery()
    elif setting == "Date and Time" or setting == "date and time" or setting == " Date & Time" or setting == "date & time":
        date_time()
    elif setting == "Sharing" or setting == "sharing":
        sharing()
    elif setting == "Time Machine" or setting == "time machine":
        time_machine()
    elif setting == "Startup Disk" or setting == "startup disk":
        startup_disk()
    elif setting == "Profiles" or setting == "profiles":
        profiles()
    else:
        print("That is not a valid setting. Please enter in the exact setting exactly how it's spelled.")
    return


settings(setting=sys.argv[1])
