<?php
// echo "<pre>";
// print_r($_REQUEST);
// echo "</pre>";

// echo "<pre>";
// print_r($_SERVER);
// echo "</pre>";

echo "Name: " . $_REQUEST['name'] . "<br>";
echo "Age: " . $_REQUEST['age'] . "<br>";
echo "User Agent: " . $_SERVER['HTTP_USER_AGENT'] . "<br>";
echo "IP Address: " . $_SERVER['REMOTE_ADDR'] . "<br>";
echo "Server Name: " . $_SERVER['SERVER_NAME'] . "<br>";

?>