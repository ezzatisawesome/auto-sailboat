import IMU_CALIB
import MPU9250
import sys
import time

mpu9250 = MPU9250.MPU9250()
IMU_CALIB = IMU_CALIB.IMU_CALIB()

try:
     while True:
        mag = mpu9250.readMagnet()
        accel = mpu9250.readAccel()
        
        magx = mag['x'] # x mag value
        magy = mag['y'] # y mag value
        magz = mag['z'] # z mag value

        accelx = accel['x'] # x mag value
        accely = accel['y'] # y mag value
        accelz = accel['z'] # z mag value

        norm = IMU_CALIB.pitch_roll(accelx, accely, accelz)

        print("{:}" .format(IMU_CALIB.pitch_roll(accelx, accely, accelz)))

        #print("{:>.3f}  {:>.3f}  {:>.3f}" .format(x, y, z)

        time.sleep(2) # repeat every second

except KeyboardInterrupt:
     sys.exit
