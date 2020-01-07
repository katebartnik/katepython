"""
Tworzenie rekordu pracownika
2 parametry obowiązkowe, 2 opcjonalne
Ma zwrócić zmienną typu słownik
"""

def utworz_pracownika(imie, nazwisko, email="info@firma.pl", telefon=None):
    pracownik = dict()
    pracownik["imie"] = imie
    pracownik["nazwisko"] = nazwisko
    pracownik["email"] = email
    pracownik["telefon"] = telefon
    return pracownik

print(utworz_pracownika("Jan","Kowalski"))
print(utworz_pracownika("Adam","Nowak", "anowak@firma.pl", "501234567"))
print(utworz_pracownika("Jan","Zieliński", telefon="601602603" ))
print(utworz_pracownika("Jan","Zieliński", email="jzielinski@firma.pl" ))
print(utworz_pracownika("Jan","Zieliński", "jzielinski@firma.pl" ))
print(utworz_pracownika("Jan","Zieliński", telefon="601602603", email="jz@firma.pl" ))