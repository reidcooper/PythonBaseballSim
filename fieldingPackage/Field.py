import os
import sys
import traceback
var = os.path.abspath(os.path.dirname(__file__)+'../..')
sys.path.append(var)

from random import random
from random import randint
from teamPackage import Player

class Field(object):

    def __init__(self, currentField):
        self.currentField = currentField
        self.temp = []
        self.currentAmountOfOuts = 0
        self.gameString = []

    def newPlayerOnBases(self, n, p, currentAmountOfOuts, walkOrHomeRun):
        self.gameString[:] = []

        self.currentField.resetOuts()
        self.currentAmountOfOuts = currentAmountOfOuts
        if walkOrHomeRun == "walk":
            self.newPlayerOnBasesWalk(p)
        elif walkOrHomeRun == "homerun":
            self.newPlayerOnBasesHomerun(p)
        else:
            self.currentField.putBallIntoRandomSquare()
            if not self.checkIfBallIsCaught():
                try:
                    print "amount of bases to move " + str(n)
                    if n > 0:
                        if not(self.currentField.three.getPlayerOnBase() is None):
                            self.playerOnThird()

                        if not(self.currentField.two.getPlayerOnBase() is None):
                            self.currentField.two.movePlayerOneBase()
                            outOn3 = self.isPlayerOutOnBase(3, self.checkIfPlayerIsOnSameBaseAsBall(3))
                            if n >= 2 and not(outOn3):
                                self.playerOnThird()

                        if not (self.currentField.one.getPlayerOnBase() is None):
                            if n == 1:
                                self.currentField.one.movePlayerOneBase()
                                self.isPlayerOutOnBase(2, self.checkIfPlayerIsOnSameBaseAsBall(2))
                                self.moveOneBase(p)
                                #break
                            elif n == 2:
                                self.currentField.one.movePlayerOneBase()
                                if not self.isPlayerOutOnBase(2, self.checkIfPlayerIsOnSameBaseAsBall(2)):
                                 self.currentField.two.movePlayerOneBase()
                                 self.isPlayerOutOnBase(3, self.checkIfPlayerIsOnSameBaseAsBall(3))
                                self.moveTwoBases(p)
                                #break
                            elif n == 3:
                                self.currentField.one.movePlayerOneBase()
                                if not self.isPlayerOutOnBase(2, self.checkIfPlayerIsOnSameBaseAsBall(2)):
                                 self.currentField.two.movePlayerOneBase()
                                 if not self.isPlayerOutOnBase(3, self.checkIfPlayerIsOnSameBaseAsBall(3)):
                                  self.playerOnThird()
                                self.movePlayerThreeBases(p)
                                #break
                        else:
                            if n == 1:
                                self.moveOneBase(p)
                                #break
                            elif n == 2:
                                self.moveTwoBases(p)
                                #break
                            elif n == 3:
                                self.movePlayerThreeBases(p)
                                #break

                except ThreeOuts, args:
                    print "three outs have happened! ending fielding"
            else:
                self.currentField.addOneToOuts()
                self.gameString.append({"code" : "OUT-BH", "description" : "Out! " + p.toString() + " made contact, but the fielding team caught the ball! Out " + str(self.currentAmountOfOuts + self.currentField.getOuts())})
        self.gameString.append({"code" : "DIAMOND", "description" : self.currentField.printFieldInfo()})
        return self.currentField.getOuts()

    def moveOneBase(self, p):
        self.currentField.one.addPlayerToBase(p)
        self.isPlayerOutOnBase(1, self.checkIfPlayerIsOnSameBaseAsBall(1))

    def moveTwoBases(self, p):
        self.currentField.one.addPlayerToBase(p)
        b = self.isPlayerOutOnBase(1, self.checkIfPlayerIsOnSameBaseAsBall(1))
        if not b:
            self.currentField.one.movePlayerOneBase()
            self.isPlayerOutOnBase(2, self.checkIfPlayerIsOnSameBaseAsBall(2))

    def movePlayerThreeBases(self, p):
        self.currentField.one.addPlayerToBase(p)
        b = self.isPlayerOutOnBase(1, self.checkIfPlayerIsOnSameBaseAsBall(1))
        if not b:
            self.currentField.one.movePlayerOneBase()
            b = self.isPlayerOutOnBase(2, self.checkIfPlayerIsOnSameBaseAsBall(2))
        if not b:
            self.currentField.two.movePlayerOneBase();
            self.isPlayerOutOnBase(3, self.checkIfPlayerIsOnSameBaseAsBall(3))

    def checkIfBallIsCaught(self):
        #gridFieldArray[0][0].setKey("LF", 15);
        #gridFieldArray[0][2].setKey("CF", 15);
        #gridFieldArray[0][4].setKey("RF", 15);
        self.temp = self.currentField.ball.getPostion()
        print "Ball hit into field at " + " Ball pos " + str(self.temp[0]) + " :" + str(self.temp[1])

        if (self.temp[0] == 0 and self.temp[1] == 0) or (self.temp[0] == 0 and self.temp[1] == 2) or (self.temp[0] == 0 and self.temp[1] == 4):
            print "...checking if ball was caught"
            return self.isBallCaught(self.temp[0], self.temp[1])
        else:
            return False

    def isBallCaught(self, x, y):
        return self.currentField.wasBallCaught(x, y)

    def checkIfPlayerIsOnSameBaseAsBall(self, baseNum):
        #gridFieldArray[2][3].setKey("2B", 8);
        #gridFieldArray[3][0].setKey("3B", 8);
        #gridFieldArray[3][4].setKey("1B", 5);
        #gridFieldArray[3][2].setKey("C", 8);
        a = (random()*100)
        if a > 60:
         return True
        else:
          return False

        self.currentField.putBallIntoRandomInFieldSquare()
        basePos = [None] * 2
        if baseNum == 1:
            basePos[0] = 3
            basePos[1] = 4

        elif baseNum == 2:
            basePos[0] = 2
            basePos[1] = 3

        elif baseNum == 3:
            basePos[0] = 3
            basePos[1] = 0

        elif baseNum ==4:
            basePos[0] = 3
            basePos[1] = 2

        temp = self.currentField.ball.getPostion()
        print "Base num " + str(basePos[0]) + " : " + str(basePos[1]) + " Ball pos " + str(self.temp[0]) + " :" + str(self.temp[1])
        if self.temp[0] == basePos[0] and self.temp[1] == basePos[1]:
            print "Ball and player are on same base"
            return self.isBallCaught(temp[0], temp[1])
        return False

    def isPlayerOutOnBase(self, baseNum, b):
        if self.currentAmountOfOuts + self.currentField.getOuts() >= 3:
            raise ThreeOuts("3 outs have happened")

        #if not b:
			#a = randint(0,10)
			#if a > 5:
				#b = True

        if b:
            print "Player may get out on base"
            if baseNum == 1:
                self.currentField.addOneToOuts()
                print "Player got out on 1st base!"
                self.gameString.append({"code" : "OUT-1B", "description" : "Out! " + self.currentField.one.getPlayerOnBase().toString() + " was thrown out at First Base! Out " + str(self.currentAmountOfOuts + self.currentField.getOuts())})
                self.currentField.one.removePlayerFromBase()
                return True
            elif baseNum == 2:
                self.currentField.addOneToOuts()
                print "Player got out on 2nd base!"
                self.gameString.append({"code" : "OUT-2B", "description" : "Out! " + self.currentField.two.getPlayerOnBase().toString() + " was thrown out at Second Base! Out " + str(self.currentAmountOfOuts + self.currentField.getOuts())})
                self.currentField.two.removePlayerFromBase()
                return True
            elif baseNum ==3 :
                self.currentField.addOneToOuts()
                print "Player got out on 3rd base!"
                self.gameString.append({"code" : "OUT-3B", "description" : "Out! " + self.currentField.three.getPlayerOnBase().toString() + " was thrown out at Third Base! Out " + str(self.currentAmountOfOuts + self.currentField.getOuts())})
                self.currentField.three.removePlayerFromBase()
                return True
            elif baseNum == 4:
                self.currentField.addOneToOuts()
                print  "Player got out on home plate!"
                self.gameString.append({"code" : "OUT-HP", "description" : "Out! " + self.currentField.home.getPlayerOnBase().toString() + " was thrown out at Home! Out " + str(self.currentAmountOfOuts + self.currentField.getOuts())})
                return True
            else:
                print "SOMETHING WENT WRONG"

        print "Player made it to base safely!" + str(b)
        return False

    def playerOnThird(self):
        if self.currentField.three.getPlayerOnBase() is None:
            pass
        else:
            try:
                self.currentField.three.movePlayerOneBase()
                test = self.isPlayerOutOnBase(4, self.checkIfPlayerIsOnSameBaseAsBall(4))
                if not test:

                    self.currentField.addScore()
                    print self.currentField.home.getPlayerOnBase().toString() + " has scored"
                    self.gameString.append({"code" : "RUN-SCORES", "description" : self.currentField.home.getPlayerOnBase().toString() + " has scored"})
            except ThreeOuts, args:
                print "3 outs have happened on the field"

    def newPlayerOnBasesWalk(self, p):
        print "amount of bases to move is 1, walk "

        if self.currentField.one.getPlayerOnBase(): # If someone is on FIRST
            if self.currentField.two.getPlayerOnBase(): # If someone is on SECOND
                if self.currentField.three.getPlayerOnBase(): # If someone is on THIRD
                    # Score, move player home
                    self.currentField.three.movePlayerOneBase()
                    self.currentField.addScore()
                    print self.currentField.home.getPlayerOnBase().toString() + " has scored"
                    self.gameString.append({"code" : "RUN-SCORES", "description" : self.currentField.home.getPlayerOnBase().toString() + " has scored"})
                # Move SECOND to THIRD
                self.currentField.two.movePlayerOneBase()
            # MOVE FIRST to SECOND
            self.currentField.one.movePlayerOneBase()
            # PLACE BATTER on FIRST
            self.currentField.one.addPlayerToBase(p)
        else:
            # PLACE BATTER on FIRST
            self.currentField.one.addPlayerToBase(p)

    def newPlayerOnBasesHomerun(self, p):
        print "Homerun!!"
        if not self.currentField.three.getPlayerOnBase() is None:
            self.currentField.three.movePlayerOneBase()
            self.currentField.addScore()
            print self.currentField.home.getPlayerOnBase().toString() + " has scored"
            self.gameString.append({"code" : "RUN-SCORES", "description" : self.currentField.home.getPlayerOnBase().toString() + " has scored"})

        if not self.currentField.two.getPlayerOnBase() is None:
            self.currentField.two.movePlayerOneBase()
            self.currentField.three.movePlayerOneBase()
            self.currentField.addScore();
            print self.currentField.home.getPlayerOnBase().toString() + " has scored"
            self.gameString.append({"code" : "RUN-SCORES", "description" : self.currentField.home.getPlayerOnBase().toString() + " has scored"})

        if not self.currentField.one.getPlayerOnBase() is None:
            self.currentField.one.movePlayerOneBase()
            self.currentField.two.movePlayerOneBase()
            self.currentField.three.movePlayerOneBase()
            self.currentField.addScore();
            print self.currentField.home.getPlayerOnBase().toString() + " has scored"
            self.gameString.append({"code" : "RUN-SCORES", "description" : self.currentField.home.getPlayerOnBase().toString() + " has scored"})

        self.currentField.one.addPlayerToBase(p)
        self.currentField.one.movePlayerOneBase()
        self.currentField.two.movePlayerOneBase()
        self.currentField.three.movePlayerOneBase()
        self.currentField.addScore()
        print self.currentField.home.getPlayerOnBase().toString() + " has scored"
        self.gameString.append({"code" : "RUN-SCORES", "description" : self.currentField.home.getPlayerOnBase().toString() + " has scored"})

    def getGameString(self):
     return self.gameString

class ThreeOuts(Exception):
 def __init__(self, arg):
  self.msg = arg
