import math

class IMU_CALIB:
    
    #@classmethod
    def pitch_roll(self, accelx, accely, accelz): # method to get pitch roll from raw accelerometer values
        
        self.accXnorm = accelx/(math.sqrt(accelx*accelx + accely*accely + accelz*accelz)) # normalize accel x values
        self.accYnorm = accely/(math.sqrt(accelx*accelx + accely*accely + accelz*accelz)) # normalize accel x values

        self.pitch = math.asin(self.accXnorm)
        self.roll = -1 * math.asin(self.accYnorm/math.cos(self.pitch))

        return(self.pitch, self.roll)