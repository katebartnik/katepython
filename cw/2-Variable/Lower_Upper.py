
name = input("Hej jak masz na imię? ")

age = input("Ile masz lat? ")
age = int(age)

weight = int(input("Ostatnie pytanie, ile kilogramów ważysz? "))

print("\nJeśli potea coś tam coś tam,\n zwróciłby się do Ciebie", name.lower())
print("Ale jeśli coś tam coś tam, nazwałby Cię", name.upper())

called = name * 5
print(called)

seconds = age * 365 * 24 * 60 * 60
print("\nŻyjesz już ponad", seconds, "sekund.")