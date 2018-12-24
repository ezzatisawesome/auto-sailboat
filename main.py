import MPU9250
import IMU_CALIB
import sys
import time

mpu9250 = MPU9250.MPU9250()
calib = IMU_CALIB.calib()

try:
     while True:
        mag = mpu9250.readMagnet()
        
        x = mag['x'] #x mag value
        y = mag['y'] #y mag value
        z = mag['z'] #z mag value

        heading = calib.heading(x, y)

        print(heading)
        
        time.sleep(1) #repeat every second

except KeyboardInterrupt:
     sys.exit
