#!/usr/bin/python

# package teamPackage
import os
import sys
var = os.path.abspath(os.path.dirname(__file__)+'../..')
sys.path.append(var)

from random import randint
from Player import Player

class Pitcher(Player):

    pos = "P"

    def __init__(self, playerData, pitcherData):
        super(Pitcher, self).__init__(playerData)
        self.name = pitcherData[0]
        self.games = int(pitcherData[1])
        self.zonePer = float(pitcherData[3])
        self.fb = float(pitcherData[4]) * 100
        self.fbV = float(pitcherData[5])
        self.sl = float(pitcherData[6]) * 100
        self.slV = float(pitcherData[7])
        self.ct = float(pitcherData[8]) * 100
        self.ctV = float(pitcherData[9])
        self.cb = float(pitcherData[10]) * 100
        self.cbV = float(pitcherData[11])
        self.ch = float(pitcherData[12]) * 100
        self.chV = float(pitcherData[13])
        self.sf = float(pitcherData[14]) * 100
        self.sfV = float(pitcherData[15])
        self.kn = float(pitcherData[16]) * 100
        self.knV = float(pitcherData[17])

    def getPitchType(self):
        temp = randint(0, 99)
        if temp < self.fb:
            return self.fbV
        elif temp < self.fb + self.sl:
            return self.slV
        elif temp < self.fb + self.sl + self.ct:
            return self.ctV
        elif temp < self.fb + self.sl + self.ct + self.cb:
            return self.cbV
        elif temp < self.fb + self.sl + self.ct + self.cb + self.ch:
            return self.chV
        elif temp < self.fb + self.sl + self.ct + self.cb + self.ch + self.sf:
            return self.sfV
        else:
            return self.knV

    def getPitchSpeed(self):
        baseSpeed = self.getPitchType()
        temp = randint(0, 9)
        if temp <= 5:
            return baseSpeed + (-1 * temp)
        else:
            return baseSpeed + temp

    def getZonePer(self):
        return self.zonePer
    def getFb(self):
        return self.fb
    def getSl(self):
        return self.sl
    def getCt(self):
        return self.ct
    def getCb(self):
        return self.cb
    def getCh(self):
        return self.ch
    def getSf(self):
        return self.sf
    def getKn(self):
        return self.kn
    def getFbV(self):
        return self.fbV
    def getSlV(self):
        return self.slV
    def getCtV(self):
        return self.ctV
    def getCbV(self):
        return self.cbV
    def getChV(self):
        return self.chV
    def getSfV(self):
        return self.sfV
    def getKnV(self):
        return self.knV
    def getName(self):
        return self.name
    def getGames(self):
        return self.games
