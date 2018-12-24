import math

class calib:

    #object to convert raw measurements to heading in degrees
    def heading(x, y):
         return(180 * math.atan2(x, y)/math.pi)