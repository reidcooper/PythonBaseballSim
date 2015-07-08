import os
import sys
var = os.path.abspath(os.path.dirname(__file__)+'../..')
sys.path.append(var)

from teamPackage.Team import Team
from Base import Base
from Ball import Ball
from FieldSquare import FieldSquare
from random import randint

class CurrentField (object):
 def __init__(self):
  self.score = 0
  self.outs = 0

  self.fieldingTeam = Team()

  self.home = Base()
  self.one = Base()
  self.two = Base()
  self.three = Base()

  self.ball = Ball()

  ''' Fielding Array (x marks plate, P is pitcher square)
    ________________
    | 0  | 1  |  2 |
    ________________
    | 3  | 4x |  5 |
    ________________
    | 6x | 7P | 8x |
    ________________
    |    | 9x |    |
    ---------------- '''

  self.rows = 5
  self.columns = 4 

  self.gridFieldArray = [[0 for x in range (self.rows)]for x in range (self.columns)]
  self.one.setNextBase(self.two)
  self.two.setNextBase(self.three)
  self.three.setNextBase(self.home)
 
  for x in range(0, 4):
   for y in range(0, 5):
    self.gridFieldArray[x][y] = FieldSquare()
  
		 
  self.gridFieldArray[0][0].setKey("LF", 15)
  self.gridFieldArray[0][2].setKey("CF", 15)
  self.gridFieldArray[0][4].setKey("RF", 15)
  self.gridFieldArray[2][1].setKey("SS", 8)
  self.gridFieldArray[2][2].setKey("P", 8)
  self.gridFieldArray[2][3].setKey("2B", 8)
  self.gridFieldArray[3][0].setKey("3B", 8)
  self.gridFieldArray[3][2].setKey("C", 8)
  self.gridFieldArray[3][4].setKey("1B", 5)


 def reset(self):
     self.score = 0
     self.resetOuts()
     self.home.removePlayerFromBase()
     self.one.removePlayerFromBase()
     self.two.removePlayerFromBase()
     self.three.removePlayerFromBase()


 def resetOuts(self):
     self.outs = 0


 def start(self, FieldingTeam):
     self.score = 0
     self.outs = 0
     self.home.removePlayerFromBase()
     self.one.removePlayerFromBase()
     self.two.removePlayerFromBase()
     self.three.removePlayerFromBase()
     self.fieldingTeam = FieldingTeam

     self.gridFieldArray[0][0].setFielder(self.fieldingTeam.getPlayerInFieldingPostion("LF"))
     self.gridFieldArray[0][2].setFielder(self.fieldingTeam.getPlayerInFieldingPostion("CF"))
     self.gridFieldArray[0][4].setFielder(self.fieldingTeam.getPlayerInFieldingPostion("RF"))
     self.gridFieldArray[2][1].setFielder(self.fieldingTeam.getPlayerInFieldingPostion("SS"))
     self.gridFieldArray[2][2].setFielder(self.fieldingTeam.getPlayerInFieldingPostion("P"))
     self.gridFieldArray[2][3].setFielder(self.fieldingTeam.getPlayerInFieldingPostion("2B"))
     self.gridFieldArray[3][0].setFielder(self.fieldingTeam.getPlayerInFieldingPostion("3B"))
     self.gridFieldArray[3][2].setFielder(self.fieldingTeam.getPlayerInFieldingPostion("C"))
     self.gridFieldArray[3][4].setFielder(self.fieldingTeam.getPlayerInFieldingPostion("1B"))


 def putBallIntoRandomSquare(self):
     self.ball.setPostion(0, randint(0, 5))
	#ball.setPostion(0, 0);


 def putBallIntoRandomInFieldSquare(self):
     self.ball.setPostion(randint(2,3),randint(0, 4))


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

 def toString(self):
     return "base 1 " +one.toString() + "\n" + "base 2 " +two.toString() + "\n"
     + "base 3 " +three.toString() + "\n"
