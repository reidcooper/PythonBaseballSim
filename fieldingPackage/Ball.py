#!/usr/bin/python

# fieldingPackage

class Ball(object):
    pos1 = 0
    pos2 = 0
    ballPostion = [pos1, pos2]

    def setPostion(self, x, y):
        self.ballPostion[0] = x
        self.ballPostion[1] = y

    def getPostion(self):
        return self.ballPostion
