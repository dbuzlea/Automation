import pyautogui as py
import time
import os


TIME_LIMIT = 10

class Siri:
	

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

		py.write("Siri")
		time.sleep(2)
		py.press('return')

		time.sleep(2)

		print("Test environmenmt successfully set up.")


	@staticmethod
	def tearDown():
		time.sleep(1)
		print("Tearing down test environment...")
		os.system("pkill -a 'System Settings'")


# Ask Siri
	@staticmethod
	def test_toggle_ask_siri_settings():
		time.sleep(1)
		print("Turning OFF Ask Siri...")

		time.sleep(2)
		py.moveTo(670, 95)
		py.click()

		time.sleep(2)
		print("Ask Siri successfully disabled.")

		time.sleep(1)
		print("Selecting cancel...")

		time.sleep(2)
		py.moveTo(299, 425)
		py.click()

		time.sleep(2)
		print("Cancel successfully selected.")


# Hey Siri
	@staticmethod
	def test_toggle_hey_siri_settings():
		time.sleep(1)
		print("Turning ON Hey Siri...")

		time.sleep(2)
		py.moveTo(670, 171)
		py.click()

		time.sleep(2)
		print("Hey Siri successfully enabled.")

		time.sleep(1)
		print("Selecting cancel...")

		time.sleep(2)
		py.moveTo(481, 562)
		py.click()

		time.sleep(2)
		print("Cancel successfully selected.")


# Keyboard shortcut
	@staticmethod
	def test_open_keyboard_shortcut_siri_settings():
		time.sleep(1)
		print("Opening keyboard shortcut drop down menu...")

		time.sleep(2)
		py.moveTo(671, 210)
		py.click()

		time.sleep(2)
		print("Keyboard shortcut drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing keyboard shortcut drop down menu...")

		time.sleep(2)
		py.moveTo(671, 210)
		py.click()

		time.sleep(2)
		print("Keyboard shortcut drop down menu successfully collapsed.")


# Language
	@staticmethod
	def test_open_language_siri_settings():
		time.sleep(1)
		print("Opening language drop down menu...")

		time.sleep(2)
		py.moveTo(671, 251)
		py.click()

		time.sleep(2)
		print("Language drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing language drop down menu...")

		time.sleep(2)
		py.moveTo(671, 251)
		py.click()

		time.sleep(2)
		print("Language drop down menu successfully collapsed.")


# Siri voice
	@staticmethod
	def test_select_siri_voice_siri_settings():
		time.sleep(1)
		print("Selecting Siri voice...")

		time.sleep(2)
		py.moveTo(652, 289)
		py.click()

		time.sleep(2)
		print("Siri voice successfully selected.")

		time.sleep(1)
		print("Selecting cancel...")

		time.sleep(2)
		py.moveTo(468, 439)
		py.click()

		time.sleep(2)
		print("Cancel successfully selected.")


# Siri history
	@staticmethod
	def test_delete_siri_history_siri_settings():
		time.sleep(1)
		print("Selecting delete Siri history...")

		time.sleep(2)
		py.moveTo(652, 329)
		py.click()

		time.sleep(2)
		print("Delete Siri history successfully selected.")

		time.sleep(1)
		print("Selecting cancel...")

		time.sleep(2)
		py.moveTo(300, 418)
		py.click()

		time.sleep(2)
		print("Cancel successfully selected.")






# =====================================================================
# Tests:
i = Siri()

print("===============================================================")
print("===============================================================")

print("Beginning test suite...")

print("===============================================================")
print("===============================================================")

i.setUp()
i.test_toggle_ask_siri_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_toggle_hey_siri_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_open_keyboard_shortcut_siri_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_open_language_siri_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_select_siri_voice_siri_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_delete_siri_history_siri_settings()
i.tearDown()

print("===============================================================")
print("===============================================================")

print("Test suite completed.")

print("===============================================================")
print("===============================================================")



