import pyautogui as py
import time
import os

TIME_LIMIT = 10

class Focus:

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

		py.write("Focus")
		time.sleep(2)
		py.press('return')

		time.sleep(2)

		print("Test environmenmt successfully set up.")


	@staticmethod
	def tearDown():
		time.sleep(1)
		print("Tearing down test environment...")
		os.system("pkill -a 'System Settings'")



# DO NOT DISTURB PANE:
	@staticmethod
	def test_open_DND_pane_focus_settings():

		i.setUp()

		time.sleep(1)
		print("Opening Do Not Disturb pane...")

		py.moveTo(678, 93)
		py.click()

		time.sleep(2)
		print("Do Not Disturb pane successfully opened.")


# ALLOWED PEOPLE:
	@staticmethod
	def test_select_allowed_people_window_DND_pane_focus_settings():

		i.test_open_DND_pane_focus_settings()

		time.sleep(2)
		print("Selecting Allowed People in DND pane...")

		py.moveTo(678, 229)
		py.click()

		time.sleep(2)
		print("Allowed People window successfully opened.")

		time.sleep(2)
		print("Selecting Notifications drop down menu...")
		# notifications
		py.moveTo(503, 154)
		py.click()

		time.sleep(2)
		print("Notifications drop down menu successfully opened.")

		time.sleep(2)
		print("Selecting Allowed calls from drop down menu...")
		# allowCallsFrom
		py.moveTo(503, 347)
		py.click()

		time.sleep(2)
		print("Allowed calls from drop down menu successfully opened.")


		time.sleep(2)
		print("Turning OFF Allow repeated calls...")
		# allowRepeatedCalls
		py.moveTo(547, 417)
		py.click()

		time.sleep(2)
		print("Allow repeated calls successfully disabled.")

		time.sleep(2)
		print("Turning ON Allow repeated calls...")
		# allowRepeatedCallsOFF
		py.moveTo(547, 417)
		py.click()

		time.sleep(2)
		print("Allow repeated calls successfully enabled.")


		time.sleep(2)
		print("Closing out Allowed People window in DND pane...")
		# Done
		py.moveTo(540, 521)
		py.click()	

		time.sleep(2)
		print("Allowed People window successfully closed.")

		i.tearDown()


# ALLOWED APPS:
	@staticmethod
	def test_select_allowed_apps_window_DND_pane_focus_settings():

		i.test_open_DND_pane_focus_settings()

		time.sleep(2)
		print("Selecting Allowed Apps in DND pane...")

		py.moveTo(678, 285)
		py.click()

		time.sleep(2)
		print("Allowed Apps window successfully opened.")

		time.sleep(2)
		print("Selecting Notifications drop down menu...")
		# notifications
		py.moveTo(551, 195)
		py.click()
		time.sleep(1)
		py.click()

		time.sleep(2)
		print("Notifications drop down menu successfully opened.")

		time.sleep(2)
		print("Selecting Add button...")
		# addButton
		py.moveTo(177, 293)
		py.click()

		time.sleep(2)
		print("Add button successfully selected.")

		time.sleep(2)
		print("Selecting Cancel button...")
		# cancelButton
		py.moveTo(464, 534)
		py.click()

		time.sleep(2)
		print("Cancel button successfully selected.")

		time.sleep(2)
		print("Turning ON Time Sensitive Notifications...")
		# timeSensitiveNotifications
		py.moveTo(549, 375)
		py.click()

		time.sleep(2)
		print("Time Sensitive Notifications successfully enabled.")

		time.sleep(2)
		print("Turning OFF Time Sensitive Notifications...")
		# timeSensitiveNotificationsOFF
		py.moveTo(549, 375)
		py.click()

		time.sleep(2)
		print("Time Sensitive Notifications successfully disabled.")

		time.sleep(2)
		print("Closing out Allowed Apps window in DND pane...")
		# Done
		py.moveTo(540, 480)
		py.click()	

		time.sleep(2)
		print("Allowed Apps window successfully closed.")

		i.tearDown()


# SLEEP PANE:
	@staticmethod
	def test_open_sleep_pane_focus_settings():

		i.setUp()

		time.sleep(1)
		print("Opening Sleep pane...")

		py.moveTo(678, 135)
		py.click()

		time.sleep(2)
		print("Sleep pane successfully opened.")


# ALLOWED PEOPLE [SLEEP]:
	@staticmethod
	def test_select_allowed_people_window_sleep_pane_focus_settings():

		i.test_open_sleep_pane_focus_settings()

		time.sleep(2)
		print("Selecting Allowed People in DND pane...")

		py.moveTo(678, 229)
		py.click()

		time.sleep(2)
		print("Allowed People window successfully opened.")

		time.sleep(2)
		print("Selecting Notifications drop down menu...")
		# notifications
		py.moveTo(503, 154)
		py.click()

		time.sleep(2)
		print("Notifications drop down menu successfully opened.")

		time.sleep(2)
		print("Selecting Allowed calls from drop down menu...")
		# allowCallsFrom
		py.moveTo(503, 347)
		py.click()

		time.sleep(2)
		print("Allowed calls from drop down menu successfully opened.")


		time.sleep(2)
		print("Turning OFF Allow repeated calls...")
		# allowRepeatedCalls
		py.moveTo(547, 417)
		py.click()

		time.sleep(2)
		print("Allow repeated calls successfully disabled.")

		time.sleep(2)
		print("Turning ON Allow repeated calls...")
		# allowRepeatedCallsOFF
		py.moveTo(547, 417)
		py.click()

		time.sleep(2)
		print("Allow repeated calls successfully enabled.")


		time.sleep(2)
		print("Closing out Allowed People window in DND pane...")
		# Done
		py.moveTo(540, 521)
		py.click()	

		time.sleep(2)
		print("Allowed People window successfully closed.")

		i.tearDown()


# ALLOWED APPS [APPS]:
	@staticmethod
	def test_select_allowed_apps_window_sleep_pane_focus_settings():

		i.test_open_sleep_pane_focus_settings()

		time.sleep(2)
		print("Selecting Allowed Apps in DND pane...")

		py.moveTo(678, 285)
		py.click()

		time.sleep(2)
		print("Allowed Apps window successfully opened.")

		time.sleep(2)
		print("Selecting Notifications drop down menu...")
		# notifications
		py.moveTo(551, 195)
		py.click()
		time.sleep(1)
		py.click()

		time.sleep(2)
		print("Notifications drop down menu successfully opened.")

		time.sleep(2)
		print("Selecting Add button...")
		# addButton
		py.moveTo(177, 293)
		py.click()

		time.sleep(2)
		print("Add button successfully selected.")

		time.sleep(2)
		print("Selecting Cancel button...")
		# cancelButton
		py.moveTo(464, 534)
		py.click()

		time.sleep(2)
		print("Cancel button successfully selected.")

		time.sleep(2)
		print("Turning ON Time Sensitive Notifications...")
		# timeSensitiveNotifications
		py.moveTo(549, 375)
		py.click()

		time.sleep(2)
		print("Time Sensitive Notifications successfully enabled.")

		time.sleep(2)
		print("Turning OFF Time Sensitive Notifications...")
		# timeSensitiveNotificationsOFF
		py.moveTo(549, 375)
		py.click()

		time.sleep(2)
		print("Time Sensitive Notifications successfully disabled.")

		time.sleep(2)
		print("Closing out Allowed Apps window in DND pane...")
		# Done
		py.moveTo(540, 480)
		py.click()	

		time.sleep(2)
		print("Allowed Apps window successfully closed.")

		i.tearDown()


# ADD FILTER [SLEEP]:
	@staticmethod
	def test_select_add_filter_button_sleep_pane_focus_settings():

		i.test_open_sleep_pane_focus_settings()

		time.sleep(2)
		print("Selecting Add Filter button...")
		# addFilterButton
		py.moveTo(638, 554)
		py.click()

		time.sleep(2)
		print("Add Filter button successfully selected.")

		time.sleep(2)
		print("Selecting Cancel button...")
		# cancelButton
		py.moveTo(538, 496)
		py.click()

		time.sleep(2)
		print("Cancel button successfully selected.")

		i.tearDown()


# DELETE FOCUS [SLEEP]:
	@staticmethod
	def test_select_delete_focus_sleep_pane_focus_settings():

		i.test_open_sleep_pane_focus_settings()

		time.sleep(2)
		print("Selecting Delete Focus button...")

		py.moveTo(638, 605)
		py.click()

		time.sleep(2)
		print("Delete Focus button successfully selected.")

		time.sleep(2)
		print("Selecting Cancel button...")

		py.moveTo(300, 402)
		py.click()

		print("Cancel button successfully selected.")
		time.sleep(1)

		i.tearDown()


# ADD FOCUS:
	@staticmethod
	def test_select_add_focus_focus_settings():

		i.setUp()

		time.sleep(2)
		print("Selecting Add Focus button...")

		py.moveTo(647, 173)
		py.click()

		time.sleep(2)
		print("Add Focus button successfully selected.")

		i.tearDown()


# SHARE ACROSS DEVICES:
	@staticmethod
	def test_toggle_share_across_devices_focus_settings():

		i.setUp()

		time.sleep(2)
		print("Turning OFF Share across devices...")

		py.moveTo(669, 243)
		py.click()

		time.sleep(2)
		print("Share across devices successfully disabled.")

		time.sleep(2)
		print("Turning ON Share across devices...")

		py.moveTo(669, 243)
		py.click()

		time.sleep(2)
		print("Share across devices successfully enabled.")

		i.tearDown()
		
# Redundant Module:
	# @staticmethod
	# def test_select_add_focus_focus_settings():



	# 	time.sleep(2)
	# 	print("Selecting Add Focus button...")
	
	# 	py.moveTo(647, 173)
	# 	py.click()

	# 	time.sleep(2)
	# 	print("Add Focus button successfully selected.")


# FOCUS STATUS:
	@staticmethod
	def test_open_focus_status_focus_settings():

		i.setUp()

		time.sleep(2)
		print("Opening Focus status...")

		py.moveTo(678, 341)
		py.click()

		time.sleep(2)
		print("Focus status successfully opened.")


# SHARE FOCUS STATUS:
	@staticmethod
	def test_toggle_share_focus_status_pane_focus_settings():

		i.test_open_focus_status_focus_settings()

		time.sleep(2)
		print("Turning OFF Share Focus status...")

		py.moveTo(671, 91)
		py.click()

		time.sleep(2)
		print("Share Focus status successfully disabled.")

		time.sleep(2)
		print("Turning ON Share Focus status...")

		py.moveTo(671, 91)
		py.click()

		time.sleep(2)
		print("Share Focus status successfully enabled.")

		i.tearDown()


# SHARE FROM - DND:
	@staticmethod
	def test_toggle_share_from_DND_focus_status_pane_focus_settings():

		i.test_open_focus_status_focus_settings()

		time.sleep(2)
		print("Turning ON Share From DND...")

		py.moveTo(671, 236)
		py.click()

		time.sleep(2)
		print("Share From DND successfully enabled.")

		time.sleep(2)
		print("Turning OFF Share From DND...")

		py.moveTo(671, 236)
		py.click()

		time.sleep(2)
		print("Share From DND successfully disabled.")

		i.tearDown()


# SHARE FROM - SLEEP:
	@staticmethod
	def test_toggle_share_from_sleep_focus_status_pane_focus_settings():

		i.test_open_focus_status_focus_settings()

		time.sleep(2)
		print("Turning OFF Share From Sleep...")

		py.moveTo(671, 273)
		py.click()

		time.sleep(2)
		print("Share From Sleep successfully disabled.")

		time.sleep(2)
		print("Turning ON Share From Sleep...")

		py.moveTo(671, 273)
		py.click()

		time.sleep(2)
		print("Share From Sleep successfully enabled.")

		i.tearDown()



	@staticmethod
	def focusTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning Focus test suite...")

		print("===============================================================")
		print("===============================================================")

		i.test_open_DND_pane_focus_settings()

		print("===============================================================")

		i.test_select_allowed_people_window_DND_pane_focus_settings()

		print("===============================================================")

		i.test_select_allowed_apps_window_DND_pane_focus_settings()

		print("===============================================================")

		i.test_open_sleep_pane_focus_settings()

		print("===============================================================")

		i.test_select_allowed_people_window_sleep_pane_focus_settings()

		print("===============================================================")

		i.test_select_allowed_apps_window_sleep_pane_focus_settings()

		print("===============================================================")

		i.test_select_add_filter_button_sleep_pane_focus_settings()

		print("===============================================================")

		i.test_select_delete_focus_sleep_pane_focus_settings()

		print("===============================================================")

		i.test_select_add_focus_focus_settings()

		print("===============================================================")

		i.test_toggle_share_across_devices_focus_settings()

		print("===============================================================")

		i.test_open_focus_status_focus_settings()

		print("===============================================================")

		i.test_toggle_share_focus_status_pane_focus_settings()

		print("===============================================================")

		i.test_toggle_share_from_DND_focus_status_pane_focus_settings()

		print("===============================================================")

		i.test_toggle_share_from_sleep_focus_status_pane_focus_settings()

		print("===============================================================")
		print("===============================================================")

		print("Focus test suite completed.")

		print("===============================================================")
		print("===============================================================")
		return			




# =====================================================================
# Tests:
i = Focus()

