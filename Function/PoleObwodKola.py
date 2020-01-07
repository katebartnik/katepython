"""
Napisać funkcje do obliczenia pola i obwodu koła
"""
from math import pi, sin

def oblicz_pole_kola(r):
    return pi*r**2

def oblicz_obwod_kola(r):
    return 2*pi*r

def oblicz_pole_i_obowod_kola(r):
    return oblicz_pole_kola(r), oblicz_obwod_kola(r)

print(oblicz_pole_i_obowod_kola(4))