from math import *
from sensors import GPS

class navigation:
    def __init__(self, lat1, long1, lat2, long2):
        self.lat1 = lat1
        self.long1 = long1
        self.lat1 = lat1
        self.long2 = long2
        self.R = 6372.7955

    def cal_bearing(self):
        change_lat = log(tan(self.lat2/2+pi/4)/tan(self.lat1/2+pi/4))
        change_long = abs(long1-long2)
        return atan2(change_long, change_lat)
    
    def cal_distance(self):
        return self.R * arccos(sin(self.lat1) * sin(self.lat2) * cos(lat1) * cos(self.lat2) * cos(self.lon1-self.long2))