zad 1 - typy danych

# str
# int
# float
# complex
#
# bool
# None
# ctr +  /


# zad 2 kolekcje - struktury danych
# tuple
# list
# dict
# set

# zad 3
lista = [3, 1, 2]
lista.sort()  # a nie lista.sorted()
sorted(lista)

# zad 4

slownik = {}
slownik['ala'] # dostane wyjatek bo nie ma takiego klucza

try:
    slownik['ala']
except KeyError:
    print("Brak takiego klucza")

if 'ala' in slownik:  # slownik.keys()
    print(slownik['ala'])

slownik.get('ala') # domyslnie zwracana jest wartosc None jesli klucza niema
slownik.get('ala', "brak") # brak jest domyślną wartością

# zad 5

def zlacz_teksty(a, b):
    c = a + b
    return c[::-1]