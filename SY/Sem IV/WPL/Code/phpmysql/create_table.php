<?php  
$host = 'localhost';  
$user = 'root';  
$pass = '';  
$dbname = 'donate';  
  
$conn = mysqli_connect($host, $user, $pass,$dbname);  
if(!$conn){  
  die('Could not connect: '.mysqli_connect_error());  
}  
echo 'Connected successfully<br/>';  
  
$sql = "create table users(id INT AUTO_INCREMENT,name VARCHAR(20) NOT NULL,  
email VARCHAR(20) NOT NULL,phone VARCHAR(20) NOT NULL,
bgroup VARCHAR(20) NOT NULL,primary key (id))";  


if(mysqli_query($conn, $sql)){  
 echo "Table created successfully";  
}else{  
echo "Could not create table: ". mysqli_error($conn);  
}  
  
mysqli_close($conn);  
?> 