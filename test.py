import random

class Grocery:
    pass    
    
class Shopper: 
    pass

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def set_price(self, new_price):
        self.price = new_price

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity


class Coupon:
# class that createa a dictionary for each new shopper, 
# and adds a randomly generated coupon from the products class
    def __init__(self, shopper):
    # Creates a dictionary of coupons for each shopper
        self.coupons = {}
    
    def generate_coupon(self):
    # method that will generate a random discount (int between 5, 20)
    # and choose a random product and print the resulting information
        discount = random.randint(5, 20)
        product = random.choice(Product.products)
        self.coupons[product.get_name()] = discount
        print(f"{Shopper} has a coupon for {discount}% off {product}")
    
