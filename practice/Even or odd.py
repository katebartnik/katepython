def is_even(number):
    if number % 2 == 0:
        return True

    return False


num = int(input("Podaj liczbę "))

if is_even(num):
    print("Jest parzysta")
else:
    print("Jest nieparzysta")