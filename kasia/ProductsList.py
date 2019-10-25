class ProductCart:
    def __init__(self):
        self.products = [
            {
                'name': 'Flour',
                'ean': 12345678,
                'weight': 1.00,
                'price': 2.50
            },
            {
                'name': 'Sugar',
                'ean': 1234533678,
                'weight': 1.00,
                'price': 3.50
            },
            {
                'name': 'Eggs',
                'ean': 2342341234,
                'weight': 0.50,
                'price': 11.00
            },
            {
                'name': 'Bread',
                'ean': 2342340234,
                'weight': 0.30,
                'price': 3.00
            },
            {
                'name': 'Milk',
                'ean': 2342394234,
                'weight': 1.00,
                'price': 2.50
            },
            {
                'name': 'Chocolate',
                'ean': 234277234,
                'weight': 0.20,
                'price': 4.00
            },
            {
                'name': 'Cola',
                'ean': 22234234,
                'weight': 1.00,
                'price': 4.50
            },
            {
                'name': 'Butter',
                'ean': 234239934,
                'weight': 0.250,
                'price': 6.50
            },
            {
                'name': 'Cheese',
                'ean': 234234200,
                'weight': 0.200,
                'price': 3.50
            },
            {
                'name': 'Avocado',
                'ean': 234777134,
                'weight': 0.200,
                'price': 5.00
            },
            {
                'name': 'Salat',
                'ean': 23444434,
                'weight': 0.100,
                'price': 3.00
            }
        ]
        self.cart = []

    def product_list(self):
        for product in self.products:
            print(product['name'])
            print(product['price'])
            print()

    def fetch_product(self, ean):
        for product in self.products:
            if ean == product['ean']:
                return product

    def add_to_cart(self, ean):
        for cart_element in self.cart:
            if cart_element['product']['ean'] == ean:
                cart_element['count'] += 1
                return

        cart_element = {
            'product': self.fetch_product(ean),
            'count': 1
        }
        self.cart.append(cart_element)

    def print_cart(self):
        cart_weight = 0
        cart_sum = 0
        for cart_element in self.cart:
            cart_sum += cart_element['count'] * cart_element['product']['price']
            cart_weight += cart_element['count'] * cart_element['product']['weight']
            print(cart_element['product']['name'])
            print(cart_element['count'])
            print(cart_element['product']['price'])
            print()
        print("Wartość Twojego koszyka: " + str(cart_sum))
        print("Waga Twojego koszyka: " + str(cart_weight))
