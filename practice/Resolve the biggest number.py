def max_tree(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            return n1
        else:
            return n3
    else:
        if n2 > n3:
            return n2
        else:
            return n3


num1 = int(input("Podaj pierwszą liczbę "))
num2 = int(input("Podaj drugą liczbę "))
num3 = int(input("Podaj trzecią liczbę "))

print(max_tree(num1, num2, num3))