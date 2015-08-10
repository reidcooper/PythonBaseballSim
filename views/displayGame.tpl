<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="BASES" content="">
    <meta name="author" content="Reid Cooper, Philip DiMarco, Mary Menges, and Nicholas-Jason Roache, Chenqi Zhu, Swethana Gopisetti, and Professor Gil Eckert">
    <title>BASES</title>
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
            <h3 class="text-muted main-title">BASES</h3>
        </div>
        <div class="row marketing">
            <div class="gameOutput" id="game1">
                <div id="game1-row1">
                    <center>
                        <h3>Game 1: {{ home_team }} vs. {{away_team}}</h3></center>
                    <div class="col-md-2 col-md-offset-5">
                        <div id="speedDisplay"></div>
                        <center><img id="playPause" type="image" onClick="playPauseDisplay()" src="/static/images/pause.png" alt="Play/Pause" width="40" height="40"></center>
                    </div>
                    <div class="col-md-12" id="scoreboard">
                        <div id="scoreboard-content">
                            <h4>Scoreboard</h4>
                            <div class="scoreboard-bgd">
                                <table style="float: left">
                                </table>
                                <table class="table table-condensed table-bordered scoreboard-teams">
                                    <tr class="warning" id="scoreboard-header">
                                        <td width='50px'>
                                            <center><b>Teams</b></center>
                                        </td>
                                        <td width='50px'>
                                            <center><b>1</b></center>
                                        </td>
                                        <td width='50px'>
                                            <center><b>2</b></center>
                                        </td>
                                        <td width='50px'>
                                            <center><b>3</b></center>
                                        </td>
                                        <td width='50px'>
                                            <center><b>4</b></center>
                                        </td>
                                        <td width='50px'>
                                            <center><b>5</b></center>
                                        </td>
                                        <td width='50px'>
                                            <center><b>6</b></center>
                                        </td>
                                        <td width='50px'>
                                            <center><b>7</b></center>
                                        </td>
                                        <td width='50px'>
                                            <center><b>8</b></center>
                                        </td>
                                        <td width='50px'>
                                            <center><b>9</b></center>
                                        </td>
                                        <td width='50px' id='s10'>
                                            <center><b>10</b></center>
                                        </td>
                                        <td width='50px' id="runs">
                                            <center><b>R</b></center>
                                        </td>
                                        <td width='50px'>
                                            <center><b>H</b></center>
                                        </td>
                                    </tr>
                                    <tr class="info" id="away-scoreboard">
                                        <td width='50px'>{{away_team}}</td>
                                        <td width='50px' id="a0"></td>
                                        <td width='50px' id="a1"></td>
                                        <td width='50px' id="a2"></td>
                                        <td width='50px' id="a3"></td>
                                        <td width='50px' id="a4"></td>
                                        <td width='50px' id="a5"></td>
                                        <td width='50px' id="a6"></td>
                                        <td width='50px' id="a7"></td>
                                        <td width='50px' id="a8"></td>
                                        <td width='50px' id="a9"></td>
                                        <td width='50px' id="ar"></td>
                                        <td width='50px' id="ah"></td>
                                    </tr>
                                    <tr class="success" id="home-scoreboard">
                                        <td width='50px'>{{home_team}}</td>
                                        <td width='50px' id="h0"></td>
                                        <td width='50px' id="h1"></td>
                                        <td width='50px' id="h2"></td>
                                        <td width='50px' id="h3"></td>
                                        <td width='50px' id="h4"></td>
                                        <td width='50px' id="h5"></td>
                                        <td width='50px' id="h6"></td>
                                        <td width='50px' id="h7"></td>
                                        <td width='50px' id="h8"></td>
                                        <td width='50px' id="h9"></td>
                                        <td width='50px' id="hr"></td>
                                        <td width='50px' id="hh"></td>
                                    </tr>
                                </table>
                                <table class="table table-condensed table-no-border pitch-count-pics">
                                    <tr>
                                        <td width='200px' style="padding: 0px">
                                            <center>
                                                <h4><p>Current Event:</p></h4>
                                            </center>
                                        </td>
                                        <td width='100px' style="padding: 0px">
                                            <center>
                                                <h4>Current Batter:</h4>
                                            </center>
                                        </td>
                                        <td width='19px' style="padding: 0px">
                                        </td>
                                        <td width='19px' style="padding: 0px">
                                        </td>
                                        <td width='19px' style="padding: 0px">
                                        </td>
                                        <td width='50px' style="padding: 0px">
                                            <center>
                                                <h4>Balls</h4></center>
                                        </td>
                                        <td width='50px' style="padding: 0px">
                                            <center>
                                                <h4>Strikes</h4></center>
                                        </td>
                                        <td width='50px' style="padding: 0px">
                                            <center>
                                                <h4>Outs</h4></center>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td width='200px' style="padding: 0px">
                                            <center>
                                                <h4><p id="current-event">Current Event:</p></h4>
                                            </center>
                                        </td>
                                        <td width='100px' id='up-to-bat' style="padding: 0px">
                                            <center>
                                                <h4><p id="current-batter">Play Ball!</p></h4>
                                            </center>
                                        </td>
                                        <td width='19px' style="padding: 0px">
                                        </td>
                                        <td width='19px' style="padding: 0px">
                                        </td>
                                        <td width='19px' style="padding: 0px">
                                        </td>
                                        <td width='50px' id="b" style="padding: 0px">
                                            <center><img id="ball0" src="/static/images/clear.png" alt="empty"> <img id="ball0" src="/static/images/clear.png" alt="empty"> <img id="ball0" src="/static/images/clear.png" alt="empty"> <img id="ball0" src="/static/images/clear.png" alt="empty"></center>
                                        </td>
                                        <td width='50px' id="s" style="padding: 0px">
                                            <center><img id="strike0" src="/static/images/clear.png" alt="empty"> <img id="strike0" src="/static/images/clear.png" alt="empty"> <img id="strike0" src="/static/images/clear.png" alt="empty"></center>
                                        </td>
                                        <td width='50px' id="o" style="padding: 0px">
                                            <center><img id="out0" src="/static/images/clear.png" alt="empty"> <img id="out0" src="/static/images/clear.png" alt="empty"> <img id="out0" src="/static/images/clear.png" alt="empty"></center>
                                        </td>
                                    </tr>
                                </table>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4" id="action-div">
                        <div class="action-container-div">
                            <center>
                                <h4>Last Event: <p id="action-img-title">Play Ball!</p></h4>
                                <img id="action-img" class="action-img" src="/static/images/play_ball.jpg" alt="action-img">
                            </center>
                            <script>
                            </script>
                        </div>
                    </div>
                    <div class="col-md-4" id="diamond-div">
                        <div class="diamond-container-div">
                            <center>
                                <!-- <h4>Diamond</h4> -->
                                <img id="baseball-img" class="diamond-img" src="/static/DiamondGraphics/empty.jpeg" alt="baseball-img">
                            </center>
                            <script>
                            </script>
                        </div>
                    </div>
                    <div class="col-md-4" id="gameEvents" align="left">
                        <h4>Game Events</h4>
                        <div class="scroll-box gameEvents-json" id="game1-row1-json">
                            <script>
                            // LOCATION OF FILE SHOULD BE LOCATED IN /static/simulations/
                            file_location = '/static/simulations/{{ game_file }}'
                            var output = "<ul>";
                            var current_event = "";

                            var playing = "true";
                            var x = "";
                            var myVar;

                            var firstHalf = true;

                            var objDiv = document.getElementById("game1-row1-json");

                            var i = 0;
                            var k = 0;
                            var playNumber = 1;
                            var top_inning = false;
                            var validHit = false;

                            // 0 .. 9 (10)
                            var home = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
                            var away = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

                            var awayRuns = 0;
                            document.getElementById("ar").innerHTML = "<center>" + awayRuns + "</center>";
                            var homeRuns = 0;
                            document.getElementById("hr").innerHTML = "<center>" + homeRuns + "</center>";
                            var awayHits = 0;
                            document.getElementById("ah").innerHTML = "<center>" + awayHits + "</center>";
                            var homeHits = 0;
                            document.getElementById("hh").innerHTML = "<center>" + homeHits + "</center>";


                            var balls = 0;
                            document.getElementById("b").innerHTML = '<center><img id="ball0" src="/static/images/clear.png" alt="empty"> <img id="ball0" src="/static/images/clear.png" alt="empty"> <img id="ball0" src="/static/images/clear.png" alt="empty"> <img id="ball0" src="/static/images/clear.png" alt="empty"></center>';
                            var strikes = 0;
                            document.getElementById("s").innerHTML = '<center><img id="strike0" src="/static/images/clear.png" alt="empty"> <img id="strike0" src="/static/images/clear.png" alt="empty"> <img id="strike0" src="/static/images/clear.png" alt="empty"></center>';
                            var outs = 0;
                            document.getElementById("o").innerHTML = '<center><img id="out0" src="/static/images/clear.png" alt="empty"> <img id="out0" src="/static/images/clear.png" alt="empty"> <img id="out0" src="/static/images/clear.png" alt="empty"></center>';

                            document.getElementById("speedDisplay").innerHTML = "<input name='displaySpeed' type='range' min='1' max='1005' value='106' step='100' onchange='showValue(this.value)'/><span id='range'></span>";

                            function showValue(newValue) {
                                // document.getElementById("range").innerHTML = (1006 - newValue);
                                clearInterval(myVar);
                                displaySpeed = (1006 - newValue);
                                if (playing == "true") {
                                    myVar = setInterval(function() {
                                        eventFunction(x)
                                    }, displaySpeed);
                                }
                            }

                            function playPauseDisplay() {
                                if (playing == "true") {
                                    clearInterval(myVar);
                                    document.getElementById("playPause").src = "/static/images/play.jpg";
                                    playing = "false";
                                } else {
                                    myVar = setInterval(function() {
                                        eventFunction(x)
                                    }, displaySpeed);
                                    document.getElementById("playPause").src = "/static/images/pause.png";
                                    playing = "true";
                                }
                            }

                            function playAudio(audio) {
                                if (displaySpeed >= 503) {
                                    audio.play();
                                }
                            }

                            var displaySpeed = 900;
                            myVar = setInterval(function() {
                                eventFunction(x)
                            }, displaySpeed);

                            function scoreFunction() {
                                if (top_inning) {

                                    if (i > 9) {
                                        away[9]++;
                                        document.getElementById("a" + 9).innerHTML = "<center>" + away[9] + "</center>";
                                    } else {
                                        away[i]++;
                                        document.getElementById("a" + i).innerHTML = "<center>" + away[i] + "</center>";
                                    }

                                    awayRuns++;
                                    document.getElementById("ar").innerHTML = "<center>" + awayRuns + "</center>";
                                    $("#baseball-img").attr('src', "/static/images/score.png");
                                    document.getElementById("action-img-title").innerHTML = "SCORE!";
                                } else {

                                    if (i > 9) {
                                        home[9]++;
                                        document.getElementById("h" + 9).innerHTML = "<center>" + home[9] + "</center>";

                                    } else {
                                        home[i]++;
                                        document.getElementById("h" + i).innerHTML = "<center>" + home[i] + "</center>";
                                    }


                                    homeRuns++;
                                    document.getElementById("hr").innerHTML = "<center>" + homeRuns + "</center>";
                                    $("#baseball-img").attr('src', "/static/images/score.png");
                                    document.getElementById("action-img-title").innerHTML = "SCORE!";

                                    if (i > 9) {
                                        if (home[9] > away[9]) {
                                            clearInterval(myVar);
                                            $("#baseball-img").attr('src', "/static/images/gameover.png");
                                            playAudio(new Audio('/static/sounds/cheering.mp3'));
                                            window.alert("Game Over! Final Score: {{home_team}} " + homeRuns + " {{away_team}} " + awayRuns);
                                            output += "------------------END OF GAME-----------------";
                                        }
                                    }
                                }
                            }

                            function hitFunction() {
                                if (top_inning) {
                                    if (validHit) {
                                        awayHits++;
                                        document.getElementById("ah").innerHTML = "<center>" + awayHits + "</center>";
                                    } else {
                                        validHit = true;
                                    }
                                } else {
                                    if (validHit) {
                                        homeHits++;
                                        document.getElementById("hh").innerHTML = "<center>" + homeHits + "</center>";
                                    } else {
                                        validHit = true;
                                    }
                                }
                            }

                            function baseRunning(diamond) {
                                // 000
                                // [First][Second][Third]
                                if (diamond == "100") {
                                    $("#baseball-img").attr('src', "/static/DiamondGraphics/1.jpeg");
                                } else if (diamond == "010") {
                                    $("#baseball-img").attr('src', "/static/DiamondGraphics/2.jpeg");
                                } else if (diamond == "001") {
                                    $("#baseball-img").attr('src', "/static/DiamondGraphics/3.jpeg");
                                } else if (diamond == "000") {
                                    $("#baseball-img").attr('src', "/static/DiamondGraphics/empty.jpeg");
                                } else if (diamond == "110") {
                                    $("#baseball-img").attr('src', "/static/DiamondGraphics/1and2.jpeg");
                                } else if (diamond == "011") {
                                    $("#baseball-img").attr('src', "/static/DiamondGraphics/2and3.jpeg");
                                } else if (diamond == "101") {
                                    $("#baseball-img").attr('src', "/static/DiamondGraphics/1and3.jpeg");
                                } else if (diamond == "111") {
                                    $("#baseball-img").attr('src', "/static/DiamondGraphics/loaded.jpeg");
                                }
                            }

                            function eventFunction(data) {

                                switch (data[i][k].code) {
                                    case "START-HALF-INNING":
                                        validHit = false;
                                        if (i == 0 && firstHalf) {
                                            firstHalf = false;
                                            playAudio(new Audio('/static/sounds/playball.mp3'));
                                        } else {
                                            $("#action-img").attr('src', "/static/images/inningover.png");
                                        }

                                        if (top_inning) {
                                            top_inning = false;
                                        } else {
                                            top_inning = true;
                                        }
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        outs = 0;
                                        pictureCount("out", outs);
                                        if (top_inning) {
                                            if (i > 9) {
                                                document.getElementById("s10").innerHTML = "<center><b>" + (i + 1) + "</b></center>";
                                                if (home[9] == 0 && away[9] == 0) {
                                                    document.getElementById("a" + 9).innerHTML = "<center>0</center>";
                                                    document.getElementById("h" + 9).innerHTML = "<center></center>";
                                                } else {
                                                    document.getElementById("a" + 9).innerHTML = "<center>" + away[9] + "</center>";
                                                }
                                            } else {
                                                document.getElementById("a" + i).innerHTML = "<center>" + away[i] + "</center>";
                                            }
                                        } else {
                                            if (i > 9) {
                                                if (home[9] == 0 && away[9] == 0) {
                                                    document.getElementById("a" + 9).innerHTML = "<center>0</center>";
                                                    document.getElementById("h" + 9).innerHTML = "<center>0</center>";
                                                } else {
                                                    document.getElementById("h" + 9).innerHTML = "<center>" + home[9] + "</center>";
                                                }
                                            } else {
                                                document.getElementById("h" + i).innerHTML = "<center>" + home[i] + "</center>";
                                            }
                                        }
                                        $("#baseball-img").attr('src', "/static/DiamondGraphics/empty.jpeg");

                                        break;
                                    case "NEW-BATTER":
                                        hitFunction();
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        var n = data[i][k].description.match(/^([^\s]+)/g);
                                        document.getElementById("current-batter").innerHTML = "<center>" + n + " is up to bat!</center>";
                                        balls = 0;
                                        pictureCount("ball", balls);
                                        strikes = 0;
                                        pictureCount("strike", strikes);
                                        break;
                                    case "NEW-PITCHER":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        break;
                                    case "BALL":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        balls++;
                                        pictureCount("ball", balls);
                                        playAudio(new Audio('/static/sounds/ball.mp3'));
                                        break;
                                    case "STRIKE":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        strikes++;
                                        pictureCount("strike", strikes);
                                        playAudio(new Audio('/static/sounds/strike.mp3'));
                                        break;
                                    case "FOUL-STRIKE":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        strikes++;
                                        pictureCount("strike", strikes);
                                        playAudio(new Audio('/static/sounds/strike.mp3'));
                                        break;
                                    case "FOUL":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        break;
                                    case "BB":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        $("#action-img").attr('src', "/static/images/walk.png");
                                        document.getElementById("action-img-title").innerHTML = "Walk!";
                                        validHit = false;
                                        break;
                                    case "KO":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        $("#action-img").attr('src', "/static/images/strike_out.jpg");
                                        document.getElementById("action-img-title").innerHTML = "Strike Out!";
                                        outs++;
                                        pictureCount("out", outs);
                                        playAudio(new Audio('/static/sounds/out.mp3'));
                                        validHit = false;
                                        break;
                                    case "1B":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        /*if (data[i][k + 1].code !== "OUT-BH" && data[i][k + 1].code !== "OUT-1BH" && data[i][k + 1].code !== "OUT-2BH" && data[i][k + 1].code !== "OUT-3BH" && data[i][k + 1].code !== "OUT-4BH") {
                                            hitFunction();
                                        }*/
                                        playAudio(new Audio('/static/sounds/hit.mp3'));
                                        validHit = true;
                                        break;
                                    case "2B":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        /*if (data[i][k + 1].code !== "OUT-BH" && data[i][k + 1].code !== "OUT-1BH" && data[i][k + 1].code !== "OUT-2BH" && data[i][k + 1].code !== "OUT-3BH" && data[i][k + 1].code !== "OUT-4BH") {
                                            hitFunction();
                                        }*/
                                        playAudio(new Audio('/static/sounds/hit.mp3'));
                                        validHit = true;
                                        break;
                                    case "3B":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        /*if (data[i][k + 1].code !== "OUT-BH" && data[i][k + 1].code !== "OUT-1BH" && data[i][k + 1].code !== "OUT-2BH" && data[i][k + 1].code !== "OUT-3BH" && data[i][k + 1].code !== "OUT-4BH") {
                                            hitFunction();
                                        }*/
                                        playAudio(new Audio('/static/sounds/hit.mp3'));
                                        validHit = true;
                                        break;
                                    case "HR":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        /*if (data[i][k + 1].code !== "OUT-BH" && data[i][k + 1].code !== "OUT-1BH" && data[i][k + 1].code !== "OUT-2BH" && data[i][k + 1].code !== "OUT-3BH" && data[i][k + 1].code !== "OUT-4BH") {
                                            hitFunction();
                                        }*/
                                        playAudio(new Audio('/static/sounds/hit.mp3'));
                                        playAudio(new Audio('/static/sounds/cheering.mp3'));
                                        $("#action-img").attr('src', "/static/images/homerun.jpeg");
                                        document.getElementById("action-img-title").innerHTML = "Home Run!";
                                        validHit = true;
                                        break;
                                    case "RUN-SCORES":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        scoreFunction();
                                        playAudio(new Audio('/static/sounds/cheering.mp3'));
                                        break;
                                    case "OUT-BH":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        outs++;
                                        pictureCount("out", outs);
                                        $("#action-img").attr('src', "/static/images/you_out.jpg");
                                        document.getElementById("action-img-title").innerHTML = "Out!";
                                        playAudio(new Audio('/static/sounds/out.mp3'));
                                        validHit = false;
                                        break;
                                    case "OUT-1BH":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        outs++;
                                        pictureCount("out", outs);
                                        $("#action-img").attr('src', "/static/images/you_out.jpg");
                                        document.getElementById("action-img-title").innerHTML = "Out!";
                                        playAudio(new Audio('/static/sounds/out.mp3'));
                                        validHit = false;
                                        break;
                                    case "OUT-2BH":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        outs++;
                                        pictureCount("out", outs);
                                        $("#action-img").attr('src', "/static/images/you_out.jpg");
                                        document.getElementById("action-img-title").innerHTML = "Out!";
                                        playAudio(new Audio('/static/sounds/out.mp3'));
                                        validHit = false;
                                        break;
                                    case "OUT-3BH":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        outs++;
                                        pictureCount("out", outs);
                                        $("#action-img").attr('src', "/static/images/you_out.jpg");
                                        document.getElementById("action-img-title").innerHTML = "Out!";
                                        playAudio(new Audio('/static/sounds/out.mp3'));
                                        validHit = false;
                                        break;
                                        /*case "OUT-4BH":
                                            output+="<p>"+ playNumber + '. ' + data[i][k].description + "</p>";
                                            outs++;
                                            pictureCount("out", outs);
                                            validHit = false;
                                            break;*/
                                    case "OUT-1B":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        outs++;
                                        pictureCount("out", outs);
                                        $("#action-img").attr('src', "/static/images/you_out.jpg");
                                        document.getElementById("action-img-title").innerHTML = "Out!";
                                        playAudio(new Audio('/static/sounds/out.mp3'));
                                        break;
                                    case "OUT-2B":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        outs++;
                                        pictureCount("out", outs);
                                        $("#action-img").attr('src', "/static/images/you_out.jpg");
                                        document.getElementById("action-img-title").innerHTML = "Out!";
                                        playAudio(new Audio('/static/sounds/out.mp3'));
                                        break;
                                    case "OUT-3B":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        outs++;
                                        pictureCount("out", outs);
                                        $("#action-img").attr('src', "/static/images/you_out.jpg");
                                        document.getElementById("action-img-title").innerHTML = "Out!";
                                        playAudio(new Audio('/static/sounds/out.mp3'));
                                        break;
                                    case "OUT-HP":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        outs++;
                                        pictureCount("out", outs);
                                        $("#action-img").attr('src', "/static/images/you_out.jpg");
                                        document.getElementById("action-img-title").innerHTML = "Out!";
                                        playAudio(new Audio('/static/sounds/out.mp3'));
                                        break;
                                    case "DIAMOND":
                                        baseRunning(data[i][k].description);
                                        break;
                                    case "END-INNING-SCORE":
                                        output += "<p>" + playNumber + '. ' + data[i][k].description + "</p>";
                                        current_event = "<center><p>" + data[i][k].description + "</p></center>";
                                        k = -1;
                                        i++;
                                        if (i == data.length) {
                                            clearInterval(myVar);
                                            $("#baseball-img").attr('src', "/static/images/gameover.png");
                                            playAudio(new Audio('/static/sounds/cheering.mp3'));
                                            window.alert("Game Over! Final Score: {{home_team}} " + homeRuns + " {{away_team}} " + awayRuns);
                                            output += "------------------END OF GAME-----------------";
                                        }
                                        break;
                                    default:
                                        clearInterval(myVar);
                                        output += "<center>------------------default------------------</center>";
                                }
                                playNumber++;
                                document.getElementById("game1-row1-json").innerHTML = output;
                                document.getElementById("current-event").innerHTML = current_event;
                                objDiv.scrollTop = objDiv.scrollHeight;
                                k++;
                                if (i == 6 && top_inning && data[i][k].code == "START-HALF-INNING" && displaySpeed >= 503) {
                                    clearInterval(myVar);
                                    $("#baseball-img").attr('src', "/static/images/Stretch.png");
                                    document.getElementById("playPause").src = "/static/images/play.jpg";
                                    new Audio('/static/sounds/TakeMeOut.mp3').play();
                                    setTimeout(function() {
                                        myVar = setInterval(function() {
                                            eventFunction(x)
                                        }, displaySpeed);
                                        document.getElementById("playPause").src = "/static/images/pause.png";
                                    }, 29000);
                                }
                            }

                            // Creates the string of pitchType to be returned to HTML
                            function makePictureCount(type, count, array) {
                                var countPics = "";

                                // Adds number of balls to array
                                for (pitch = 0; pitch < count; pitch++) {
                                    array[pitch] = '<img id="' + type + (pitch + 1) + '" src="/static/images/' + type + '.png" alt="' + type + '"> ';
                                }

                                // Outputs array to countPics string which is then displayed on HTML page
                                countPics = "<center>";
                                for (pitch = 0; pitch < array.length; pitch++) {
                                    countPics += array[pitch];
                                }
                                countPics += "</center>";

                                return countPics;
                            }

                            // Handles adding the Count Pictures to the HTML, calls makePictureCount() to create the string of pictures
                            function pictureCount(type, count) {

                                var clearPic = '<img id="' + type + '0" src="/static/images/clear.png" alt="empty"> ';

                                switch (type) {
                                    case "ball":

                                        var ball_array = [clearPic, clearPic, clearPic, clearPic];
                                        document.getElementById("b").innerHTML = makePictureCount(type, count, ball_array);

                                        break;

                                    case "strike":

                                        var ball_array = [clearPic, clearPic, clearPic];
                                        document.getElementById("s").innerHTML = makePictureCount(type, count, ball_array);
                                        break;

                                    case "out":

                                        var ball_array = [clearPic, clearPic, clearPic];
                                        document.getElementById("o").innerHTML = makePictureCount(type, count, ball_array);

                                        break;
                                    default:
                                }
                            }

                            $.getJSON(file_location, function(data) {
                                x = data;

                                output += "</ul>";
                            });
                            </script>
                        </div>
                    </div>
                </div>
                <!-- End Game1 Row1 -->
            </div>
            <!-- End GameOutput -->
        </div>
        <!-- /container -->
        <footer class="footer">
            <center>
                <p>Created By Reid Cooper, Philip DiMarco, Mary Menges, and Nicholas-Jason Roache, Chenqi Zhu, Swethana Gopisetti, and Professor Gil Eckert</p>
                <p>&copy; Monmouth University 2015
                    <script>
                    new Date().getFullYear() > 2015 && document.write(" - " + new Date().getFullYear());
                    </script>
                </p>
            </center>
        </footer>
</body>

</html>
