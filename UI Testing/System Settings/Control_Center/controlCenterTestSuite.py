import pyautogui as py
import time
import os


TIME_LIMIT = 10

class ControlCenter:
	

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

		py.write("Control Center")
		time.sleep(2)
		py.press('return')

		time.sleep(2)

		print("Test environmenmt successfully set up.")


	@staticmethod
	def tearDown():
		time.sleep(1)
		print("Tearing down test environment...")
		os.system("pkill -a 'System Settings'")


# WiFi
	@staticmethod
	def test_open_wifi_control_center_settings():
		time.sleep(1)
		print("Opening wifi drop down menu...")

		time.sleep(2)
		py.moveTo(671, 157)
		py.click()

		time.sleep(2)
		print("WiFi drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing wifi drop down menu...")

		time.sleep(2)
		py.moveTo(671, 157)
		py.click()

		time.sleep(2)
		print("WiFi drop down menu successfully collapsed.")

# Blutooth
	@staticmethod
	def test_open_bluetooth_control_center_settings():
		time.sleep(1)
		print("Opening blutooth drop down menu...")

		time.sleep(2)
		py.moveTo(671, 199)
		py.click()

		time.sleep(2)
		print("Bluetooth drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing bluetooth drop down menu...")

		time.sleep(2)
		py.moveTo(671, 199)
		py.click()

		time.sleep(2)
		print("Bluetooth drop down menu successfully collapsed.")


# AirDrop
	@staticmethod
	def test_open_AirDrop_control_center_settings():
		time.sleep(1)
		print("Opening AirDrop drop down menu...")

		time.sleep(2)
		py.moveTo(671, 242)
		py.click()

		time.sleep(2)
		print("AirDrop drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing AirDrop drop down menu...")

		time.sleep(2)
		py.moveTo(671, 242)
		py.click()

		time.sleep(2)
		print("AirDrop drop down menu successfully collapsed.")


# Focus
	@staticmethod
	def test_open_focus_control_center_settings():
		time.sleep(1)
		print("Opening Focus drop down menu...")

		time.sleep(2)
		py.moveTo(671, 287)
		py.click()

		time.sleep(2)
		print("Focus drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing Focus drop down menu...")

		time.sleep(2)
		py.moveTo(671, 287)
		py.click()

		time.sleep(2)
		print("Focus drop down menu successfully collapsed.")


# Stage Manager
	@staticmethod
	def test_open_stage_manager_control_center_settings():
		time.sleep(1)
		print("Opening Stage Manager drop down menu...")

		time.sleep(2)
		py.moveTo(671, 330)
		py.click()

		time.sleep(2)
		print("Stage Manager drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing Stage Manager drop down menu...")

		time.sleep(2)
		py.moveTo(671, 330)
		py.click()

		time.sleep(2)
		print("Stage Manager drop down menu successfully collapsed.")


# Screen Mirroring
	@staticmethod
	def test_open_screen_mirroring_control_center_settings():
		time.sleep(1)
		print("Opening screen mirroring drop down menu...")

		time.sleep(2)
		py.moveTo(671, 371)
		py.click()

		time.sleep(2)
		print("Screen mirroring drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing screen mirroring drop down menu...")

		time.sleep(2)
		py.moveTo(671, 371)
		py.click()

		time.sleep(2)
		print("Screen mirroring drop down menu successfully collapsed.")


# Display
	@staticmethod
	def test_open_display_control_center_settings():
		time.sleep(1)
		print("Opening display drop down menu...")

		time.sleep(2)
		py.moveTo(671, 415)
		py.click()

		time.sleep(2)
		print("Display drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing display drop down menu...")

		time.sleep(2)
		py.moveTo(671, 415)
		py.click()

		time.sleep(2)
		print("Display drop down menu successfully collapsed.")


# Sound
	@staticmethod
	def test_open_sound_control_center_settings():
		time.sleep(1)
		print("Opening sound drop down menu...")

		time.sleep(2)
		py.moveTo(671, 456)
		py.click()

		time.sleep(2)
		print("Sound drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing sound drop down menu...")

		time.sleep(2)
		py.moveTo(671, 456)
		py.click()

		time.sleep(2)
		print("Sound drop down menu successfully collapsed.")


# Now Playing
	@staticmethod
	def test_open_now_playing_control_center_settings():
		time.sleep(1)
		print("Opening Now Playing drop down menu...")

		time.sleep(2)
		py.moveTo(671, 500)
		py.click()

		time.sleep(2)
		print("Now Playing drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing Now Playing drop down menu...")

		time.sleep(2)
		py.moveTo(671, 500)
		py.click()

		time.sleep(2)
		print("Now Playing drop down menu successfully collapsed.")


	@staticmethod
	def controlCenterTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning Control Center test suite...")

		print("===============================================================")
		print("===============================================================")

		i.setUp()
		i.test_open_wifi_control_center_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_bluetooth_control_center_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_AirDrop_control_center_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_focus_control_center_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_stage_manager_control_center_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_screen_mirroring_control_center_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_display_control_center_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_sound_control_center_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_now_playing_control_center_settings()
		i.tearDown()

		print("===============================================================")
		print("===============================================================")

		print("Test suite completed.")

		print("===============================================================")
		print("===============================================================")
		return	






# =====================================================================
# Tests:
i = ControlCenter()

# print("===============================================================")
# print("===============================================================")

# print("Beginning test suite...")

# print("===============================================================")
# print("===============================================================")

# i.setUp()
# i.test_open_wifi_control_center_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_bluetooth_control_center_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_AirDrop_control_center_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_focus_control_center_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_stage_manager_control_center_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_screen_mirroring_control_center_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_display_control_center_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_sound_control_center_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_now_playing_control_center_settings()
# i.tearDown()

# print("===============================================================")
# print("===============================================================")

# print("Test suite completed.")

# print("===============================================================")
# print("===============================================================")



