#Tworzenie wycinków łańcucha

word = "pizza"

print(
"""
    'Ściągawka' tworzenia wycinków
    
    0   1   2   3   4   5
    +---+---+---+---+---+
    | p | i | z | z | a |
    +---+---+---+---+---+
    -5  -4  -3  -2  -1  
    
"""
)

print("Wprowadź początkowy i końcowy indeks wycinka łańcuca 'pizza'.")
print("Aby zakończyć tworzenie wycinków, w odpowiedzi na monik 'Początek:' naciśnij klawisz Enter.")

start = finish = ""
while start == "" or finish == "":
    start = input("\nPoczątek: ")
    if start:
        start = int(start)

    finish = input("Koniec: ")
    if finish:
        finish = int(finish)


print("word[", start, ":", finish,"] to: ", end=" ")
print(word[start:finish])
