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
            <form action="CHECKOUT.php" method="POST">
                <div class="menu"><span class="left"><p value="espresso">Espresso</p></span><span class="right"><input class="quant" type="number" name="quantity_espresso" min="1" max="1000"></span></div>
                <div class="menu"><span class="left"><p value="latte">Latte</p></span><span class="right"><input class="quant" type="number" name="quantity_latte" min="1" max="1000"></span></div>
                <div class="menu"><span class="left"><p value="cappuccino">Cappuccino</p></span><span class="right"><input class="quant" type="number" name="quantity_cappuccino" min="1" max="1000"></span></div>
                <div class="menu"><span class="left"><p value="americano">Americano</p></span><span class="right"><input class="quant" type="number" name="quantity_americano" min="1" max="1000"></span></div>
                <div class="menu"><span class="left"><p value="mocha">Mocha</p></span><span class="right"><input class="quant" type="number" name ="quantity_mocha" min="1" max="1000"></span></div>
                
                <input type="text" name="customer_name" placeholder="Your Name" class="coffee-input">
                <input type="text" name="Money" placeholder="Amount Paid" class="coffee-input"></br>
                <input type="submit" value="Order" class="button">
            </form>
        </div>
    </div>
    <script src="ORDER.js"></script>
</body>
</html>