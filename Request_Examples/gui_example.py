import tkinter
import math

def pierwiastkuj():
    liczba = int(pole.get())
    pierwiastek = math.sqrt(liczba)
    wynik.configure(text=pierwiastek)

root = tkinter.Tk()
label = tkinter.Label(master=root, text="Wpisz liczbe: ")
label.grid(row=1, column=1)

pole = tkinter.Entry(master=root)
pole.grid(row=1, column=2)

button = tkinter.Button(master=root, text="Przelicz", command=pierwiastkuj)
button.grid(row=2, column=1)

wynik = tkinter.Label(master=root)
wynik.grid(row=2, column=2)

root.mainloop()
print("To jest po mainloop")