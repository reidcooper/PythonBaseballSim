import csv

def printTeam(team):
    with open('Batting_Standard_2014_AllLeagues.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if (row['Team'] == team):
                print(row['Team'], row['IBB'], row['1B'])

printTeam('Royals')
printTeam('Phillies')