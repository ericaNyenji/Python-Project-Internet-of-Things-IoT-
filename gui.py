import tkinter as tk
from tkinter import ttk
import random
import time
import threading
from queue import Queue
from main import AutomationSystem, SmartLight, SecurityCamera, Thermostat

def run_simulation(automation_system, queue):
    for _ in range(5):
        automation_system.run_simulation()
        time.sleep(3)  # Add a delay to simulate the interval between iterations
        queue.put(automation_system.simulation_output)  # Put the output in the queue

class MonitoringDashboard:
    def __init__(self, automation_system, update_interval=1000):#default value is 1000 milliseconds
        self.automation_system = automation_system
        self.update_interval = update_interval

        self.root = tk.Tk()#root attribute which represents the main Tkinter window
        self.root.title("Smart Home Monitoring Dashboard")

        self.device_status_vars = []#stores StringVar variables for each device. >>used dynamically update the text in the GUI based on the state of the devices.
        self.device_properties_vars = []

        self.create_device_widgets()#call the methods
        self.create_controls()
        self.create_console()

    def create_device_widgets(self):
        for i, device in enumerate(self.automation_system.devices):
            frame = ttk.Frame(self.root, padding="10")#For each device, it creates a new ttk.Frame named frame with padding.
            frame.grid(row=i + 1, column=1, padx=10, pady=10)# it's position in the grid

            device_status_var = tk.StringVar()#store the status information
            device_properties_var = tk.StringVar()#store the properties information

            self.device_status_vars.append(device_status_var)#append
            self.device_properties_vars.append(device_properties_var)

            ttk.Label(frame, text=f"{device.device_id} Status:").grid(column=1, row=1, sticky="w")#displaying the device's status.
            ttk.Label(frame, textvariable=device_status_var).grid(column=2, row=1, sticky="w")

            ttk.Label(frame, text=f"{device.device_id} Properties:").grid(column=1, row=2, sticky="w")#displaying the device's properties.
            ttk.Label(frame, textvariable=device_properties_var).grid(column=2, row=2, sticky="w")

    def create_controls(self):#the buttons are arranged in a grid within the control_frame.
        control_frame = ttk.Frame(self.root, padding="10")# creates a frame (control_frame) on the GUI to hold the toggle buttons
        control_frame.grid(row=1, column=2, padx=10, pady=10)

        for i, device in enumerate(self.automation_system.devices):
            ttk.Button(
                control_frame,
                text=f"Toggle {device.device_id} ON/OFF",
                command=lambda dev=device: self.toggle_device(dev)#creates a ttk.Button for each device,,,dev is the current device.
            ).grid(column=1, row=i, pady=5)
# Add a button to manually trigger motion detection
        ttk.Button(
            control_frame,
            text="Detect Motion",
            command=self.detect_motion
        ).grid(column=1, row=len(self.automation_system.devices), pady=10)

    def create_console(self):
        console_frame = ttk.Frame(self.root, padding="10")#creates a ttk.Frame with padding and places it on the GUI
        console_frame.grid(row=len(self.automation_system.devices) + 2, columnspan=2, padx=10, pady=10) #The row for console_frame is calculated based on the length of self.automation_system.devices.

        self.console_text = tk.Text(console_frame, height=10, width=50)#Inside console_frame, a tk.Text widget named self.console_text
        self.console_text.grid(row=1, column=1, padx=5, pady=5)#It's position in the grid

    def toggle_device(self, device):# to handle turning the devices ON or OFF based on their current state
        if isinstance(device, SmartLight):
            device.turn_on() if not device.status else device.turn_off()
        elif isinstance(device, Thermostat):
            device.turn_on() if not device.status else device.turn_off()
        elif isinstance(device, SecurityCamera):
            device.turn_on() if not device.status else device.turn_off()
    def detect_motion(self):
        # Manually trigger motion detection
        for device in self.automation_system.devices:
            if isinstance(device, SecurityCamera):
                device.detect_motion()

    def update_dashboard(self):#ensures that the GUI reflects the current status and properties of each device in the automation system.
        for i, device in enumerate(self.automation_system.devices):# iterates through each device in self.automation_system.devices.
            device_status_var = self.device_status_vars[i]#sets the device_status_var to the current status of the device.
            device_properties_var = self.device_properties_vars[i]

            device_status_var.set(device.status)
            if isinstance(device, SmartLight):
                device_properties_var.set(f"Brightness: {device.brightness}")
            elif isinstance(device, Thermostat):
                device_properties_var.set(f"Temperature: {device.temperature}")
            elif isinstance(device, SecurityCamera):
                device_properties_var.set(f"Security Status: {device.security_status}")

        # Get the simulation output from the queue
        while not self.queue.empty():
            output = self.queue.get()
            self.console_text.delete(1.0, tk.END)  # Clear existing text
            self.console_text.insert(tk.END, output)

        # Schedule the next update
        self.root.after(self.update_interval, self.update_dashboard)

    def run(self):
        # Create a queue for communication between threads
        self.queue = Queue()

        # Start a separate thread for the simulation loop
        simulation_thread = threading.Thread(target=run_simulation, args=(self.automation_system, self.queue))
        simulation_thread.start()

        # Schedule the initial update
        self.root.after(0, self.update_dashboard)
        self.root.mainloop()

# Example usage:

# Create an AutomationSystem instance
automation_system = AutomationSystem()

light1 = SmartLight(device_id="SmartLight")
thermostat1 = Thermostat(device_id="Thermostat")
camera1 = SecurityCamera(device_id="Security Camera")

automation_system.discover_device(light1)
automation_system.discover_device(thermostat1)
automation_system.discover_device(camera1)

# Create a MonitoringDashboard instance
dashboard = MonitoringDashboard(automation_system)

# Run the GUI
dashboard.run()
