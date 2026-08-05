<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample HTML Page</title>
    <link rel="stylesheet" href="cash.css">
</head>
<body>
    <?php
    $user = $_POST["user"];
    $item = $_POST["item"];
    $jumlah = (int) $_POST["jumlah"];
    $bayar = (float) $_POST["bayar"];
    
    if($item == "Nasgor"){
        $item = "Nasi Goreng";
        $harga = 15000;
    }elseif($item == "Miegor"){
        $item = "Mie Goreng";
        $harga = 12000;
    }elseif($item == "Sate"){
        $item = "Sata Ayam";
        $harga = 20000;
    }elseif($item == "Perkedel"){
        $item = "Perkedel";
        $harga = 7000;
    }elseif($item == "EsTeh"){
        $item = "Es Teh";
        $harga = 5000;
    }else{
        $item = "Item tidak ditemukan";
        $harga = 0;
    }
    $total_harga = $jumlah * $harga;
    $kembalian = $bayar - $total_harga;
    ?>
    <div class="container">
        <div class="result-box">
            <h1>Profile Form</h1>
            <div class="results"><div class="bold">Name</div><span class="right"><?php echo $user; ?></span></div>
            <div class="results"><div class="bold">Item</div><span class="right"><?php echo $item; ?></span></div>
            <div class="results"><div class="bold">Jumlah</div><span class="right"><?php echo $jumlah; ?></span></div>
            <div class="results"><div class="bold">Bayar</div><span class="right"><?php echo $bayar; ?></span></div>
        </div>
    </div>
    <div class="container">
        <div class="result-box">
            <h1>Payment Result</h1>
            <div class="results"><div class="bold">Total Harga</div><span class="right"><?php echo $total_harga; ?></span></div>
            <div class="results"><div class="bold">Kembalian</div><span class="right"><?php echo $kembalian; ?></span></div>
        </div>
    </div>
</body>
</html>