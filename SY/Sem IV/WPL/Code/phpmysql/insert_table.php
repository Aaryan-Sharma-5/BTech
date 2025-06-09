<?php  
$host = 'localhost';  
$user = 'root';  
$pass = '';  
$dbname = 'donation';  
  
$conn = mysqli_connect($host, $user, $pass,$dbname);  
if(!$conn){  
  die('Could not connect: '.mysqli_connect_error());  
}  
echo 'Connected successfully<br/>';  
  
$sql = 'INSERT INTO users(name,email,phone, bgroup) VALUES ("Sam", "sam@mail.com","+12345678","B+")';  
if(mysqli_query($conn, $sql)){  
 echo "Record inserted successfully";  
}else{  
echo "Could not insert record: ". mysqli_error($conn);  
}  
  
mysqli_close($conn);  
?> 