import pytest


def przytnij(lista, start, stop):
    wynik = []
    czy_dodawac = False
    for el in lista:
        if not czy_dodawac and start(el): # 1(1)
            czy_dodawac = True
        if czy_dodawac:
            wynik.append(el)
            if stop(el):
                break
    return wynik

# [7, 1, 8, 9]   start x > 6 stop x%9 == 0 -> [7,1,8,9]
def przytnij(lista, start, stop):
    wynik = []
    czy_dodawac = False
    for el in lista:
        if czy_dodawac or start(el):
            czy_dodawac = True
            wynik.append(el)
            if stop(el):
                break

    return wynik


def test_przytnij_zle_dane():
    rezult = przytnij([], 1, 3)
    assert rezult == []
    with pytest.raises(TypeError):
        przytnij([1], 1, 3)



def test_przytnij():
    rezult = przytnij(
        [1, 2, 3, 4, 1, 6, 7],
        start=lambda x: x == 2,
        stop=lambda x: x <= 6
    )
    assert rezult == [2]

    rezult = przytnij(
        [8, 9, 3, 1, 5, 12, 19, 21, 0],
        start=lambda x: x % 3 == 0,
        stop=lambda x: x % 4 == 0
    )
    assert rezult == [9, 3, 1, 5, 12]