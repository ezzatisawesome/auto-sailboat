import math
#import magrawvalues (trying to import .csv file in MPU9250)

class calib:
    #def __init__():
    
    # object to convert raw measurements to heading in degrees
    def heading(self, x, y):
        return(180 * math.atan2(y, x)/math.pi)
    
    # convert radians to degrees
    def raw_to_deg(self, x):
        return(x * 180/math.pi)
    
    # tilt compensation equation
    def tilt_comp(self, x, y, z, phi, theta):
        # x = magnetometer x value
        # y = magmetometer y value
        # z = magnetometer z value
        # phi =  pitch
        # theta = roll
        x = 0

    def norm_accel(self, x, y, z):
        # where x, y, and z would correlate to the x, y, and z raw accelerometer values

        self.accXnorm = (x/math.sqrt(x*x + y*y + z*z)
        self.accYnorm = (y/math.sqrt(x*x + y*y + z*z)) #SyntaxError: invalid syntax on this line

        self.pitch = math.asin(accXnorm)
        self.roll = -1 * math.asin(accYnorm/math.cos(pitch))