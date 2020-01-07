# definicja
def do_potegi(podstawa, wykladnik):
    return podstawa ** wykladnik

# uzycie:

wynik = do_potegi(2, 12)
wynik2 = do_potegi(5, 5)

def unique_letters(text):
    u_letters = set(text)
    u_letters = "".join(u_letters)
    return u_letters, len(text)

dane = unique_letters("Rafał Korzeniewski")

print("litery: ", dane[0])

litery, dlugosc = unique_letters("Rafał Korzeniewski")