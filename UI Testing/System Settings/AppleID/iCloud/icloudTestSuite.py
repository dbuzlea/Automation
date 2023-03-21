import pyautogui as py
import time
import os

TIME_LIMIT = 10

class iCloud:

	@staticmethod
	def setUp():
		time.sleep(1)
		print("Setting up test environment...")
		os.system("open -a 'System Settings'")
		time.sleep(2)

		py.keyDown('command')
		py.press('f')
		py.keyUp('command')

		time.sleep(2)

		py.write("iClou")
		time.sleep(2)
		py.press('return')

		time.sleep(2)

		py.press('down')
		# py.press('down')
		time.sleep(1)
		# py.press('return')
		print("Test environmenmt successfully set up.")


	@staticmethod
	def tearDown():
		time.sleep(1)
		print("Tearing down test environment...")
		os.system("pkill -a 'System Settings'")



# MANAGE iCLOUD:
	@staticmethod
	def test_open_manage_icloud_settings():

		i.setUp()

		print("Selecting Manage button...")
		time.sleep(1)

		py.moveTo(644, 96)
		py.click()

		time.sleep(TIME_LIMIT)
		print("Manage button successfully opened.")

		i.tearDown()

# iCLOUD DRIVE:
	@staticmethod
	def test_open_icloud_drive_icloud_settings():

		i.setUp()

		print("Opening iCloud Drive pane...")
		time.sleep(1)

		py.moveTo(679, 266)
		py.click()

		time.sleep(TIME_LIMIT)
		print("iCloud Drive pane successfully opened.")

		i.tearDown()

# iCLOUD MAIL:
	@staticmethod
	def test_open_icloud_mail_icloud_settings():

		i.setUp()

		print("Opening iCloud Mail pane...")
		time.sleep(1)

		py.moveTo(679, 309)
		py.click()

		time.sleep(TIME_LIMIT)
		print("iCloud Mail pane successfully opened.")

		i.tearDown()

# PRIVATE RELAY:
	@staticmethod
	def test_open_private_relay_icloud_settings():

		i.setUp()

		print("Opening Private Relay pane...")

		py.moveTo(679, 351)
		py.click()

		time.sleep(TIME_LIMIT)
		print("Private Relay pane successfully opened.")

		i.tearDown()				

# HIDE MY EMAIL:
	@staticmethod
	def test_open_hide_email_icloud_settings():

		i.setUp()

		print("Opening Hide my Email pane...")
		time.sleep(1)

		py.moveTo(679, 392)
		py.click()

		time.sleep(TIME_LIMIT)
		print("Hide my Email pane successfully opened.")

		i.tearDown()

# FIND MY MAC:
	@staticmethod
	def test_open_find_my_mac_icloud_settings():

		i.setUp()

		print("Opening Find My Mac pane...")
		time.sleep(1)

		py.moveTo(679, 437)
		py.click()

		time.sleep(TIME_LIMIT)
		print("Find My Mac pane successfully opened.")

		i.tearDown()


	@staticmethod
	def icloudTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning iCloud test suite...")

		print("===============================================================")
		print("===============================================================")

		i.test_open_manage_icloud_settings()

		print("===============================================================")

		i.test_open_icloud_drive_icloud_settings()

		print("===============================================================")

		i.test_open_icloud_mail_icloud_settings()

		print("===============================================================")

		i.test_open_private_relay_icloud_settings()

		print("===============================================================")

		i.test_open_hide_email_icloud_settings()

		print("===============================================================")

		i.test_open_find_my_mac_icloud_settings()

		print("===============================================================")
		print("===============================================================")

		print("iCloud test suite completed.")

		print("===============================================================")
		print("===============================================================")
		return			



# =====================================================================
# Tests:
i = iCloud()

