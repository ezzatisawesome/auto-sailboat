from sensors.sensor import sensor_data
from gpiozero import Servo
from math import *
from time import sleep

sensor = sensor_data()
sensor.connectArduino()

servo = Servo(17)

pre_scale = 0

def sail_control(sail_angle):
    r = cos(sail_angle)
    return r
    

try:
    while True:
        sensor.callArduino()
        wind_angle = float(sensor.windvane())
        
        print(wind_angle)

        scale = round(sail_control(wind_angle), 3)

        servo.value = scale
        
        print("Scale:"+str(scale))    
    


except KeyboardInterrupt:
    print("\ninterrupt: cutting arduino connection and stopping program")
finally:
    sensor.endSerial()
