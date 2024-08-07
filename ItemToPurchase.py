# create a class
class ItemToPurchase:
   def __init__(self, item_name='none', item_price=0.0, item_quantity=0):
       self.item_name = str(item_name)
       self.item_price = float(item_price)
       self.item_quantity = int(item_quantity)
       self.item_cost = float(item_price * item_quantity)


   # method to display item cost
   def print_item_cost(self):
       print('{}: {} @ ${:.2f} = ${:.2f}'.format(self.item_name, self.item_quantity,
                                                 self.item_price, self.item_cost))
