<!DOCTYPE html>
<html lang="en">

<head>
    <title>B.A.S.E.S.</title>

    <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">

    <link href="http://getbootstrap.com/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">

    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>

    <link rel="stylesheet" href="/static/css/custom.css">

</head>

<body>

    <div class="col-md-12">
        <div class="header">
            <nav>
                <ul class="nav nav-pills pull-right">
                    <li role="presentation" class="active"><a href="/">Home</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">B.A.S.E.S.</h3>
        </div>

        <div class="row">
            <div class="col-md-12" id="displayInfo">
                <p>Braves</p>
                <script>
                    jQuery.get('/static/teams/Braves_batting.txt', function(data) {
                        $('#insert').html(data.replace('\n','</br>'));
                    });
                </script>
                <div class="col-md-12" id="insert"></div>
            </div>
        </div>

        <div class="row">
            <div class="col-md-12" id="displayJSON">
                <p>JSON</p>
                <script>
                    $.getJSON('/static/simulations/sample.json', function(data) {
                            //now json variable contains data in json format
                            //let's display a few items
                            var output="<ul>";
                            for(var i in data.sample){
                                output += '<li>Name: ' + data.sample[i].name + '<br />About: ' + data.sample[i].about+"</li>";
                            }
                            output += "</ul>";
                            $('#insert2').html(output);
                        });
                </script>
                <div class="col-md-12" id="insert2"></div>
            </div>
        </div>

        <footer class="footer">
            <p>&copy; Monmouth University
                <script type="text/javascript">
                  document.write(new Date().getFullYear());
              </script>
          </p>
      </footer>

  </div>
</body>

</html>