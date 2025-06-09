<?php
if ($_SERVER["REQUEST_METHOD"] == "GET") {
    $name = trim($_GET['name']);
    $email = trim($_GET['email']);
    $phone = trim($_GET['phone']);

    if (empty($name) || empty($email) || empty($phone)) {
        echo "All fields are required.";
        exit();
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Invalid email format.";
        exit();
    }

    echo "<h2>Registration Successful (GET Method)</h2>";
    echo "<p><strong>Name:</strong> $name</p>";
    echo "<p><strong>Email:</strong> $email</p>";
    echo "<p><strong>Phone:</strong> $phone</p>";
} else {
    echo "Invalid request method.";
}
