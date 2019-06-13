import sys
import time
import numpy as np
import IMU_CALIB
import IMU
from madgwick import MadgwickAHRS
import micropython_fusion
from quaternion import Quaternion


MPU9250 = IMU.MPU9250()
calib = IMU_CALIB.IMU_CALIB()

quat = Quaternion(1, 0, 0, 0)
madgwick = MadgwickAHRS(1/256, quat, 1)

"""
try:
    while True: 
        mag = MPU9250.readMagnet()
        accel = MPU9250.readAccel()
        mx = mag['x']
        my = (mag['y'])
        mz = mag['z']
        ax = accel['x']
        ay = accel['y']
        az = accel['z']
        print(calib.mag_tilt_comp(mx, my, mz, ax, ay, az))
        time.sleep(2)
except KeyboardInterrupt:
    sys.exit()
"""

try:
    while True: 
        mag = MPU9250.readMagnet()
        accel = MPU9250.readAccel()
        gyro = MPU9250.readGyro()
        mx = mag['x']
        my = (mag['y'])
        mz = mag['z']
        ax = accel['x']
        ay = accel['y']
        az = accel['z']
        gx = gyro['x']
        gy = gyro['y']
        gz = gyro['z']
        m = [mx, my, mz]
        a = [ax, ay, az]
        g = [gx, gy, gz]
        
        north = madgwick.update(m, a, g)
        north = Quaternion.to_euler_angles(north)
        
        print(north)
        
        time.sleep(2)
except KeyboardInterrupt:
    sys.exit()
