<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" || $_SERVER["REQUEST_METHOD"] == "GET") {
    $name = trim($_REQUEST['name']);
    $email = trim($_REQUEST['email']);
    $phone = trim($_REQUEST['phone']);

    if (empty($name) || empty($email) || empty($phone)) {
        echo "All fields are required.";
        exit();
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Invalid email format.";
        exit();
    }

    echo "<h2>Registration Successful (REQUEST Method)</h2>";
    echo "<p><strong>Name:</strong> $name</p>";
    echo "<p><strong>Email:</strong> $email</p>";
    echo "<p><strong>Phone:</strong> $phone</p>";
} else {
    echo "Invalid request method.";
}
