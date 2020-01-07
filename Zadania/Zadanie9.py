"""
a) Napisz funkcje, która wymnozy przez siebie
elementy podane w liscie wejsciowej
pomnoz(lista)
b) podaje nieokreslona liczbe argumentow
pomnoz(1, 2)
2
pomnoz(4,5,1)
20
c) napisz funkcje ktora wybierze i zwroci z podane napisu liste liczb
x = "a1b2c1d2"
[1,2,1,2]
x = "a100v200"
[1, 0, 0, 2, 0 ,0]
d)
x = "a100v200"
[100, 200]
"""
for i in "0123456789":
    print(i.isdigit())


# ad c)
def wybierz_cyfry(napis):
    wynik = []
    for litera in napis:
        if litera.isdigit():
            wynik.append(int(litera))
    return wynik

x = "a1b2c1d2"

print(wybierz_cyfry(x))