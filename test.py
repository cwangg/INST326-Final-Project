import sys
import random
import pandas as pd

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
    def __init__(self, name, category, quantity, price):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        

    def get_category(self):
        return self.category

    def get_name(self):
        return self.name
    
    def __repr__(self):
        return f'Item: {self.name}, Category: {self.category}, Quantity = {self.quantity}), Price = ${self.price}'
    
    
class GroceryStore:
    """
    A class that represents a grocery store. Uses with statement and sequence
    unpacking.

    Attributes:
    - name (str): the name of the grocery store
    - inventory (dict): a dictionary of product names and their quantities in the store

    Methods:
    - __init__(self, name, inventory): Initializes a grocery store with the name of it and its inventory.
    - setup_store(self, stock): Populates the inventory of the grocery store with products and their quantities 
                                from a file named "stock". 
    """
    def __init__(self, name = "", inventory = "grocery store inventory.csv"):
        # Intitialize a grocery store with the name of it and its inventory.
        self.name = name
        self.inventory = {}
        with open(inventory, "r", encoding="utf-8") as f:
            for line in f:
                item, category, quantity, price = line.strip().split(',')
                self.inventory[item] = Product(item, category, quantity, price)

    def get_inventory(self):
        return self.inventory
    
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
    def __init__(self, name, budget):
        self.name = name
        self.cart = {}
        self.budget = budget
        self.coupon = None

    def add(self, product_name, quantity):
        if product_name not in GroceryStore().inventory.fromkeys(product_name):
            print(f"Sorry! We dont have {product_name}")
            return
        product = GroceryStore().inventory[product_name]
        total_price = product.price * quantity
        if total_price > self.budget:
            print(f"Item cost to much, put it back!")
            return
        if product_name in self.cart:
            self.cart[product_name] += quantity
        else:
            self.cart[product_name] = quantity
        print(f"{quantity} {product_name}s added to your cart.")

    def checkout(self):
        total_price = 0
        for product_name, quantity in self.cart.items():
            product = GroceryStore.inventory[product_name]
            total_price += product.price * quantity
        if self.coupon is not None and self.coupon.product_name in self.cart:
            discount = self.coupon.discount
            product_name = self.coupon.product_name
            print(f"You have a {discount}% discount on {product_name}!")
            total_price *= (1 - discount/100)
        print(f"Total price: ${total_price}")
        return total_price
    #If at checkout the price is greater than the shopper's budget, remove the most expensive item from the person's cart. Keep doing that until
    #total price is < the shopper's budget.

class Coupon:
    """
    A class that represents a coupon for a shopper. Ues conditional expression and set operations.

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
    def __init__(self, product_name, discount):
        self.discount = discount
        self.product_name = product_name
    
    def generate_coupon(self, inventory):
    # method that will generate a random discount (int between 5, 20)
    # and choose a random product and print the resulting information
        product_name, product = random.choice(list(inventory.items()))
        discount = random.randint(5, 20)
        coupon = self(product_name, discount)
        return coupon
    
    def check_coupons(self, shopper):
        if shopper.coupon is not None:
            print(f"You have a coupon for {shopper.coupon.product_name}!")
        else:
            coupon = self.generate_coupon(GroceryStore.inventory)
            shopper.coupon = coupon
            print(f"You received a {coupon.discount}% discount coupon for {coupon.product_name}!")

if __name__ == '__main__':
    store_name = input("Welcome! What grocery store would you like to shop at today? ")
    store = GroceryStore(store_name,)
    
    shopper_name = input(f"Thanks for choosing {store_name}! What's your name? ")
    budget = float(input(f"{shopper_name}, What's your budget for today? $"))

    shopper = Shopper(shopper_name, budget, store_name)
    
    while True:
        choice = input("Would you like to add an item to your cart, checkout, or quit? ").lower()
        if choice == "add":
            item_name = input("What would you like to add to your cart? ")
            quantity = int(input(f"How many {item_name} would you like to add to your cart? "))
            shopper.add(item_name, quantity)
        elif choice == "checkout":
            if not shopper.cart:
                print("Your cart is empty!")
                continue
            Coupon().check_coupons(shopper)
            coupon_choice = input("Would you like to use a coupon? ").lower()
            if coupon_choice == "yes":
                shopper.checkout()
            print("You spent $")
        elif choice == "quit":
            print ("Come back again!")
            break