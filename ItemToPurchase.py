# create a class
class ItemToPurchase:
    def __init__(self, item_name='none', item_description='none', item_price=0.0, item_quantity=0):
        self.item_name = str(item_name)
        self.item_description = str(item_description)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

    def calculate_cost(self):
        item_cost = self.item_price * self.item_quantity
        return item_cost

    # method to display item cost
    def print_item_cost(self):
        return '{}: {} @ ${:.2f} = ${:.2f}'.format(self.item_name, self.item_quantity, self.item_price, self.calculate_cost())

