
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
          <li role="presentation"><a href="/historicGame">Historic Game</a></li>
          <li role="presentation"><a href="/about">About</a></li>
        </ul>
      </nav>
      <h3 class="text-muted main-title">B.A.S.E.S.</h3>
    </div>

    <div class="row marketing">

      <div class="gameOutput" id="game1">

        <div id="game1-row1">
          <center><h3>Game 1</h3></center>

          <div class="col-md-6" id="scoreboard">
            <div id="scoreboard-content">
              <h4>Scoreboard</h4>
              <div class="scoreboard-bgd">
                <table class="table table-condensed table-bordered">
                  <tr class="warning">
                    <td><b>Team</b></td>
                    <td><b>-</b></td>
                    <td><b>1</b></td>
                    <td><b>2</b></td>
                    <td><b>3</b></td>
                    <td><b>4</b></td>
                    <td><b>5</b></td>
                    <td><b>6</b></td>
                    <td><b>7</b></td>
                    <td><b>8</b></td>
                    <td><b>9</b></td>
                    <td><b>-</b></td>
                    <td><b>R</b></td>
                    <td><b>H</b></td>
                    <td><b>E</b></td>
                  </tr>
                  <tr class="success">
                    <td>Home Team</td>
                    <td>-</td>
                    <td>1</td>
                    <td>2</td>
                    <td>3</td>
                    <td>4</td>
                    <td>5</td>
                    <td>6</td>
                    <td>7</td>
                    <td>8</td>
                    <td>9</td>
                    <td>-</td>
                    <td>00</td>
                    <td>00</td>
                    <td>00</td>
                  </tr>
                  <tr class="info">
                    <td>Away Team</td>
                    <td>-</td>
                    <td>1</td>
                    <td>2</td>
                    <td>3</td>
                    <td>4</td>
                    <td>5</td>
                    <td>6</td>
                    <td>7</td>
                    <td>8</td>
                    <td>9</td>
                    <td>-</td>
                    <td>00</td>
                    <td>00</td>
                    <td>00</td>
                  </tr>
                </table>
              </div>
            </div>
          </div>

          <div class="col-md-6" id="gameEvents">
            <center>
              <h4>Game Events</h4>
            </center>
            <div class="scroll-box gameEvents-json" id="game1-row1-json">
              <script>
                $.getJSON('/static/simulations/butt.json', function(data) {
                            //now json variable contains data in json format
                            //let's display a few items
                            var output="<ul>";
                            for(var i in data.sample){
                              output += '<li>Index: ' + data.sample[i].index + '<br />About: ' + data.sample[i].about+"</li>";
                            }
                            output += "</ul>";
                            $('#game1-row1-json').html(output);
                          });
              </script>
            </div>
          </div>
        </div> <!-- End Game1 Row1 -->
      </div> <!-- End GameOutput -->

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
