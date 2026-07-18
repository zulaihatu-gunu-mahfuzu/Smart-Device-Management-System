# Parent Class
class SmartDevice:
    def __init__(self, name, device_id):
        self.name = name
        self.__device_id = device_id
        self.__power_status = False

    # Getter and Setter for device ID
    @property
    def device_id(self):
        return self.__device_id

    @device_id.setter
    def device_id(self, value):
        if value != "":
            self.__device_id = value
        else:
            print("Device ID cannot be empty.")

    # Getter for power status
    @property
    def power_status(self):
        return self.__power_status

    def turn_on(self):
        self.__power_status = True
        print(self.name, "is now ON.")

    def turn_off(self):
        self.__power_status = False
        print(self.name, "is now OFF.")

    def display_info(self):
        print("\nDevice Name:", self.name)
        print("Device ID:", self.__device_id)
        print("Power Status:", "ON" if self.__power_status else "OFF")

# Child Class 1
class TemperatureSensor(SmartDevice):
    def __init__(self, name, device_id, temperature):
        super().init(name, device_id)
        self.temperature = temperature

    def read_temperature(self):
        print("Temperature:", self.temperature, "°C")

# Child Class 2
class SmartLight(SmartDevice):
    def __init__(self, name, device_id, brightness):
        super().init(name, device_id)

        if 0 <= brightness <= 100:
            self.brightness = brightness
        else:
            self.brightness = 50

    def increase_brightness(self):
        if self.brightness < 100:
            self.brightness += 10
        print("Brightness:", self.brightness)

    def decrease_brightness(self):
        if self.brightness > 0:
            self.brightness -= 10
        print("Brightness:", self.brightness)

# Child Class 3
class SecurityCamera(SmartDevice):
    def __init__(self, name, device_id):
        super().init(name, device_id)
        self.recording_status = False

    def start_recording(self):
        self.recording_status = True
        print("Recording Started.")
    def stop_recording(self):
        self.recording_status = False
        print("Recording Stopped.")

Create Objects
sensor = TemperatureSensor("Living Room 
Sensor", "TS001", 26)
light = SmartLight("Bedroom Light", "SL001", 50)
camera = SecurityCamera("Front Door Camera", "SC001")

# Menu
while True:
    print("\n===== Smart Device Management System =====")
    print("1. Display Device Information")
    print("2. Turn Devices ON")
    print("2. Turn Devices ON")
    print("3. Turn Devices OFF")
    print("4. Read Temperature")
    print("5. Adjust Brightness")
    print("6. Start Recording")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sensor.display_info()
        light.display_info()
        camera.display_info()

    elif choice == "2":
        sensor.turn_on()
        light.turn_on()
        camera.turn_on()

    elif choice == "3":
        sensor.turn_off()
        light.turn_off()
        camera.turn_off()

    elif choice == "4":
        sensor.read_temperature()

    elif choice == "5":
        print("1. Increase Brightness")
        print("2. Decrease Brightness")
        option = input("Choose: ")

    if option == "1":

light.increase_brightness()
        elif option == "2":
l
ight.decrease_brightness()
       else:
           print("Invalid option.")

    elif choice == "6":
        camera.start_recording()

    elif choice == "7":
        print("Program Ended.")
        break

    else:
        print("Invalid choice.")
