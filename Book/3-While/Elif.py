# Operatory logiczne i warunki złożone

print("\t Eksluzywna sieć Komputerów")
print("\t Tylko dla członków")

security = 0
username = ""
while not username:
    username = input("Użytkownik: ")

password = ""
while not password:
    password = input("Hasło: ")

if username == "Arturek" and password == "nic":
    print("Cześć Artur! Co masz dzisiaj na obiad?")
    security = 5
elif username == "Kasiek" and password == "nic":
    print("Hej Kasia, miło Cię widzieć")
    security = 3
else:
    print("Nieudana próba logowania")
