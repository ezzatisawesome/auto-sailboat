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

<<<<<<< HEAD
        print("{:.4f},{:.4f},{:.4f}".format(x, y, z)) #format
=======
        print("{:.4f}, {:.4f}, {:.4f}".format(x, y, z)) #format
>>>>>>> 9f6022c5185099921544cbb536d552595c027981
        
        time.sleep(0.2) #repeat every half second

except KeyboardInterrupt:
    sys.exit


