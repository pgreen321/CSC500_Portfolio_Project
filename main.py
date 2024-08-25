from ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart

# Implement main method to output a menu of options to manipulate the shopping cart Build and output the menu within the function.
def print_menu(ShoppingCart):
    user_action = 0
    while user_action != 'q':
        user_action = input("MENU\n"
                            "a - Add item to cart\n"
                            "r - Remove item from cart\n"
                            "c - Change item quantity\n"
                            "i - Output items' descriptions\n"
                            "o - Output shopping cart\n"
                            "q - Quit\n"
                            "Choose an option:\n")

        if user_action == "a":
            item_to_purchase = ItemToPurchase(str(input('Enter the item name:\n')),
                                              str(input('Enter the item description:\n')),
                                              float(input('Enter the item price:\n')),
                                              int(input('Enter the item quantity:\n')))
            ShoppingCart.add_item(item_to_purchase)
        if user_action == "r":
            item_name = input('which item to remove?\n')
            ShoppingCart.remove_item(item_name)
        if user_action == "c":
            item_name = input('which item to modify?\n')
            shopping_cart.modify_item(item_name)
        if user_action == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS:")
            ShoppingCart.print_descriptions()
        if user_action == "o":
            print('OUTPUT SHOPPING CART')
            ShoppingCart.print_total()
            ShoppingCart.get_cost_of_cart()


shopping_cart = ShoppingCart()
print_menu(shopping_cart)
