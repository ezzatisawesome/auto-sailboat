import MPU9250
import time
import math
import sys

mpu9250 = MPU9250.MPU9250() #MPU9250 class
mag = mpu9250.readMagnet() #readMagnet method

try:
    while True:
        print(mag['x'])   
        print(mag['y'])
        print(mag['z'], "\n")
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit()