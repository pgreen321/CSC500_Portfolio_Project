# In the main section of your code, prompt the user for two items to create two objects of the ItemToPurchase class

from ItemToPurchase import ItemToPurchase


item_1 = ItemToPurchase(str(input('Enter the item name:\n')),
                       float(input('Enter the item price:\n')),
                       int(input('Enter the item quantity:\n')))
item_2 = ItemToPurchase(str(input('Enter the item name:\n')),
                       float(input('Enter the item price:\n')),
                       int(input('Enter the item quantity:\n')))

# Add the costs of the two items together and output the total cost

total_cost = item_1.item_cost + item_2.item_cost

print()
print('TOTAL COST')
item_1.print_item_cost()
item_2.print_item_cost()
print('Total: ${:.2f}'.format(total_cost))
