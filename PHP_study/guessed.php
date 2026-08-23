<?php
    require 'connects.php';
    session_start();
?>
<?php
if(!isset($_SESSION['rand_num'])){
        $_SESSION['rand_num'] = rand(1, 100);
    }
?>
<?php
    if($_SERVER["REQUEST_METHOD"] === "POST"){
        $count = 0;
        $guess = (int)$_POST['guess'];
        $Real_num = (int)$_SESSION['rand_num'];

        if($guess === $Real_num){
            $query = "INSERT INTO leaderboard (Username, Counter, Number) VALUES ('{$_SESSION['name']}', {$_SESSION['count']}, $Real_num)";
            mysqli_query($conn, $query);
            $message = "Congratulations! You guessed the correct number: $Real_num";
            header("Location: guessed.php?msg=$message&isTrue=1");
        } elseif($guess < $Real_num){
            $_SESSION['count'] = isset($_SESSION['count']) ? $_SESSION['count'] + 1 : 1;
            $message = "Too low! Try again.";
            header("Location: guessed.php?msg=$message&isTrue=0");
        } else {
            $_SESSION['count'] = isset($_SESSION['count']) ? $_SESSION['count'] + 1 : 1;
            $message = "Too high! Try again.";
            header("Location: guessed.php?msg=$message&isTrue=0");
        }
    }
if(isset($_GET['reset'])){
    $count = 0;
    unset($_SESSION['rand_num']);
    unset($_SESSION['count']);
    header("Location: guessed.php");
}
?>
<?php if(isset($_GET['isTrue']) && $_GET['isTrue']==1) :?>
    <p class="question">
        <?= $_SESSION['rand_num'] ?>
    </p>
<?php else :?>
    <p class="question">?</p>
<?php endif; ?>
<?php if(isset($_GET['msg'])) :?>
    <p class="message">
        <?= $_GET['msg'] ?>
    </p>
<?php endif; ?>
<!DOCTYPE html>
<html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="leaderboard.css">
    <title>Number Guessered</title>
</head>
<body>
    <div class="carded">
    <?php if(isset($_GET['isTrue']) && $_GET['isTrue']==1) :?>
    <div class="dropdown">
        <a href="guessed.php?reset=1" class="button-sent">New Game</a>
        <a href="leaderboard.php" class="button-sent">Leaderboard</a>
    </div>
    <?php else :?>
    <form accept="" method="POST">
        <div class="guess_card">
        <div class="counter">
            Guesses: <?= isset($_SESSION['count']) ? $_SESSION['count'] : 0 ?>
        </div>
        <input type="number" name="guess" placeholder="Enter your guess" min="0" max="100" required>
        <button type="submit">Submit Guess</button>
        </div>
    </form>
    <?php endif; ?>
</div>
</body>
</html>