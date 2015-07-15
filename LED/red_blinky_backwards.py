import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error, you prolly need some extra permissions")

pin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, True)
time.sleep(2);
GPIO.output(pin, False) 
time.sleep(2);
GPIO.output(pin, True) 
time.sleep(2);
GPIO.output(pin, False) 

GPIO.cleanup()

