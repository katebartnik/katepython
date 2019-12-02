class ProductCart:
    def __init__(self):
        pass

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
