import IMU_CALIB
import MPU9250
import sys
import time

MPU9250 = MPU9250.MPU9250()
IMU_CALIB = IMU_CALIB.IMU_CALIB()

try:
     while True:
        mag = MPU9250.readMagnet()
        accel = MPU9250.readAccel()
        
        magx = mag['x'] # x mag value
        magy = mag['y'] # y mag value
        magz = mag['z'] # z mag value

        accelx = accel['x'] # x mag value
        accely = accel['y'] # y mag value
        accelz = accel['z'] # z mag value

        pitch = IMU_CALIB.pitch(accelx, accely, accelz)
        roll = IMU_CALIB.roll(accelx, accely, accelz)

        print("{:>.4f} {:>.4f}" .format(pitch(accelx, accely, accelz), roll(accelx, accely, accelz)))

        #print("{:>.3f}  {:>.3f}  {:>.3f}" .format(x, y, z)

        time.sleep(2) # repeat every second

except KeyboardInterrupt:
     sys.exit
