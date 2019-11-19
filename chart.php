<?php
	/* Database connection settings */
	$host = 'localhost';
	$user = 'tackchen';
	$pass = 'tackchen831';
	$db = 'g2';
	$mysqli = new mysqli($host,$user,$pass,$db) or die($mysqli->error);

	$Current_Weight = '';
    $Date = '';


	//query to get data from the table
	$sql = "SELECT * FROM `Exercise_Log` WHERE User_ID = 1 ORDER BY Date ASC ";
    $result = mysqli_query($mysqli, $sql);

	//loop through the returned data
	while ($row = mysqli_fetch_array($result)) {
		$Current_Weight = $Current_Weight . '"'. $row['Current_Weight'].'",';
		$Date = $Date . '"'. $row['Date'].'",';
	}

	$Current_Weight = trim($Current_Weight,",");
    $Date = trim($Date,",");


	?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
		<meta name="description" content="">
		<meta name="author" content="">
		<link rel="icon" href="../../favicon.ico">
    	<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.bundle.min.js"></script>
		<title>Weight Graph</title>

		<!-- Bootstrap core CSS -->
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">

		<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
		<link href="../../assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">

		<!-- Custom styles for this template -->
		<link href="./css/dashboard.css" rel="stylesheet">

		<!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
		<!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
		<script src="../../assets/js/ie-emulation-modes-warning.js"></script>

		<!-- Chart.js and graph data -->
		<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>

		<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
		<!--[if lt IE 9]>
		<script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
		<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
		<![endif]-->

	</head>

	<body>
		
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Hello<span id="userName"></span></a>
        </div>
        <ul class="nav navbar-nav navbar-right">
          <li><a href="https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/fitness/art-20048269" target="_blank">Getting Started</a></li>
          <li><a href="https://www.jefit.com/exercises/" target="_blank">Exercises</a></li>
          <li><a href="https://www.webmd.com/fitness-exercise/default.htm" target="_blank">Health</a></li>
        </ul>
      </div>
    </nav>

		<div class="container-fluid">
			<div class="row">
				<div class="col-sm-3 col-md-2 sidebar">
					<ul class="nav nav-sidebar">
						<li><a href="./exlog.html">Workout Log <span class="sr-only">Workout Log</span></a></li>
						<li class="active"><a href="#">Weight Chart</a></li>
						<li><a href="./profile.html">Profile</a></li>
						<li><a href="./signin.html" class="text-danger">Sign Out</a></li>
					</ul>
				</div>
				<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
					<h1>Your Weight</h1>       
					<canvas id="chart" style="width: 100%; height: 65vh; background: #F0F0F0; border: 1px solid #555652; margin-top: 10px;"></canvas>

					<script>
						var ctx = document.getElementById("chart").getContext('2d');
						var myChart = new Chart(ctx, {
						type: 'line',
						data: {
							labels: [<?php echo $Date; ?>],
							datasets: [{
								label: 'Current Weight',
								data: [<?php echo $Current_Weight; ?>],
								backgroundColor: 'transparent',
								borderColor:'rgba(77, 166, 255)',
								borderWidth: 3
							}]		        
						},
							
					
						options:{
							scales: {scales:{yAxes: [{beginAtZero: false}], xAxes: [{autoskip: true, maxTicketsLimit: 20}]}},
							tooltips:{mode: 'index'},
							legend:{display: true, position: 'top', labels: {fontColor: 'rgb(0,0,0)', fontSize: 16}}
						}
						}
					);
					</script>
				</div>
			</div>
		</div>
		<!-- Bootstrap core JavaScript
		================================================== -->
		<!-- Placed at the end of the document so the pages load faster -->
		<script src="https://code.jquery.com/jquery-1.12.4.min.js" integrity="sha384-nvAa0+6Qg9clwYCGGPpDQLVpLNn0fRaROjHqs13t4Ggj3Ez50XnGQqc/r8MhnRDZ" crossorigin="anonymous"></script>
		<script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>
		<script src="../../dist/js/bootstrap.min.js"></script>
		<!-- Just to make our placeholder images work. Don't actually copy the next line! -->
		<script src="../../assets/js/vendor/holder.min.js"></script>
		<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
		<script src="../../assets/js/ie10-viewport-bug-workaround.js"></script>
	</body>
</html>