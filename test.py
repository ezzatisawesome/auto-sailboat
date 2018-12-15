import MPU9250
import smbus
import time
import math
import sys

mpu9250 = MPU9250.MPU9250()

try:
	while True:
		mag = mpu9250.readMagnet()
		print(mag['x'])
		print(mag['y'])
		print(mag['z'], '\n')
		time.sleep(1)

except KeyboardInterrupt:
	sys.exit


