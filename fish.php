<html>
<head>
<title>Results</title>
<?php
    $servername = "localhost";
    $username = "dyck5795";
    $password = "guest";
    $dbname = "dyck5795";
    
    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    ?>

</head>
<body>
<?php
    $sql = "SELECT *
    FROM Results
    WHERE 1
    ";
$rows = array();
while($r = mysqli_fetch_assoc($sql)) {
    $rows[] = $r;
}
print json_encode($rows);

?>

</body>
</html>