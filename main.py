from sensors.sensor import sensor_data
from waypoint import waypoints
import time
import signal

wp = waypoints()
sensors = sensor_data()

sensors.connectArduino()

user_on = True

try:
    while user_on:
        sensors.callArduino()
        print(str(sensors.latitude())+','+str(sensors.longitude()))
        print(sensors.windvane())
        print(sensors.heading())
        time.sleep(3)
except KeyboardInterrupt:
    print("\ninterrupt: cutting arduino connection and stopping program")
finally:
    sensors.endSerial()
