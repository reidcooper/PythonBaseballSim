#!/usr/bin/python

# fieldingPackage
import os
import sys
var = os.path.abspath(os.path.dirname(__file__)+'../..')
sys.path.append(var)

from teamPackage.Player import Player
import random

class FieldSquare(object):
 def __init__(self):
  self.hasBall = False
  self.key = None
  self.playerSpace = [0,0,0]
  self.fielder = None

 def setSize(self, this_size):
       self.playerSpace = [0]*this_size

 def getHasBall(self):
       return self.hasBall

 def setHasBall(self, HasBall):
       self.hasBall = HasBall

 def getKey(self):
       return self.key

 def setKey(self,this_key,this_size):
       self.key = this_key
       self.setSize(this_size)

 def  getFielder(self, Player):
       return Player.fielder

 def setFielder(self, this_fielder):
       self.fielder = this_fielder
       for i in range(0, len(self.playerSpace)):
           if i < 50:
               self.playerSpace[i] = (int)(self.fielder.getFP()*100) - (i)
           else:
               playerSpace[i] = 60
               #playerSpace[i] = 60;
 def toString(self):
  return "This is a FieldSquare"

 def wasBallCaught(self):
       temp = (int)(random.random() * (len(self.playerSpace)-1))
       temp2 = (int)(random.random() * 100)
       print "chance " + (str(100 - self.playerSpace[temp])) + " random num " + str(temp2)
       if temp2 > (100 - self.playerSpace[temp]):
           print "BALL HAS BEEN CAUGHT OUT"
           return True
       else:
           return False
