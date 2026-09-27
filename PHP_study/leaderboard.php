<?php
    require 'connects.php';
    $query = "SELECT * FROM leaderboard";
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
        <tr>
        <div class="table_head">
            <th class="table_head">ID</th>
</div>
<div class="table_head">
            <th class="table_head">USER</th>
</div>
<div class="table_head">
            <th class="table_head">COUNTER</th>
</div>
<div class="table_head">
            <th class="table_head">NUMBER</th>
        </div>
    </tr>
    </div>
    <?php if (mysqli_num_rows($result) > 0): ?>
            <?php $number = 1 ?>
            <?php while($row = $result->fetch_assoc()): ?>
                <td><?php echo $number; ?></td>
                <td><?php echo $row['user']; ?></td>
                <td><?php echo $row['counter']; ?></td>
                <td><?php echo $row['number']; ?></td>
            <?php $number += 1 ?>
            <?php endwhile ?>
        <?php else: ?>
            <div class="no-data">
            <td>
                <p>No data found</p>
            </td>
            </div>
        <?php endif ?>
        
</body>
</html>