#!/usr/bin/python

# package teamPackage

class Team(object):

    def __init__(self):
     self.playerAtBat = -1
     self.fullTeam = []
     self.players = []
     self.fieldingRoster = []
     self.missingPositions = []
     self.teamName = "temp"
     self.score = 0
     self.outs = 0
     self.found = False
     self.count = 0

    def configFieldingRoster(self):
        self.fieldingRoster.append(self.getPlayerFromArray("LF"))
        self.fieldingRoster.append(self.getPlayerFromArray("CF"))
        self.fieldingRoster.append(self.getPlayerFromArray("RF"))
        self.fieldingRoster.append(self.getPlayerFromArray("3B"))
        self.fieldingRoster.append(self.getPlayerFromArray("SS"))
        self.fieldingRoster.append(self.getPlayerFromArray("2B"))
        self.fieldingRoster.append(self.getPlayerFromArray("1B"))
        self.fieldingRoster.append(self.getPlayerFromArray("C"))
        self.fieldingRoster.append(self.getPlayerFromArray("P"))

        for x in range(0, len(self.fieldingRoster)):
            if self.fieldingRoster[x] == False:
                temp = self.fillPlayerSpot()
                temp2 = temp.duplicatePlayer()
                self.fieldingRoster[x]= temp2
                self.fieldingRoster[x].setPosition(self.missingPositions[0]);
                self.missingPositions.pop(0)
                #self.missing_Positions.remove(0)

        for h in range (0, len(self.fieldingRoster)):
            print self.fieldingRoster[h].toString()


    def getPlayerInFieldingPostion(self,pos):
     for x in range(0, len(self.fieldingRoster)):
        if self.fieldingRoster[x].getPosition() == pos:
                return self.fieldingRoster[x]

     print "null player found this is very bad " + pos
     return None


    def fillPlayerSpot(self):
     playerOnList = False
     for x in range (0, len(self.fullTeam)):
        for y in range(0, len(self.fieldingRoster)):
            if self.fieldingRoster[y] != False:
                if self.fullTeam[x].toString() == self.fieldingRoster[y].toString():
                    playerOnList = True
            if not playerOnList:
                return self.fullTeam[x]

     return None


    def getPlayerFromArray(self, position):
        self.count = 0;
        self.found = False;
        while not self.found and self.count < len(self.fullTeam):
            if self.fullTeam[self.count].getPosition() == position:
                return self.fullTeam[self.count]
            else:
                self.count = self.count + 1
        self.missingPositions.append(position)
        return False

    def configBattingRoster(self):
     for x in range(0,8):
        self.players.append(self.fullTeam[x])
     self.players.append(self.fullTeam[(len(self.fullTeam)-1)])


    def addOneToScore(self):
     self.score+=1

    def addNumToScore(self, n):
     self.score = self.score + n

    def addOneToOuts(self):
     self.outs+=1

    def addNumToOuts(self, o):
     self.outs = self.outs + o

    def setOutsToZero(self):
     self.outs = 0

    def getOuts(self):
     return self.outs

    def getScore(self):
     return self.score

    def addPlayer(self, p):
     self.fullTeam.append(p)

    def getPlayer(self, index):
     return self.players.get(index)

    def getNextPlayerAtBat(self):
     self.playerAtBat = self.playerAtBat + 1
     return self.players[self.playerAtBat % 7]

    def getPitcher(self):
     return self.players[8]

    def getTeamName(self):
     return self.teamName

    def setTeamName(self, TeamName):
     self.teamName = TeamName
