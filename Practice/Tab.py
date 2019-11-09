def max_number_count(tab_number):
    max_number = tab_number[0]
    count = 1
    for number in tab_number:
        if number > max_number:
            max_number = number
            count = 1
        elif number == max_number:
            count += 1

    return count


a = [1, 55, 1, 5, 74, 9, 11, 74, 15, 43, 15, 20, 20]
print(max_number_count(a))



