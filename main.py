from sensors.sensor import sensor_data 
from autonomous.waypoint import waypoints
from autonomous.PID import PID
import time
import signal
import RPi.GPIO as GPIO

wp = waypoints() #create instance of waypoints class
sensors = sensor_data() #create instance of sensor_data class

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

sensors.connectArduino() # establish connection to arduino

p = 1.0
i = 0.5
d = 0.3
pid = PID(p, i, d)
pid.clear()
pid.setpoint(0)

user_on = True

try:
    while user_on:
        heading = sensors.heading()
        beta = pid.update(heading)
        print(beta)


        
except KeyboardInterrupt:
    print("\ninterrupt: cutting arduino connection and stopping program")
finally:
   sensors.endSerial()
