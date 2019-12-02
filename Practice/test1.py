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
        pass

    def resolveProductById(self, identifier):
        pass

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
