from typing import *
from Product_Class import Product

class Shop:
    def __init__(self) -> None:
        self.products: Dict[Product] = []

    def appendProduct(self, productObject):
        self.products.append(productObject)

    def removeProductById(self, identifier):
        for productObject in self.products:
            if productObject.getId() == identifier:
                self.products.remove(productObject)

    def resolveProductById(self, identifier):
        for productObject in self.products:
            if productObject.getId() == identifier:
                return productObject

    def getProductList(self):
        return self.products

    def printProductList(self):
        print('--------- Product List ---------')
        for product in self.products:
            print()
            print(product.getId())
            print(product.getName())
        print('--------- ------------ ---------')
