"""
Obliczanie silni
"""

# na podstawie rekurencji
# n! = n*(n-1)!
import time

def silnia_rek(n):
    if n <= 1:
        return 1
    else:
        return n*silnia_rek(n-1)

def silnia_iter(n):
    wynik = 1
    for i in range(1,n+1):
        wynik *= i
    return wynik

LICZNIK = 1000
ts1 = time.time()
for _ in range(0,LICZNIK):
    silnia_rek(800)
ts2 = time.time()
print("Czas dla rekurencji:", ts2-ts1)

ts1 = time.time()
for _ in range(0,LICZNIK):
    silnia_iter(800)
ts2 = time.time()
print("Czas dla iteracji:", ts2-ts1)