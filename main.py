from sensors.sensor import sensor_data 
from autonomous.waypoint import waypoints
import time
import signal

wp = waypoints() #create instance of waypoints class
sensors = sensor_data() #create instance of sensor_data class

sensors.connectArduino() # establish connection to arduino

user_on = True
test_coordinate = (42.324988, -87.845216)
test2 = (42.324958, -87.841385)

try:
    while user_on:
        heading = sensors.heading()
        sensors.callArduino()
        position = sensors.coords()
        wp.modifyWp(0, test2)
        wp.modifyWp(1, test_coordinate)
        distance = wp.haversine(0, 1)
        angle = wp.cal_bearing(0, 1)
        print(distance)
        print(angle)


        
except KeyboardInterrupt:
    print("\ninterrupt: cutting arduino connection and stopping program")
finally:
   sensors.endSerial()
