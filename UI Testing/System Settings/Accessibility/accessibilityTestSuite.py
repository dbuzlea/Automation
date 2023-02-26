import pyautogui as py
import time
import os


TIME_LIMIT = 10

class Accessibility:
	

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

		py.write("Accessibility")
		time.sleep(2)
		py.press('return')

		time.sleep(2)

		print("Test environmenmt successfully set up.")


	@staticmethod
	def tearDown():
		time.sleep(1)
		print("Tearing down test environment...")
		os.system("pkill -a 'System Settings'")



# VoiceOver
	@staticmethod
	def test_open_voice_over_accessibility_settings():
		time.sleep(1)
		print("Opening VoiceOver tab...")

		time.sleep(2)
		py.moveTo(679, 126)
		py.click()

		time.sleep(2)
		print("VoiceOver tab successfully opened.")


	@staticmethod
	def test_toggle_voice_over_accessibility_settings():
		time.sleep(1)
		print("Turning ON VoiceOver...")

		time.sleep(2)
		py.moveTo(664, 92)
		py.click()

		time.sleep(2)
		print("VoiceOver successfully enabled.")

		time.sleep(1)
		print("Turning OFF VoiceOver...")

		time.sleep(2)
		py.moveTo(664, 92)
		py.click()

		time.sleep(2)
		print("VoiceOver successfully disabled.")

# Zoom
	@staticmethod
	def test_open_zoom_accessibility_settings():
		time.sleep(1)
		print("Opening Zoom tab...")

		time.sleep(2)
		py.moveTo(679, 166)
		py.click()

		time.sleep(2)
		print("Zoom tab successfully opened.")


	@staticmethod
	def test_toggle_zoom_settings_accessibility_settings():
		time.sleep(1)
		print("Turning ON keyboard shortcuts to zoom...")

		time.sleep(2)
		py.moveTo(668, 91)
		py.click()

		time.sleep(2)
		print("keyboard shortcuts to zoom successfully enabled.")

		time.sleep(1)
		print("Turning OFF keyboard shortcuts to zoom...")

		time.sleep(2)
		py.moveTo(668, 91)
		py.click()

		time.sleep(2)
		print("keyboard shortcuts to zoom successfully disabled.")


		# Trackpad gesture to zoom
		time.sleep(1)
		print("Turning ON trackpad gesture to zoom...")

		time.sleep(2)
		py.moveTo(668, 178)
		py.click()

		time.sleep(2)
		print("Trackpad gesture to zoom successfully enabled.")

		time.sleep(1)
		print("Turning OFF trackpad gesture to zoom...")

		time.sleep(2)
		py.moveTo(668, 178)
		py.click()

		time.sleep(2)
		print("Trackpad gesture to zoom successfully disabled.")


		# Scroll gesture with modifier keys to zoom
		time.sleep(1)
		print("Turning ON scroll gesture to zoom...")

		time.sleep(2)
		py.moveTo(668, 247)
		py.click()

		time.sleep(2)
		print("Scroll gesture to zoom successfully enabled.")

		time.sleep(1)
		print("Turning OFF scroll gesture to zoom...")

		time.sleep(2)
		py.moveTo(668, 247)
		py.click()

		time.sleep(2)
		print("Scroll gesture to zoom successfully disabled.")

		# Modifier key for scroll gesture
		time.sleep(1)
		print("Opening modifier key for scroll gesture drop down menu...")

		time.sleep(2)
		py.moveTo(671, 291)
		py.click()

		time.sleep(2)
		print("Modifier key for scroll gesture drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing modifier key for scroll gesture drop down menu...")

		time.sleep(2)
		py.moveTo(671, 291)
		py.click()

		time.sleep(2)
		print("Modifier key for scroll gesture drop down menu successfully collapsed.")

		# Zoom Style
		time.sleep(1)
		print("Opening zoom style drop down menu...")

		time.sleep(2)
		py.moveTo(545, 331)
		py.click()

		time.sleep(2)
		print("Zoom style drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing zoom style drop down menu...")

		time.sleep(2)
		py.moveTo(545, 331)
		py.click()

		time.sleep(2)
		print("Zoom style drop down menu successfully collapsed.")

		# Hover Text
		time.sleep(1)
		print("Turning ON Hover Text...")

		time.sleep(2)
		py.moveTo(649, 420)
		py.click()

		time.sleep(2)
		print("Hover Text successfully enabled.")

		time.sleep(1)
		print("Turning OFF Hover Text...")

		time.sleep(2)
		py.moveTo(649, 420)
		py.click()

		time.sleep(2)
		print("Hover Text successfully disabled.")

		# Touch Bar zoom
		time.sleep(1)
		print("Turning ON Touch Bar zoom...")

		time.sleep(2)
		py.moveTo(671, 484)
		py.click()

		time.sleep(2)
		print("Touch Bar zoom successfully enabled.")

		time.sleep(1)
		print("Turning OFF Touch Bar zoom...")

		time.sleep(2)
		py.moveTo(671, 484)
		py.click()

		time.sleep(2)
		print("Touch Bar zoom successfully disabled.")


# Display
	@staticmethod
	def test_open_display_accessibility_settings():
		time.sleep(1)
		print("Opening Display tab...")

		time.sleep(2)
		py.moveTo(681, 212)
		py.click()

		time.sleep(2)
		print("Display tab successfully opened.")


	@staticmethod
	def test_toggle_display_settings_accessibility_settings():
		time.sleep(1)
		print("Turning ON invert colors...")

		time.sleep(2)
		py.moveTo(669, 122)
		py.click()

		time.sleep(2)
		print("Invert colors successfully enabled.")

		time.sleep(1)
		print("Turning OFF invert colors...")

		time.sleep(2)
		py.moveTo(669, 122)
		py.click()

		time.sleep(2)
		print("Invert colors successfully disabled.")


		# Reduce motion
		time.sleep(1)
		print("Turning ON reduce motion...")

		time.sleep(2)
		py.moveTo(669, 201)
		py.click()

		time.sleep(2)
		print("Reduce motion successfully enabled.")

		time.sleep(1)
		print("Turning OFF reduce motion...")

		time.sleep(2)
		py.moveTo(669, 201)
		py.click()

		time.sleep(2)
		print("Reduce motion successfully disabled.")


		# Increase contrast
		time.sleep(1)
		print("Turning ON Increase contrast...")

		time.sleep(2)
		py.moveTo(669, 243)
		py.click()

		time.sleep(2)
		print("Increase contrast successfully enabled.")

		time.sleep(1)
		print("Turning OFF Increase contrast...")

		time.sleep(2)
		py.moveTo(669, 243)
		py.click()

		time.sleep(2)
		print("Increase contrast successfully disabled.")

		# Reduce transparency
		time.sleep(1)
		print("Turning ON reduce transparency...")

		time.sleep(2)
		py.moveTo(669, 284)
		py.click()

		time.sleep(2)
		print("Reduce transparency successfully enabled.")

		time.sleep(1)
		print("Turning OFF reduce transparency...")

		time.sleep(2)
		py.moveTo(669, 284)
		py.click()

		time.sleep(2)
		print("Reduce transparency successfully disabled.")

		# Differentiate without color
		time.sleep(1)
		print("Turning ON differentiate without color...")

		time.sleep(2)
		py.moveTo(669, 323)
		py.click()

		time.sleep(2)
		print("Differentiate without color successfully enabled.")

		time.sleep(1)
		print("Turning OFF differentiate without color...")

		time.sleep(2)
		py.moveTo(669, 323)
		py.click()

		time.sleep(2)
		print("Differentiate without color successfully disabled.")

		# Show window title icons
		time.sleep(1)
		print("Turning ON show window title icons...")

		time.sleep(2)
		py.moveTo(670, 362)
		py.click()

		time.sleep(2)
		print("Show window title icons successfully enabled.")

		time.sleep(1)
		print("Turning OFF show window title icons...")

		time.sleep(2)
		py.moveTo(670, 362)
		py.click()

		time.sleep(2)
		print("Show window title icons successfully disabled.")


		# Show toolbar button shapes
		time.sleep(1)
		print("Turning ON show toolbar button shapes...")

		time.sleep(2)
		py.moveTo(669, 311)
		py.click()

		time.sleep(2)
		print("Show toolbar button shapes successfully enabled.")

		time.sleep(1)
		print("Turning OFF show toolbar button shapes...")

		time.sleep(2)
		py.moveTo(669, 311)
		py.click()

		time.sleep(2)
		print("Show toolbar button shapes successfully disabled.")

		# Menu bar size
		time.sleep(1)
		print("Selecting Large for menu bar size...")

		time.sleep(2)
		py.moveTo(639, 448)
		py.click()

		time.sleep(2)
		print("Menu bar size successfully selected.")

		time.sleep(1)
		print("Changing menu bar size back to default...")

		time.sleep(2)
		py.moveTo(559, 448)
		py.click()

		time.sleep(2)
		print("Menu bar size successfully changed.")


		# Shake mouse pointer to locate
		time.sleep(1)
		print("Turning OFF shake mouse pointer to locate...")

		time.sleep(2)
		py.moveTo(669, 598)
		py.click()

		time.sleep(2)
		print("Shake mouse pointer to locate successfully disabled.")

		time.sleep(1)
		print("Turning ON shake mouse pointer to locate...")

		time.sleep(2)
		py.moveTo(669, 598)
		py.click()

		time.sleep(2)
		print("Shake mouse pointer to locate successfully enabled.")


# Spoken Content
	@staticmethod
	def test_open_spoken_content_accessibility_settings():
		time.sleep(1)
		print("Opening Spoken Content tab...")

		time.sleep(2)
		py.moveTo(679, 257)
		py.click()

		time.sleep(2)
		print("Spoken Content tab successfully opened.")


	@staticmethod
	def test_spoken_content_settings_accessibility_settings():
		time.sleep(1)
		print("Selecting system speech language drop down menu...")

		time.sleep(2)
		py.moveTo(649, 92)
		py.click()

		time.sleep(2)
		print("System speech language menu successfully selected.")

		time.sleep(1)
		print("Collapsing system speech language drop down menu...")

		time.sleep(2)
		py.moveTo(649, 92)
		py.click()

		time.sleep(2)
		print("System speech language menu successfully collapsed.")


		# Speak announcements
		time.sleep(1)
		print("Turning ON speak announcements...")

		time.sleep(2)
		py.moveTo(641, 304)
		py.click()

		time.sleep(2)
		print("Speak announcements successfully enabled.")

		time.sleep(1)
		print("Turning OFF speak announcements...")

		time.sleep(2)
		py.moveTo(641, 304)
		py.click()

		time.sleep(2)
		print("Speak announcements successfully disabled.")


		# Speak selection
		time.sleep(1)
		print("Turning ON speak selection...")

		time.sleep(2)
		py.moveTo(641, 345)
		py.click()

		time.sleep(2)
		print("Speak selection successfully enabled.")

		time.sleep(1)
		print("Turning OFF speak selection...")

		time.sleep(2)
		py.moveTo(641, 345)
		py.click()

		time.sleep(2)
		print("Speak selection successfully disabled.")


		# Speak item under pointer
		time.sleep(1)
		print("Turning ON speak item under pointer...")

		time.sleep(2)
		py.moveTo(641, 384)
		py.click()

		time.sleep(2)
		print("Speak item under pointer successfully enabled.")

		time.sleep(1)
		print("Turning OFF speak item under pointer...")

		time.sleep(2)
		py.moveTo(641, 384)
		py.click()

		time.sleep(2)
		print("Speak item under pointer successfully disabled.")


		# Speak typing feedback
		time.sleep(1)
		print("Turning ON speak typing feedback...")

		time.sleep(2)
		py.moveTo(641, 426)
		py.click()

		time.sleep(2)
		print("Speak typing feedback successfully enabled.")

		time.sleep(1)
		print("Turning OFF speak typing feedback...")

		time.sleep(2)
		py.moveTo(641, 426)
		py.click()

		time.sleep(2)
		print("Speak typing feedback successfully disabled.")


# Descriptions
	@staticmethod
	def test_open_descriptions_accessibility_settings():
		time.sleep(1)
		print("Opening descriptions tab...")

		time.sleep(2)
		py.moveTo(679, 299)
		py.click()

		time.sleep(2)
		print("Descriptions tab successfully opened.")


	@staticmethod
	def test_descriptions_settings_accessibility_settings():
		time.sleep(1)
		print("Turning ON audio descriptions when available...")

		time.sleep(2)
		py.moveTo(670, 90)
		py.click()

		time.sleep(2)
		print("Audio descriptions when available successfully enabled.")

		time.sleep(1)
		print("Turning OFF audio descriptions when available...")

		time.sleep(2)
		py.moveTo(670, 90)
		py.click()

		time.sleep(2)
		print("Audio descriptions when available successfully disabled.")


# Audio
	@staticmethod
	def test_open_audio_accessibility_settings():
		time.sleep(1)
		print("Opening audio tab...")

		time.sleep(2)
		py.moveTo(679, 399)
		py.click()

		time.sleep(2)
		print("Audio tab successfully opened.")
			

	@staticmethod
	def test_audio_settings_accessibility_settings():
		time.sleep(1)
		print("Turning ON screen flash when an alert sounds...")

		time.sleep(2)
		py.moveTo(670, 90)
		py.click()

		time.sleep(2)
		print("Screen flash when an alert sounds successfully enabled.")

		time.sleep(1)
		print("Turning OFF screen flash when an alert sounds...")

		time.sleep(2)
		py.moveTo(670, 90)
		py.click()

		time.sleep(2)
		print("Screen flash when an alert sounds successfully disabled.")

		# Play stereo audio as mono	
		time.sleep(1)
		print("Turning ON stereo audio as mono...")

		time.sleep(2)
		py.moveTo(670, 131)
		py.click()

		time.sleep(2)
		print("Stereo audio successfully enabled.")

		time.sleep(1)
		print("Turning OFF stereo audio as mono...")

		time.sleep(2)
		py.moveTo(670, 131)
		py.click()

		time.sleep(2)
		print("Stereo audio successfully disabled.")

		# Spatial audio follows head movements
		time.sleep(1)
		print("Turning OFF spatial audio...")

		time.sleep(2)
		py.moveTo(670, 173)
		py.click()

		time.sleep(2)
		print("Spatial audio successfully disabled.")

		time.sleep(1)
		print("Turning ON spatial audio...")

		time.sleep(2)
		py.moveTo(670, 173)
		py.click()

		time.sleep(2)
		print("Spatial audio successfully enabled.")

		# Background sounds
		time.sleep(1)
		print("Turning ON background sounds...")

		time.sleep(2)
		py.moveTo(670, 487)
		py.click()

		time.sleep(2)
		print("Background sounds successfully enabled.")

		time.sleep(1)
		print("Turning OFF background sounds...")

		time.sleep(2)
		py.moveTo(670, 487)
		py.click()

		time.sleep(2)
		print("Background sounds successfully disabled.")


# RTT
	@staticmethod
	def test_open_rtt_accessibility_settings():
		time.sleep(1)
		print("Opening RTT tab...")

		time.sleep(2)
		py.moveTo(679, 443)
		py.click()

		time.sleep(2)
		print("RTT tab successfully opened.")
			

	@staticmethod
	def test_rtt_settings_accessibility_settings():
		time.sleep(1)
		print("Turning ON RTT...")

		time.sleep(2)
		py.moveTo(670, 94)
		py.click()

		time.sleep(2)
		print("RTT successfully enabled.")

		time.sleep(1)
		print("Turning OFF RTT...")

		time.sleep(2)
		py.moveTo(670, 94)
		py.click()

		time.sleep(2)
		print("RTT successfully disabled.")

		# Send immediately
		time.sleep(1)
		print("Turning OFF send immediately...")

		time.sleep(2)
		py.moveTo(670, 143)
		py.click()

		time.sleep(2)
		print("Send immediately successfully disabled.")

		time.sleep(1)
		print("Turning ON stereo audio as mono...")

		time.sleep(2)
		py.moveTo(670, 143)
		py.click()

		time.sleep(2)
		print("Send immediately successfully enabled.")


# Captions
	@staticmethod
	def test_open_captions_accessibility_settings():
		time.sleep(1)
		print("Opening captions tab...")

		time.sleep(2)
		py.moveTo(679, 486)
		py.click()

		time.sleep(2)
		print("Captions tab successfully opened.")
			

	@staticmethod
	def test_captions_settings_accessibility_settings():
		time.sleep(1)
		print("Turning ON closed captions and SDH...")

		time.sleep(2)
		py.moveTo(670, 322)
		py.click()

		time.sleep(2)
		print("Closed captions and SDH successfully enabled.")

		time.sleep(1)
		print("Turning OFF closed captions and SDH...")

		time.sleep(2)
		py.moveTo(670, 322)
		py.click()

		time.sleep(2)
		print("Closed captions and SDH successfully disabled.")


# Live Captions
	@staticmethod
	def test_open_live_captions_accessibility_settings():
		time.sleep(1)
		print("Opening live captions tab...")

		time.sleep(2)
		py.moveTo(679, 527)
		py.click()

		time.sleep(2)
		print("Live captions tab successfully opened.")
			

	@staticmethod
	def test_live_captions_settings_accessibility_settings():
		time.sleep(1)
		print("Turning ON live captions...")

		time.sleep(2)
		py.moveTo(670, 95)
		py.click()

		time.sleep(2)
		print("Live captions successfully enabled.")

		time.sleep(1)
		print("Turning OFF live captions...")

		time.sleep(2)
		py.moveTo(670, 95)
		py.click()

		time.sleep(2)
		print("Live captions successfully disabled.")

		# Font family
		time.sleep(1)
		print("Opening font family drop down menu...")

		time.sleep(2)
		py.moveTo(671, 179)
		py.click()

		time.sleep(2)
		print("Font family drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing font family drop down menu...")

		time.sleep(2)
		py.moveTo(671, 179)
		py.click()

		time.sleep(2)
		print("Font family drop down menu successfully collapsed.")


		# Font color
		time.sleep(1)
		print("Opening font color drop down menu...")

		time.sleep(2)
		py.moveTo(671, 259)
		py.click()

		time.sleep(2)
		print("Font color drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing font color drop down menu...")

		time.sleep(2)
		py.moveTo(671, 259)
		py.click()

		time.sleep(2)
		print("Font color drop down menu successfully collapsed.")


		# Background color
		time.sleep(1)
		print("Opening background color drop down menu...")

		time.sleep(2)
		py.moveTo(671, 295)
		py.click()

		time.sleep(2)
		print("Background color drop down menu successfully opened.")

		time.sleep(1)
		print("Collapsing background color drop down menu...")

		time.sleep(2)
		py.moveTo(671, 295)
		py.click()

		time.sleep(2)
		print("Background color drop down menu successfully collapsed.")


		# Live captions in FaceTime
		time.sleep(1)
		print("Turning ON live captions in FaceTime...")

		time.sleep(2)
		py.moveTo(670, 391)
		py.click()

		time.sleep(2)
		print("Live captions in FaceTime successfully enabled.")

		time.sleep(1)
		print("Turning OFF live captions in FaceTime...")

		time.sleep(2)
		py.moveTo(670, 391)
		py.click()

		time.sleep(2)
		print("Live captions in FaceTime successfully disabled.")

# TODO: Voice Control
# Voice Control
	@staticmethod
	def test_open_voice_control_accessibility_settings():
		time.sleep(1)
		print("Opening voice control tab...")

		time.sleep(2)
		py.moveTo(679, 628)
		py.click()

		time.sleep(2)
		print("Voice control tab successfully opened.")

	@staticmethod
	def accessibilityTestSuite():
		print("===============================================================")
		print("===============================================================")

		print("Beginning Accessibility test suite...")

		print("===============================================================")
		print("===============================================================")

		i.setUp()
		i.test_open_voice_over_accessibility_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_voice_over_accessibility_settings()
		i.test_toggle_voice_over_accessibility_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_zoom_accessibility_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_zoom_accessibility_settings()
		i.test_toggle_zoom_settings_accessibility_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_display_accessibility_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_display_accessibility_settings()
		i.test_toggle_display_settings_accessibility_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_spoken_content_accessibility_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_spoken_content_accessibility_settings()
		i.test_spoken_content_settings_accessibility_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_descriptions_accessibility_settings()
		i.test_descriptions_settings_accessibility_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_audio_accessibility_settings()
		i.test_audio_settings_accessibility_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_rtt_accessibility_settings()
		i.test_rtt_settings_accessibility_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_captions_accessibility_settings()
		i.test_captions_settings_accessibility_settings()
		i.tearDown()

		print("===============================================================")

		i.setUp()
		i.test_open_live_captions_accessibility_settings()
		i.test_live_captions_settings_accessibility_settings()
		i.tearDown()

		print("===============================================================")
		print("===============================================================")

		print("Test suite completed.")

		print("===============================================================")
		print("===============================================================")
		return	






# =====================================================================
# Tests:
# i = Accessibility()


# print("===============================================================")
# print("===============================================================")

# print("Beginning test suite...")

# print("===============================================================")
# print("===============================================================")

# i.setUp()
# i.test_open_voice_over_accessibility_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_voice_over_accessibility_settings()
# i.test_toggle_voice_over_accessibility_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_zoom_accessibility_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_zoom_accessibility_settings()
# i.test_toggle_zoom_settings_accessibility_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_display_accessibility_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_display_accessibility_settings()
# i.test_toggle_display_settings_accessibility_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_spoken_content_accessibility_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_spoken_content_accessibility_settings()
# i.test_spoken_content_settings_accessibility_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_descriptions_accessibility_settings()
# i.test_descriptions_settings_accessibility_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_audio_accessibility_settings()
# i.test_audio_settings_accessibility_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_rtt_accessibility_settings()
# i.test_rtt_settings_accessibility_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_captions_accessibility_settings()
# i.test_captions_settings_accessibility_settings()
# i.tearDown()

# print("===============================================================")

# i.setUp()
# i.test_open_live_captions_accessibility_settings()
# i.test_live_captions_settings_accessibility_settings()
# i.tearDown()

# print("===============================================================")
# print("===============================================================")

# print("Test suite completed.")

# print("===============================================================")
# print("===============================================================")



