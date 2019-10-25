health = 10
trolls = 0
damage = 3

while health > 0:
    trolls += 1
    health -= damage
    print("Bohater pokonuje złego trolla, ale odnosi obrażenia", damage, "punkty zdrowia")
print("Twój bohater umiera")
