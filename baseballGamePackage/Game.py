#!/usr/bin/python

#baseballGamePackage
import os
import sys
import json
import time
import datetime
var = os.path.abspath(os.path.dirname(__file__)+'../..')
sys.path.append(var)

from battingPackage.Batting import Batting
from battingPackage.CurrentBatting import CurrentBatting
from teamPackage.CreateTeam import CreateTeam
from teamPackage.Player import Player
from teamPackage.Team import Team
from fieldingPackage.CurrentField import CurrentField
from fieldingPackage.Field import Field

class Game(object):

 def __init__(self, home, away):
    self.ct = CreateTeam()
    self.teams = self.ct.createTeams(home, away)
    self.bat = Batting()
    self.cf = CurrentField()
    self.f = Field(self.cf)
    self.amountOfBasesToMove = 0
    self.currentBattingPlayer = None
    self.battingTeam = 0
    self.pitchingTeam = 1
    self.initOrder = True
    self.innings = 1
    self.inningEventList = []
    self.gameEventList = []

 def switchTeams(self):
    if self.initOrder == True:
        self.battingTeam = 1
        self.pitchingTeam = 0
        self.initOrder = False

    else:
        self.battingTeam = 0
        self.pitchingTeam = 1
        self.initOrder = True

 def teamAtBat(self):
  self.cf.start(self.teams[self.pitchingTeam])
  self.createInningData([{"code" : "START-HALF-INNING", "description" : "The " + self.teams[self.battingTeam].get_Team_Name() + " are up at bat!"}])
  while self.teams[self.battingTeam].getOuts() < 3:
   self.currentBattingPlayer = self.teams[self.battingTeam].getNextPlayerAtBat()
   cb = CurrentBatting(self.teams[self.pitchingTeam].get_Pitcher(), self.currentBattingPlayer)
   self.amountOfBasesToMove = self.bat.startBatting(cb)
   self.createInningData(self.bat.getGameString())
   if self.amountOfBasesToMove > 0:
    outsToBeAdded = self.f.newPlayerOnBases(self.amountOfBasesToMove, self.currentBattingPlayer, self.teams[self.battingTeam].getOuts(), cb.getHomerunOrWalk())
    self.createInningData(self.f.getGameString())
    if outsToBeAdded > 0:
      self.teams[self.battingTeam].addNumToOuts(outsToBeAdded)
   else:
    self.teams[self.battingTeam].addOneToOuts()
    print "OUT HAS HAPPENED " + str(self.teams[self.battingTeam].getOuts())
  self.teams[self.battingTeam].addNumToScore(self.cf.getScore())
  self.teams[self.battingTeam].setOutsToZero()
  self.cf.reset()
  
 def inning(self):
    self.teamAtBat()
    print "NEW TEAM AT BAT"
    print
    self.switchTeams()
    self.teamAtBat()
    self.switchTeams()
    print "NEW TEAM AT BAT"
    print
    self.innings = self.innings + 1

 def playGame(self):
    while self.innings < 10:
        self.inning()
        print "score at end of inning " + str(self.innings) + " is: " + "\n" + "Home Team: " + str(self.teams[0].getScore()) + "\n" + "Away Team: " + str(self.teams[1].getScore())
        self.createInningData([{"code" : "END-INNING-SCORE", "description" : "Home Team: " + str(self.teams[0].getScore()) + "  " + "Away Team: " + str(self.teams[1].getScore())}])
        self.addGameEvents()

    while self.teams[0].getScore() == self.teams[1].getScore():
        self.inning()
        print "score at end of inning " + str(self.innings) + " is: " + "\n" + "Home Team: " + str(self.teams[0].getScore()) + "\n" + "Away Team: " + str(self.teams[1].getScore())
        self.createInningData([{"code" : "END-INNING-SCORE", "description" : "Home Team: " + str(self.teams[0].getScore()) + "  " + "Away Team: " + str(self.teams[1].getScore())}])
        self.addGameEvents() 

    temp = [self.teams[0].getScore(), self.teams[1].getScore()]
    return temp
 
 def addGameEvents(self):
  self.gameEventList.append(self.inningEventList) 
  self.inningEventList = [] 

 def createInningData(self, aList):
  self.inningEventList.extend(aList) 
 
 def createJSON(self):
  with open('data.json' , 'w') as outfile:
	  json.dump(self.gameEventList, outfile, sort_keys = True, indent = 4, ensure_ascii = False)
  test = open('data.json')
  son = json.load(test)
  print son[0][0]["description"] 


 def getJSONData(self):
  ts = time.time()
  ts = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d-%H-%M-%S")
  with open(ts+ "_" + self.teams[0].get_Team_Name() + "_" + self.teams[1].get_Team_Name() +'_.json' , 'w') as outfile:
	  json.dump(self.gameEventList, outfile, sort_keys = True, indent = 4, ensure_ascii = False)
  return ts+ "_" + self.teams[0].get_Team_Name() + "_" + self.teams[1].get_Team_Name() +'_.json'
