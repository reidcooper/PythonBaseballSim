
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

          <div class="col-md-6" id="scoreboard">
            <div id="scoreboard-content">
              <h4>Scoreboard</h4>
              <div class="scoreboard-bgd">
                <table style="float: left">
                  <tr><td><b>Team</b></td></tr>
                  <tr><td>Home Team</td></tr>
                  <tr><td>Away Team</td></tr>
                </table>
                <table class="table table-condensed table-bordered">
                  <tr class="warning">
                    <td width='50px'><center><b>1</b></center></td>
                    <td width='50px'><center><b>2</b></center></td>
                    <td width='50px'><center><b>3</b></center></td>
                    <td width='50px'><center><b>4</b></center></td>
                    <td width='50px'><center><b>5</b></center></td>
                    <td width='50px'><center><b>6</b></center></td>
                    <td width='50px'><center><b>7</b></center></td>
                    <td width='50px'><center><b>8</b></center></td>
                    <td width='50px'><center><b>9</b></center></td>
                    <td width='50px'><center><b>R</b></center></td>
                    <td width='50px'><center><b>H</b></center></td>
                    <td width='50px'><center><b>E</b></center></td>
                  </tr>
                  <tr class="success" id="home">
                  </tr>
                  <tr class="info" id="away">
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
                file_location = '/static/simulations/{{ game_file }}'

                $.getJSON(file_location, function(data) {
                  var output="<ul>";

                  i=1;
                  var away=" ";
                  var home="";
                  var j=0, k=0;
                  var speedInterval = 200; // Change this to varry speed of simulation

                  setInterval(function(){ eventFunction(data.half_innings)}, speedInterval);

                  function scoreFunction() {
                    home+="<td width='50px'><center>"+data.half_innings[i].home_score+"</td></center>";
                    away+="<td width='50px'><center>"+data.half_innings[i].away_score+"</td></center>";
                    i+=2;
                    document.getElementById("away").innerHTML=away;
                    document.getElementById("home").innerHTML=home;
                  }

                  function eventFunction(arr) {
                    output="<center>" + arr[k].events[j].description + "</center>";
                    document.getElementById("game1-row1-json").innerHTML = output;
                    if (arr[k].events[j].code=="OUT-1BH" || arr[k].events[j].code=="OUT-3B") {
                      j=-1;
                      k++;
                      if (k%2==0) {
                        scoreFunction();
                      }
                    }
                    j++;
                    if (k==18) {
                      output="<center>***** Final Score -- " + data.home_team + ": " + data.final_home_score + " -- " + data.away_team + ": " + data.final_away_score + " *****</center>";
                      document.getElementById("game1-row1-json").innerHTML = output;
                      home+="<td width='50px'><center>"+data.final_home_score+"</td></center>";
                      away+="<td width='50px'><center>"+data.final_away_score+"</td></center>";
                      document.getElementById("away").innerHTML=away;
                      document.getElementById("home").innerHTML=home;
                    }
                  }
                  output+="</ul>";
                });
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
