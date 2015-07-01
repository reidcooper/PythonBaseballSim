
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
  <meta name="B.A.S.E.S." content="">
  <meta name="Reid Cooper, Philip DiMarco, Mary Menges, and Nicholas-Jason Roache" content="">
  <link rel="icon" href="/static/icons/favicon.ico">

  <title>B.A.S.E.S.</title>

  <!-- Bootstrap core CSS -->
  <link href="static/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="static/css/jumbotron-narrow.css" rel="stylesheet">

  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>

  <script type="text/javascript" src="/static/js/submit_teams.js" charset="utf-8"></script>

  <link rel="stylesheet" href="/static/css/custom.css">

  <link href="//cdnjs.cloudflare.com/ajax/libs/select2/4.0.0/css/select2.min.css" rel="stylesheet" />
  <script src="//cdnjs.cloudflare.com/ajax/libs/select2/4.0.0/js/select2.min.js"></script>
</head>

<body>

  <div class="container">
    <div class="header clearfix">
      <nav>
        <ul class="nav nav-pills pull-right">
          <li role="presentation" class="active"><a href="/">Home</a></li>
          <li role="presentation"><a href="/about">About</a></li>
        </ul>
      </nav>
      <h3 class="text-muted main-title">B.A.S.E.S.</h3>
    </div>

    <div class="jumbotron">
      <h1>Baseball's Accurate Statistical Engine Simulator</h1>
      <p class="lead">Just provide two selected teams below and simulate a real life baseball game!</p>
    </div>

    <div class="row marketing center-content">
      <div class="col-md-6">
        <h4>Python's Baseball Simulator</h4>
        <p>Pick Two Teams!</p>

        <div id= "select-team">
          <form class="select-team-form" id="select-team-form" action="/submitTeams" method="post" role="form">
            <div id="homeTeam">
              <script type="text/javascript">
                $(document).ready(function() {
                  $(".js-example-basic-single").select2();
                });
              </script>
              <h4>Home Team:</h4>
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

            <div id="awayTeam">
              <h4>Away Team:</h4>
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
              <a class="btn btn-success" id="btnCreateTeams" type="button">Create Teams</a>
            </div>
          </form>
        </div>
      </div>
      <div class="col-md-6">
        <img class="baseball" src="https://upload.wikimedia.org/wikipedia/en/1/1e/Baseball_(crop).jpg" alt="baseball" style="width:250px;height:250px;">
      </div>
    </div>

    <footer class="footer">
      <center>
        <p>Created By Reid Cooper, Philip DiMarco, Mary Menges, and Nicholas-Jason Roache, and Professor Gil Eckert</p>
        <p>&copy; Monmouth University
        2015<script>new Date().getFullYear()>2015&&document.write("-"+new Date().getFullYear());</script>
        </p>
      </center>
    </footer>

  </div> <!-- /container -->
</body>
</html>
