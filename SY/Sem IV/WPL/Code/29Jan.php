<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>29 / 01 / 2025</title>
  <style>
    * {
      margin: 10px;
      text-align: center;
      font-family: Georgia, 'Times New Roman', Times, serif;
      font-size: 24px;
    }
  </style>
</head>

<body>
  <?php
  echo "Hello World!";
  echo "<br>";
  $msg = "Hello!";
  echo "Message is $msg";
  $x = 5;
  $y = 10.5;
  echo "<br>";
  $msg = "Hello PHP";
  echo "Message is $msg";
  echo "<br>";
  echo $x = 537;
  echo "<br>";
  var_dump($x);
  echo "<br>";
  echo $y;
  echo "<br>";
  echo $x + $y;
  echo "<br>";
  $z = "abc";
  $$z = 200;
  echo $z;
  echo "<br>";
  echo $$z;
  echo "<br>";
  echo $abc;
  echo "<br>";
  $a = 10;
  for ($i = 0; $i < 11; $i++) {
    echo "$a * $i <br>";
  }

  define("College", "KJSCE");
  echo College;
  echo "<br>";
  const message = "Hello KJSCE";
  echo message;
  echo "<br>";



  $cars = array("Volvo", "BMW", "Toyota");
  echo "I like " . $cars[0] . ", " . $cars[1] . " and " . $cars[2] . ".";
  echo "<br>";
  echo count($cars);
  echo "<br>";
  ?>

</body>

</html>