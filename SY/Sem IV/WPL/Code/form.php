<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Select Box Control</title>
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
  <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="get">
    Name: <input type="text" name="name"><br>
    Age: <input type="text" name="age"><br>
    <input type="submit" name="submit">
  </form>

  <?php
  if (isset($_GET['submit'])) {
    echo $_GET['name']; 
    echo "<br>";
    echo $_GET['age'];
  }

  // if ($_SERVER["REQUEST_METHOD"] == "POST") {
  //   $name = $_POST['name'];
  //   $age = $_POST['age'];
  //   echo "Name: $name <br>";
  //   echo "Age: $age <br>";
  // }
  ?>

  <!-- <select name="dropdown">
    <option value="1" selected>One</option>
    <option value="2">Two</option>
    <option value="3">Three</option>
    <option value="4">Four</option>
    <option value="5">Five</option>
    <hr>
    
    <input type="radio" name="Number" value="1" checked>One
    <br>
    <input type="radio" name="Number" value="2">Two
    <hr> 
  </select> -->

  </form>
</body>

</html>