import RPi.GPIO as GPIO #import GPIO library
import smbus
import time
import sys

GPIO.setwarnings(False) #disable GPIO warnings
GPIO.setmode(GPIO.BOARD) #set GPIO mode to BOARD
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) #initialize pin 12 for input and pulls down wire

try:
  while True:
    

except KeyboardInterrupt:

GPIO.cleanup() #reset GPIO