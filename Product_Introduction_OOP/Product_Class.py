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

Zrobić przykład w nowym pliku o nazwie test.py który będzie:
 - inicjalizował sklep
 - dodawał produkty, jeden z wszystkimi danymi drugi z danymi wymaganymi (appendProduct)
 - pobierał dane produktu pierwszego na podstawie resolveProductById
 - dodawał produkt trzeci, a usuwał pierwszy (resolveProductById) - dowolne dane
 - wyświetlał listę produktów (productList)
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


