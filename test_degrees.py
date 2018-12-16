import MPU9250
import smbus 
import time
import math
import sys

#mpu9250 equals MPU9250 class
mpu9250 = MPU9250.MPU9250()

#function for converting raw magnetometer data to degrees
def raw_to_degrees():
	heading = math.atan2(y, x) * 180/math.pi
