from bottle import *
import teamtxt

@route('/')
@route('/index')
def homepage():
    return template('index')

@route('/about')
def homepage():
    return template('about')

@route('/submitTeams')
def simulation():
    return template('displayCSV')

# Submit Teams to Form
@route('/submitTeams', method='POST')
def submit_teams():
    home_team = request.json['myDict']['selectHomeTeam']
    away_team = request.json['myDict']['selectAwayTeam']

    # Example Python Method Call with Team Names
    # if home_team and away_team:
    #     teamtxt.produceTeamFiles(home_team)
    #     teamtxt.produceTeamFiles(away_team)

    print "Home Team: " + str(home_team) + " Away Team: " + str(away_team)

# Return any static file <> are wildcards
@route('/static/<directory>/<filename>')
def static(filename, directory):
    return static_file(filename, root='static/'+directory+'/')

# 404 returns index page
@error(404)
def error404(error):
    return template('index')

# Set debug to false for production
if __name__ == '__main__':

    # Change for production to false
    debug = True

    port = int(os.environ.get('PORT', 5000))
    run(host='0.0.0.0', port=port, debug=debug)