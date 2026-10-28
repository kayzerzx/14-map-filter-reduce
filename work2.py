products = [
    {"name": "keyboard", "price": 45},
    {"name": "monitor", "price": 180},
    {"name": "mouse", "price": 25},
    {"name": "headphones", "price": 75},
    {"name": "usb drive", "price": 15},
    {"name": "webcam", "price": 60}   
]

products_under_50 = list(filter(lambda products: products["price"] <= 50, products))
products_above_50 = list(filter(lambda products: products["price"] > 50, products))
print(products_under_50)
print(products_above_50)