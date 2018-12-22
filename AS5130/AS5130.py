import RPi.GPIO as GPIO #import GPIO library to access GPIO pins on Raspi
import time
import math

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #set up GPIO pins on Raspi
GPIO.setup(12, GPIO.IN)

modes = {-1:"Unset", 11:"BCM", 10:"BOARD"}
mode = GPIO.getmode(12)

print(modes[mode])

GPIO.cleanup()
