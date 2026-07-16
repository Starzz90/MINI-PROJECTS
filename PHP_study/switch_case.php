<!DOCTYPE.html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="ORDER.css">
    <title>Data Filing</title>
</head>
<body>
    <div class="container">
        <div class="box">
            <input type="text" name="user" id="name" placeholder="Please input your name">
            <form method="POST">
                <select class="input" id="role" name="role">
                    <option value="guest">Guest</option> 
                    <option value="Developer">Developer</option> 
                    <option value="Manager">Manager</option> 
                    <option value="Admin">Admin</option> 
                </select>
                <button class="button" name="submit" id="submit">Submit</button>
            </form>

        </div>
        <div class="box">
            <?php
                if((isset($_POST['submit']))){
                    $role = $_POST['role'];

                    echo"<div class='result'>";
                    switch($role){
                        case "guest":
                            echo "Kamu tidak akan bisa mengubah data di dalam website ini<br>";
                            echo "Kamu memasuki situs sebagai . $role <br>";
                            break;
                        case "Developer":
                            echo "Kamu dapat mengubah data dalam website ini</br>";
                            echo "Kamu memasuki situs sebagai . $role  <br>";
                            break;
                        case "Manager":
                            echo "Kamu dapat mengatur, melihat, dan mengubah database ini</br>";
                            echo "Kamu memasuki situs sebagai . $role . <br>";
                            break;
                        case "Admin":
                            echo "Kamu dapat mengatur, melihat, dan mengambil database ini</br>";
                            echo "Kamu memasuki situs sebagai . $role . <br>";
                            break;

                    }
                    echo "</div>";

                }
            ?>

        </div>
    </div>
</body>
</html>