<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cookie and Session</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<?php
session_start();
$cookie_name = "user";
$cookie_value = "Aaryan";
if (!isset($_COOKIE[$cookie_name])) {
  setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");
  echo "Cookie '" . $cookie_name . "' has been set!<br>";
} else {
  echo "Cookie '" . $cookie_name . "' is already set!<br>";
  echo "Cookie Value: " . $_COOKIE[$cookie_name] . "<br>";
}

if (isset($_POST['modify_cookie'])) {
  setcookie($cookie_name, "OtherUser", time() + (86400 * 30), "/");
  header("Location: " . $_SERVER['PHP_SELF']);
  exit();
}

if (isset($_POST['delete_cookie'])) {
  setcookie($cookie_name, "", time() - 3600, "/");
  echo "Cookie '" . $cookie_name . "' has been deleted!<br>";
}

if (!isset($_SESSION['username'])) {
  $_SESSION['username'] = 'DefaultUser';
  echo "Session variable 'username' is set to: " . $_SESSION['username'] . "<br>";
} else {
  echo "Session variable 'username' is: " . $_SESSION['username'] . "<br>";
}

if (isset($_POST['modify_session'])) {
  $_SESSION['username'] = 'UpdatedUser';
  echo "Session variable 'username' has been updated to: " . $_SESSION['username'] . "<br>";
}

if (isset($_POST['destroy_session'])) {
  session_unset();
  session_destroy();
  header("Location: " . $_SERVER['PHP_SELF']);
  exit();
}
?>

<body class="bg-light">
  <div class="container mt-4">
    <div class="card p-4 shadow">
      <h2 class="text-center">PHP Cookies & Session Handling</h2>

      <div class="d-flex justify-content-between mt-3">
        <form method="POST">
          <input type="submit" name="modify_cookie" value="Modify Cookie" class="btn btn-primary">
          <input type="submit" name="delete_cookie" value="Delete Cookie" class="btn btn-danger">
        </form>
        <form method="POST">
          <input type="submit" name="modify_session" value="Modify Session" class="btn btn-warning">
          <input type="submit" name="destroy_session" value="Destroy Session" class="btn btn-dark">
        </form>
      </div>

      <form method="POST" class="mt-4">
        <div class="mb-3">
          <label for="name" class="form-label">Name:</label>
          <input type="text" id="name" name="name" class="form-control">
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">Email:</label>
          <input type="email" id="email" name="email" class="form-control">
        </div>
        <div class="mb-3">
          <label for="message" class="form-label">Message:</label>
          <textarea id="message" name="message" class="form-control"></textarea>
        </div>
        <button type="submit" class="btn btn-success mt-3">Submit</button>
      </form>

      <?php if ($_SERVER['REQUEST_METHOD'] == 'POST' && !isset($_POST['modify_cookie']) && !isset($_POST['delete_cookie'])): ?>
        <div class="mt-4">
          <h2>Submitted Form Data:</h2>
          <p><strong>Name:</strong> <?= isset($_POST['name']) ? htmlspecialchars($_POST['name']) : 'N/A' ?></p>
          <p><strong>Email:</strong> <?= isset($_POST['email']) ? htmlspecialchars($_POST['email']) : 'N/A' ?></p>
          <p><strong>Message:</strong> <?= isset($_POST['message']) ? htmlspecialchars($_POST['message']) : 'N/A' ?></p>
        </div>
      <?php endif; ?>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>