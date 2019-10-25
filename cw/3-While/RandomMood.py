#Komputer nastrojów
#Pokazanie elif o co chodzi

import random

print("Wyczuwam Twoją energię. Twoje prawdziwe emocje znajdują odbicie na moim ekranie.")
print("Jesteś...")

mood = random.randint(1, 4)

if mood == 1:
    # szczęśliwy
    print(":)")
elif mood == 2:
    #obojętny
    print(":/")
elif mood == 3:
    #smutny
    print(":(")
else:
    print("Nieprawidłowa wartość nastroju.")
print("...dzisiaj")
