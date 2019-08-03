import RTIMU

SETTINGS_FILE = "RTIMULib"

s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

imu.IMUInit()

#poll_interval = imu.IMUGetPollInterval()

imu.IMURead()

i = 0
while i < 1: 
    if imu.IMURead():
        #print("test")
        x, y, z = imu.getFusionData()
        print("%f,%f,%f" % (x,y,z))
        i += 1
