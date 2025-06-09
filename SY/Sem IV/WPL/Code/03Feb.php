<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>03 / 02 / 2025</title>
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
  $x = "Hello World!";
  $x = null;
  var_dump($x);
  echo "<br>";

  $t = date("H");
  if ($t < "10") {
    echo "Have a good morning!";
  } elseif ($t < "20") {
    echo "Have a good day!";
  } else {
    echo "Have a good night!";
  }
  echo "<br>";

  $favcolor = "red";
  switch ($favcolor) {
    case "red":
      echo "Your favorite color is red!";
      break;
    case "blue":
      echo "Your favorite color is blue!";
      break;
    case "green":
      echo "Your favorite color is green!";
      break;
    default:
      echo "Your favorite color is neither red, blue, nor green!";
  }
  echo "<br>";

  $colors = array("red", "green", "blue", "yellow");
  foreach ($colors as $value) {
    echo "$value <br>";
  }
  echo "<br>";

  $seasons = array("summer", "winter", "spring", "autumn");
  echo "Seasons are: $seasons[0], $seasons[1], $seasons[2], $seasons[3]";
  echo "<br>";
  echo count($seasons);
  echo "<br>";
  sort($seasons);
  foreach ($seasons as $s) {
    echo "$s<br/>";
  }
  echo "<br>";

  $salaries = array("John" => 2000, "Sally" => 3000, "Jane" => 4000);
  echo "John's salary is " . $salaries['John'] . "<br>";
  echo "Sally's salary is " . $salaries['Sally'] . "<br>";
  echo "Jane's salary is " . $salaries['Jane'] . "<br>";
  echo "<br>";
  print_r(array_change_key_case($salaries, CASE_UPPER));
  echo "<br>";
  print_r(array_chunk($salaries, 2));
  echo "<br>";

  $emp = array(
    array(1, "John", 2000),
    array(2, "Sally", 3000),
    array(3, "Jane", 4000)
  );
  for ($row = 0; $row < 3; $row++) {
    for ($col = 0; $col < 3; $col++) {
      echo $emp[$row][$col] . " ";
    }
    echo "<br>";
  }
  echo "<br>";

  ?>

</body>

</html>