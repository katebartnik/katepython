# Rzut kośćmi / generowanie losowych liczb

import random

dice1 = random.randint(1, 6)
dice2 = random.randrange(6) + 1

total = dice1 + dice2

print("Wyrzuciłeś", dice1, "oraz", dice2, "i uzyskałeś sumę", total)
