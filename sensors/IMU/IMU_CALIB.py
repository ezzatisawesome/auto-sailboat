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


    #def mag_calibration(self, magx, magy, magz, magXmax, magXmin, magYmax, magYmin, magZmax, magZmin): #to apply calibration
        
        #offset_x = (magXmax + magXmin) / 2
        #offset_y = (magYmax + magYmin) / 2
        #offset_z = (magZmax + magZmin) / 2

        #avg_delta_x = (magXmax - magXmin) / 2
        #avg_delta_y = (magYmax - magYmin) / 2
        #avg_delta_z = (magZmax - magZmin) / 2

        #avg_delta = (avg_delta_x + avg_delta_y + avg_delta_z) / 3

        #scale_x = avg_delta / avg_delta_x
        #scale_y = avg_delta / avg_delta_y
        #scale_z = avg_delta / avg_delta_z

        #self.corrected_x = (magx - offset_x) * scale_x
        #self.corrected_y = (magy - offset_y) * scale_y
        #self.corrected_z = (magz - offset_z) * scale_z

        #return(self.corrected_x, self.corrected_y, self.corrected_z)
    
    def mag_calibration(self, mag_val, offset_val, scale_val):

        return(mag_val - offset_val) * scale_val
        #return(self.corrected_mag_val)

    def mag_tilt_comp(self, magx, magy, magz, accelx, accely, accelz):

        accXnorm = accelx/(math.sqrt(accelx*accelx + accely*accely + accelz*accelz)) # normalize accel x values
        self.calcpitch = math.asin(accXnorm) #converting to pitch values in radians

        accYnorm = accely/(math.sqrt(accelx*accelx + accely*accely + accelz*accelz)) # normalize accel y values
        self.calcroll = -1*math.asin(accYnorm/math.cos(self.calcpitch)) #converting to roll values in radians

        magXcomp = magx*math.cos(self.calcpitch) + magz*math.sin(self.calcpitch) #calucluate compensated magx values
        magYcomp = magx*math.sin(self.calcroll)*math.sin(self.calcpitch) + magy*math.cos(self.calcroll) - magz*math.sin(self.calcroll)*math.cos(self.calcpitch) # calculate compensated magy values

        self.comp_heading = 180 * math.atan2(magYcomp, magXcomp) / math.pi #heading function and convert to degrees

        if self.comp_heading < 0:
            self.comp_heading += 360

        return(self.comp_heading)
 

        #sudo code
    #magXcomp = mag_raw[0]*cos(pitch)+mag_raw[2]*sin(pitch);
    #magYcomp = mag_raw[o]*sin(roll)*sin(pitch)+mag_raw[1]*cos(roll)-mag_raw[2]*sin(roll)*cos(pitch);
    #heading = 180*atan2(magYcomp,magXcomp)/M_PI;
