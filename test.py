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



from gpiozero import Servo
from time import sleep

f of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 250  # Min pulse length out of 4096
servo_max = 500  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    # Move servo on channel O between extremes.
    pwm.set_pwm(7, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(7, 0, servo_max)
    time.sleep(1)
