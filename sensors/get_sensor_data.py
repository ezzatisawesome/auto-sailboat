import comm_arduino
import RTIMU
import time
import math

SETTINGS_FILE = "RTIMULib"

print("Using settings file " + SETTINGS_FILE + ".ini")
if not os.path.exists(SETTINGS_FILE + ".ini"):
  print("Settings file does not exist--one will be created")

s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

if (not imu.IMUInit()):
    print("IMU Init Failed")
    sys.exit(1)
else:
    print("IMU Init Succeeded")

imu.setSlerpPower(0.02)
imu.setGyroEnable(True)
imu.setAccelEnable(True)
imu.setCompassEnable(True)

poll_interval = imu.IMUGetPollInterval()

def heading():
    pass


""""
import serial


ser = serial.Serial('/dev/ttyACM0', 115200)
while 1:
    if(ser.in_waiting > 0):
        line = ser.readline()
        print(line)


class comm_arduino:
    def __init__(com = '/dev/ttyACMO', baud_rate = 115200):
        self.ser = serial.Serial(com, baud_rate)
    def getEncoder(self):
        self.ser.write('1')
        return self.ser.readline()
    def getGPS(self):
        pass
    def getEncoderGPS(self):
        pass
    def close():
        self.ser.close()
