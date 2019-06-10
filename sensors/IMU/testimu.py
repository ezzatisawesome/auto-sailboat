from IMU import MPU9250
import sys
import time

try:
    while True:
        mag = MPU9250.readMagnet()
        print(" mx = " , ( mag['x'] ))
        print(" my = " , ( mag['y'] ))
        print(" mz = " , ( mag['z'] ))
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit()