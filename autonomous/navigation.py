from math import *

class navigation:
    def __init__(self, lat1=0, long1=0, lat2=0, long2=0):
        self.lat1 = lat1
        self.long1 = long1
        self.lat2 = lat2
        self.long2 = long2
        self.R = 6372.7955

    def cal_bearing(self):
        y = math.sin(self.long2-self.long1) * math.cos(self.lat2)
        x = math.cos(self.lat1) * math.sin(self.lat2) - math.sin(self.lat1) * math.cos(self.lat2) * math.cos(self.long2-self.long1)
        return math.atan2(y,x)
    
    def cal_distance(self):
        return self.R * acos(sin(self.lat1) * sin(self.lat2) * cos(lat1) * cos(self.lat2) * cos(self.lon1-self.long2)) #this is using the spherical Law of Cosines
    
    def haversine(self, lat1, long1, lat2, long2): #this function uses the Haversine formula        
        dLat = radians(lat2 - lat1)
        dLon = radians(long2 - long1)
        lat1 = radians(lat1)
        lat2 = radians(lat2)
                                  
        a = sin(dLat / 2)**2 + cos(lat1) * cos(lat2) * sin(dLon / 2)**2
        c = 2 * asin(sqrt(a))

        return self.R * c
    
    def input1(self, input_lat, input_long):
        self.lat1 = float(input_lat)
        self.lon1 = float(input_long)


    def input2(self, input_lat, input_long):
        self.lat2 = float(input_lat)
        self.lon2 = float(input_long)

