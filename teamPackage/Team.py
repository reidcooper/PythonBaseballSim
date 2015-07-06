#!/usr/bin/python

# package teamPackage

class Team(object):

    def __init__(self):
     self.player_At_Bat = -1
     self.full_Team = []
     self.players = []
     self.fielding_Roster = []
     self.missing_Positions = []
     self.team_Name = "temp"
     self.score = 0
     self.outs = 0
     self.found = False
     self.count = 0

    def config_Fielding_Roster(self):
        self.fielding_Roster.append(self.get_Player_From_Array("LF"))
        self.fielding_Roster.append(self.get_Player_From_Array("CF"))
        self.fielding_Roster.append(self.get_Player_From_Array("RF"))
        self.fielding_Roster.append(self.get_Player_From_Array("3B"))
        self.fielding_Roster.append(self.get_Player_From_Array("SS"))
        self.fielding_Roster.append(self.get_Player_From_Array("2B"))
        self.fielding_Roster.append(self.get_Player_From_Array("1B"))
        self.fielding_Roster.append(self.get_Player_From_Array("C"))
        self.fielding_Roster.append(self.get_Player_From_Array("P"))

        for x in range(0, len(self.fielding_Roster)):
            if self.fielding_Roster[x] == False:
                temp = self.fill_Player_Spot()
                temp2 = temp.duplicate_Player()
                self.fielding_Roster[x]= temp
                self.fielding_Roster[x].set_Position(self.missing_Positions[0]);
                self.missing_Positions.pop(0)
                #self.missing_Positions.remove(0)

        for h in range (0, len(self.fielding_Roster)):
            print self.fielding_Roster[h]


    def get_Player_In_Fielding_Postion(self,pos):
     for x in range(0, len(self.fielding_Roster)):
        if self.fielding_Roster.get(x).getPosition() == pos:
                return self.fielding_Roster.get(x)

     print "null player found this is very bad " + pos
     return None


    def fill_Player_Spot(self):
     player_On_List = False
     for x in range (0, len(self.full_Team)):
        for y in range(0, len(self.fielding_Roster)):
            if self.fielding_Roster[y] != False:
                if self.full_Team[x].to_String() == self.fielding_Roster[y].to_String():
                    playerOnList = True
            if not player_On_List:
                return self.full_Team[x]

     return none


    def get_Player_From_Array(self, position):
        self.count = 0;
        self.found = False;
        while not self.found and self.count < len(self.full_Team):
            if self.full_Team[self.count].get_Position() == position:
                return self.full_Team[self.count]
            else:
                self.count = self.count + 1
        self.missing_Positions.append(position)
        return False

    def config_Batting_Roster(self):
     for x in range(0,8):
        self.players.append(self.full_Team[x])
     self.players.append(self.full_Team[(len(self.full_Team)-1)])


    def addOneToScore(self):
     self.score+=1

    def add_Num_To_Score(self, n):
     self.score = self.score + n

    def add_One_To_Outs(self):
     self.outs+=1

    def add_Num_To_Outs(self, o):
     self.outs = self.outs + o

    def set_Outs_To_Zero(self):
     self.outs = 0

    def get_Outs(self):
     return self.outs

    def get_Score(self):
     return self.score

    def add_Player(self, p):
     self.full_Team.append(p)

    def get_Player(self, index):
     return self.players.get(index)

    def get_Next_Player_At_Bat(self):
     self.player_At_Bat = self.player_At_Bat + 1
     print self.player_At_Bat % 7
     return self.players[self.player_At_Bat % 7]

    def get_Pitcher(self):
     return self.players[8]

    def get_Team_Name(self):
     return self.team_Name

    def set_Team_Name(self, Team_Name):
     self.team_Name = Team_Name
