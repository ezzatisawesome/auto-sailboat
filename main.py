import MPU9250
#import AS5130
import smbus
import time
import math
import sys

mpu9250 = MPU9250.MPU9250()

def heading(x, y):
    return(180 * math.atan2(x, y)/math.pi)

try:
     while True:
        mag = mpu9250.readMagnet()
        
        x = mag['x'] #x mag value
        y = mag['y'] #y mag value
        z = mag['z'] #z mag value

        heading(x, y)
       
        #print("{:.4f}, {:.4f}, {:.4f}".format(x, y, z)) #format
        print(heading(x, y))
        
        time.sleep(1) #repeat every half second

except KeyboardInterrupt:
     sys.exit
