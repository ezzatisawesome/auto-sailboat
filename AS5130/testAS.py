import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False) #disable GPIO warnings
GPIO.setmode(GPIO.BOARD) #set GPIO mode to BOARD
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) #initialize pin 12 for input and pulls down wire

if GPIO.input(channel):
    print('Input was HIGH')
else:
    print('Input was LOW')

#try:
    #while True:

GPIO.cleanup() #reset GPIO