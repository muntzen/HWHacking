'''
    this is what the example JSON data from the PHP serverside code will look like.  it needs to be fully wired up, but for now 
    this is what we'll get
    $vals = array(
        'current_status'=>array('active'=>'Y', 'balls'=>1, 'strikes'=>1, 'outs'=>2),
        'home_team'=>'ATL',
        'away_team'=>'NYM',
        'totals'=>array('home_runs'=>1, 'home_hits'=>4, 'home_errors'=>1,'away_runs'=>4, 'away_hits'=>6, 'away_errors'=>0),
        'innings'=>array(
            1 => array(0,0),
            2 => array(1,1),
            3 => array(0,4),
            4 => array(0,0),

        )
    );
'''
import RPi.GPIO as GPIO

class Display:
    ''' Class that handles communicating with the display elements on the Pi from the data from the server '''
    def __init__(self)
        GPIO.setmode(GPIO.BOARD)
        # TODO: Read config with the gpio pin numbers for everything into instance vars
        GPIO.setup([11, 13, 15], GPIO.OUT)

    def output(self, gamestate):
        if gamestate['current_status']['active'] == 'Y':
            self.lightBalls(gamestate['current_status']['balls'])
            self.lightStrikes(gamestate['current_status']['strikes'])
            self.lightOuts(gamestate['current_status']['outs'])
        else:
            print 'not active game'

    def lightBalls(self, balls):
        on = []
        off = []
        if balls == 0:
            off = [11, 13, 15]
        elif balls == 1:
            off = [11, 13]
            on = [15]
        elif balls == 2:
            off = [11]
            on = [13, 15]
        else:
            on = [11, 13, 15]
        GPIO.output(off, False)
        GPIO.output(on, True)

    def lightStrikes(self, strikes):
        print "light up the first {} strike indicators".format(strikes)

    def lightOuts(self, outs):
        print "light up the first {} out indicators".format(outs)

