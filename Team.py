

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
     self.found = false
     self.count = 0

    def config_Fielding_Roster(self):
    
     self.fielding_Roster.append(get_Player_From_Array("LF"))
     self.fielding_Roster.append(get_Player_From_Array("CF"))
     self.fielding_Roster.append(get_Player_From_Array("RF"))
     self.fielding_Roster.append(get_Player_From_Array("3B"))
     self.fielding_Roster.append(get_Player_From_Array("SS"))
     self.fielding_Roster.append(get_Player_From_Array("2B"))
     self.fielding_Roster.append(get_Player_From_Array("1B"))
     self.fielding_Roster.append(get_Player_From_Array("C"))
     self.fielding_Roster.append(get_Player_From_Array("P"))

    for x in range(0,len(self.fielding_Roster)): 
        if fieldingRoster.get(x) == null:
             temp = Player.fill_Player_Spot()
             temp2 = temp.duplicatePlayer(temp)
             fieldingRoster[x]= temp
             fieldingRoster[x].setPosition(missing_Positions.get(0));
             missingPositions.remove(0)
        x+=1
    
    
    for h in range (0, len(self.fielding_Roster)):
        print self.fielding_Roster.get(h)
        h+=1
    


    def getPlayer_InFielding_Postion(self,pos):
     for x in range(0, len(self.fielding_Roster)): 
        if self.fielding_Roster.get(x).getPosition() == pos:
                return self.fielding_Roster.get(x)
            
        
    
     print "null player found this is very bad " + pos
     return null


    def fill_Player_Spot(self):
    
     player_On_List = false
    
     for x in range (0, len(self.full_Team)):
        for y in range(0, len(self.fielding_Roster)):
            if self.fielding_Roster.get(y) != null:
                if fullTeam.get(x).toString() == self.fielding_Roster.get(y).toString() == true:
                    playerOnList = true
                    
                 
            
            if not player_On_List:
                return full_Team.get(x)
            
        
    
    
     return null


    def get_PlayerFrom_Array(self,position):
     self.count = 0;
     self.found = false;
    
    while not found and count < len(full_Team()):
        
        if full_Team.get(count).get_Position() == position:
            return fullTeam.get(count)
         else:
             count+=1
    
     missingPositions.append(position)
     return null

    def config_Batting_Roster(self):
    
     for x in range(0,8):
        players.append(full_Team.get(x))
                x+=1
    
     players.append(full_Team.get(len(full_Team)-1))


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


    def get_Outs():
     return outs


    def get_Score():
     return score


    def add_Player(p):
     full_Team.append(p)


    def get_Player(self, index):
     return self.players.get(index);


    def get_Next_Player_At_Bat(self){
     self.player_At_Bat+=1
     return players.get(player_At_Bat % 7)


    def get_Pitcher():
     return (Pitcher) players.get(8)


    def get_Team_Name(self):
     return self.team_Name


    def set_Team_Name(self, Team_Name):
     self.team_Name = Team_Name


