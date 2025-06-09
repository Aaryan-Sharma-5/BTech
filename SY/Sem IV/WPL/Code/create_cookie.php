<?php
$cookie_name = "user";
$cookie_value = "admin";
setcookie($cookie_name, $cookie_value, time() + (86400), "/");
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Cookie</title>
  <style>
    * {
      margin: 10px;
      text-align: center;
      font-family: Georgia, "Times New Roman", Times, serif;
      font-size: 20px;
    }
  </style>
</head>

<body>
  <?php
  if (!isset($_COOKIE[$cookie_name])) {
    echo "Cookie named '" . $cookie_name . "' is not set!";
  } else {
    echo "Value is: " . $_COOKIE[$cookie_name];
  }
  ?>
</body>
</html>