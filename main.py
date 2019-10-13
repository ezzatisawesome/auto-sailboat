from sensors.sensor import sensor_data
import RTIMU
import Adafruit_PCA9685

sensors = sensor_data() #wind and gps sensor data collection library
pwm = Adafruit_PCA9685.PCA9685() #servo driver library


SETTINGS_FILE = "RTIMULib"
                                    #initializing RTIMULib--a library for the IMU
s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

#loop

try:
    while True:
        pass

except KeyboardInterrupt:
    print("Stopping program")

finally:
    sensors.endSerial()
