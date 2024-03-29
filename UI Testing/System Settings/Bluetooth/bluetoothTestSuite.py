import pyautogui as py
import time
import os

TIME_LIMIT = 10

class Bluetooth:

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

		py.write("Bluetooth")
		time.sleep(2)
		py.press('return')

		time.sleep(2)

		print("Test environmenmt successfully set up.")


	@staticmethod
	def tearDown():
		time.sleep(1)
		print("Tearing down test environment...")
		os.system("pkill -a 'System Settings'")


# DISABLE BLUETOOTH
	@staticmethod
	def test_turn_off_bluetooth_settings():

		i.setUp()

		time.sleep(1)
		print("Turning OFF Bluetooth...")

		py.moveTo(665, 93)
		py.click()

		time.sleep(2)
		print("Bluetooth successfully turned OFF.")

		i.tearDown()

# ENABLE BLUETOOTH
	@staticmethod
	def test_turn_on_bluetooth_settings():

		i.setUp()

		time.sleep(1)
		print("Turning ON Bluetooth...")

		py.moveTo(665, 93)
		py.click()

		time.sleep(2)
		print("Bluetooth successfully turned ON.")

		i.tearDown()



	@staticmethod
	def bluetoothTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning Bluetooth test suite...")

		print("===============================================================")
		print("===============================================================")

		i.test_turn_off_bluetooth_settings()

		print("===============================================================")

		i.test_turn_on_bluetooth_settings()

		print("===============================================================")
		print("===============================================================")

		print("Bluetooth test suite completed.")

		print("===============================================================")
		print("===============================================================")
		return	
				

# =====================================================================
# Tests:
i = Bluetooth()

