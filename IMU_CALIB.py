import math

class IMU_CALIB:
    def __init__(self):
        pass

    def pitch(self, accelx, accely, accelz): #method to get pitch from raw accelerometer values

        accXnorm = accelx/(math.sqrt(accelx*accelx + accely*accely + accelz*accelz)) # normalize accel x values
        self.calcpitch = math.asin(accXnorm) #converting to pitch values in radians

        return(self.calcpitch)

    def roll(self, accelx, accely, accelz): #method to get roll from raw accelerometer values

        accYnorm = accely/(math.sqrt(accelx*accelx + accely*accely + accelz*accelz)) # normalize accel y values
        self.calcroll = -1*math.asin(accYnorm/math.cos(self.calcpitch)) #converting to roll values in radians

        return(self.calcroll)


    def tilt_comp(self, magx, magy, magz):

        magXcomp = magx*math.cos(self.pitch) + magz*math.sin(self.pitch) # calucluate compensated magx values
        magYcomp = magx*math.sin(self.roll)*math.sin(self.pitch) + magy*math.cos(self.roll) - magz*math.sin(self.roll)*math.cos(self.pitch) # calculate compensated magy values

        self.comp_heading = 180 * math.atan2(magYcomp, magXcomp) / math.pi

        return(self.comp_heading)

 
        #sudo code
    #magXcomp = mag_raw[0]*cos(pitch)+mag_raw[2]*sin(pitch);
    #magYcomp = mag_raw[o]*sin(roll)*sin(pitch)+mag_raw[1]*cos(roll)-mag_raw[2]*sin(roll)*cos(pitch);
    #heading = 180*atan2(magYcomp,magXcomp)/M_PI;
