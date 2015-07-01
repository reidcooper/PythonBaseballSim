from bottle import *
# from PythonBaseballSim import teamtxt

# @route('/')
# def homepage():
#     return static_file("index.html", root='static/')

# @post('/submitTeams', method='POST')
# def submitTeams():
#     home_team = request.form('inputHomeTeam')
#     away_team = request.form('inputAwayTeam')

#     if home_team and away_team:
#         json.dumps({'html':'<span>All fields good !!</span>'})

# @route('/<filename>')
# def server_static(filename):
#     if (filename == "displayCSV.html"):
#         # teamtxt.printBatting("Mets")
#         # teamtxt.printPitching("Mets")
#         print "hello"

#     return static_file(filename, root='static/')
@route('/')
@route('/index')
def homepage():
    return template('index')

@route('/simulation')
def simulation():
    return template('displayCSV')

# Submit Teams to Form
@route('/submitTeams', method='POST')
def submit_teams():
    home_team = request.json['myDict']['selectHomeTeam']
    away_team = request.json['myDict']['selectAwayTeam']

    print "Home Team: " + str(home_team) + " Away Team: " + str(away_team)

# Return any static file
@route('/static/<directory>/<filename>')
def static(filename, directory):
    return static_file(filename, root='static/'+directory+'/')

# Set debug to false for production
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    run(host='0.0.0.0', port=port, debug=True)