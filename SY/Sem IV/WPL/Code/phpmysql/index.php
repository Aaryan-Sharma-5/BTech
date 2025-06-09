<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Form</title>
</head>
<body bgcolor=#D6EAF8 align="center">
   <h1>Blood Donation Camp</h1>
   <div><h2>Registraion Form</h2></div>
   <form action="insert_db.php" method="POST">
       <label for="name">Name:</label><br />
       <input type="text" name="name" id="name" required><br/><br />

       <label for="email">Email:</label><br />
       <input type="text" name="email" id="email" required><br/><br />

       <label for="phone">Phone No.:</label><br />
       <input type="text" name="phone" id="phone" required><br/><br />

       <label for="bgroup">Blood Group:</label><br />
       <input type="text" name="bgroup" id="bgroup" required><br/><br />


        <input type="submit" name="submit" id="submit">

   </form> 
</body>
</html>