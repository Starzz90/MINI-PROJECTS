<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cashier Page</title>
    <link rel="stylesheet" href="cash.css">
</head>
<body>
    <div class="container">
        <h1>Cashier Page</h1>
        <div class="inputs">
        <form action="CO.php" method="POST">
            <label for="user">Username: </label>
            <input class="inputbox" type="text" id="user" name="user"><br><br>
            <label for="item">Item: </label>
            <select class="inputbox" id="item" name="item">
                <option value="Nasgor">Nasi Goreng -- Rp.15.000</option></br>
                <option value="Miegor">Mie Goreng -- Rp.12.000</option></br>
                <option value="Sate">Sate Ayam -- Rp.20.000</option></br>
                <option value="Perkedel">Perkedel -- Rp.7.000</option></br>
                <option value="EsTeh">Es Teh -- Rp.5.000</option></br>
            </select>
            <br><br>
            <label for="jumlah">Jumlah: </label>
            <input class="inputbox" type="number" id="jumlah" name="jumlah" min="1" max="100"><br><br>
            <label for="bayar">Bayar: </label>
            <input class="inputbox" type="text" id="bayar" name="bayar" placeholder="Rp."><br><br>
            <button class="button" type="submit">Submit Order</button>
        </form>
        </div>
    </div>
</body>
</html>