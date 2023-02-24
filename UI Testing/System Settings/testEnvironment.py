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






TIME_LIMIT = 5

class TestEnvironment:

	def run_battery_test_suite(self):
		Battery.batteryTestSuite()
		return

	def run_appleID_test_suite(self):
		AppleID.appleIDTestSuite()
		return

		# TODO:
	def run_accessibility_test_suite(self):
		Accessibility.accessibilityTestSuite()
		return

	def run_appearance_test_suite(self):
		Appearance.appearanceTestSuite()
		return

	def run_icloud_test_suite(self):
		iCloud.icloudTestSuite()
		return

	def run_bluetooth_test_suite(self):
		Bluetooth.bluetoothTestSuite()
		return

	def run_control_center_test_suite(self):
		ControlCenter.controlCenterTestSuite()
		return

	def run_desktop_and_dock_test_suite(self):
		DesktopAndDock.desktop_and_dockTestSuite()
		return

	def run_displays_test_suite(self):
		Displays.displaysTestSuite()
		return

	def run_focus_test_suite(self):
		Focus.focusTestSuite()
		return

	def run_general_test_suite(self):
		General.generalTestSuite()
		return

	def run_internet_accounts_test_suite(self):
		InternetAccounts.internetAccountsTestSuite()
		return

	def run_lock_screen_test_suite(self):
		LockScreen.lockScreenTestSuite()
		return

	def run_notifications_test_suite(self):
		Notifications.notificationsTestSuite()
		return

	def run_privacy_and_security_test_suite(self):
		Privacy.privacyAndSecurityTestSuite()
		return

	def run_screen_time_test_suite(self):
		ScreenTime.screenTimeTestSuite()
		return

	def run_siri_test_suite(self):
		Siri.siriTestSuite()
		return

	def run_sound_test_suite(self):
		Sound.soundTestSuite()
		return

	def run_touchID_and_password_test_suite(self):
		TouchIDAndPassword.touchIDAndPasswordTestSuite()
		return

	def run_users_and_groups_test_suite(self):
		UsersAndGroups.usersAndGroupsTestSuite()
		return

	def run_wallpaper_test_suite(self):
		Wallpaper.wallpaperTestSuite()
		return

	def run_wifi_test_suite(self):
		WiFi.wifiTestSuite()
		return


	def runTestEnvironment(self):
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
i.runTestEnvironment()

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



