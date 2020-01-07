# "baza danych" pacowników

import datetime
import json

# miejsce przechowujace dane na temat rekordów pracowników
dane_pracownikow = list()

try:
    with open("pracownicy.dat", "rt") as fd:
        dane_pracownikow = json.load(fd)
except:
    print("Odczyt pliku nie udał się")

def wprowadz_dane():
    print("=" * 40)
    print("Wprowadz dane pracownika")

    imie = None
    while True:
        imie = input("Podaj imie: ").upper().strip()
        if len(imie) <= 2:
            print("Podaj imię")
        else:
            break

    nazwisko = None
    while True:
        nazwisko = input("Podaj nazwisko: ").upper().strip()
        if len(nazwisko) >=3:
            break
        print("Podaj nazwisko")

    rok_urodzenia = None
    while True:
        try:
            rok_urodzenia = int(input("Podaj rok urodzenia: "))
            if rok_urodzenia<1930:
                print("Idź na emerytuę")
                continue

            rok_biezacy = datetime.datetime.now().year
            if rok_biezacy-rok_urodzenia>=15:
                break

            print("Za młodyś na pracę")
        except Exception as exc:
            print("Podaj rok urodzenia",exc)

    pensja = None
    while True:
        try:
            pensja = float(input("Podaj wartość wynagrodzenia: "))
            if (pensja>0):
                break
            print("Podaj kwote wynagrodzenia")
        except Exception as exc:
            print("Podaj kwote", exc)

    return {
        "imie" : imie, "nazwisko" : nazwisko, "rok_urodzenia" : rok_urodzenia, "pensja": pensja
    }

# pokaz zawartosci zmiennej "dane_pracownikow"
def pokaz_rekordy():
    print("========= Lista pracownikow =========")
    if len(dane_pracownikow)==0:
        print("Brak danych")
        return

    for rekord in dane_pracownikow:
        print(f"{rekord.get('imie')}\t{rekord.get('nazwisko')}\t{rekord.get('rok_urodzenia')}\t{rekord.get('pensja')}")


###### pętla główna
while True:
    operacja = input("Podaj operację [d/w/q]: ").strip().upper()
    if operacja == "Q":
        print("Koniec aplikacji")
        break

    if operacja == "W":
        # a tu bede wypisywal dane uzytkownikow
        pokaz_rekordy()

    if operacja == "D":
        # a tu bede prosil o dane pracownika
        rekord =  wprowadz_dane()
        dane_pracownikow.append(rekord)
        with open("pracownicy.dat", "wt") as fd:
            json.dump(dane_pracownikow, fd)