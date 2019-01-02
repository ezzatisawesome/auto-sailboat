import IMU_CALIB
import MPU9250
import sys
import time

mpu9250 = MPU9250.MPU9250()
IMU_CALIB = IMU_CALIB.IMU_CALIB()

try:
     while True:
          mag = mpu9250.readMagnet() #read magnetometer
          accel = mpu9250.readAccel() #read accelerometer
          
          magx = mag['x'] #x mag value
          magy = mag['y'] #y mag value
          magz = mag['z'] #z mag value
          
          accelx = accel['x'] #x mag value
          accely = accel['y'] #y mag value
          accelz = accel['z'] #z mag value
          
          #pitch = IMU_CALIB.pitch(accelx, accely, accelz) #creating instance of pitch method in IMU_CALIB lib
          #roll = IMU_CALIB.roll(accelx, accely, accelz) #creating instance of roll method in IMU_CALIB lib


          calibrated_x = IMU_CALIB.mag_calibration(magx, 22.33, 0.944)
          calibrated_y = IMU_CALIB.mag_calibration(magy, 30.577, 1.037)
          calibrated_z = IMU_CALIB.mag_calibration(magz, 9.071, 0.972)
          tiltcomp_heading = IMU_CALIB.mag_tilt_comp(calibrated_x, calibrated_y, calibrated_z, accelx, accely, accelz) #creating instance of tilt compensation method in IMU_CALIB lib

          print("{:>.3f}" .format(tiltcomp_heading))

          time.sleep(2) #repeat two every seconds

except KeyboardInterrupt:
     sys.exit
