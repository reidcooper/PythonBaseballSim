<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
  <meta name="B.A.S.E.S." content="">
  <meta name="author" content="Reid Cooper, Philip DiMarco, Mary Menges, and Nicholas-Jason Roache, Chenqi Zhu, Swethana Gopisetti, and Professor Gil Eckert">

  <title>B.A.S.E.S.</title>

  <!-- Bootstrap core CSS -->
  <link href="static/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="static/css/jumbotron-narrow.css" rel="stylesheet">

  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>

  <script type="text/javascript" src="/static/js/submit_teams.js" charset="utf-8"></script>

  <script type="text/javascript" src="/static/js/dist/jstree.min.js" charset="utf-8"></script>
  <script type="text/javascript" src="/static/js/file_tree.js" charset="utf-8"></script>
  <link rel="stylesheet" href="/static/js/dist/themes/default/style.min.css">

  <link rel="stylesheet" href="/static/css/custom.css">

  <link href="//cdnjs.cloudflare.com/ajax/libs/select2/4.0.0/css/select2.min.css" rel="stylesheet" />
  <script src="//cdnjs.cloudflare.com/ajax/libs/select2/4.0.0/js/select2.min.js"></script>
</head>

<body>

  <div class="container">
    <div class="header clearfix">
      <nav>
        <ul class="nav nav-pills pull-right">
          <li role="presentation"><a href="/">Home</a></li>
          <li role="presentation" class="active"><a href="/historicGame">Historic Game</a></li>
          <li role="presentation"><a href="/about">About</a></li>
        </ul>
      </nav>
      <h3 class="text-muted main-title">B.A.S.E.S.</h3>
    </div>

    <div class="jumbotron">
      <h1>Historical Games</h1>
    </div>

    <div class="row marketing center-content">
      <div class="col-md-12">
        <h4>Here you can select a previously simulated game and view the results!</h4>
        <p>Since we are able to simulate baseball games, provided two teams, wouldn't it be nice to revisit a game already simulated? That's why we provided this tool to allow the user to select a previously simulate game and either: view the results of the game, download the game file, or upload a game file!</p>
        <p>Just make sure the Game File is the correct format!</p>
      </div>
      <div class="col-md-12 game-browser">
        <h4>Game Browser</h4>
        <form class="select-game-form" id="select-game-form" name="select-game-form" action="/submitHistoricGame" method="POST" enctype="multipart/form-data">
          <div class="scroll-box historicGameFiles" id="game1-row1-json">
            <div id="jstree"></div>
          </div>
          <!-- Holds the value of the game file to be submitted -->
          <input type="hidden" name="gameFile" value="0"/>
          <br>
          <center><input type="file" name="upload" /></center>
          <div id="createTeams" class="createTeams">
            <input class="btn btn-success" name="play_ball_btn" value="Play Ball!" type="submit"/>
            <a href="/index" id="download_btn" name="download_btn" class="btn btn-success mylink">Download!</a>
            <input class="btn btn-success" name="upload_btn" value="Upload!" type="submit"/>
          </div>
        </form>
      </div>
    </div>

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
