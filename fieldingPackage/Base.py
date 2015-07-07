#!/usr/bin/python

# fieldingPackage
import os
import sys
var = os.path.abspath(os.path.dirname(__file__)+'../..')
sys.path.append(var)

from teamPackage import Player

class Base(object):
 def __init(self):
  self.isFull = False
  self.nextBase = Base()
  self.playerOnBase = None

 def addPlayerToBase(self,p):
  self.playerOnBase = p
  self.isFull = True

 def movePlayerOneBase(self):
  self.nextBase.addPlayerToBase(self.playerOnBase)
  self.removePlayerFromBase()

 def removePlayerFromBase(self):
  self.playerOnBase = None
  self.isFull = False


 def getPlayerOnBase(self):
  return self.playerOnBase

#This is a test change
 def getIsFull(self):
  return self.isFull

 def nextBase(self):
  return self.nextBase

 def setNextBase(self,b):
  self.nextBase = b


 def toString(self):
  return "Player " + getPlayerOnBase() + " is on base"
