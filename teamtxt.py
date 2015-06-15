import csv

def printTeam(team):
    with open('FanGraphs/FanGraphsPitching/2014_pitching_master.csv', 'rU') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if (row["Team"] == team):
                print(row["Team"], row["Name"], row["HR"])

printTeam("Mets")
printTeam("Giants")
printTeam("Red Sox")