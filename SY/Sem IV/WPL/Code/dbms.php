<?php
$db_host = "localhost";
$db_user = "root";
$db_pass = "";
$db_name = "wpl";
$conn = new mysqli($db_host, $db_user, $db_pass, $db_name);
if (!$conn) {
  die("Connection failed");
} 
echo "Connected successfully";

$sql = "CREATE TABLE files (
  id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  file_name VARCHAR(50) NOT NULL,
  file_size INT(10) NOT NULL,
  file_type VARCHAR(50) NOT NULL
)";
if ($conn->query($sql) === TRUE) {
  echo "Table created successfully";
} else {
  echo "Error creating table: " . $conn->error;
}
?>