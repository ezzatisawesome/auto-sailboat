import math

class waypoints:
    def __init__(self):
        self.waypoints = {}
        self.R = 6372.7955
    
    def modifyWp(self, key: int, value: tuple): #modifies or adds a gps coordinate
        self.waypoints[key] = value

    def deleteWp(self, key: int):
        self.waypoints.pop(key)

    def decode(self, key: int): #splits tuples in dictionary definitions
        return self.waypoints.get(key)
    
    def haversine(self, key1: int, key2: int): #calculates distance between two coords
        lat1, long1 = self.decode(key1)
        lat2, long2 = self.decode(key2)

        dLat = radians(lat2 - lat1)
        dLon = radians(long2 - long1)
        lat1 = radians(lat1)
        lat2 = radians(lat2)
                                  
        a = sin(dLat / 2)**2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
        c = 2 * asin(sqrt(a))

        return self.R * c

        
    def cal_bearing(self):
        y = math.sin(self.long2-self.long1) * math.cos(self.lat2)
        x = math.cos(self.lat1) * math.sin(self.lat2) -  math.sin(self.lat1) * math.cos(self.lat2) * math.cos(self.long2-self.long1)
        return math.atan2(y,x)
