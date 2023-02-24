import pyautogui as py
import time
import os


TIME_LIMIT = 5

class UsersAndGroups:
	

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

		py.write("Users & Groups")
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
	def test_create_user_account_users_and_groups_settings():
		time.sleep(1)
		print("Adding new user account...")

		# Add Account
		time.sleep(2)
		py.moveTo(640, 205)
		py.click()

		# authenticate
		print("Authenticating...")
		time.sleep(2)
		py.write("apple")
		time.sleep(1)
		py.press("return")
		time.sleep(1)
		print("Authentication complete")

		# username
		print("Entering username...")
		time.sleep(2)
		py.write("Test Account")
		time.sleep(1)
		py.press("Tab")
		time.sleep(1)
		py.press("Tab")
		time.sleep(1)
		print("Usename successfully entered.")


		# Password
		print("Entering password...")
		py.write("apple")
		time.sleep(1)
		py.press("Tab")
		print("Password successfully entered.")
		# Verify
		print("Verifying password...")
		py.write("apple")
		py.press("Tab")
		time.sleep(1)
		print("Password successfully verified.")

		# hint
		print("Entering in password hint...")
		time.sleep(2)
		py.write("Password is 'apple'")
		time.sleep(1)
		print("Hint successfully entered.")

		# create user
		print("Selecting Create User...")
		py.moveTo(515, 473)
		py.click()
		print("Create User successfully selected.")

		time.sleep(TIME_LIMIT)
		print("New user account successfully created.")



# Delete new account
	@staticmethod
	def test_delete_user_account_users_and_groups_settings():
		time.sleep(1)
		print("Deleting new user account...")

		time.sleep(2)
		py.moveTo(674, 151)
		py.click()

		# Delete account
		print("Selecting Delete User...")
		time.sleep(2)
		py.moveTo(222, 403)
		py.click()
		print("Delete User successfully selected.")

		# authenticate
		print("Authenticating...")
		time.sleep(2)
		py.write("apple")
		time.sleep(1)
		py.press("return")
		time.sleep(1)
		print("Authentication complete")

		# Delete the home folder
		print("Selecting Delete the home folder...")
		time.sleep(2)
		py.moveTo(160, 388)
		py.click()
		print("Delete the home folder successfully selected.")

		# Select delete the home folder
		time.sleep(2)
		py.moveTo(515, 457)
		py.click()

		time.sleep(2)
		print("New user account successfully removed.")


	@staticmethod
	def usersAndGroupsTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning Users & Groups test suite...")

		print("===============================================================")
		print("===============================================================")

		i.setUp()
		i.test_create_user_account_users_and_groups_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_delete_user_account_users_and_groups_settings()
		i.tearDown()

		print("===============================================================")
		print("===============================================================")

		print("Test suite completed.")

		print("===============================================================")
		print("===============================================================")
		return		








# =====================================================================
# Tests:
i = UsersAndGroups()

# print("===============================================================")
# print("===============================================================")

# print("Beginning test suite...")

# print("===============================================================")
# print("===============================================================")

# i.setUp()
# i.test_create_user_account_users_and_groups_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_delete_user_account_users_and_groups_settings()
# i.tearDown()

# print("===============================================================")
# print("===============================================================")

# print("Test suite completed.")

# print("===============================================================")
# print("===============================================================")



