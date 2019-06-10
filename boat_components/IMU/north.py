from IMU import MPU9250
import system

try:
    while True:
        mag = MP9250.readMagnet()
        print(" mx = " , ( mag['x'] ))
        print(" my = " , ( mag['y'] ))
        print(" mz = " , ( mag['z'] ))
except KeyboardInterrupt:
    sys.exit()