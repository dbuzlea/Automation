import pyautogui as py
import time
import os

TIME_LIMIT = 10

class WiFi:

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

		py.write("WiFi")
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
	def test_turn_off_wifi_settings():
		time.sleep(1)
		print("Turning OFF WiFi...")

		py.moveTo(665, 93)
		py.click()

		time.sleep(2)
		print("WiFi successfully turned OFF.")


	@staticmethod
	def test_turn_on_wifi_settings():
		time.sleep(1)
		print("Turning ON WiFi...")

		py.moveTo(665, 93)
		py.click()

		time.sleep(2)
		print("WiFi successfully turned ON.")


	@staticmethod
	def test_open_details_wifi_settings():
		time.sleep(1)
		print("Selecting WiFi details button...")

		py.moveTo(650, 143)
		py.click()

		time.sleep(2)
		print("WiFi details window successfully opened.")				

# =====================================================================
# Tests:
i = WiFi()

print("===============================================================")
print("===============================================================")

print("Beginning test suite...")

print("===============================================================")
print("===============================================================")

i.setUp()
i.test_turn_off_wifi_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_on_wifi_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_open_details_wifi_settings()
i.tearDown()

print("===============================================================")



print("===============================================================")
print("===============================================================")

print("Test suite completed.")

print("===============================================================")
print("===============================================================")



