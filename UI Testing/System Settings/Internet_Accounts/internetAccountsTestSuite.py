import pyautogui as py
import time
import os


TIME_LIMIT = 5

# Change to proper email credentials:
EMAIL = "mailAccount@gmail.com"
PASSWORD = "Password123"

class InternetAccounts:
	

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

		py.write("Internet Accounts")
		time.sleep(2)
		py.press('return')

		time.sleep(2)

		print("Test environmenmt successfully set up.")


	@staticmethod
	def tearDown():
		time.sleep(1)
		print("Tearing down test environment...")
		os.system("pkill -a 'System Settings'")



# Add Account
	@staticmethod
	def test_add_account_internet_accounts_settings():

		i.setUp()

		time.sleep(1)
		print("Selecting Add Account...")

		py.moveTo(612, 299)
		py.click()
		time.sleep(2)

		time.sleep(2)
		print("Add Account successfully selected.")

		# Select Google
		time.sleep(1)
		print("Selecting Google...")

		py.moveTo(362, 324)
		py.click()

		time.sleep(2)
		print("Google successfully selected.")

		# Open Browser
		time.sleep(1)
		print("Selecting Open Browser...")

		py.moveTo(411, 427)
		py.click()

		time.sleep(2)
		print("Open Browser successfully selected.")

		time.sleep(TIME_LIMIT)

		# Login
		time.sleep(1)
		print("Entering in username...")

		py.write(EMAIL)
		time.sleep(1)
		py.press("return")

		time.sleep(2)
		print("Username successfully entered.")

		# Password
		time.sleep(3)
		print("Entering in password...")

		py.write(PASSWORD)
		time.sleep(1)
		py.press("return")

		time.sleep(2)
		print("Password successfully entered.")

# UNCOMMENT ONCE EMAIL CREDENTIALS ARE ADDED: 		

		# # Send
		# time.sleep(1)
		# print("Selecting send...")

		# py.moveTo(656, 702)
		# py.click()

		# time.sleep(2)
		# print("Send successfully selected.")

		# # 2FA
		# time.sleep(2)
		# print("Entering in 2FA code...")

		# py.press("return")

		# time.sleep(1)
		# print("2FA successfully entered.")

		# # Done
		# time.sleep(3)
		# print("Selecting Done...")

		# py.moveTo(494, 466)
		# py.click()

		# time.sleep(2)
		# print("Done successfully selected.")

		# time.sleep(TIME_LIMIT)

		print("Mail account successfully added.")

		i.tearDown()



# Delete Account [CAUTION: THIS WILL REMOVE AN ACCOUNT FROM YOUR MAIL SETTINGS!]
	@staticmethod
	def test_delete_account_internet_accounts_settings():

		i.setUp()

		time.sleep(1)
		print("Selecting mail account...")

		py.moveTo(622, 224)
		py.click()
		time.sleep(1)

		time.sleep(1)
		print("Mail account successfully selected.")

		# Delete Account
		time.sleep(1)
		print("Selecting Delete Account...")

		py.moveTo(286, 339)
		py.click()

		time.sleep(2)
		print("Delete Account successfully selected.")

		# OK
		time.sleep(1)
		print("Deleting mail account...")

		py.moveTo(414, 437)
		py.click()

		time.sleep(2)
		print("Mail account successfully deleted.")

		i.tearDown()



	@staticmethod
	def internetAccountsTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning Internet Accounts test suite...")

		print("===============================================================")
		print("===============================================================")

		i.test_add_account_internet_accounts_settings()

		print("===============================================================")

		i.test_delete_account_internet_accounts_settings()

		print("===============================================================")
		print("===============================================================")

		print("Internet Accounts test suite completed.")

		print("===============================================================")
		print("===============================================================")
		return	




# =====================================================================
# Tests:
i = InternetAccounts()

