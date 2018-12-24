import MPU9250
import IMU_CALIB
import sys

try:
     while True:
        mag = mpu9250.readMagnet()
        heading = IMU_CALIB.heading()
        
        x = mag['x'] #x mag value
        y = mag['y'] #y mag value
        z = mag['z'] #z mag value

        heading(x, y)
       
        #print("{:.4f}, {:.4f}, {:.4f}".format(x, y, z)) #format
        print(heading(x, y))
        
        time.sleep(1) #repeat every half second

except KeyboardInterrupt:
     sys.exit