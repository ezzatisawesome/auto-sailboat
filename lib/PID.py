import math

'''
PID Controller
'''


class rudder_control:
    def __init__(self, Kc, bias, output, heading, desired_heading = 0):
        self.Kc = Kc  #tuning parameter
        self.bias = bias  #bias
        self.output = output
        self.heading = heading  #boat heading
        self.desired_heading = desired_heading  #desired heading

    def controller_error(self, heading, desired_heading):  #difference between desired heading and heading
        self.control_error = abs(math.desired_heading - heading)

    def update(self, Kc, control_error, output):
        self.output = Kc * self.control_error  