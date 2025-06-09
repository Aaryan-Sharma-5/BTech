<?php
$host = 'localhost';  
$user = 'root';  
$pass = '';  
$dbname = 'donate';  
  
$conn = mysqli_connect($host, $user, $pass,$dbname);
if(isset($_POST['submit'])){
    if(!empty($_POST['name']) && !empty($_POST['email']) && !empty($_POST['phone']) && !empty($_POST['bgroup'])){
        $name = $_POST['name'];
        $email = $_POST['email'];
        $phone = $_POST['phone'];
        $bgroup = $_POST['bgroup'];
         
        $sql = "insert into users(name,email,phone,bgroup) values('$name','$email','$phone','$bgroup')";

        $run = mysqli_query($conn, $sql) or die(mysqli_error());

        if($run){
            echo "Form submitted successfully";
        }
        else{
            echo "Form not submitted";
        }
    }
    else{
        "all fields required";
    }
}

?>