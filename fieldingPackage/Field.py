import os
import sys
import traceback
var = os.path.abspath(os.path.dirname(__file__)+'../..')
sys.path.append(var)

from random import random
from teamPackage import Player

class Field(object):

    def __init__(self, currentField):
        self.currentField = currentField
        self.temp = []
        self.currentAmountOfOuts = 0

    def newPlayerOnBases(self, n, p, currentAmountOfOuts, walkOrHomeRun):
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
                            self.isPlayerOutOnBase(3, self.checkIfPlayerIsOnSameBaseAsBall(3))
                            if n >= 2:
                                self.playerOnThird()

                        if not (self.currentField.one.getPlayerOnBase() is None):
                            if n == 1:
                                self.currentField.one.movePlayerOneBase()
                                self.isPlayerOutOnBase(2, self.checkIfPlayerIsOnSameBaseAsBall(2))
                                self.moveOneBase(p)
                                #break
                            elif n == 2:
                                self.currentField.one.movePlayerOneBase()
                                self.isPlayerOutOnBase(2, self.checkIfPlayerIsOnSameBaseAsBall(2))
                                self.currentField.two.movePlayerOneBase()
                                self.isPlayerOutOnBase(3, self.checkIfPlayerIsOnSameBaseAsBall(3))
                                self.moveTwoBases(p)
                                #break
                            elif n == 3:
                                self.currentField.one.movePlayerOneBase()
                                self.isPlayerOutOnBase(2, self.checkIfPlayerIsOnSameBaseAsBall(2))
                                self.currentField.two.movePlayerOneBase()
                                self.isPlayerOutOnBase(3, self.checkIfPlayerIsOnSameBaseAsBall(3))
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
        #rand = (rand.randint()*100)
        #if rand > 60:
        #return True
        #else:
        #return False

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
        if b:
            print "Player may get out on base"
            if baseNum == 1:
                self.currentField.addOneToOuts()
                print "Player got out on 1st base!"
                self.currentField.one.removePlayerFromBase()
                return True
            elif baseNum == 2:
                self.currentField.addOneToOuts()
                print "Player got out on 2nd base!"
                self.currentField.two.removePlayerFromBase()
                return True
            elif baseNum ==3 :
                self.currentField.addOneToOuts()
                print "Player got out on 3rd base!"
                self.currentField.three.removePlayerFromBase()
                return True
            elif baseNum == 4:
                self.currentField.addOneToOuts()
                print  "Player got out on home plate!"
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
                test = self.isPlayerOutOnBase(4, self.checkIfPlayerIsOnSameBaseAsBall(4))
                if not test:
                    self.currentField.three.movePlayerOneBase()
                    self.currentField.addScore()
                    print self.currentField.home.getPlayerOnBase().to_String() + " has scored"
            except ThreeOuts, args:
                print "3 outs have happened on the field"

    def newPlayerOnBasesWalk(self, p):
        print "amount of bases to move is 1, walk "
        if not self.currentField.one.getPlayerOnBase() is None:
            self.currentField.one.movePlayerOneBase()
            if not self.currentField.two.getPlayerOnBase() is None:
             self.currentField.two.movePlayerOnBase()
             if not self.currentField.three.getPlayerOnBase() is None:
                self.currentField.three.getPlayerOnBase() is None
        else:
            self.currentField.one.addPlayerToBase(p)

    def newPlayerOnBasesHomerun(self, p):
        print "Homerun!!"
        if not self.currentField.three.getPlayerOnBase() is None:
            self.currentField.three.movePlayerOneBase()
            self.currentField.addScore()
            print self.currentField.home.getPlayerOnBase().to_String() + " has scored"

        if not self.currentField.two.getPlayerOnBase() is None:
            self.currentField.two.movePlayerOneBase()
            self.currentField.three.movePlayerOneBase()
            self.currentField.addScore();
            print self.currentField.home.getPlayerOnBase().to_String() + " has scored"

        if not self.currentField.one.getPlayerOnBase() is None:
            self.currentField.one.movePlayerOneBase()
            self.currentField.two.movePlayerOneBase()
            self.currentField.three.movePlayerOneBase()
            self.currentField.addScore();
            print self.currentField.home.getPlayerOnBase().to_String() + " has scored"

        self.currentField.one.addPlayerToBase(p)
        self.currentField.one.movePlayerOneBase()
        self.currentField.two.movePlayerOneBase()
        self.currentField.three.movePlayerOneBase()
        self.currentField.addScore()
        print self.currentField.home.getPlayerOnBase().to_String() + " has scored"
        print "amount of outs " + str(self.currentField.getOuts())

class ThreeOuts(Exception):
 def __init__(self, arg):
  self.msg = arg
