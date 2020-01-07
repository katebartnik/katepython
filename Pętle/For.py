napis = "Ala ma kota!"
"i" in "ala ma kota i psa"

for znak in napis:
    znak = znak.upper()
    print(znak)

print("Wartość w znak po skończeniu pętli" , znak)

elementy = (1, 'a', 2, 'c')

for e in elementy:
    print(e)


lista = [4, 12, 11, 1]
for l in lista:
    print(l**2)

print("-"*40)
slownik = {1:"a", "Ala":"kot", "Albert": "Einstein"}

for k in slownik.keys():
    print(k)

for k in slownik:
    print(k)

for k in slownik.values():
    print(k)

for k in slownik.items():
    print(k)


zbior = {1, 2, 3, 'a'}

zbior = {40, 181, 100, "Rafał"}

i = 0
for el in zbior:
    if i == 0:
        print("Wiek", el)
    elif i == 1:
        print("Wzrost", el)
    elif i == 2:
        print("Waga", el)
    elif i == 3:
        print("Imie", el)
    i += 1

print(list(zbior))


liczby = [1, 2, 3, 6, 7, 0, 10, 20 , 30]
for liczba in liczby:
    if liczba == 0:
        break
    print(10/liczba)
else:
    print("Wykonałem się")
print("jestem po pętli")

for liczba in liczby:
    if liczba == 0:
        continue
    print(10/liczba)
else:
    print("Wykonałem się")
print("jestem po pętli")


print(range(10))
print(list(range(10)))

for i in range(10):
    print(i)
print(i)

if i:
    print(i)