import csv

batting_players = []
batting_output = []
batting_text = []

pitching_players = []
pitching_output = []


def printBatting(team):
    with open('FanGraphs/FanGraphsBatting/2014_batting_master_withoutPercentage.csv', 'rU') as csvfile:
        reader = csv.DictReader(csvfile)

        # team_text = open(team + "_team.txt", "w")
        team_text = open("team.txt", "w")

        for row in reader:
            if (row["Team"] == team):
                # print(row["Name"], row["H"], row["IPR"])
                batting_players.append(([row["Name"].replace(" ", ""), row["Position"], row["H"], float(row["IPR"]), float(row["O-Swing%"]), float(row["Z-Swing%"]), float(row["O-Contact%"]), float(row["Z-Contact%"]), float(row["1B%"]), float(row["2B%"]), float(row["3B%"]), float(row["HR%"]), float(row["FP"])]))


    batting_output = sorted(batting_players, key=lambda x: x[2], reverse=True)


    for x in batting_output:
        print x
        team_text.write("{} {} {} {} {} {} {} {} {} {} {} {} {}\n".format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12]))
    team_text.close


def printPitching(team):
    with open('FanGraphs/FanGraphsPitching/2014_pitching_master_withoutPercentage.csv', 'rU') as csvfile:
        reader = csv.DictReader(csvfile)

        # pitcher_text = open(team + "_pitchers.txt", "w")
        pitcher_text = open("pitchers.txt", "w")

        for row in reader:
            if (row["Team"] == team):
                # print(row["Name"], row["H"], row["IPR"])
                pitching_players.append((row["Name"].replace(" ", ""), row["G"], "P", (float(row["Zone%"])), (float(row["FB%"])), (float(row["FBv"])), (float(row["SL%"])), (float(row["SLv"])), (float(row["CT%"])), (float(row["CTv"])), (float(row["CB%"])), (float(row["CBv"])), (float(row["CH%"])), (float(row["CHv"])), (float(row["SF%"])), (float(row["SFv"])), (float(row["KN%"])), (float(row["KNv"]))))

    pitching_output = sorted(pitching_players, key=lambda x: x[1], reverse=True)

    for x in pitching_output:
        print x
        pitcher_text.write("{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}\n".format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],x[14],x[15],x[16],x[17]))

    pitcher_text.close

printBatting("Mets")
printPitching("Mets")