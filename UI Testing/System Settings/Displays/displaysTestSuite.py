import pyautogui as py
import time
import os


TIME_LIMIT = 10

class Displays:
	

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

		py.write("Displays")
		time.sleep(2)
		py.press('return')

		time.sleep(2)

		print("Test environmenmt successfully set up.")


	@staticmethod
	def tearDown():
		time.sleep(1)
		print("Tearing down test environment...")
		os.system("pkill -a 'System Settings'")


# Automatically adjust brightness
	@staticmethod
	def test_toggle_automatic_brightness_adjust_displays_setting():
		time.sleep(1)
		print("Turning OFF automatic adjust brightness...")

		time.sleep(2)
		py.moveTo(669, 431)
		py.click()

		time.sleep(2)
		print("Automatic adjust brightness successfully disabled.")

		time.sleep(1)
		print("Turning ON automatic adjust brightness...")

		time.sleep(2)
		py.moveTo(669, 431)
		py.click()

		time.sleep(2)
		print("Automatic adjust brightness successfully enabled.")


# True Tone
	@staticmethod
	def test_toggle_true_tone_displays_setting():
		time.sleep(1)
		print("Turning OFF True Tone...")

		time.sleep(2)
		py.moveTo(669, 471)
		py.click()

		time.sleep(2)
		print("True Tone successfully disabled.")

		time.sleep(1)
		print("Turning ON True Tone...")

		time.sleep(2)
		py.moveTo(669, 471)
		py.click()

		time.sleep(2)
		print("True Tone successfully enabled.")


# Color Profile
	@staticmethod
	def test_select_color_profile_displays_setting():
		time.sleep(1)
		print("Opening color profile drop down menu...")

		time.sleep(2)
		py.moveTo(669, 550)
		py.click()

		time.sleep(2)
		print("Color profile drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing color profile drop down menu...")

		time.sleep(2)
		py.moveTo(669, 550)
		py.click()

		time.sleep(2)
		print("Color profile drop down menu successfully collapsed.")

# TODO: Failed Tests Below
# Advance
	@staticmethod	
	def test_open_advance_displays_setting():
		time.sleep(1)
		print("Opening Advance window...")

		time.sleep(2)
		py,moveTo(524, 605)
		py.click()

		time.sleep(2)
		print("Advance window successfully opened.")


# Close Advance window
	@staticmethod	
	def test_close_advance_displays_setting():
		time.sleep(1)
		print("Closing Advance window...")

		time.sleep(2)
		py,moveTo(541, 566)
		py.click()

		time.sleep(2)
		print("Advance window successfully closed.")	


# Allow pointer to move between any nearby Mac or iPad
	@staticmethod
	def test_toggle_allow_pointer_nearby_mac_or_ipad_displays_setting():
		time.sleep(1)
		print("Turning OFF allow pointer to move between nearby Mac or iPad...")

		time.sleep(2)
		py.moveTo(550, 141)
		py.click()

		time.sleep(2)
		print("Allow pointer to move between nearby Mac or iPad successfully disabled.")

		time.sleep(1)
		print("Turning ON allow pointer to move between nearby Mac or iPad...")

		time.sleep(2)
		py.moveTo(550, 141)
		py.click()

		time.sleep(2)
		print("Allow pointer to move between nearby Mac or iPad successfully enabled.")


# Push through the edge of a display to connect to a nearby Mac or iPad
	@staticmethod
	def test_toggle_push_through_edge_of_screen_displays_setting():
		time.sleep(1)
		print("Turning OFF push through edge of display to connect...")

		time.sleep(2)
		py.moveTo(550, 141)
		py.click()

		time.sleep(2)
		print("Push through edge of display to connect successfully disabled.")

		time.sleep(1)
		print("Turning ON push through edge of display to connect...")

		time.sleep(2)
		py.moveTo(550, 141)
		py.click()

		time.sleep(2)
		print("Push through edge of display to connect successfully enabled.")


	@staticmethod
	def displaysTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning Displays test suite...")

		print("===============================================================")
		print("===============================================================")

		i.setUp()
		i.test_toggle_automatic_brightness_adjust_displays_setting()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_toggle_true_tone_displays_setting()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_select_color_profile_displays_setting()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_advance_displays_setting()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_advance_displays_setting()
		i.test_toggle_allow_pointer_nearby_mac_or_ipad_displays_setting()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_advance_displays_setting()
		i.test_toggle_push_through_edge_of_screen_displays_setting()
		i.tearDown()

		print("===============================================================")

		print("===============================================================")
		print("===============================================================")

		print("Test suite completed.")

		print("===============================================================")
		print("===============================================================")
		return						






# =====================================================================
# Tests:
i = Displays()

# print("===============================================================")
# print("===============================================================")

# print("Beginning test suite...")

# print("===============================================================")
# print("===============================================================")

# i.setUp()
# i.test_toggle_automatic_brightness_adjust_displays_setting()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_toggle_true_tone_displays_setting()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_select_color_profile_displays_setting()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_advance_displays_setting()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_advance_displays_setting()
# i.test_toggle_allow_pointer_nearby_mac_or_ipad_displays_setting()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_advance_displays_setting()
# i.test_toggle_push_through_edge_of_screen_displays_setting()
# i.tearDown()

# print("===============================================================")

# print("===============================================================")
# print("===============================================================")

# print("Test suite completed.")

# print("===============================================================")
# print("===============================================================")



