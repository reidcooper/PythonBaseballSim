# teamPackage
import os
import sys
var = os.path.abspath(os.path.dirname(__file__)+'../..')
sys.path.append(var)

from Team import Team

class CreateTeam(object):

    home = Team()
    away = Team()
    teamNameHome = ""
    teamNameAway = ""
    teamCounter = 0
    pitcherCount = 1
    battingLineup = 9

    teamBatting = ""
    teamPitching = ""

    def createTeams(self, teamNameHome, teamNameAway):
        self.teamNameHome = teamNameHome
        self.teamNameAway = teamNameAway

        self.home = createTeam(self.teamNameHome)
        self.away = createTeam(self.teamNameAway)

        self.teams = [self.home, self.away]

        return self.teams

    def createTeam(self, teamName):
        #batting_players.append(([row["Name"].replace(" ", ""), row["Position"], float(row["H"]), float(row["IPR"]), float(row["O-Swing%"]), float(row["Z-Swing%"]), float(row["O-Contact%"]), float(row["Z-Contact%"]), float(row["1B%"]), float(row["2B%"]), float(row["3B%"]), float(row["HR%"]), float(row["FP"])]))
        team = Team()
        team.set_Team_Name(teamName)
        temp2 = 0

        if teamName == "Yankees":
            self.teamBatting = "team/Yankees_batting.txt"
            self.teamPitching = "team/Yankees_pitchers.txt"
        elif teamName == "Phillies":
            self.teamBatting = "team/Phillies_batting.txt"
            self.teamPitching = "team/Phillies_pitchers.txt"
        elif teamName == "Red_Sox":
            self.teamBatting = "team/Red_Sox_batting.txt"
            self.teamPitching = "team/Red_Sox_pitchers.txt"
        elif teamName == "Angels":
            self.teamBatting = "team/Angels_batting.txt"
            self.teamPitching = "team/Angels_pitchers.txt"
        elif teamName == "White_Sox":
            self.teamBatting = "team/White_Sox_batting.txt"
            self.teamPitching = "team/White_Sox_pitchers.txt"
        elif teamName == "Cubs":
            self.teamBatting = "team/Cubs_batting.txt"
            self.teamPitching = "team/Cubs_pitchers.txt"
        elif teamName == "Mets":
            self.teamBatting = "team/Mets_batting.txt"
            self.teamPitching = "team/Mets_pitchers.txt"
        elif teamName == "Giants":
            self.teamBatting = "team/Giants_batting.txt"
            self.teamPitching = "team/Giants_pitchers.txt"
        elif teamName == "Twins":
            self.teamBatting = "team/Twins_batting.txt"
            self.teamPitching = "team/Twins_pitchers.txt"
        elif teamName == "Tigers":
            self.teamBatting = "team/Tigers_batting.txt"
            self.teamPitching = "team/Tigers_pitchers.txt"
        elif teamName == "Cardinals":
            self.teamBatting = "team/Cardinals_batting.txt"
            self.teamPitching = "team/Cardinals_pitchers.txt"
        elif teamName == "Dodgers":
            self.teamBatting = "team/Dodgers_batting.txt"
            self.teamPitching = "team/Dodgers_pitchers.txt"
        elif teamName == "Rangers":
            self.teamBatting = "team/Rangers_batting.txt"
            self.teamPitching = "team/Rangers_pitchers.txt"
        elif teamName == "Rockies":
            self.teamBatting = "team/Rockies_batting.txt"
            self.teamPitching = "team/Rockies_pitchers.txt"
        elif teamName == "Braves":
            self.teamBatting = "team/Braves_batting.txt"
            self.teamPitching = "team/Braves_pitchers.txt"
        elif teamName == "Mariners":
            self.teamBatting = "team/Mariners_batting.txt"
            self.teamPitching = "team/Mariners_pitchers.txt"
        elif teamName == "Brewers":
            self.teamBatting = "team/Brewers_batting.txt"
            self.teamPitching = "team/Brewers_pitchers.txt"
        elif teamName == "Orioles":
            self.teamBatting = "team/Orioles_batting.txt"
            self.teamPitching = "team/Orioles_pitchers.txt"
        elif teamName == "Reds":
            self.teamBatting = "team/Reds_batting.txt"
            self.teamPitching = "team/Reds_pitchers.txt"
        elif teamName == "Astros":
            self.teamBatting = "team/Astros_batting.txt"
            self.teamPitching = "team/Astros_pitchers.txt"
        elif teamName == "Athletics":
            self.teamBatting = "team/Athletics_batting.txt"
            self.teamPitching = "team/Athletics_pitchers.txt"
        elif teamName == "Nationals":
            self.teamBatting = "team/Nationals_batting.txt"
            self.teamPitching = "team/Nationals_pitchers.txt"
        elif teamName == "Blue_Jays":
            self.teamBatting = "team/Blue_Jays_batting.txt"
            self.teamPitching = "team/Blue_Jays_pitchers.txt"
        elif teamName == "Marlins":
            self.teamBatting = "team/Marlins_batting.txt"
            self.teamPitching = "team/Marlins_pitchers.txt"
        elif teamName == "Diamondbacks":
            self.teamBatting = "team/Diamondbacks_batting.txt"
            self.teamPitching = "team/Diamondbacks_pitchers.txt"
        elif teamName == "Indians":
            self.teamBatting = "team/Indians_batting.txt"
            self.teamPitching = "team/Indians_pitchers.txt"
        elif teamName == "Padres":
            self.teamBatting = "team/Padres_batting.txt"
            self.teamPitching = "team/Padres_pitchers.txt"
        elif teamName == "Pirates":
            self.teamBatting = "team/Pirates_batting.txt"
            self.teamPitching = "team/Pirates_pitchers.txt"
        elif teamName == "Rays":
            self.teamBatting = "team/Rays_batting.txt"
            self.teamPitching = "team/Rays_pitchers.txt"
        elif teamName == "Royals":
            self.teamBatting = "team/Royals_batting.txt"
            self.teamPitching = "team/Royals_pitchers.txt"
        else:
            print "enter a valid team, capitalize"

        try:
            scanner = open(teamBatting, "r")
            scanner2 = open(teamPitching, "r")

            for line in scanner:
                playerData = scanner.readline().split()
                player = Player(playerData)
                team.add_Player(player)

            for line in scanner2:# find a better way!
                if temp2 < pitchCount:
                    playerData = ["0"] * 13
                    pitcherData = scanner2.readline().split()
                    pitcher = Pitcher(playerData, pitcherData)
                    team.add_Player(pitcher)
                    temp2 += 1

            team.config_Batting_Roster()
            team.config_Fielding_Roster()

        except:
            print "Unexpected error"

        scanner.close()
        scanner2.close()

        return team
