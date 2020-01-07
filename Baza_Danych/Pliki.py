#
# powtórka z obsługi plików
#

"""
fd = open("dane.txt", "rt")
for index, linia in enumerate(fd, 1):
    print("krok",index,":", linia, end='')
fd.close()
"""

with open("dane.txt", "rt") as fd:
    for index, linia in enumerate(fd, 1):
        print("krok", index, ":", linia, end='')
print("\nCzy plik zamknięty:", fd.closed)