import csv

players = []
new_players = []

def printTeam(team):
    with open('FanGraphs/FanGraphsBatting/2014_batting_master.csv', 'rU') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if (row["Team"] == team):
                # print(row["Name"], row["H"], row["IPR"])
                players.append((row["Name"], row["H"], row["IPR"]))

    def getKey(item):
        return item[1]
    new_players = sorted(players, key=getKey)

    for x in new_players:
        print x

printTeam("Mets")