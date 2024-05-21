import pyautogui as py
import time
import os


TIME_LIMIT = 10

class Privacy:
	

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

		py.write("Privacy & Security")
		time.sleep(2)
		py.press('return')

		time.sleep(2)

		print("Test environmenmt successfully set up.")


	@staticmethod
	def tearDown():
		time.sleep(1)
		print("Tearing down test environment...")
		os.system("pkill -a 'System Settings'")


# Location Services
	@staticmethod
	def test_open_location_services_privacy_settings():

		i.setUp()

		time.sleep(1)
		print("Opening location services tab...")

		time.sleep(2)
		py.moveTo(679, 126)
		py.click()

		time.sleep(2)
		print("Location services tab successfully opened.")


	@staticmethod
	def test_location_services_privacy_settings():

		i.test_open_location_services_privacy_settings()

		time.sleep(1)
		print("Turning OFF location services...")

		time.sleep(2)
		py.moveTo(670, 94)
		py.click()

		time.sleep(2)
		print("Location services successfully disabled.")

		time.sleep(1)
		print("Selecting cancel...")

		# Selecting TouchID window to foreground
		time.sleep(2)
		py.moveTo(663, 198)
		py.click()

		time.sleep(2)
		py.moveTo(355, 457)
		py.click()

		time.sleep(2)
		print("Cancel successfully selected.")


		# AppleConnect
		time.sleep(1)
		print("Turning OFF AppleConnect...")

		time.sleep(2)
		py.moveTo(670, 151)
		py.click()

		time.sleep(2)
		print("AppleConnect successfully disabled.")

		time.sleep(1)
		print("Selecting cancel...")

		# Selecting TouchID window to foreground
		time.sleep(2)
		py.moveTo(663, 198)
		py.click()

		time.sleep(2)
		py.moveTo(355, 457)
		py.click()

		time.sleep(2)
		print("Cancel successfully selected.")


		# AppleConnectAgent
		time.sleep(1)
		print("Turning OFF AppleConnectAgent...")

		time.sleep(2)
		py.moveTo(670, 195)
		py.click()

		time.sleep(2)
		print("AppleConnectAgent successfully disabled.")

		time.sleep(1)
		print("Selecting cancel...")

		# Selecting TouchID window to foreground
		time.sleep(2)
		py.moveTo(663, 198)
		py.click()

		time.sleep(2)
		py.moveTo(355, 457)
		py.click()

		time.sleep(2)
		print("Cancel successfully selected.")


		# Calendar
		time.sleep(1)
		print("Turning OFF Calendar...")

		time.sleep(2)
		py.moveTo(670, 237)
		py.click()

		time.sleep(2)
		print("Calendar successfully disabled.")

		time.sleep(1)
		print("Selecting cancel...")

		# Selecting TouchID window to foreground
		time.sleep(2)
		py.moveTo(663, 198)
		py.click()

		time.sleep(2)
		py.moveTo(355, 457)
		py.click()

		time.sleep(2)
		print("Cancel successfully selected.")


		# Discord
		time.sleep(1)
		print("Turning OFF Discord...")

		time.sleep(2)
		py.moveTo(670, 281)
		py.click()

		time.sleep(2)
		print("Discord successfully disabled.")

		time.sleep(1)
		print("Selecting cancel...")

		# Selecting TouchID window to foreground
		time.sleep(2)
		py.moveTo(663, 198)
		py.click()

		time.sleep(2)
		py.moveTo(355, 457)
		py.click()

		time.sleep(2)
		print("Cancel successfully selected.")


		# Find My
		time.sleep(1)
		print("Turning OFF Find My...")

		time.sleep(2)
		py.moveTo(670, 323)
		py.click()

		time.sleep(2)
		print("Find My successfully disabled.")

		time.sleep(1)
		print("Selecting cancel...")

		# Selecting TouchID window to foreground
		time.sleep(2)
		py.moveTo(663, 198)
		py.click()

		time.sleep(2)
		py.moveTo(355, 457)
		py.click()

		time.sleep(2)
		print("Cancel successfully selected.")


		# GitHub Desktop
		time.sleep(1)
		print("Turning ON GitHub Desktop...")

		time.sleep(2)
		py.moveTo(670, 365)
		py.click()

		time.sleep(2)
		print("GitHub Desktop successfully enabled.")

		time.sleep(1)
		print("Selecting cancel...")

		# Selecting TouchID window to foreground
		time.sleep(2)
		py.moveTo(663, 198)
		py.click()

		time.sleep(2)
		py.moveTo(355, 457)
		py.click()

		time.sleep(2)
		print("Cancel successfully selected.")


		# Google Chrome
		time.sleep(1)
		print("Turning OFF Google Chrome...")

		time.sleep(2)
		py.moveTo(670, 488)
		py.click()

		time.sleep(2)
		print("Google Chrome successfully disabled.")

		time.sleep(1)
		print("Selecting cancel...")

		# Selecting TouchID window to foreground
		time.sleep(2)
		py.moveTo(663, 198)
		py.click()

		time.sleep(2)
		py.moveTo(355, 457)
		py.click()

		time.sleep(2)
		print("Cancel successfully selected.")


		# Home
		time.sleep(1)
		print("Turning OFF Home...")

		time.sleep(2)
		py.moveTo(670, 453)
		py.click()

		time.sleep(2)
		print("Home successfully disabled.")

		time.sleep(1)
		print("Selecting cancel...")

		# Selecting TouchID window to foreground
		time.sleep(2)
		py.moveTo(663, 198)
		py.click()

		time.sleep(2)
		py.moveTo(355, 457)
		py.click()

		time.sleep(2)
		print("Cancel successfully selected.")


		# Maps
		time.sleep(1)
		print("Turning OFF Maps...")

		time.sleep(2)
		py.moveTo(670, 496)
		py.click()

		time.sleep(2)
		print("Maps successfully disabled.")

		time.sleep(1)
		print("Selecting cancel...")

		# Selecting TouchID window to foreground
		time.sleep(2)
		py.moveTo(663, 198)
		py.click()

		time.sleep(2)
		py.moveTo(355, 457)
		py.click()

		time.sleep(2)
		print("Cancel successfully selected.")


		# Messages
		time.sleep(1)
		print("Turning OFF Messages...")

		time.sleep(2)
		py.moveTo(670, 540)
		py.click()

		time.sleep(2)
		print("Messages successfully disabled.")

		time.sleep(1)
		print("Selecting cancel...")

		# Selecting TouchID window to foreground
		time.sleep(2)
		py.moveTo(663, 198)
		py.click()

		time.sleep(2)
		py.moveTo(355, 457)
		py.click()

		time.sleep(2)
		print("Cancel successfully selected.")


		# News
		time.sleep(1)
		print("Turning OFF News...")

		time.sleep(2)
		py.moveTo(670, 582)
		py.click()

		time.sleep(2)
		print("News successfully disabled.")

		time.sleep(1)
		print("Selecting cancel...")

		# Selecting TouchID window to foreground
		time.sleep(2)
		py.moveTo(663, 198)
		py.click()

		time.sleep(2)
		py.moveTo(355, 457)
		py.click()

		time.sleep(2)
		print("Cancel successfully selected.")


		# Reminders
		time.sleep(1)
		print("Turning OFF Reminders...")

		time.sleep(2)
		py.moveTo(670, 627)
		py.click()

		time.sleep(2)
		print("Reminders successfully disabled.")

		time.sleep(1)
		print("Selecting cancel...")

		# Selecting TouchID window to foreground
		time.sleep(2)
		py.moveTo(663, 198)
		py.click()

		time.sleep(2)
		py.moveTo(355, 457)
		py.click()

		time.sleep(2)
		print("Cancel successfully selected.")

		i.tearDown()


# Contacts
	@staticmethod
	def test_open_contacts_privacy_settings():

		i.setUp()

		time.sleep(1)
		print("Opening contacts tab...")

		time.sleep(2)
		py.moveTo(679, 168)
		py.click()

		time.sleep(2)
		print("Contacts tab successfully opened.")

		i.tearDown()


# Calendars
	@staticmethod
	def test_open_calendars_privacy_settings():

		i.setUp()

		time.sleep(1)
		print("Opening calendars tab...")

		time.sleep(2)
		py.moveTo(679, 212)
		py.click()

		time.sleep(2)
		print("Calendars tab successfully opened.")

		i.tearDown()


# Reminders
	@staticmethod
	def test_open_reminders_privacy_settings():

		i.setUp()

		time.sleep(1)
		print("Opening Reminders tab...")

		time.sleep(2)
		py.moveTo(679, 255)
		py.click()

		time.sleep(2)
		print("Reminders tab successfully opened.")

		i.tearDown()


# Photos
	@staticmethod
	def test_open_photos_privacy_settings():

		i.setUp()

		time.sleep(1)
		print("Opening photos tab...")

		time.sleep(2)
		py.moveTo(679, 298)
		py.click()

		time.sleep(2)
		print("Photos tab successfully opened.")

		# Final Cut Pro
		time.sleep(1)
		print("Turning OFF Final Cut Pro...")

		time.sleep(2)
		py.moveTo(670, 131)
		py.click()

		time.sleep(2)
		print("Final Cut Pro successfully disabled.")

		time.sleep(1)
		print("Turning ON Final Cut Pro...")

		time.sleep(2)
		py.moveTo(670, 131)
		py.click()

		time.sleep(2)
		print("Final Cut Pro successfully enabled.")

		i.tearDown()


# Blutooth
	@staticmethod
	def test_open_blutooth_privacy_settings():

		i.setUp()

		time.sleep(1)
		print("Opening bluetooth tab...")

		time.sleep(2)
		py.moveTo(679, 342)
		py.click()

		time.sleep(2)
		print("Bluetooth tab successfully opened.")

		i.tearDown()


# Microphone
	@staticmethod
	def test_open_microphone_privacy_settings():

		i.setUp()

		time.sleep(1)
		print("Opening microphone tab...")

		time.sleep(2)
		py.moveTo(679, 384)
		py.click()

		time.sleep(2)
		print("Microphone tab successfully opened.")

		# Cisco Webex Meetings
		time.sleep(1)
		print("Turning OFF Webex Meetings...")

		time.sleep(2)
		py.moveTo(670, 134)
		py.click()

		time.sleep(2)
		print("Webex Meetings successfully disabled.")

		time.sleep(1)
		print("Turning ON Webex Meetings...")

		time.sleep(2)
		py.moveTo(670, 134)
		py.click()

		time.sleep(2)
		print("Webex Meetings successfully enabled.")


		# Discord
		time.sleep(1)
		print("Turning OFF Discord...")

		time.sleep(2)
		py.moveTo(670, 176)
		py.click()

		time.sleep(2)
		print("Discord successfully disabled.")

		time.sleep(1)
		print("Turning ON Discord...")

		time.sleep(2)
		py.moveTo(670, 176)
		py.click()

		time.sleep(2)
		print("Discord successfully enabled.")


		# Final Cut Pro
		time.sleep(1)
		print("Turning OFF Final Cut Pro...")

		time.sleep(2)
		py.moveTo(670, 220)
		py.click()

		time.sleep(2)
		print("Final Cut Pro successfully disabled.")

		time.sleep(1)
		print("Turning ON Final Cut Pro...")

		time.sleep(2)
		py.moveTo(670, 220)
		py.click()

		time.sleep(2)
		print("Final Cut Pro successfully enabled.")


		# GarageBand
		time.sleep(1)
		print("Turning OFF GarageBand...")

		time.sleep(2)
		py.moveTo(670, 263)
		py.click()

		time.sleep(2)
		print("GarageBand successfully disabled.")

		time.sleep(1)
		print("Turning ON GarageBand...")

		time.sleep(2)
		py.moveTo(670, 263)
		py.click()

		time.sleep(2)
		print("GarageBand successfully enabled.")


		# PyCharm CE
		time.sleep(1)
		print("Turning OFF PyCharm CE...")

		time.sleep(2)
		py.moveTo(670, 305)
		py.click()

		time.sleep(2)
		print("PyCharm CE successfully disabled.")

		time.sleep(1)
		print("Turning ON PyCharm CE...")

		time.sleep(2)
		py.moveTo(670, 305)
		py.click()

		time.sleep(2)
		print("PyCharm CE successfully enabled.")


		# Webex
		time.sleep(1)
		print("Turning OFF Webex...")

		time.sleep(2)
		py.moveTo(670, 348)
		py.click()

		time.sleep(2)
		print("Webex successfully disabled.")

		time.sleep(1)
		print("Turning ON Webex...")

		time.sleep(2)
		py.moveTo(670, 348)
		py.click()

		time.sleep(2)
		print("Webex successfully enabled.")

		i.tearDown()


# Camera
	@staticmethod
	def test_open_camera_privacy_settings():

		i.setUp()

		time.sleep(1)
		print("Opening camera tab...")

		time.sleep(2)
		py.moveTo(679, 425)
		py.click()

		time.sleep(2)
		print("Camera tab successfully opened.")

		# Cisco Webex Meetings
		time.sleep(1)
		print("Turning OFF Webex Meetings...")

		time.sleep(2)
		py.moveTo(670, 134)
		py.click()

		time.sleep(2)
		print("Webex Meetings successfully disabled.")

		time.sleep(1)
		print("Turning ON Webex Meetings...")

		time.sleep(2)
		py.moveTo(670, 134)
		py.click()

		time.sleep(2)
		print("Webex Meetings successfully enabled.")


		# Discord
		time.sleep(1)
		print("Turning OFF Discord...")

		time.sleep(2)
		py.moveTo(670, 176)
		py.click()

		time.sleep(2)
		print("Discord successfully disabled.")

		time.sleep(1)
		print("Turning ON Discord...")

		time.sleep(2)
		py.moveTo(670, 176)
		py.click()

		time.sleep(2)
		print("Discord successfully enabled.")


		# Final Cut Pro
		time.sleep(1)
		print("Turning OFF Final Cut Pro...")

		time.sleep(2)
		py.moveTo(670, 220)
		py.click()

		time.sleep(2)
		print("Final Cut Pro successfully disabled.")

		time.sleep(1)
		print("Turning ON Final Cut Pro...")

		time.sleep(2)
		py.moveTo(670, 220)
		py.click()

		time.sleep(2)
		print("Final Cut Pro successfully enabled.")


		# PyCharm CE
		time.sleep(1)
		print("Turning OFF PyCharm CE...")

		time.sleep(2)
		py.moveTo(670, 263)
		py.click()

		time.sleep(2)
		print("PyCharm CE successfully disabled.")

		time.sleep(1)
		print("Turning ON PyCharm CE...")

		time.sleep(2)
		py.moveTo(670, 263)
		py.click()

		time.sleep(2)
		print("PyCharm CE successfully enabled.")


		# Webex
		time.sleep(1)
		print("Turning OFF Webex...")

		time.sleep(2)
		py.moveTo(670, 306)
		py.click()

		time.sleep(2)
		print("Webex successfully disabled.")

		time.sleep(1)
		print("Turning ON Webex...")

		time.sleep(2)
		py.moveTo(670, 306)
		py.click()

		time.sleep(2)
		print("Webex successfully enabled.")

		i.tearDown()


# HomeKit
	@staticmethod
	def test_open_homekit_privacy_settings():

		i.setUp()

		time.sleep(1)
		print("Opening HomeKit tab...")

		time.sleep(2)
		py.moveTo(679, 471)
		py.click()

		time.sleep(2)
		print("HomeKit tab successfully opened.")

		i.tearDown()


# Speech Recognition
	@staticmethod
	def test_open_speech_recognition_privacy_settings():

		i.setUp()

		time.sleep(1)
		print("Opening speech recognition tab...")

		time.sleep(2)
		py.moveTo(679, 513)
		py.click()

		time.sleep(2)
		print("Speech recognition tab successfully opened.")

		i.tearDown()


# Media & Apple Music
	@staticmethod
	def test_open_apple_music_privacy_settings():

		i.setUp()

		time.sleep(1)
		print("Opening media & Apple Music tab...")

		time.sleep(2)
		py.moveTo(679, 556)
		py.click()

		time.sleep(2)
		print("Media & Apple Music tab successfully opened.")

		i.tearDown()


# Files and Folders
	@staticmethod
	def test_open_files_and_folders_privacy_settings():

		i.setUp()

		time.sleep(1)
		print("Opening files and folders tab...")

		time.sleep(2)
		py.moveTo(679, 599)
		py.click()

		time.sleep(2)
		print("Files and folders tab successfully opened.")

		i.tearDown()


	@staticmethod
	def privacyAndSecurityTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning Privacy & Security test suite...")

		print("===============================================================")
		print("===============================================================")

		i.test_open_location_services_privacy_settings()
		i.tearDown()

		print("===============================================================")

		i.test_location_services_privacy_settings()

		print("===============================================================")

		i.test_open_contacts_privacy_settings()

		print("===============================================================")

		i.test_open_calendars_privacy_settings()

		print("===============================================================")

		i.test_open_reminders_privacy_settings()

		print("===============================================================")

		i.test_open_photos_privacy_settings()

		print("===============================================================")

		i.test_open_blutooth_privacy_settings()

		print("===============================================================")

		i.test_open_microphone_privacy_settings()

		print("===============================================================")

		i.test_open_camera_privacy_settings()

		print("===============================================================")

		i.test_open_homekit_privacy_settings()

		print("===============================================================")

		i.test_open_speech_recognition_privacy_settings()

		print("===============================================================")

		i.test_open_apple_music_privacy_settings()

		print("===============================================================")

		i.test_open_files_and_folders_privacy_settings()

		print("===============================================================")
		print("===============================================================")

		print("Test suite completed.")

		print("===============================================================")
		print("===============================================================")
		return	





# =====================================================================
# Tests:
i = Privacy()

