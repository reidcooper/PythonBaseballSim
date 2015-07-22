
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
                    <td width='50px'><center><b>R</b></center></td>
                    <td width='50px'><center><b>H</b></center></td>
                  </tr>
                  <tr class="info">
                    <td width='50px'>{{away_team}}</td>
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
                    <td width='50px' id = "b"></td>
                    <td width='50px' id = "s"></td>
                    <td width='50px' id = "o"></td>
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

                  var i = -1;
                  var k = 0;

                  var home = [0,0,0,0,0,0,0,0,0];
                  var away = [0,0,0,0,0,0,0,0,0];

                  var awayRuns = 0;
                  document.getElementById("ar").innerHTML = "<center>"+awayRuns+"</center>";
                  var homeRuns = 0;
                  document.getElementById("hr").innerHTML = "<center>"+homeRuns+"</center>";
                  var awayHits = 0;
                  document.getElementById("ah").innerHTML = "<center>"+awayHits+"</center>";
                  var homeHits = 0;
                  document.getElementById("hh").innerHTML = "<center>"+homeHits+"</center>";


                  var balls = 0;
                  document.getElementById("b").innerHTML = "<center>"+balls+"</center>";
                  var strikes = 0;
                  document.getElementById("s").innerHTML = "<center>"+strikes+"</center>";
                  var outs = 0;
                  document.getElementById("o").innerHTML = "<center>"+outs+"</center>";
    /*var away="";
    var home="";*/
    setInterval(function(){ eventFunction()}, 100);

    function scoreFunction() {
      if(i%2 === 0){
        away[Math.floor(i/2 + 1)-1]++;
        document.getElementById("a"+ Math.floor(i/2 + 1)).innerHTML = "<center>"+away[Math.floor(i/2 + 1)-1]+"</center>";
        awayRuns++;
        document.getElementById("ar").innerHTML = "<center>"+awayRuns+"</center>";
      } else {
        home[Math.floor(i/2 + 1)-1]++;
        document.getElementById("h"+ Math.floor(i/2 + 1)).innerHTML = "<center>"+home[Math.floor(i/2 + 1)-1]+"</center>";
        homeRuns++;
        document.getElementById("hr").innerHTML = "<center>"+homeRuns+"</center>";
      }
    }

    function hitFunction() {
      if(i%2 === 0){
        awayHits++;
        document.getElementById("ah").innerHTML = "<center>"+awayHits+"</center>";
      } else {
        homeHits++;
        document.getElementById("hh").innerHTML = "<center>"+homeHits+"</center>";
      }
    }

    function eventFunction() {

      switch(data[k].code){
        case "START-HALF-INNING":
        output="<center>" + data[k].description + "</center>";
        outs = 0;
        document.getElementById("o").innerHTML = "<center>"+outs+"</center>";
        i++;
        if(i%2 === 0){
          document.getElementById("a"+ Math.floor(i/2 + 1)).innerHTML = "<center>"+away[Math.floor(i/2 + 1)-1]+"</center>";
        } else {
          document.getElementById("h"+ Math.floor(i/2 + 1)).innerHTML = "<center>"+home[Math.floor(i/2 + 1)-1]+"</center>";
        }
        break;
        case "NEW-BATTER":
        output="<center>" + data[k].description + "</center>";
        balls = 0;
        document.getElementById("b").innerHTML = "<center>"+balls+"</center>";
        strikes = 0;
        document.getElementById("s").innerHTML = "<center>"+strikes+"</center>";
        break;
        case "NEW-PITCHER":
        output="<center>" + data[k].description + "</center>";
        break;
        case "BALL":
        output="<center>" + data[k].description + "</center>";
        balls++;
        document.getElementById("b").innerHTML = "<center>"+balls+"</center>";
        break;
        case "STRIKE":
        output="<center>" + data[k].description + "</center>";
        strikes++;
        document.getElementById("s").innerHTML = "<center>"+strikes+"</center>";
        break;
        case "FOUL-STRIKE":
        output="<center>" + data[k].description + "</center>";
        strikes++;
        document.getElementById("s").innerHTML = "<center>"+strikes+"</center>";
        break;
        case "FOUL":
        output="<center>" + data[k].description + "</center>";
        break;
        case "BB":
        output="<center>" + data[k].description + "</center>";
        break;
        case "KO":
        output="<center>" + data[k].description + "</center>";
        outs++;
        document.getElementById("o").innerHTML = "<center>"+outs+"</center>";
        break;
        case "1B":
        output="<center>" + data[k].description + "</center>";
        if(data[k+1].code !== "OUT-BH" && data[k+1].code !== "OUT-1BH" && data[k+1].code !== "OUT-2BH" && data[k+1].code !== "OUT-3BH" && data[k+1].code !== "OUT-4BH"){
          hitFunction();
        }
        break;
        case "2B":
        output="<center>" + data[k].description + "</center>";
        break;
        case "3B":
        output="<center>" + data[k].description + "</center>";
        break;
        case "HR":
        output="<center>" + data[k].description + "</center>";
        break;
        case "RUN-SCORES":
        output="<center>" + data[k].description + "</center>";
        scoreFunction();
        break;
        case "OUT-BH":
        output="<center>" + data[k].description + "</center>";
        outs++;
        document.getElementById("o").innerHTML = "<center>"+outs+"</center>";
        break;
        case "OUT-1BH":
        output="<center>" + data[k].description + "</center>";
        outs++;
        document.getElementById("o").innerHTML = "<center>"+outs+"</center>";
        break;
        case "OUT-2BH":
        output="<center>" + data[k].description + "</center>";
        outs++;
        document.getElementById("o").innerHTML = "<center>"+outs+"</center>";
        break;
        case "OUT-3BH":
        output="<center>" + data[k].description + "</center>";
        outs++;
        document.getElementById("o").innerHTML = "<center>"+outs+"</center>";
        break;
              /*case "OUT-4BH":
        output="<center>" + data[k].description + "</center>";
        outs++;
        document.getElementById("o").innerHTML = "<center>"+outs+"</center>";
        break;*/
        case "OUT-1B":
        output="<center>" + data[k].description + "</center>";
        outs++;
        document.getElementById("o").innerHTML = "<center>"+outs+"</center>";
        break;
        case "OUT-2B":
        output="<center>" + data[k].description + "</center>";
        outs++;
        document.getElementById("o").innerHTML = "<center>"+outs+"</center>";
        break;
        case "OUT-3B":
        output="<center>" + data[k].description + "</center>";
        outs++;
        document.getElementById("o").innerHTML = "<center>"+outs+"</center>";
        break;
        case "OUT-HP":
        output="<center>" + data[k].description + "</center>";
        outs++;
        document.getElementById("o").innerHTML = "<center>"+outs+"</center>";
        break;
        case "DIAMOND":
        break;
        default:
        output="<center>------------------------------default-----------------------------</center>";
      }
      document.getElementById("game1-row1-json").innerHTML = output;
      k++;


      /*if (events[k].code=="OUT-1BH" || events[k].code=="OUT-3B") {
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
      }*/
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
