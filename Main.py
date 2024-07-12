import random
import time

#Self refers to the current instance of the class.

class SmartLight:
    def __init__(self, device_id):
        self.device_id = device_id #attribute
        self.status = False  # off by default
        self.brightness = 0  # brightness level (0-100)

    def turn_on(self):
        self.status = True #True corresponds to LIGHT ON
        print(f"SmartLight {self.device_id} turned on.")

    def turn_off(self):
        self.status = False#False corresponds to LIGHT OFF 
        print(f"SmartLight {self.device_id} turned off.")

    def set_brightness(self, brightness):
        self.brightness = brightness
        print(f"SmartLight {self.device_id} brightness set to {brightness}.")

    def gradual_dimming(self, target_brightness, steps=10, delay_seconds=0.1):
        if self.status:
            current_brightness = self.brightness
            brightness_step = (target_brightness - current_brightness) / steps#e.g (15 - 10) / 10= 0.5(calculated step size)

            for _ in range(steps):#over 10 steps, the brightness level will change by 0.5 units in each step. In other words, the 
                current_brightness += brightness_step
                self.set_brightness(int(current_brightness))#brightness will gradually increase or decrease in 0.5-unit increments over the specified number of steps.

                time.sleep(delay_seconds)# time.sleep(seconds) function in Python is used to pause the execution of a program for a specified number of seconds. It's part of the time module. 

    def randomize_state(self):
        if random.choice([True, False]):  # 50% chance of changing state,,,if TRUE execute code inside ,,if FALSE dO nothing
            if self.status:#If status is TRUE change to OFF
                self.turn_off()
            else:#If status is FALSE change to ON
                self.turn_on()

            new_brightness = random.randint(0, 100)
            self.gradual_dimming(new_brightness)



class Thermostat:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False  # off by default
        self.temperature = 20  # default temperature in Celsius

    def turn_on(self):
        self.status = True
        print(f"Thermostat {self.device_id} turned on.")

    def turn_off(self):
        self.status = False
        print(f"Thermostat {self.device_id} turned off.")

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Thermostat {self.device_id} temperature set to {temperature}°C.")

    def gradual_temperature_change(self, target_temperature, steps=10, delay_seconds=0.1):
        current_temperature = self.temperature
        temperature_step = (target_temperature - current_temperature) / steps

        for _ in range(steps):
            current_temperature += temperature_step
            self.set_temperature(round(current_temperature, 2))  # Round to 2 decimal places for precision
            time.sleep(delay_seconds)

    def randomize_state(self):
        if random.choice([True, False]):  # 50% chance of changing state
            if self.status:
                self.turn_off()
            else:
                self.turn_on()

            new_temperature = random.uniform(15, 25)  # Simulating a temperature range
            self.gradual_temperature_change(new_temperature)



class SecurityCamera:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False  # off by default
        self.security_status = "Idle"

    def turn_on(self):
        self.status = True
        print(f"SecurityCamera {self.device_id} turned on.")

    def turn_off(self):
        self.status = False
        print(f"SecurityCamera {self.device_id} turned off.")

    def set_security_status(self, status):
        self.security_status = status
        print(f"SecurityCamera {self.device_id} security status set to {status}.")



    def detect_motion(self):
        if random.choice([True, False]):
            print(f"Motion detected by {self.device_id}!")
            self.security_status = "Alert"
        else:
            print(f"No motion detected by {self.device_id}.")
            self.security_status = "Idle"

    def randomize_state(self):
        if random.choice([True, False]):  
            if self.status:
                self.turn_off()
            else:
                self.turn_on()

            new_security_status = random.choice(["Idle", "Recording", "Alert"])
            self.set_security_status(new_security_status)
                        #Idle State: The camera is powered ON but not actively recording or monitoring.

            #Alert State: The camera transitions to an "alert" state when it detects a significant event, such as unexpected motion or a breach of a predefined security zone. In this state, the camera may start recording, activate alarms, or take other actions to draw attention to the detected activity.

            #Recording State: After entering the "alert" state, the camera may initiate a recording state. During this state, the camera actively captures and stores video footage, providing a record of the event that triggered the alert.
            
class AutomationSystem:
    def __init__(self):
        self.devices = []#devices attribute,,,,but we don't define it using the constructor
        self.simulation_output = []  # Initialize an empty list for simulation output
    def discover_device(self, device):
        self.devices.append(device)
        print(f"Discovered device: {device.device_id}")

    def add_device(self, device):
        if device not in self.devices:
            self.devices.append(device)
            print(f"Added device: {device.device_id} to the system.")

    def run_simulation(self, num_iterations=5, interval_seconds=3):#This method is responsible for running a simulation of the automation system.
        #num_iterations: The number of iterations the simulation should run. Default is set to 5.
#interval_seconds: The time interval (in seconds) between each iteration of the simulation. Default is set to 3 seconds.
        for _ in range(num_iterations):
            print("Simulation iteration:", _ + 1)

            if random.choice([True, False]):
                print("Motion detected!")
                # Trigger the automation rule to turn on lights
                light_devices = [device for device in self.devices if isinstance(device, SmartLight)]
                for light_device in light_devices:
                    light_device.turn_on()

                    
            for device in self.devices:
                device.randomize_state()#expected to simulate changes in the state of the current device.

             # Collect and display simulation output
            iteration_output = f"Simulation iteration: {_ + 1}\n"
            for device in self.devices:
                iteration_output += f"{type(device).__name__} {device.device_id} "
                iteration_output += f"turned {'on' if device.status else 'off'}.\n"

            self.simulation_output.append(iteration_output)
            print("--------------------")
            time.sleep(interval_seconds)#, causing the simulation to pause for a certain duration before moving to the next iteration.
#The purpose is to simulate the passage of time and the dynamic behavior of the devices in the automation system.

# # Example usage:
# automation_system = AutomationSystem()

# light1 = SmartLight(device_id="L1")
# thermostat1 = Thermostat(device_id="T1")
# camera1 = SecurityCamera(device_id="C1")

# automation_system.discover_device(light1)
# automation_system.discover_device(thermostat1)
# automation_system.discover_device(camera1)

# automation_system.run_simulation(num_iterations=5, interval_seconds=3)
