"""
Przekazywanie listy parametrów nazwanych
"""

def fun_parametry(nr, **kwargs):
    print("nr pracownika=",nr)
    print("Imie: ",kwargs.get("imie",'-brak-'))

fun_parametry(102, imie="Jan", nazwisko="Kowalski",
              email="jk@firma.pl", wiek=44)

