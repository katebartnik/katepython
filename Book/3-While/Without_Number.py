#Wybredny licznik - pomijający wybraną liczbę
#Demonstracja break i continue

count = 0
while True:
    count += 1
    # zakończ pętlę, jeśli wartość zmiennej count jest więcksza niż 10
    if count > 10:
        break
    # pomiń liczbę 6 i 7
    if count == 6 or count == 7:
        continue
    print(count)
