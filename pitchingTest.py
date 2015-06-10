import csv

batting_players = []
batting_output = []

pitching_players = []
pitching_output = []

def printBatting(team):
    with open('FanGraphs/FanGraphsBatting/2014_batting_master.csv', 'rU') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if (row["Team"] == team):
                # print(row["Name"], row["H"], row["IPR"])
                batting_players.append((row["Name"], int(row["H"]), float(row["IPR"])))


    batting_output = sorted(batting_players, key=lambda x: x[1], reverse=True)

    for x in batting_output:
        print x

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

print "\n"

printPitching("Yankees")