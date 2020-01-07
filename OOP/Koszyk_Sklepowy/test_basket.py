from produkt import Product
from baskets import Basket

class TestBasket:

    def test_create_basket(self):
        basket = Basket()
        assert True

    def test_add_product_to_basket(self):
        basket = Basket()
        product = Product("Woda", 10)
        basket.add_product(product, 5)
        assert len(basket.items) == 1
        product2 = Product("Chleb", 2)
        basket.add_product(product2, 2)
        assert len(basket.items) == 2
        Product._NEXT_iD = 1  # sprzątanie

    def test_count_total_price(self):
        basket = Basket()
        product = Product("Woda", 10)
        basket.add_product(product, 5)
        assert basket.count_total_price() == 50
        product2 = Product("Chleb", 2)
        basket.add_product(product2, 2)
        assert basket.count_total_price() == 54
        Product._NEXT_iD = 1

    def test_generate_report(self):
        basket = Basket()
        product = Product("Woda", 10)
        basket.add_product(product, 5)
        product2 = Product("Chleb", 2)
        basket.add_product(product2, 2)
        expected = """Produkty w koszyku:
- Woda (5), cena: 10 x 5
- Chleb (6), cena: 2 x 2
W sumie: 54"""
        assert basket.generate_report() == expected
        Product._NEXT_iD = 1
