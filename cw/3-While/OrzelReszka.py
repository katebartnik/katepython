import random

loops = 0
counterHeads = 0
counterTeils = 0

hit = int(input("Podaj ilość rzutów: "))
while loops < hit:
    x = random.randint(1, 2)
    if x == 2:
        counterHeads += 1
    else:
        counterTeils += 1

    loops += 1


print("Liczba reszek: ", counterTeils, ", Liczba Orłów: ", counterHeads)
