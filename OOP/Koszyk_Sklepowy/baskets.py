from collections import namedtuple

Item = namedtuple("Item", ["product", "quantity"])

Class Item:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class Basket:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):

        item = Item(product=product, quantity=quantity)
        self.items.append(item)

    def count_total_price(self):
        total_price = 0
        for entry in self.items:
            total_price += entry.count_price()

        return total_price

    def generate_report(self):
        report = "Produkty w koszyku:\n"
        for entry in self.items:
            report += entry.generate_report()
        report += f"W sumie: {self.count_total_price():}"
        return report

    #
    # def with_products(products_list):
    #     basket = Basket()
    #     for product in products_list:
    #         basket.add_product(product, 1)
    #     return basket

