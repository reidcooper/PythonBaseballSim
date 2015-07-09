#!/usr/bin/python

from bottle import *
import teamtxt
import json
import sys
import os
from baseballGamePackage.Game import Game

''' Global Settings '''
historical_games_location = "teams/"
debug = True # Change for production to false
port = 8888 # Typically 80 for websites

@route('/')
@route('/index.html')
def homepage():
    '''Routes for index page'''

    return template('index')

@route('/about')
def about():
    '''Routes for about page'''

    return template('about')

@route('/historicGame')
def historicGame():
    '''When the historical page loads, the method obtainDirectoryListing() is called to create a JSON file listing of all the files in the simulations directory'''

    obtainDirectoryListing()
    return template('historicGame')

@route('/submitHistoricGame', method='POST')
def submitHistoricGame():
    '''When user selects a previously simulated game and selects Play Ball! the webpage will call this route and then return the displayGame page'''

    # Play Ball with a selected JSON game file
    if request.forms.get('play_ball_btn'):
        json_game = request.forms.get('gameFile')
        print "Game Selected: " + json_game
        return template('displayGame')

    # If the User wants to upload a JSON game file
    elif request.forms.get('upload_btn'):
        if request.files.get('upload'):

            upload = request.files.get('upload')
            name, ext = os.path.splitext(upload.filename)

            if re.match('.json', ext):
                var = os.path.abspath(os.path.dirname(__file__))+"/static/"+historical_games_location

                file_path = "{path}/{file}".format(path=var, file=upload.filename)
                upload.save(file_path, overwrite=True)
                return template('displayGame')
            else:
                print "Error - Not a JSON file"
                return template('historicGame')
        else:
            print "Error - No file uploaded"
            return template('historicGame')
    else:
        print "Did not select Play Ball or Upload"
        return template('historicGame')

# Submit Teams to Form
@route('/submitTeams', method='POST')
def submitTeams():
    '''Submits the two baseball teams ready for simulation, obtains those two teams, and runs the Python Simulator'''
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

@route('/download/<filename>')
def static(filename):
    '''Download Simulation Files'''
    print "DOWNLOAD FROM "+historical_games_location
    return static_file(filename, root='static/teams/', download=filename)

@route('/static/<directory>/<filename>')
def static(filename, directory):
    '''Serve Directory Files from the Static Directory <> are wildcards'''
    print "SERVE STATIC DIRECTORY"
    return static_file(filename, root='static/'+directory+'/')

''' ====== FILE TREE ======= '''
''' These next four methods serve the purpose of creating the jQuery File Tree shown on the historical game page'''
@route('/static/js/dist/<filename>')
def static(filename):
    print "SERVE JQUERY JS DIRECTORY"
    return static_file(filename, root='static/js/dist/')

@route('/static/js/dist/themes/default/style.min.css')
def static():
    print "SERVE JQUERY CSS DIRECTORY"
    return static_file('style.min.css', root='static/js/dist/themes/default/')

@route('/static/js/dist/themes/default/<filename>')
def static(filename):
    print "SERVE JQUERY PICTURE/ICONS DIRECTORY"
    return static_file(filename, root='static/js/dist/themes/default/')

# Creates JSON file of all the historical games simulated
def obtainDirectoryListing():
    '''Creates a JSON file listing all files within the scanned directory. Typically it will be scanning the /simulations directory '''
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

    print "CREATED JSON DIRECTORY LISTING"
''' ====== FILE TREE ======= '''

''' 404 returns index page'''
@error(404)
def error404(error):
    print "404 Error"
    return template('index')

''' 405 returns index page'''
@error(405)
def error405(error):
    print "404 Error"
    return template('index')

# Set debug to false for production
if __name__ == '__main__':
    print "\nServinging Up PythonBaseballSimulator...\n"
    port = int(os.environ.get('PORT', port))
    run(host='0.0.0.0', port=port, debug=debug)