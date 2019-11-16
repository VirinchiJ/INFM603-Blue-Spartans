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
    	<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.bundle.min.js"></script>
		<title>Accelerometer data</title>

		<style type="text/css">			
			body{
				font-family: Arial;
			    margin: 80px 100px 10px 100px;
			    padding: 0;
			    color: white;
			    text-align: center;
			    background: #555652;
			}

			.container {
				color: #E8E9EB;
				background: #222;
				border: #555652 1px solid;
				padding: 10px;
			}
		</style>

	</head>

	<body>	   
	    <div class="container">	
	    <h1>Your weight fluctuation by date</h1>       
			<canvas id="chart" style="width: 100%; height: 65vh; background: #222; border: 1px solid #555652; margin-top: 10px;"></canvas>

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
		                borderColor:'rgba(255,99,132)',
		                borderWidth: 3
		            }]		        
				},
		            
		     
		        options:{
		            scales: {scales:{yAxes: [{beginAtZero: false}], xAxes: [{autoskip: true, maxTicketsLimit: 20}]}},
		            tooltips:{mode: 'index'},
		            legend:{display: true, position: 'top', labels: {fontColor: 'rgb(255,255,255)', fontSize: 16}}
		        }
				}
		    );
			</script>
	    </div>
	    
	</body>
</html>