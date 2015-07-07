#!/usr/bin/python

from bottle import *
import teamtxt
import json

@route('/')
@route('/index')
def homepage():
    return template('index')

@route('/about')
def about():
    return template('about')

# Works in Progress ==========================================
@route('/historicGame')
def historicGame():
    return template('historicGame')

@route('/submitHistoricGame', method='POST')
def submitHistoricGame():

    json_game = request.forms.get('selectGame')

    print "Game Selected: " + json_game

    return template('displayGame', json_game=json_game)
# Works in Progress ==========================================

# Submit Teams to Form
@route('/submitTeams', method='POST')
def submitTeams():
    # For using JSON and Javascript
    # home_team = request.json['myDict']['selectHomeTeam']
    # away_team = request.json['myDict']['selectAwayTeam']

    home_team = request.forms.get('selectHomeTeam')
    away_team = request.forms.get('selectAwayTeam')

    # Example Python Method Call with Team Names
    # if home_team and away_team:
    #     teamtxt.produceTeamFiles(home_team)
    #     teamtxt.produceTeamFiles(away_team)

    print "Home Team: " + str(home_team) + " Away Team: " + str(away_team)

    return template('displayGame', home_team=home_team, away_team=away_team)

# Return any static file <> are wildcards
@route('/static/<directory>/<filename>')
def static(filename, directory):
    return static_file(filename, root='static/'+directory+'/')

# ====== File Tree =======
@route('/static/js/dist/<filename>')
def static(filename):
    json_files = obtainDirectoryListing()
    print json_files
    return static_file(filename, root='static/js/dist/')

@route('/static/js/dist/themes/default/style.min.css')
def static():
    return static_file('style.min.css', root='static/js/dist/themes/default/')

@route('/static/js/dist/themes/default/<filename>')
def static(filename):
    return static_file(filename, root='static/js/dist/themes/default/')
# ====== File Tree =======

# 404 returns index page
@error(404)
def error404(error):
    return template('index')

# 405 returns index page
@error(405)
def error405(error):
    return template('index')

def obtainDirectoryListing():
    import os
    import sys
    var = os.path.abspath(os.path.dirname(__file__))
    var = var+"/static/teams/"
    files = os.listdir(var)
    # print var # Print Directory Path
    # print files # Print Directory Files

    files_dict = {}
    record_array = []
    count = 0

    for file in files:
        # Regex to detect .dotFiles, we do not want them
        if not re.match('\.\w*', file):
            record = {'id': str(file), 'parent' : '#', 'text': str(file)}
            record_array.append(record)
    files_dict['data'] = record_array

    json_data = json.dumps(files_dict)

    # print json_data
    return json_data

# Set debug to false for production
if __name__ == '__main__':

    # Change for production to false
    debug = True
    port = 8888

    port = int(os.environ.get('PORT', port))
    run(host='0.0.0.0', port=port, debug=debug)