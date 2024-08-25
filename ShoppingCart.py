# Create a ShoppingCart class
class ShoppingCart:
    def __init__(self, customer_name='none', current_date='none'):
        self.customer_name = str(customer_name)
        self.current_date = str(current_date)
        self.cart_items = []

    # Method to add item. Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    # Method to remove item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
    # If item name cannot be found, output this message: Item not found in cart. Nothing removed.
    def remove_item(self, item_name):
        item_in_cart = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_in_cart = True
        if not item_in_cart:
            print('Item not found in cart. Nothing Removed')

    # Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
    # If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity.
    # If not, modify item in cart.
    # If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
    def modify_item(self, item_name ):
        item_in_cart = False
        for item in self.cart_items:
            if item.item_name == item_name:
                item.item_quantity = int(input("Enter updated item quantity: "))
                item_in_cart = True
        if not item_in_cart:
            print('Item not found in cart. Nothing modified')

    # Method to return quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items += item.item_quantity
        return total_items

    # Method to determine and return the total cost of items in the cart. Has no parameters.
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            item_cost = item.calculate_cost()
            total_cost += item_cost
        return total_cost

    # Method to output total of objects in cart. If cart is empty, output the message "shopping cart is empty"
    def print_total(self):
        if len(self.cart_items) > 0:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print('Number of items: {}'.format(self.get_num_items_in_cart()))
            for item in self.cart_items:
                print(item.print_item_cost())
            print('Total: ${:.2f}'.format(self.get_cost_of_cart()))
        else:
            print('SHOPPING CART IS EMPTY')

    # Method to output each item's description
    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print('Item Descriptions')
        for item in self.cart_items:
            print('{}: {}'.format(item.item_name, item.item_description))
