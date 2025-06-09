<?php
if(isset($_FILES['file'])) {
  echo "<pre>";
  print_r($_FILES);
  echo "</pre>";
  $file_name = $_FILES['file']['name'];
  $file_size = $_FILES['file']['size'];
  $file_tmp = $_FILES['file']['tmp_name'];
  $file_type = $_FILES['file']['type'];
  if(move_uploaded_file($file_tmp, "uploads/".$file_name)) {
    echo "File uploaded successfully";
  } else {
    echo "File not uploaded";
  }
}
?>

<html>
  <head>
    <title>Form 2</title>
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
    <form action="form2.php" method="post" enctype="multipart/form-data">
      <input type="file" name="file" /> <br>
      <input type="submit" value="Submit" />
    </form>
  </body>
</html>
