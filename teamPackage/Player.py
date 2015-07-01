# package teamPackage

class Player(object):
    def __init__(self):
        self.name = ""
        self.chance_Single = 0
        self.chance_Double = 0
        self.chance_Triple = 0
        self.chance_Homerun = 0
        self.IPR = 0
        self.hits = 0
        self.o_Swing = 0
        self.z_Swing = 0
        self.o_Contact = 0
        self.z_Contact = 0
        self.FP = 0
        self.position = ""
        clonedData = []

    def Player(self, playerData):
        #batting_players.append(([row["Name"].replace(" ", ""), row["Position"], float(row["H"]), float(row["IPR"]), float(row["O-Swing%"]), float(row["Z-Swing%"]), float(row["O-Contact%"]), float(row["Z-Contact%"]), float(row["1B%"]), float(row["2B%"]), float(row["3B%"]), float(row["HR%"]), float(row["FP"])]))
        name = playerData[0]
        set_Position(playerData[1])
        set_Hits((playerData[2]))
        set_IPR((playerData[3]))
        set_o_Swing((playerData[4]))
        set_z_Swing((playerData[5]))
        set_o_Contact((playerData[6]))
        set_z_Contact((playerData[7]))
        set_Chance_Single((playerData[8]))
        set_Chance_Double((playerData[9]))
        set_Chance_Triple((playerData[10]))
        set_Chance_Homerun((playerData[11]))
        set_FP((playerData[12]))

        clonedData = playerData

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
        return self.IPR

    def set_IPR(self, iPR):
        self.IPR = iPR

    def get_Hits(self):
        return self.hits

    def set_Hits(self, Hits):
        self.hits = Hits

    def get_o_Swing(self):
        return self.o_Swing

    def set_o_Swing(self, O_Swing):
        self.o_Swing = O_Swing

    def get_z_Swing(self):
        return self.z_Swing

    def set_z_Swing(self, Z_Swing):
        self.z_Swing = Z_Swing

    def get_o_Contact(self):
        return self_o_Contact

    def set_o_Contact(self, O_Contact):
        self.o_Contact = O_Contact

    def get_z_Contact(self):
        return self.z_Contact

    def set_z_Contact(self, Z_Contact):
        self.z_Contact = Z_Contact

    def get_FP(self):
        return self.FP

    def set_FP(self, fP):
        self.FP = fP

    def get_Position(self):
        return self.position

    def set_Position(self, Position):
        self.position = Position

    def duplicate_Player(temp):
        return new (temp.clonedData)
