"""
Oferujemy następujace produkty
 - marchew: 2.35 PLN
 - ziemniaki: 2.2 PLN
 - cebula: 1.8 PLN
 - ogorki: 4 PLN
co chcesz kupic? marchew
ile chesz kupic [marchew]? 3
Za [marchew] płacisz 7.05 PLN
2. Dodajemy obsługę magazynu
2.1 po zakupie ilosc towaru w magazynie sie zmniejsza
2.2 jesli ktos chce kupic wiecej niz w magazynie to mowie ze nie moze
"""

def wyprintuj(slownik, jednostka):
    for k, v in slownik.items():
        print(f" - {k}: {v} {jednostka}")


towary = {
    "marchew": 2.35,
    "ziemniaki": 2.2,
    "cebula": 1.8,
    "ogorki": 4,
}

magazyn = {
    "marchew": 40,
    "ziemniaki": 40,
    "cebula": 40,
    "ogorki": 40,
}

print("""
Witaj w naszym PyZieleniaku!
Oferujemy w atrakcyjnych cenach ekoprodukty:
""")




while True:
    tryb = input("Wybierz tryb: [z-zakupowy] [m-magazynowy] [k-konczymy]")
    if tryb == "k":
        break
    elif tryb == 'z':
        while True:
            # for towar in towary:
            #     print(f" - {towar}: {towary[towar]} PLN")
            wyprintuj(towary, "PLN")
            co_kupuje = input("Jaki towar chcesz kupić [wpisz k by zakończyć]? ")
            if co_kupuje.lower() == 'k':
                break
            if co_kupuje in towary:
                ile = input(f"Ile chcesz kupić [{co_kupuje}]? ")
                ile = float(ile)
                if ile <= magazyn[co_kupuje]:
                    naleznosc = ile * towary[co_kupuje]
                    magazyn[co_kupuje] = magazyn[co_kupuje] - ile
                    # magazyn[co_kupuje] -= 1
                    print(f"Za [{co_kupuje}] płacisz: {naleznosc:.2f} PLN")
                else:
                    print("Ma za mało towaru")
            else:
                print("Nie mam takiego produktu! ")
    elif tryb=="m":
        while True:
            print("W magazynie: ")
            # for product, ilosc in magazyn.items():
            #     print(f" - {product}: {ilosc} kg")
            wyprintuj(magazyn, "kg")
            produkt_do_dodania = input("Co chcesz dodać [wpisz k by zakończyć] ? ")
            if produkt_do_dodania == 'k':
                break
            ile_do_dodania = int(input("Ile chcesz dodać? "))

            if not produkt_do_dodania in towary:
                cena_nowego_pr = float(input("Jaka będzie cena? "))
                towary[produkt_do_dodania] = cena_nowego_pr

            magazyn[produkt_do_dodania] = magazyn.get(produkt_do_dodania, 0) + ile_do_dodania