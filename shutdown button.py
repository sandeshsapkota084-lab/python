class Device:
    def __init__(self, device_id):
        self.device_id = device_id
        self.is_on = True
    def shutdown(self):
        if self.is_on:
            print(f"Device {self.device_id} shutting down")
            self.is_on = False
            return True
        else:
            print(f"Device {self.device_id} is already off")
            return False
    def is_shutdown(self):
        """Check if device is actually off"""
        return not self.is_on

class Controller:
    def __init__(self, devices):
        self.devices = devices
    def shutdown_all(self):
        print("Single button pressed: shutting down all devices")
        shutdown_successful = 0
        already_off = 0
        for device in self.devices:
            was_shutdown = device.shutdown()
            if was_shutdown:
                shutdown_successful += 1
            else:
                already_off += 1
        all_verified_off = all(not device.is_on for device in self.devices)
        print(f"\n--- Shutdown Summary ---")
        print(f"Devices shut down: {shutdown_successful}")
        print(f"Devices already off: {already_off}")
        print(f"Total devices: {len(self.devices)}")
        print(f"All devices verified OFF: {all_verified_off}")
        return all_verified_off

if __name__ == "__main__":
    devices = [Device(i) for i in range(1, 51)]
    controller = Controller(devices)
    result = controller.shutdown_all()
    if result:
        print("\n SUCCESS: All devices have been shut down!")
    else:
        print("\n ERROR: Some devices failed to shutdown!")