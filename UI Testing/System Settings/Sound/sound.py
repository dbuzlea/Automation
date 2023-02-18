import pyautogui as py
import time
import os

TIME_LIMIT = 10

class Sound:

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

		py.write("Sound")
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
	def test_alert_sound_sound_settings():
		time.sleep(1)
		print("Selecting Alert Sound drop down menu...")

		py.moveTo(646, 124)
		py.click()

		time.sleep(2)
		print("Alert Sound drop down menu successfully opened.")


	@staticmethod
	def test_play_alert_sound_sound_settings():
		time.sleep(1)
		print("Playing current alert sound...")

		py.moveTo(674, 125)
		py.click()

		time.sleep(2)
		print("Alert Sound successfully played.")	


	@staticmethod
	def test_play_sound_effects_through_sound_settings():
		time.sleep(1)
		print("Selecting Play sound effects through drop down menu...")

		py.moveTo(673, 164)
		py.click()

		time.sleep(2)
		print("Play sound effects through drop down menu successfully opened.")


	@staticmethod
	def test_turn_OFF_sound_on_startup_sound_settings():
		time.sleep(1)
		print("Turning OFF Sound on startup...")

		py.moveTo(670, 244)
		py.click()

		time.sleep(2)
		print("Sound on startup successfully disabled.")


	@staticmethod
	def test_turn_ON_sound_on_startup_sound_settings():
		time.sleep(1)
		print("Turning ON Sound on startup...")

		py.moveTo(670, 244)
		py.click()

		time.sleep(2)
		print("Sound on startup successfully enabled.")


	@staticmethod
	def test_turn_OFF_ui_sound_effects_sound_settings():
		time.sleep(1)
		print("Turning OFF UI sound effects...")

		py.moveTo(670, 244)
		py.click()

		time.sleep(2)
		print("UI sound effects successfully disabled.")


	@staticmethod
	def test_turn_ON_ui_sound_effects_sound_settings():
		time.sleep(1)
		print("Turning ON UI sound effects...")

		py.moveTo(670, 244)
		py.click()

		time.sleep(2)
		print("UI sound effects successfully enabled.")

	
	@staticmethod
	def test_turn_ON_feedback_volume_is_changed_sound_settings():
		time.sleep(1)
		print("Turning ON feedback when volume is changed...")

		py.moveTo(670, 320)
		py.click()

		time.sleep(2)
		print("Feedback when volume is changed successfully enabled.")


	@staticmethod
	def test_turn_OFF_feedback_volume_is_changed_sound_settings():
		time.sleep(1)
		print("Turning OFF feedback when volume is changed...")

		py.moveTo(670, 320)
		py.click()

		time.sleep(2)
		print("Feedback when volume is changed successfully disabled.")	



# =====================================================================
# Tests:
i = Sound()

print("===============================================================")
print("===============================================================")

print("Beginning test suite...")

print("===============================================================")
print("===============================================================")

i.setUp()
i.test_alert_sound_sound_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_play_alert_sound_sound_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_play_sound_effects_through_sound_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_OFF_sound_on_startup_sound_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_ON_sound_on_startup_sound_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_OFF_ui_sound_effects_sound_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_ON_ui_sound_effects_sound_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_ON_feedback_volume_is_changed_sound_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_OFF_feedback_volume_is_changed_sound_settings()
i.tearDown()

print("===============================================================")

print("===============================================================")
print("===============================================================")

print("Test suite completed.")

print("===============================================================")
print("===============================================================")



