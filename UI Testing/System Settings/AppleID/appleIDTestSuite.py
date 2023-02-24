import pyautogui as py
import time
import os

class AppleID:

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

		py.write("AppleID")

		time.sleep(2)
		py.press('return')
		print("Test environmenmt successfully set up.")


	@staticmethod
	def tearDown():
		time.sleep(1)
		print("Tearing down test environment...")
		os.system("pkill -a 'System Settings'")




	@staticmethod
	def test_open_name_phone_email_appleID_settings():
		print("Opening Name, Phone, and Email pane...")
		time.sleep(1)

		py.moveTo(449, 277)
		py.click()

		time.sleep(10)
		print("Name, Phone, Email pane successfully opened.")

	
	@staticmethod
	def test_open_password_and_security_appleID_settings():
		print("Opening Password and Security pane...")
		time.sleep(1)

		py.moveTo(462, 319)
		py.click()

		time.sleep(10)
		print("Password and Security pane successfully opened.")


	@staticmethod
	def test_open_payment_and_shipping_appleID_settings():
		print("Opening Payment and Shipping pane...")
		time.sleep(1)

		py.moveTo(511, 365)
		py.click()

		time.sleep(10)
		print("Payment and Shipping pane successfully opened.")	


	@staticmethod	
	def appleIDTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning AppleID test suite...")

		print("===============================================================")
		print("===============================================================")

		i.setUp()
		i.test_open_name_phone_email_appleID_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_password_and_security_appleID_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_payment_and_shipping_appleID_settings()
		i.tearDown()

		print("===============================================================")
		print("===============================================================")

		print("Test suite completed.")

		print("===============================================================")
		print("===============================================================")
		return			




# ======================================================================
i = AppleID()

# print("===============================================================")
# print("===============================================================")

# print("Beginning test suite...")

# print("===============================================================")
# print("===============================================================")

# i.setUp()
# i.test_open_name_phone_email_appleID_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_password_and_security_appleID_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_payment_and_shipping_appleID_settings()
# i.tearDown()

# print("===============================================================")
# print("===============================================================")

# print("Test suite completed.")

# print("===============================================================")
# print("===============================================================")

