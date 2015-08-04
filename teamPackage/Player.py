#!/usr/bin/python

# package teamPackage

class Player(object):

    name = ""
    chanceSingle = 0
    chanceDouble = 0
    chanceTriple = 0
    chanceHomerun = 0
    IPR = 0
    hits = 0
    oSwing = 0
    zSwing = 0
    oContact = 0
    zContact = 0
    FP = 0
    position = ""
    clonedData = []

    def __init__(self, playerData):
        #batting_players.append(([row["Name"].replace(" ", ""), row["Position"], float(row["H"]), float(row["IPR"]), float(row["O-Swing%"]), float(row["Z-Swing%"]), float(row["O-Contact%"]), float(row["Z-Contact%"]), float(row["1B%"]), float(row["2B%"]), float(row["3B%"]), float(row["HR%"]), float(row["FP"])]))
        self.name = playerData[0]
        self.setPosition(playerData[1])
        self.setHits((playerData[2]))
        self.setIPR((playerData[3]))
        self.setOSwing((playerData[4]))
        self.setZSwing((playerData[5]))
        print
        print playerData[5]
        print
        self.setOContact((playerData[6]))
        self.setZContact((playerData[7]))
        self.setChanceSingle((playerData[8]))
        self.setChanceDouble((playerData[9]))
        self.setChanceTriple((playerData[10]))
        self.setChanceHomerun((playerData[11]))
        self.setFP((playerData[12]))

        self.clonedData = playerData

    def toString(self):
        return self.name

    def getChanceSingle(self):
        return float(self.chanceSingle)

    def setChanceSingle(self,chanceSingle):
        self.chanceSingle = chanceSingle

    def getChanceDouble(self):
        return float(self.chanceDouble)

    def setChanceDouble(self,chanceDouble):
        self.chanceDouble = chanceDouble

    def getChanceTriple(self):
        return float(self.chanceTriple)

    def setChanceTriple(self, chanceTriple):
        self.chanceTriple = chanceTriple

    def getChanceHomerun(self):
        return float(self.chanceHomerun)

    def setChanceHomerun(self, chanceHomerun):
        self.chanceHomerun = chanceHomerun

    def getIPR(self):
        return float(self.IPR)

    def setIPR(self, IPR):
        self.IPR = IPR

    def getHits(self):
        return float(self.hits)

    def setHits(self, Hits):
        self.hits = Hits

    def getOSwing(self):
        return float(self.oSwing)

    def setOSwing(self, oSwing):
        self.oSwing = oSwing

    def getZSwing(self):
        return float(self.zSwing)

    def setZSwing(self, zSwing):
        self.zSwing = zSwing

    def getOContact(self):
        return float(self.oContact)

    def setOContact(self, oContact):
        self.oContact = oContact

    def getZContact(self):
        return float(self.zContact)

    def setZContact(self, zContact):
        self.zContact = zContact

    def getFP(self):
        return float(self.FP)

    def setFP(self, fP):
        self.FP = fP

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def duplicatePlayer(self):
        return Player(self.clonedData)
