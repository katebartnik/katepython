from produkt import Product
from baskets import Basket

class TestProduct:

    def test_initialization(self):
        pr = Product(id=10, nazwa="woda", cena=10)
        assert pr.id == 10
        assert pr.nazwa == "woda"
        assert pr.cena == 10


class TestBasket:

    def test_initialization(self):
        basket = Basket()
        assert len(basket.items) == 0

    def test_add_product(self):
        basket = Basket()
        product = Product("Woda", 10)
        basket.add_product(product, 5)
        assert len(basket.items) == 1

    def test_count_total_price(self):
        basket = Basket()
        product = Product("Woda", 10)
        basket.add_product(product, 5)
        assert basket.count_total_price() == 50

    def test_generate_report(self):
        basket = Basket()
        product = Product("Woda", 10)
        basket.add_product(product, 5)

        expected = f"""Produkty w koszyku:
 - Woda ({product.id}), cena: 10.00 x 5
W sumie: 50.00
"""
        assert basket.generate_report() == expected



