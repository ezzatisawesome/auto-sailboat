import MPU9250
import smbus
import time
import math
import sys

mpu9250 = MPU9250.MPU9250()

try:
	while True:
		mag = mpu9250.readMagnet()
		x = mag['x']  # the z
		y = mag['y']  # the y
		z = mag['z']  # the z
		# print(mag['x'])
		# print(mag['y'])
		# print(mag['z'], '\n')
		print("x: {:<10} y: {:<10} z: {:<10}".format(x, y, z))
		time.sleep(1)

except KeyboardInterrupt:
	sys.exit


