import pytest
import subprocess

class TestBluetoothFunction:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Fixture to setup and teardown test environment."""

        print("\nSetting up Bluetooth test environment...")
        yield  # This is where the test runs
        print("Tearing down Bluetooth test environment...")

        

    def test_is_bluetooth_on(self):
        """Test if Bluetooth is turned ON."""

        output = subprocess.run(["blueutil", "--power", "1"])
        assert output == "1", "Bluetooth is not ON"

    def test_is_bluetooth_off(self):
        """Test if Bluetooth is turned OFF."""

        output = subprocess.run(["blueutil", "--power", "0"])
        assert output == "0", "Bluetooth is not OFF"

    def test_is_any_bluetooth_device_connected(self):
        """Test if any Bluetooth device is connected."""

        output = subprocess.check_output(
            ["blueutil", "connected"], text=True
        )
        assert "connected" in output, "No Bluetooth devices are connected"

    def test_connect_to_bluetooth_device(self):
        """Test connecting to a Bluetooth device (replace with actual MAC address)."""

        device_mac = "XX:XX:XX:XX:XX:XX"  # Replace with actual device MAC
        result = subprocess.run(["blueutil", "--connect", device_mac], capture_output=True, text=True)
        assert result.returncode == 0, f"Failed to connect to {device_mac}"

    def test_disconnect_from_bluetooth_device(self):
        """Test disconnecting from a Bluetooth device."""

        device_mac = "XX:XX:XX:XX:XX:XX"  # Replace with actual device MAC
        result = subprocess.run(["blueutil", "--disconnect", device_mac], capture_output=True, text=True)
        assert result.returncode == 0, f"Failed to disconnect from {device_mac}"
 