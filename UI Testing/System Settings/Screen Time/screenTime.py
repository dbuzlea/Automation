import pyautogui as py
import time
import os

TIME_LIMIT = 10

class ScreenTime:

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

		py.write("Screen Time")
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
	def test_toggle_screen_time_settings():
		time.sleep(1)
		print("Turning OFF ScreenTime...")

		py.moveTo(665, 94)
		py.click()

		time.sleep(2)
		# turnOFFButton
		py.moveTo(418, 425)
		py.click()

		time.sleep(2)
		print("ScreenTime successfully disabled.")

		time.sleep(1)
		print("Turning ON ScreenTime...")

		py.moveTo(665, 94)
		py.click()

		time.sleep(2)
		print("ScreenTime successfully enabled.")


	@staticmethod
	def test_open_app_usage_screen_time_settings():
		time.sleep(2)
		print("Opening App Usage...")

		py.moveTo(680, 153)
		py.click()

		time.sleep(2)
		print("App Usage successfully opened.")


	@staticmethod
	def test_select_device_app_usage_screen_time_settings():
		time.sleep(2)
		print("Opening Device drop down menu...")

		py.moveTo(674, 92)
		py.click()

		time.sleep(2)
		print("Device drop down menu successfully opened.")


	@staticmethod
	def test_open_notifications_screen_time_settings():
		time.sleep(2)
		print("Opening Notifications...")

		py.moveTo(680, 197)
		py.click()

		time.sleep(2)
		print("Notifications successfully opened.")


	@staticmethod
	def test_select_device_notifications_screen_time_settings():
		time.sleep(2)
		print("Opening Device drop down menu...")

		py.moveTo(674, 92)
		py.click()

		time.sleep(2)
		print("Device drop down menu successfully opened.")


	@staticmethod
	def test_open_pickUps_screen_time_settings():
		time.sleep(2)
		print("Opening Pickups...")

		py.moveTo(680, 242)
		py.click()

		time.sleep(2)
		print("Pickups successfully opened.")


	@staticmethod
	def test_select_device_pickUps_screen_time_settings():
		time.sleep(2)
		print("Opening Device drop down menu...")

		py.moveTo(674, 92)
		py.click()

		time.sleep(2)
		print("Device drop down menu successfully opened.")


	@staticmethod
	def test_open_downTime_screen_time_settings():
		time.sleep(2)
		print("Opening Downtime...")

		py.moveTo(680, 297)
		py.click()

		time.sleep(2)
		print("Downtime successfully opened.")

		#  TODO: 
	@staticmethod
	def test_toggle_downTime_screen_time_settings():
		time.sleep(2)
		print("Turning ON Downtime...")

		py.moveTo(428, 586)  # TODO
		py.click()

		time.sleep(2)
		print("Downtime successfully enabled.")

		time.sleep(2)
		print("Turning OFF Downtime...")

		py.moveTo(405, 586) # TODO
		py.click()

		time.sleep(2)
		print("Downtime successfully disabled.")

		# TODO:
	@staticmethod
	def test_select_schedule_downTime_screen_time_settings():
		time.sleep(2)
		print("Selecting Schedule drop down menu...")

		py.moveTo(405, 586) # TODO
		py.click()

		time.sleep(2)
		print("Schedule drop down menu successfully opened.")								




# =====================================================================
# Tests:
i = ScreenTime()

print("===============================================================")
print("===============================================================")

print("Beginning test suite...")

print("===============================================================")
print("===============================================================")

i.setUp()
i.test_toggle_screen_time_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_open_app_usage_screen_time_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_open_app_usage_screen_time_settings()
i.test_select_device_app_usage_screen_time_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_open_notifications_screen_time_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_open_notifications_screen_time_settings()
i.test_select_device_notifications_screen_time_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_open_pickUps_screen_time_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_open_pickUps_screen_time_settings()
i.test_select_device_pickUps_screen_time_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_open_downTime_screen_time_settings()
i.tearDown()

print("===============================================================")

# i.setUp()
# i.test_open_downTime_screen_time_settings()
# i.test_toggle_downTime_screen_time_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_downTime_screen_time_settings()
# i.test_select_schedule_downTime_screen_time_settings()
# i.tearDown()



print("===============================================================")

print("===============================================================")
print("===============================================================")
print("===============================================================")

print("Test suite completed.")

print("===============================================================")
print("===============================================================")



