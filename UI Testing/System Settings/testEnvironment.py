import pyautogui as py
import time
import os

from Battery.batteryTestSuite import Battery
from AppleID.appleIDTestSuite import AppleID
# from Accessibility.accessibilityTestSuite import Accessibility
from Appearance.appearanceTestSuite import Appearance
from AppleID.iCloud.icloudTestSuite import iCloud
from Bluetooth.bluetoothTestSuite import Bluetooth
from Control_Center.controlCenterTestSuite import ControlCenter
from Desktop_and_Dock.desktop_and_dockTestSuite import DesktopAndDock
from Displays.displaysTestSuite import Displays
from Focus.focusTestSuite import Focus
from General.generalTestSuite import General
from Internet_Accounts.internetAccountsTestSuite import InternetAccounts
from Lock_Screen.lockScreenTestSuite import LockScreen
from Notifications.notificationsTestSuite import Notifications
from Privacy_and_Security.privacyAndSecurityTestSuite import Privacy
from Screen_Time.screenTimeTestSuite import ScreenTime
from Siri.siriTestSuite import Siri
from Sound.soundTestSuite import Sound
from TouchID_and_Password.touchIDAndPasswordTestSuite import TouchIDAndPassword
from Users_and_Groups.usersAndGroupsTestSuite import UsersAndGroups
from Wallpaper.wallpaperTestSuite import Wallpaper
from WiFi.wifiTestSuite import WiFi


"""
TODO: Fix Accessibility  

Error: Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/danielbuzlea/Desktop/code/Programs/Python/app/Automation Projects/Automation/UI Testing/System Settings/testEnvironment.py", line 47, in run_accessibility_test_suite
    Accessibility.accessibilityTestSuite()
NameError: name 'Accessibility' is not defined

"""



TIME_LIMIT = 5

class TestEnvironment:

	@staticmethod
	def run_battery_test_suite():
		Battery.batteryTestSuite()
		return

	@staticmethod	
	def run_appleID_test_suite():
		AppleID.appleIDTestSuite()
		return

	@staticmethod	
		# TODO:
	def run_accessibility_test_suite():
		Accessibility.accessibilityTestSuite()
		return

	@staticmethod	
	def run_appearance_test_suite():
		Appearance.appearanceTestSuite()
		return

	@staticmethod	
	def run_icloud_test_suite():
		iCloud.icloudTestSuite()
		return

	@staticmethod	
	def run_bluetooth_test_suite():
		Bluetooth.bluetoothTestSuite()
		return

	@staticmethod	
	def run_control_center_test_suite():
		ControlCenter.controlCenterTestSuite()
		return

	@staticmethod	
	def run_desktop_and_dock_test_suite():
		DesktopAndDock.desktop_and_dockTestSuite()
		return

	@staticmethod	
	def run_displays_test_suite():
		Displays.displaysTestSuite()
		return

	@staticmethod	
	def run_focus_test_suite():
		Focus.focusTestSuite()
		return

	@staticmethod	
	def run_general_test_suite():
		General.generalTestSuite()
		return

	@staticmethod	
	def run_internet_accounts_test_suite():
		InternetAccounts.internetAccountsTestSuite()
		return

	@staticmethod	
	def run_lock_screen_test_suite():
		LockScreen.lockScreenTestSuite()
		return

	@staticmethod	
	def run_notifications_test_suite():
		Notifications.notificationsTestSuite()
		return

	@staticmethod	
	def run_privacy_and_security_test_suite():
		Privacy.privacyAndSecurityTestSuite()
		return

	@staticmethod	
	def run_screen_time_test_suite():
		ScreenTime.screenTimeTestSuite()
		return

	@staticmethod	
	def run_siri_test_suite():
		Siri.siriTestSuite()
		return

	@staticmethod	
	def run_sound_test_suite():
		Sound.soundTestSuite()
		return

	@staticmethod	
	def run_touchID_and_password_test_suite():
		TouchIDAndPassword.touchIDAndPasswordTestSuite()
		return

	@staticmethod	
	def run_users_and_groups_test_suite():
		UsersAndGroups.usersAndGroupsTestSuite()
		return

	@staticmethod	
	def run_wallpaper_test_suite():
		Wallpaper.wallpaperTestSuite()
		return

	@staticmethod	
	def run_wifi_test_suite():
		WiFi.wifiTestSuite()
		return


	@staticmethod	
	def run_all_test_suites():
		print("===============================================================")
		print("===============================================================")

		print("Running Test Environment...")

		print("===============================================================")
		print("===============================================================")

		i.run_battery_test_suite()

		print("===============================================================")

		i.run_appleID_test_suite()

		print("===============================================================")

		# i.run_accessibility_test_suite()

		print("===============================================================")

		i.run_appearance_test_suite()

		print("===============================================================")

		i.run_icloud_test_suite()

		print("===============================================================")

		i.run_bluetooth_test_suite()

		print("===============================================================")

		i.run_control_center_test_suite()

		print("===============================================================")

		i.run_desktop_and_dock_test_suite()

		print("===============================================================")

		i.run_displays_test_suite()

		print("===============================================================")

		i.run_focus_test_suite()

		print("===============================================================")

		i.run_general_test_suite()

		print("===============================================================")

		i.run_internet_accounts_test_suite()

		print("===============================================================")

		i.run_lock_screen_test_suite()

		print("===============================================================")

		i.run_notifications_test_suite()

		print("===============================================================")

		i.run_privacy_and_security_test_suite()

		print("===============================================================")

		i.run_screen_time_test_suite()

		print("===============================================================")

		i.run_siri_test_suite()

		print("===============================================================")

		i.run_sound_test_suite()

		print("===============================================================")

		i.run_touchID_and_password_test_suite()

		print("===============================================================")

		i.run_users_and_groups_test_suite()

		print("===============================================================")

		i.run_wallpaper_test_suite()

		print("===============================================================")

		i.run_wifi_test_suite()

		print("===============================================================")

		print("===============================================================")
		print("===============================================================")

		print("Test Environmenmt Finished.")

		print("===============================================================")
		print("===============================================================")
		return																				
			

# =====================================================================
# Tests:
i = TestEnvironment()

"""
Uncomment to run full program, 
comment out to run individual test cases 
in python interpretor.
"""
# i.run_all_test_suites()







# print("===============================================================")
# print("===============================================================")

# print("Running Test Environment...")

# print("===============================================================")
# print("===============================================================")

# i.run_battery_test_suite()

# print("===============================================================")

# i.run_appleID_test_suite()

# print("===============================================================")

# # i.run_accessibility_test_suite()

# print("===============================================================")

# i.run_appearance_test_suite()

# print("===============================================================")

# i.run_icloud_test_suite()

# print("===============================================================")

# i.run_bluetooth_test_suite()

# print("===============================================================")

# i.run_control_center_test_suite()

# print("===============================================================")

# i.run_desktop_and_dock_test_suite()

# print("===============================================================")

# i.run_displays_test_suite()

# print("===============================================================")

# i.run_focus_test_suite()

# print("===============================================================")

# i.run_general_test_suite()

# print("===============================================================")

# i.run_internet_accounts_test_suite()

# print("===============================================================")

# i.run_lock_screen_test_suite()

# print("===============================================================")

# i.run_notifications_test_suite()

# print("===============================================================")

# i.run_privacy_and_security_test_suite()

# print("===============================================================")

# i.run_screen_time_test_suite()

# print("===============================================================")

# i.run_siri_test_suite()

# print("===============================================================")

# i.run_sound_test_suite()

# print("===============================================================")

# i.run_touchID_and_password_test_suite()

# print("===============================================================")

# i.run_users_and_groups_test_suite()

# print("===============================================================")

# i.run_wallpaper_test_suite()

# print("===============================================================")

# i.run_wifi_test_suite()

# print("===============================================================")

# print("===============================================================")
# print("===============================================================")

# print("Test Environmenmt Finished.")

# print("===============================================================")
# print("===============================================================")



