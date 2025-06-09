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
  
$id=1;  
$name="Rahul";  
$mail="rahul@mail.com";
$phone="+21345678";
$bgroup="A+";  
$sql = "update users set name=\"$name\", bgroup=$bgroup where id=$id";  
if(mysqli_query($conn, $sql)){  
 echo "Record updated successfully";  
}else{  
echo "Could not update record: ". mysqli_error($conn);  
}  
  
mysqli_close($conn);  
?> 