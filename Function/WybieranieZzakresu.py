"""
lista = [-2, 10, 0, 5, 1, 16, 9]
wybierz_z_przedzialu(lista, 5, 10)
[10, 5, 9]
"""


def wybierz_z_przedzialu(lista, a, b):
    wynik = []
    for i in lista:
        # if i >= a and i <= b:
        #     wynik.append(i)
        if isinstance(i, int) and a <= i <= b:
            wynik.append(i)

    return wynik


def test_wybierz_z_przedzialu_pusta_lista():
    assert wybierz_z_przedzialu([], 10, 20) == []


def test_wybierz_z_przedzialu():
    assert wybierz_z_przedzialu([1, 10, 11, 20, 30], 10, 20) == [10, 11, 20]
    assert wybierz_z_przedzialu([1, 10, 11, "ala", 20, 30], 10, 20) == [10, 11, 20]