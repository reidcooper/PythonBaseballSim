# teamPackage
import os
import sys
var = os.path.abspath(os.path.dirname(__file__)+'../..')
sys.path.append(var)

from Team import Team
from Player import Player
from Pitcher import Pitcher


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

        self.home = self.createTeam(self.teamNameHome)
        self.away = self.createTeam(self.teamNameAway)

        self.teams = [self.home, self.away]

        return self.teams

    def createTeam(self, teamName):
        #batting_players.append(([row["Name"].replace(" ", ""), row["Position"], float(row["H"]), float(row["IPR"]), float(row["O-Swing%"]), float(row["Z-Swing%"]), float(row["O-Contact%"]), float(row["Z-Contact%"]), float(row["1B%"]), float(row["2B%"]), float(row["3B%"]), float(row["HR%"]), float(row["FP"])]))
        team = Team()
        team.setTeamName(teamName)
        temp2 = 0

        if teamName == "Yankees":
            self.teamBatting = "static/teams/Yankees_batting.txt"
            self.teamPitching = "static/teams/Yankees_pitchers.txt"
        elif teamName == "Phillies":
            self.teamBatting = "static/teams/Phillies_batting.txt"
            self.teamPitching = "static/teams/Phillies_pitchers.txt"
        elif teamName == "Red-Sox":
            self.teamBatting = "static/teams/Red-Sox_batting.txt"
            self.teamPitching = "static/teams/Red-Sox_pitchers.txt"
        elif teamName == "Angels":
            self.teamBatting = "static/teams/Angels_batting.txt"
            self.teamPitching = "static/teams/Angels_pitchers.txt"
        elif teamName == "White-Sox":
            self.teamBatting = "static/teams/White-Sox_batting.txt"
            self.teamPitching = "static/teams/White-Sox_pitchers.txt"
        elif teamName == "Cubs":
            self.teamBatting = "static/teams/Cubs_batting.txt"
            self.teamPitching = "static/teams/Cubs_pitchers.txt"
        elif teamName == "Mets":
            self.teamBatting = "static/teams/Mets_batting.txt"
            self.teamPitching = "static/teams/Mets_pitchers.txt"
        elif teamName == "Giants":
            self.teamBatting = "static/teams/Giants_batting.txt"
            self.teamPitching = "static/teams/Giants_pitchers.txt"
        elif teamName == "Twins":
            self.teamBatting = "static/teams/Twins_batting.txt"
            self.teamPitching = "static/teams/Twins_pitchers.txt"
        elif teamName == "Tigers":
            self.teamBatting = "static/teams/Tigers_batting.txt"
            self.teamPitching = "static/teams/Tigers_pitchers.txt"
        elif teamName == "Cardinals":
            self.teamBatting = "static/teams/Cardinals_batting.txt"
            self.teamPitching = "static/teams/Cardinals_pitchers.txt"
        elif teamName == "Dodgers":
            self.teamBatting = "static/teams/Dodgers_batting.txt"
            self.teamPitching = "static/teams/Dodgers_pitchers.txt"
        elif teamName == "Rangers":
            self.teamBatting = "static/teams/Rangers_batting.txt"
            self.teamPitching = "static/teams/Rangers_pitchers.txt"
        elif teamName == "Rockies":
            self.teamBatting = "static/teams/Rockies_batting.txt"
            self.teamPitching = "static/teams/Rockies_pitchers.txt"
        elif teamName == "Braves":
            self.teamBatting = "static/teams/Braves_batting.txt"
            self.teamPitching = "static/teams/Braves_pitchers.txt"
        elif teamName == "Mariners":
            self.teamBatting = "static/teams/Mariners_batting.txt"
            self.teamPitching = "static/teams/Mariners_pitchers.txt"
        elif teamName == "Brewers":
            self.teamBatting = "static/teams/Brewers_batting.txt"
            self.teamPitching = "static/teams/Brewers_pitchers.txt"
        elif teamName == "Orioles":
            self.teamBatting = "static/teams/Orioles_batting.txt"
            self.teamPitching = "static/teams/Orioles_pitchers.txt"
        elif teamName == "Reds":
            self.teamBatting = "static/teams/Reds_batting.txt"
            self.teamPitching = "static/teams/Reds_pitchers.txt"
        elif teamName == "Astros":
            self.teamBatting = "static/teams/Astros_batting.txt"
            self.teamPitching = "static/teams/Astros_pitchers.txt"
        elif teamName == "Athletics":
            self.teamBatting = "static/teams/Athletics_batting.txt"
            self.teamPitching = "static/teams/Athletics_pitchers.txt"
        elif teamName == "Nationals":
            self.teamBatting = "static/teams/Nationals_batting.txt"
            self.teamPitching = "static/teams/Nationals_pitchers.txt"
        elif teamName == "Blue-Jays":
            self.teamBatting = "static/teams/Blue-Jays_batting.txt"
            self.teamPitching = "static/teams/Blue-Jays_pitchers.txt"
        elif teamName == "Marlins":
            self.teamBatting = "static/teams/Marlins_batting.txt"
            self.teamPitching = "static/teams/Marlins_pitchers.txt"
        elif teamName == "Diamondbacks":
            self.teamBatting = "static/teams/Diamondbacks_batting.txt"
            self.teamPitching = "static/teams/Diamondbacks_pitchers.txt"
        elif teamName == "Indians":
            self.teamBatting = "static/teams/Indians_batting.txt"
            self.teamPitching = "static/teams/Indians_pitchers.txt"
        elif teamName == "Padres":
            self.teamBatting = "static/teams/Padres_batting.txt"
            self.teamPitching = "static/teams/Padres_pitchers.txt"
        elif teamName == "Pirates":
            self.teamBatting = "static/teams/Pirates_batting.txt"
            self.teamPitching = "static/teams/Pirates_pitchers.txt"
        elif teamName == "Rays":
            self.teamBatting = "static/teams/Rays_batting.txt"
            self.teamPitching = "static/teams/Rays_pitchers.txt"
        elif teamName == "Royals":
            self.teamBatting = "static/teams/Royals_batting.txt"
            self.teamPitching = "static/teams/Royals_pitchers.txt"
        else:
            print "enter a valid team, capitalize"


        scanner = open(var + "/"+ self.teamBatting, "r")
        scanner2 = open(var + "/" + self.teamPitching, "r")


        for line in scanner:
                playerData = line.split()
                player = Player(playerData)
                team.addPlayer(player)

        for line in scanner2:# find a better way!
                if temp2 < self.pitcherCount:
                    playerData = ["0"] * 13
                    pitcherData = line.split()
                    pitcher = Pitcher(playerData, pitcherData)
                    team.addPlayer(pitcher)
                    temp2 = temp2 + 1

        team.configBattingRoster()
        team.configFieldingRoster()

        scanner.close()
        scanner2.close()

        return team
