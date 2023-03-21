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
		


# ABOUT
	@staticmethod
	def test_open_about_general_settings():

		i.setUp()

		print("Opening About pane...")
		time.sleep(2)

		py.moveTo(679, 94)
		py.click()

		time.sleep(4)
		print("About pane successfully opened.")

		i.tearDown()

# SOFTWARE UPDATE
	@staticmethod	
	def test_open_software_update_settings():

		i.setUp()

		print("Opening Software Update pane...")
		time.sleep(2)

		py.moveTo(679, 140)
		py.click()

		time.sleep(4)
		print("Software Update pane successfully opened.")

		i.tearDown()

# STORAGE
	@staticmethod
	def test_open_storage_settings():

		i.setUp()

		print("Opening Storage pane...")
		time.sleep(2)

		py.moveTo(679, 180)
		py.click()

		time.sleep(4)
		print("Storage pane successfully opened.")

		i.tearDown()

# AIRDROP & HANDOFF 
	@staticmethod
	def test_open_airDrop_and_handOff_settings():

		i.setUp()

		print("Opening AirDrop & Handoff pane...")
		time.sleep(2)

		py.moveTo(679, 223)
		py.click()

		time.sleep(4)
		print("AirDrop & Handoff pane successfully opened.")

		i.tearDown()

# LOGIN ITEMS
	@staticmethod
	def test_open_loginItems_settings():

		i.setUp()

		print("Opening Login Items pane...")
		time.sleep(2)

		py.moveTo(679, 271)
		py.click()

		time.sleep(4)
		print("Login Items pane successfully opened.")

		i.tearDown()

# LANGUAGE & REGION
	@staticmethod
	def test_open_language_and_region_settings():

		i.setUp()

		print("Opening Language & Region pane...")
		time.sleep(2)

		py.moveTo(679, 322)
		py.click()

		time.sleep(4)
		print("Language & Region pane successfully opened.")

		i.tearDown()

# DATE & TIME
	@staticmethod
	def test_open_date_and_time_settings():

		i.setUp()

		print("Opening Date & Time pane...")
		time.sleep(2)

		py.moveTo(679, 364)
		py.click()

		time.sleep(4)
		print("Date & Time pane successfully opened.")

		i.tearDown()

# SHARING
	@staticmethod
	def test_open_sharing_settings():

		i.setUp()

		print("Opening Sharing pane...")
		time.sleep(2)

		py.moveTo(679, 418)
		py.click()

		time.sleep(4)
		print("Sharing pane successfully opened.")

		i.tearDown()

# TIME MACHINE
	@staticmethod
	def test_open_time_machine_settings():

		i.setUp()

		print("Opening Time Machine pane...")
		time.sleep(2)

		py.moveTo(679, 460)
		py.click()

		time.sleep(4)
		print("Time Machine pane successfully opened.")

		i.tearDown()

# TRANSFER OR RESET
	@staticmethod
	def test_open_transfer_or_reset_settings():

		i.setUp()

		print("Opening Transfer or Reset pane...")
		time.sleep(2)

		py.moveTo(679, 497)
		py.click()

		time.sleep(3)

		py.moveTo(560, 216)
		py.click()

		time.sleep(3)

		py.moveTo(663, 510)
		py.click()

		time.sleep(4)
		print("Transfer or Reset pane successfully opened.")

		i.tearDown()

# STARTUP DISK
	@staticmethod
	def test_open_startUp_disk_settings():

		i.setUp()

		print("Opening Startup Disk pane...")
		time.sleep(2)

		py.moveTo(679, 545)
		py.click()

		time.sleep(4)
		print("Startup Disk pane successfully opened.")

		i.tearDown()



	@staticmethod
	def generalTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning General test suite...")

		print("===============================================================")
		print("===============================================================")

		i.test_open_about_general_settings()

		print("===============================================================")

		i.test_open_software_update_settings()

		print("===============================================================")

		i.test_open_storage_settings()

		print("===============================================================")

		i.test_open_airDrop_and_handOff_settings()

		print("===============================================================")

		i.test_open_loginItems_settings()

		print("===============================================================")

		i.test_open_language_and_region_settings()

		print("===============================================================")

		i.test_open_date_and_time_settings()

		print("===============================================================")

		i.test_open_sharing_settings()

		print("===============================================================")

		i.test_open_time_machine_settings()

		print("===============================================================")

		i.test_open_transfer_or_reset_settings()

		print("===============================================================")

		i.test_open_startUp_disk_settings()

		print("===============================================================")
		print("===============================================================")

		print("General test suite completed.")

		print("===============================================================")
		print("===============================================================")
		return					


# Tests:
# ======================================================================
i = General()

