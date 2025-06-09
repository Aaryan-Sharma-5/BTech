<!-- 
  1. PHP mysqli_connect() function is used to connect with Mysql database. 
  2. It returns resource if connection is established or null.
        SYNTAX: resource mysqli_connect (server, username, password) 
 -->

<?php
$servername = "localhost";
$username = "root";
$password = " ";
//$conn = new mysqli($servername, $username, $password);
$conn = mysqli_connect($servername, $username, $password);

if(!$conn )  
{  
  die('Could not connect: ' . mysqli_connect_error());  
}  
echo 'Connected successfully <br/>';  

// PHP Mysqli Create Database Example

$sql = 'CREATE Database donate';  
if(mysqli_query( $conn,$sql)){  
  echo "Database created successfully.";  
}
else{  
echo "Sorry, database creation failed ".mysqli_error($conn);  
}  

mysqli_close($conn); 




?>