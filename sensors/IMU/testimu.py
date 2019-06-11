import IMU
import sys
import time
import IMU_CALIB

MPU9250 = IMU.MPU9250()
calib = IMU_CALIB.IMU_CALIB()
mag = MPU9250.readMagnet()
accel = MPU9250.readAccel()

try:
    while True:
        mx = mag['x']
        my = mag['y']
        mz = mag['z']
        ax = accel['x']
        ay = accel['y']
        az = accel['z']
        print(mx)
        print(my)
        print(mz)
        north = calib.mag_tilt_comp(mx, my, mz, ax, ay, az)
        print(north)
        time.sleep(2)
except KeyboardInterrupt:
    sys.exit()