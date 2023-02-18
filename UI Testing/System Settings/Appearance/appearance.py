import pyautogui as py
import time
import os

TIME_LIMIT = 10

class Appearance:

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

		py.write("Appearance")
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
	def test_change_appearance_settings():
		time.sleep(1)
		print("Changing appearance...")

		time.sleep(2)
		py.moveTo(565, 105)
		py.click()

		time.sleep(2)
		print("Appearance successfully changed.")

		time.sleep(1)
		print("Changing appearance back to auto...")

		time.sleep(2)
		py.moveTo(643, 105)
		py.click()

		time.sleep(2)
		print("Appearance successfully changed back to auto.")


	@staticmethod
	def test_change_accent_color_appearance_settings():
		time.sleep(1)
		print("Changing accent color...")

		time.sleep(2)
		py.moveTo(519, 188)
		py.click()

		time.sleep(2)
		print("Accent color successfully changed.")

		time.sleep(1)
		print("Changing accent color back to multicolor...")

		time.sleep(2)
		py.moveTo(466, 187)
		py.click()

		time.sleep(2)
		print("Accent color successfully changed back to multicolor.")


	@staticmethod
	def test_select_highlight_color_appearance_settings():
		time.sleep(1)
		print("Selecting highlight color dropdown bar...")

		time.sleep(2)
		py.moveTo(669, 245)
		py.click()

		time.sleep(2)
		print("Highlight color dropdown bar successfully opened.")


	@staticmethod
	def test_select_sidebar_size_appearance_settings():
		time.sleep(1)
		print("Selecting sibebar icon size dropdown bar...")

		time.sleep(2)
		py.moveTo(673, 284)
		py.click()

		time.sleep(2)
		print("Sidebar icon size dropdown bar successfully opened.")


	@staticmethod
	def test_toggle_allow_wallpaper_tinting_appearance_settings():
		time.sleep(1)
		print("Tunring OFF allow wallpaper tinting in windows...")

		time.sleep(2)
		py.moveTo(669, 323)
		py.click()

		time.sleep(2)
		print("Allow wallpaper tinting in windows successfully disabled.")

		time.sleep(2)
		print("Tunring ON allow wallpaper tinting in windows...")

		time.sleep(2)
		py.moveTo(669, 323)
		py.click()

		time.sleep(2)
		print("Allow wallpaper tinting in windows successfully enabled.")												




# =====================================================================
# Tests:
i = Appearance()

print("===============================================================")
print("===============================================================")

print("Beginning test suite...")

print("===============================================================")
print("===============================================================")

i.setUp()
i.test_change_appearance_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_change_accent_color_appearance_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_select_highlight_color_appearance_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_select_sidebar_size_appearance_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_toggle_allow_wallpaper_tinting_appearance_settings()
i.tearDown()

print("===============================================================")

print("===============================================================")
print("===============================================================")
print("===============================================================")

print("Test suite completed.")

print("===============================================================")
print("===============================================================")



