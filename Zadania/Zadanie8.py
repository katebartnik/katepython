# Napisz funkcje ktora zwroci
# maximum z 3 podanych liczb
# max_of_three(10, 1, 17)
# 17
# max_of_three(1, 2, 3)
# 3
# w celu rozwiazania mozna napisac wiecej niz jedna funkcje
# Ograniczenia: funkcja nie moze zawierac wiecej niz 1 if

def max_of_two(x, y):
    if x > y:
        return x
    return y

def max_of_three(a, b, c):
    return max_of_two(max_of_two(a, b), c)

print(max_of_three(10, 20, 1))