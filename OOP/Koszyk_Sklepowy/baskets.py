from collections import namedtuple

class BasketEntry:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.price * self.quantity

    def generate_report(self):
        return f" - {self.product.name} ({self.product.id}), price: {self.product.price:.2f} x {self.quantity}\n"


class Basket:
    def __init__(self):
        self.entries = []
        self.discounts = []

    def add_product(self, product, quantity: int):
        """add basket entry to basket"""

        self.entries.append(BasketEntry(product, quantity))

    def add_discount(self, discount):
        self.discounts.append(discount)

    def count_total_price(self):
        total_price = 0
        for entry in self.entries:
            total_price += entry.count_price()

        temp_vd = ValueDiscount(0)
        temp_pd = PercentDiscount(0)
        for d in self.discounts:
            if isinstance(d, ValueDiscount):
                temp_vd += d
            elif isinstance(d, PercentDiscount):
                temp_pd += d

        total_price = temp_vd.calculate(total_price)
        total_price = temp_pd.calculate(total_price)

        return total_price

    def generate_report(self):
        report = "Produkty w koszyku:\n"
        for entry in self.entries:
            report += entry.generate_report()
        report += f"W sumie: {self.count_total_price():.2f}\n"
        return report

    @staticmethod
    def with_products(products_list):
        basket = Basket()
        for product in products_list:
            basket.add_product(product, 1)
        return basket
