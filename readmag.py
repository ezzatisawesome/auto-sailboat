import MPU9250.MPU9250
import smbus
import time
import sys

mpu9250 = MPU9250.MPU9250()

try:
    while True:
        mag = mpu9250.readMagnet()
        x = mag['x'] #x mag value
        y = mag['y'] #y mag value
        z = mag['z'] #z mag value

        print("{:.4f} {:.4f} {:.4f}".format(x, y, z)) #format
        
        time.sleep(0.5) #repeat every half second

except KeyboardInterrupt:
    sys.exit


