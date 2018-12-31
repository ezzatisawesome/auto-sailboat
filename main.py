import MPU9250
import sys
import time

mpu9250 = MPU9250.MPU9250()

try:
     while True:
        mag = mpu9250.readMagnet()
        
        x = mag['x'] #x mag value
        y = mag['y'] #y mag value
        z = mag['z'] #z mag value

        print("{:>.3f}  {:>.3f}  {:>.3f}" .format(x, y, z))
        
        time.sleep(1) #repeat every second

except KeyboardInterrupt:
     sys.exit
