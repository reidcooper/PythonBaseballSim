#!/usr/bin/python

# package battingPackage
import os
import sys
var = os.path.abspath(os.path.dirname(__file__)+'../..')
sys.path.append(var)

from teamPackage import Pitcher
from teamPackage import Player
from random import randint

class Batting(object):

    chanceOfBall = 0
    chanceOfStrike = 0
    chanceOfHit = 0
    chanceOfFoul = 0
    z = 0
    avgIPR = 52.7
    maxZ = 144.0
    FBPR = 0
    gameString = [{"code" : "THIS IS THE START OF THE FILE"}]

    def __init__(self):
        pass

    def startBatting(self, cb):
        self.gameString[:] = []
        self.balls = 0
        self.strikes = 0
        self.currentBatting = cb
        self.pitcher = cb.getPitcher()
        self.player = cb.getPlayer()
        self.FBPR = self.generateFBPR()
        
        self.gameString.append({"code" : "NEW-BATTER", "description" : str(self.player.toString()) + " is next up to bat!"})

        self.chanceOfBall = (1 - self.pitcher.getZonePer()) * (1 - self.player.getOSwing())
        self.chanceOfStrike = (self.pitcher.getZonePer() * self.player.getZSwing() * (1 - self.player.getZContact())) + (self.pitcher.getZonePer() * (1 - self.player.getZSwing())) + (((1 - self.pitcher.getZonePer()) * self.player.getOSwing() * (1 - self.player.getOContact())))
        self.chanceOfFoul = ((1 - self.pitcher.getZonePer()) * self.player.getOSwing() * self.player.getOContact() * self.FBPR) + (self.pitcher.getZonePer() * self.player.getZSwing() * self.player.getZContact() * self.FBPR)
        self.chanceOfHit = ((1 - self.pitcher.getZonePer()) * self.player.getOSwing() * self.player.getOContact() * (1 - self.FBPR)) + (self.pitcher.getZonePer() * self.player.getZSwing() * self.player.getZContact() * (1 - self.FBPR))

        self.chanceOfBall = self.chanceOfBall * 1000
        self.chanceOfStrike = self.chanceOfStrike * 1000
        self.chanceOfHit = self.chanceOfHit * 1000
        self.chanceOfFoul = self.chanceOfFoul * 1000

        self.aSingle = int(self.player.getChanceSingle() * 100)
        self.aDouble = int(self.player.getChanceDouble() * 100)
        self.aTriple = int(self.player.getChanceTriple() * 100)

        return self.atBat()

    def generateFBPR(self):
        z = -66.7 + (self.generatePitchSpeed()/self.player.getIPR())
        if z < self.avgIPR:
            z = (z/self.avgIPR) * 0.5
        else:
            z = 0.5 + (((self.z-self.avgIPR)/(self.maxZ - self.avgIPR)) * 0.5) #use to be .. z = 0.5 + (((z-self.avgIPR)/(self.maxZ - self.avgIPR)) * 0.5) not sure if this line ever even runs
        return z

    def generateNewFBPR(self):

        self.FBPR = self.generateFBPR()
        self.chanceOfFoul = ((1 - self.pitcher.getZonePer()) * self.player.getOSwing() * self.player.getOContact() * self.FBPR) + (self.pitcher.getZonePer() * self.player.getZSwing() * self.player.getZContact() * self.FBPR)
        self.chanceOfHit = ((1 - self.pitcher.getZonePer()) * self.player.getOSwing() * self.player.getOContact() * (1 - self.FBPR)) + (self.pitcher.getZonePer() * self.player.getZSwing() * self.player.getZContact() * (1 - self.FBPR))

        self.chanceOfFoul = 1000 * self.chanceOfFoul
        self.chanceOfHit = 1000 * self.chanceOfHit

    def generatePitchSpeed(self):
        return self.pitcher.getPitchSpeed()

    def atBat(self):
        self.strikes = self.currentBatting.getStrikes()
        while self.strikes <= 2 and self.balls <= 3:
            self.generateNewFBPR()
            outcome = self.pitch()

            if outcome == 0:
               return self.hit()

            if self.currentBatting.getBalls() == 4:
               self.gameString.append({"code" : "BB", "description" : "Take a Base! " + str(self.player.toString()) + " walked"})
               self.currentBatting.setHomerunOrWalk("walk")
               return 1
        self.gameString.append({"code" : "KO", "description" : "You're Out! " + str(self.player.toString()) + " struck out!"})
        return 0

    def pitch(self):
        temp = randint(0, 999)
        #ball
        if temp < self.chanceOfBall:
            self.currentBatting.addBall()
            self.balls = self.currentBatting.getBalls()
            print "Ball " + str(self.balls) + " outcome " + str(temp)
            self.gameString.append({"code" : "BALL" , "description" : "Ball " + str(self.balls)})
            return 1
        #strike
        elif temp < self.chanceOfBall + self.chanceOfStrike:
            self.currentBatting.addStrike()
            self.strikes = self.currentBatting.getStrikes()
            print "Strike " + str(self.strikes) + " outcome " + str(temp)
            self.gameString.append({"code" : "STRIKE", "description" : "Strike " + str(self.strikes)})
            return 1
        #foul
        elif temp < self.chanceOfBall + self.chanceOfStrike + self.chanceOfFoul:
            if self.currentBatting.getStrikes() < 2:
                self.currentBatting.addStrike()
                self.strikes = self.currentBatting.getStrikes()
                print "Foul that was strike " + str(self.strikes) + " outcome " + str(temp)
                self.gameString.append({"code" : "FOUL-STRIKE", "description" : "Foul that was strike " + str(self.strikes)})
                return 1
            else:
                self.currentBatting.addFoul()
                print "foul " + str(self.currentBatting.getFouls()) + " outcome " + str(temp)
                self.gameString.append({"code" : "FOUL", "description" : "Foul " + str(self.currentBatting.getFouls())})
                return 1
        #hit
        else:
            print "Ball was hit by " + str(self.player.toString()) + " outcome = " + str(temp)
            return 0

    def hit(self):
        temp = randint(0, 100)
        if temp < self.aSingle:
            self.gameString.append({"code" : "1B", "description" : "Hit! " + str(self.player.toString()) + " hit a single!"})
            return 1
        elif temp < self.aSingle + self.aDouble:
            self.gameString.append({"code" : "2B", "description" : "Hit! " + str(self.player.toString()) + " hit a double!"})
            return 2
        elif temp < self.aSingle + self.aDouble + self.aTriple:
            self.gameString.append({"code" : "3B", "description" : "Hit! " + str(self.player.toString()) + " hit a triple!"})
            return 3
        else:
            self.currentBatting.setHomerunOrWalk("homerun")
            self.gameString.append({"code" : "HR", "description" : "Hit! " + str(self.player.toString()) + " hit a homerun!"})
            return 4

    def getBatter(self):
        return self.currentBatting.getPlayer()

    def toString(self):
        return "Chance of ball: " + str(self.chanceOfBall) + "\n" + "Chance of hit: " + str(self.chanceOfHit) + "\n" + "Chance of foul: " + str(self.chanceOfFoul) + "\n" + "Chance of strike: " + str(self.chanceOfStrike) + "\n"
    
    def getGameString(self):
		return self.gameString
