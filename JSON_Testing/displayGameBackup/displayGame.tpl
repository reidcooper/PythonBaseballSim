
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
                file_location = '/static/simulations/{{ game_file }}'
                $.getJSON(file_location, function(data) {
                  var output="<ul>";

                  var i = 0;
                  var k = 0;
                  var top = false;

                  var home = [0,0,0,0,0,0,0,0,0,0];
                  var away = [0,0,0,0,0,0,0,0,0,0];

                  var awayRuns = 0;
                  document.getElementById("ar").innerHTML = "<center>"+awayRuns+"</center>";
                  var homeRuns = 0;
                  document.getElementById("hr").innerHTML = "<center>"+homeRuns+"</center>";
                  var awayHits = 0;
                  document.getElementById("ah").innerHTML = "<center>"+awayHits+"</center>";
                  var homeHits = 0;
                  document.getElementById("hh").innerHTML = "<center>"+homeHits+"</center>";


                  var balls = 0;
                  document.getElementById("b").innerHTML = '<center><img id="ball1" src="/static/images/clear.png" alt="empty"> <img id="ball2" src="/static/images/clear.png" alt="empty"> <img id="ball3" src="/static/images/clear.png" alt="empty"> <img id="ball4" src="/static/images/clear.png" alt="empty"></center>';
                  var strikes = 0;
                  document.getElementById("s").innerHTML = '<center><img id="strike1" src="/static/images/clear.png" alt="empty"> <img id="strike2" src="/static/images/clear.png" alt="empty"> <img id="strike3" src="/static/images/clear.png" alt="empty"></center>';
                  var outs = 0;
                  document.getElementById("o").innerHTML = '<center><img id="out1" src="/static/images/clear.png" alt="empty"> <img id="out2" src="/static/images/clear.png" alt="empty"> <img id="out3" src="/static/images/clear.png" alt="empty"></center>';
    
    setInterval(function(){ eventFunction()}, 10);

    function scoreFunction() {
      if(top){
        away[i]++;
        document.getElementById("a"+ i).innerHTML = "<center>"+away[i]+"</center>";
        awayRuns++;
        document.getElementById("ar").innerHTML = "<center>"+awayRuns+"</center>";
      } else {
        home[i]++;
        document.getElementById("h"+ i).innerHTML = "<center>"+home[i]+"</center>";
        homeRuns++;
        document.getElementById("hr").innerHTML = "<center>"+homeRuns+"</center>";
      }
    }

    function hitFunction() {
      if(top){
        awayHits++;
        document.getElementById("ah").innerHTML = "<center>"+awayHits+"</center>";
      } else {
        homeHits++;
        document.getElementById("hh").innerHTML = "<center>"+homeHits+"</center>";
      }
    }

    function eventFunction() {

      switch(data[i][k].code){
        case "START-HALF-INNING":
        if(top){
        	top = false;
        } else {
        	top = true;
        }
        output="<center>" + data[i][k].description + "</center>";
        outs = 0;
		pictureCount("out", outs);        
		if(top){
        	document.getElementById("a" + i).innerHTML = "<center>"+away[i]+"</center>";
        } else {
        	document.getElementById("h"+ i).innerHTML = "<center>"+home[i]+"</center>";
        }
        break;
        case "NEW-BATTER":
        output="<center>" + data[i][k].description + "</center>";
        balls = 0;
		pictureCount("ball", balls);        
		strikes = 0;
        pictureCount("strike", strikes);
        break;
        case "NEW-PITCHER":
        output="<center>" + data[i][k].description + "</center>";
        break;
        case "BALL":
        output="<center>" + data[i][k].description + "</center>";
        balls++;
        pictureCount("ball", balls);
        break;
        case "STRIKE":
        output="<center>" + data[i][k].description + "</center>";
        strikes++;
        pictureCount("strike", strikes);
        break;
        case "FOUL-STRIKE":
        output="<center>" + data[i][k].description + "</center>";
        strikes++;
        pictureCount("strike", strikes);
        break;
        case "FOUL":
        output="<center>" + data[i][k].description + "</center>";
        break;
        case "BB":
        output="<center>" + data[i][k].description + "</center>";
        break;
        case "KO":
        output="<center>" + data[i][k].description + "</center>";
        outs++;
        pictureCount("out", outs);
        break;
        case "1B":
        output="<center>" + data[i][k].description + "</center>";
        if(data[i][k+1].code !== "OUT-BH" && data[i][k+1].code !== "OUT-1BH" && data[i][k+1].code !== "OUT-2BH" && data[i][k+1].code !== "OUT-3BH" && data[i][k+1].code !== "OUT-4BH"){
          hitFunction();
        }
        break;
        case "2B":
        output="<center>" + data[i][k].description + "</center>";
        if(data[i][k+1].code !== "OUT-BH" && data[i][k+1].code !== "OUT-1BH" && data[i][k+1].code !== "OUT-2BH" && data[i][k+1].code !== "OUT-3BH" && data[i][k+1].code !== "OUT-4BH"){
          hitFunction();
        }
        break;
        case "3B":
        output="<center>" + data[i][k].description + "</center>";
        if(data[i][k+1].code !== "OUT-BH" && data[i][k+1].code !== "OUT-1BH" && data[i][k+1].code !== "OUT-2BH" && data[i][k+1].code !== "OUT-3BH" && data[i][k+1].code !== "OUT-4BH"){
          hitFunction();
        }
        break;
        case "HR":
        output="<center>" + data[i][k].description + "</center>";
        if(data[i][k+1].code !== "OUT-BH" && data[i][k+1].code !== "OUT-1BH" && data[i][k+1].code !== "OUT-2BH" && data[i][k+1].code !== "OUT-3BH" && data[i][k+1].code !== "OUT-4BH"){
          hitFunction();
        }
        break;
        case "RUN-SCORES":
        output="<center>" + data[i][k].description + "</center>";
        scoreFunction();
        break;
        case "OUT-BH":
        output="<center>" + data[i][k].description + "</center>";
        outs++;
        pictureCount("out", outs);
        break;
        case "OUT-1BH":
        output="<center>" + data[i][k].description + "</center>";
        outs++;
        pictureCount("out", outs);
        break;
        case "OUT-2BH":
        output="<center>" + data[i][k].description + "</center>";
        outs++;
        pictureCount("out", outs);
        break;
        case "OUT-3BH":
        output="<center>" + data[i][k].description + "</center>";
        outs++;
        pictureCount("out", outs);
        break;
        /*case "OUT-4BH":
        output="<center>" + data[i][k].description + "</center>";
        outs++;
        pictureCount("out", outs);
        break;*/
        case "OUT-1B":
        output="<center>" + data[i][k].description + "</center>";
        outs++;
        pictureCount("out", outs);
        break;
        case "OUT-2B":
        output="<center>" + data[i][k].description + "</center>";
        outs++;
        pictureCount("out", outs);
        break;
        case "OUT-3B":
        output="<center>" + data[i][k].description + "</center>";
        outs++;
        pictureCount("out", outs);
        break;
        case "OUT-HP":
        output="<center>" + data[i][k].description + "</center>";
        outs++;
        pictureCount("out", outs);
        break;
        case "DIAMOND":
        break;
        case "END-INNING-SCORE":
        output="<center>" + data[i][k].description + "</center>";   
        	k = -1;
        	i++;
		break;
        default:
        output="<center>------------------------------default-----------------------------</center>";
      }
      document.getElementById("game1-row1-json").innerHTML = output;
      k++;

    }
    function pictureCount(type, count){
      ballCountPics = "";
      switch(type) {
        case "ball":
        switch(count){
          case 0:
          ballCountPics = '<center><img id="ball1" src="/static/images/clear.png" alt="empty"> <img id="ball2" src="/static/images/clear.png" alt="empty"> <img id="ball3" src="/static/images/clear.png" alt="empty"> <img id="ball4" src="/static/images/clear.png" alt="empty"></center>';
          break;
          case 1:
          ballCountPics = '<center><img id="ball1" src="/static/images/ball.png" alt="ball"> <img id="ball2" src="/static/images/clear.png" alt="empty"> <img id="ball3" src="/static/images/clear.png" alt="empty"> <img id="ball4" src="/static/images/clear.png" alt="empty"></center>';
          break;
          case 2:
          ballCountPics = '<center><img id="ball1" src="/static/images/ball.png" alt="ball"> <img id="ball2" src="/static/images/ball.png" alt="ball"> <img id="ball3" src="/static/images/clear.png" alt="empty"> <img id="ball4" src="/static/images/clear.png" alt="empty"></center>';
          break;
          case 3:
          ballCountPics = '<center><img id="ball1" src="/static/images/ball.png" alt="ball"> <img id="ball2" src="/static/images/ball.png" alt="ball"> <img id="ball3" src="/static/images/ball.png" alt="ball"> <img id="ball4" src="/static/images/clear.png" alt="empty"></center>';
          break;
          case 4:
          ballCountPics = '<center><img id="ball1" src="/static/images/ball.png" alt="ball"> <img id="ball2" src="/static/images/ball.png" alt="ball"> <img id="ball3" src="/static/images/ball.png" alt="ball"> <img id="ball4" src="/static/images/ball.png" alt="ball"></center>';
          break;
          default:
        }
        document.getElementById("b").innerHTML = ballCountPics;
        break;
        case "strike":
        ballCountPics = "";
        switch(count){
          case 0:
          ballCountPics = '<center><img id="strike1" src="/static/images/clear.png" alt="empty"> <img id="strike2" src="/static/images/clear.png" alt="empty"> <img id="strike3" src="/static/images/clear.png" alt="empty"></center>';
          break;
          case 1:
          ballCountPics = '<center><img id="strike1" src="/static/images/foul.png" alt="strike"> <img id="strike2" src="/static/images/clear.png" alt="empty"> <img id="strike3" src="/static/images/clear.png" alt="empty"></center>';
          break;
          case 2:
          ballCountPics = '<center><img id="strike1" src="/static/images/foul.png" alt="strike"> <img id="strike2" src="/static/images/foul.png" alt="strike"> <img id="strike3" src="/static/images/clear.png" alt="empty"></center>';
          break;
          case 3:
          ballCountPics = '<center><img id="strike1" src="/static/images/foul.png" alt="strike"> <img id="strike2" src="/static/images/foul.png" alt="strike"> <img id="strike3" src="/static/images/foul.png" alt="strike"></center>';
          break;
          default:
        }
        document.getElementById("s").innerHTML = ballCountPics;
        break;
        case "out":
        ballCountPics = "";
        switch(count){
          case 0:
          ballCountPics = '<center><img id="out1" src="/static/images/clear.png" alt="empty"> <img id="out2" src="/static/images/clear.png" alt="empty"> <img id="out3" src="/static/images/clear.png" alt="empty"></center>';
          break;
          case 1:
          ballCountPics = '<center><img id="out1" src="/static/images/out.png" alt="out"> <img id="out2" src="/static/images/clear.png" alt="empty"> <img id="out3" src="/static/images/clear.png" alt="empty"></center>';
          break;
          case 2:
          ballCountPics = '<center><img id="out1" src="/static/images/out.png" alt="out"> <img id="out2" src="/static/images/out.png" alt="out"> <img id="out3" src="/static/images/clear.png" alt="empty"></center>';
          break;
          case 3:
          ballCountPics = '<center><img id="out1" src="/static/images/out.png" alt="out"> <img id="out2" src="/static/images/out.png" alt="out"> <img id="out3" src="/static/images/out.png" alt="out"></center>';
          break;
          default:
        }
        document.getElementById("o").innerHTML = ballCountPics;
        break;
        default:
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
