<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "exp8";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

if (isset($_POST['create'])) {
  $firstname = $_POST['firstname'];
  $lastname = $_POST['lastname'];
  $email = $_POST['email'];

  $stmt = $conn->prepare("INSERT INTO exp8 (firstname, lastname, email) VALUES (?, ?, ?)");
  $stmt->bind_param("sss", $firstname, $lastname, $email);

  if ($stmt->execute()) {
    echo "<div class='alert alert-success'>New record created successfully!</div>";
  } else {
    echo "<div class='alert alert-danger'>Error: " . $stmt->error . "</div>";
  }
  $stmt->close();
}

if (isset($_POST['update'])) {
  $id = $_POST['id'];
  $firstname = $_POST['firstname'];
  $lastname = $_POST['lastname'];
  $email = $_POST['email'];

  $stmt = $conn->prepare("UPDATE exp8 SET firstname=?, lastname=?, email=? WHERE id=?");
  $stmt->bind_param("sssi", $firstname, $lastname, $email, $id);

  if ($stmt->execute()) {
    echo "<div class='alert alert-success'>Record updated successfully!</div>";
  } else {
    echo "<div class='alert alert-danger'>Error updating record: " . $stmt->error . "</div>";
  }
  $stmt->close();
}

if (isset($_POST['delete'])) {
  $firstname = $_POST['firstname'];

  if (!empty($firstname)) {
    $stmt = $conn->prepare("DELETE FROM exp8 WHERE firstname=?");
    $stmt->bind_param("s", $firstname);

    if ($stmt->execute()) {
      echo "<div class='alert alert-success'>Record(s) deleted successfully!</div>";
    } else {
      echo "<div class='alert alert-danger'>Error deleting record: " . $stmt->error . "</div>";
    }
    $stmt->close();
  } else {
    echo "<div class='alert alert-warning'>Please enter a valid first name!</div>";
  }
}

$sql = "SELECT * FROM exp8";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PHP CRUD - MyGuests</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="container mt-5">
  <h2 class="text-center mb-4">PHP CRUD - Guest Management</h2>

  <div class="card mb-4">
    <div class="card-header">Add New Guest</div>
    <div class="card-body">
      <form method="POST">
        <div class="mb-3">
          <label class="form-label">First Name</label>
          <input type="text" name="firstname" class="form-control" required>
        </div>
        <div class="mb-3">
          <label class="form-label">Last Name</label>
          <input type="text" name="lastname" class="form-control" required>
        </div>
        <div class="mb-3">
          <label class="form-label">Email</label>
          <input type="email" name="email" class="form-control" required>
        </div>
        <button type="submit" name="create" class="btn btn-success">Add Guest</button>
      </form>
    </div>
  </div>

  <div class="card mb-4">
    <div class="card-header">Update Guest</div>
    <div class="card-body">
      <form method="POST">
        <div class="mb-3">
          <label class="form-label">Guest ID</label>
          <input type="number" name="id" class="form-control" required>
        </div>
        <div class="mb-3">
          <label class="form-label">First Name</label>
          <input type="text" name="firstname" class="form-control" required>
        </div>
        <div class="mb-3">
          <label class="form-label">Last Name</label>
          <input type="text" name="lastname" class="form-control" required>
        </div>
        <div class="mb-3">
          <label class="form-label">Email</label>
          <input type="email" name="email" class="form-control" required>
        </div>
        <button type="submit" name="update" class="btn btn-primary">Update Guest</button>
      </form>
    </div>
  </div>

  <div class="card mb-4">
    <div class="card-header">Delete Guest by Name</div>
    <div class="card-body">
      <form method="POST">
        <div class="mb-3">
          <label class="form-label">Enter First Name</label>
          <input type="text" name="firstname" class="form-control" required>
        </div>
        <button type="submit" name="delete" class="btn btn-danger">Delete Guest</button>
      </form>
    </div>
  </div>

  <div class="card">
    <div class="card-header">Guest List</div>
    <div class="card-body">
      <table class="table table-bordered text-center">
        <thead class="table-dark">
          <tr>
            <th>ID</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          <?php
          if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
              echo "<tr>
                    <td>{$row['id']}</td>
                    <td>{$row['firstname']}</td>
                    <td>{$row['lastname']}</td>
                    <td>{$row['email']}</td>
                  </tr>";
            }
          } else {
            echo "<tr><td colspan='4' class='text-center'>No records found</td></tr>";
          }
          $conn->close();
          ?>
        </tbody>
      </table>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>