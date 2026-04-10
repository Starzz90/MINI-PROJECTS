<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="ORDER.css">
    <title>Checkout Order</title>
</head>
<body>
<?php
    $quantity_espresso = (int) $_POST["quantity_espresso"];
    $quantity_latte = (int) $_POST["quantity_latte"];
    $quantity_cappuccino = (int) $_POST["quantity_cappuccino"];
    $quantity_americano = (int) $_POST["quantity_americano"];
    $quantity_mocha = (int) $_POST["quantity_mocha"];

    $total_price = ($quantity_espresso * 20000) + ($quantity_latte * 25000) + ($quantity_cappuccino * 30000) + ($quantity_americano * 15000) + ($quantity_mocha * 35000);
    $customer_name = $_POST["customer_name"];
    $change = (float) $_POST["Money"] - $total_price;
?>
    <div class="container">
        <div class="coffee">
            <h2>CHECKOUT</h2>
                    <form action="CHECHKOUT.php" method="POST">
                        <h4>Order Summary</h4>
                            <div class="menu"><li><span class="left">Espresso: </span><span class="right"><?php echo $quantity_espresso; ?></span></div></li>
                            <div class="menu"><li><span class="left">Latte: </span><span class="right"><?php echo $quantity_latte; ?></span></div></li>
                            <div class="menu"><li><span class="left">Cappuccino: </span><span class="right"><?php echo $quantity_cappuccino; ?></span></div></li>
                            <div class="menu"><li><span class="left">Americano: </span><span class="right"><?php echo $quantity_americano; ?></span></div></li>
                            <div class="menu"><li><span class="left">Mocha: </span><span class="right"><?php echo $quantity_mocha; ?></span></div></li>

                        <div class="menu"><span class="left">Customer Name</span><span class="right"><?php echo $customer_name; ?></span></div>
                        <div class="menu"><span class="left">Total Price</span><span class="right"><?php echo $total_price; ?></span></div>
                        <div class="menu"><span class="left">Change</span><span class="right"><?php echo $change; ?></span></div>
                    </form>
        </div>
    </div>
</body>
</html>