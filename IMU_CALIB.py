import math

class IMU_CALIB:
    def __init__(self):
        pass
    #@classmethod
    def pitch(self, accelx, accely, accelz): # method to get pitch from raw accelerometer values
        
        self.accXnorm = accelx/(math.sqrt(accelx*accelx + accely*accely + accelz*accelz)) # normalize accel x values
        self.calcpitch = math.asin(self.accXnorm)

        return(selfcalcpitch)

    #@classmethod
    def roll(self, accelx, accely, accelz): # method to get roll from raw accelerometer values

        self.accXnorm = accelx/(math.sqrt(accelx*accelx + accely*accely + accelz*accelz)) # normalize accel x values
        self.accYnorm = accely/(math.sqrt(accelx*accelx + accely*accely + accelz*accelz)) # normalize accel y values

        calcroll = -1 * math.asin(self.accYnorm/math.cos(self.pitch))

        return(calcroll)

    
    def tilt_comp(self, magx, magy, magz):

        self.magXcomp = magx*math.cos(self.pitch) + magz*math.sin(self.pitch) # calucluate compensated magx values
        self.magYcomp = magx*math.sin(self.roll)*math.sin(self.pitch) + magy*math.cos(self.roll) - magz*math.sin(self.roll)*math.cos(self.pitch) # calculate compensated magy values

        self.comp_heading = (180 * math.atan2(self.magYcomp, self.magXcomp)) / math.pi

        return(self.comp_heading)

 
        #sudo code
    #magXcomp = mag_raw[0]*cos(pitch)+mag_raw[2]*sin(pitch);
    #magYcomp = mag_raw[o]*sin(roll)*sin(pitch)+mag_raw[1]*cos(roll)-mag_raw[2]*sin(roll)*cos(pitch);
    #heading = 180*atan2(magYcomp,magXcomp)/M_PI;
