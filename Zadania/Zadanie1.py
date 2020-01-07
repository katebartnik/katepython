"""
Napisz funkcję, która sprawdzi, czy podana liczba jest liczba pierwszą
"""
def czy_pierwsza(x):
    """Ten obszar nazywa się docstring i służy
    do tworzenia dokumentacji funkcji.
    Sprawdza czy x jest liczba pierwszą
    Przykłady użycia:
    # przykład użycia doctestów
    >>> czy_pierwsza(10)
    True
    >>> czy_pierwsza(7)
    True
    """
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

# print(help(czy_pierwsza))
# prymitywna forma testów -  bez zadnego frameworka
# assert czy_pierwsza(2) is True
# assert czy_pierwsza(11) is True
# assert czy_pierwsza(10) is False

# unittesty
# import unittest
#
# class TestCzyPierwsza(unittest.TestCase):
#
#     def test_czy_pierwsza_dla_liczby_pierwszej(self):
#         self.assertEqual(czy_pierwsza(7), True)
#         self.assertEqual(czy_pierwsza(11), True)
#         self.assertEqual(czy_pierwsza(17), True)
#
#     def test_czy_pierwsza_dla_liczby_niepierwszej(self):
#         self.assertIs(czy_pierwsza(10), False)
#         self.assertIs(czy_pierwsza(366), False)
#         self.assertIs(czy_pierwsza(21), False)


def test_czy_pierwsza_dla_liczby_pierwszej():
    assert czy_pierwsza(7) is True
    assert czy_pierwsza(11) is True
    assert czy_pierwsza(17) is True

def test_czy_pierwsza_dla_liczby_niepierwszej():
    assert czy_pierwsza(10) is False
    assert czy_pierwsza(366) is False
    assert czy_pierwsza(21) is False