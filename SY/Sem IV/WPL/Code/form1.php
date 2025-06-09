<html>
  <head>
    <title>Form 1</title>
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
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
      setcookie("fname", $_POST["fname"], time() + 3600, "/");
      setcookie("lname", $_POST["lname"], time() + 3600, "/");
      setcookie("age", $_POST["age"], time() + 3600, "/");
      setcookie("address", $_POST["address"], time() + 3600, "/");
      echo "Cookies set successfully!";
    }
    ?>
    <form class="form-style" method="post" action="">
      First Name: <input type="text" name="fname" /><br>
      Last Name: <input type="text" name="lname" /><br>
      Age: <input type="text" name="age" /><br>
      Address: <input type="text" name="address" /><br>
      <input type="submit" value="Submit" />
    </form>
  </body>
</html>