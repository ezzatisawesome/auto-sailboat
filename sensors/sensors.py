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
        self.ser = serial.Serial('/dev/ttyACM0', 115200)

    def getHeading(self):
        '''
        if self.imu.IMURead():
            data = self.imu.getIMUData()
            fusionPose = data["fusionPose"]
            return(fusionPose[2])
        '''
        '''
        data = self.imu.getIMUData()
        fusionPose = data["fusionPose"]
        return(fusionPose[2])
        '''
        while True:
            if self.imu.IMURead():
                # x, y, z = imu.getFusionData()
                # print("%f %f %f" % (x,y,z))
                data = self.imu.getIMUData()
                fusionPose = data["fusionPose"]
                print("r: %f p: %f y: %f" % (math.degrees(fusionPose[0]), 
                    math.degrees(fusionPose[1]), math.degrees(fusionPose[2])))
                time.sleep(poll_interval*1.0/1000.0)
    def fusionParameters(self):
        self.imu.setSlerpPower(0.02)
        self.imu.setGyroEnable(True)
        self.imu.setAccelEnable(True)
        self.imu.setCompassEnable(True)

    def getGPS(self):
        self.ser.write('2')
    def getEncoder(self):
        self.ser.write('1')
