<!DOCTYPE html>
<html lang="en">

<head>
    <title>B.A.S.E.S.</title>
    <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">

    <link href="http://getbootstrap.com/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">

    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>

    <script type="text/javascript" src="/static/js/submit_teams.js" charset="utf-8"></script>

    <link rel="stylesheet" href="/static/css/custom.css">

    <link href="//cdnjs.cloudflare.com/ajax/libs/select2/4.0.0/css/select2.min.css" rel="stylesheet" />
    <script src="//cdnjs.cloudflare.com/ajax/libs/select2/4.0.0/js/select2.min.js"></script>

</head>

<body>

    <div class="col-md-12">
        <div class="header">
            <nav>
                <ul class="nav nav-pills pull-right">
                    <li role="presentation" class="active"><a href="#">Home</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">B.A.S.E.S.</h3>
        </div>

        <div class="jumbotron">
            <h2>Baseball's Accurate Statistical Engine Simulator</h2>
            <p class="lead"></p>
            <p><center><a class="btn btn-success" href="/simulation" role="button">View CSV</center></a>
            </p>
        </div>

        <div class="row marketing">
            <div class="col-md-12">
                <h4>Python's Baseball Simulator</h4>
                <p>This website will help us develop our Python Baseball Simulator!</p>
            </div>

            <div id= "select-team">
                <form class="select-team-form" id="select-team-form" action="/submitTeams" method="post" role="form">
                    <div id="homeTeam" class="col-md-6">
                        <script type="text/javascript">
                            $(document).ready(function() {
                              $(".js-example-basic-single").select2();
                          });
                        </script>
                        <p><h4>Home Team:</h4></p>
                        <select class="js-example-basic-single" id="selectHomeTeam">
                            <option value="Diamondbacks">Arizona Diamondbacks</option>
                            <option value="Braves">Atlanta Braves</option>
                            <option value="Orioles">Baltimore Orioles</option>
                            <option value="Red Sox">Boston Red Sox</option>
                            <option value="White Sox">Chicago White Sox</option>
                            <option value="Cubs">Chicago Cubs</option>
                            <option value="Reds">Cincinnati Reds</option>
                            <option value="Indians">Cleveland Indians</option>
                            <option value="Rockies">Colorado Rockies</option>
                            <option value="Tigers">Detroit Tigers</option>
                            <option value="Marlins">Florida Marlins</option>
                            <option value="Astros">Houston Astros</option>
                            <option value="Royals">Kansas City Royals</option>
                            <option value="Angels">Los Angeles Angels</option>
                            <option value="Dodgers">Los Angeles Dodgers</option>
                            <option value="Brewers">Milwaukee Brewers</option>
                            <option value="Twins">Minnesota Twins</option>
                            <option value="Mets">New York Mets</option>
                            <option value="Yankees">New York Yankees</option>
                            <option value="Athletics">Oakland Athletics</option>
                            <option value="Phillies">Philadelphia Phillies</option>
                            <option value="Pirates">Pittsburgh Pirates</option>
                            <option value="Padres">San Diego Padres</option>
                            <option value="Giants">San Francisco Giants</option>
                            <option value="Mariners">Seattle Mariners</option>
                            <option value="Cardinals">St. Louis Cardinals</option>
                            <option value="Rays">Tampa Bay Rays</option>
                            <option value="Rangers">Texas Rangers</option>
                            <option value="Blue Jays">Toronto Blue Jays</option>
                            <option value="Nationals">Washington Nationals</option>
                        </select>
                    </div>

                    <div id="awayTeam" class="col-md-6">
                        <p><h4>Away Team:</h4></p>
                        <select class="js-example-basic-single" id="selectAwayTeam">
                            <option value="Diamondbacks">Arizona Diamondbacks</option>
                            <option value="Braves">Atlanta Braves</option>
                            <option value="Orioles">Baltimore Orioles</option>
                            <option value="Red Sox">Boston Red Sox</option>
                            <option value="White Sox">Chicago White Sox</option>
                            <option value="Cubs">Chicago Cubs</option>
                            <option value="Reds">Cincinnati Reds</option>
                            <option value="Indians">Cleveland Indians</option>
                            <option value="Rockies">Colorado Rockies</option>
                            <option value="Tigers">Detroit Tigers</option>
                            <option value="Marlins">Florida Marlins</option>
                            <option value="Astros">Houston Astros</option>
                            <option value="Royals">Kansas City Royals</option>
                            <option value="Angels">Los Angeles Angels</option>
                            <option value="Dodgers">Los Angeles Dodgers</option>
                            <option value="Brewers">Milwaukee Brewers</option>
                            <option value="Twins">Minnesota Twins</option>
                            <option value="Mets">New York Mets</option>
                            <option value="Yankees">New York Yankees</option>
                            <option value="Athletics">Oakland Athletics</option>
                            <option value="Phillies">Philadelphia Phillies</option>
                            <option value="Pirates">Pittsburgh Pirates</option>
                            <option value="Padres">San Diego Padres</option>
                            <option value="Giants">San Francisco Giants</option>
                            <option value="Mariners">Seattle Mariners</option>
                            <option value="Cardinals">St. Louis Cardinals</option>
                            <option value="Rays">Tampa Bay Rays</option>
                            <option value="Rangers">Texas Rangers</option>
                            <option value="Blue Jays">Toronto Blue Jays</option>
                            <option value="Nationals">Washington Nationals</option>
                        </select>
                    </div>
                    <div id="createTeams" class="createTeams">
                        <center><a class="btn btn-success" id="btnCreateTeams" type="button">Create Teams</center></a>
                    </div>
                </form>
            </div>
        </div>

        <footer class="footer">
            <p>&copy; Monmouth University
                <script type="text/javascript">
                  document.write(new Date().getFullYear());
              </script>
          </p>
      </footer>

  </div>
</body>

</html>