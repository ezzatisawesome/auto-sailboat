import IMU
import sys
import time
import IMU_CALIB

MPU9250 = IMU.MPU9250()
calib = IMU_CALIB.IMU_CALIB()
mag = MPU9250.readMagnet()
accel = MPU9250.readAccel()
north = calib.mag_tilt_comp()
try:
    while True:
        
        mx = mag['x']
        my = mag['y']
        mz = mag['z']
        ax = accel['x']
        ay = accel['y']
        az = accel['z']
        print(north(mx, my, mz, ax, ay, az))
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit()