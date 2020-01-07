import random  # noqa:F401

# ctrl + alt + l

lista = [1, 0, 10, 'a']  # comment


def xxx(a=1, b=2):
    x = "ala ma kota ala ma kotya ala k sdfoe gfowe rog wefovg " + \
        "weor gower gowerk gowerk gowek rgowke rogk weorgkowerkg woerkg woerkgowergk owerkgowerkgwoeg"

    return a + b


for i in lista:
    try:
        print(10 / i)
    except ZeroDivisionError:
        print("Dzielisz przez zero")
    except TypeError:
        print("Dzielisz przez cos co nie jest liczba")
    # except:  # noqa
    #     pass
    finally:
        print("Wykonałem się")


# try:
#     f = open("nazwa", 'w')
#     1 / 0
# except:
#     1/0
# finally:
#     f.close()

with open("nazwa", 'w') as f:
    1/0