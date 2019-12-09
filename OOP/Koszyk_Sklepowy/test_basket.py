from produkt import Product
from baskets import Basket

class TestProduct:

    def test_initialization(self):
        pr = Product(id=10, name="woda", price=10)
        assert pr.id == 10
        assert pr.name == "woda"
        assert pr.price == 10


class TestBasket:

    def test_initialization(self):
        basket = Basket()
        assert len(basket.entries) == 0

    def test_add_product(self):
        basket = Basket()
        product = Product("Woda", 10)
        basket.add_product(product, 5)
        assert len(basket.entries) == 1

#     def test_count_total_price(self):
#         basket = Basket()
#         product = Product("Woda", 10)
#         basket.add_product(product, 5)
#         assert basket.count_total_price() == 50
#
#     def test_generate_report(self):
#         basket = Basket()
#         product = Product("Woda", 10)
#         basket.add_product(product, 5)
#
#         expected = f"""Produkty w koszyku:
#  - Woda ({product.id}), cena: 10.00 x 5
# W sumie: 50.00
# """
#         assert basket.generate_report() == expected
    #
    # def test_with_products(self):
    #     pr1 = Product("A", 10)
    #     pr2 = Product("B", 20)
    #
    #     basket = Basket.with_products([pr1, pr2])
    #
    #     assert len(basket.entries) == 2
    #     assert basket.entries[0].quantity == 1
    #     assert basket.entries[0].product.nazwa == "A"
    #     assert basket.entries[1].quantity == 1
    #
    #
    # def test_add_discount(self):
    #     pr1 = Product("A", 10)
    #     pr2 = Product("B", 20)
    #
    #     basket = Basket.with_products([pr1, pr2])
    #     assert basket.count_total_price() == 30
    #
    #     vd1 = ValueDiscount(5)
    #     vd2 = ValueDiscount(5)
    #     pd1 = PercentDiscount(10)
    #     pd2 = PercentDiscount(10)
    #
    #     basket.add_discount(vd1)
    #     basket.add_discount(vd2)
    #     basket.add_discount(pd1)
    #     basket.add_discount(pd2)
    #
    #     assert basket.count_total_price() == 16