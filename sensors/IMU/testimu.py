import sys
import time
import IMU_CALIB
import IMU
import madgwick
import micropython_fusion

MPU9250 = IMU.MPU9250()
calib = IMU_CALIB.IMU_CALIB()


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
        madgwick = madgwick.MadgwickAHRS(1/256, [1,0,0,0], 1)
        quaternion = madgwick.update(m, a, g)
        print(quaternion)
        time.sleep(2)
except KeyboardInterrupt:
    sys.exit()
