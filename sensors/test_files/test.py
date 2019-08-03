import serial
import time

port = '/dev/ttyACM0'
baudrate = 115280

ser = serial.Serial(port, baudrate)
ser.flushInput()

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        
    
    except:
        print("Keyboard Interrupt")
        break
