import sys
import time
from sensors.IMU import IMU_CALIB
from sensors.IMU import IMU
from sensors.IMU import madgwick

MPU9250 = IMU.MPU9250()
calib = IMU_CALIB.IMU_CALIB()
madgwick = madgwick.MadgwickAHRS()


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
        filter = madgwick.update_imu()
        mx = mag['x']
        my = (mag['y'])
        mz = mag['z']
        ax = accel['x']
        ay = accel['y']
        az = accel['z']
        gx = gyro['x']
        gy = gyro['y']
        gz = gyro['z']
        quaternion = filter([mx, my, mz], [ax, ay, az], [gx, gy, gz])
        print(filter.quaternion)
        time.sleep(2)
except KeyboardInterrupt:
    sys.exit()