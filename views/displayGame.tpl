
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
  <meta name="B.A.S.E.S." content="">
  <meta name="" content="">
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

  <div class="col-md-12">
    <div class="header clearfix">
      <nav>
        <ul class="nav nav-pills pull-right">
          <li role="presentation" class="active"><a href="/">Home</a></li>
          <li role="presentation"><a href="/about">About</a></li>
        </ul>
      </nav>
      <h3 class="text-muted main-title">B.A.S.E.S.</h3>
    </div>

    <div class="row marketing center-content">

      <div id="gameOutput" class="gameOutput">

        <div id="gameOutputRow1" class="gameOutputRow1">
          <center><h3>Game 1: {{ home_team }} vs. {{away_team}}</h3></center>

          <div class="col-md-6">
            <center>
              <h4>Scoreboard</h4>
              <img class="scoreboard img-rounded" src="/static/images/scoreboard.jpg" alt="scoreboard" style="">
            </center>
          </div>

          <div class="col-md-6">
            <center>
              <h4>Game Events</h4>
            </center>
            <div class="scroll-box" id="gameEvents">
              <script>
                $.getJSON('/static/simulations/sample.json', function(data) {
                            //now json variable contains data in json format
                            //let's display a few items
                            var output="<ul>";
                            for(var i in data.sample){
                              output += '<li>Name: ' + data.sample[i].name + '<br />About: ' + data.sample[i].about+"</li>";
                            }
                            output += "</ul>";
                            $('#gameEvents').html(output);
                          });
              </script>
            </div>
          </div>
        </div>

        <div id="gameOutputRow2" class="gameOutputRow2">
          <div class="col-md-6">
            <center>
              <h4>Scoreboard</h4>
              <img class="scoreboard  img-rounded" src="/static/images/scoreboard.jpg" alt="scoreboard" style="">
            </center>
          </div>

          <div class="col-md-6">
            <center>
              <h4>Game Events</h4>
            </center>
            <div class="scroll-box" id="gameEvents2">
              <script>
                $.getJSON('/static/simulations/sample.json', function(data) {
                            //now json variable contains data in json format
                            //let's display a few items
                            var output="<ul>";
                            for(var i in data.sample){
                              output += '<li>Name: ' + data.sample[i].name + '<br />About: ' + data.sample[i].about+"</li>";
                            }
                            output += "</ul>";
                            $('#gameEvents2').html(output);
                          });
              </script>
            </div>
          </div>
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
