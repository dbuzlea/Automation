import pyautogui as py
import time
import os

TIME_LIMIT = 10

class Battery:

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

		py.write("Battery")
		time.sleep(2)
		py.press('return')

		time.sleep(2)

		print("Test environmenmt successfully set up.")


	@staticmethod
	def tearDown():
		time.sleep(1)
		print("Tearing down test environment...")
		os.system("pkill -a 'System Settings'")


# LOW POWER MODE:
	@staticmethod
	def test_change_low_power_mode_battery_settings():

		i.setUp()

		time.sleep(1)
		print("Selecting Low Power Mode drop down menu...")

		py.moveTo(674, 92)
		py.click()

		time.sleep(3)
		print("Low Power Mode drop down menu successfully opened.")

		i.tearDown()

# BATTERY HEALTH:
	@staticmethod
	def test_open_battery_health_options_battery_settings():

		i.setUp()

		time.sleep(1)
		print("Selecting Battery Health options...")

		py.moveTo(674, 173)
		py.click()

		time.sleep(3)
		print("Battery Health window successfully opened.")

		i.tearDown()	

# OPTIONS:
	@staticmethod
	def test_open_options_battery_settings():

		i.setUp()

		time.sleep(1)
		print("Selecting Battery options button...")
		# TODO: fix scroll
		py.scroll(10)

		time.sleep(2)

		py.moveTo(628, 616)
		py.click()

		time.sleep(3)
		print("Battery options window successfully opened.")

		i.tearDown()



	@staticmethod	
	def batteryTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning Battery test suite...")

		print("===============================================================")
		print("===============================================================")

		i.test_change_low_power_mode_battery_settings()

		print("===============================================================")

		i.test_open_battery_health_options_battery_settings()

		print("===============================================================")

		i.test_open_options_battery_settings()

		print("===============================================================")
		print("===============================================================")

		print("Battery test suite completed.")

		print("===============================================================")
		print("===============================================================")
		return			

# =====================================================================
# Tests:
i = Battery()

