import IMU
import sys
import time

MPU9250 = IMU.MPU9250()

try:
    while True:
        mag = MPU9250.readMagnet()
        print(" mx = " , ( mag['x'] ))
        print(" my = " , ( mag['y'] ))
        print(" mz = " , ( mag['z'] ))
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit()