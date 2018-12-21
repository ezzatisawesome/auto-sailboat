import RPi.GPIO as GPIO
import time
import math

GIO.setwarnings(False) #got from random website
GIO.setmode(IO.BCM) #got from random website
GIO.setup(19,IO.IN) #got from random website

p = GIO.PWM(output channel , frequency of PWM signal) #got from random website

angle = 0 #angle value
angle = (365/256)*(257(ton/(ton*toff)-1) #equation from datasheet of AS5130 to convert pwn to degree value (HAVE TO DEFINE WHAT "ton" and "toff" are)
