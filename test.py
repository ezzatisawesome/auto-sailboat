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

        #print("{:>.4f}  {:>.4f}  {:>.4f}" .format(accelx, accely, accelz))


        pitch = IMU_CALIB.pitch(accelx, accely, accelz)
        roll = IMU_CALIB.roll(accelx, accely, accelz)

        print("{:>.4f} {:>.4f}" .format(pitch, roll))

        time.sleep(2) # repeat two every seconds

except KeyboardInterrupt:
     sys.exit
