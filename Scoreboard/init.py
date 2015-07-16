# base handler, make a request to BSM to get the game status or the next
# time we need to run, then sling that output to the display classes

import sys
import requests
from display import Display


display = Display()
try:
    while(True):
        r = requests.get('https://boxscoremania.com/api/game-status', verify=False)
        gamestate = r.json()
        display.output(gamestate)
except KeyboardInterrupt:
    display.clear()
except:
    display.clear()

