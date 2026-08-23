<?php
    require 'connects.php';
    $query = "SELECT * FROM `leaderboard` ORDER BY Counter ASC;";
    $result = mysqli_query($conn, $query);
?>


<!DOCTYPE html>
<html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="leaderboard.css">
    <title>Leaderboard</title>
</head>
<body>
    <div class="carded">
        <div class="table_head">ID</div>
        <div class="table_head">USER</div>
        <div class="table_head">COUNTER</div>
        <div class="table_head">NUMBER</div>
    </div>

    <?php if (mysqli_num_rows($result) > 0): ?>
        <?php $number = 1 ?>
        <?php while($row = $result->fetch_assoc()): ?>
            <div class="carded">
                <div class="table_head"><?php echo $number++ ?></div>
                <div class="table_head"><?php echo htmlspecialchars($row['Username']); ?></div>
                <div class="table_head"><?php echo htmlspecialchars($row['Counter']); ?></div>
                <div class="table_head"><?php echo htmlspecialchars($row['Number']); ?></div>
            </div>
        <?php endwhile ?>
    <?php else: ?>
        <div class="carded no-data">
            <div style="grid-column: span 4; text-align:center; color:#000; background:none;">
                <p>No data found</p>
            </div>
        </div>
    <?php endif ?>
<div class="center">
    <a href="guessed.php?reset=1" class="button-sent">New Game</a>
</div>
</body>
</html>