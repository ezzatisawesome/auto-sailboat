from IMU import MPU9250
import sys

try:
    while True:
        mag = MP9250.readMagnet()
        print(" mx = " , ( mag['x'] ))
        print(" my = " , ( mag['y'] ))
        print(" mz = " , ( mag['z'] ))
except KeyboardInterrupt:
    sys.exit()