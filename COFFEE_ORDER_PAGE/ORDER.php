<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="ORDER.css">
    <title>Coffee Order</title>
</head>
<body>
    <div class="container">
        <div class="coffee">
            <h2>Menu</h2>
            <form action="CHECHKOUT.php" method="POST">
                <div class="menu"><span class="left"><p>Espresso ---- 20000</p></span><span class="right"><input class="quant" type="number" name="quantity_espresso" min="1" max="1000"></span></div>
                <div class="menu"><span class="left"><p>Latte ---- 25000</p></span><span class="right"><input class="quant" type="number" name="quantity_latte" min="1" max="1000"></span></div>
                <div class="menu"><span class="left"><p>Cappuccino ---- 30000</p></span><span class="right"><input class="quant" type="number" name="quantity_cappuccino" min="1" max="1000"></span></div>
                <div class="menu"><span class="left"><p>Americano ---- 15000</p></span><span class="right"><input class="quant" type="number" name="quantity_americano" min="1" max="1000"></span></div>
                <div class="menu"><span class="left"><p>Mocha ---- 35000</p></span><span class="right"><input class="quant" type="number" name ="quantity_mocha" min="1" max="1000"></span></div>
                
                <input id="name" type="text" name="customer_name" placeholder="Your Name" class="coffee-input">
                <input id="money" type="text" name="Money" placeholder="Amount Paid" class="coffee-input"></br>
                <input type="submit" value="Order" class="button">
            </form>
        </div>
    </div>
</body>
</html>