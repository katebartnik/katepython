# definicja klasy
class Pies:

    gatunek = "Canis Familiaris"
    ile = 0

    def __init__(self, imie, waga):
        self.imie = imie
        self.waga = waga
        self.incr()

    def szczekaj(self):
        print(f"{self.imie} szczeka")

    @classmethod
    def incr(cls):
        cls.ile += 1

    @staticmethod
    def tanczy():
        print("Tanczy")

# tworzę instancje klasy Pies
# jest przypisana do zmienna azor
azor = Pies("Azor", 10)
print(Pies.ile)

reks = Pies("Reksio", 85)
print(Pies.ile)
# reks.tanczy()
Pies.tanczy()
reks.szczekaj()
Pies.szczekaj(azor)
azor.szczekaj()

# print(azor == reks)
# print(azor, reks)
Pies.gatunek = "Canis Lupus"
print(azor.gatunek)
print(reks.gatunek)
print(Pies.gatunek)