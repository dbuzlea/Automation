import pyautogui as py
import time
import os


TIME_LIMIT = 10

class LockScreen:
	

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

		py.write("Lock Screen")
		time.sleep(2)
		py.press('return')

		time.sleep(2)

		print("Test environmenmt successfully set up.")


	@staticmethod
	def tearDown():
		time.sleep(1)
		print("Tearing down test environment...")
		os.system("pkill -a 'System Settings'")


# Start Screen Saver when inactive
	@staticmethod
	def test_select_start_screen_saver_when_inactive_screen_saver_setting():
		time.sleep(1)
		print("Opening start screen saver when inactive drop down menu...")

		time.sleep(2)
		py.moveTo(671, 93)
		py.click()

		time.sleep(2)
		print("Start screen saver when inactive drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing start screen saver when inactive drop down menu...")

		time.sleep(2)
		py.moveTo(671, 93)
		py.click()

		time.sleep(2)
		print("Start screen saver when inactive drop down menu successfully collapsed.")



# Turn off display on battery when inactive
	@staticmethod
	def test_select_turn_off_display_battery_inactive_screen_saver_setting():
		time.sleep(1)
		print("Opening turn display off on battery when inactive drop down menu...")

		time.sleep(2)
		py.moveTo(671, 148)
		py.click()

		time.sleep(2)
		print("Turn display off on battery when inactive drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing turn display off on battery when inactive drop down menu...")

		time.sleep(2)
		py.moveTo(671, 148)
		py.click()

		time.sleep(2)
		print("Turn display off on battery when inactive drop down menu successfully collapsed.")


# Turn off display on power adapter when inactive
	@staticmethod
	def test_select_turn_off_display_power_adapter_inactive_screen_saver_setting():
		time.sleep(1)
		print("Opening turn display off on power adapter when inactive drop down menu...")

		time.sleep(2)
		py.moveTo(671, 187)
		py.click()

		time.sleep(2)
		print("Turn display off on power adapter when inactive drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing turn display off on power adapter when inactive drop down menu...")

		time.sleep(2)
		py.moveTo(671, 187)
		py.click()

		time.sleep(2)
		print("Turn display off on power adapter when inactive drop down menu successfully collapsed.")



# Require password after screen saver begins
	@staticmethod
	def test_select_require_password_after_screen_saver_screen_saver_setting():
		time.sleep(1)
		print("Opening require password after screen saver begins drop down menu...")

		time.sleep(2)
		py.moveTo(671, 222)
		py.click()

		time.sleep(2)
		print("Require password after screen saver begins drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing require password after screen saver begins drop down menu...")

		time.sleep(2)
		py.moveTo(671, 222)
		py.click()

		time.sleep(2)
		print("Require password after screen saver begins drop down menu successfully collapsed.")


# Show message when locked
	@staticmethod
	def test_toggle_show_message_when_locked_screen_saver_settings():
		time.sleep(1)
		print("Turning ON show message when locked...")

		time.sleep(2)
		py.moveTo(613, 290)
		py.click()

		time.sleep(2)
		print("Show message when locked successfully enabled.")

		time.sleep(1)
		print("Turning OFF show message when locked...")

		time.sleep(2)
		py.moveTo(613, 290)
		py.click()

		time.sleep(2)
		print("Show message when locked successfully disabled.")



# Show the Sleep, Restart, and Shut Down buttons
	@staticmethod
	def test_toggle_show_sleep_restart_shutdown_buttons_screen_saver_settings():
		time.sleep(1)
		print("Turning OFF show the Sleep, Restart, and Shut Down buttons...")

		time.sleep(2)
		py.moveTo(671, 426)
		py.click()

		time.sleep(2)
		print("Show the Sleep, Restart, and Shut Down buttons successfully disabled.")

		time.sleep(1)
		print("Turning ON show the Sleep, Restart, and Shut Down buttons...")

		time.sleep(2)
		py.moveTo(671, 426)
		py.click()

		time.sleep(2)
		print("Show the Sleep, Restart, and Shut Down buttons successfully enabled.")



# Show password hints
	@staticmethod
	def test_toggle_show_password_hints_screen_saver_settings():
		time.sleep(1)
		print("Turning ON show password hints...")

		time.sleep(2)
		py.moveTo(671, 464)
		py.click()

		time.sleep(2)
		print("Show password hints successfully enabled.")

		time.sleep(1)
		print("Turning OFF show password hints...")

		time.sleep(2)
		py.moveTo(671, 464)
		py.click()

		time.sleep(2)
		print("Show password hints successfully disabled.")						





# =====================================================================
# Tests:
i = LockScreen()

print("===============================================================")
print("===============================================================")

print("Beginning test suite...")

print("===============================================================")
print("===============================================================")

i.setUp()
i.test_select_start_screen_saver_when_inactive_screen_saver_setting()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_select_turn_off_display_battery_inactive_screen_saver_setting()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_select_turn_off_display_power_adapter_inactive_screen_saver_setting()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_select_require_password_after_screen_saver_screen_saver_setting()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_toggle_show_message_when_locked_screen_saver_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_toggle_show_sleep_restart_shutdown_buttons_screen_saver_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_toggle_show_password_hints_screen_saver_settings()
i.tearDown()

print("===============================================================")

print("===============================================================")
print("===============================================================")

print("Test suite completed.")

print("===============================================================")
print("===============================================================")



