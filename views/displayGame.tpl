
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
  <meta name="B.A.S.E.S." content="">
  <meta name="author" content="Reid Cooper, Philip DiMarco, Mary Menges, and Nicholas-Jason Roache, Chenqi Zhu, Swethana Gopisetti, and Professor Gil Eckert">
  <link rel="icon" href="/static/icons/favicon.ico">

  <title>B.A.S.E.S.</title>

  <!-- Bootstrap core CSS -->
  <link href="static/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="static/css/jumbotron-narrow.css" rel="stylesheet">

  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
  <script type="text/javascript" src="/static/js/displayGame.js" charset="utf-8"></script>
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
          <center><h3>Game 1: {{ home_team }} vs. {{away_team}}</h3></center>

          <div class="col-md-12" id="scoreboard">
            <div id="scoreboard-content">
              <h4>Scoreboard</h4>
              <div class="scoreboard-bgd">
                <table style="float: left">
                </table>
                <table class="table table-condensed table-bordered">
                  <tr class="warning">
                    <td width='50px'><center><b>Teams</b></center></td>
                    <td width='50px'><center><b>1</b></center></td>
                    <td width='50px'><center><b>2</b></center></td>
                    <td width='50px'><center><b>3</b></center></td>
                    <td width='50px'><center><b>4</b></center></td>
                    <td width='50px'><center><b>5</b></center></td>
                    <td width='50px'><center><b>6</b></center></td>
                    <td width='50px'><center><b>7</b></center></td>
                    <td width='50px'><center><b>8</b></center></td>
                    <td width='50px'><center><b>9</b></center></td>
                    <td width='50px'><center><b>10</b></center></td>
                    <td width='50px'><center><b>R</b></center></td>
                    <td width='50px'><center><b>H</b></center></td>
                  </tr>
                  <tr class="info">
                    <td width='50px'>{{away_team}}</td>
                    <td width='50px' id = "a0"></td>
                    <td width='50px' id = "a1"></td>
                    <td width='50px' id = "a2"></td>
                    <td width='50px' id = "a3"></td>
                    <td width='50px' id = "a4"></td>
                    <td width='50px' id = "a5"></td>
                    <td width='50px' id = "a6"></td>
                    <td width='50px' id = "a7"></td>
                    <td width='50px' id = "a8"></td>
                    <td width='50px' id = "a9"></td>
                    <td width='50px' id = "ar"></td>
                    <td width='50px' id = "ah"></td>
                  </tr>
                  <tr class="success">
                    <td width='50px'>{{home_team}}</td>
                    <td width='50px' id = "h0"></td>
                    <td width='50px' id = "h1"></td>
                    <td width='50px' id = "h2"></td>
                    <td width='50px' id = "h3"></td>
                    <td width='50px' id = "h4"></td>
                    <td width='50px' id = "h5"></td>
                    <td width='50px' id = "h6"></td>
                    <td width='50px' id = "h7"></td>
                    <td width='50px' id = "h8"></td>
                    <td width='50px' id = "h9"></td>
                    <td width='50px' id = "hr"></td>
                    <td width='50px' id = "hh"></td>
                  </tr>
                </table>
                <table class="table table-condensed table-bordered">
                  <tr>
                    <td width='50px'><center><b>Balls</b></center></td>
                    <td width='50px'><center><b>Strikes</b></center></td>
                    <td width='50px'><center><b>Outs</b></center></td>
                  </tr>
                  <tr>
                    <td width='50px' id = "b"><center><img id="ball1" src="/static/images/clear.png" alt="empty"> <img id="ball2" src="/static/images/clear.png" alt="empty"> <img id="ball3" src="/static/images/clear.png" alt="empty"> <img id="ball4" src="/static/images/clear.png" alt="empty"></center></td>
                    <td width='50px' id = "s"><center><img id="strike1" src="/static/images/clear.png" alt="empty"> <img id="strike2" src="/static/images/clear.png" alt="empty"> <img id="strike3" src="/static/images/clear.png" alt="empty"></center></td>
                    <td width='50px' id = "o"><center><img id="out1" src="/static/images/clear.png" alt="empty"> <img id="out2" src="/static/images/clear.png" alt="empty"> <img id="out3" src="/static/images/clear.png" alt="empty"></center></td>
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
                // LOCATION OF FILE SHOULD BE LOCATED IN /static/simulations/
                // Script has been moved to /static/js/displayGame.js
                file_location = '/static/simulations/{{ game_file }}'
                displayGameWeb(file_location);
              </script>
            </div>
          </div>
          <div class="col-md-6" id="diamond-div">
            <div class="scroll-box diamond" id="diamond">
              <script>
              </script>
            </div>
          </div>
        </div> <!-- End Game1 Row1 -->
      </div> <!-- End GameOutput -->

      <footer class="footer">
        <center>
          <p>Created By Reid Cooper, Philip DiMarco, Mary Menges, and Nicholas-Jason Roache, Chenqi Zhu, Swethana Gopisetti, and Professor Gil Eckert</p>
          <p>&copy; Monmouth University
            2015<script>new Date().getFullYear()>2015&&document.write(" - "+new Date().getFullYear());</script>
          </p>
        </center>
      </footer>

    </div> <!-- /container -->
  </body>
  </html>
