#!/usr/bin/python

# package teamPackage

class Player(object):

    name = ""
    chance_Single = 0
    chance_Double = 0
    chance_Triple = 0
    chance_Homerun = 0
    IPR = 0
    hits = 0
    o_Swing = 0
    z_Swing = 0
    o_Contact = 0
    z_Contact = 0
    FP = 0
    position = ""
    clonedData = []

    def __init__(self, playerData):
        #batting_players.append(([row["Name"].replace(" ", ""), row["Position"], float(row["H"]), float(row["IPR"]), float(row["O-Swing%"]), float(row["Z-Swing%"]), float(row["O-Contact%"]), float(row["Z-Contact%"]), float(row["1B%"]), float(row["2B%"]), float(row["3B%"]), float(row["HR%"]), float(row["FP"])]))
        self.name = playerData[0]
        self.set_Position(playerData[1])
        self.set_Hits((playerData[2]))
        self.set_IPR((playerData[3]))
        self.set_o_Swing((playerData[4]))
        self.set_z_Swing((playerData[5]))
        self.set_o_Contact((playerData[6]))
        self.set_z_Contact((playerData[7]))
        self.set_Chance_Single((playerData[8]))
        self.set_Chance_Double((playerData[9]))
        self.set_Chance_Triple((playerData[10]))
        self.set_Chance_Homerun((playerData[11]))
        self.set_FP((playerData[12]))

        self.clonedData = playerData

    def to_String(self):
        return self.name + " " + self.position

    def get_Chance_Single(self):
        return self.chance_Single

    def set_Chance_Single(self,Chance_Single):
        self.chance_Single = Chance_Single

    def get_Chance_Double(self):
        return self.chance_Double

    def set_Chance_Double(self,Chance_Double):
        self.chance_Double = Chance_Double

    def get_Chance_Triple(self):
        return self.chance_Triple

    def set_Chance_Triple(self,Chance_Triple):
        self.chance_Triple = Chance_Triple

    def get_Chance_Homerun(self):
        return self.chance_Homerun

    def set_Chance_Homerun(self, Chance_Homerun):
        self.chance_Homerun = Chance_Homerun

    def get_IPR(self):
        return float(self.IPR)

    def set_IPR(self, iPR):
        self.IPR = iPR

    def get_Hits(self):
        return float(self.hits)

    def set_Hits(self, Hits):
        self.hits = Hits

    def get_o_Swing(self):
        return float(self.o_Swing)

    def set_o_Swing(self, O_Swing):
        self.o_Swing = O_Swing

    def get_z_Swing(self):
        return float(self.z_Swing)

    def set_z_Swing(self, Z_Swing):
        self.z_Swing = Z_Swing

    def get_o_Contact(self):
        return float(self.o_Contact)

    def set_o_Contact(self, O_Contact):
        self.o_Contact = O_Contact

    def get_z_Contact(self):
        return float(self.z_Contact)

    def set_z_Contact(self, Z_Contact):
        self.z_Contact = Z_Contact

    def get_FP(self):
        return float(self.FP)

    def set_FP(self, fP):
        self.FP = fP

    def get_Position(self):
        return self.position

    def set_Position(self, Position):
        self.position = Position

    def duplicate_Player(self):
        return Player(self.clonedData)
