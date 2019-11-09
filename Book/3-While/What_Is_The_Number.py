# ustaw wartośći początkowete

import random

the_number = random.randint(1, 50)
guess = 0
tries = 0

#pętla zgadywania
while guess != the_number:
    guess = int(input("Ta liczba to: "))
    tries += 1
    if guess > the_number:
        print("Za duża...")
    elif guess < the_number:
        print("Za mała...")
    else:
        print("Zgadłeś")
        break

    if tries >= 7:
        print("Koniec prób")
        break
