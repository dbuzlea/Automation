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



# NAME, PHONE, EMAIL:
	@staticmethod
	def test_open_name_phone_email_appleID_settings():

		i.setUp()

		print("Opening Name, Phone, and Email pane...")
		time.sleep(3)

		py.moveTo(679, 280)
		py.click()

		time.sleep(10)
		print("Name, Phone, Email pane successfully opened.")

		i.tearDown()

# PASSWORD & SECURITY:	
	@staticmethod
	def test_open_password_and_security_appleID_settings():

		i.setUp()

		print("Opening Password and Security pane...")
		time.sleep(3)

		py.moveTo(679, 324)
		py.click()

		time.sleep(10)
		print("Password and Security pane successfully opened.")

		i.tearDown()

# PAYMENT & SHIPPING:
	@staticmethod
	def test_open_payment_and_shipping_appleID_settings():

		i.setUp()

		print("Opening Payment and Shipping pane...")
		time.sleep(3)

		py.moveTo(679, 365)
		py.click()

		time.sleep(10)
		print("Payment and Shipping pane successfully opened.")

		i.tearDown()	


	@staticmethod	
	def appleIDTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning AppleID test suite...")

		print("===============================================================")
		print("===============================================================")

		i.test_open_name_phone_email_appleID_settings()

		print("===============================================================")

		i.test_open_password_and_security_appleID_settings()

		print("===============================================================")

		i.test_open_payment_and_shipping_appleID_settings()

		print("===============================================================")
		print("===============================================================")

		print("AppleID test suite completed.")

		print("===============================================================")
		print("===============================================================")
		return			




# ======================================================================
i = AppleID()

