# base handler, make a request to BSM to get the game status or the next
# time we need to run, then sling that output to the display classes

import sys
import requests
import time
from display import Display


display = Display()
try:
    while(True): #TODO: figure out the right way to poll and control state around that
        r = requests.get('https://boxscoremania.com/api/game-status', verify=False)
        gamestate = r.json()
        display.output(gamestate)
        time.sleep(2)

except KeyboardInterrupt:
    display.clear()
except:
    display.clear()

