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
    def __init__(self):
    # Creates a dictionary of coupons for each shopper
        self.coupons = {}
    
    def generate_coupon(self):
    # method that will generate a random discount (int between 5, 20)
    # and choose a random product and print the resulting information
        discount = random.randint(5, 20)
        product = random.choice(Product.products)
        self.coupons[product.get_name()] = discount
        print(f"{Shopper} has a coupon for {discount}% off {product}")
    
    def get_coupons(self):
    # method that returns the shoppers dictionary of coupons
        return self.coupons
    
    def get_discount(self, product_name):
    # method that gets the discount of a specific product
        return self.coupons.get(product_name)
        # might add error message "no coupon" if product not found
    
    def set_discount(self, product_name, new_discount):
    # method that sets new discount for a specific product if needed
    # or allows for manually created coupon
        self.coupons[product_name] = new_discount
        
    def get_product(self, product_name):
    # method that loops through Products and checks if the Shopper has
    # a discount for that product
        for product in Product.products:
            if product.get_name() == product_name:
                return product
        return None
    
    