from math import *

class cal_bearing:
    def __init__(self, lat1, long1, lat2, long2):
        self.lat1 = lat1
        self.long1 = long1
        self.lat1 = lat1
        self.long2 = long2
        self.R = 6372.7955

    def cal_bearing(self):
        change_lat = log(tan(self.lat2/2+pi/4)/tan(self.lat1/2+pi/4))
        change_long = abs(long1-long2)
        return = atan2(change_long, change_lat)
    
    def cal_distance(self):
        return self.R * arccos(sin(lat1) * sin(lat2) * cos(lat1) * cos(lat2) * cos(lon1 -long2))