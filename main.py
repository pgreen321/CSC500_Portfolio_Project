from ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart
from datetime import datetime

# Implement main method to output a menu of options to manipulate the shopping cart Build and output the menu within the function.
def print_menu(ShoppingCart):
    user_action = 0
    while user_action != 'q':
        user_action = input("MENU\n"
                            "a - Add item to cart\n"
                            "r - Remove item from cart\n"
                            "c - Change an item's quantity\n"
                            "i - Output items' descriptions\n"
                            "o - Output shopping cart\n"
                            "q - Quit\n"
                            "Choose an option:\n").lower()

        if user_action == "a":
            print('ADD AN ITEM TO CART:')
            try:
                item_to_purchase = ItemToPurchase(str(input('Enter the item name:\n')),
                                                  str(input('Enter the item description:\n')),
                                                  float(input('Enter the item price $:\n')),
                                                  int(input('Enter the item quantity:\n')))
                ShoppingCart.add_item(item_to_purchase)
            except ValueError:
                print('Invalid input. Please try again.')
        elif user_action == "r":
            print('REMOVE AN ITEM FROM CART:')
            item_name = input('Which item to remove?\n')
            ShoppingCart.remove_item(item_name)
        elif user_action == "c":
            print("CHANGE AN ITEM'S QUANTITY:")
            item_name = input('which item to modify?\n')
            shopping_cart.modify_item(item_name)
        elif user_action == "i":
            print()
            print("OUTPUT ITEMS' DESCRIPTIONS:".center(50))
            ShoppingCart.print_descriptions()
            print()
        elif user_action == "o":
            print()
            print('OUTPUT SHOPPING CART'.center(50))
            ShoppingCart.print_total()
            ShoppingCart.get_cost_of_cart()
            print()
        elif user_action == "q":
            break
        else:
            print("Invalid input. Please try again.")


# Implement a method to validate the format of the name input

def is_valid_name(customer_name):
    parts = customer_name.split(' ')
    if len(parts) >= 2:
        return True
    else:
        return False


# Implement a method to validate the format of the date input
def is_valid_date_format(current_date):
    try:
        datetime.strptime(current_date, '%B %d, %Y')
        return True
    except:
        return False


# Ask for Customer Name
customer_name = str(input("Please enter the customer's first and last name:\n"))
valid_name = False
while not valid_name:
    if is_valid_name(customer_name):
        valid_name = True
    else:
        customer_name = str(input("Invalid input: Please enter the customer's first and last name:\n"))

# Ask for Current date and check for valid format
current_date = str(input("Please enter today's date in the following format (month day, year):\n"))
valid_date = False
while not valid_date:
    if is_valid_date_format(current_date):
        valid_date = True
    else:
        current_date = str(input(
            "Invalid date or format entered: Please enter today's date in the following format (month day, year):\n"))

# Output customer name and date
print()
print('Customer name: {}:'.format(customer_name).center(50))
print("Today's date: {}".format(current_date).center(50))
print()

# Create a shopping cart by executing Shopping Cart Class
shopping_cart = ShoppingCart(customer_name, current_date)

# # Present user with menu to add, remove, edit and print items
print_menu(shopping_cart)
