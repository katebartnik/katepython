import math

guessNumber = 0
tryCount = 1
maxTryNumber = 1000

print("Pomyś liczbę od 1 do %s" % maxTryNumber)
guessNumber = maxTryNumber / 2
lastDifferenceNumber = guessNumber

while True:
    print("Czy to jest liczba %s?" % guessNumber)
    print("[1] - Tak, [2] - Moja liczba jest mniejsza, [3] - Moja liczba jest większa")
    userResponse = int(input(""))

    if userResponse == 1:
        break
    elif userResponse == 2:
        change = -1
    elif userResponse == 3:
        change = 1

    guessNumber = guessNumber + change * int(lastDifferenceNumber / 2)
    lastDifferenceNumber = math.ceil((lastDifferenceNumber / 2))
    tryCount += 1


print("Zgadłem Twoją liczbę po %s próbach" % tryCount)