import datetime


def till_onehundret(input_age):
    now = datetime.datetime.now()
    return now.year + 100 - input_age


input_fullname = input("Podaj swoje imię i nazwisko: ")
input_age = int(input("Podaj swój wiek: "))


print(till_onehundret(input_age))

