import pyautogui as py
import time
import os

TIME_LIMIT = 10

class Notifications:

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

		py.write("Notifications")
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
	def test_show_previews_notifications_settings():
		time.sleep(1)
		print("Selecting Show Previews drop down menu...")

		py.moveTo(677, 155)
		py.click()

		time.sleep(2)
		print("Show Previews drop down menu successfully opened.")


	@staticmethod
	def test_turn_ON_display_sleeping_notifications_settings():
		time.sleep(1)
		print("Turning ON Notifications when display is sleeping...")

		py.moveTo(671, 191)
		py.click()

		time.sleep(2)
		print("Notifications when display is sleeping successfully enabled.")


	@staticmethod
	def test_turn_OFF_display_sleeping_notifications_settings():
		time.sleep(1)
		print("Turning OFF Notifications when display is sleeping...")

		py.moveTo(671, 191)
		py.click()

		time.sleep(2)
		print("Notifications when display is sleeping successfully disabled.")


	@staticmethod
	def test_turn_OFF_screen_locked_notifications_settings():
		time.sleep(1)
		print("Turning OFF Notifications when screen is locked...")

		py.moveTo(671, 231)
		py.click()

		time.sleep(2)
		print("Notifications when screen is locked successfully disabled.")			
				

	@staticmethod
	def test_turn_ON_screen_locked_notifications_settings():
		time.sleep(1)
		print("Turning ON Notifications when screen is locked...")

		py.moveTo(671, 231)
		py.click()

		time.sleep(2)
		print("Notifications when screen is locked successfully enabled.")


	@staticmethod
	def test_turn_ON_mirroring_screenSharing_notifications_settings():
		time.sleep(1)
		print("Turning ON Notifications when mirroring or sharing display...")

		py.moveTo(671, 271)
		py.click()

		time.sleep(2)
		print("Notifications when mirroring or sharing display successfully enabled.")


	@staticmethod
	def test_turn_OFF_mirroring_screenSharing_notifications_settings():
		time.sleep(1)
		print("Turning OFF Notifications when mirroring or sharing display...")

		py.moveTo(671, 271)
		py.click()

		time.sleep(2)
		print("Notifications when mirroring or sharing display successfully disabled.")


	@staticmethod
	def test_turn_ON_app_store_notifications_settings():
		time.sleep(1)
		print("Turning ON Notifications for App Store...")

		py.moveTo(680, 374)
		py.click()

		time.sleep(1)

		py.moveTo(664, 92)
		py.click()

		time.sleep(2)
		print("Notifications for App Store successfully enabled.")


	@staticmethod
	def test_turn_OFF_app_store_notifications_settings():
		time.sleep(1)
		print("Turning OFF Notifications for App Store...")

		py.moveTo(680, 374)
		py.click()

		time.sleep(1)

		py.moveTo(664, 92)
		py.click()

		time.sleep(2)
		print("Notifications for App Store successfully disabled.")	


	@staticmethod
	def test_turn_ON_books_notifications_settings():
		time.sleep(1)
		print("Turning ON Notifications for Books...")

		py.moveTo(680, 539)
		py.click()

		time.sleep(1)

		py.moveTo(664, 92)
		py.click()

		time.sleep(2)
		print("Notifications for Books successfully enabled.")


	@staticmethod
	def test_turn_OFF_books_notifications_settings():
		time.sleep(1)
		print("Turning OFF Notifications for Books...")

		py.moveTo(680, 539)
		py.click()

		time.sleep(1)

		py.moveTo(664, 92)
		py.click()

		time.sleep(2)
		print("Notifications for Books successfully disabled.")


	@staticmethod
	def test_turn_ON_calendar_notifications_settings():
		time.sleep(1)
		print("Turning ON Notifications for Calendar...")

		py.moveTo(680, 596)
		py.click()

		time.sleep(1)

		py.moveTo(664, 92)
		py.click()

		time.sleep(2)
		print("Notifications for Calendar successfully enabled.")


	@staticmethod
	def test_turn_OFF_calendar_notifications_settings():
		time.sleep(1)
		print("Turning OFF Notifications for Calendar...")

		py.moveTo(680, 596)
		py.click()

		time.sleep(1)

		py.moveTo(664, 92)
		py.click()

		time.sleep(2)
		print("Notifications for Calendar successfully disabled.")							


# =====================================================================
# Tests:
i = Notifications()

print("===============================================================")
print("===============================================================")

print("Beginning test suite...")

print("===============================================================")
print("===============================================================")

i.setUp()
i.test_show_previews_notifications_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_ON_display_sleeping_notifications_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_OFF_display_sleeping_notifications_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_OFF_screen_locked_notifications_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_ON_screen_locked_notifications_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_ON_mirroring_screenSharing_notifications_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_OFF_mirroring_screenSharing_notifications_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_ON_app_store_notifications_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_OFF_app_store_notifications_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_ON_books_notifications_settings()
i.tearDown()

print("===============================================================")

i.setUp()
i.test_turn_OFF_books_notifications_settings()
i.tearDown()

print("===============================================================")

print("===============================================================")
print("===============================================================")

print("Test suite completed.")

print("===============================================================")
print("===============================================================")



