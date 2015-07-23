// From displayGame.tpl
// Now located here in /static/js/
// Too big to keep on webpage so it has been moved to is own javascript file

function displayGameWeb(file_location){

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

    var myTimer = setInterval(function(){ eventFunction()}, 1);


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
        if(i == data.length) {
          clearInterval(myTimer);
          window.alert("END OF GAME");
          console.log("END OF GAME");
        }
        break;
        default:
        clearInterval(myTimer);
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
}