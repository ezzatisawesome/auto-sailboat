from MPU9250 import MPU9250
import time
import sys


try:
    while True:
        accel = MPU9250.readAccel(self)
        print(" ax = " , ( accel['x'] ))
        print(" ay = " , ( accel['y'] ))
        print(" az = " , ( accel['z'] ))

        gyro = MPU9250.readGyro(self)
        print(" gx = " , ( gyro['x'] ))
        print(" gy = " , ( gyro['y'] ))
        print(" gz = " , ( gyro['z'] ))

        mag = MPU9250.readMagnet(self)
        print(" mx = " , ( mag['x'] ))
        print(" my = " , ( mag['y'] ))
        print(" mz = " , ( mag['z'] ))

        time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()
