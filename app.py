#!/usr/bin/python

from bottle import *
import teamtxt
import json
from baseballGamePackage.Game import Game

@route('/')
@route('/index')
def homepage():
    return template('index')

@route('/about')
def about():
    return template('about')

@route('/historicGame')
def historicGame():
    return template('historicGame')

@route('/submitHistoricGame', method='POST')
def submitHistoricGame():

    json_game = request.forms.get('gameFile')
    print "Game Selected: " + json_game

    return template('displayGame')

# Submit Teams to Form
@route('/submitTeams', method='POST')
def submitTeams():
    # For using JSON and Javascript
    # home_team = request.json['myDict']['selectHomeTeam']
    # away_team = request.json['myDict']['selectAwayTeam']

    home_team = request.forms.get('selectHomeTeam')
    away_team = request.forms.get('selectAwayTeam')

    print "Home Team: " + str(home_team) + " Away Team: " + str(away_team)

    # Run Simulation ======
    g = Game(str(home_team), str(away_team))
    game = g.playGame()
    print game

    # For A Dynamic Page
    # <center><h3>Game 1: {{ home_team }} vs. {{away_team}}</h3></center>
    # return template('displayGame', home_team=home_team, away_team=away_team)
    return template('displayGame')

# Return any static file <> are wildcards
@route('/static/<directory>/<filename>')
def static(filename, directory):
    # Creates JSON file of all the historical games simulated
    obtainDirectoryListing()
    return static_file(filename, root='static/'+directory+'/')

# ====== File Tree =======
@route('/static/js/dist/<filename>')
def static(filename):
    return static_file(filename, root='static/js/dist/')

@route('/static/js/dist/themes/default/style.min.css')
def static():
    return static_file('style.min.css', root='static/js/dist/themes/default/')

@route('/static/js/dist/themes/default/<filename>')
def static(filename):
    return static_file(filename, root='static/js/dist/themes/default/')

# Creates JSON file of all the historical games simulated
def obtainDirectoryListing():
    import os
    import sys
    historical_games_location = "teams/"
    var = os.path.abspath(os.path.dirname(__file__))+"/static/"+historical_games_location
    files = os.listdir(var)

    record_array = []
    count = 0

    for file in files:
        # Regex to detect .dotFiles, we do not want them
        if (not re.match('\.\w*', file)) and (not re.match('file_tree.json', file)):
                record = {'id': str(file), 'parent' : '#', 'text': str(file), "icon":"glyphicon glyphicon-leaf"}
                record_array.append(record)

    with open(var+'file_tree.json', 'w') as outfile:
        json.dump(record_array, outfile)
# ====== File Tree =======

# 404 returns index page
@error(404)
def error404(error):
    return template('index')

# 405 returns index page
@error(405)
def error405(error):
    return template('index')

# Set debug to false for production
if __name__ == '__main__':

    # Change for production to false
    debug = True
    port = 8888

    port = int(os.environ.get('PORT', port))
    run(host='0.0.0.0', port=port, debug=debug)