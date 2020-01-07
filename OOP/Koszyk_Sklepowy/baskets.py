# from collections import namedtuple
# Item = namedtuple("Item", ["product", "quantity"])

class Item:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def generate_report(self):
        return f"- {self.product.name} ({self.product.id}), cena: {self.product.price} x {self.quantity}\n"

    def count_price(self):
        return self.product.price * self.quantity

class Basket:

    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        item = Item(product=product, quantity=quantity)
        self.items.append(item)

    def count_total_price(self):
        price = 0
        for item in self.items:
            price += item.count_price()
        return price

    def generate_report(self):
        output = "Produkty w koszyku:\n"
        for item in self.items:
            output += item.generate_report()
        output += f"W sumie: {self.count_total_price()}"
        return output