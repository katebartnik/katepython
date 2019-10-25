kij = "Hej Wiktoria, jesteś supcio"
print(kij[2] + kij[8])

b = "Kocham Arturka"
print(b[2:5])

a = " Kocham Arturka "
print(a.strip())

a = "Kocham Arturka"
print(len(a))

a = "Kocham Arturka"
print(a.lower())

a = "Kocham Arturka"
print(a.upper())

a = "Kocham Arturka"
print(a.replace("o", "j"))

a = "Kocham i Arturka"
print(a.split("i"))

# 1. Zamiana w wyrazie spacji na _
# 2. Zmiana na same duże litery


def string_to_upper(string):
    return string.upper()


def string_replace_spaces_to_underscore(string):
    return string.replace(" ", "_")


print(string_to_upper("kasia"))
print(string_replace_spaces_to_underscore("huj  uyhyuyub hbjbhjh hjjbj"))