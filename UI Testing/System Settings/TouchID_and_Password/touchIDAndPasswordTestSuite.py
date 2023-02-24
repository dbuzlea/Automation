import pyautogui as py
import time
import os


# TODO: Re-enable toggles after initial run

TIME_LIMIT = 10

class TouchIDAndPassword:
	

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

		py.write("TouchID")
		time.sleep(2)
		py.press('return')

		time.sleep(2)

		print("Test environmenmt successfully set up.")


	@staticmethod
	def tearDown():
		time.sleep(1)
		print("Tearing down test environment...")
		os.system("pkill -a 'System Settings'")


# Use TouchID to unlock your Mac
	@staticmethod
	def test_toggle_use_touchID_to_unlock_mac_touchID_settings():
		time.sleep(1)
		print("Turning OFF unlock Touch ID to unlock your Mac...")

		time.sleep(2)
		py.moveTo(671, 340)
		py.click()

		time.sleep(2)
		print("Unlock Touch ID to unlock your Mac successfully disabled.")

		time.sleep(1)
		print("Turning ON unlock Touch ID to unlock your Mac...")

		time.sleep(2)
		py.moveTo(671, 340)
		py.click()

		time.sleep(2)
		print("Unlock Touch ID to unlock your Mac successfully enabled.")



# Use TouchID for Apple Pay
	@staticmethod
	def test_toggle_use_touchID_for_apple_pay_touchID_settings():
		time.sleep(1)
		print("Turning OFF unlock Touch ID for Apple Pay...")

		time.sleep(2)
		py.moveTo(671, 379)
		py.click()

		time.sleep(2)
		print("Unlock Touch ID for Apple Pay successfully disabled.")

		time.sleep(1)
		print("Turning ON unlock Touch ID for Apple Pa...")

		time.sleep(2)
		py.moveTo(671, 379)
		py.click()

		time.sleep(2)
		print("Unlock Touch ID for Apple Pay successfully enabled.")



# Use TouchID for purchases in iTunes Store, App Store, and Apple Books
	@staticmethod
	def test_toggle_use_touchID_for_purchases_touchID_settings():
		time.sleep(1)
		print("Turning OFF unlock Touch ID for purchases...")

		time.sleep(2)
		py.moveTo(671, 416)
		py.click()

		time.sleep(2)
		print("Unlock Touch ID for purchases successfully disabled.")

		time.sleep(1)
		print("Turning ON unlock Touch ID for purchases...")

		time.sleep(2)
		py.moveTo(671, 416)
		py.click()

		time.sleep(2)
		print("Unlock Touch ID for purchases successfully enabled.")



# Use TouchID for autofilling passwords
	@staticmethod
	def test_toggle_use_touchID_for_passwords_touchID_settings():
		time.sleep(1)
		print("Turning OFF unlock Touch ID for autofilling passwords...")

		time.sleep(2)
		py.moveTo(671, 472)
		py.click()

		time.sleep(2)
		print("Unlock Touch ID for autofilling passwords successfully disabled.")

		time.sleep(1)
		print("Turning ON unlock Touch ID for autofilling passwords...")

		time.sleep(2)
		py.moveTo(671, 472)
		py.click()

		time.sleep(2)
		print("Unlock Touch ID for autofilling passwords successfully enabled.")



# Use TouchID for fast user switching
	@staticmethod
	def test_toggle_use_touchID_for_user_switching_touchID_settings():
		time.sleep(1)
		print("Turning OFF unlock Touch ID for fast user switching...")

		time.sleep(2)
		py.moveTo(671, 511)
		py.click()

		time.sleep(2)
		print("Unlock Touch ID for fast user switching successfully disabled.")

		time.sleep(1)
		print("Turning ON unlock Touch ID for fast user switching...")

		time.sleep(2)
		py.moveTo(671, 511)
		py.click()

		time.sleep(2)
		print("Unlock Touch ID for fast user switching successfully enabled.")


	@staticmethod
	def touchIDAndPasswordTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning TouchID & Password test suite...")

		print("===============================================================")
		print("===============================================================")

		i.setUp()
		i.test_toggle_use_touchID_to_unlock_mac_touchID_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_toggle_use_touchID_for_apple_pay_touchID_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_toggle_use_touchID_for_purchases_touchID_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_toggle_use_touchID_for_passwords_touchID_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_toggle_use_touchID_for_user_switching_touchID_settings()
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
i = TouchIDAndPassword()

# print("===============================================================")
# print("===============================================================")

# print("Beginning test suite...")

# print("===============================================================")
# print("===============================================================")

# i.setUp()
# i.test_toggle_use_touchID_to_unlock_mac_touchID_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_toggle_use_touchID_for_apple_pay_touchID_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_toggle_use_touchID_for_purchases_touchID_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_toggle_use_touchID_for_passwords_touchID_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_toggle_use_touchID_for_user_switching_touchID_settings()
# i.tearDown()

# print("===============================================================")

# print("===============================================================")
# print("===============================================================")

# print("Test suite completed.")

# print("===============================================================")
# print("===============================================================")



