import RPi.GPIO as GPIO

class rudder:
    def __init__(self, input):
        self.servoPIN = servoPIN
        self.input = input
    def setup(self, servoPIN, ):
        self.servoPIN = servoPIN
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(servoPIN, GPIO.OUT)

    def control(self, input):
        p = GPIO.PWM(servoPIN, 50)
        p.start(2.5)
        p.ChangeDutyCycle(input)
        p.stop()
        GPIO.cleanup()
