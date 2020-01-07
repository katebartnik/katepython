lista = [5, 10, 0, -1, 200, -34]

print(lista)
print(sorted(lista, reverse=True))
print(lista)

print("-" * 40)

print(lista)
print(lista.sort(reverse=True))
print(lista)

print("-" * 40)
zbior = {5, 10, 0, -1, 200, -34}
print(sorted(zbior))

print("-" * 40)
slownik = {'a': 1, 'c': 2, 'b': 3}

print(sorted(slownik))

lista = [5, "d", 10, 0, -1, "b", 200, -34, "a"]
# print(sorted(lista)) # to się nie powiedzie
# bo nie ma sensu np 5 > "d"
lista = [str(x) for x in lista]
print(lista)
print(sorted(lista))
#print(sorted(lista, key=lambda x: str(x)))


lista = "10 11 5 6 201 1 101 111".split()
print(lista)
print(sorted(lista))