import pytest
import subprocess
import time

TIME_LIMIT = 10

class TestWiFiFunction:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Fixture to setup and teardown test environment."""
        print("\nSetting up environment...")
        yield  # This is where the test runs
        print("Tearing down environment...")


    def test_is_wifi_ON(self):
        """Test if WiFi is ON."""

        output = subprocess.check_output(
            ["networksetup", "-getairportpower", "en0"], text=True
        ).strip()
        assert output == "Wi-Fi Power (en0): On"

    def test_is_wifi_OFF(self):
        """Test if WiFi is OFF."""

        output = subprocess.check_output(
            ["networksetup", "-getairportpower", "en0"], text=True
        ).strip()
        assert output == "Wi-Fi Power (en0): Off"

    def test_is_connected_to_wifi(self):
        """Test if WiFi is connected."""

        output = subprocess.check_output(
            ["networksetup", "-getinfo", "Wi-Fi"], text=True
        ).strip()
        assert "IP address:" in output

    def test_is_not_connected_to_wifi(self):
        """Test if WiFi is not connected."""

        output = subprocess.check_output(
            ["networksetup", "-getinfo", "Wi-Fi"], text=True
        ).strip()
        assert "IP address:" not in output

    def test_is_connected_to_ethernet(self):
        """Test if connected via Ethernet."""

        output = subprocess.check_output(
            ["networksetup", "-getinfo", "Thunderbolt\ Bridge"], text=True
        ).strip()
        assert "IP address:" in output

    def test_is_not_connected_to_ethernet(self):
        """Test if not connected via Ethernet."""

        output = subprocess.check_output(
            ["networksetup", "-getinfo", "Thunderbolt\ Bridge"], text=True
        ).strip()
        assert "IP address:" not in output

    def test_join_local_SSID(self):
        """Test if device can connect to a local SSID, and verifies if connected to SSID."""

        ssid = "INFINITYSTONES"
        password = "Friday237"

        subprocess.run(["networksetup", "-setairportnetwork", "en0", ssid, password])

        output = subprocess.check_output(
            ["networksetup", "-getairportnetwork", "en0"], text=True
        ).strip()
        assert ssid in output
