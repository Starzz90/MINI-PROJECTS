<?php
    include "connected.php";

    if($_SERVER["REQUEST_METHOD"] === "POST"){
        $user = $_POST["user"];
        $email = $_POST["email"];
        $password = $_POST["password"];
        $encrypt = password_hash($password, PASSWORD_DEFAULT);

        $query = "INSERT INTO log(user, email, password) VALUES ($user, $email, $encrypt)";

        mysqli_query($conn, $query);

    header("Location: login.php");
    }
?>
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="database.css">
    <title>Register</title>
</head>
<body>
    <div class="body">
        <form method="POST" action="">
            <input type="text" name="user" placeholder="Type in username" class="input" required></br>
            <input type="text" name="email" placeholder="Type in email" class="input" required></br>
            <input type="text" name="password" placeholder="Type in password" class="input" required></br>

            <div class="center">
                <button class="button" type="submmit" name="register">REGISTER</button>
            </div>
        </form>
    </div>
</body>
</html>