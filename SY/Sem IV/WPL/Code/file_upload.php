<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["fileToUpload"])) {
  $targetDir = "uploads/";
  $targetFile = $targetDir . basename($_FILES["fileToUpload"]["name"]);
  $uploadOk = 1;
  $fileType = strtolower(pathinfo($targetFile, PATHINFO_EXTENSION));

  if (file_exists($targetFile)) {
    echo "File already exists.";
    $uploadOk = 0;
  }

  $allowedTypes = array("jpg", "png", "txt", "pdf", "docx");
  if (!in_array($fileType, $allowedTypes)) {
    echo "Only JPG, PNG, TXT, PDF, DOCX files are allowed.";
    $uploadOk = 0;
  }

  if ($uploadOk == 1) {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $targetFile)) {
      echo "File uploaded successfully: " . htmlspecialchars(basename($_FILES["fileToUpload"]["name"]));
    } else {
      echo "Error uploading file.";
    }
  }
}
?>

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>File Upload & Operations</title>
  <style>
    * {
      margin: 10px;
      font-family: Georgia, "Times New Roman", Times, serif;
      font-size: 24px;
    }
  </style>
</head>

<body>
  <h2>Upload File</h2>
  <form action="" method="post" enctype="multipart/form-data"><br>
    <input type="file" name="fileToUpload"><br>
    <input type="submit" value="Upload File">
  </form>
</body>
</html>