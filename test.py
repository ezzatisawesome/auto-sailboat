from MPU9250.MPU9250 import MPU9250
import I2CMPU.python_i2c_mpu9250 as mpu
import smbus
import time
import math

sensor = mpu.mpu9250() # default pin is AIN0
while True:
    value = sensor.read_all()
    print(value)
    time.sleep(0.2)

