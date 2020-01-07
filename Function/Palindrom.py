"""
Napisz funkcję która sprawdzi czy dany napis jest palindromem
czy jest taki sam czytany wstecz
is_palindrom("kajak") is True
is_palindrom("kot") is False
# pip install pytest
"""


def is_palindrom(text):
    text = text.lower()
    # text = text.lower().replace(" ", "").replace(".", "").replace(",", "")
    signs_to_remove = ". ,;!?"
    for s in signs_to_remove:
        text = text.replace(s, "")

    return text == text[::-1]
    # if text == text[::-1]:
    #     return True
    # return False


def test_is_palindrom_for_palindrom():
    assert is_palindrom("kajak") is True
    assert is_palindrom("Kajak") is True
    assert is_palindrom("A to idiota") is True
    assert is_palindrom("A to idiota.") is True
    assert is_palindrom("Ada, gmina za nim gada.") is True


def test_is_palindrom_for_no_palindrom():
    assert is_palindrom("ala ma kota") is False