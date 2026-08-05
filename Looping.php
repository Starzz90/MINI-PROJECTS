<!DOCTYPE.html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="looping.css">
    <title>Looping simulation</title>
</head>
<body>
    <div class="divide">
        <div class="card"> 
            <h2>While loop</h2>
            <form method="POST">
                <label>Jumlah Baris: </label>
                <input type="number" class="boxed" name="Quant" min="1" max="100" placeholder="Input jumlah baris" required>
                <button type="submit" name="While" class=>Make it</button>
            </form>
        </div>
        <div class="card"> 
            <h2>Do while loop</h2>
            <form method="POST">
                <label>Jumlah Baris: </baris>
                <input type="number" class="boxed" name="Numb" min="1" max="100" placeholder="Input jumlah baris" required>
                <button type="submit" name="Do-while">Make it</button>
            </form>
        </div>
        <div class="card"> 
            <h2>For Loop</h2>
            <form method="POST">
                <label>Jumlah Baris: </baris>
                <input type="number" class="boxed" name="Bunch" min="1" max="100" placeholder="Input jumlah baris" required>
                <button type="submit" name="For-loop">Make it</button>
            </form>
        </div>
    </div>
    <div class="table">
    <?php
        if(isset($_POST["While"])){
            $Quant = $_POST['Quant'];
            $i = 1;

            echo "<table>";
            echo "<thead><tr><th>No</th><th>Looped</th></tr></thead>";
            echo"<tbody>";

            for ($i = 1; $i <= $Quant; $i++){
                echo "<tr>";
                echo "<td>$i</td>";
                echo "<td>Baris ke-$i</td>";
                echo "</tr>";
            }

            echo "</tbody>";
            echo "</table>";
        }
        if(isset($_POST["Do-while"])){
            $Numb = $_POST['Numb'];
            $i = 1;

            echo "<table>";
            echo "<thead><tr><th>No</th><th>Looped</th></tr></thead>";
            echo"<tbody>";

            do{
                echo "<tr>";
                echo "<td>$i</td>";
                echo "<td>Baris ke-$i</td>";
                echo "</tr>";

                $i++;
            } while ($i <= $Numb);

            echo "</tbody>";
            echo "</table>";
        }
        if(isset($_POST["For-loop"])){
            $Bunch = $_POST['Bunch'];
            $i = 1;

            echo "<table>";
            echo "<thead><tr><th>No</th><th>Looped</th></tr></thead>";
            echo"<tbody>";

            while ($i <= $Bunch){
                echo "<tr>";
                echo "<td>$i</td>";
                echo "<td>Baris ke-$i</td>";
                echo "</tr>";

                $i++;
            }

            echo "</tbody>";
            echo "</table>";
        }
    ?>
    </div>
</body>
</html>