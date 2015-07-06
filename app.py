#!/usr/bin/python

from bottle import *
import teamtxt

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