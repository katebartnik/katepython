"""
Zaimplementuj funkcję, zwracającą listę lat przestępnych na podstawie zadanego zakresu.
lata_przestepne(1990, 2020)
[1992, 1996, 2000, 2004, 2008, 2016, 2020]
rok przestepny jest co (4 lata, o ile nie dzieli się przez 100) albo dzieli się
przez 400
Do sprawdzenia (!!)
"""

def czy_przestepny(rok):
#    if rok%4==0 and (rok%100!=0 or rok%400==0): można i tak
    return (rok%4==0 and rok%100!=0) or (rok%4==0 and rok%400==0)


def lata_przestepne(rok_od, rok_do):
    if rok_od>rok_do: #walidacja zakresu lat
        return None

    lata = list()
    for rok in range(rok_od, rok_do+1):
        if czy_przestepny(rok):
            lata.append(rok)
    return lata

#print(lata_przestepne(2000,2030))

def test_lata_przestepne():
    assert lata_przestepne(2020, 2030) == [2020, 2024, 2028]
