import math

class calib:

    #object to convert raw measurements to heading in degrees
    def heading(self, x, y):
        return(180 * math.atan2(y, x)/math.pi)
    
    def raw_to_deg(self, x):
        return(x * 180/math.pi)
    
    #def tilt_comp(bx, by, bz, phi, theta):
