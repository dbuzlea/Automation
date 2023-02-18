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




	@staticmethod
	def test_open_manage_icloud_settings():
		print("Selecting Manage button...")
		time.sleep(1)

		py.moveTo(644, 96)
		py.click()

		time.sleep(TIME_LIMIT)
		print("Manage button successfully opened.")


	@staticmethod
	def test_open_icloud_drive_icloud_settings():
		print("Opening iCloud Drive pane...")
		time.sleep(1)

		py.moveTo(664, 264)
		py.click()

		time.sleep(TIME_LIMIT)
		print("iCloud Drive pane successfully opened.")


	@staticmethod
	def test_open_icloud_mail_icloud_settings():
		print("Opening iCloud Mail pane...")
		time.sleep(1)

		py.moveTo(447, 307)
		py.click()

		time.sleep(TIME_LIMIT)
		print("iCloud Mail pane successfully opened.")


	@staticmethod
	def test_open_private_relay_icloud_settings():
		print("Opening Private Relay pane...")

		py.moveTo(447, 347)
		py.click()

		time.sleep(TIME_LIMIT)
		print("Private Relay pane successfully opened.")				


	@staticmethod
	def test_open_hide_email_icloud_settings():
		print("Opening Hide my Email pane...")
		time.sleep(1)

		py.moveTo(447, 390)
		py.click()

		time.sleep(TIME_LIMIT)
		print("Hide my Email pane successfully opened.")


	@staticmethod
	def test_open_find_my_mac_icloud_settings():
		print("Opening Find My Mac pane...")
		time.sleep(1)

		py.moveTo(447, 437)
		py.click()

		time.sleep(TIME_LIMIT)
		print("Find My Mac pane successfully opened.")		



# =====================================================================
# Tests:
i = iCloud()

print("===============================================================")
print("===============================================================")

print("Beginning test suite...")

print("===============================================================")
print("===============================================================")

i.setUp()
i.test_open_manage_icloud_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_open_icloud_drive_icloud_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_open_icloud_mail_icloud_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_open_private_relay_icloud_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_open_hide_email_icloud_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_open_find_my_mac_icloud_settings()
i.tearDown()

print("===============================================================")
print("===============================================================")

print("Test suite completed.")

print("===============================================================")
print("===============================================================")



