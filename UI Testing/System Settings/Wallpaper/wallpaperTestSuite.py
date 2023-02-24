import pyautogui as py
import time
import os


TIME_LIMIT = 10

class Wallpaper:
	

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

		py.write("Wallpaper")
		time.sleep(2)
		py.press('return')

		time.sleep(2)

		print("Test environmenmt successfully set up.")


	@staticmethod
	def tearDown():
		time.sleep(1)
		print("Tearing down test environment...")
		os.system("pkill -a 'System Settings'")


# Safari desktop picture
	@staticmethod
	def test_select_safari_desktop_picture_wallpaper_setting():
		time.sleep(1)
		print("Opening safari desktop picture drop down menu...")

		time.sleep(2)
		py.moveTo(671, 265)
		py.click()

		time.sleep(2)
		print("Safari desktop picture drop down menu successfully opened.")

		time.sleep(1)
		print("Safari desktop picture drop down menu...")

		time.sleep(2)
		py.moveTo(671, 265)
		py.click()

		time.sleep(2)
		print("Safari desktop picture drop down menu successfully collapsed.")


	@staticmethod
	def wallpaperTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning Wallpaper test suite...")

		print("===============================================================")
		print("===============================================================")

		i.setUp()
		i.test_select_safari_desktop_picture_wallpaper_setting()
		i.tearDown()

		print("===============================================================")
		print("===============================================================")

		print("Test suite completed.")

		print("===============================================================")
		print("===============================================================")
		return	



# =====================================================================
# Tests:
i = Wallpaper()

# print("===============================================================")
# print("===============================================================")

# print("Beginning test suite...")

# print("===============================================================")
# print("===============================================================")

# i.setUp()
# i.test_select_safari_desktop_picture_wallpaper_setting()
# i.tearDown()

# print("===============================================================")
# print("===============================================================")

# print("Test suite completed.")

# print("===============================================================")
# print("===============================================================")



