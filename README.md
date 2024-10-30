A smart home simulation system with components structured across various files for different functionalities:

main.py for device simulation logic, 

a Flask web server for web-based interaction(Flask app enables users to interact with the smart home system via a web interface. In app.py, main.py is imported to use its functionalities),

and a Tkinter-based GUI for real-time monitoring(The GUI provides a dynamic interface for monitoring the status of each smart home device. Since this interface requires real-time updates, it uses Tkinter’s after() method for refreshing device statuses).


This project defines an Automation System for a smart home, which includes smart lights, a thermostat, and a security camera.
The key components and functionalities are:
SmartLight can turn on/off, adjust brightness, and dim gradually, with a randomized state change feature.
Thermostat controls temperature, supports gradual temperature adjustments, and can toggle its state randomly.
SecurityCamera detects motion and changes its security status, with states like "Idle," "Alert," and "Recording."
AutomationSystem manages devices, runs a simulation, and logs actions across multiple iterations.
The run_simulation method randomly detects motion, alters device states, and adjusts lights automatically to simulate dynamic home automation.
