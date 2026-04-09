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
    
    $total_harga = $jumlah * $harga;
    $kembalian = $bayar - $total_harga;
    ?>
    <div class="container">
    <div class="input-group">
            <h1>Profile Form</h1>
            <div class="bold">Name</div><span class="right"><?php echo $user; ?></span>
            <div class="bold">Item</div><span class="right"><?php echo $item; ?></span>
            <div class="bold">Jumlah</div><span class="right"><?php echo $jumlah; ?></span>
            <div class="bold">Bayar</div><span class="right"><?php echo $bayar; ?></span>
    
        </div>
    </div>
    <div class="container">
        <div class="input-group">
            <h1>Payment Result</h1>
            <div class="bold">Total Harga</div><span class="right"><?php echo $total_harga; ?></span>
            <div class="bold">Kembalian</div><span class="right"><?php echo $kembalian; ?></span>
        </div>
    </div>
</body>
</html>