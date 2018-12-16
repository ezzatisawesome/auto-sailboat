import MPU9250
import smbus
import time
import math
import sys

#mpu9250 equals MPU9250 class
mpu9250 = MPU9250.MPU9250()

#function for converting raw magnetometer data to degrees
def raw_to_degrees(x, y):
	return math.atan2(y, x) * 180/math.pi

try:
	while True:
		mag = mpu9250.readMagnet()
		x = mag['x']  # the z
		y = mag['y']  # the y
		z = mag['z']  # the z
		print(raw_to_degrees(x, y)) #get input into raw_to_degrees function
		time.sleep(1)

except KeyboardInterrupt:
	sys.exit
