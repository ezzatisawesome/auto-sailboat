import MPU9250
import AS5130.AS5130
import time
import math
import sys

mpu9250 = MPU9250.MPU9250()
rad_to_deg = MPU9250.calfunc.raw_to_deg() #radians to degrees object

try:
    while True:
        mag = mpu9250.readMagnet()
        x = mag['x'] #x mag value
        y = mag['y'] #y mag value
        z = mag['z'] #z mag value

        xc = rad_to_deg(x)
        yc = rad_to_deg(y)
        zc = rad_to_deg(z)


        print("{:.4f}, {:.4f}, {:.4f}".format(xc, yc, zc)) #format
        
        time.sleep(0.2) #repeat every half second

except KeyboardInterrupt:
    sys.exit