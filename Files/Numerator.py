import sys
print(__name__)


def ponumeruj(nazwa_pliku):
    with open(nazwa_pliku) as f:
        # i = 1
        # for line in f:
        #     print(i, line.rstrip())
        #     i += 1
        for i, line in enumerate(f, start=1):
            print(i, line.rstrip())

if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("Nie podano nazwy pliku")
        exit()

    try:
        ponumeruj(file_name)
    except FileNotFoundError:
        print("Nie ma takiego pliku!")

