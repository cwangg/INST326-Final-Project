import sys
import re
import random
import pandas as pd
import matplotlib.pyplot as plt

class Product:
    """
    A class that represents a product in a grocery store.

    Attributes:
    - name (str): the name of the product
    - category (str): the category of the product
    - price (float): the price of the product
    - quantity (int): the quantity of the product in the store

    Methods:
    - __init__(self, name, price, quantity): Initializes a product with its name, category, quantity, and price.
    - get_name(self): Returns the name of the product.
    - get_category(self): Returns the category of the product.
    - get_quantity(self): Returns the quantity of the product in the store.
    - get_price(self): Returns the price of the product.
    - __repr__(self): Returns the formal representation of a product
    """

    def __init__(self, name, category, quantity, price):
        if not re.match(r'^[a-zA-Z0-9_\- ]+$', name):
            raise ValueError('Name can only contain letters, numbers, underscores, dashes and spaces.')
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        
    def get_name(self):
        return self.name
    
    def get_category(self):
        return self.category
    
    def get_quantity(self):
        return self.quantity
    
    def get_price(self):
        return self.price
    
    def __repr__(self):
        return f'(Item: {self.name}, Category: {self.category}, Quantity = {self.quantity}, Price = ${self.price})'
    
    
class GroceryStore:
    """
    A class that represents a grocery store.

    Attributes:
    - name (str): the name of the grocery store
    - inventory (dict): a dictionary of product names and their quantities in the store

    Methods:
    - __init__(self, name, inventory): Initializes a grocery store with the name of it and populates the 
        inventory of the grocery store with products and their quantities 
        from a file named "grocery store inventory.csv". 
    - get_inventory(self): returns the inventory of the grocery store
    """
    def __init__(self, name = "", inventory = "grocery store inventory.csv"):
        """Intializes a grocery store and creates its inventory from a csv file.
        
        Args:
            name (str): the name of the grocery store
            inventory (csv): a file containing the product name, category, quantity, price
            
        Side effects:
            Sets attributes
        """
        self.name = name
        self.inventory = dict()
        with open(inventory, "r", encoding="utf-8") as f:
            next(f)
            for line in f:
                item, category, quantity, price = line.strip().split(',')
                self.inventory[item] = Product(item, category, int(quantity), int(price))

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
        """Intializes a shopper with their name, cart, budget, and coupon
        
        Args:
            name (str): the name of the shopper
            budget (int): the shoppers budget
        
        Attributes:
            name (str): the name of the shopper
            cart(dict): dictionary to hold the shoppers list of products
            budget (int): the shoppers budget
            coupon (Coupon): whether the shopper has a coupon

        Side effects:
            Sets attributes
        """
        self.name = name
        self.cart = {}
        self.budget = budget
        self.coupon = None

    def add(self, product_name, quantity, store):
        """ This function adds a specified amount/product to the shoppers cart as long as the item 
            is in stock and the shopper does not go over their specified budget. 
        
        Args:
            product_name (str): the name of the product
            quantity (int): the quantity of the product they want to add
            store (str): the grocery store and its inventory

        Side effects:
            Adds specified product(s) to the shopper's cart attribute
        """
        if product_name not in store.inventory:
            print(f"Sorry! We dont have {product_name}")
            return
        product = store.inventory[product_name]
        total_price = product.price * quantity
        if total_price + sum([store.inventory[p].price * self.cart[p] for p in self.cart]) > self.budget:
            print(f"Item cost to much, put it back!")
            return
        if product_name in self.cart:
            self.cart[product_name] += quantity
        else:
            self.cart[product_name] = quantity
        df.loc[product_name, "Quantity"] = (store.inventory[product_name].get_quantity() - quantity)
        print(f"{quantity} {product_name} added to your cart.")
    
    def generate_coupon(self):
        """ This function will generate a random discount between 5% and 20% 
            and apply it to the total cost of the cart

        Side effects:
            Creates a coupon object using the randomg discount
            
        Returns:
            the coupon object
        """
        discount = random.randint(5, 20)
        coupon = Coupon(discount)
        self.coupon = coupon
        print(f"You received a {discount}% discount on your cart.")

        return coupon

    
    def checkout(self, store):
        total_price = 0
        for product_name, quantity in self.cart.items():
            product = store.inventory[product_name]
            total_price += product.price * quantity
        if self.coupon:
            total_price = self.coupon.apply(total_price)
        print(f"Your total price comes to: ${round(total_price, 2)}")
        return total_price



class Coupon:
    """
    A class that represents a coupon with a discount and product name and gives the formal representation

    Attributes:
    - discount (int): the randomly generated discount for the coupon
    - product_name (str): the name of the product the coupon is for

    Methods:
    - __init__(self): Initializes the discount and product name of the coupon
    - get_discount(self): Returns the discount of the coupon
    - __repr__(self): formal representation of a coupon
    
    """
    def __init__(self, discount, product_name): 
        """Intializes a coupon with its discount and product name. 
        
        Args:
            discount (int): randomly generated int
            product_name (str): randomly selected product from the shopper's cart
            
        Side effects:
            Sets attributes
        """
        self.discount = discount
        self.product_name = product_name
    
    def __init__(self, discount): 
        self.discount = discount
    
    def apply(self, total_price):
        return total_price * (1 - (self.discount/100))
    
    def __repr__(self):
        return f'Coupon: {self.discount}% off'



if __name__ == '__main__':
    store_name = input("Welcome! What grocery store would you like to shop at today? ")
    store = GroceryStore(store_name,)
    
    shopper_name = input(f"Thanks for choosing {store_name}! What's your name? ")
    budget = float(input(f"{shopper_name}, What's your budget for today? $"))

    shopper = Shopper(shopper_name, budget)
    df = pd.read_csv("grocery store inventory.csv", index_col="Item")
    
    while True:
        choice = input("Would you like to add an item to your cart, checkout, or leave? ").lower()
        if choice == "add":
            print(df)
            item_name = input("What would you like to add to your cart? ")
            quantity = int(input(f"How many {item_name} would you like to add to your cart? "))
            shopper.add(item_name, quantity, store)
        elif choice == "checkout":
            if not shopper.cart:
                print("Your cart is empty!")
                continue
            shopper.coupon = shopper.generate_coupon()
            coupon_choice = input("Would you like to use a coupon? ").lower()
            if coupon_choice == "yes":
                shopper.checkout(store)
                print("Have a nice day!")

                break
            elif coupon_choice == "no":
                print("Ok! Keep Shopping!")
        elif choice == "leave":
            print ("Come back again!")
            break
    
   # Show a bar graph of the previous inventory
dfbefore = pd.read_csv("before inventory.csv")
name = dfbefore['Item']
quantity = dfbefore['Quantity']
# Figure Size
plt.bar(quantity, name, color="red")
plt.xlabel("Quantity")
plt.ylabel("Food Items")
plt.title("Previous Store Inventory")
plt.show()

# Show a bar graph of the current inventory
df = df.reset_index()
name = df['Item']
quantity = df['Quantity']
# Figure Size
plt.bar(quantity, name)
plt.xlabel("Quantity")
plt.ylabel("Food Items")
plt.title("Current Store Inventory")
plt.show()
