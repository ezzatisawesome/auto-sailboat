import math

class IMU_CALIB:
    def __init__(self):
        pass
    #@classmethod
    def pitch(self, accelx, accely, accelz): # method to get pitch from raw accelerometer values
        
        self.accXnorm = accelx/(math.sqrt(accelx*accelx + accely*accely + accelz*accelz)) # normalize accel x values
        self.calcpitch = math.asin(self.accXnorm)

        return(self.calcpitch)

    #@classmethod
    def roll(self, accelx, accely, accelz): # method to get roll from raw accelerometer values
        self.accXnorm = accelx/(math.sqrt(accelx*accelx + accely*accely + accelz*accelz)) # normalize accel x values
        self.accYnorm = accely/(math.sqrt(accelx*accelx + accely*accely + accelz*accelz)) # normalize accel y values

        self.calcroll = -1 * math.asin(self.accYnorm/math.cos(self.pitch))

        return(self.calcroll)