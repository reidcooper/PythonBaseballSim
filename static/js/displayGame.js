// From displayGame.tpl
// Now located here in /static/js/
// Too big to keep on webpage so it has been moved to is own javascript file

function displayGameWeb() {
    playAudio(new Audio('/static/sounds/playball.mp3'));


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
                        document.getElementById("a" + 9).innerHTML = "<center>" + away[9] + "</center>";
                    } else {
                        document.getElementById("a" + i).innerHTML = "<center>" + away[i] + "</center>";
                    }
                } else {
                    if (i > 9) {
                        document.getElementById("h" + 9).innerHTML = "<center>" + home[9] + "</center>";
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
}
