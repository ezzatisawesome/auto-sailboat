import MPU9250 
import time
import math

class calibrating:
    #mpu9250 = MPU9250 class
    mpu9250 = MPU9250.MPU9250()
    
    x = mag['x']  # the z
	y = mag['y']  # the y
	z = mag['z']  # the z

    def calibration():

        return 
    def raw_to_degrees(x, y):
	    return math.atan2(y, x) * 180/math.pi
