<?php if(isset($_GET['isTrue'])) :?>
    <p class="question">
        <?= $_SESSION['Rand_num'] ?>
    </p>
<?php else :?>
        <p class="question">?</p>
<?php endif; ?>
<form accept="" method="POST">
    <input type="number" name="guess" placeholder="Enter your guess" required>
    <button type="submit">Submit Guess</button>
</form>
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
    <link rel="stylesheet" href="database.css">
    <title>Number Guessered</title>
</head>
<body>
</body>
</html>