import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error, you prolly need some extra permissions")

pins = [11, 13, 15, 16, 18, 22, 24]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins, True)
time.sleep(2);
GPIO.output(pins, False) 
time.sleep(2);
GPIO.output(pins, True) 
time.sleep(2);
GPIO.output(pins, False) 

GPIO.cleanup()

