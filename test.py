import random

class GroceryStore:
    """
    A class that represents a grocery store.

    Attributes:
    - name (str): the name of the grocery store
    - inventory (dict): a dictionary of product names and their quantities in the store

    Methods:
    - __init__(self, name, inventory): Initializes a grocery store with the name of it and its inventory.
    - setup_store(self, stock): Populates the inventory of the grocery store with products and their quantities 
                                from a file named "stock". 
    """
    def __init__(self, name, inventory):
        # Intitialize a grocery store with the name of it and its inventory.
        self.name = name
        self.inventory = dict()
    
    def setup_store(self, stock):
        # Stock will be a file containing the name of an item and it's quantity
        with open(stock, "r", encoding="utf-8") as f:
            for line in f:
                for item, quantity in line.strip().split():
                    self.inventory[item] = quantity

class Product:
    """
    A class that represents a product in a grocery store.

    Attributes:
    - name (str): the name of the product
    - price (float): the price of the product
    - quantity (int): the quantity of the product in the store

    Methods:
    - __init__(self, name, price, quantity): Initializes a product with its name, price, and quantity.
    - get_name(self): Returns the name of the product.
    - get_price(self): Returns the price of the product.
    - get_quantity(self): Returns the quantity of the product in the store.
    - set_price(self, new_price): Sets a new price for the product.
    - set_quantity(self, new_quantity): Sets a new quantity for the product in the store.
    """
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

class Coupon():
    """
    A class that represents a coupon for a shopper.

    Attributes:
    - coupons (dict): a dictionary of product names and their discounts for a shopper

    Methods:
    - __init__(self): Initializes a dictionary of coupons for each shopper.
    - generate_coupon(self): Generates a random discount (integer between 5 and 20) 
                             for a random product and adds it to the shopper's coupons dictionary.
    - get_coupons(self): Returns the shopper's coupons dictionary.
    - get_discount(self, product_name): Returns the discount for a specific product in the shopper's coupons.
    - set_discount(self, product_name, new_discount): Sets a new discount for a specific product in the shopper's coupons.
    - get_product(self, product_name): Loops through Products and checks if the Shopper has a discount for that product.
    - set_product(self, product_name, new_product): Switches the product on a coupon to a different product.
    """
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
    
    def set_product(self, product_name, new_product):
    # method that switches the product on a coupon to a different product
        self.coupons.pop(product_name, None)
        # removing old product and adding new product with its name as key
        self.coupons[new_product.get_name()] = self.get_discount(product_name)

class Shopper: 
    """
    A class that represents a shopper.

    Attributes:
    - cart (list): a list of items in the shopper's cart
    - budget (float): the amount of money the shopper has to spend
    - store_prices (dict): a dictionary of product names and their prices in the grocery store

    Methods:
    - __init__(self, budget, store_prices): Initializes a shopper with a budget and the prices of products 
                                             in the grocery store.
    - add(self, item, price, inventory): Adds an item to the shopper's cart if it is available in the inventory 
                                         and the shopper's budget is sufficient to buy it.
    - checkout(self): Calculates the total cost of items in the shopper's cart and returns it. 
                      The cart is then cleared.
    """
    def init(self, budget, store_prices):
        self.cart = []
        self.budget = budget
        self.store_prices = store_prices

    def add(self, item, price, inventory):
        if item in inventory and price <= self.budget:
            self.cart.append(item)
            self.budget -= price
            return True
        else:
            print(f"Item cost to much, put it back!")

    def checkout(self):
        total = 0
        for item in self.cart:
            total += self.store_prices[item]
        self.cart = []
        return total
    
    