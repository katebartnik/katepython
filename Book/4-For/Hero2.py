#Inwentrarz bohatera 2.0
#Demonstaracja krotek

#tworzenie krotki zawietrajacej pwene elefemty i wyświetl jej zawartość
#za pomoca petli for

inventory = ("miecz", "zbroja", "tarcza", "potion")
print("Elementy Twojego inwentrarza:")
for item in inventory:
    print(item)

input("\nAby kontynuować grę naciśnij klawisz Enter.")

#wyświetl długość krotki

print("Twój dobytek zawiera", len(inventory), "elementy(ów).")

#wyświetl jeden element wskazany przez indeks

index = int(input("\nWprowadź indeks elementu: "))
print("Pos indeksem", index, "znajduje się", inventory[index])

#Wycinanie krotek

start = int(input("\nWprowadź indeks wyznaczający początek wycinka: "))
finish = int(input("\nWprowadź indeks wyznaczający koniec wycinka: "))
print("inventory[", start, ":", finish, "] to", end= " ")
print(inventory[start:finish])

#konkatenacja dwóch krotek

chest = ("złoto", "klejnoty")
print("\nZnajdujesz skrzynię, któ©a zawiera:")
print(chest)
print("Dodajesz wartość skrzyni do swojego inwentrarza.")
inventory += chest
print("Twój aktualny inwentrarz to:")
print(inventory)
