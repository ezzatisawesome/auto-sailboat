import RTIMU
import serial
import sys
import time
import math

class sensors:
    def __init__(self):
        #setup for accessing the IMU via the RTIMU library
        SETTINGS_FILE = "RTIMULib"
        s = RTIMU.Settings(SETTINGS_FILE)
        self.imu = RTIMU.RTIMU(s)

        #setup for access the Arduino and the encoder and GPS
        self.ser = serial.Serial('/dev/ttyACMO', 115200)

    def getHeading(self):
        if self.imu.IMURead():
            data = self.imu.getIMUData()
            fusionPose = data["fusionPose"]
            return(fusionPose[2])
    def getGPS(self):
        self.ser.write('2')
    def getEncoder(self):
        self.ser.write('1')
