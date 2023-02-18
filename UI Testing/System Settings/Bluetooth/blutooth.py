import pyautogui as py
import time
import os

TIME_LIMIT = 10

class Blutooth:

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


	@staticmethod
	def test_turn_off_bluetooth_settings():
		time.sleep(1)
		print("Turning OFF WiFi...")

		py.moveTo(665, 93)
		py.click()

		time.sleep(2)
		print("WiFi successfully turned OFF.")


	@staticmethod
	def test_turn_on_bluetooth_settings():
		time.sleep(1)
		print("Turning ON WiFi...")

		py.moveTo(665, 93)
		py.click()

		time.sleep(2)
		print("WiFi successfully turned ON.")
				

# =====================================================================
# Tests:
i = Blutooth()

print("===============================================================")
print("===============================================================")

print("Beginning test suite...")

print("===============================================================")
print("===============================================================")

i.setUp()
i.test_turn_off_bluetooth_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_on_bluetooth_settings()
i.tearDown()

print("===============================================================")

print("===============================================================")
print("===============================================================")

print("Test suite completed.")

print("===============================================================")
print("===============================================================")



