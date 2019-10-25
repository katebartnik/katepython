
#tworzenie pustej krotki

inventory = ()

#potraktuj krotkę jako warunek

if not inventory:
    print("Nie posiadasz niczego.")

input("\nAby kontynuować misję, naciśnij klawisz Enter.")

#utwórz krotkę zawierającą pewne elementy

inventory = ("miecz", "jhghjh", "zbroja", "tarcza", "potion")

#wyświetl krotkę
print("\nWykaz zawartości krotki:")
print(inventory)

#wyświetl każdy element krotki
print("\nElement Twojego wyposazenia:")
for item in inventory:
    print(item)

