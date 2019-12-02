"""
Wykonanie obiektowe wprowadzanie produktów.

Potrzebujemy posiadać klasę sklep która będzie posiadać metody:
appendProduct - wprowadzanie obiektu produktu
removeById - usuwanie produktu na podstawie jego identyfiatora
resolveProductById - wyciągniecie obiektu produktu na podstawie identyfikatora
productList - zwrócenie pełnej listy produktowej

W tej klasie nie ma żadnych printów.

Klasa Product (jest to model produktu), która będzie posiadać zmienne przypisane do obiektu, a init będzie przyjmował permamentnie wymagane elementy
przez obiekt klasy
Dodatkowo metody setter(...) i getter(...) dla parametrów dodatkowych - nie wymaganych.

Parametry produktu:
- id - wymagane
- nazwa - wymagane
- cena - wymagane
- kod kreskowy
"""

from typing import *


















class Product:
    def __init__(self, identifier: int, name: str, price: float) -> None:
        self.id: int = identifier
        self.name: str = name
        self.price: float = price
        self.quantity: Optional[int] = None
        self.urlPicture: Optional[str] = None
        self.barCode: Optional[str] = None

    def getUrlPictures(self) -> Optional[str]:
        return self.urlPicture

    def setUrlPictures(self, urlPicutre: Optional[str]):
        self.urlPicture = urlPicutre

    def getBarCode(self) -> Optional[str]:
        return self.barCode

    def setBarCode(self, barCode: Optional[str]):
        self.barCode = barCode

    def getQuantity(self) -> Optional[int]:
        return self.quantity

    def setQuantity(self, quantity: Optional[int]):
        self.quantity = quantity

    def getId(self) -> int:
        return self.id

    def getName(self) -> str:
        return self.name

    def getPrice(self) -> float:
        return self.price




















class Shop:
    def __init__(self) -> None:
        self.products: Dict[Product] = []

    def appendProduct(self, productObject):
        self.products.append(productObject)

    def removeById(self, identifier):
        for productObject in self.products:
            if productObject.getId() == identifier:
                self.products.remove(productObject)

    def resolveProductById(self, identifier):
        for productObject in self.products:
            if productObject.getId() == identifier:
                return productObject

    def getProductList(self):
        return self.products













































waterProductObject = Product(1, "Water", 2.99)
breadProductObject = Product(2, "Bread", 3.99)
breadProductObject.setQuantity(20)

ourShopObject = Shop()
ourShopObject.appendProduct(waterProductObject)
ourShopObject.appendProduct(breadProductObject)
ourShopObjectProducts = ourShopObject.getProductList()


for product in ourShopObjectProducts:
    print(product.getName())
    print(product.getPrice())
    print(product.getQuantity())
    print(product.getUrlPictures())

findedProduct = ourShopObject.resolveProductById(1)
print(findedProduct.getName())