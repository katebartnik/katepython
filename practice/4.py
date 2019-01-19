def divisors_finder(number):
    counter = 1
    if number % 2 != 0:
        counter = 2

    x = 1
    while x <= number:
        if number % x == 0:
            print(x)
        x += counter


input_number = int(input("Podaj wartość: "))
divisors_finder(input_number)