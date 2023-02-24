import pyautogui as py
import time
import os

class General:

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

		py.write("General")

		time.sleep(2)
		py.press('return')
		print("Test environmenmt successfully set up.")


	@staticmethod
	def tearDown():
		time.sleep(1)
		print("Tearing down test environment...")
		os.system("pkill -a 'System Settings'")	
		



	@staticmethod
	def test_open_about_general_settings():
		print("Opening About pane...")
		time.sleep(2)

		py.moveTo(278, 8)
		py.click()

		time.sleep(2)

		py.moveTo(296, 39)
		py.click()

		time.sleep(4)
		print("About pane successfully opened.")


	@staticmethod	
	def test_open_software_update_settings():
		print("Opening Software Update pane...")
		time.sleep(2)

		py.moveTo(278, 8)
		py.click()

		time.sleep(2)

		py.moveTo(273, 720)
		py.click()

		time.sleep(4)
		print("Software Update pane successfully opened.")


	@staticmethod
	def test_open_storage_settings():
		print("Opening Storage pane...")
		time.sleep(2)

		py.moveTo(278, 8)
		py.click()

		time.sleep(2)

		py.moveTo(276, 789)
		py.click()

		time.sleep(4)
		print("Storage pane successfully opened.")


	@staticmethod
	def test_open_airDrop_and_handOff_settings():
		print("Opening AirDrop & Handoff pane...")
		time.sleep(2)

		py.moveTo(278, 8)
		py.click()

		time.sleep(2)

		py.moveTo(273, 82)
		py.click()

		time.sleep(4)
		print("AirDrop & Handoff pane successfully opened.")


	@staticmethod
	def test_open_loginItems_settings():
		print("Opening Login Items pane...")
		time.sleep(2)

		py.moveTo(278, 8)
		py.click()

		time.sleep(2)

		py.moveTo(273, 456)
		py.click()

		time.sleep(4)
		print("Login Items pane successfully opened.")


	@staticmethod
	def test_open_language_and_region_settings():
		print("Opening Language & Region pane...")
		time.sleep(2)

		py.moveTo(278, 8)
		py.click()

		time.sleep(2)

		py.moveTo(273, 413)
		py.click()

		time.sleep(4)
		print("Language & Region pane successfully opened.")


	@staticmethod
	def test_open_date_and_time_settings():
		print("Opening Date & Time pane...")
		time.sleep(2)

		py.moveTo(278, 8)
		py.click()

		py.moveTo(273, 215)
		py.click()

		time.sleep(4)
		print("Date & Time pane successfully opened.")


	@staticmethod
	def test_open_sharing_settings():
		print("Opening Sharing pane...")
		time.sleep(2)

		py.moveTo(278, 8)
		py.click()

		py.moveTo(273, 676)
		py.click()

		time.sleep(4)
		print("Sharing pane successfully opened.")


	@staticmethod
	def test_open_time_machine_settings():
		print("Opening Time Machine pane...")
		time.sleep(2)

		py.moveTo(278, 8)
		py.click()

		py.moveTo(273, 809)
		py.click()

		time.sleep(4)
		print("Time Machine pane successfully opened.")


	@staticmethod
	def test_open_transfer_or_reset_settings():
		print("Opening Transfer or Reset pane...")
		time.sleep(2)

		py.moveTo(278, 8)
		py.click()

		py.moveTo(360, 834)
		time.sleep(3)

		py.moveTo(273, 711)
		py.click()

		time.sleep(4)
		print("Transfer or Reset pane successfully opened.")


	@staticmethod
	def test_open_startUp_disk_settings():
		print("Opening Startup Disk pane...")
		time.sleep(2)

		py.moveTo(278, 8)
		py.click()

		py.moveTo(273, 765)
		py.click()

		time.sleep(4)
		print("Startup Disk pane successfully opened.")


	@staticmethod
	def generalTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning General test suite...")

		print("===============================================================")
		print("===============================================================")

		m.setUp()
		m.test_open_about_general_settings()
		m.tearDown()

		print("===============================================================")

		m.setUp()
		m.test_open_software_update_settings()
		m.tearDown()

		print("===============================================================")

		m.setUp()
		m.test_open_storage_settings()
		m.tearDown()

		print("===============================================================")

		m.setUp()
		m.test_open_airDrop_and_handOff_settings()
		m.tearDown()

		print("===============================================================")

		m.setUp()
		m.test_open_loginItems_settings()
		m.tearDown()

		print("===============================================================")

		m.setUp()
		m.test_open_language_and_region_settings()
		m.tearDown()

		print("===============================================================")

		m.setUp()
		m.test_open_date_and_time_settings()
		m.tearDown()

		print("===============================================================")

		m.setUp()
		m.test_open_sharing_settings()
		m.tearDown()

		print("===============================================================")

		m.setUp()
		m.test_open_time_machine_settings()
		m.tearDown()

		print("===============================================================")

		m.setUp()
		m.test_open_transfer_or_reset_settings()
		m.tearDown()

		print("===============================================================")

		m.setUp()
		m.test_open_startUp_disk_settings()
		m.tearDown()

		print("===============================================================")
		print("===============================================================")

		print("Test suite completed.")

		print("===============================================================")
		print("===============================================================")
		return					


# Tests:
# ======================================================================
m = General()

# print("===============================================================")
# print("===============================================================")

# print("Beginning test suite...")

# print("===============================================================")
# print("===============================================================")

# m.setUp()
# m.test_open_about_general_settings()
# m.tearDown()

# print("===============================================================")

# m.setUp()
# m.test_open_software_update_settings()
# m.tearDown()

# print("===============================================================")

# m.setUp()
# m.test_open_storage_settings()
# m.tearDown()

# print("===============================================================")

# m.setUp()
# m.test_open_airDrop_and_handOff_settings()
# m.tearDown()

# print("===============================================================")

# m.setUp()
# m.test_open_loginItems_settings()
# m.tearDown()

# print("===============================================================")

# m.setUp()
# m.test_open_language_and_region_settings()
# m.tearDown()

# print("===============================================================")

# m.setUp()
# m.test_open_date_and_time_settings()
# m.tearDown()

# print("===============================================================")

# m.setUp()
# m.test_open_sharing_settings()
# m.tearDown()

# print("===============================================================")

# m.setUp()
# m.test_open_time_machine_settings()
# m.tearDown()

# print("===============================================================")

# m.setUp()
# m.test_open_transfer_or_reset_settings()
# m.tearDown()

# print("===============================================================")

# m.setUp()
# m.test_open_startUp_disk_settings()
# m.tearDown()

# print("===============================================================")
# print("===============================================================")

# print("Test suite completed.")

# print("===============================================================")
# print("===============================================================")



