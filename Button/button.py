# using an input pin to control the output, will connect this to my LED to make it blink when i fucking say so
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(7, gpio.OUT)
gpio.output(7, 0)

try:
    print "Press the button on the bready board to light up the light"
    existing = gpio.input(11)
    while True:
        val = gpio.input(11)
        gpio.output(7, val)
        if (existing != val):
            print "pressed" if val else "released" # I really like this syntax over typical ternary conditional things
        existing = val
except KeyboardInterrupt:
    gpio.cleanup()

