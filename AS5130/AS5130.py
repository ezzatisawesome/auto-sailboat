import RPi.GPIO as GPIO
import time
import math

IO.setwarnings(False) #got from random website
IO.setmode(IO.BCM) #got from random website
IO.setup(19,IO.IN) #got from random website

p = IO.PWM(output channel , frequency of PWM signal) #got from random website

angle = 0 #angle value
angle = (365/256)*(257(ton/(ton*toff)-1) #equation from datasheet of AS5130 to convert pwn to degree value (HAVE TO DEFINE WHAT "ton" and "toff" are)