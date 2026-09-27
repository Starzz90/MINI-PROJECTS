price: float = 0
discount: float = 0
def apply_discount(price: float, discount: float):
    if price <= 0:
        print('The price should be greater than 0')
    elif 100 < discount <= 0:
        print('The discount should be between 0 and 100')
    else:
        total_price = round(price * (discount/100), 2)
        print(f'Your total price: {total_price}')

while True:
    try:
        price = float(input('Enter your price: '))
        discount = float(input('Enter your discount: '))
        apply_discount(price, discount)
    except ValueError:
        print('The price or discount should be a number')




