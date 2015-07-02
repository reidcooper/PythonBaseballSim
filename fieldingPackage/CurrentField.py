import os
import sys
var = os.path.abspath(os.path.dirname(__file__)+'../..')
sys.path.append(var)

from teamPackage import Team
from random import randint
class CurrentField (object):
 def __init__ (self):
  self.score = 0
  self.outs = 0

  Team.fieldingTeam = fieldingTeam

  Base.home = Base()
  Base.one = Base()
  Base.two = Base()
  Base.three = Base()

  Ball.ball = Ball()

#* Fielding Array (x marks plate, P is pitcher square)
 #* | 0 | 1 |  2   |
 #* ________________
 #* | 3 | 4x | 5   |
 #* ________________
 #* | 6x | 7P | 8x |
 #* ________________
 #* |   | 9x |     |
 #* ----------------
 #*

  self.rows = 4
  self.columns = 5

  self.gridFieldArray = [rows][columns]

 def CurrentField(self):
     one.setNextBase(two)
     two.setNextBase(three)
     three.setNextBase(home)
	
     for x in range(0,len(rows)):
                for y in range(0,len(column)):
                  gridFieldArray[x][y] = false, null
                  y+=1
                  
                x+=1
     gridFieldArray[0][0].setKey("LF", 15)
     gridFieldArray[0][2].setKey("CF", 15)
     gridFieldArray[0][4].setKey("RF", 15)
     gridFieldArray[2][1].setKey("SS", 8)
     gridFieldArray[2][2].setKey("P", 8)
     gridFieldArray[2][3].setKey("2B", 8)
     gridFieldArray[3][0].setKey("3B", 8)
     gridFieldArray[3][2].setKey("C", 8)
     gridFieldArray[3][4].setKey("1B", 5)


 def reset():
     score = 0
     resetOuts()
     home.removePlayerFromBase()
     one.removePlayerFromBase()
     two.removePlayerFromBase()
     three.removePlayerFromBase()


 def resetOuts():
     outs = 0


 def start(self, FieldingTeam):
     self.score = 0
     self.outs = 0
     home.removePlayerFromBase()
     one.removePlayerFromBase()
     two.removePlayerFromBase()
     three.removePlayerFromBase()
     fieldingTeam = FieldingTeam
	
     gridFieldArray[0][0].setFielder(fieldingTeam.getPlayerInFieldingPostion("LF"))
     gridFieldArray[0][2].setFielder(fieldingTeam.getPlayerInFieldingPostion("CF"))
     gridFieldArray[0][4].setFielder(fieldingTeam.getPlayerInFieldingPostion("RF"))
     gridFieldArray[2][1].setFielder(fieldingTeam.getPlayerInFieldingPostion("SS"))
     gridFieldArray[2][2].setFielder(fieldingTeam.getPlayerInFieldingPostion("P"))
     gridFieldArray[2][3].setFielder(fieldingTeam.getPlayerInFieldingPostion("2B"))
     gridFieldArray[3][0].setFielder(fieldingTeam.getPlayerInFieldingPostion("3B"))
     gridFieldArray[3][2].setFielder(fieldingTeam.getPlayerInFieldingPostion("C"))
     gridFieldArray[3][4].setFielder(fieldingTeam.getPlayerInFieldingPostion("1B"))


 def putBallIntoRandomSquare():
     ball.setPostion((random.randint()*4), (random.randit()*5))
	#ball.setPostion(0, 0);


 def putBallIntoRandomInFieldSquare():
     ball.setPostion((random.randint()*2 + 2), (random.randint()*4))


 def wasBallCaught(self, x, y):
     return self.gridFieldArray[x][y].wasBallCaught()


 def getScore(self):
     return self.score

 def addScore(self):
     self.score = self.score +1

 def getOuts(self):
     return self.outs

 def addOneToOuts(self):
     self.outs = self.outs + 1

 def toString():
     return "base 1 " +one.toString() + "\n" + "base 2 " +two.toString() + "\n"
     + "base 3 " +three.toString() + "\n"


