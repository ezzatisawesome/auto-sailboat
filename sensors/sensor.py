import serial
import RTIMU
import time

class sensor_data:
    def __init__(self, settings_file = "/home/pi/autoSailboat/sensors/RTIMULib", port='/dev/ttyACM0', baudrate=115200):
        self.settings_file = settings_file # settings file for IMU calibration values
        
        self.port = port # serial port communication
        self.baudrate = baudrate # serial port communication speed

        self.lat = 0 # latitude
        self.lng = 0 # longitude
        self.coordinates = (0,0)

    #function for intializing RTIMULib and getting fusion values
    def heading(self):
        settings = RTIMU.Settings(self.settings_file) #intializing RTIMULib
        imu = RTIMU.RTIMU(settings)
        imu.IMUInit()
        i = 0
        while i < 1: 
            if imu.IMURead():
                x, y, z = imu.getFusionData() #gets x, y, and z values of imu
                return ("%f,%f,%f" % (x,y,z)) #need to round values
                i += 1

    #all these functions are for calling sensor data from the arduino
    def connectArduino(self):
        self.ser = serial.Serial(self.port, self.baudrate) #begin connection to Arduino

    def callArduino(self):
        self.ser.flushInput()
        ser_bytes = self.ser.readline()
        self.parsed = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8")).split(',')
        while self.parsed[0] != '$$':
            self.ser.flushInput()
            ser_bytes = self.ser.readline()
            self.parsed = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8")).split(',')

    def latitude(self):
        if (self.parsed[6] == 'N'):
            self.lat = float(self.parsed[5])
        elif (self.parsed[6] == 'S'):
            self.lat = float('-'+self.parsed[5])
        #latitude = self.parsed[5] + ',' + self.parsed[6] #array value 5 and 6 for latitude and direction
        return self.lat/100
    
    def longitude(self):
        if (self.parsed[8] == 'E'):
            self.lng = float(self.parsed[7])
        elif (self.parsed[8] == 'W'):
            self.lng = float('-'+self.parsed[7])
        #longitude = self.parsed[7] + ',' + self.parsed[8] #array value 7 and 8 for longitude and direction
        return self.lng/100
    
    def coords(self):
        self.coordinates = (self.latitude(), self.longitude())
        return self.coordinates

    def windvane(self):
        return self.parsed[1] #array value 1 for windvane angle
    
    def endSerial(self):
        self.ser.close()
