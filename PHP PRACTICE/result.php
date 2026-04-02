<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample HTML Page</title>
    <link rel="stylesheet" href="second.css">
    
    <?php
            $name = $_POST['name'];
            $age = (int) $_POST['age'];
            $GPA = (float) $_POST['GPA'];
            $country = $_POST['country'];
            
    ?>
</head>
<body>
    <div class="container">
    <div class="input-group">
        <form action="result.php" method="FORM">
            <h1>Profile Result</h1>
            <span class="form-label"><label>Name</label></span><p><?php echo $name; ?></p>
            <span class="form-label"><label>Age</label></span><p><?php echo $age; ?></p>
            <span class="form-label"><label>GPA</label></span><p><?php echo $GPA; ?></p>
            <span class="form-label"><label>Country</label></span><p><?php echo $country; ?></p>
        </form>
        </div>
    </div>
</body>
</html>
