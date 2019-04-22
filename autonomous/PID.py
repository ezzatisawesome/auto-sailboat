#Code adapted from IvPID on GitHub

#This code has been modified to work be adapted to the heading of the boat
#Code is modified so that self.error is wrapped from -180 to 180
import time
from math import pi

class PID:
    def __init__(self, P=0.1, I=0.0, D=0.0):
        self.Kp = P
        self.Ki = I
        self.Kd = D

        self.sample_time = 0.00
        self.current_time = time.time()
        self.last_time = self.current_time
    
    def clear(self):
        """Clears PID computations and coefficients"""
        self.SetPoint = 0.0
        
        self.PTerm = 0.0
        self.ITerm = 0.0
        self.DTerm = 0.0
        self.last_error = 0.0
        
        self.windup_guard = 20.0
        self.output = 0.0
    
    def update(self, feedback):
        self.error = feedback - self.SetPoint
        
        self.current_time = time.time()
        self.delta_time = self.current_time - self.last_time
        self.delta_error = 0.0
        # error jumps when boat heading shifts from first quadrant to fourth quadrant NO GOOD

        if (self.delta_time >= self.sample_time):
            
            if self.error < -pi:
                self.error += (2.0*pi)
            if self.error > pi:
                self.error -= (2.0*pi)
            
            self.delta_error = self.error - self.last_error

            self.PTerm = self.Kp * self.error
            self.ITerm += self.error * self.delta_time

            if (self.ITerm < -self.windup_guard):
                self.ITerm = -self.windup_guard
            elif (self.ITerm > self.windup_guard):
                self.ITerm = self.windup_guard

            self.DTerm = 0.0
            if self.delta_time > 0:
                self.DTerm = self.delta_error / self.delta_time
            
            self.last_time = self.current_time
            self.last_error = self.error

            self.output = self.PTerm + (self.Ki * self.ITerm) + (self.Kd * self.DTerm)
    
    def setSampleTime(self, sample_time):
        self.sample_time = sample_time
    
    def setWindup(self, windup):
        self.windup_guard = windup