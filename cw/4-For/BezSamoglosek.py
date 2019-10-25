message = input("Wprowadź komunikat: ")
new_message = ""
VOWELS = "aąeęioóuy"

print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter

      ##print nie jest potrzebny, pokazuje jak działa program

        print("Został utworzony nowy łańcuch: ", new_message)

print("Twój komunikat bez samogłosek to: ", new_message)