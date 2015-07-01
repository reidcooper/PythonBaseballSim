

import battingPackage.Batting
import battingPackage.CurrentBatting
import teamPackage.CreateTeam
import teamPackage.Player
import teamPackage.Team
import fieldingPackage.CurrentField
import fieldingPackage.Field


class Game(object):
	
 def __init__(self,home, away):
    CreateTeam.ct =  CreateTeam()
    Team.teams = ct.createTeams(home, away)
    Batting.bat = Batting()
    CurrentFielding.cf = CurrentField()
    Field.f = Field(cf)
    self.amountOfBasesToMove = 0
    Player.currentBattingPlayer = null
    self.battingTeam = 0
    self.pitchingTeam = 1
    self.initOrder = true
    self.innings = 1
    self.outsToBeAdded = 0

 def switchTeams():
    if initOrder == true:
        battingTeam = 1
        pitchingTeam = 0
        initOrder = false
	
    else:
        battingTeam = 0
        pitchingTeam = 1
        initOrder = true

 def teamAtBat():
    cf.start(teams[pitchingTeam])
    while teams[battingTeam].getOuts() < 3:
        currentBattingPlayer = teams[battingTeam].getNextPlayerAtBat()
        CurrentBatting.cb = CurrentBatting(teams[pitchingTeam].getPitcher(), currentBattingPlayer)
        amountOfBasesToMove = bat.startBatting(cb)
        
        if amountOfBasesToMove > 0:
            outsToBeAdded = f.newPlayerOnBases(amountOfBasesToMove, currentBattingPlayer, teams[battingTeam].getOuts(), cb.getHomerunOrWalk())
            if outsToBeAdded > 0:
                teams[battingTeam].addNumToOuts(outsToBeAdded)
        else:
            teams[battingTeam].addOneToOuts()
            print "OUT HAS HAPPENED " + teams[battingTeam].getOuts()
        teams[battingTeam].addNumToScore(cf.getScore())
        teams[battingTeam].setOutsToZero()
        cf.reset()


 def inning():
    teamAtBat()
    print "NEW TEAM AT BAT"
    print 
    switchTeams()
    teamAtBat()
    switchTeams()
    print "NEW TEAM AT BAT"
    print
    innings+= 1

 def playGame():
    while innings < 9:
        inning()
        print "score at end of inning " + innings + " is: " +"\n"
        +"Home Team: "+ teams[0].getScore() +"\n"+ "Away Team: "+ teams[1].getScore()

    while teams[0].getScore() == teams[1].getScore():
        inning()
        print "score at end of inning " + innings + " is: " +"\n"
        +"Home Team: "+ teams[0].getScore() +"\n" + "Away Team: "+ teams[1].getScore()

