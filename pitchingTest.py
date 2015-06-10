import csv

players = []
new_players = []

def printTeam(team):
    with open('FanGraphs/FanGraphsBatting/2014_batting_master.csv', 'rU') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if (row["Team"] == team):
                # print(row["Name"], row["H"], row["IPR"])
                players.append((row["Name"], int(row["H"]), float(row["IPR"])))


    new_players = sorted(players, key=lambda x: x[1], reverse=True)

    for x in new_players:
        print x

printTeam("Mets")