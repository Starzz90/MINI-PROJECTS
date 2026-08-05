<!DOCTYPE.html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="ORDER.css">
    <title>VS Computer</title>
</head>
<body>
    <div class="container">
        <div class="box">
            <form method="POST">
                <h2>Player</h2>
                <select class="input" id="player" name="player">
                    <option value="Gunting">Gunting</option> 
                    <option value="Batu">Batu</option> 
                    <option value="Kertas">Kertas</option> 
                </select>
                <button class="button" name="submit" id="submit">Play</button>
            </form>

        </div>
        <div class="box">
            <?php
                if(isset($_POST['submit'])){
                    $player = $_POST['player'];
                    $ran = rand(1, 3);
                    $komputer = "";

                    switch($ran){
                        case "1":
                            $komputer = "Gunting";
                            break;
                        case "2":
                            $komputer = "Batu";
                            break;
                        case "3":
                            $komputer = "Kertas";
                            break;
                    }

                    // echo"< class='result'>";
                    if($player == $komputer){
                        echo "Pertandingan seri";
                    }else{
                        switch($player){
                            case "Gunting":
                                if ($komputer == "Kertas"){
                                    echo "Kamu menang";
                                }else{
                                    echo "Kamu kalah";
                                }
                                break;
                            case "Batu":
                                if ($komputer == "Gunting"){
                                    echo "kamu menang";
                                } else {
                                    echo "kamu kalah";
                                }
                                break;
                            case "Kertas":
                                if ($komputer == "Batu"){
                                    echo "Kamu menang";
                                } else {
                                    echo "Kamu kalah";
                                }
                                break;
                        }
                    }
                    echo " Pemain:" .ucfirst($player). " VS Komputer:" .ucfirst($komputer);  
                }

            ?>

        </div>
    </div>
</body>
</html>