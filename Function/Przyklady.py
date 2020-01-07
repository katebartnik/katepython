# definicja funkcji, procedury, zestawu instrukcji...
def nazwa_funkcji():  # ta funkcjha nie przyjmuje arg
    # to cialo funkcji
    # blok instrukcji
    print("Hello World!!")


nazwa_funkcji
# wywołanie
nazwa_funkcji()

# nazwa_funkcji("Ala ma kota")

def funkcja_z_argumentem(x):
    """
    x - argument mojej funkcji. Mogę używać go wewnątrz niej
    bedzie dostepny pod nazwa x
    """
    # return None - to jest domyślne zachowanie

def do_piatej(liczba):
    # print(liczba**5)
    return liczba**5
x = do_piatej(4)
print(x)

# napisz funkcje, ktora przyjmie napis i zwroci kopie napisu
# zamieniona na duze litery
def powieksz(text):
    return text.upper()

x = powieksz("male litery")
print(powieksz("ala ma kota"))
print(x)