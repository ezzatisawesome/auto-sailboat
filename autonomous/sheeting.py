import math
import sys
import time
import sensor

class sheet:
    def __init__(self, opt_angle, sheet_length, diameter, exit2boom, rel_wind = 0):
        self.opt_angle = opt_angle #optimum angle for sail
        self.sheet_length = sheet_length #sheet length 
        self.diameter = diameter #diameter of spool (will be a constant value)
        self.exit2boom = exit2boom #length of the sheet exit to the boom (will be a constant value)
        self.rel_wind = rel_wind #direction of wind relative to boat centerline (directly measured by wind vane)

    def opt_sail_angle(self, rel_wind):
        self.opt_angle = 3 + 3 * math.cos(self.rel_wind) #equation is 3+3cos(rel_wind)    limit to 0 and 2pi
        return(self.opt_angle)
    
    def sheet(self, opt_angle, sheet_length):  #funciton to calculate rotations pulley (pul_rot) has to make to based on sheet_length based and  opt_sail_angle
        self.sheet_length = math.sqrt(math.pow(self.sheet_length,2) + math.pow(self.exit2boom,2) - 2 * self.sheet_length * self.exit2boom * math.cos(self.opt_angle))
        self.pul_rot = 360 * (self.sheet_length / self.diameter * math.pi) #finds the revolution(s) that the servo
