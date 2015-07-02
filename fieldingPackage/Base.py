# fieldingPackage
from Player import Player

class Base(object):
 def __init(self,nextBase,playeronBase):
  self.isFull = false
  Base.nextBase = nextBase
  Player.playerOnBase = playeronBase

 def addPlayerToBase(self,p):
  Player.playerOnBase = p
  self.isFull = true

 def movePlayerOneBase():
  nextBase.addPlayerToBase(playerOnBase)
  removePlayerFromBase()

 def removePlayerFromBase(self):
  Player.playerOnBase = null
  self.isFull = false


 def getPlayerOnBase():
  return Player.playerOnBase

#This is a test change
 def getIsFull():
  return isFull

 def nextBase():
  return Base.nextBase

 def setNextBase(b):
  Base.nextBase = b


 def toString():
  return "Player " + getPlayerOnBase() + " is on base"
