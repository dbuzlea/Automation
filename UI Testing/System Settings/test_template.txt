import pyautogui as py
import time
import os


TIME_LIMIT = 5

class TestClassName:
	

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

		py.write("TestClassName")
		time.sleep(2)
		py.press('return')

		time.sleep(2)

		print("Test environmenmt successfully set up.")


	@staticmethod
	def tearDown():
		time.sleep(1)
		print("Tearing down test environment...")
		os.system("pkill -a 'System Settings'")


# First Test Method
	@staticmethod
	def test_first_method():
		# code






# =====================================================================
# Tests:
i = TestClassName()

print("===============================================================")
print("===============================================================")

print("Beginning test suite...")

print("===============================================================")
print("===============================================================")

i.setUp()
i.test_first_method()
i.tearDown()

print("===============================================================")

i.setUp()
# last test method
i.tearDown()

print("===============================================================")
print("===============================================================")

print("Test suite completed.")

print("===============================================================")
print("===============================================================")



