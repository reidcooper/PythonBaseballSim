from bottle import *
# from PythonBaseballSim import teamtxt

@route('/')
@route('/index')
def homepage():
    return template('index')

@route('/about')
def homepage():
    return template('about')

@route('/simulation')
def simulation():
    return template('displayCSV')

# Submit Teams to Form
@route('/submitTeams', method='POST')
def submit_teams():
    home_team = request.json['myDict']['selectHomeTeam']
    away_team = request.json['myDict']['selectAwayTeam']

    print "Home Team: " + str(home_team) + " Away Team: " + str(away_team)

# Return any static file <> are wildcards
@route('/static/<directory>/<filename>')
def static(filename, directory):
    return static_file(filename, root='static/'+directory+'/')

# Set debug to false for production
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    run(host='0.0.0.0', port=port, debug=True)