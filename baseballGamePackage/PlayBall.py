import os
import sys
var = os.path.abspath(os.path.dirname(__file__)+'../..')
sys.path.append(var)

from baseballGamePackage import Game
class PlayBall(object):
    def __init__(self):
        pass
    
    avg = [0,1]
	
    amountOfGames = 20
	
	
    for x in range(0, amountOfGames - 1):
	    b = Game("Yankees", "Yankees")
	    b.playGame()
	    avg[0] = avg[0] + b.playGame()[0]
	    avg[1] = avg[1] + b.playGame()[1]
		
	    print "\n" +amountOfGames + " game average is\n Home team : "
	    + ((avg[0])/amountOfGames)
	    + "\n average of Away team : " + ((avg[1])/amountOfGames)
	    x+=1
