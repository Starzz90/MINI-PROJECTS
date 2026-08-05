<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample HTML Page</title>
    <link rel="stylesheet" href="second.css">
    
</head>
<body>
    <?php
        $name = $_POST["name"];
        $age = (int) $_POST["age"];
        $GPA = (float) $_POST["GPA"];
        $country = $_POST["Country"];  
    ?>

    <div class="container">
    <div class="input-group">
        <form action="result.php" method="POST">
            <h1>Profile Result</h1>
            <label>Name</label><span class="input-label"><?php echo $name; ?></span></br>
            <label>Age</label><span class="input-label"><?php echo $age; ?></span></br>
            <label>GPA</label><span class="input-label"><?php echo $GPA; ?></span></br>
            <label>Country</label><span class="input-label"><?php echo $country; ?></span></br>
        </form>
        </div>
    </div>
</body>
</html>

