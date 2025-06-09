<?php  
$host = 'localhost:3306';  
$user = 'root';  
$pass = '';  
$dbname = 'donation';  
  
$conn = mysqli_connect($host, $user, $pass,$dbname);  
if(!$conn){  
  die('Could not connect: '.mysqli_connect_error());  
}  
echo 'Connected successfully<br/>';  
  
$id=1;  
$sql = "delete from users where id=$id";  
if(mysqli_query($conn, $sql)){  
 echo "Record deleted successfully";  
}else{  
echo "Could not deleted record: ". mysqli_error($conn);  
}  
?>