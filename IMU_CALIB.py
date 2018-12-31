import math

class IMU_CALIB:
    
    @classmethod
    def pitch_roll(cls, accelx, accely, accelz): # method to get pitch roll from raw accelerometer values
        
        cls.accXnorm = accelx/(math.sqrt(accelx*accelx + accely*accely + accelz*accelz)) # normalize accel x values
        cls.accYnorm = accely/(math.sqrt(accelx*accelx + accely*accely + accelz*accelz)) # normalize accel x values

        cls.pitch = math.asin(cls.accXnorm)
        cls.roll = -1 * math.asin(cls.accYnorm/math.cos(cls.pitch))

        return(cls.pitch, cls.roll)