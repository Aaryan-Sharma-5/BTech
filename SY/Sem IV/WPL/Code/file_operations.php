<?php
$targetDir = "uploads/";

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_FILES["fileToUpload"])) {
  $fileName = basename($_FILES["fileToUpload"]["name"]);
  $targetFile = $targetDir . $fileName;
  $fileType = strtolower(pathinfo($targetFile, PATHINFO_EXTENSION));

  $allowedTypes = array("jpg", "png", "txt", "pdf", "docx");
  if (in_array($fileType, $allowedTypes)) {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $targetFile)) {
      echo "File uploaded successfully: " . htmlspecialchars($fileName);
    } else {
      echo "Error uploading file.";
    }
  } else {
    echo "Invalid file type. Only JPG, PNG, TXT, PDF, and DOCX files are allowed.";
  }
}

if (isset($_POST['readFile'])) {
  $file = $targetDir . $_POST['readFile'];
  if (file_exists($file)) {
    echo "<h3>File Contents:</h3><pre>" . htmlspecialchars(file_get_contents($file)) . "</pre>";
  } else {
    echo "File does not exist.";
  }
}

if (isset($_POST['writeFile']) && isset($_POST['writeText'])) {
  $file = $targetDir . $_POST['writeFile'];
  file_put_contents($file, $_POST['writeText']);
  echo "File written successfully.";
}

if (isset($_POST['appendFile']) && isset($_POST['appendText'])) {
  $file = $targetDir . $_POST['appendFile'];
  file_put_contents($file, $_POST['appendText'] . PHP_EOL, FILE_APPEND);
  echo "Text appended successfully.";
}

if (isset($_POST['deleteFile'])) {
  $file = $targetDir . $_POST['deleteFile'];
  if (file_exists($file)) {
    unlink($file);
    echo "File deleted successfully.";
  } else {
    echo "File not found.";
  }
}

if (isset($_POST['downloadFile'])) {
  $file = $targetDir . $_POST['downloadFile'];
  if (file_exists($file)) {
    header("Content-Disposition: attachment; filename=" . basename($file));
    header("Content-Type: application/octet-stream");
    readfile($file);
    exit;
  } else {
    echo "File not found.";
  }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>File Upload & Operations</title>
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
  <h2>Upload a File</h2>
  <form action="" method="post" enctype="multipart/form-data"><br>
    <input type="file" name="fileToUpload" required><br>
    <input type="submit" value="Upload File">
  </form>

  <h2>File Operations</h2>

  <form method="post">
    <input type="text" name="readFile" placeholder="Enter file name"><br>
    <input type="submit" value="Read File"><br>
  </form>

  <form method="post">
    <input type="text" name="writeFile" placeholder="Enter file name"><br>
    <textarea name="writeText" placeholder="Enter text to write"></textarea><br>
    <input type="submit" value="Write to File">
  </form>

  <form method="post">
    <input type="text" name="appendFile" placeholder="Enter file name"><br>
    <textarea name="appendText" placeholder="Enter text to append"></textarea><br>
    <input type="submit" value="Append to File">
  </form>

  <form method="post">
    <input type="text" name="deleteFile" placeholder="Enter file name"><br>
    <input type="submit" value="Delete File"><br>
  </form>

  <form method="post">
    <input type="text" name="downloadFile" placeholder="Enter file name"><br>
    <input type="submit" value="Download File"><br>
  </form>
</body>
</html>