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


	@staticmethod
	def test_change_low_power_mode_battery_settings():
		time.sleep(1)
		print("Selecting Low Power Mode drop down menu...")

		py.moveTo(674, 92)
		py.click()

		time.sleep(3)
		print("Low Power Mode drop down menu successfully opened.")


	@staticmethod
	def test_open_battery_health_options_battery_settings():
		time.sleep(1)
		print("Selecting Battery Health options...")

		py.moveTo(674, 173)
		py.click()

		time.sleep(3)
		print("Battery Health window successfully opened.")	


	@staticmethod
	def test_open_options_battery_settings():
		time.sleep(1)
		print("Selecting Battery options button...")

		py.scroll(10)

		time.sleep(2)

		py.moveTo(628, 616)
		py.click()

		time.sleep(3)
		print("Battery options window successfully opened.")

	@staticmethod	
	def batteryTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning Battery test suite...")

		print("===============================================================")
		print("===============================================================")

		i.setUp()
		i.test_change_low_power_mode_battery_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_battery_health_options_battery_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_options_battery_settings()
		i.tearDown()

		print("===============================================================")
		print("===============================================================")

		print("Test suite completed.")

		print("===============================================================")
		print("===============================================================")
		return			

# =====================================================================
# Tests:
i = Battery()



# def runBatteryTest():
# 	print("===============================================================")
# 	print("===============================================================")

# 	print("Beginning test suite...")

# 	print("===============================================================")
# 	print("===============================================================")

# 	i.setUp()
# 	i.test_change_low_power_mode_battery_settings()
# 	i.tearDown()

# 	print("===============================================================")

# 	i.setUp()
# 	i.test_open_battery_health_options_battery_settings()
# 	i.tearDown()

# 	print("===============================================================")

# 	i.setUp()
# 	i.test_open_options_battery_settings()
# 	i.tearDown()

# 	print("===============================================================")
# 	print("===============================================================")

# 	print("Test suite completed.")

# 	print("===============================================================")
# 	print("===============================================================")
# 	return



