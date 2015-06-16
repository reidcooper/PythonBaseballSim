import csv

batting_players = []
batting_output = []
batting_text = []

pitching_players = []
pitching_output = []


def printBatting(team):
    with open('FanGraphs/FanGraphsBatting/2014_batting_master_withoutPercentage.csv', 'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        
        team_text = open("team.txt", "w")

        for row in reader:
            if (row["Team"] == team):
                # print(row["Name"], row["H"], row["IPR"])
                batting_players.append(([row["Name"], float(row["H"]), float(row["IPR"]), float(row["O-Swing%"]), float(row["Z-Swing%"]), float(row["O-Contact%"]), float(row["Z-Contact%"]), , float(row["1B"])]))


    batting_output = sorted(batting_players, key=lambda x: x[1], reverse=True)
   

    for x in batting_output:
        print x
        team_text.write("{} {} {} {} {} {} {}\n".format(x[0],x[1],x[2],x[3],x[4],x[5],x[6])) 
    team_text.close
	

def printPitching(team):
    with open('FanGraphs/FanGraphsPitching/2014_pitching_master_withoutPercentage.csv', 'rU') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if (row["Team"] == team):
                # print(row["Name"], row["H"], row["IPR"])
                pitching_players.append((row["Name"], float(row["G"]), (float(row["FB%"])), (float(row["FBv"])), (float(row["SL%"])), (float(row["SLv"])), (float(row["CT%"])), (float(row["CTv"])), (float(row["CB%"])), (float(row["CBv"])), (float(row["CH%"])), (float(row["CHv"])), (float(row["SF%"])), (float(row["SFv"])), (float(row["KN%"])), (float(row["KNv"])), (float(row["XX%"]))))

    pitching_output = sorted(pitching_players, key=lambda x: x[1], reverse=True)

    for x in pitching_output:
        print x

printBatting("Mets")


printPitching("Yankees")
