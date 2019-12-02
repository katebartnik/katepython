class Checkout:
    def get_total(self, product_list):
        total = 0
        for product in product_list:
            total += product.price
        return total

    def print_list(self, product_list, total):
        #print products with sku, price and the total
        for item in product_list:
            print(item.name + ": sku: " + item.sku + " price: " + str(item.price), end="")
        print()
        print("total: " + str(total))

checkout = Checkout()
product_list = [
    #The properties are: "name", "sku", price
    PhysicalProduct("television", "100", 100),
    PhysicalProduct("radio", "101", 80),
    PhysicalProduct("computer", "105", 1080),
]
total = checkout.get_total(product_list)
checkout.print_list(product_list, total)