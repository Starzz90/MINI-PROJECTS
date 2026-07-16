<?php
    if($_SERVER["REQUEST_METHOD"] === "POST"){
        session_start();
        $_SESSION['name'] = $_POST['name'];
        header("Location: guess.php");
    }
    if(!isset($_SESSION['rand_num'])){
        $_SESSION['rand_num'] = rand(1, 100);
    }
    if($_SERVER["REQUEST_METHOD"] === "POST"){
        session_start();
        $guess = $_POST['guess'];
        $Real_num = $_SESSION['rand_num'];

        if($guess == $Real_num){
            $message = "Congratulations! You guessed the correct number: $Real_num";
            header("Location: guess.php?msg=$message&isTrue=1");
            unset($_SESSION['rand_num']);
        } elseif($guess < $Real_num){
            $message = "Too low! Try again.";
            header("Location: guess.php?msg=$message&isTrue=0");
        } else {
            $message = "Too high! Try again.";
            header("Location: guess.php?msg=$message&isTrue=0");
        }
    }
?>
<!DOCTYPE html>
<html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="guess.css">
    <title>Number Guesser</title>
</head>
<body>
    <h1>Welcome to the Number Guesser Game!</h1>
    <form method="POST" action="">
        <div class="card">
            <input type="text" id="name" name="name" class="name" placeholder="Enter your Name" required>
            <button type="submit" class="buttoned">Start Game</button>
        </div>
</body>
</html>

