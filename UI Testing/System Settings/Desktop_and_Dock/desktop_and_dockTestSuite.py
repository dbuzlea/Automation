import pyautogui as py
import time
import os


TIME_LIMIT = 10

class DesktopAndDock:
	

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

		py.write("Desktop & Dock")
		time.sleep(2)
		py.press('return')

		time.sleep(2)

		print("Test environmenmt successfully set up.")


	@staticmethod
	def tearDown():
		time.sleep(1)
		print("Tearing down test environment...")
		os.system("pkill -a 'System Settings'")



# Position on screen
	@staticmethod
	def test_select_position_on_screen_desktop_and_dock_settings():

		i.setUp()

		time.sleep(1)
		print("Opening position on screen drop down menu...")

		time.sleep(2)
		py.moveTo(671, 208)
		py.click()

		time.sleep(2)
		print("Position on screen drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing position on screen drop down menu...")

		time.sleep(2)
		py.press("Escape")

		time.sleep(2)
		print("Position on screen drop down menu successfully collapsed.")

		i.tearDown()


# Minimize windows using
	@staticmethod
	def test_select_minimize_windows_using_desktop_and_dock_settings():

		i.setUp()

		time.sleep(1)
		print("Opening minimize windows using drop down menu...")

		time.sleep(2)
		py.moveTo(671, 244)
		py.click()

		time.sleep(2)
		print("Minimize windows using drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing minimize windows using drop down menu...")

		time.sleep(2)
		py.press("Escape")

		time.sleep(2)
		print("Minimize windows using drop down menu successfully collapsed.")

		i.tearDown()


# Double-click window title bar to
	@staticmethod
	def test_select_doubleClick_window_title_bar_desktop_and_dock_settings():

		i.setUp()

		time.sleep(1)
		print("Opening double-click window title bar drop down menu...")

		time.sleep(2)
		py.moveTo(671, 284)
		py.click()

		time.sleep(2)
		print("Double-click window title bar drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing double-click window title bar drop down menu...")

		time.sleep(2)
		py.press("Escape")

		time.sleep(2)
		print("Double-click window title bar drop down menu successfully collapsed.")

		i.tearDown()


	@staticmethod
	def desktop_and_dockTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning Desktop and Dock test suite...")

		print("===============================================================")
		print("===============================================================")

		i.test_select_position_on_screen_desktop_and_dock_settings()

		print("===============================================================")

		i.test_select_minimize_windows_using_desktop_and_dock_settings()

		print("===============================================================")

		i.test_select_doubleClick_window_title_bar_desktop_and_dock_settings()

		print("===============================================================")
		print("===============================================================")

		print("Desktop & Dock test suite completed.")

		print("===============================================================")
		print("===============================================================")
		return		

# =====================================================================
# Tests:
i = DesktopAndDock()

