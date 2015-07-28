#!/usr/bin/python

#package battingPackage
import os
import sys
var = os.path.abspath(os.path.dirname(__file__)+'../..')
sys.path.append(var)

from teamPackage import Pitcher
from teamPackage import Player

class CurrentBatting(object):

    def __init__(self, pitcher, player):
        self.strikes = 0
        self.fouls = 0
        self.balls = 0
        self.homerunOrWalk = ""
        self.pitcher = pitcher
        self.player = player

    def addStrike(self):
        self.strikes = self.strikes + 1

    def addBall(self):
        self.balls = self.balls + 1

    def addFoul(self):
        self.fouls = self.fouls + 1

    def getStrikes(self):
        return self.strikes

    def setStrikes(self, strikes):
        self.strikes = strikes

    def getBalls(self):
        return self.balls

    def setBalls(self, balls):
        self.balls = balls;

    def getFouls(self):
        return self.fouls;

    def setFouls(self, fouls):
        self.fouls = fouls

    def getPlayer(self):
        return self.player

    def getPitcher(self):
        return self.pitcher

    def getHomerunOrWalk(self):
        return self.homerunOrWalk

    def setHomerunOrWalk(self, homerunOrWalk):
        self.homerunOrWalk = homerunOrWalk
