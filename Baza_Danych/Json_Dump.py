import json

# serializacja zmiennych do formatu JSON
pracownik = {
    "imie" : "Jan",
    "nazwisko" :"Kowalski",
    "wiek" : 42,
    "dostepy" : ['SALA01','SALA02','SALA03'],
    "wynagrodzenie" : 12345.67,
    "manager" : False,
    "auto" : None
}

# zapis (serializacja) do pliku wartości zmiennej
with open("pracownik.dat","wt") as fd:
    json.dump(pracownik, fd)