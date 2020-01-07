"""
Funkcja anonimowe
"""

x = lambda a, b: a * b

print(x(10, 6))


def fun_sort(x):
    return x[1]


lista = [("Winogrona", 7.99), ('Jabłko', 2.99), ("Banan", 4.99)]
print(sorted(lista, key=lambda x: x[1]))

# Napisz funkcję, która z zadane listy liczb
# wybierze elementy określone przez funkcję klucza
lista = [1, 2, 3, 4, 5, 6]


# wybierz(lista, key=lambda x: x%2 == 0)
# [2, 4, 6]
# wybierz(lista, lambda x: x > 5)
# [6]
# wybierz(lista, lambda x: x>=4)
# lista2 = wybierz(lista1, lambda x: x>4)
# print(list(filter(lambda x: x % 2 == 0, lista)))

def wybierz(lista, funkcja):
    wynik = []
    for el in lista:
        if funkcja(el) is True:
            wynik.append(el)
    return wynik


print(wybierz(lista, lambda x: x % 3 == 0))


def wieksz_niz_4(x):
    return x > 4


print(wybierz(lista, wieksz_niz_4))

lista_funkcji = [print]

print(lista_funkcji)

x = "123"
ostatni_wynik = None

for i in lista_funkcji:
    ostatni_wynik = i(x)

print(ostatni_wynik)


# >>> przytnij(
# data=[11, 2, 0, 3, 4, 5, 6, 7],
# start=lambda x: x > 3,
# stop=lambda x: x == 6,
# )
# [11, 2, 0, 3, 4, 5, 6]