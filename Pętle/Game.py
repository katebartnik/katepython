import random

DEBUG = True

# Teraz wylosujemy początkowe położenia
gracz_x = random.randint(1, 10)
gracz_y = random.randint(1, 10)

skarb_x = random.randint(1, 10)
skarb_y = random.randint(1, 10)

# Obliczam odleglosc po wylosowaniu
odleglosc_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

# w zależność od wartośći zmiennej DEBUG
# printuje informacje o położeniu skarbu i gracza
if DEBUG:
    print(f"Położenie gracza (x={gracz_x}, y={gracz_y})")
    print(f"Położenie skarbu (x={skarb_x}, y={skarb_y})")
    print(f"Minimalna liczba ruchów = {odleglosc_po_wylosowaniu}")

print("""
Witaj!
Twoim zadaniem jest odnalezienie Skarbu!
Możesz się poruszać wpisując komendy:
w - góra
s - dół
a - lewo
d - prawo
Uważaj! Możesz wypaść poza planszę. 
Po każdy ruchu możesz dostać informację o tym czy się zbliżasz czy oddalasz
Zaczynamy!
""")
liczba_ruchow = 0
while True:

    # pytamy gracza o ruch
    ruch = input("Wpisz komendę (a-lewo, d-prawo, w-góra, s-dół): ")

    odleglosc_przed = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    # zmieniamy pozycję gracza - zgodnie z komendą
    if ruch == 'a':
        gracz_x = gracz_x - 1
    elif ruch == 's':
        gracz_y = gracz_y - 1
    elif ruch == 'd':
        gracz_x += 1
    elif ruch == 'w':
        gracz_y += 1
    else:
        print("Trzymaj sie reguł... $#^&*%%!!")
        continue

    if DEBUG:
        print(f"Położenie gracza po ruchu (x={gracz_x}, y={gracz_y})")
        print(f"Położenie skrbu (x={skarb_x}, y={skarb_y})")

    # po ruchu robimy sprawdzenia
    if not (1 <= gracz_x <= 10 and 1 <= gracz_y <= 10):
        print("Wypadłeś poza planszę")
        break

    odleglosc_po_ruchu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

    if odleglosc_po_ruchu == 0:
        print("Wygrałeś!!!! Brawo!!!")
        break

    if DEBUG:
        print()
        print("#"*40)
        print(f"Odl przed: {odleglosc_przed}")
        print(f"Odl po: {odleglosc_po_ruchu}")


    los = random.randint(1, 5)

    if los != 1:
        # sprawdzamy czy sie zbliżyliśmy
        if odleglosc_po_ruchu < odleglosc_przed:
            print("Ciepło")
        elif odleglosc_po_ruchu > odleglosc_przed:
            print("Zimno")
        else:
            print("Bez zmian")
            if DEBUG:
                print(f"""
To jest dziwne miejsce:
    gracz: {gracz_x} {gracz_y},
    skarb: {skarb_x} {skarb_y}
                """
                      )
    else:
        print("Pozostawię Cię w niepewności...")

    liczba_ruchow += 1  # liczba_ruchow = liczba_ruchow + 1
    if DEBUG:
        print("Liczba ruchów", liczba_ruchow)

    if liczba_ruchow > 2 * odleglosc_po_wylosowaniu:
        skarb_x = random.randint(1, 10)
        skarb_y = random.randint(1, 10)

        # Obliczam odleglosc po wylosowaniu
        odleglosc_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
        print("Jesteś Gapa! Skarb Zmienił położenie!! Hahaha!")
