import RPi.GPIO as GPIO #import GPIO library to access GPIO pins on Raspi
import time
import math

GPIO.setwarnings(False) #set GPIO warnings to false
GPIO.setmode(GPIO.BOARD) #set up GPIO pins on Raspi
GPIO.setup(12, GPIO.IN) #setup pin 12 for input
pwm = GPIO.PWM(12, 100) #initialize PWM on pwmPin 100Hz frequency

dc = 0 #set duty cycle to 0
pwm.start(dc) # Start PWM with 0% duty cycle


#obtained from mbtechworks.com (needs to be modified for sailboat application)
try:
  while True:                      # Loop until Ctl C is pressed to stop.
    for dc in range(0, 101, 5):    # Loop 0 to 100 stepping dc by 5 each loop
      pwm.ChangeDutyCycle(dc)
      time.sleep(0.05)             # wait .05 seconds at current LED brightness
      print(dc)
    for dc in range(95, 0, -5):    # Loop 95 to 5 stepping dc down by 5 each loop
      pwm.ChangeDutyCycle(dc)
      time.sleep(0.05)             # wait .05 seconds at current LED brightness
      print(dc)
except KeyboardInterrupt:
  print("Ctl C pressed - ending program")

pwm.stop()                         # stop PWM
GPIO.cleanup()                     # resets GPIO ports used back to input mode



modes = {-1:"Unset", 11:"BCM", 10:"BOARD"}
mode = GPIO.getmode(12)