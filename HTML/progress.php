<?php
// getting all values from the html form
if(isset($_POST['submit']))
{
    $Day = $_POST['Day'];
    $Date = $_POST['Date'];
    $Progress = $_POST['Progress'];
    $New_learnt = $_POST['New_learnt'];
}

// database details
$host= "localhost";
$username = "root";
$password = "";
$dbname = "progress";

// creating a connection
$con = mysqli_connect($host, $username, $password, $dbname);

// to ensure the connection is made
if (!$con)
{
    die("connection failed!" >mysqli_connect_error());
}

// using sql to create a data entry query
$sql = "INSERT INTO progress (Day,Date,Progress,New_learnt) Values('$Day','$Date','$Progress','$New_learnt')";

// send query to the database to add values and confirm if successful
$rs = mysqli_query($con, $sql);
if($rs)
{
    echo "Entries added!";
}

// close connection
mysqli_close($con);