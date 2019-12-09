class Product:
    id_ = 0

    def __init__(self, name, price, id=None):

        if id is not None:
            self.id = id
        else:
            Product.id_ += 1
            self.id = self.id_
        self.name = name
        self.price = price

    def print_info(self):
        print(f"Produkt \"{self.name}\", id: {self.id}, cena: {self.price} PLN")


class Discount:
    def __init__(self, amount):
        self.amount = amount

    def calculate(self, basket_total_price):
        return basket_total_price - self.amount


class ValueDiscount(Discount):

    def __add__(self, other):
        return ValueDiscount(self.amount + other.amount)


class PercentDiscount(Discount):

    def calculate(self, basket_total_price):
        if self.amount:
            return basket_total_price - basket_total_price * (self.amount / 100)
        return basket_total_price

    def __add__(self, other):
        return PercentDiscount(self.amount + other.amount)


class BasketEntry:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.cena * self.quantity

    def generate_report(self):
        return f" - {self.product.name} ({self.product.id}), cena: {self.product.price:.2f} x {self.quantity}\n"
