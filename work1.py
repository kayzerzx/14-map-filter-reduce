prices = [25.00, 50.00, 75.00, 100.00, 150.00]

def p_to_d(price):
    return f"{price * 0.2:.2f}" 

discount = map(lambda price: round(price * 0.8, 2), prices)
print(f"original price: {list(prices)}")
print(f"New Prices: {list(discount)}")