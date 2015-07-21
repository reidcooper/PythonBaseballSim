
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

  <div class="container">
    <div class="header clearfix">
      <nav>
        <ul class="nav nav-pills pull-right">
          <li role="presentation"><a href="/">Home</a></li>
          <li role="presentation"><a href="/historicGame">Historic Game</a></li>
          <li role="presentation" class="active"><a href="/about">About</a></li>
        </ul>
      </nav>
      <h3 class="text-muted">B.A.S.E.S.</h3>
    </div>

    <div class="row marketing">
      <div class="col-md-12">
        <h4>About the Project</h4>
        <p>The B.A.S.E.S. project was developed by a group of summer research students and professors at Monmouth University during the university's annual School of Science Summer Research Program.</p>
        <p>This program intends to accurately simulate a baseball game from first pitch to last. The simulation will be based on real data obtained from the 2014 MLB season. The simulation will model a game pitch-by-pitch and use batting and pitching statistics as well as fielding statistics to best predict the outcome of a game.</p>
        <p>Major Features/Goals:</p>
        <ul>
          <li>Store relevant statistics of a single Major League Baseball Season in comma-separated values (CSV) files</li>
          <li>Simulate the interaction between a batter and a pitcher</li>
          <li>Simulate the actions of players on the field</li>
          <li>Simulate the interaction between the home and away teams</li>
          <li>Analyze the outcome of a simulated game based on the data provided</li>
          <li>Allow the user to choose any two Major League Baseball teams to simulate a game</li>
          <li>Provide a user interface with a scoreboard which updates throughout the game</li>
        </ul>

        <h4>Development</h4>
        <p>The B.A.S.E.S. project was developed using these following tools and frameworks</p>
        <ul>
          <li>Google Drive</li>
          <li>Github</li>
          <ul>
            <li><a href="https://github.com/reidcooper/PythonBaseballSim">Python Repo</a></li>
            <li><a href="https://github.com/SoftwarePhil/BaseballSim">Java Skeleton Prototype Repo</a></li>
          </ul>
          <li>Python 2.7.x</li>
          <li>Java 1.7</li>
          <li>Bottle: Python Web Framework 0.12</li>
          <li>Javascript, HTML, and CSS</li>
          <li>Bootstrap CSS Framework</li>
        </ul>

        <h4>Members</h4>
        <p>B.A.S.E.S. development team members, without us, this whole thing wouldn't of happened.</p>
        <ul>
          <li>Reid Cooper</li>
          <li>Philip DiMarco</li>
          <li>Mary Menges</li>
          <li>Nicholas-Jason Roache</li>
          <li>Chenqi Zhu</li>
          <li>Swethana Gopisetti</li>
          <li>Our Research Mentor and Professor, Gil Eckert</li>
        </ul>

        <h4>Funding</h4>
        <p>Our project wouldn't be possible if it wasn't for our wonderful sponsors!</p>
        <ul>
          <li><a href="http://www.definedlogic.com/">Defined Logic</a></li>
          <li><a href="http://www.starschallenge.org/stars/">Drs. Margaret Ann and Steven Chappell</a></li>
          <li><a href="http://www.monmouth.edu">Monmouth University</a></li>
          <li><a href="http://www.monmouth.edu/school-of-science/school-of-science.aspx">Monmouth University School of Science</a></li>

        </ul>

        <h4>Sources</h4>
        <p>Items used on our website and in our simulation are given credit below.</p>
        <ul>
          <li><a href="https://en.wikipedia.org/wiki/File:Baseball_(crop).jpg">Baseball Photo on main page was provided by Wikipedia</a></li>
          <li><a href="http://www.fangraphs.com/">Fangraphs, for their data and statistical glossaries</a></li>
          <li><a href="http://www.mlb.com/">Major League Baseball</a></li>
          <li>Scoreboard (edited) from Backyard Baseball</li>
        </ul>
      </div>
    </div>

    <footer class="footer">
      <center>
        <p>Created By Reid Cooper, Philip DiMarco, Mary Menges, and Nicholas-Jason Roache, Chenqi Zhu, Swethana Gopisetti, and Professor Gil Eckert</p>
        <p>&copy; Monmouth University
          2015<script>new Date().getFullYear()>2015&&document.write("-"+new Date().getFullYear());</script>
        </p>
      </center>
    </footer>

  </div> <!-- /container -->
</body>
</html>
